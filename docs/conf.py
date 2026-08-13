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
    "nav_links": [
        {
            "title": "Projects",
            "children": [
                {
                    "title": "Shibuya",
                    "url": "https://shibuya.lepture.com/",
                    "summary": "A responsive, good looking with modern design documentation theme for Sphinx.",
                },
                {
                    "title": "Pygments Styles",
                    "url": "https://pygments-styles.org/",
                    "summary": "A curated collection of Pygments styles based on VS Code themes.",
                },
                {
                    "title": "Sphinx Iconify",
                    "url": "https://sphinx-iconify.lepture.com/",
                    "summary": "A sphinx extension to use <code>&lt;iconify-icon&gt;</code> web component.",
                },
                {
                    "title": "Mistune",
                    "url": "http://mistune.lepture.com/",
                    "summary": "A fast yet powerful Python Markdown parser with renderers and plugins.",
                },
                {
                    "title": "Wenmode",
                    "url": "http://wenmode.lepture.com/",
                    "summary": "A fast, composable Markdown parser and renderer toolkit.",
                },
            ],
        },
        {
            "title": "Sponsor me",
            "url": "https://github.com/sponsors/lepture",
            "external": True,
        },
    ],
}

# shibuya theme has built-in <iconify-icon>
iconify_script_url = ""

html_context = {
    "source_type": "github",
    "source_user": "lepture",
    "source_repo": "sphinx-iconify",
}
