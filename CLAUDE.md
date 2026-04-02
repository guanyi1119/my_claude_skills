```
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.
```

## 代码库概览

这是一个包含自定义Claude技能的仓库，主要用于扩展Claude Code的功能。目前包含一个核心技能：

### paper-interpreter（论文解读技能）

**功能**：深度解读学术论文，提取主要贡献点、方法论细节、消融实验分析，支持中英文论文和PDF/文本格式。包含论文归档功能，可将论文和解读报告按标签分类保存到Excel中，支持超链接直接打开。

## 仓库结构

```
my_claude_skills/
├── skills/                      # 技能目录
│   └── paper-interpreter/       # 论文解读技能
│       ├── SKILL.md             # 主技能定义文件
│       ├── README.md            # 技能说明文档
│       ├── scripts/             # 辅助脚本
│       │   ├── pdf_extractor.py # PDF文本提取工具
│       │   └── archiver.py      # 论文归档管理脚本
│       ├── references/          # 参考资源
│       │   └── paper_analysis_template.md # 论文分析模板
│       ├── evals/               # 测试用例
│       │   └── evals.json       # 评估配置文件
│       ├── archive/             # 归档目录（运行时创建）
│       │   ├── paper_archive.xlsx
│       │   ├── pdf/
│       │   └── md/
│       └── interpretations/     # 临时解析结果目录（运行时创建）
├── .claude-plugin/              # Claude Code插件配置
├── LICENSE                      # 许可证
└── README.md                    # 仓库说明
```

## 核心技能：paper-interpreter

### 主要功能特性

- 📄 支持PDF和纯文本格式论文
- 🌐 中英文论文自动识别和处理
- 📊 结构化提取关键信息（贡献点、方法论、实验等）
- 🔬 专门分析消融实验
- 💡 自动解释专业术语
- 🎯 交互式输出，可展开的详细分析
- 📚 论文归档管理功能

### 工作流程

1. **输入处理**：确定论文形式（PDF/文本/文件路径）
2. **语言检测**：自动判断中文或英文论文
3. **结构化分析**：按模板提取并分析论文内容
4. **交互式输出**：使用可展开的details标签呈现结果
5. **归档管理**：询问是否归档，支持标签分类和Excel管理

### 关键脚本

#### pdf_extractor.py
- 用途：提取PDF文件中的文本内容
- 使用方法：`python scripts/pdf_extractor.py <pdf文件路径>`
- 依赖：pdfplumber库

#### archiver.py
- 用途：管理论文归档
- 功能：重命名文件、创建Excel归档、添加超链接
- 使用方法：`python scripts/archiver.py <base_dir> --title "论文标题" --year "2024" --affiliation "作者单位" --venue "CVPR" --keywords "关键词" --tag "标签" --reason "归档原因" --pdf <pdf路径> --md <md路径>`
- 依赖：openpyxl库

### 归档管理

- **Excel文件**：`skills/paper-interpreter/archive/paper_archive.xlsx`
- **PDF存储**：`skills/paper-interpreter/archive/pdf/`
- **解读报告**：`skills/paper-interpreter/archive/md/`

归档文件命名规则：
- PDF：`{论文标题}_{年份}.pdf`
- MD：`{论文标题}_{年份}_解读.md`

### 依赖安装

```bash
pip install pdfplumber openpyxl
```

## 开发说明

### 添加新技能

在skills目录下创建新的技能文件夹，包含以下基本文件：
- SKILL.md：技能定义和工作流程
- README.md：技能说明文档
- 必要的辅助脚本和资源文件

### 测试技能

使用evals目录下的测试用例文件（evals.json）验证技能功能。

## 许可证

仓库采用开放许可证，具体见LICENSE文件。
