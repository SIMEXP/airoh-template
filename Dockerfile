FROM jupyter/datascience-notebook

LABEL maintainer="Lune Bellec <lune.bellec@gmail.com>"

# Switch to notebook user
USER $NB_UID

# Copy project code
COPY tasks.py tasks.py
COPY invoke.yaml invoke.yaml
COPY requirements.txt requirements.txt
COPY setup.txt setup.txt

# Setup environment via user-editable script
RUN pip install -r setup.txt && \
    invoke setup
