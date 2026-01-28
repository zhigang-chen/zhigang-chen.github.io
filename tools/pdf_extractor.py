#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF Content Extractor and Analyzer Tool
PDF内容提取与分析工具

This tool extracts text content from PDF files and provides various analysis functions.
本工具用于提取PDF文件中的文本内容并提供多种分析功能。

Features / 功能:
1. Extract text from PDF files / 从PDF文件提取文本
2. Keyword extraction / 关键词提取
3. Word frequency analysis / 词频分析
4. Content summarization / 内容摘要
5. Export results to various formats / 导出结果到多种格式

Usage / 使用方法:
    python pdf_extractor.py <pdf_file> [options]
    
Options / 选项:
    --extract     Extract text content / 提取文本内容
    --keywords    Extract keywords / 提取关键词
    --frequency   Analyze word frequency / 分析词频
    --summary     Generate content summary / 生成内容摘要
    --output      Output file path / 输出文件路径
    --format      Output format (txt, json, csv) / 输出格式

Author: Zhigang Chen
"""

import argparse
import json
import os
import re
import sys
from collections import Counter
from typing import Dict, List, Optional, Tuple

try:
    import pdfplumber
except ImportError:
    pdfplumber = None

try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None


class PDFExtractor:
    """PDF内容提取器类"""
    
    def __init__(self, pdf_path: str):
        """
        初始化PDF提取器
        
        Args:
            pdf_path: PDF文件路径
        """
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF文件不存在: {pdf_path}")
        
        if not pdf_path.lower().endswith('.pdf'):
            raise ValueError(f"文件不是PDF格式: {pdf_path}")
        
        self.pdf_path = pdf_path
        self.text_content = ""
        self.pages = []
        self.metadata = {}
    
    def extract_text(self, use_pdfplumber: bool = True) -> str:
        """
        提取PDF文本内容
        
        Args:
            use_pdfplumber: 是否优先使用pdfplumber库
            
        Returns:
            提取的文本内容
        """
        if use_pdfplumber and pdfplumber:
            return self._extract_with_pdfplumber()
        elif PdfReader:
            return self._extract_with_pypdf2()
        else:
            raise ImportError(
                "请安装PDF处理库: pip install pdfplumber 或 pip install PyPDF2"
            )
    
    def _extract_with_pdfplumber(self) -> str:
        """使用pdfplumber提取文本"""
        text_content = []
        
        with pdfplumber.open(self.pdf_path) as pdf:
            self.metadata = pdf.metadata or {}
            
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text() or ""
                self.pages.append({
                    'page_number': i + 1,
                    'text': page_text,
                    'width': page.width,
                    'height': page.height
                })
                text_content.append(page_text)
        
        self.text_content = "\n\n".join(text_content)
        return self.text_content
    
    def _extract_with_pypdf2(self) -> str:
        """使用PyPDF2提取文本"""
        text_content = []
        
        with open(self.pdf_path, 'rb') as file:
            reader = PdfReader(file)
            self.metadata = dict(reader.metadata) if reader.metadata else {}
            
            for i, page in enumerate(reader.pages):
                page_text = page.extract_text() or ""
                self.pages.append({
                    'page_number': i + 1,
                    'text': page_text
                })
                text_content.append(page_text)
        
        self.text_content = "\n\n".join(text_content)
        return self.text_content
    
    def get_page_count(self) -> int:
        """获取PDF页数"""
        return len(self.pages)
    
    def get_page_text(self, page_number: int) -> str:
        """
        获取指定页面的文本
        
        Args:
            page_number: 页码（从1开始）
            
        Returns:
            页面文本内容
        """
        if 1 <= page_number <= len(self.pages):
            return self.pages[page_number - 1]['text']
        raise ValueError(f"页码超出范围: {page_number}")


class ContentAnalyzer:
    """内容分析器类"""
    
    # 中文停用词列表
    CHINESE_STOPWORDS = {
        '的', '了', '和', '是', '在', '有', '这', '不', '也', '与', '对', '为',
        '以', '或', '等', '其', '中', '本', '上', '下', '可', '将', '从', '被',
        '所', '个', '到', '由', '如', '及', '于', '但', '而', '之', '则', '能',
        '就', '会', '还', '要', '把', '使', '它', '这个', '那个', '一个', '我们',
        '他们', '她们', '什么', '怎么', '如何', '可以', '通过', '进行', '使用',
        '以及', '并且', '但是', '因为', '所以', '如果', '虽然', '然而', '因此'
    }
    
    # 英文停用词列表
    ENGLISH_STOPWORDS = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
        'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
        'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that',
        'these', 'those', 'it', 'its', 'as', 'if', 'not', 'no', 'so', 'than',
        'too', 'very', 'just', 'also', 'only', 'such', 'more', 'most', 'other',
        'some', 'any', 'each', 'all', 'both', 'few', 'many', 'much', 'own',
        'same', 'about', 'into', 'over', 'after', 'before', 'between', 'under',
        'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where',
        'why', 'how', 'what', 'which', 'who', 'whom'
    }
    
    def __init__(self, text: str):
        """
        初始化内容分析器
        
        Args:
            text: 要分析的文本
        """
        self.text = text
        self.words = self._tokenize()
    
    def _tokenize(self) -> List[str]:
        """
        分词处理
        
        Returns:
            分词结果列表
        """
        # 提取中文词汇和英文单词
        # 中文使用简单的字符切分，英文使用空格切分
        chinese_pattern = r'[\u4e00-\u9fff]+'
        english_pattern = r'[a-zA-Z]+'
        
        chinese_words = re.findall(chinese_pattern, self.text)
        english_words = re.findall(english_pattern, self.text.lower())
        
        # 合并词汇列表
        all_words = chinese_words + english_words
        return all_words
    
    def word_frequency(self, top_n: int = 20, 
                       include_stopwords: bool = False) -> List[Tuple[str, int]]:
        """
        统计词频
        
        Args:
            top_n: 返回前N个高频词
            include_stopwords: 是否包含停用词
            
        Returns:
            词频列表，格式为[(词, 频次), ...]
        """
        words = self.words
        
        if not include_stopwords:
            stopwords = self.CHINESE_STOPWORDS | self.ENGLISH_STOPWORDS
            words = [w for w in words if w not in stopwords and len(w) > 1]
        
        counter = Counter(words)
        return counter.most_common(top_n)
    
    def extract_keywords(self, top_n: int = 10) -> List[str]:
        """
        提取关键词
        
        Args:
            top_n: 返回前N个关键词
            
        Returns:
            关键词列表
        """
        freq = self.word_frequency(top_n=top_n, include_stopwords=False)
        return [word for word, _ in freq]
    
    def get_summary(self, max_sentences: int = 5) -> str:
        """
        生成内容摘要（基于句子重要性）
        
        Args:
            max_sentences: 摘要包含的最大句子数
            
        Returns:
            内容摘要
        """
        # 简单的摘要方法：基于关键词出现频率选择重要句子
        sentences = re.split(r'[。！？.!?\n]+', self.text)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
        
        if not sentences:
            return ""
        
        # 获取关键词
        keywords = set(self.extract_keywords(top_n=20))
        
        # 计算每个句子的得分
        sentence_scores = []
        for sentence in sentences:
            score = sum(1 for word in self._tokenize_sentence(sentence) 
                       if word in keywords)
            sentence_scores.append((sentence, score))
        
        # 按得分排序并选取前N个句子
        sentence_scores.sort(key=lambda x: x[1], reverse=True)
        top_sentences = sentence_scores[:max_sentences]
        
        # 按原文顺序重新排列
        summary_sentences = []
        for sentence in sentences:
            for top_sent, _ in top_sentences:
                if sentence == top_sent:
                    summary_sentences.append(sentence)
                    break
            if len(summary_sentences) >= max_sentences:
                break
        
        return '。'.join(summary_sentences) + '。' if summary_sentences else ""
    
    def _tokenize_sentence(self, sentence: str) -> List[str]:
        """对单个句子进行分词"""
        chinese_pattern = r'[\u4e00-\u9fff]+'
        english_pattern = r'[a-zA-Z]+'
        
        chinese_words = re.findall(chinese_pattern, sentence)
        english_words = re.findall(english_pattern, sentence.lower())
        
        return chinese_words + english_words
    
    def get_statistics(self) -> Dict:
        """
        获取文本统计信息
        
        Returns:
            统计信息字典
        """
        char_count = len(self.text)
        word_count = len(self.words)
        chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', self.text))
        english_words = len(re.findall(r'[a-zA-Z]+', self.text))
        sentences = len(re.split(r'[。！？.!?]+', self.text))
        paragraphs = len([p for p in self.text.split('\n\n') if p.strip()])
        
        return {
            '总字符数': char_count,
            '总词数': word_count,
            '中文字符数': chinese_chars,
            '英文单词数': english_words,
            '句子数': sentences,
            '段落数': paragraphs
        }


class ResultExporter:
    """结果导出器类"""
    
    def __init__(self, output_path: Optional[str] = None):
        """
        初始化导出器
        
        Args:
            output_path: 输出文件路径
        """
        self.output_path = output_path
    
    def export_text(self, content: str, output_path: Optional[str] = None) -> str:
        """
        导出为文本文件
        
        Args:
            content: 要导出的内容
            output_path: 输出路径
            
        Returns:
            输出文件路径
        """
        path = output_path or self.output_path or 'output.txt'
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return path
    
    def export_json(self, data: Dict, output_path: Optional[str] = None) -> str:
        """
        导出为JSON文件
        
        Args:
            data: 要导出的数据
            output_path: 输出路径
            
        Returns:
            输出文件路径
        """
        path = output_path or self.output_path or 'output.json'
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return path
    
    def export_csv(self, data: List[Tuple], headers: List[str],
                   output_path: Optional[str] = None) -> str:
        """
        导出为CSV文件
        
        Args:
            data: 要导出的数据列表
            headers: 列头
            output_path: 输出路径
            
        Returns:
            输出文件路径
        """
        import csv
        
        path = output_path or self.output_path or 'output.csv'
        with open(path, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(data)
        return path


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='PDF内容提取与分析工具 / PDF Content Extractor and Analyzer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例 / Examples:
  python pdf_extractor.py document.pdf --extract
  python pdf_extractor.py document.pdf --keywords --top 10
  python pdf_extractor.py document.pdf --frequency --output result.json
  python pdf_extractor.py document.pdf --summary --sentences 5
  python pdf_extractor.py document.pdf --all --output result.json
        """
    )
    
    parser.add_argument('pdf_file', help='PDF文件路径')
    parser.add_argument('--extract', action='store_true',
                        help='提取文本内容')
    parser.add_argument('--keywords', action='store_true',
                        help='提取关键词')
    parser.add_argument('--frequency', action='store_true',
                        help='分析词频')
    parser.add_argument('--summary', action='store_true',
                        help='生成内容摘要')
    parser.add_argument('--statistics', action='store_true',
                        help='显示文本统计信息')
    parser.add_argument('--all', action='store_true',
                        help='执行所有分析')
    parser.add_argument('--top', type=int, default=20,
                        help='关键词/词频返回数量 (默认: 20)')
    parser.add_argument('--sentences', type=int, default=5,
                        help='摘要句子数量 (默认: 5)')
    parser.add_argument('--output', '-o', type=str,
                        help='输出文件路径')
    parser.add_argument('--format', '-f', type=str, 
                        choices=['txt', 'json', 'csv'],
                        default='json',
                        help='输出格式 (默认: json)')
    parser.add_argument('--page', type=int,
                        help='只处理指定页面')
    
    args = parser.parse_args()
    
    # 如果没有指定任何分析选项，默认执行全部分析
    if not any([args.extract, args.keywords, args.frequency, 
                args.summary, args.statistics, args.all]):
        args.all = True
    
    try:
        # 提取PDF内容
        print(f"正在读取PDF文件: {args.pdf_file}")
        extractor = PDFExtractor(args.pdf_file)
        text = extractor.extract_text()
        
        if args.page:
            text = extractor.get_page_text(args.page)
            print(f"已提取第 {args.page} 页内容")
        else:
            print(f"已提取 {extractor.get_page_count()} 页内容")
        
        # 分析内容
        analyzer = ContentAnalyzer(text)
        
        # 收集结果
        results = {
            'file': args.pdf_file,
            'pages': extractor.get_page_count(),
            'metadata': extractor.metadata
        }
        
        if args.extract or args.all:
            results['text'] = text
            print("\n=== 文本内容 ===")
            print(text[:500] + "..." if len(text) > 500 else text)
        
        if args.statistics or args.all:
            stats = analyzer.get_statistics()
            results['statistics'] = stats
            print("\n=== 文本统计 ===")
            for key, value in stats.items():
                print(f"  {key}: {value}")
        
        if args.keywords or args.all:
            keywords = analyzer.extract_keywords(top_n=args.top)
            results['keywords'] = keywords
            print(f"\n=== 关键词 (Top {args.top}) ===")
            print("  " + ", ".join(keywords))
        
        if args.frequency or args.all:
            frequency = analyzer.word_frequency(top_n=args.top)
            results['word_frequency'] = [{'word': w, 'count': c} 
                                         for w, c in frequency]
            print(f"\n=== 词频统计 (Top {args.top}) ===")
            for word, count in frequency:
                print(f"  {word}: {count}")
        
        if args.summary or args.all:
            summary = analyzer.get_summary(max_sentences=args.sentences)
            results['summary'] = summary
            print(f"\n=== 内容摘要 ({args.sentences}句) ===")
            print(f"  {summary}")
        
        # 导出结果
        if args.output:
            exporter = ResultExporter()
            
            if args.format == 'json':
                output_file = exporter.export_json(results, args.output)
            elif args.format == 'txt':
                text_output = f"PDF分析结果: {args.pdf_file}\n"
                text_output += "=" * 50 + "\n\n"
                if 'statistics' in results:
                    text_output += "统计信息:\n"
                    for k, v in results['statistics'].items():
                        text_output += f"  {k}: {v}\n"
                    text_output += "\n"
                if 'keywords' in results:
                    text_output += f"关键词: {', '.join(results['keywords'])}\n\n"
                if 'summary' in results:
                    text_output += f"摘要:\n{results['summary']}\n\n"
                if 'text' in results:
                    text_output += f"全文:\n{results['text']}\n"
                output_file = exporter.export_text(text_output, args.output)
            elif args.format == 'csv':
                if 'word_frequency' in results:
                    csv_data = [(item['word'], item['count']) 
                               for item in results['word_frequency']]
                    output_file = exporter.export_csv(
                        csv_data, ['词汇', '频次'], args.output
                    )
                else:
                    print("CSV格式仅支持词频数据导出")
                    output_file = None
            
            if output_file:
                print(f"\n结果已保存至: {output_file}")
        
        print("\n分析完成!")
        return 0
        
    except FileNotFoundError as e:
        print(f"错误: {e}")
        return 1
    except ValueError as e:
        print(f"错误: {e}")
        return 1
    except ImportError as e:
        print(f"依赖错误: {e}")
        return 1
    except Exception as e:
        print(f"未知错误: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
