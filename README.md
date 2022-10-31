## Basic Sample Structure

For what it's worth, this is my preferred structure for a python/R project (provided code is in python, but similar concepts exist in R)

The core principles are:

In projects, updates (not code runs) generally happen in discrete buckets:

1. Data Preprocessing
2. Modeling
3. Output  

Because of this we don't want to mix the code. This allows us to revert individual files to a certain commit, rather than figuring out what has to be reverted in each individual file. It also makes testing your code in discrete units a bit simpler. NOTE: OS X -> Linux has an issue with this only because when we use an explicit 

I prefer using the spec-file vs. the requirements file because in DS projects, it's easier to create a conda env from it:

```bash
conda list --explicit > spec-file.txt            # creates the export
conda create --name new_env --file spec-file.txt # creates the env
```

Make sure you run the following command in your project:

```bash
pip install -e .                     #run this under your code directory 
```

### Code Concepts

#### Hydra

I like using [hydra-core](https://hydra.cc/) to maintain run configurations. It has a default set of configurations that you maintain through a yaml file. Each parameter can then be overridden through commandline prompts. This also provides information to engineering what bits of your configuration might be user configuarable

### Use of TransformersMixin/RegressorMixin

It pays to break down each step of data processing into a specific class. This allows each seperate step to 
1. be debugged independently, 
2. tested independently, 
3. if clients are indecisive, makes it easy revert individual components of the pipeline back with a git command rather than having to modify code (with tests this is less error prone as well) 
4. If you want to ship a model, you can pickle the single pipeline object, and with transforms that require fitting, that comes included without needing to do anything special
5. This makes it easy for the engineers to wrap whatever you did into an application

#### Test Folders

The test folder should be an **exact** copy of your src folder, except that rather than the code itself, you're writing tests. One of the most useful things I find about having tests is that during a code review, if I think that someone isn't covering all edge cases, I can easily plop that edge case into the tests, and see whether it passes or not. 

Link to the presentation that covers more of this:

https://docs.google.com/presentation/u/0/d/1IbreB_NY5XKnrzW7BeFLQeQhlyvZh0rK/edit?usp=slides_home&ths=true&rtpof=true