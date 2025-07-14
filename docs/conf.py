# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Sphinx Iconify"
copyright = "2025, Hsiaoming Yang"
author = "Hsiaoming Yang"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_design",
    "sphinx_iconify",
]

templates_path = ["_templates"]
html_static_path = ["_static"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "shibuya"

html_favicon = "_static/favicon.svg"

html_theme_options = {
    "page_layout": "simple",
    "light_logo": "_static/logo.svg",
    "dark_logo": "_static/logo.svg",
    "accent_color": "indigo",
    "twitter_creator": "lepture",
    "twitter_site": "lepture",
    "twitter_url": "https://twitter.com/lepture",
    "github_url": "https://github.com/lepture/sphinx-iconify",
}

# shibuya theme has built-in <iconify-icon>
iconify_script_url = ""
