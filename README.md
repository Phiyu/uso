# USO 手册

中国科学技术大学学生管弦乐团（USTC SO）社团指北，基于 Sphinx + reStructuredText 构建的文档站点，托管于 Read the Docs。

在线文档：<https://uso-manual.readthedocs.io/>

## 构建现状

可正常构建。当前 `make html` 通过，输出到 `build/html/`。

```bash
pip install -r requirements.txt
make html          # 构建 HTML 到 build/html/
make clean         # 清理构建产物
```

本地热更新预览：

```bash
pip install sphinx-autobuild
sphinx-autobuild docs build/html --port 8000
```

## 贡献方式

1. Fork 本仓库并新建分支。
2. 编辑 `docs/` 下的 `.rst` 文件（目录结构见 `docs/index.rst`，图片放 `assets/`）。
3. 本地 `make html` 确认构建无误。
4. 提交 PR 到 `main` 分支。
