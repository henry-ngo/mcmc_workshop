# Python/emcee setup instructions

## A note on environments

I highly recommend using "environments" for your coding and to create a special environment for this workshop. In particular, I recommend using Conda environments. If you are not familiar, Conda environments are basically directories that is a collection of specific versions of the software packages you are using. This is incredibly useful when working with different pieces of code that have different version requirements. I use a new environment for each project/analysis so that I don't have to worry about my old code breaking if I update a package. For example, when I switched to Python3, I kept my old Python2 setup in an environment so I can still run code that I have not yet updated to Python3 there. If you have questions about this, feel free to email me!

I recommend just following the Conda environment instructions below, but if you know what you are doing, feel free to use your own environment manager. (For example, `pyenv`)

# Step 1: Install Anaconda and conda

Anaconda is a python distribution and package manager. [conda](https://conda.io/docs/index.html) is packaged with Anaconda and it is the software that manages environments and packages. There are many other ways to run python and manage all the packages so you can choose a different method but for this tutorial I will assume you are using conda with the Anaconda. Even if you already have python installed (e.g. by default on Mac or Linux) you can still install Anaconda without issues (actually better to not touch your base python installation).

Follow the installation steps on the conda install page based on your operating system:

Windows: https://conda.io/docs/user-guide/install/windows.html

macOS: https://conda.io/docs/user-guide/install/macos.html

Linux: https://conda.io/docs/user-guide/install/linux.html

Note that the first step is to install Anaconda (since conda is packaged within Anaconda). Here, you will have the option between Python2.7 and Python3.7. If you don't know the difference, choose Python3.7. 2019 is the final year that many scientific python packages, including astronomy ones, will support Python2.7. In addition, `astropy`, a great python package (not part of this workshop though) has already dropped Python2 support. 

Also note that you do not need to do the "silent mode" install. That's for a special use case.

## If you already installed Anaconda with Python2.7 and want to "upgrade" to Python3.7

Come back later for this.

# Step 2: Create an environment for this workshop
