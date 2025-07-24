import os
import glob
import cv2
from libero.libero import benchmark, get_libero_path
from libero.libero.envs import OffScreenRenderEnv
import torch
### environment varibale egl is for the mujoco
os.environ["MUJOCO_GL"] = "egl"
# task_suite_names = [
#        "libero_object",
#        "libero_goal",
#        "libero_spatial",
#        "libero_10",
# ]
# task_suite_name = task_suite_names[-1]

# if not os.path.exists(f"./scene_image/{task_suite_name}"):
#     os.makedirs(f"./scene_image/{task_suite_name}")
                
# benchmark_dict = benchmark.get_benchmark_dict()
# task_suite = benchmark_dict[task_suite_name]()

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

#     cv2.imwrite(f"./scene_image/{task_suite_name}/test_{task_id}.png", cv2.cvtColor(agent_view, cv2.COLOR_RGB2BGR))
file_name = "libero_10_OOD_flip"
task_bddl_files = glob.glob(f"./libero/libero/bddl_files/{file_name}/*.bddl")
print(task_bddl_files)
file_name += "_offset"
if not os.path.exists(f"./scene_image/{file_name}"):
    os.makedirs(f"./scene_image/{file_name}")


for i in range(len(task_bddl_files)):
    print(os.path.basename(task_bddl_files[i]))
    env_args = {"bddl_file_name": task_bddl_files[i], "camera_heights": 256, "camera_widths": 256, "camera_pos_offset":[-0.2, 0, 0.1], "camera_ori_offset":[0.2, 0.1, 0]}
    env = OffScreenRenderEnv(**env_args)
    env.seed(0)
    env.reset()

    obs = env.env._get_observations()

    agent_view = obs["agentview_image"][::-1, ::-1]
    
    cv2.imwrite(f"./scene_image/{file_name}/test_{i}.png", cv2.cvtColor(agent_view, cv2.COLOR_RGB2BGR))