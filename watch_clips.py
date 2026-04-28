# watch_clips.py
# Monitors raw/ (PDFs) and raw/clips/ (clips) for new files and auto-ingests via Claude Code.
# Usage: python watch_clips.py
# Requires: pip install watchdog winotify

import time
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WORKSPACE = Path(__file__).parent
RAW_DIR = WORKSPACE / "raw"
CLIPS_DIR = WORKSPACE / "raw" / "clips"


class IngestHandler(FileSystemEventHandler):
    def __init__(self, watch_ext: set, ignore_names: set = None):
        self.watch_ext = watch_ext
        self.ignore_names = ignore_names or set()
        self._recent: dict[str, float] = {}

    def on_created(self, event):
        if event.is_directory:
            return
        path = Path(event.src_path)
        if path.suffix not in self.watch_ext or path.name in self.ignore_names:
            return

        # Debounce: ignore if same file triggered within 5 seconds
        now = time.time()
        if now - self._recent.get(str(path), 0) < 5:
            return
        self._recent[str(path)] = now

        print(f"[{time.strftime('%H:%M:%S')}] New file detected: {path.name}")
        time.sleep(2)  # wait for file to finish writing
        self._notify(path.name)
        self._launch_claude()

    def _notify(self, filename: str):
        try:
            from winotify import Notification, audio
            toast = Notification(
                app_id="LLM Wiki",
                title="New File — Ingesting…",
                msg=filename,
                duration="short",
            )
            toast.set_audio(audio.Default, loop=False)
            toast.show()
        except ImportError:
            print("(winotify not installed — skipping toast)")

    def _launch_claude(self):
        subprocess.Popen(
            ["claude", "ingest the new file"],
            cwd=str(WORKSPACE),
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )


if __name__ == "__main__":
    print(f"Watching: {RAW_DIR} (PDFs) and {CLIPS_DIR} (clips)")
    observer = Observer()
    observer.schedule(IngestHandler({".pdf"}), str(RAW_DIR), recursive=False)
    observer.schedule(IngestHandler({".md"}, {"ingested.md"}), str(CLIPS_DIR), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
