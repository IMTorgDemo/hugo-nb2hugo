FROM python:3.7


LABEL Maintainer=""


WORKDIR /home


COPY /* ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install nb2hugo


#python3 docker_run.py tests/resources/blog_test-hugo_blog.ipynb  --site-dir ./Hugo_Site_Repo/ --section posts
CMD ["bash", "-c", "nb2hugo $INPUT --site-dir $OUTPUT --section posts"]