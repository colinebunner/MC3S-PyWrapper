FROM       python:3
LABEL      maintainer="Colin Bunner"
LABEL      email="colinebunner@gmail.com"

RUN        mkdir -p /cssi-cp2k
WORKDIR    /cssi-cp2k
COPY       . /cssi-cp2k
RUN        python setup.py install
RUN        pip install -r /cssi-cp2k/cssi_cp2k.egg-info/requires.txt

CMD        ["python","/cssi-cp2k/cssi_cp2k/tests/simple-test.py"]
