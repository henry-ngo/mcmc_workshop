# Session 0: Set up instructions and recommended review

## Setting up the workshop environment with required packages
Please click on [setup_python.md](./setup_python.md) to read instructions for setting up your laptop for this workshop. 

## Viewing the recommended review (Jupyter notebook)
If you have experience with git, you can clone this repository to get all the files. If not, you can just use the file tree above to get to any file you need and then view them on the Github website or download them to your computer.

Many files in this repository have the `.ipynb` extension and are known as Jupyter Notebooks (or iPython notebooks, to use the old name). These are interactive notebooks that allow you to see the code, run snippets and see the results. On the Github website, clicking on the file just shows you a *static* HTML rendering (no interaction). To get the full experience, you must download them and then open them with your notebook interface. It's easiest if you first navigate to the `Session0` directory in your Terminal then run
```
jupyter notebook
```
I found that for some reason, on my machine, I sometimes get an error about importing `dateutil.tz`. I am not sure why it happens but when I try:
```
ipython notebook
```
it works after a redirect from ipython to Jupyter. ipython will soon be deprecated in favour of Jupyter but this seems to be a good workaround for now. I will update this space when I figure out what the problem is.

After setting up your environment as per the first section, this command should a directory tree in your web browser. You can then navigate around and click on an existing notebook file or create a new one. Within the notebook file, each cell can be code or text formatted in the Markdown language, and you can "run" each cell by pressing Shift and Enter while selecting that cell. If you don't want to run notebooks or if you can't get it to work, you can also type the lines into your own python code.

Here is a page showing some basics for using these notebooks: https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html

The recommended review is in a notebook format to get you familiar with it since the rest of the sessions will use the notebook a lot. But if you have trouble getting it to work, there isn't much interaction so you can just view it by clicking on [review.ipynb](./review.ipynb) above.

Finally, a shortcut if you want to just open a notebook file directly, you can type `jupyter notebook <filename>`
