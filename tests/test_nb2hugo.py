import pytest
from nb2hugo.writer import HugoWriter

"""
nb2hugo ./IMTorgDemo-Notebooks/blog_test-hugo_blog.ipynb --site-dir ./Hugo_Site/ --section posts
"""


notebook = './tests/resources/blog_test-hugo_blog.json'
site_dir = './tests/output'
section = 'posts'

writer = HugoWriter()
writer.convert(notebook, site_dir, section)


"""
def test_exporter(tmpdir):
    exporter = HugoExporter()
    with pytest.warns(UserWarning, match='should be ignored.$'):
        markdown, resources = exporter.from_notebook_node(notebook)
    assert markdown == expected_markdown
"""