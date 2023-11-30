#!/usr/bin/bash
#
obs_type=${1}
domain=${2}
task=${3}
ratio=${4}

# print input args for debug
echo "obs_type: ${obs_type}"
echo "domain: ${domain}"
echo "task: ${task}"
echo "ratio: ${ratio}"

if [ "$obs_type" == "pixel" ]; then
	dmc_config="dmc_vision"
else
	dmc_config="dmc_proprio"
fi

if [ "$domain" == "walker" ]; then
	model_path="/code/dreamerv3-torch/logdir/dmc_walker_walk/23111624/"
elif [ "$domain" == "quadruped" ]; then
	model_path="/code/dreamerv3-torch/logdir/dmc_quadruped_walk/23111624/"
fi

sdate=$(date '+%Y%m%d_%H%M%S')

sbatch --export=ALL,A="fine --configs ${dmc_config} --task dmc_${domain}_${task} --wandb_group dreamerv3_${domain}_${task} --wandb_name ${domain}_${task}_pixel_finetune_${ratio} --modeldir /code/dreamerv3-torch/logdir/dmc_walker_walk/23111624/ --logdir /code/dreamerv3-torch/logdir/dmc_walker_run/${sdate}/ --reward_off False --trunc_buffer 0 --expl_until 10 --train_ratio ${ratio} --start_finetuning True --steps 1e5 " ./dreamer_job_git.sh


