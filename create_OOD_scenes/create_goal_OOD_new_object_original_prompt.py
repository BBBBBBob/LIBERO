import os
import numpy as np
from libero.libero.utils.bddl_generation_utils import get_xy_region_kwargs_list_from_regions_info
from libero.libero.utils.mu_utils import register_mu, InitialSceneTemplates
from libero.libero.utils.task_generation_utils import register_task_info, get_task_info, generate_bddl_from_task_info



@register_mu(scene_type="general")
class GoalObjectScene1(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "table": 1,
            "wooden_cabinet": 1,
            "flat_stove": 1,
            "wine_rack": 1
        }

        object_num_info = {
            "glazed_rim_porcelain_ramekin": 1,
            "cream_cheese": 1,
            "wine_bottle": 1,
            "plate": 1,
        }

        super().__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.02],
                region_name="plate_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.09, 0.00],
                region_name="ramekin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.05],
                region_name="wine_bottle_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.13],
                region_name="cream_cheese_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.21],
                region_name="stove_front_region",
                target_name=self.workspace_name,
                region_half_len=0.04,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.03, -0.24],
                region_name="wooden_cabinet_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.41, 0.21],
                region_name="stove_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.26, -0.26],
                region_name="wine_rack_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wine_bottle_1", "main_table_wine_bottle_region"),
            ("On", "glazed_rim_porcelain_ramekin_1", "main_table_ramekin_region"),
            ("On", "plate_1", "main_table_plate_region"),
            ("On", "cream_cheese_1", "main_table_cream_cheese_region"),
            ("On", "wooden_cabinet_1", "main_table_wooden_cabinet_region"),
            ("On", "flat_stove_1", "main_table_stove_region"),
            ("On", "wine_rack_1", "main_table_wine_rack_region")
        ]
        return states


@register_mu(scene_type="general")
class GoalObjectScene2(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "table": 1,
            "wooden_cabinet": 1,
            "flat_stove": 1,
            "wine_rack": 1
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "cream_cheese": 1,
            "wine_bottle": 1,
            "glazed_rim_porcelain_ramekin": 1,
        }

        super().__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.02],
                region_name="ramekin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.09, 0.00],
                region_name="akita_black_bowl_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.05],
                region_name="wine_bottle_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.13],
                region_name="cream_cheese_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.21],
                region_name="stove_front_region",
                target_name=self.workspace_name,
                region_half_len=0.04,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.03, -0.24],
                region_name="wooden_cabinet_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.41, 0.21],
                region_name="stove_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.26, -0.26],
                region_name="wine_rack_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wine_bottle_1", "main_table_wine_bottle_region"),
            ("On", "akita_black_bowl_1", "main_table_akita_black_bowl_region"),
            ("On", "glazed_rim_porcelain_ramekin_1", "main_table_ramekin_region"),
            ("On", "cream_cheese_1", "main_table_cream_cheese_region"),
            ("On", "wooden_cabinet_1", "main_table_wooden_cabinet_region"),
            ("On", "flat_stove_1", "main_table_stove_region"),
            ("On", "wine_rack_1", "main_table_wine_rack_region")
        ]
        return states


@register_mu(scene_type="general")
class GoalObjectScene3(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "table": 1,
            "wooden_cabinet": 1,
            "flat_stove": 1,
            "wine_rack": 1
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "butter": 1,
            "wine_bottle": 1,
            "plate": 1,
        }

        super().__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.02],
                region_name="plate_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.09, 0.00],
                region_name="akita_black_bowl_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.05],
                region_name="wine_bottle_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.13],
                region_name="butter_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.21],
                region_name="stove_front_region",
                target_name=self.workspace_name,
                region_half_len=0.04,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.03, -0.24],
                region_name="wooden_cabinet_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.41, 0.21],
                region_name="stove_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.26, -0.26],
                region_name="wine_rack_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "wine_bottle_1", "main_table_wine_bottle_region"),
            ("On", "akita_black_bowl_1", "main_table_akita_black_bowl_region"),
            ("On", "plate_1", "main_table_plate_region"),
            ("On", "butter_1", "main_table_butter_region"),
            ("On", "wooden_cabinet_1", "main_table_wooden_cabinet_region"),
            ("On", "flat_stove_1", "main_table_stove_region"),
            ("On", "wine_rack_1", "main_table_wine_rack_region")
        ]
        return states


@register_mu(scene_type="general")
class GoalObjectScene4(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "table": 1,
            "wooden_cabinet": 1,
            "flat_stove": 1,
            "wine_rack": 1
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "cream_cheese": 1,
            "salad_dressing": 1,
            "plate": 1,
        }

        super().__init__(
            workspace_name="main_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.02],
                region_name="plate_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.09, 0.00],
                region_name="akita_black_bowl_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.05],
                region_name="salad_dressing_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.13],
                region_name="cream_cheese_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.21],
                region_name="stove_front_region",
                target_name=self.workspace_name,
                region_half_len=0.04,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.03, -0.24],
                region_name="wooden_cabinet_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.41, 0.21],
                region_name="stove_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.26, -0.26],
                region_name="wine_rack_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "salad_dressing_1", "main_table_salad_dressing_region"),
            ("On", "akita_black_bowl_1", "main_table_akita_black_bowl_region"),
            ("On", "plate_1", "main_table_plate_region"),
            ("On", "cream_cheese_1", "main_table_cream_cheese_region"),
            ("On", "wooden_cabinet_1", "main_table_wooden_cabinet_region"),
            ("On", "flat_stove_1", "main_table_stove_region"),
            ("On", "wine_rack_1", "main_table_wine_rack_region")
        ]
        return states

def main():
    # task 1
    scene_name = "goal_object_scene1"
    language = "open_the_top_drawer_and_put_the_bowl_inside".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["glazed_rim_porcelain_ramekin_1", "wooden_cabinet_1"],
        goal_states=[
            ("In", "glazed_rim_porcelain_ramekin_1", "wooden_cabinet_1_top_region"),
        ],
    )

    # task 2
    scene_name = "goal_object_scene1"
    language = "put_the_bowl_on_the_plate".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["glazed_rim_porcelain_ramekin_1", "plate_1"],
        goal_states=[
            ("On", "glazed_rim_porcelain_ramekin_1", "plate_1"),
        ],
    )

    # task 3
    scene_name = "goal_object_scene1"
    language = "put_the_bowl_on_the_stove".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["glazed_rim_porcelain_ramekin_1", "flat_stove_1"],
        goal_states=[
            ("On", "glazed_rim_porcelain_ramekin_1", "flat_stove_1_cook_region"),
        ],
    )

    # task 4
    scene_name = "goal_object_scene1"
    language = "put_the_bowl_on_top_of_the_cabinet".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["glazed_rim_porcelain_ramekin_1", "wooden_cabinet_1"],
        goal_states=[
            ("On", "glazed_rim_porcelain_ramekin_1", "wooden_cabinet_1_top_side"),
        ],
    )

    # task 5
    scene_name = "goal_object_scene2"
    language = "push_the_plate_to_the_front_of_the_stove".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["glazed_rim_porcelain_ramekin_1"],
        goal_states=[
            ("On", "glazed_rim_porcelain_ramekin_1", "main_table_stove_front_region"),
        ],
    )

    # task 6
    scene_name = "goal_object_scene3"
    language = "put_the_cream_cheese_in_the_bowl".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["butter_1", "akita_black_bowl_1"],
        goal_states=[
            ("On", "butter_1", "akita_black_bowl_1"),
        ],
    )

    # task 7
    scene_name = "goal_object_scene4"
    language = "put_the_wine_bottle_on_the_rack".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["salad_dressing_1", "wine_rack_1"],
        goal_states=[
            ("On", "salad_dressing_1", "wine_rack_1_top_region"),
        ],
    )

    # task 8
    scene_name = "goal_object_scene4"
    language = "put_the_wine_bottle_on_top_of_the_cabinet".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["salad_dressing_1", "wooden_cabinet_1"],
        goal_states=[
            ("On", "salad_dressing_1", "wooden_cabinet_1_top_side"),
        ],
    )


    BDDL_FILE_PATH = "./libero/libero/bddl_files/libero_goal_OOD_new_object_origin_prompt"
    if not os.path.exists(BDDL_FILE_PATH):
        os.makedirs(BDDL_FILE_PATH)
    bddl_file_names, failures = generate_bddl_from_task_info(BDDL_FILE_PATH)
    print(bddl_file_names)


if __name__ == "__main__":
    main()
