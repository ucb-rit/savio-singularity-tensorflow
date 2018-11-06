# savio-singularity-tensorflow
Materials for creating Singularity container for running Tensorflow and Keras on Savio in Python either at the command line or in a Jupyter notebook.

## To use the container on Savio

### Using the container via command-line Python

To start an interactive Python session, start an srun session and invoke the following in the shell on the compute node:

```
singularity run --nv tf-gpu-savio.simg 
```

To execute the code in a Python script (here `check-tensorflow.py`), either in an srun session or via sbatch, invoke:

```
singularity run --nv tf-gpu-savio.simg check-tensorflow.py
```

### Using the container via a Jupyter notebook

Start an srun session and invoke the following in the shell (or include the following as the command in your sbatch job script):

```
singularity exec --nv tf-gpu-savio.simg jupyter notebook --no-browser --ip=${SLURMD_NODENAME}
```

```
singularity instance.start --nv tf-gpu-savio.simg
```

Either in the interactive session or in the SLURM .out file for the running sbatch job, note the URL provided by Jupyter, e.g.,

```
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://n0223.savio2:8888/?token=b886deabc6b2fdaba36ccd55d9ac8db425e798a4494e7e12
```

Now follow [these instructions](https://research-it.berkeley.edu/services/high-performance-computing/using-brc-visualization-node-realvnc) to start a browser session on the Savio visualization node.

Paste the URL from above into the browser and you're ready to compute after you start a Python 3 notebook.

 When you are done with your Jupyter notebook, make sure to kill your `srun` or `sbatch` session so you are not charged for time you don't need.

## To build the container

```
sudo singularity build tf-gpu-savio.simg tf_gpu_0.1.def
```

Notes:

These instructions should work for both savio2_gpu and savio2_1080ti nodes. Note that building the container off of nvcr.io/nvidia/tensorflow:18.02-py3 as done in https://github.comb/ucberkeley/brc-cyberinfrastructure in the deep-learning-singularity directory will only work on savio2_1080ti. 

These materials inherit from work by Nicolas Chan and Oliver Muellerklein.
