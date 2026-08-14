# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'uso-manual'
copyright = '2025, 中国科学技术大学学生管弦乐团'
author = '中国科学技术大学学生管弦乐团'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Try to use sphinx_rtd_theme, fallback to default if not available
try:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
except ImportError:
    html_theme = 'default'

html_static_path = ['_static']
html_css_files = ['custom.css']
html_favicon = '_static/uso-icon.png'
html_logo = '_static/uso-icon.png'

# -- 自定义内联图标 role ------------------------------------------------
# 用法：正文写 :uso-icon:`x`\管弦乐团，即在「管弦乐团」前插入圆形 logo 图标并紧贴文字。
# `x` 为 role 的占位内容（被忽略）；`\` 转义后续首字，使图标与中文紧贴不换行。
from docutils import nodes


def uso_icon_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    node = nodes.image(uri='_static/uso-icon.png', alt='', classes=['inline-logo'])
    return [node], []


def setup(app):
    app.add_role('uso-icon', uso_icon_role)
