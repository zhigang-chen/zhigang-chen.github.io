# PDF内容提取与分析工具 / PDF Content Extractor and Analyzer

这是一个用于提取PDF文件内容并进行分析的Python工具。

This is a Python tool for extracting and analyzing PDF file content.

## 功能特点 / Features

1. **文本提取** / Text Extraction
   - 从PDF文件中提取全部文本内容
   - 支持分页提取
   - 支持获取PDF元数据

2. **关键词提取** / Keyword Extraction
   - 自动识别文档关键词
   - 支持中英文混合文档
   - 内置停用词过滤

3. **词频分析** / Word Frequency Analysis
   - 统计词汇出现频率
   - 可自定义返回数量
   - 支持停用词过滤

4. **内容摘要** / Content Summary
   - 基于关键词重要性生成摘要
   - 可自定义摘要长度

5. **导出功能** / Export Options
   - 支持JSON、TXT、CSV格式导出
   - 保留结构化数据

## 安装 / Installation

### 1. 安装依赖 / Install dependencies

```bash
cd tools
pip install -r requirements.txt
```

或者单独安装 / Or install separately:

```bash
pip install pdfplumber PyPDF2
```

### 2. 验证安装 / Verify installation

```bash
python pdf_extractor.py --help
```

## 使用方法 / Usage

### 基本用法 / Basic usage

```bash
# 提取全部信息（默认行为）
python pdf_extractor.py document.pdf

# 仅提取文本
python pdf_extractor.py document.pdf --extract

# 提取关键词
python pdf_extractor.py document.pdf --keywords

# 词频分析
python pdf_extractor.py document.pdf --frequency

# 生成摘要
python pdf_extractor.py document.pdf --summary

# 显示统计信息
python pdf_extractor.py document.pdf --statistics
```

### 高级选项 / Advanced options

```bash
# 自定义关键词/词频返回数量
python pdf_extractor.py document.pdf --keywords --top 30

# 自定义摘要句子数
python pdf_extractor.py document.pdf --summary --sentences 10

# 只处理特定页面
python pdf_extractor.py document.pdf --page 5

# 导出结果到JSON文件
python pdf_extractor.py document.pdf --all --output result.json

# 导出结果到TXT文件
python pdf_extractor.py document.pdf --all --output result.txt --format txt

# 导出词频到CSV文件
python pdf_extractor.py document.pdf --frequency --output freq.csv --format csv
```

### 命令行参数 / Command Line Arguments

| 参数 | 描述 / Description |
|------|---------------------|
| `pdf_file` | PDF文件路径 (必需) |
| `--extract` | 提取文本内容 |
| `--keywords` | 提取关键词 |
| `--frequency` | 分析词频 |
| `--summary` | 生成内容摘要 |
| `--statistics` | 显示文本统计信息 |
| `--all` | 执行所有分析 |
| `--top N` | 关键词/词频返回数量 (默认: 20) |
| `--sentences N` | 摘要句子数量 (默认: 5) |
| `--output, -o` | 输出文件路径 |
| `--format, -f` | 输出格式: txt, json, csv (默认: json) |
| `--page N` | 只处理指定页面 |

## 示例输出 / Example Output

```
正在读取PDF文件: sample.pdf
已提取 10 页内容

=== 文本统计 ===
  总字符数: 15234
  总词数: 2456
  中文字符数: 8000
  英文单词数: 456
  句子数: 120
  段落数: 25

=== 关键词 (Top 20) ===
  加密, 同态, 算法, 安全, 计算, 密文, 方案, homomorphic, encryption, scheme

=== 词频统计 (Top 20) ===
  加密: 45
  同态: 38
  算法: 32
  ...

=== 内容摘要 (5句) ===
  本文提出了一种新的全同态加密方案...

结果已保存至: result.json
分析完成!
```

## 作为模块使用 / Using as a Module

```python
from pdf_extractor import PDFExtractor, ContentAnalyzer

# 提取PDF内容
extractor = PDFExtractor('document.pdf')
text = extractor.extract_text()

# 分析内容
analyzer = ContentAnalyzer(text)

# 获取关键词
keywords = analyzer.extract_keywords(top_n=10)
print(f"关键词: {keywords}")

# 获取词频
frequency = analyzer.word_frequency(top_n=20)
print(f"词频: {frequency}")

# 获取摘要
summary = analyzer.get_summary(max_sentences=5)
print(f"摘要: {summary}")

# 获取统计信息
stats = analyzer.get_statistics()
print(f"统计: {stats}")
```

## 注意事项 / Notes

1. **编码问题** / Encoding
   - 工具使用UTF-8编码，支持中英文混合文档
   - 导出CSV时使用UTF-8-BOM以支持Excel正确显示中文

2. **PDF兼容性** / PDF Compatibility
   - 支持大多数标准PDF文件
   - 扫描版PDF（图片）需要OCR支持，当前版本不支持
   - 加密PDF需要先解密

3. **分词说明** / Tokenization
   - 中文使用简单字符切分，复杂场景建议安装jieba库
   - 英文使用空格切分

4. **性能** / Performance
   - 大文件处理可能需要较长时间
   - 建议对大文件使用`--page`参数分页处理

## 扩展功能 / Extensions

如需更高级的功能，可以考虑：

1. **中文分词增强**: 安装 `jieba` 库
2. **OCR支持**: 安装 `pytesseract` 和 `pdf2image`
3. **自然语言处理**: 安装 `nltk` 或 `spacy`

## 许可证 / License

MIT License

## 作者 / Author

Zhigang Chen
