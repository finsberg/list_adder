# A simple example of how to set up a good workflow on GitHub

Have look at notebook in this repository for more information.

## Install

Make sure you what `virtualenv` installed

```
[sudo] python -m pip install virtualenv
```

Create a virtual enviroment

```
python -m virtualenv venv
```

Activate the virtual environment

```
source venv/bin/activate
```

Install the code in your newly created virtual environment

```
python -m pip install .
```

Note that if you plan to change the code that you install, then you should install the code in editable mode

```
python -m pip install -e .
```

This allows you to edit the code without having to install it again every time you want to try out your new changes.
