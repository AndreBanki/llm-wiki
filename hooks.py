"""
hooks.py — MkDocs hook that resolves [[wikilinks]] to proper markdown links.

Supported format: [[category/filename-without-extension]]
The hook searches all docs files for a path that ends with the given suffix,
so [[ai-engineering/rag-approaches]] resolves to either
concepts/ai-engineering/rag-approaches.md or sources/ai-engineering/rag-approaches.md.

Core files (glossary, index, overview, log) can be linked as [[filename]].
"""

import os
import re

# Maps "suffix/path" (no extension) -> "full/src/path.md" (from docs root)
_file_map: dict[str, str] = {}


def on_files(files, config, **kwargs):
    global _file_map
    _file_map = {}
    for f in files:
        src = f.src_path.replace("\\", "/")
        if not src.endswith(".md"):
            continue
        path_no_ext = src[:-3]  # strip .md
        parts = path_no_ext.split("/")
        # Register every trailing suffix so both "filename" and "category/filename"
        # and "parent/category/filename" all resolve to the same file.
        for i in range(len(parts)):
            suffix = "/".join(parts[i:])
            if suffix not in _file_map:
                _file_map[suffix] = src


def on_page_markdown(markdown, page, config, files, **kwargs):
    src_path = page.file.src_path.replace("\\", "/")
    src_dir = "/".join(src_path.split("/")[:-1])  # directory of the current page

    def replace_wikilink(m: re.Match) -> str:
        target = m.group(1).strip()
        # Strip optional display text after pipe: [[target|Label]]
        if "|" in target:
            target, label = target.split("|", 1)
            target = target.strip()
            label = label.strip()
        else:
            label = target.split("/")[-1]  # use filename as display text

        target_src = _file_map.get(target)
        if target_src is None:
            # Link target not found — leave as plain text to avoid broken HTML
            return label

        # Compute a forward-slash relative path from the current page's directory
        if src_dir:
            rel = os.path.relpath(target_src, src_dir).replace("\\", "/")
        else:
            rel = target_src

        return f"[{label}]({rel})"

    return re.sub(r"\[\[([^\]]+)\]\]", replace_wikilink, markdown)
