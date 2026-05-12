# watch-clips.ps1
# Monitors raw/ (PDFs) and raw/clips/ (clips) for new files and auto-ingests via Claude Code.
# Run this in a background terminal: pwsh -NoExit -File watch-clips.ps1

$clipsPath = Join-Path $PSScriptRoot "raw\clips"
$rawPath   = Join-Path $PSScriptRoot "raw"

# Watcher for new clips (.md)
$watcherClips = New-Object System.IO.FileSystemWatcher
$watcherClips.Path = $clipsPath
$watcherClips.Filter = "*.md"
$watcherClips.NotifyFilter = [System.IO.NotifyFilters]::FileName
$watcherClips.EnableRaisingEvents = $true

# Watcher for new PDFs
$watcherPDF = New-Object System.IO.FileSystemWatcher
$watcherPDF.Path = $rawPath
$watcherPDF.Filter = "*.pdf"
$watcherPDF.NotifyFilter = [System.IO.NotifyFilters]::FileName
$watcherPDF.EnableRaisingEvents = $true

Register-ObjectEvent $watcherClips Created -SourceIdentifier ClipCreated | Out-Null
Register-ObjectEvent $watcherPDF   Created -SourceIdentifier PDFCreated  | Out-Null

Write-Host "Watching $clipsPath (clips) and $rawPath (PDFs)..." -ForegroundColor Cyan

function Show-ToastNotification {
    param([string]$Title, [string]$Message)
    [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
    [Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime] | Out-Null

    $template = @"
<toast>
  <visual>
    <binding template="ToastGeneric">
      <text>$Title</text>
      <text>$Message</text>
    </binding>
  </visual>
</toast>
"@
    $xml = New-Object Windows.Data.Xml.Dom.XmlDocument
    $xml.LoadXml($template)
    $toast = [Windows.UI.Notifications.ToastNotification]::new($xml)
    [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("LLM Wiki").Show($toast)
}

try {
    while ($true) {
        $ev = Wait-Event -SourceIdentifier ClipCreated, PDFCreated -Timeout 5
        if ($null -eq $ev) { continue }

        $filename = $ev.SourceEventArgs.Name
        Remove-Event -EventIdentifier $ev.EventIdentifier

        Write-Host "[$(Get-Date -Format 'HH:mm:ss')] New file detected: $filename" -ForegroundColor Green

        Show-ToastNotification -Title "LLM Wiki — Ingesting…" -Message $filename

        Start-Sleep -Seconds 2  # wait for file to finish writing
        if ($ev.SourceIdentifier -eq "ClipCreated") {
          $prompt = "ingest clip file '$filename' from raw/clips; after the ingest is complete, move the original file to raw/ and keep raw/clips only as an inbox"
        } else {
          $prompt = "ingest the new file"
        }

        Start-Process -FilePath "claude" -ArgumentList ('"' + $prompt + '"') -WorkingDirectory $PSScriptRoot
    }
} finally {
    Unregister-Event -SourceIdentifier ClipCreated -ErrorAction SilentlyContinue
    Unregister-Event -SourceIdentifier PDFCreated  -ErrorAction SilentlyContinue
    $watcherClips.Dispose()
    $watcherPDF.Dispose()
}
