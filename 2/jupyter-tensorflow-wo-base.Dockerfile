FROM ubuntu:22.04

RUN apt-get update &amp;&amp; apt-get install -y \
python3 \
python3-pip

RUN python3 -m pip --no-cache-dir install --upgrade \
"pip&lt;20.3" \
setuptools

RUN python3 -m pip install --no-cache-dir \
jupyter \
tensorflow==2.5.3 \
fast-transformer==0.2.0

RUN apt-get install -y --no-install-recommends \
git \
libgl1-mesa-glx

EXPOSE 8888

ENV NB_PREFIX /

CMD ["bash","-c", "jupyter notebook --notebook-dir=/home/jovyan --ip=0.0.0.0 --no-browser --allow-root --port=8888 --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.allow_origin='*' --NotebookApp.base_url=${NB_PREFIX}"]
