"""
scenarios.py CARLA-Gym collection of Carla scenarios based on node IDs
from 0.8.x. Currently needs a conversion tool to convert between node IDs and
(x, y, z) coordinate locations
__author__:PP
"""

TEST_WEATHERS = [0, 2, 5, 7, 9, 10, 11, 12, 13]
TRAIN_WEATHERS = [1, 3, 4, 6, 8, 14]

PAPER_TEST_WEATHERS = [
    1, 8, 5, 3
]  # clear day, clear sunset, daytime rain, daytime after rain
PAPER_TRAIN_WEATHERS = [2, 14]  # cloudy daytime, soft rain at sunset


def build_scenario(city, start, end, vehicles, pedestrians, max_steps,
                   weathers):
    scenario = {
        "city": city,
        "num_vehicles": vehicles,
        "num_pedestrians": pedestrians,
        "weather_distribution": weathers,
        "max_steps": max_steps,
    }
    if isinstance(start, list) and isinstance(end, list):
        scenario.update({"start_pos_loc": start, "end_pos_loc": end})
    elif isinstance(start, int) and isinstance(end, int):
        scenario.update({"start_pos_id": start, "end_pos_id": end})
    return scenario


def build_ma_scenario(city, vehicles, pedestrians, max_steps, weathers):
    scenario = {
        "city": city,
        "vehicles": vehicles,
        "pedestrians": pedestrians,
        "weather_distribution": weathers,
        "max_steps": max_steps,
    }

    return scenario


# Temporary (quick) soln to use MA. By defining one dict per agent in
# the scenario. Can be improved by using something like the triple quoted eg:
"""
# Scenario for Town02 that involves driving through an intersection with a
# pedestrian crossing one side
INTERSECTION_SCENARIO_TOWN2 = build_ma_scenario(
   city="Town02",
   vehicles=[(start1,end1),(start2,end2)],
   pedestrians=[(start1,end1)],
   max_steps=2000,
   weathers=[0])
"""
"""Stop Sign Urban Intersection scenario with 3 Cars passing through.
TAG: SSUIC3
"""

SSUIC3_TOWN3_CAR1 = build_scenario(
    city="Town03",
    start=[170.5, 80, 0.4],
    end=[144, 59, 0],
    vehicles=1,
    pedestrians=0,
    max_steps=500,
    weathers=[0])

SSUIC3_TOWN3_CAR2 = build_scenario(
    city="Town03",
    start=[188, 59, 0.4],
    end=[167, 75.7, 0.13],
    vehicles=1,
    pedestrians=0,
    max_steps=500,
    weathers=[0])

SSUIC3_TOWN3_CAR3 = build_scenario(
    city="Town03",
    start=[147.6, 62.6, 0.4],
    end=[191.2, 62.7, 0],
    vehicles=1,
    pedestrians=0,
    max_steps=500,
    weathers=[0])

# End of TAG: SSUIC3
"""Signalized Urban Intersection scenario with 3 Cars passing through.
CAR1: Starts almost inside the intersection, goes straight
CAR2: Starts 90 wrt CAR1 close to intersection, turns right to merge
CAR3: Starts behind CAR1 away from intersection, goes straight
TAG: SUIC3
"""

SUIC3_TOWN3_CAR1 = build_scenario(
    city="Town03",
    start=[70, -132.8, 8],
    end=[127, -132, 8],
    vehicles=1,
    pedestrians=0,
    max_steps=500,
    weathers=[0])

SUIC3_TOWN3_CAR2 = build_scenario(
    city="Town03",
    start=[84.3, -118, 9],
    end=[120, -132, 8],
    vehicles=1,
    pedestrians=0,
    max_steps=500,
    weathers=[0])

SUIC3_TOWN3_CAR3 = build_scenario(
    city="Town03",
    start=[43, -133, 4],
    end=[100, -132, 8],
    vehicles=1,
    pedestrians=0,
    max_steps=500,
    weathers=[0])
# End of TAG: SUIC3

INTERSECTION_TOWN3_CAR1 = build_scenario(
    city="Town03",
    start=[94, -132.7, 10],
    end=[106, -132.7, 8],
    vehicles=1,
    pedestrians=0,
    max_steps=300,
    weathers=[0])
INTERSECTION_TOWN3_CAR2 = build_scenario(
    city="Town03",
    start=[84, -115, 10],
    end=[41, -137, 8],
    vehicles=1,
    pedestrians=0,
    max_steps=300,
    weathers=[0])
INTERSECTION_TOWN3_PED1 = build_scenario(
    city="Town03",
    start=[74, -126, 10],
    end=[92, -125, 8],
    vehicles=0,
    pedestrians=1,
    max_steps=300,
    weathers=[0])
INTERSECTION_TOWN3_BIKE1 = build_scenario(
    city="Town03",
    start=[69, -132, 8],
    end=[104, -132, 8],
    vehicles=1,
    pedestrians=0,
    max_steps=300,
    weathers=[0])

# Simple scenario for Town01 that involves driving down a road
DEFAULT_SCENARIO_TOWN1 = build_ma_scenario(
    city="Town01",
    vehicles={"vehicle1": {
        "start": 128,
        "end": 133
    }},
    pedestrians={},
    max_steps=2000,
    weathers=[0])

DEFAULT_SCENARIO_TOWN1_2 = build_ma_scenario(
    city="Town01",
    vehicles={"vehicle1": {
        "start": 133,
        "end": 65
    }},
    pedestrians={},
    max_steps=2000,
    weathers=[0])

DEFAULT_SCENARIO_TOWN1_COMBINED = build_ma_scenario(
    city="Town01",
    vehicles={
        "vehicle1": {
            "start": [
                217.50997924804688, 198.75999450683594, 39.430625915527344,
                -0.16
            ],
            "end": [
                299.39996337890625, 199.05999755859375, 39.430625915527344,
                -0.16
            ]
        },
        "vehicle2": {
            "start": 133,
            "end": 65
        }
    },
    pedestrians={},
    max_steps=2000,
    weathers=[0])

DEFAULT_SCENARIO_TOWN1_COMBINED_WITH_MANUAL = build_ma_scenario(
    city="Town01",
    vehicles={
        "vehicle1": {
            "start": [
                217.50997924804688, 198.75999450683594, 39.430625915527344,
                -0.16
            ],
            "end": [
                299.39996337890625, 199.05999755859375, 39.430625915527344,
                -0.16
            ]
        },
        "vehicle2": {
            "start": 133,
            "end": 65
        },
        "manual": {
            "start": [
                299.39996337890625, 194.75999450683594, 39.430625915527344,
                180.0
            ],
            "end": [
                217.50997924804688, 194.05999755859375, 39.430625915527344,
                180.0
            ]
        },
    },
    pedestrians={},
    max_steps=2000,
    weathers=[0])

DEFAULT_SCENARIO_TOWN2 = build_scenario(
    city="Town01",
    start=[47],
    end=[52],
    vehicles=20,
    pedestrians=40,
    max_steps=200,
    weathers=[0])

DEFAULT_CURVE_TOWN1 = build_scenario(
    city="Town01",
    start=[133],
    end=[150],
    vehicles=20,
    pedestrians=40,
    max_steps=200,
    weathers=[0])

# Simple scenario for Town02 that involves driving down a road
LANE_KEEP_TOWN2 = build_scenario(
    city="Town02",
    start=36,
    end=40,
    vehicles=0,
    pedestrians=0,
    max_steps=2000,
    weathers=[0])

# Simple scenario for Town01 that involves driving down a road
LANE_KEEP_TOWN1 = build_scenario(
    city="Town01",
    start=36,
    end=40,
    vehicles=0,
    pedestrians=0,
    max_steps=2000,
    weathers=[0])

CURVE_TOWN1 = build_scenario(
    city="Town01",
    start=[131, 133],
    end=[65, 64],
    vehicles=0,
    pedestrians=0,
    max_steps=2000,
    weathers=[0])
CURVE_TOWN2 = build_scenario(
    city="Town01",
    start=[16, 27],
    end=[74, 75],
    vehicles=0,
    pedestrians=0,
    max_steps=2000,
    weathers=[0])

# Scenarios from the CoRL2017 paper
POSES_TOWN1_STRAIGHT = [[[9, 8], [1, 0]], [[142, 148], [141, 147]],
                        [[114, 115], [110, 111]], [[7, 6], [3, 2]],
                        [[4, 5], [149, 150]]]
# POSES_TOWN1_STRAIGHT = [
#    [36, 40], [39, 35], [110, 114], [7, 3], [0, 4],
#    [68, 50], [61, 59], [47, 64], [147, 90], [33, 87],
#    [26, 19], [80, 76], [45, 49], [55, 44], [29, 107],
#    [95, 104], [84, 34], [53, 67], [22, 17], [91, 148],
#    [20, 107], [78, 70], [95, 102], [68, 44], [45, 69]]

POSES_TOWN1_ONE_CURVE = [[138, 17], [47, 16], [26, 9], [42, 49], [140, 124],
                         [85, 98], [65, 133], [137, 51], [76, 66], [46, 39],
                         [40, 60], [0, 29], [4, 129], [121, 140], [2, 129],
                         [78, 44], [68, 85], [41, 102], [95, 70], [68, 129],
                         [84, 69], [47, 79], [110, 15], [130, 17], [0, 17]]

POSES_TOWN1_NAV = [[105, 29], [27, 130], [102, 87], [132, 27], [24, 44],
                   [96, 26], [34, 67], [28, 1], [140, 134], [105,
                                                             9], [148, 129],
                   [65, 18], [21, 16], [147, 97], [42, 51], [30, 41],
                   [18, 107], [69, 45], [102, 95], [18, 145], [111, 64],
                   [79, 45], [84, 69], [73, 31], [37, 81]]

POSES_TOWN2_STRAIGHT = [[38, 34], [4, 2], [12, 10], [62, 55], [43, 47],
                        [64, 66], [78, 76], [59, 57], [61, 18], [35, 39],
                        [12, 8], [0, 18], [75, 68], [54, 60], [45,
                                                               49], [46, 42],
                        [53, 46], [80, 29], [65, 63], [0, 81], [54, 63],
                        [51, 42], [16, 19], [17, 26], [77, 68]]

POSES_TOWN2_ONE_CURVE = [[37, 76], [8, 24], [60, 69], [38, 10], [21, 1],
                         [58, 71], [74, 32], [44, 0], [71, 16], [14, 24],
                         [34, 11], [43, 14], [75, 16], [80, 21], [3, 23],
                         [75, 59], [50, 47], [11, 19], [77, 34], [79, 25],
                         [40, 63], [58, 76], [79, 55], [16, 61], [27, 11]]

POSES_TOWN2_NAV = [[19, 66], [79, 14], [19, 57], [23, 1], [53, 76], [42, 13],
                   [31, 71], [33, 5], [54, 30], [10, 61], [66, 3], [27, 12],
                   [79, 19], [2, 29], [16, 14], [5, 57], [70, 73], [46, 67],
                   [57, 50], [61, 49], [21, 12], [51, 81], [77, 68], [56, 65],
                   [43, 54]]

TOWN1_STRAIGHT = [
    build_scenario("Town01", start, end, 0, 0, 300, TEST_WEATHERS)
    for (start, end) in POSES_TOWN1_STRAIGHT
]

TOWN1_ONE_CURVE = [
    build_scenario("Town01", start, end, 0, 0, 600, TEST_WEATHERS)
    for (start, end) in POSES_TOWN1_ONE_CURVE
]

TOWN1_NAVIGATION = [
    build_scenario("Town01", start, end, 0, 0, 900, TEST_WEATHERS)
    for (start, end) in POSES_TOWN1_NAV
]

TOWN1_NAVIGATION_DYNAMIC = [
    build_scenario("Town01", start, end, 20, 50, 900, TEST_WEATHERS)
    for (start, end) in POSES_TOWN1_NAV
]

TOWN2_STRAIGHT = [
    build_scenario("Town02", start, end, 0, 0, 300, TRAIN_WEATHERS)
    for (start, end) in POSES_TOWN2_STRAIGHT
]

TOWN2_STRAIGHT_DYNAMIC = [
    build_scenario("Town02", start, end, 20, 50, 300, TRAIN_WEATHERS)
    for (start, end) in POSES_TOWN2_STRAIGHT
]

TOWN2_ONE_CURVE = [
    build_scenario("Town02", start, end, 0, 0, 600, TRAIN_WEATHERS)
    for (start, end) in POSES_TOWN2_ONE_CURVE
]

TOWN2_NAVIGATION = [
    build_scenario("Town02", start, end, 0, 0, 900, TRAIN_WEATHERS)
    for (start, end) in POSES_TOWN2_NAV
]

TOWN2_NAVIGATION_DYNAMIC = [
    build_scenario("Town02", start, end, 20, 50, 900, TRAIN_WEATHERS)
    for (start, end) in POSES_TOWN2_NAV
]

TOWN1_ALL = (TOWN1_STRAIGHT + TOWN1_ONE_CURVE + TOWN1_NAVIGATION +
             TOWN1_NAVIGATION_DYNAMIC)

TOWN2_ALL = (TOWN2_STRAIGHT + TOWN2_ONE_CURVE + TOWN2_NAVIGATION +
             TOWN2_NAVIGATION_DYNAMIC)

local_map = locals()


def update_scenarios_parameter(config_map):
    if "scenarios" in config_map:
        config_map["scenarios"] = local_map[config_map["scenarios"]]
    return config_map


def get_scenario_parameter(scenario_name):
    if scenario_name in local_map:
        return local_map[scenario_name]
    else:
        return None
