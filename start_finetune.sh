#!/usr/bin/bash
#
obs_type="pixel"
domain=${1}
task=${2}
ratio=${3}


if [ "$obs_type" == "pixel" ]; then
	dmc_config="dmc_vision"
else
	dmc_config="dmc_proprio"
fi

if [ "$domain" == "walker" ]; then
	model_path="/code/dreamerv3-torch/logdir/dmc_walker_walk/23111624/"
elif [ "$domain" == "quadruped" ]; then
	model_path="/code/dreamerv3-torch/logdir/dmc_quadruped_stand/30111423/"
elif [ "$domain" == "jaco" ]; then
	model_path="/code/dreamerv3-torch/logdir/dmc_jaco_pretrain/30111648/"
fi

sdate=$(date '+%Y%m%d_%H%M%S')

# print input args for debug
echo "obs_type: ${obs_type}"
echo "domain: ${domain}"
echo "task: ${task}"
echo "ratio: ${ratio}"
echo "model_path: ${model_path}"
echo "dmc_config: ${dmc_config}"
echo "date: ${sdate}"



sbatch --export=ALL,A="fine --configs ${dmc_config} --task dmc_${domain}_${task} --wandb_group dreamerv3_${domain}_${task} --wandb_name ${domain}_${task}_pixel_finetune_${ratio} --modeldir ${model_path} --logdir /code/dreamerv3-torch/logdir/dmc_${domain}_${task}/${sdate}/ --reward_off False --trunc_buffer 0 --expl_until 10 --train_ratio ${ratio} --start_finetuning True --steps 1e5 " ./dreamer_job_git.sh


