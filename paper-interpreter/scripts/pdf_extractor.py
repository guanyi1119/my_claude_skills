#!/usr/bin/env python3
"""
PDF文本提取脚本
用于从学术论文PDF中提取文本内容
"""

import argparse
import sys
import os

try:
    import pdfplumber
except ImportError:
    print("错误: 需要安装pdfplumber库")
    print("请运行: pip install pdfplumber")
    sys.exit(1)


def extract_text_from_pdf(pdf_path, output_path=None):
    """
    从PDF文件中提取文本

    Args:
        pdf_path: PDF文件路径
        output_path: 输出文本文件路径（可选）

    Returns:
        提取的文本内容
    """
    if not os.path.exists(pdf_path):
        print(f"错误: 文件不存在 - {pdf_path}")
        return None

    try:
        text_content = []

        with pdfplumber.open(pdf_path) as pdf:
            print(f"PDF总页数: {len(pdf.pages)}")

            for i, page in enumerate(pdf.pages):
                print(f"正在处理第 {i+1} 页...")

                # 提取页面文本
                page_text = page.extract_text()
                if page_text:
                    text_content.append(page_text)

                # 尝试提取表格（学术论文可能包含重要表格）
                tables = page.extract_tables()
                if tables:
                    text_content.append(f"\n[第{i+1}页表格]\n")
                    for table_idx, table in enumerate(tables):
                        text_content.append(f"表格 {table_idx + 1}:\n")
                        for row in table:
                            if row:
                                text_content.append(" | ".join(str(cell) if cell else "" for cell in row))
                        text_content.append("\n")

        full_text = "\n\n".join(text_content)

        # 保存到文件
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_text)
            print(f"文本已保存到: {output_path}")

        return full_text

    except Exception as e:
        print(f"提取PDF文本时出错: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description='从PDF文件中提取文本内容')
    parser.add_argument('pdf_file', help='PDF文件路径')
    parser.add_argument('-o', '--output', help='输出文本文件路径（可选）')

    args = parser.parse_args()

    if not args.output:
        # 默认输出文件名
        base_name = os.path.splitext(args.pdf_file)[0]
        args.output = f"{base_name}_extracted.txt"

    print("=" * 60)
    print("PDF文本提取工具")
    print("=" * 60)
    print(f"输入文件: {args.pdf_file}")
    print(f"输出文件: {args.output}")
    print()

    text = extract_text_from_pdf(args.pdf_file, args.output)

    if text:
        print()
        print("=" * 60)
        print("提取完成!")
        print(f"总字符数: {len(text)}")
        print("=" * 60)
        print()
        print("前500个字符预览:")
        print("-" * 60)
        print(text[:500])
        print("-" * 60)
        return 0
    else:
        print("提取失败")
        return 1


if __name__ == "__main__":
    sys.exit(main())
