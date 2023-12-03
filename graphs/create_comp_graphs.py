
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

FILES = {"quadruped": {
    "jump": {
        "dreamer":{
            "global": "wandb_export_2023-12-03T11_36_11.156+02_00.csv",
            "eval": "wandb_export_2023-12-03T12_48_30.798+02_00.csv"},
        "rnd": {
            "global": "wandb_export_2023-12-03T11_36_11.156+02_00.csv",
            "eval": "wandb_export_2023-12-03T12_48_30.798+02_00.csv"}
        }}}

def load_urlb_result(domain, task, algo, obs):
    data = []
    return data

def load_dreamer_result(domain, task, obs):
    data = []
    return data

def align_results(results, dreamer_res):
    pass

def save_plot(aligned_df):
    pass

if __name__ == "__main__":
    tasks = {
            "walker": ["stand", "walk", "flip", "run"],
            "quadruped": ["stand", "walk", "jump", "fall"],
            "jaco": ["stand", "walk", "jump", "fall"],
            }
    algos = ["icm", "rnd", "ddpg"]

    obs = "pixels"
    for domain in tasks:
        for task in tasks[domain]:
            results = {}
            for algo in algos:
                results[algo] = load_urlb_result(domain, task, algo, obs)
            dreamer_res = load_dreamer_result(domain, task, obs)
            aligned_df = align_results(results, dreamer_res)
            save_plot(aligned_df)
