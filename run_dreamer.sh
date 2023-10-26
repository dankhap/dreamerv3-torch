#!/bin/bash
echo "in bash script"
export PATH=$PATH:/opt/conda/envs/urlb2/bin:/opt/conda/bin
echo "all arguments: $@"
eval "$(conda shell.bash hook)"
conda activate urlb2

python dreamer.py ${@:2}

