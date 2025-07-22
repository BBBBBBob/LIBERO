import os
import numpy as np
from libero.libero.utils.bddl_generation_utils import get_xy_region_kwargs_list_from_regions_info
from libero.libero.utils.mu_utils import register_mu, InitialSceneTemplates
from libero.libero.utils.task_generation_utils import register_task_info, get_task_info, generate_bddl_from_task_info

@register_mu(scene_type="general")
class LongFlipScene1(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "chefmate_8_frypan": 1,
            "moka_pot": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, -0.2],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, 0.25],
                region_name="frypan_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
                yaw_rotation=(-np.pi/2, -np.pi/2)
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.00],
                region_name="moka_pot_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
                yaw_rotation=(np.pi, np.pi)
            )
        )
       

        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "chefmate_8_frypan_1", "kitchen_table_frypan_init_region"),
            ("On", "moka_pot_1", "kitchen_table_moka_pot_init_region"),
        ]
        return states


@register_mu(scene_type="general")
class LongFlipScene2(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "white_cabinet": 1,
            "wine_rack": 1
        }

        object_num_info = {
            "akita_black_bowl": 1,
            "wine_bottle": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.3],
                region_name="white_cabinet_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.10, 0.30],
                region_name="wine_rack_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.03, 0.05],
                region_name="akita_black_bowl_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.05],
                region_name="wine_bottle_init_region",
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
            ("On", "akita_black_bowl_1", "kitchen_table_akita_black_bowl_init_region"),
            ("On", "wine_bottle_1", "kitchen_table_wine_bottle_init_region"),
            ("On", "white_cabinet_1", "kitchen_table_white_cabinet_init_region"),
            ("On", "wine_rack_1", "kitchen_table_wine_rack_init_region"),
            ("Open", "white_cabinet_1_bottom_region")

        ]
        return states


@register_mu(scene_type="general")
class LongFlipScene3(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "microwave": 1,
        }

        object_num_info = {
            "porcelain_mug": 1,
            "white_yellow_mug": 1,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.35],
                region_name="microwave_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.0],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
                yaw_rotation=(np.pi/2, np.pi/2)
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.10, 0.25],
                region_name="porcelain_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
                yaw_rotation=(np.pi/2, np.pi/2)
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.25],
                region_name="porcelain_mug_front_region",
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
            ("On", "porcelain_mug_1", "kitchen_table_porcelain_mug_init_region"),
            ("On", "white_yellow_mug_1", "kitchen_table_white_yellow_mug_init_region"),
            ("On", "microwave_1", "kitchen_table_microwave_init_region"),
            ("Open", "microwave_1")

        ]
        return states


@register_mu(scene_type="general")
class LongFlipScene4(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "kitchen_table": 1,
            "flat_stove": 1,
        }

        object_num_info = {
            "moka_pot": 2,
        }

        super().__init__(
            workspace_name="kitchen_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.2, 0.2],
                region_name="flat_stove_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.05, -0.25],
                region_name="moka_pot_left_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
                yaw_rotation=(np.pi, np.pi)
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.05],
                region_name="moka_pot_right_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
                yaw_rotation=(np.pi, np.pi)
            )
        )
       

        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(
            self.regions
        )

    @property
    def init_states(self):
        states = [
            ("On", "flat_stove_1", "kitchen_table_flat_stove_init_region"),
            ("On", "moka_pot_1", "kitchen_table_moka_pot_left_init_region"),
            ("On", "moka_pot_2", "kitchen_table_moka_pot_right_init_region"),
            ("Turnon", "flat_stove_1")

        ]
        return states


@register_mu(scene_type="general")
class LongFlipScene5(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "living_room_table": 1,
        }

        object_num_info = {
            "alphabet_soup": 1,
            "cream_cheese": 1,
            "tomato_sauce": 1,
            "ketchup": 1,
            "basket": 1,
        }

        super().__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.26],
                region_name="basket_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.1],
                region_name="alphabet_soup_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.15, -0.06],
                region_name="cream_cheese_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.20],
                region_name="tomato_sauce_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.20, 0.15],
                region_name="ketchup_init_region",
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
            ("On", "alphabet_soup_1", "living_room_table_alphabet_soup_init_region"),
            ("On", "cream_cheese_1", "living_room_table_cream_cheese_init_region"),
            ("On", "tomato_sauce_1", "living_room_table_tomato_sauce_init_region"),
            ("On", "ketchup_1", "living_room_table_ketchup_init_region"),
            ("On", "basket_1", "living_room_table_basket_init_region"),
        ]
        return states


@register_mu(scene_type="general")
class LongFlipScene6(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "living_room_table": 1,
        }

        object_num_info = {
            "alphabet_soup": 1,
            "cream_cheese": 1,
            "tomato_sauce": 1,
            "ketchup": 1,
            "orange_juice": 1,
            "milk": 1,
            "butter": 1,
            "basket": 1,
        }

        super().__init__(
            workspace_name="living_room_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.26],
                region_name="basket_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, 0.1],
                region_name="milk_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.20],
                region_name="cream_cheese_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, 0.25],
                region_name="orange_juice_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.10, -0.05],
                region_name="tomato_sauce_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.10, 0.15],
                region_name="alphabet_soup_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.05, -0.05],
                region_name="butter_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
            )
        )

        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.25, 0.15],
                region_name="ketchup_init_region",
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
            ("On", "alphabet_soup_1", "living_room_table_alphabet_soup_init_region"),
            ("On", "cream_cheese_1", "living_room_table_cream_cheese_init_region"),
            ("On", "tomato_sauce_1", "living_room_table_tomato_sauce_init_region"),
            ("On", "ketchup_1", "living_room_table_ketchup_init_region"),
            ("On", "milk_1", "living_room_table_milk_init_region"),
            ("On", "orange_juice_1", "living_room_table_orange_juice_init_region"),
            ("On", "butter_1", "living_room_table_butter_init_region"),
            ("On", "basket_1", "living_room_table_basket_init_region"),
        ]
        return states
    

@register_mu(scene_type="general")
class LongFlipScene7(InitialSceneTemplates):
    def __init__(self):

        fixture_num_info = {
            "study_table": 1,
            "desk_caddy": 1,
        }

        object_num_info = {
            "black_book": 1,
            "white_yellow_mug": 1,
        }

        super().__init__(
            workspace_name="study_table",
            fixture_num_info=fixture_num_info,
            object_num_info=object_num_info,
        )

    def define_regions(self):
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.20, 0.14],
                region_name="desk_caddy_init_region",
                target_name=self.workspace_name,
                region_half_len=0.01,
                yaw_rotation=(np.pi, np.pi)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.0, -0.15],
                region_name="black_book_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
                yaw_rotation=(-np.pi / 2, 5 * np.pi / 4),
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[0.10, 0.0],
                region_name="white_yellow_mug_init_region",
                target_name=self.workspace_name,
                region_half_len=0.025,
                yaw_rotation=(np.pi / 2, np.pi / 2)
            )
        )
        self.regions.update(
            self.get_region_dict(
                region_centroid_xy=[-0.20, -0.15],
                region_name="desk_caddy_left_region",
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
            ("On", "desk_caddy_1", "study_table_desk_caddy_init_region"),
            ("On", "black_book_1", "study_table_black_book_init_region"),
            ("On", "white_yellow_mug_1", "study_table_white_yellow_mug_init_region"),
        ]
        return states

    

def main():
    # task 1
    scene_name = "long_flip_scene1"
    language = "turn_on_the_stove_and_put_the_moka_pot_on_it".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["moka_pot_1", "flat_stove_1"],
        goal_states=[
            ("Turnon", "flat_stove_1"),
            ("On", "moka_pot_1", "flat_stove_1_cook_region")
        ],
    )

    # task 2
    scene_name = "long_flip_scene2"
    language = "put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["akita_black_bowl_1", "white_cabinet_1"],
        goal_states=[
            ("Close", "white_cabinet_1_bottom_region"),
            ("On", "akita_black_bowl_1", "white_cabinet_1_bottom_region")
        ],
    )

    # task 3
    scene_name = "long_flip_scene3"
    language = "put_the_yellow_and_white_mug_in_the_microwave_and_close_it".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["white_yellow_mug_1", "microwave_1"],
        goal_states=[
            ("In", "white_yellow_mug_1", "microwave_1_heating_region"),
            ("Close", "microwave_1")
        ],
    )

    # task 4
    scene_name = "long_flip_scene4"
    language = "put_both_moka_pots_on_the_stove".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["moka_pot_1", "moka_pot_2", "flat_stove_1"],
        goal_states=[
            ("On", "moka_pot_1", "flat_stove_1_cook_region"),
            ("On", "moka_pot_2", "flat_stove_1_cook_region"),
            ("Turnon", "flat_stove_1")
        ],
    )

    # task 5
    scene_name = "long_flip_scene5"
    language = "put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["alphabet_soup_1", "cream_cheese_1", "basket_1"],
        goal_states=[
            ("In", "alphabet_soup_1", "basket_1_contain_region"),
            ("In", "cream_cheese_1", "basket_1_contain_region")
        ],
    )

    # task 6
    scene_name = "long_flip_scene6"
    language = "put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["alphabet_soup_1", "tomato_sauce_1", "basket_1"],
        goal_states=[
            ("In", "alphabet_soup_1", "basket_1_contain_region"),
            ("In", "tomato_sauce_1", "basket_1_contain_region")
        ],
    )

    # task 7
    scene_name = "long_flip_scene6"
    language = "put_both_the_cream_cheese_box_and_the_butter_in_the_basket".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["cream_cheese_1", "butter_1", "basket_1"],
        goal_states=[
            ("In", "cream_cheese_1", "basket_1_contain_region"),
            ("In", "butter_1", "basket_1_contain_region")
        ],
    )

    # task 8
    scene_name = "long_flip_scene7"
    language = "pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy".replace("_", " ")
    register_task_info(
        language,
        scene_name=scene_name,
        objects_of_interest=["black_book_1", "desk_caddy_1"],
        goal_states=[
            ("In", "black_book_1", "desk_caddy_1_back_contain_region")
        ],
    )



    BDDL_FILE_PATH = "./libero/libero/bddl_files/libero_10_OOD_flip"
    if not os.path.exists(BDDL_FILE_PATH):
        os.makedirs(BDDL_FILE_PATH)
    bddl_file_names, failures = generate_bddl_from_task_info(BDDL_FILE_PATH)
    print(bddl_file_names)


if __name__ == "__main__":
    main()