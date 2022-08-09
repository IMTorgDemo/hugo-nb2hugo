import pytest
from nb2hugo.writer import HugoWriter

"""
nb2hugo ./IMTorgDemo-Notebooks/blog_test-hugo_blog.ipynb --site-dir ./Hugo_Site/ --section posts
"""


notebook = './tests/resources/blog_test-hugo_blog.ipynb'
site_dir = './tests/output'
section = 'posts'

writer = HugoWriter()




def test_exporter():
    writer.convert(notebook, site_dir, section)
    assert True == True