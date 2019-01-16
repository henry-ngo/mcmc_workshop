# Python/emcee setup instructions

## A note on environments

I highly recommend using "environments" for your coding and to create a special environment for this workshop. In particular, I recommend using Conda environments. If you are not familiar, Conda environments are basically directories that is a collection of specific versions of the software packages you are using. This is incredibly useful when working with different pieces of code that have different version requirements. I use a new environment for each project/analysis so that I don't have to worry about my old code breaking if I update a package. For example, when I switched to Python3, I kept my old Python2 setup in an environment so I can still run code that I have not yet updated to Python3 there. If you have questions about this, feel free to email me!

I recommend just following the Conda environment instructions below, but if you know what you are doing, feel free to use your own environment manager. (For example, `pyenv`)

# Step 1: Install Anaconda and conda

Anaconda is a python distribution and package manager. It is also super useful for scientists since it also inlcudes all of the main scientific python packages (SciPy, Numpy etc.). [conda](https://conda.io/docs/index.html) is also packaged with Anaconda and it is the software that manages environments and packages. 

There are many other ways to run python and manage all the packages (e.g. Canopy) so you can choose a different method but for this tutorial I will assume you are using conda with Anaconda. Even if you already have python installed (e.g. by default on Mac or Linux) you can still install Anaconda without issues (actually better to not touch your base python installation).

Follow the installation steps on the conda install page based on your operating system:

Windows: https://conda.io/docs/user-guide/install/windows.html

macOS: https://conda.io/docs/user-guide/install/macos.html

Linux: https://conda.io/docs/user-guide/install/linux.html

Note that the first step is to install Anaconda (since conda is packaged within Anaconda). Here, you will have the option between Python2.7 and Python3.7. If you don't know the difference, choose Python3.7. 2019 is the final year that many scientific python packages, including astronomy ones, will support Python2.7. In addition, `astropy`, a great python package (not part of this workshop though) has already dropped Python2 support. See the end of this page for a bonus note on switching from Python2 to Python3.

Also note that you do not need to do the "silent mode" install. That's for a special use case.

**If you already installed Anaconda with Python2.7, it's not a problem. Python, it turns out, is just another package that conda can manage, so you will just have to specify Python3.7 when creating your new environment for this workshop and Python3.7 will be installed for the environment. See below.**

# Step 2: Create an environment for this workshop

Here is the conda environment help page in case you get stuck: https://conda.io/docs/user-guide/tasks/manage-environments.html

First, let's create a brand new environment for this workshop. At your terminal/command prompt, type
```
conda create --name emcee_workshop python=3.7
```
Say yes to the prompts. This will create a new environment named `emcee_workshop` using Python3.7. You can name it whatever you want, just replace `emcee_workshop` in the following lines with your name. Remember that this is a directory, and it has a location on your hard disk---within the `anaconda` installation directory (for me, it's `$HOME/anaconda`) there is now a new directory named `emcee_workshop/`.

Next, switch your environment to your new `emcee_workshop` environment. On macOS or Linux, open the Terminal and type:
```
source activate emcee_workshop
```
On Windows, open the Anaconda Prompt and type:
```
activate emcee_workshop
```

Now, we are in this new environment. Your command prompt is prepended with the environment name, which reminds you that you are in this environment. Let's set it up with all of the software you need for this workshop. Install the packages with:
```
conda install numpy scipy matplotlib
```
Say yes to the prompts. `numpy` and `scipy` are scientific python computing packages. `matplotlib` is a plotting package.

`emcee` is not part of conda and has to be installed with pip. I recommend doing this after the conda installation with
```
pip install emcee
```
We're using emcee v2.2.1 for now. There is an upcoming update to emcee v3.0.

Now you have all the packages you need installed! You're still in this environment, so you can leave it and go back to your default or root environment. On macOS/Linux:
```
source deactivate
```
and on Windows:
```
deactivate
```

Later, just activate the environment again (see above) when you're working on the workshop. If you forget your environment names, you can see a list of all of them with:
```
conda env list
```

### Bonus: Interested in switching your default environment to Python3?

Here is a bonus in case you started with Python2 ages ago and now want to switch to Python3. This is not necessary for the workshop. We're not meant to do most of our computing in the default environment, but like many people, that's exactly what I did at first. Now, I create new environments for different analyses (which you can just specify python3 for as above) but sometimes it's handy to have a working set of scientific packages to do something quick or mess around with. So if you installed Anaconda with Python2 in the past and want to default to python3 when you start up a Terminal window, follow these steps. There are many ways to do this, here's my solution with macOS:

I started by creating a copy of my current default environment and naming the copied environment `py2`:
```
conda create --name py2 --clone root
```
(If you are not on macOS, the default environment may not be called `root`, so check with `conda env list`).

This might take awhile if you have a lot of packages in that environment! If you'd like you could do `conda list` first while in the default environment to see what was installed and you can remove unneeded packages with `conda uninstall <pkg name>`.

After this copy is made, create a new environment for python3, with a few basic packages installed
```
conda create --name py3 python=3 numpy scipy matplotlib pandas astropy
```
You can add whatever package names you want, these are just some that I find useful. After you create and switch to this environment, feel free to install more packages.

The last step to automatically switch to this environment whenever you log into your machine or open Terminal. In `.bashrc` or whatever startup script you use, add
```
source activate py3
```
near the end so that you switch to this environment right away. 

Finally, since you saved your old setup (Python2) in the `py2` environment, whenever you need to run the old Python2 code and don't want to deal with updating your code to Python3 (e.g. fixing those print statements), you can just switch to `py2`, run your old code, then switch back.
