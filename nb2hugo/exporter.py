from nbconvert.exporters import MarkdownExporter
from traitlets import List
from .preprocessors import (FrontMatterPreprocessor, FixLatexPreprocessor,
                            ImagesPreprocessor, RawPreprocessor, 
                            CodeOutputPreprocessor)

class HugoExporter(MarkdownExporter):
    """Export a Jupyter notebook to a pair of markdown and resources
    compatible with Hugo.
    """
    
    preprocessors = List([
            FrontMatterPreprocessor,
            FixLatexPreprocessor,
            RawPreprocessor,
            CodeOutputPreprocessor,
            ImagesPreprocessor,
        ],
        help="""List of preprocessors, by name or namespace, to enable."""
    ).tag(config=True)