# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

中国科学技术大学学生管弦乐团（USO）社团指北，基于 Sphinx + reStructuredText 构建的文档站点，托管于 Read the Docs。

## 常用命令

```bash
# 安装依赖
pip install -r requirements.txt sphinx-autobuild

# 构建 HTML（输出到 build/html/）
make html

# 清理构建产物
make clean

# 本地热更新预览（文件修改自动重建）
sphinx-autobuild docs build/html --port 8000
```

## 文件结构

- `docs/conf.py` — Sphinx 配置（语言 zh_CN、sphinx_rtd_theme 主题）
- `docs/index.rst` — 根 toctree，定义文档的整体目录结构
- `docs/*.rst` — 主要章节（intro、begin、concert-history、qna 等）
- `docs/manual/` — 活动手册子章节（音乐会、迎新、游园会等活动的操作指南）
- `docs/_static/` — 静态资源（图片、PDF 策划案和表单）
- `.readthedocs.yaml` — RTD 部署配置（Python 3.13，Ubuntu 24.04）
