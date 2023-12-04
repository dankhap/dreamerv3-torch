import numpy as np
import gymnasium as gym
import jsbsim_gym
class JsbsimEnv:
    metadata = {}

    def __init__(self, name, action_repeat=1, size=(64, 64), camera=None, seed=0, root=''):
        self._env = gym.make(name, config={"root": root})
        self._action_repeat = action_repeat
        self._size = size
        self._camera = 0
        self.reward_range = [-np.inf, np.inf]

    @property
    def observation_space(self):
        spaces = {}
        spaces['obs'] = self._env.observation_space
        spaces["image"] = gym.spaces.Box(0, 255, self._size + (3,), dtype=np.uint8)
        return gym.spaces.Dict(spaces)

    @property
    def action_space(self):
        spec = self._env.action_space
        return spec

    def step(self, action):
        assert np.isfinite(action).all(), action
        reward = 0
        edone = False
        done, trunc = False, False
        for _ in range(self._action_repeat):
            observation, reward, done, trunc, info = self._env.step(action)
            reward += reward
            if done or trunc:
                break
        edone = done or trunc
        obs = dict(obs=observation)
        obs = {key: [val] if len(val.shape) == 0 else val for key, val in obs.items()}
        obs["image"] = self.render()
        # There is no terminal state in DMC
        obs["is_terminal"] = done 
        obs["is_first"] = False
        # info = {"discount": np.array(time_step.discount, np.float32)}
        info = {}
        return obs, reward, edone, info

    def reset(self, seed=None, options=None):
        obs, _ = self._env.reset()
        obs = dict(obs=obs)
        obs = {key: [val] if len(val.shape) == 0 else val for key, val in obs.items()}
        obs["image"] = self.render()
        obs["is_terminal"] = False
        obs["is_first"] = True
        return obs

    def render(self, *args, **kwargs):
        if kwargs.get("mode", "rgb_array") != "rgb_array":
            raise ValueError("Only render mode 'rgb_array' is supported.")
        return self._env.render()
