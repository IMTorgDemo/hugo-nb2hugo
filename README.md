# nb2hugo

*nb2hugo* is a simple way to convert a Jupyter notebook to a Hugo markdown page.


## Motivation

Jupyter Notebook is a great way to create a single document that contains code that can be executed, formatted text to provide detailed explanations, as well as figures. Hugo is a simple yet very powerful static site generator. While a few solutions to convert a Jupyter notebook to a Hugo markdown with front matter already exist, *nb2hugo* put an emphasis on getting a result that looks similar to the original Jupyter notebook.


## Usage

In your Jupyter notebook, start by using one or more markdown cells that will contain the front matter information. Next, add an html comment as a front matter divider: everything in the notebook before the End Of Front Matter divider `<!--eofm-->` will be the front matter. This approach is similar to the one used for [content summaries](https://gohugo.io/content-management/summaries/).  
A markdown title before the `<!--eofm-->` divider will automatically become the front matter title. You can also provide other front matter fields by writting pairs of "key: value" on different lines.  
Below is an example of a notebook markdown cell that will become a front matter:

```text
# My notebook title

Date: 2018-06-01  
Author: firstname lastname  
Categories: category1, category2  
Tags: tag1, tag2, tag3  
<!--eofm-->
```

All content after the `<!--eofm-->` divider will be considered as normal notebook content.

Once you have finished writing your notebook, you can convert it using the following command:

```bash
nb2hugo notebook_file --site-dir hugo_website_directory --section content_section
```


## Run

Because of breakages between versions, this package is only used with original versions.  This includes python == 3.7, nbconvert = "==5.5.0", and other constratints.

Using docker
```
docker rmi nb2hugo
docker build -t nb2hugo .
python3 docker_run.py tests/resources/blog_test-hugo_blog.ipynb  ./ 
```

Using setup.py
```
python3 setup.py install --force
pip3 install .
```


## Development

Automated configuration and testing.

```
pipenv sync             #use Pipfile.lock for installing modules
pipenv lock -r          #display requirements.txt
pytest --collect-only
pytest
```

Manual testing with vscode 'Run and Debug'

* open `manual_run.py`
* choose 'Python: Current File (Integrated Terminal)
* run


## A workflow for easily publishing notebooks

A [demo site](https://nb2hugo.netlify.com/) shows how to combine *nb2hugo*, Hugo and Netlify to easily blog with Jupyter notebooks. 
The associated Git repository is available at <https://github.com/vlunot/nb2hugo-demo>.


## Author

**Vincent Lunot** - *Initial work*.


## License

This project is licensed under the MIT License - see the [LICENSE.txt](https://github.com/vlunot/nb2hugo/blob/master/LICENSE.txt) file for details.


## Acknowledgements

*nb2hugo* is based on [nbconvert](https://github.com/jupyter/nbconvert).
