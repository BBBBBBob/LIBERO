import os
import numpy as np
from libero.libero.utils.bddl_generation_utils import get_xy_region_kwargs_list_from_regions_info
from libero.libero.utils.mu_utils import register_mu, InitialSceneTemplates
from libero.libero.utils.task_generation_utils import register_task_info, get_task_info, generate_bddl_from_task_info


@register_mu(scene_type="general")
class ObjectFlipScene1(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "floor": 1,
        }

        object_num_info = {
            "alphabet_soup": 1,
            "basket": 1,
            "salad_dressing": 1,
            "cream_cheese": 1,
            "milk": 1,
            "tomato_sauce": 1,
            "butter": 1
        }

        super().__init__(
            workspace_name="floor",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.00, -0.26],
                region_name="bin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, 0.24],
                region_name="target_object_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.10],
                region_name="other_object_region_0",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.06],
                region_name="other_object_region_1",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.20],
                region_name="other_object_region_2",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.03],
                region_name="other_object_region_3",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.08],
                region_name="other_object_region_4",
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
            ("On", "alphabet_soup_1", "floor_target_object_region"),
            ("On", "salad_dressing_1", "floor_other_object_region_0"),
            ("On", "cream_cheese_1", "floor_other_object_region_1"),
            ("On", "milk_1", "floor_other_object_region_2"),
            ("On", "tomato_sauce_1", "floor_other_object_region_3"),
            ("On", "butter_1", "floor_other_object_region_4"),
            ("On", "basket_1", "floor_bin_region")
        ]
        return states


@register_mu(scene_type="general")
class ObjectFlipScene2(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "floor": 1,
        }

        object_num_info = {
            "bbq_sauce": 1,
            "basket": 1,
            "chocolate_pudding": 1,
            "ketchup": 1,
            "salad_dressing": 1,
            "alphabet_soup": 1,
            "cream_cheese": 1
        }

        super().__init__(
            workspace_name="floor",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.00, -0.26],
                region_name="bin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.10],  
                region_name="target_object_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, 0.24], 
                region_name="other_object_region_0",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.06],
                region_name="other_object_region_1",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.20],
                region_name="other_object_region_2",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.03],
                region_name="other_object_region_3",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.08],
                region_name="other_object_region_4",
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
            ("On", "chocolate_pudding_1", "floor_other_object_region_0"),
            ("On", "ketchup_1", "floor_other_object_region_1"),
            ("On", "salad_dressing_1", "floor_other_object_region_2"),
            ("On", "alphabet_soup_1", "floor_other_object_region_3"),
            ("On", "cream_cheese_1", "floor_other_object_region_4"),
            ("On", "basket_1", "floor_bin_region")
        ]
        return states


@register_mu(scene_type="general")
class ObjectFlipScene3(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "floor": 1,
        }

        object_num_info = {
            "butter": 1,
            "basket": 1,
            "tomato_sauce": 1,
            "orange_juice": 1,
            "chocolate_pudding": 1,
            "bbq_sauce": 1,
            "ketchup": 1
        }

        super().__init__(
            workspace_name="floor",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.00, -0.26],
                region_name="bin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, 0.24],
                region_name="target_object_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.10],
                region_name="other_object_region_0",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.06],
                region_name="other_object_region_1",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.20],
                region_name="other_object_region_2",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.03],
                region_name="other_object_region_3",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.08],
                region_name="other_object_region_4",
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
            ("On", "butter_1", "floor_target_object_region"),
            ("On", "tomato_sauce_1", "floor_other_object_region_0"),
            ("On", "orange_juice_1", "floor_other_object_region_1"),
            ("On", "chocolate_pudding_1", "floor_other_object_region_2"),
            ("On", "bbq_sauce_1", "floor_other_object_region_3"),
            ("On", "ketchup_1", "floor_other_object_region_4"),
            ("On", "basket_1", "floor_bin_region")
        ]
        return states


@register_mu(scene_type="general")
class ObjectFlipScene4(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "floor": 1,
        }

        object_num_info = {
            "chocolate_pudding": 1,
            "basket": 1,
            "orange_juice": 1,
            "bbq_sauce": 1,
            "ketchup": 1,
            "salad_dressing": 1,
            "alphabet_soup": 1
        }

        super().__init__(
            workspace_name="floor",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.00, -0.26],
                region_name="bin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, 0.24],
                region_name="target_object_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.10],
                region_name="other_object_region_0",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.06],
                region_name="other_object_region_1",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.20],
                region_name="other_object_region_2",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.03],
                region_name="other_object_region_3",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.08],
                region_name="other_object_region_4",
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
            ("On", "chocolate_pudding_1", "floor_target_object_region"),
            ("On", "orange_juice_1", "floor_other_object_region_0"),
            ("On", "bbq_sauce_1", "floor_other_object_region_1"),
            ("On", "ketchup_1", "floor_other_object_region_2"),
            ("On", "salad_dressing_1", "floor_other_object_region_3"),
            ("On", "alphabet_soup_1", "floor_other_object_region_4"),
            ("On", "basket_1", "floor_bin_region")
        ]
        return states
    

@register_mu(scene_type="general")
class ObjectFlipScene5(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "floor": 1,
        }

        object_num_info = {
            "cream_cheese": 1,
            "basket": 1,
            "alphabet_soup": 1,
            "milk": 1,
            "tomato_sauce": 1,
            "butter": 1,
            "orange_juice": 1
        }

        super().__init__(
            workspace_name="floor",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.00, -0.26],
                region_name="bin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.10],  
                region_name="target_object_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, 0.24], 
                region_name="other_object_region_0",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.06],
                region_name="other_object_region_1",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.20],
                region_name="other_object_region_2",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.03],
                region_name="other_object_region_3",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.08],
                region_name="other_object_region_4",
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
            ("On", "cream_cheese_1", "floor_target_object_region"),
            ("On", "alphabet_soup_1", "floor_other_object_region_0"),
            ("On", "milk_1", "floor_other_object_region_1"),
            ("On", "tomato_sauce_1", "floor_other_object_region_2"),
            ("On", "butter_1", "floor_other_object_region_3"),
            ("On", "orange_juice_1", "floor_other_object_region_4"),
            ("On", "basket_1", "floor_bin_region")
        ]
        return states


@register_mu(scene_type="general")
class ObjectFlipScene6(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "floor": 1,
        }

        object_num_info = {
            "ketchup": 1,
            "basket": 1,
            "bbq_sauce": 1,
            "salad_dressing": 1,
            "alphabet_soup": 1,
            "cream_cheese": 1,
            "milk": 1
        }

        super().__init__(
            workspace_name="floor",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.00, -0.26],
                region_name="bin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, 0.24],  
                region_name="target_object_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.10], 
                region_name="other_object_region_0",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.06],
                region_name="other_object_region_1",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.20],
                region_name="other_object_region_2",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.03],
                region_name="other_object_region_3",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.08],
                region_name="other_object_region_4",
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
            ("On", "ketchup_1", "floor_target_object_region"),
            ("On", "bbq_sauce_1", "floor_other_object_region_0"),
            ("On", "salad_dressing_1", "floor_other_object_region_1"),
            ("On", "alphabet_soup_1", "floor_other_object_region_2"),
            ("On", "cream_cheese_1", "floor_other_object_region_3"),
            ("On", "milk_1", "floor_other_object_region_4"),
            ("On", "basket_1", "floor_bin_region")
        ]
        return states


@register_mu(scene_type="general")
class ObjectFlipScene7(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "floor": 1,
        }

        object_num_info = {
            "milk": 1,
            "basket": 1,
            "cream_cheese": 1,
            "tomato_sauce": 1,
            "butter": 1,
            "orange_juice": 1,
            "chocolate_pudding": 1
        }

        super().__init__(
            workspace_name="floor",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.00, -0.26],
                region_name="bin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, 0.24],  
                region_name="target_object_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.10], 
                region_name="other_object_region_0",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.06],
                region_name="other_object_region_1",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.20],
                region_name="other_object_region_2",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.03],
                region_name="other_object_region_3",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.08],
                region_name="other_object_region_4",
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
            ("On", "milk_1", "floor_target_object_region"),
            ("On", "cream_cheese_1", "floor_other_object_region_0"),
            ("On", "tomato_sauce_1", "floor_other_object_region_1"),
            ("On", "butter_1", "floor_other_object_region_2"),
            ("On", "orange_juice_1", "floor_other_object_region_3"),
            ("On", "chocolate_pudding_1", "floor_other_object_region_4"),
            ("On", "basket_1", "floor_bin_region")
        ]
        return states
    

@register_mu(scene_type="general")
class ObjectFlipScene8(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "floor": 1,
        }

        object_num_info = {
            "orange_juice": 1,
            "basket": 1,
            "butter": 1,
            "chocolate_pudding": 1,
            "bbq_sauce": 1,
            "ketchup": 1,
            "salad_dressing": 1
        }

        super().__init__(
            workspace_name="floor",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.00, -0.26],
                region_name="bin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.10],  
                region_name="target_object_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, 0.24], 
                region_name="other_object_region_0",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.06],
                region_name="other_object_region_1",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.20],
                region_name="other_object_region_2",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.03],
                region_name="other_object_region_3",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.08],
                region_name="other_object_region_4",
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
            ("On", "orange_juice_1", "floor_target_object_region"),
            ("On", "butter_1", "floor_other_object_region_0"),
            ("On", "chocolate_pudding_1", "floor_other_object_region_1"),
            ("On", "bbq_sauce_1", "floor_other_object_region_2"),
            ("On", "ketchup_1", "floor_other_object_region_3"),
            ("On", "salad_dressing_1", "floor_other_object_region_4"),
            ("On", "basket_1", "floor_bin_region")
        ]
        return states


@register_mu(scene_type="general")
class ObjectFlipScene9(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "floor": 1,
        }

        object_num_info = {
            "salad_dressing": 1,
            "basket": 1,
            "ketchup": 1,
            "alphabet_soup": 1,
            "cream_cheese": 1,
            "milk": 1,
            "tomato_sauce": 1
        }

        super().__init__(
            workspace_name="floor",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.00, -0.26],
                region_name="bin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.10],  
                region_name="target_object_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, 0.24], 
                region_name="other_object_region_0",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.06],
                region_name="other_object_region_1",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.20],
                region_name="other_object_region_2",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.03],
                region_name="other_object_region_3",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.08],
                region_name="other_object_region_4",
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
            ("On", "salad_dressing_1", "floor_target_object_region"),
            ("On", "ketchup_1", "floor_other_object_region_0"),
            ("On", "alphabet_soup_1", "floor_other_object_region_1"),
            ("On", "cream_cheese_1", "floor_other_object_region_2"),
            ("On", "milk_1", "floor_other_object_region_3"),
            ("On", "tomato_sauce_1", "floor_other_object_region_4"),
            ("On", "basket_1", "floor_bin_region")
        ]
        return states


@register_mu(scene_type="general")
class ObjectFlipScene10(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "floor": 1,
        }

        object_num_info = {
            "tomato_sauce": 1,
            "basket": 1,
            "milk": 1,
            "butter": 1,
            "orange_juice": 1,
            "chocolate_pudding": 1,
            "bbq_sauce": 1
        }

        super().__init__(
            workspace_name="floor",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.00, -0.26],
                region_name="bin_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.10],  
                region_name="target_object_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.12, 0.24], 
                region_name="other_object_region_0",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.06],
                region_name="other_object_region_1",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.20],
                region_name="other_object_region_2",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.15, -0.03],
                region_name="other_object_region_3",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.08],
                region_name="other_object_region_4",
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
            ("On", "tomato_sauce_1", "floor_target_object_region"),
            ("On", "milk_1", "floor_other_object_region_0"),
            ("On", "butter_1", "floor_other_object_region_1"),
            ("On", "orange_juice_1", "floor_other_object_region_2"),
            ("On", "chocolate_pudding_1", "floor_other_object_region_3"),
            ("On", "bbq_sauce_1", "floor_other_object_region_4"),
            ("On", "basket_1", "floor_bin_region")
        ]
        return states
    

def main():
    # task 1
    scene_name = "object_flip_scene1"
    language = "pick_up_the_alphabet_soup_and_place_it_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["alphabet_soup_1", "basket_1"],
        goal_states=[
            ("In", "alphabet_soup_1", "basket_1_contain_region"),
        ],
    )

    # task 2
    scene_name = "object_flip_scene2"
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
    scene_name = "object_flip_scene3"
    language = "pick_up_the_butter_and_place_it_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["butter_1", "basket_1"],
        goal_states=[
            ("In", "butter_1", "basket_1_contain_region"),
        ],
    )

    # task 4
    scene_name = "object_flip_scene4"
    language = "pick_up_the_chocolate_pudding_and_place_it_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["chocolate_pudding_1", "basket_1"],
        goal_states=[
            ("In", "chocolate_pudding_1", "basket_1_contain_region"),
        ],
    )

    # task 5
    scene_name = "object_flip_scene5"
    language = "pick_up_the_cream_cheese_and_place_it_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["cream_cheese_1", "basket_1"],
        goal_states=[
            ("In", "cream_cheese_1", "basket_1_contain_region"),
        ],
    )

    # task 6
    scene_name = "object_flip_scene6"
    language = "pick_up_the_ketchup_and_place_it_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["ketchup_1", "basket_1"],
        goal_states=[
            ("In", "ketchup_1", "basket_1_contain_region"),
        ],
    )

    # task 7
    scene_name = "object_flip_scene7"
    language = "pick_up_the_milk_and_place_it_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["milk_1", "basket_1"],
        goal_states=[
            ("In", "milk_1", "basket_1_contain_region"),
        ],
    )

    # task 8
    scene_name = "object_flip_scene8"
    language = "pick_up_the_orange_juice_and_place_it_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["orange_juice_1", "basket_1"],
        goal_states=[
            ("In", "orange_juice_1", "basket_1_contain_region"),
        ],
    )

    # task 9
    scene_name = "object_flip_scene9"
    language = "pick_up_the_salad_dressing_and_place_it_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["salad_dressing_1", "basket_1"],
        goal_states=[
            ("In", "salad_dressing_1", "basket_1_contain_region"),
        ],
    )

    # task 10
    scene_name = "object_flip_scene10"
    language = "pick_up_the_tomato_sauce_and_place_it_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["tomato_sauce_1", "basket_1"],
        goal_states=[
            ("In", "tomato_sauce_1", "basket_1_contain_region"),
        ],
    )

    BDDL_FILE_PATH = "./libero/libero/bddl_files/libero_object_OOD_flip"
    if not os.path.exists(BDDL_FILE_PATH):
        os.makedirs(BDDL_FILE_PATH)
    bddl_file_names, failures = generate_bddl_from_task_info(BDDL_FILE_PATH)
    print(bddl_file_names)


if __name__ == "__main__":
    main()
