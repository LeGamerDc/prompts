#!/usr/bin/env python3
"""
EPUB 生成脚本

用法：
    python scripts/create_epub.py [项目根目录]

依赖：
    pip install ebooklib markdown pyyaml

功能：
    - 自动扫描 production/drafts/chapters/ 下的章节文件
    - 从 core/positioning.md 读取书名等元数据
    - 按卷号/章号排序生成 EPUB
    - 包含目录、中文排版 CSS
"""

import sys
import re
import glob
from pathlib import Path

try:
    import yaml
    import markdown
    from ebooklib import epub
except ImportError:
    print("缺少依赖，请先安装：pip install ebooklib markdown pyyaml")
    sys.exit(1)


CSS_CONTENT = """
body {
    font-family: "Noto Serif SC", "Source Han Serif CN", "Songti SC", serif;
    line-height: 1.8;
    margin: 1em;
    text-align: justify;
}
h1 { font-size: 1.6em; margin-top: 2em; margin-bottom: 0.5em; text-align: center; }
h2 { font-size: 1.3em; margin-top: 1.5em; margin-bottom: 0.4em; }
p { text-indent: 2em; margin: 0.5em 0; }
hr { border: none; border-top: 1px solid #ccc; margin: 2em 0; }
blockquote { margin: 1em 2em; color: #555; font-style: italic; }
"""


def extract_frontmatter(text: str) -> tuple[dict, str]:
    """从 markdown 文件中提取 YAML frontmatter 和正文。"""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if match:
        try:
            meta = yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError:
            meta = {}
        return meta, match.group(2)
    return {}, text


def find_chapters(project_root: Path) -> list[Path]:
    """扫描并排序章节文件。"""
    pattern = str(project_root / "production" / "drafts" / "chapters" / "**" / "*.md")
    files = glob.glob(pattern, recursive=True)
    return sorted(Path(f) for f in files)


def get_book_title(project_root: Path) -> str:
    """从 positioning.md 或目录名获取书名。"""
    positioning = project_root / "core" / "positioning.md"
    if positioning.exists():
        text = positioning.read_text(encoding="utf-8")
        for line in text.splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return project_root.name


def build_epub(project_root: Path, output_path: Path | None = None):
    """生成 EPUB 文件。"""
    chapters = find_chapters(project_root)
    if not chapters:
        print(f"未找到章节文件：{project_root / 'production/drafts/chapters/'}")
        sys.exit(1)

    title = get_book_title(project_root)
    book = epub.EpubBook()
    book.set_identifier(f"novel-craft-{project_root.name}")
    book.set_title(title)
    book.set_language("zh")
    book.add_author("AI 协作创作")

    style = epub.EpubItem(
        uid="style",
        file_name="style/default.css",
        media_type="text/css",
        content=CSS_CONTENT.encode("utf-8"),
    )
    book.add_item(style)

    md = markdown.Markdown(extensions=["extra"])
    epub_chapters = []
    toc = []
    current_volume = None

    for ch_path in chapters:
        text = ch_path.read_text(encoding="utf-8")
        meta, body = extract_frontmatter(text)

        vol = meta.get("volume", "")
        ch_num = meta.get("chapter", "")
        ch_title = meta.get("title", ch_path.stem)
        display_title = f"第{ch_num}章 {ch_title}" if ch_num else ch_title

        html_body = md.convert(body)
        md.reset()

        html_content = f"<h1>{display_title}</h1>\n{html_body}"

        epub_ch = epub.EpubHtml(
            title=display_title,
            file_name=f"chapters/{ch_path.stem}.xhtml",
            lang="zh",
        )
        epub_ch.content = html_content.encode("utf-8")
        epub_ch.add_item(style)
        book.add_item(epub_ch)
        epub_chapters.append(epub_ch)

        if vol and vol != current_volume:
            vol_title = f"第{vol}卷" if str(vol).isdigit() else str(vol)
            toc.append((epub.Section(vol_title), []))
            current_volume = vol

        if toc:
            toc[-1][1].append(epub_ch)
        else:
            toc.append(epub_ch)

    book.toc = toc
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ["nav"] + epub_chapters

    if output_path is None:
        output_path = project_root / f"{project_root.name}.epub"

    epub.write_epub(str(output_path), book)
    print(f"已生成：{output_path}")
    print(f"共 {len(epub_chapters)} 章")


def main():
    if len(sys.argv) > 1:
        project_root = Path(sys.argv[1]).resolve()
    else:
        project_root = Path.cwd()

    if not (project_root / "AGENTS.md").exists():
        print(f"错误：{project_root} 不是有效的小说项目（未找到 AGENTS.md）")
        sys.exit(1)

    output = None
    if len(sys.argv) > 2:
        output = Path(sys.argv[2]).resolve()

    build_epub(project_root, output)


if __name__ == "__main__":
    main()
