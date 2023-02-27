<p align="center">
 <img width=200px height=200px src="./ml_readme.png" alt="Project logo">
</p>

<h3 align="center">Machine Learning: Classification using Sklearn.</h3>

<p align="center">
<img src="https://img.shields.io/github/last-commit/raferdev/classification_with_sklearn?style=for-the-badge">
<img src="https://img.shields.io/github/languages/count/raferdev/classification_with_sklearn?style=for-the-badge">
<img src="https://img.shields.io/github/license/raferdev/classification_with_sklearn?style=for-the-badge">
</p>

---

<p align="center">

This is a project divided in 4 parts to learn how use machine learning classification using Sklearn library. I made this project based on course ministred on [Alura](https://cursos.alura.com.br/).

</p>

---

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

---

## 🧐 About <a name = "about"></a>

The projects are divided on python files, the first is classificaiton_101,second ...\_102,... The complexity are encreased on each project, to run this files i made a docker file to each python file. So you can go to [Getting Started](#getting_started) below and copy the commands to run on your desktop easily.

---

## 🏁 Getting Started <a name = "getting_started"></a>

You can clone the project and start on your local host like below.

### Prerequisites

You need install **_GIT_** if you don't already have, to clone project,.

<a href="https://git-scm.com/downloads">Click here</a> or Acess:

```
https://git-scm.com/downloads
```

You need install **_Docker_** on your machine if you don't already have.

<a href="https://docs.docker.com/get-docker">Click here</a> or Acess:

```
https://docs.docker.com/get-docker/
```

And use the step-by-step doc to download and install on your specific system.

### Installing

1 - Clone on your local system

```
git clone https://github.com/raferdev/classification_with_sklearn
```

2 - Go to project path

```
cd classification_with_sklearn
```

### Start

To simplify the command i choose to use the build and run command on the same input, making a little weird, but this just create a new image and start the container.

Use on terminal:

To run the first python file, _classification_101.py_

```
docker run -it $(docker build -q .)
```

To run the _classification_102.py_.

```
docker run -it $(docker build -q . -f Dockerfile.102)
```

To run the _classification_103.py_.

```
docker run -it $(docker build -q . -f Dockerfile.103)
```

To run the _classification_104.py_.

```
docker run -it $(docker build -q . -f Dockerfile.104)
```

You will see the docker downloading the packages he need to create and start the environment and after that a log with the inputs of the classification predicties.

_Doesn't are really cool if you don't understand what are going but works!_

---

## 🎈 Usage <a name="usage"></a>

After running the docker command the terminal will go show a logs about the predicties and others details about the project. These logs are very descritive and nothing more like percentages and numbers the algoritm about was fit.

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Programming Language
- [Sklearn](https://scikit-learn.org/stable/) - Machine Learn library in Python
- [Docker](https://www.docker.com/) - Container Technology
- [Matplotlib](https://matplotlib.org/) - Data visualization library in Python
- [Seaborn](https://seaborn.pydata.org/index.html) - Based on Matplotlib and have high level interface.

---

## ✍️ Authors <a name = "authors"></a>

- [@raferdev](https://github.com/raferdev)
- [@alura](https://github.com/alura-cursos)
