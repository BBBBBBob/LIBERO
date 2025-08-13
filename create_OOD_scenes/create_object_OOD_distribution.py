import os
import numpy as np
from libero.libero.utils.bddl_generation_utils import get_xy_region_kwargs_list_from_regions_info
from libero.libero.utils.mu_utils import register_mu, InitialSceneTemplates
from libero.libero.utils.task_generation_utils import register_task_info, get_task_info, generate_bddl_from_task_info

@register_mu(scene_type="general")
class ObjectDistScene1(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "floor": 1,
        }

        object_num_info = {
            "bbq_sauce": 1,
            "basket": 1,
        }

        super().__init__(
            workspace_name="floor",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.00, 0.26],
                region_name="bin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.10],  
                region_name="target_object_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "bbq_sauce_1", "floor_target_object_region"),
            ("On", "basket_1", "floor_bin_region")
        ]
        return states


@register_mu(scene_type="general")
class ObjectDistScene2(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "floor": 1,
        }

        object_num_info = {
            "bbq_sauce": 1,
            "basket": 1,
        }

        super().__init__(
            workspace_name="floor",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.00, 0.26],
                region_name="bin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.10],  
                region_name="target_object_region",
                target_name=self.workspace_name,
                region_half_len=0.05,
            )
        )

        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "bbq_sauce_1", "floor_target_object_region"),
            ("On", "basket_1", "floor_bin_region")
        ]
        return states



@register_mu(scene_type="general")
class ObjectDistScene3(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "floor": 1,
        }

        object_num_info = {
            "bbq_sauce": 1,
            "basket": 1,
        }

        super().__init__(
            workspace_name="floor",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.00, 0.26],
                region_name="bin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.10],  
                region_name="target_object_region",
                target_name=self.workspace_name,
                region_half_len=0.1,
            )
        )

        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "bbq_sauce_1", "floor_target_object_region"),
            ("On", "basket_1", "floor_bin_region")
        ]
        return states



@register_mu(scene_type="general")
class ObjectDistScene4(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "floor": 1,
        }

        object_num_info = {
            "bbq_sauce": 1,
            "basket": 1,
        }

        super().__init__(
            workspace_name="floor",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.00, 0.26],
                region_name="bin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.10],  
                region_name="target_object_region",
                target_name=self.workspace_name,
                region_half_len=0.2,
            )
        )

        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "bbq_sauce_1", "floor_target_object_region"),
            ("On", "basket_1", "floor_bin_region")
        ]
        return states



def main():
    # task 1
    scene_name = "object_dist_scene1"
    language = "pick_up_the_bbq_sauce_and_place_it_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["bbq_sauce_1", "basket_1"],
        goal_states=[
            ("In", "bbq_sauce_1", "basket_1_contain_region"),
        ],
    )

    # task 2
    scene_name = "object_dist_scene2"
    language = "pick_up_the_bbq_sauce_and_place_it_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["bbq_sauce_1", "basket_1"],
        goal_states=[
            ("In", "bbq_sauce_1", "basket_1_contain_region"),
        ],
    )

    # task 3
    scene_name = "object_dist_scene3"
    language = "pick_up_the_bbq_sauce_and_place_it_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["bbq_sauce_1", "basket_1"],
        goal_states=[
            ("In", "bbq_sauce_1", "basket_1_contain_region"),
        ],
    )

    # task 4
    scene_name = "object_dist_scene4"
    language = "pick_up_the_bbq_sauce_and_place_it_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["bbq_sauce_1", "basket_1"],
        goal_states=[
            ("In", "bbq_sauce_1", "basket_1_contain_region"),
        ],
    )

    BDDL_FILE_PATH = "./libero/libero/bddl_files/libero_object_OOD_distribution"
    if not os.path.exists(BDDL_FILE_PATH):
        os.makedirs(BDDL_FILE_PATH)
    bddl_file_names, failures = generate_bddl_from_task_info(BDDL_FILE_PATH)
    print(bddl_file_names)


if __name__ == "__main__":
    main()
