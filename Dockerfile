FROM python
ENV PYTHONBUFFERED 1 
COPY requirements.txt .
RUN apt update \
    && apt upgrade -y \
    && apt install -y apt-utils python3-ipython python3-ipdb python3-setuptools
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir /djanog
COPY django /django/
WORKDIR /django
