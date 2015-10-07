# The README for the CellBlender Tutorials

## Overview

The CellBlender and MCell tutorials located at http://www.mcell.org/tutorials/
are generated using Sphinx (http://sphinx-doc.org/index.html) from
reStructuredText files.

Some of the binary files are not stored in the repo to keep the size of it
small, but that policy will likely change if more collaborators need to
contribute images, blend files, etc.

## Dependencies

We will be assuming that you are using Debian or Ubuntu, but most of the
instructions should be fairly similar for CentOS or other distros.

Although it's entirely possible to install all the dependencies manually at the
system level, we will be installing most of the Python libraries with
virtualenv. This will minimize possible version conflicts and simplify life
considerably.

First, you will want to install pip for Python3:

    sudo apt-get install python3-pip

Then install virtualenv:

    sudo pip3 install virtualenv

Create a new virtual environment in the cloned mcell_qrg directory:

    cd mcell_qrg
    virutalenv .

Activate it:

    source bin/activate

Install sphinx and other necessary python libraries:

    pip3 install -r requirements.txt

## Build the Tutorials

To build the html version, use this command:

    make html

The tutorials are not designed with PDF viewing in mind and currently ``make
latexpdf`` will fail.

## Viewing the Tutorials

Open ``_build/html/index.html`` from the browser of your choice.

## Learn More about Sphinx

Here are some instructions for new developers who want to contribute
to the QRG but are unfamiliar with ReST and Sphinx:

* Read this page to develop a basic understanding of ReST syntax:
  http://sphinx-doc.org/rest.html
    * The official "quick start" guide:
      http://docutils.sourceforge.net/docs/user/rst/quickstart.html
    * The official ReST reference guide:
      http://docutils.sourceforge.net/docs/user/rst/quickref.html
    * Sphinx specific syntax: http://sphinx-doc.org/markup/index.html
* Follow this tutorial, which will briefly explain how Sphinx projects work:
  http://sphinx-doc.org/tutorial.html

## Additional Notes for Contributors

  * This repository is a Sphinx project made up of various ReST files and
    Sphinx configuration files (e.g conf.py).
  * Each ReST file will create a corresponding HTML file.
  * If you add a completely new ReST file, make sure you add it to
    the table of content tree (toctree) in "index.rst"
  * Be sure to read the output from "make html". In addition to telling you if
    the build was successful, it will also give your warnings about improper
    formatting.
