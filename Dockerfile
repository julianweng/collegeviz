ARG BASE_CONTAINER=jupyter/base-notebook:python-3.8.6
FROM $BASE_CONTAINER
LABEL author="Julian Weng"
USER root
RUN pip3 install matplotlib==3.4.2 pandas==1.3.1 streamlit==0.85.1 plotly==5.1.0 seaborn==0.11.1
USER $NB_UID