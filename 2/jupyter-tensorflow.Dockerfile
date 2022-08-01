FROM public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/jupyter:v1.5.0

RUN python3 -m pip install \
tensorflow==2.5.3 \
fast-transformer==0.2.0
