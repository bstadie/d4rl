HOPPER_RANDOM_SCORE = -20.272305
HALFCHEETAH_RANDOM_SCORE = -280.178953
WALKER_RANDOM_SCORE = 1.629008
ANT_RANDOM_SCORE = -325.6

HOPPER_EXPERT_SCORE = 3234.3
HALFCHEETAH_EXPERT_SCORE = 12135.0
WALKER_EXPERT_SCORE = 4592.3
ANT_EXPERT_SCORE = 3879.7

from gym.envs.registration import register


def get_half_cheetah():
    register(
    id='halfcheetah-medium-v2',
    entry_point='d4rl.gym_mujoco.gym_envs:get_cheetah_env',
    max_episode_steps=1000,
    kwargs={
        'deprecated': False,
        'ref_min_score': HALFCHEETAH_RANDOM_SCORE,
        'ref_max_score': HALFCHEETAH_EXPERT_SCORE,
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/gym_mujoco/halfcheetah_medium.hdf5'
    }
    )
    return gym.make('halfcheetah-medium-v2')




