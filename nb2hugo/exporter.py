import os.path

from nbconvert.exporters import MarkdownExporter
from traitlets import List
from traitlets import default
from .preprocessors import (FrontMatterPreprocessor, FixLatexPreprocessor,
                            ImagesPreprocessor, RawPreprocessor)

class HugoExporter(MarkdownExporter):
    """Export a Jupyter notebook to a pair of markdown and resources
    compatible with Hugo.
    """

    @property
    def template_path(self):
        r"""Extend the template_path to include this library's directory."""
        return super().template_path + [os.path.dirname(__file__)]

    @default('template_file')
    def _template_file_default(self):
        r"""Override and return the traitlet template_file."""
        return 'hugo_markdown.tpl'
    
    preprocessors = List([
            FrontMatterPreprocessor,
            FixLatexPreprocessor,
            RawPreprocessor,
            ImagesPreprocessor
        ],
        help="""List of preprocessors, by name or namespace, to enable."""
    ).tag(config=True)