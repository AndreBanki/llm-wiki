# watch-clips.ps1
# Monitors raw/clips/ for new .md files and shows a Windows notification.
# Run this in a background terminal: pwsh -NoExit -File watch-clips.ps1

$watchPath = Join-Path $PSScriptRoot "raw\clips"

$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $watchPath
$watcher.Filter = "*.md"
$watcher.NotifyFilter = [System.IO.NotifyFilters]::FileName
$watcher.EnableRaisingEvents = $true

Write-Host "Watching $watchPath for new clips..." -ForegroundColor Cyan

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

while ($true) {
    $event = $watcher.WaitForChanged([System.IO.WatcherChangeTypes]::Created, 5000)
    if (-not $event.TimedOut) {
        $filename = $event.Name
        # Ignore the ingested.md tracking file
        if ($filename -eq "ingested.md") { continue }

        Write-Host "[$(Get-Date -Format 'HH:mm:ss')] New clip detected: $filename" -ForegroundColor Green

        Show-ToastNotification `
            -Title "LLM Wiki — New Clip" `
            -Message "Ready to ingest: $filename"

        # Open VS Code focused on the workspace (if not already open)
        code "g:\Meu Drive\llm-wiki"
    }
}
