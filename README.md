# Airoh Template: Reproducible Pipelines Made Simple

\_why don't you have a cup of relaxing jasmin tea?\_

This repository provides a minimal, modular, and **fully reproducible** template for scientific workflows. Built on the [`invoke`](https://www.pyinvoke.org/) task runner and containerization (Docker or Apptainer), it lets you go from clean clone to output figures with just a few commands.

The logic is powered by [`airoh`](https://pypi.org/project/airoh/), a lightweight, pip-installable Python package of reusable `invoke` tasks.

> 🧠 **Background**: This repository reproduces the figures used in the editorial [Craddock et al., 2018](https://doi.org/10.1016/j.neuroimage.2017.11.063) to demonstrate how the `airoh-template` works. The original analysis grouped papers from a 2017 special issue on brain parcellation and segmentation using a data-driven categorization of abstract terms. This template shows how to reproduce that analysis using Jupyter notebooks and reusable infrastructure. It should be easy to adapt to a variety of other projects.

---

## 🚀 Quick Start

### 1⃣ Install `invoke` and clone core airoh dependencies

```
bash
pip install -r setup.txt
```

---

### 2⃣ Fetch the source data

```
bash
invoke fetch
```

This uses Datalad under the hood to retrieve the configured file(s) listed in `invoke.yaml`.

---

### 3⃣ Run the analysis pipeline

```
bash
invoke run
```

This will:

* create the output folder if missing
* run all notebooks found in the figure directory
* skip any that already have outputs

---

### 4⃣ Build and archive a Docker image (optional)

If you want to freeze the environment:

```
bash
invoke docker-build
invoke docker-archive
```

This will save your image to a `.tar.gz` archive that can later be loaded with `docker-setup`, e.g.:

```
bash
invoke docker-setup --url https://some/zenodo/archive.tar.gz
```

---

### 5⃣ Run inside container (optional)

Once built or loaded:

```
bash
invoke docker-run --task run
```

This re-runs your pipeline inside the container.

---

### 6⃣ Clean output data

```
bash
invoke clean
```

Removes the output folder listed in `invoke.yaml` under `output_data_dir`.

---

## 🧠 Core Features

* Modular `tasks.py` that imports reusable code from `airoh`
* Minimal and readable `invoke.yaml` configuration file
* Optional containerization for full reproducibility
* Real output notebooks & figures — ready to publish

---

## 🧰 Task Overview

```
| Task             | Description                                                    |
| ---------------- | -------------------------------------------------------------- |
| `setup`          | Installs Python dependencies from `requirements.txt`           |
| `fetch`          | Downloads dataset using Datalad and config in `invoke.yaml`    |
| `run`            | Executes Jupyter notebooks for each figure                     |
| `clean`          | Removes the `output_data_dir` contents                         |
| `docker-build`   | Builds a Docker image from the current repo                    |
| `docker-archive` | Archives the Docker image into a `.tar.gz` for sharing         |
| `docker-setup`   | Loads a prebuilt image from a `.tar.gz` archive (e.g., Zenodo) |
| `docker-run`     | Runs any task inside the Docker image                          |
```

Use `invoke --list` or `invoke --help <task>` for descriptions and usage.

---

## 🧭 Tips

* Use `invoke --complete` for tab-completion support
* Configure paths and data sources in `invoke.yaml`
* To use this template for a new project, start from [`airoh-template`](https://github.com/SIMEXP/airoh-template) and customize `tasks.py` + `invoke.yaml`

---

## 📁 Folder Structure

```
| Folder         | Description                              |
| -------------- | ---------------------------------------- |
| `notebooks/`   | Jupyter notebooks (e.g., one per figure) |
| `source_data/` | Raw source datasets                      |
| `output_data/` | Generated results and figures            |
| `tasks.py`     | Project-specific invoke entrypoint       |
| `invoke.yaml`  | Config file for all reusable tasks       |
```

---

## 🧪 Want to use containers?

```
- Build: invoke docker-build
- Archive: invoke docker-archive
- Run: invoke docker-run --task run
- Setup from archive: invoke docker-setup --url <zenodo_url>
```

---

## 🔁 Want to contribute?

Submit an issue or PR on [`airoh`](https://github.com/SIMEXP/airoh).

---

## Philosophy

Inspired by Uncle Iroh from *Avatar: The Last Airbender*, `airoh` aims to bring simplicity, reusability, and clarity to research infrastructure — one well-structured task at a time. It is meant to support a concrete implementation of the [YODA principles](https://handbook.datalad.org/en/latest/basics/101-127-yoda.html).

