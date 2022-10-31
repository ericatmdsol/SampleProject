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

#### Test Folders

The test folder should be an **exact** copy of your src folder, except that rather than the code itself, you're writing tests. One of the most useful things I find about having tests is that during a code review, if I think that someone isn't covering all edge cases, I can easily plop that edge case into the tests, and see whether it passes or not. 