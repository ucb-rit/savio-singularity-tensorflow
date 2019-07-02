# savio-singularity-tensorflow
Materials for creating a Singularity container for running Tensorflow and Keras on Savio either in the Python interpreter or in a Jupyter notebook.

## To use the container on Savio

You first need access to the container image file. If the image file has not been provided to you, you'll need to create it via the instructions below on building the container. You'll need root access to a Linux machine (one option here is an Amazon EC2 or Google Cloud Platform virtual machine instance; another option is running within a Docker container) in which you've installed Singularity in order to build the container.

### Using the container via command-line Python

To start an interactive Python session with access to Tensorflow and Keras, start an srun session and invoke the following in the shell on the compute node:

```
singularity run --nv tf-gpu.simg 
```

To execute the code in a Python script (here `check-tensorflow.py`), either in an srun session or via sbatch, invoke:

```
singularity run --nv tf-gpu.simg check-tensorflow.py
```

### Using the container via a Jupyter notebook

Start an srun session and invoke the following in the shell (or include the following in your sbatch job script):

```
singularity exec --nv tf-gpu.simg jupyter notebook --no-browser --ip=${SLURMD_NODENAME}
```

Either in the interactive session terminal output or in the SLURM .out file for the running sbatch job, you should see a note about the URL that will allow you to connect to the Jupyter session:

```
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://n0223.savio2:8888/?token=b886deabc6b2fdaba36ccd55d9ac8db425e798a4494e7e12
```

Note that URL, in this case `http://n0223.savio2:8888/?token=b886deabc6b2fdaba36ccd55d9ac8db425e798a4494e7e12`.

Now follow [these instructions](https://research-it.berkeley.edu/services/high-performance-computing/using-brc-visualization-node-realvnc) to start a browser session on the Savio visualization node.

Paste the URL you obtained earlier into the browser and you're ready to compute after you start a Python 3 notebook.

 When you are done with your Jupyter notebook, make sure to kill your `srun` or `sbatch` session so you are not charged for time you don't need.

### Adding Python packages to your container

While one could add additional Python packages to the container itself, the easiest thing to do as a user is to install additional packages outside the container, which is easy to do because Singularity automatically gives you access to files on the host system.

One possibility is to use `pip install --user packageName` inside the container. That will install into the `.local` subdirectory of your home directory on the host system. This might be fine but runs the risk of conflicting with Python packages that you've installed for use on the host system.

Here's an alternative that isolates the additional (statsmodels and scipy and their dependencies in this case) in a directory:

```
export SING_PY_DIRS=~/singularity_tf_pylibs
mkdir ${SING_PY_DIRS}
SINGULARITYENV_PYTHONPATH=${SING_PY_DIRS} singularity exec --nv \
   tf-gpu.simg pip install -t ${SING_PY_DIRS} statsmodels scipy
```

Now when you want to run Python inside the container, make sure to set `SINGULARITYENV_PYTHONPATH` (which sets `PYTHONPATH` inside the container, such that Python knows where to find the packages you've just installed), for example:

```
SINGULARITYENV_PYTHONPATH=${PYTHONPATH} singularity run --nv tf-gpu.simg
```


## To build the container

You'll need access to a machine where you have administrative privileges (i.e., 'root' access). 

```
sudo singularity build tf-gpu.simg tf-gpu-0.3.def
```

Alternatively (i.e., without any special privileges), if you're using a newer version of Singularity, you may be able to build the container via Sylabs Cloud Remote Builder, like this:

```
singularity build --remote tf-gpu.sif tf-gpu-0.3.def
```

You'll need to create an account with Sylabs Cloud. More details are [here](https://www.sylabs.io/guides/3.1/user-guide/singularity_and_docker.html#building-containers-remotely).

## Notes

It won't work to build a container using Tensorflow version 1.13 or higher as they need later versions of the NVIDIA drivers than are available on Savio as of June 2019. 

These instructions should work for both savio2_gpu and savio2_1080ti nodes. Note that building the container off of *nvcr.io/nvidia/tensorflow:18.02-py3* as done in [https://github.com/ucberkeley/brc-cyberinfrastructure] in the *deep-learning-singularity* directory will only work on savio2_1080ti.

Also, I tried to get the container to start Jupyterhub via instance.start but couldn't figure out how to write out the Jupyter URL to a file accessible to the user, nor to print to the screen.

These materials inherit from work by Nicolas Chan and Oliver Muellerklein.
