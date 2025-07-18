import os
import glob
import cv2
from libero.libero import benchmark, get_libero_path
from libero.libero.envs import OffScreenRenderEnv

task_suite_names = [
       "libero_object",
       "libero_goal",
       "libero_spatial",
       "libero_10",
]
task_suite_name = task_suite_names[0]
benchmark_dict = benchmark.get_benchmark_dict()
task_suite = benchmark_dict[task_suite_name]()

# num_tasks = task_suite.get_num_tasks()
# language_list = []
# for task_id in range(num_tasks):
#     task = task_suite.get_task(task_id)
#     print("The task is: ", task.language)
#     task_bddl_file = os.path.join(get_libero_path("bddl_files"), task.problem_folder, task.bddl_file)
#     env_args = {"bddl_file_name": task_bddl_file, "camera_heights": 256, "camera_widths": 256}
#     env = OffScreenRenderEnv(**env_args)
#     env.seed(0)

#     initial_states = task_suite.get_task_init_states(task_id)
    
#     env.reset()
#     obs = env.set_init_state(initial_states[0])

#     agent_view = obs["agentview_image"][::-1, ::-1]

#     cv2.imwrite(f"./scene_image/{task_suite_name}/{task_suite_name}_{task_id}.png", cv2.cvtColor(agent_view, cv2.COLOR_RGB2BGR))

task_bddl_files = glob.glob("libero/libero/bddl_files/libero_goal_random/*.bddl")
for i in range(len(task_bddl_files)):
    env_args = {"bddl_file_name": task_bddl_files[i], "camera_heights": 256, "camera_widths": 256, "camera_offset_pos": [0, 0.3, 0], "camera_offset_quat": [0, 0, 0, 1]}  #"camera_offset_quat": [ 0, 0.1081878, 0, 0.9941305]
    env = OffScreenRenderEnv(**env_args)
    env.seed(0)
    env.reset()

    obs = env.env._get_observations()

    agent_view = obs["agentview_image"][::-1, ::-1]

    cv2.imwrite(f"./scene_image/libero_goal_random/test_{i}_shift_extrem.png", cv2.cvtColor(agent_view, cv2.COLOR_RGB2BGR))