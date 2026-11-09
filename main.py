#!/usr/bin/env python3
"""テキストファイルの統計情報を表示するツール"""

import sys
import re
from collections import Counter

# 日本語の単語も拾えるように、英数字と日本語の連続を単語とする
WORD_PATTERN = re.compile(r"[A-Za-z0-9]+|[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]+")

def analyze(path):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"エラー: ファイルが見つかりません: {path}")
        return
    except UnicodeDecodeError:
        print(f"エラー: UTF-8 として読めません: {path}")
        return

    lines = text.splitlines()
    line_count = len(lines)
    words = WORD_PATTERN.findall(text)
    word_count = len(words)
    char_count = len(text)
    char_count_no_space = len(re.sub(r"\s", "", text))

    print(f"ファイル: {path}")
    print(f"行数:  {line_count}")
    print(f"単語数:  {word_count}")
    print(f"文字数:  {char_count}（空白除く: {char_count_no_space}）")
    print()

    if words:
        counter = Counter(w.lower() for w in words)
        top = counter.most_common(10)
        print("頻出単語トップ10:")
        for rank, (word, count) in enumerate(top, 1):
            bar = "#" * min(count, 40)
            print(f"  {rank:>2}. {word:<20} {count:>5} 回  {bar}")
    else:
        print("単語が見つかりませんでした")

def main():
    if len(sys.argv) < 2:
        print("使い方: python main.py <テキストファイル> [ファイル2 ...]")
        print("  例:   python main.py sample.txt")
        sys.exit(0)

    for i, path in enumerate(sys.argv[1:]):
        if i > 0:
            print()
            print("=" * 50)
            print()
        analyze(path)

if __name__ == "__main__":
    main()
