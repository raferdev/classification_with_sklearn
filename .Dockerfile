FROM jupyter/datascience-notebook 

RUN pymp

COPY . .
