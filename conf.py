from datetime import date
import os

from pygments import formatters
from sphinx import highlighting

# General configuration
# ---------------------

exclude_patterns = ["README.rst"]

# ELIMINAR sphinx_gallery de las extensiones
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.imgmath",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx_copybutton",
]

copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_copy_empty_lines = False

doctest_test_doctest_blocks = "true"

# ELIMINAR completamente sphinx_gallery_conf
# sphinx_gallery_conf = {
#     "examples_dirs": [
#         "intro/scipy/summary-exercises/examples",
#     ],
#     "gallery_dirs": [
#         "intro/scipy/summary-exercises/auto_examples",
#     ],
#     "doc_module": "sistemas-operativos-apuntes",
#     "backreferences_dir": "tmp",
#     "plot_gallery": "0",
# }

templates_path = ["_templates"]
source_suffix = ".rst"

project = "Sistemas Operativos - apuntes"
copyright = f"{date.today().year}"
release = "2025.1rc0.dev0"
version = release

language = "es"
pygments_style = "sphinx"

class MyHtmlFormatter(formatters.HtmlFormatter):
    def __init__(self, **options):
        options["lineseparator"] = '\n<div class="newline"></div>'
        formatters.HtmlFormatter.__init__(self, **options)

highlighting.PygmentsBridge.html_formatter = MyHtmlFormatter

rst_epilog = """

.. |clear-floats| raw:: html

    <div style="clear: both"></div>

|clear-floats|

"""

html_theme = "mart"
html_theme_path = ["themes"]

html_theme_options = {
    'nosidebar': 'true',
    "footerbgcolor": "#000000",
    "relbarbgcolor": "#000000",
}

html_title = "Sistemas Operativos - apuntes"
html_static_path = ["themes/mart/static"]
html_css_files = [
    'nature.css',
]
html_use_index = False
htmlhelp_basename = "mart"

epub_theme = "epub"
epub_theme_options = {"relbar1": False, "footer": False}
epub_show_urls = "no"
epub_tocdup = False

latex_show_pagerefs = False

latex_documents = [
    (
        "intro/index",
        "mart.tex",
        r"Sistemas Operativos - Apuntes",
        r"Sistemas Operativos",
        "manual",
    ),
]

latex_logo = "images/cover.pdf"
latex_toplevel_sectioning = "part"
latex_domain_indices = False

preamble = r"""
\definecolor{VerbatimColor}{rgb}{0.961, .98, 1.}
\definecolor{VerbatimBorderColor}{rgb}{0.6,0.6,0.6}
\usepackage{graphics}
\usepackage[final]{pdfpages}
\setcounter{tocdepth}{1}
\usepackage{amssymb}
\usepackage{pifont}
\usepackage{multicol}
"""

latex_elements = {
    "papersize": "a4paper",
    "preamble": preamble,
    "fontpkg": "\\usepackage{lmodern}",
    "fncychap": r"""%
        \usepackage[Sonny]{fncychap}%
        \ChRuleWidth{1.5pt}%
        \ChNumVar{\fontsize{76}{80}\sffamily\slshape}
        \ChTitleVar{\raggedleft\Huge\sffamily\bfseries}
    """,
    "classoptions": ",oneside,openany",
    "babel": r"\usepackage[english]{babel}",
    "releasename": "Edición",
    "sphinxsetup": "warningBgColor={RGB}{255,204,204}",
}

_python_doc_base = "https://docs.python.org/3/"

intersphinx_mapping = {
    "python": (_python_doc_base, None),
}

extlinks = {
    "simple": (_python_doc_base + "/reference/simple_stmts.html#%s", "%s"),
    "compound": (_python_doc_base + "/reference/compound_stmts.html#%s", "%s"),
}

imgmath_use_preview = True

def add_per_page_js(app, pagename, templatename, context, doctree):
    if pagename.split("/")[-1] == "index":
        app.add_js_file("foldable_toc.js")
        app.add_css_file("foldable_toc.css")

def setup(app):
    app.add_js_file("https://code.jquery.com/jquery-3.7.0.min.js")
    app.add_js_file("scroll_highlight_toc.js")
    app.connect("html-page-context", add_per_page_js)

domain = os.getenv("DOMAIN", "lectures.scientific-python.org")
html_context = {"domain": domain}
print(f"Building for domain: {domain}")