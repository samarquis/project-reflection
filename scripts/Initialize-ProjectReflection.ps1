[CmdletBinding()]
param(
    [Parameter(Mandatory = $false)]
    [string]$RepositoryPath = (Get-Location).Path,

    [Parameter(Mandatory = $false)]
    [string]$VaultProjectsPath = $env:PROJECT_REFLECTION_VAULT,

    [Parameter(Mandatory = $false)]
    [string]$ProjectName
)

$ErrorActionPreference = 'Stop'

if (-not $VaultProjectsPath) {
    throw 'Provide -VaultProjectsPath or set PROJECT_REFLECTION_VAULT.'
}

$repository = (Resolve-Path -LiteralPath $RepositoryPath).Path
if (-not (Test-Path -LiteralPath $repository -PathType Container)) {
    throw "Repository path is not a directory: $repository"
}

if (-not $ProjectName) {
    $ProjectName = Split-Path -Leaf $repository
}

$invalidChars = [IO.Path]::GetInvalidFileNameChars()
$safeName = -join ($ProjectName.ToCharArray() | ForEach-Object {
    if ($invalidChars -contains $_) { '-' } else { $_ }
})
$safeName = $safeName.Trim().TrimEnd('.')
if (-not $safeName) {
    throw 'Project name is empty after removing invalid filename characters.'
}

New-Item -ItemType Directory -Path $VaultProjectsPath -Force | Out-Null
$projectDirectory = Join-Path $VaultProjectsPath $safeName
$reflectionsDirectory = Join-Path $projectDirectory 'Reflections'
$ticketEventsDirectory = Join-Path $projectDirectory 'Ticket Events'
$workEventsDirectory = Join-Path $projectDirectory 'Work Events'
$selfReviewsDirectory = Join-Path $projectDirectory 'Self Reviews'
New-Item -ItemType Directory -Path $reflectionsDirectory -Force | Out-Null
New-Item -ItemType Directory -Path $ticketEventsDirectory -Force | Out-Null
New-Item -ItemType Directory -Path $workEventsDirectory -Force | Out-Null
New-Item -ItemType Directory -Path $selfReviewsDirectory -Force | Out-Null

$memoryPath = Join-Path $projectDirectory 'Project Memory.md'
$created = $false
$updatedSchema = $false
if (-not (Test-Path -LiteralPath $memoryPath)) {
    $initialized = (Get-Date).ToString('o')
    $safeNameYaml = $safeName.Replace("'", "''")
    $repositoryYaml = $repository.Replace("'", "''")
    $memory = @"
---
project: '$safeNameYaml'
repository: '$repositoryYaml'
reflection_window_days: 30
initialized: "$initialized"
last_reflection:
---

# $safeName Project Memory

This record accumulates evidence-backed lessons. Full reports live in [[Reflections]].

<!-- project-reflection:current-state:start -->
## Current state

Not reviewed yet.
<!-- project-reflection:current-state:end -->

<!-- project-reflection:wins:start -->
## Durable wins and proven practices

None recorded yet.
<!-- project-reflection:wins:end -->

<!-- project-reflection:friction:start -->
## Durable failure patterns and friction

None recorded yet.
<!-- project-reflection:friction:end -->

<!-- project-reflection:decisions:start -->
## Decisions and constraints still in force

None recorded yet.
<!-- project-reflection:decisions:end -->

<!-- project-reflection:risks:start -->
## Unresolved risks and next experiments

None recorded yet.
<!-- project-reflection:risks:end -->

<!-- project-reflection:index:start -->
## Reflection history

No reflections yet.
<!-- project-reflection:index:end -->

<!-- project-reflection:tickets:start -->
## Ticket learning log

No ticket events yet.
<!-- project-reflection:tickets:end -->

<!-- project-reflection:work-events:start -->
## Work event history

No work events yet.
<!-- project-reflection:work-events:end -->

<!-- project-reflection:lessons:start -->
## Lesson registry

| ID | Status | Lesson | Evidence | Canonical owner | Revisit when |
|---|---|---|---|---|---|
| - | - | No lessons recorded yet. | - | - | - |
<!-- project-reflection:lessons:end -->

<!-- project-reflection:effectiveness:start -->
## Lesson effectiveness

| ID | Applied | Successful | Failed | Unknown | Last applied | Last validated | Evidence |
|---|---:|---:|---:|---:|---|---|---|
| - | 0 | 0 | 0 | 0 | - | - | No applications recorded yet. |
<!-- project-reflection:effectiveness:end -->

<!-- project-reflection:self-reviews:start -->
## Project Reflection self-review history

No self-reviews yet.
<!-- project-reflection:self-reviews:end -->
"@
    Set-Content -LiteralPath $memoryPath -Value $memory -Encoding utf8NoBOM
    $created = $true
}

$lessonMarker = '<!-- project-reflection:lessons:start -->'
$existingMemory = Get-Content -LiteralPath $memoryPath -Raw
if (-not $existingMemory.Contains($lessonMarker)) {
    $lessonRegistry = @"

<!-- project-reflection:lessons:start -->
## Lesson registry

| ID | Status | Lesson | Evidence | Canonical owner | Revisit when |
|---|---|---|---|---|---|
| - | - | No lessons recorded yet. | - | - | - |
<!-- project-reflection:lessons:end -->
"@
    [IO.File]::AppendAllText(
        $memoryPath,
        [Environment]::NewLine + $lessonRegistry + [Environment]::NewLine,
        [Text.UTF8Encoding]::new($false)
    )
    $updatedSchema = $true
}

$managedSections = @(
    @{
        Marker = '<!-- project-reflection:work-events:start -->'
        Content = @"

<!-- project-reflection:work-events:start -->
## Work event history

No work events yet.
<!-- project-reflection:work-events:end -->
"@
    },
    @{
        Marker = '<!-- project-reflection:effectiveness:start -->'
        Content = @"

<!-- project-reflection:effectiveness:start -->
## Lesson effectiveness

| ID | Applied | Successful | Failed | Unknown | Last applied | Last validated | Evidence |
|---|---:|---:|---:|---:|---|---|---|
| - | 0 | 0 | 0 | 0 | - | - | No applications recorded yet. |
<!-- project-reflection:effectiveness:end -->
"@
    },
    @{
        Marker = '<!-- project-reflection:self-reviews:start -->'
        Content = @"

<!-- project-reflection:self-reviews:start -->
## Project Reflection self-review history

No self-reviews yet.
<!-- project-reflection:self-reviews:end -->
"@
    }
)

foreach ($section in $managedSections) {
    $existingMemory = Get-Content -LiteralPath $memoryPath -Raw
    if (-not $existingMemory.Contains($section.Marker)) {
        [IO.File]::AppendAllText(
            $memoryPath,
            [Environment]::NewLine + $section.Content + [Environment]::NewLine,
            [Text.UTF8Encoding]::new($false)
        )
        $updatedSchema = $true
    }
}

[pscustomobject]@{
    Project = $safeName
    Repository = $repository
    ProjectDirectory = $projectDirectory
    MemoryPath = $memoryPath
    ReflectionsDirectory = $reflectionsDirectory
    TicketEventsDirectory = $ticketEventsDirectory
    WorkEventsDirectory = $workEventsDirectory
    SelfReviewsDirectory = $selfReviewsDirectory
    Created = $created
    UpdatedSchema = $updatedSchema
} | ConvertTo-Json
