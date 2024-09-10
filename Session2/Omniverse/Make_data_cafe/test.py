import omni.replicator.core as rep
import random
import datetime
now = datetime.datetime.now()

base_path = "C:/Users/User/Desktop/For_simulate"
base_path_DLI = "/home/user/Downloads"

# TODO: Set the path to the USDZ files
Basket_URL = base_path + "/Basket.usdz"
Cafe_URL = base_path + "/cafe_interior.usdz"

Objects = {}
Objects["Beer_URL"] = base_path + "/Beer_Bottle.usdz"
Objects["Beer2_URL"] = base_path + "/alcohol.usdz"
Objects["Can_URL"] = base_path + "/Can.usdz"
Objects["Coffe_URL"] = base_path + "/Coffee_Cup.usdz"
Objects["Hot_S_URL"] = base_path + "/Hot_Sauce_Bottle.usdz"

Objects_Property = {}
Objects_Property["Beer_URL"] = {
    "scale": 0.002,
    "minx": None, "maxx": None,
    "miny": None, "maxy": None,
    "minz": None, "maxz": None
}
Objects_Property["Beer2_URL"] = {
    "scale": 0.002,
    "minx": None, "maxx": None,
    "miny": None, "maxy": None,
    "minz": None, "maxz": None
}
Objects_Property["Can_URL"] = {
    "scale": 0.001,
    "minx": -85, "maxx": 110,
    "miny": None, "maxy": None,
    "minz": None, "maxz": None
}
Objects_Property["Coffe_URL"] = {
    "scale": 0.0009,
    "minx": None, "maxx": None,
    "miny": None, "maxy": None,
    "minz": None, "maxz": None
}
Objects_Property["Hot_S_URL"] = {
    "scale": 0.01,
    "minx": None, "maxx": None,
    "miny": None, "maxy": None,
    "minz": None, "maxz": None
}

"""
Pos1min = (0.77716, 1.3078, 6.05963)
Pos1max = (-0.72546, 1.3078, 5.01738)
Pos2min = (0.76, 1.3078, 4.7477)
Pos2max = (-0.72546, 1.3078, 3.74684)
"""

# Create a new authoring layer context.
with rep.new_layer():
    
    # Cam
    camera = rep.create.camera(
        position=(1.5, 5.5, -1.6),
        look_at=(0.085, 1.38, 3.62)
    )

    """
    Beer = rep.create.from_usd(Beer_URL)
    with Beer:
        rep.modify.pose(
            position=(0.03334, 1.30783, 4.68313),
            rotation=(0.0, -90.0, 0.0),
            scale=0.002
        )

    Can = rep.create.from_usd(Can_URL)
    with Can:
        rep.modify.pose(
            position=(0.03334, 1.24204, 4.1),
            rotation=(11.4, 26.9, 39.4),
            scale=0.001
        )
    """

    # 테이블 위에
    def get_props1(object_name, one_in_n_chance=3):
        my_object = rep.create.from_usd(Objects[object_name])
        with my_object:
            rep.physics.collider()
            rep.modify.pose(
                position=rep.distribution.uniform(
                    (-0.72546, 1.5078, 3.74684),
                    (0.77716, 1.6078, 4.7477)
                ),
                rotation=rep.distribution.uniform(
                    (-180,-180, -180),
                    (180, 180, 180)
                ),
                scale=rep.distribution.uniform(
                    (Objects_Property[object_name]["scale"]),
                    (Objects_Property[object_name]["scale"])
                )
            )
            rep.modify.visibility(rep.distribution.choice([True],[False]*(one_in_n_chance)))
        return my_object.node

    # 바구니 안에에
    def get_props2(object_name, one_in_n_chance=3):
        my_object = rep.create.from_usd(Objects[object_name])
        with my_object:
            rep.physics.collider()
            rep.modify.pose(
                position=rep.distribution.uniform(
                    (-0.21, 0.31, 2.9),
                    (0.33, 0.82, 3.47)
                ),
                rotation=rep.distribution.uniform(
                    (-180,-180, -180),
                    (180, 180, 180)
                ),
                scale=rep.distribution.uniform(
                    (Objects_Property[object_name]["scale"]),
                    (Objects_Property[object_name]["scale"])
                )
            )
            rep.modify.visibility(rep.distribution.choice([True],[False]*(one_in_n_chance)))
        return my_object.node

    # 랜덤 조명
    def sphere_lights(num):
        lights = rep.create.light(
            light_type="Sphere",
            temperature=rep.distribution.normal(3000, 500),
            intensity=rep.distribution.normal(30000, 1000),
            position=rep.distribution.uniform((-300, -300, -300), (300, 300, 300)),
            scale=rep.distribution.uniform(50, 100),
            count=num        )
        return lights.node

    # BG
    cafe = rep.create.from_usd(Cafe_URL)
    with cafe:
        rep.modify.pose(
            position=(0.0, 0.0, 0.0),
            rotation=(0.0, 0.0, 0.0),
            scale=0.02
        )
        rep.physics.collider() 

    # BackGround
    Basket = rep.create.from_usd(Basket_URL)
    with Basket:
        rep.physics.collider()
        rep.physics.mass(mass=100)
        rep.modify.pose(
            position=(0.06628, 0.47819, 3.09413),
            rotation=(0.0, -90.0, 0.0),
            scale=0.005
        )

    sphereLight1 = rep.create.light(
        position=(-10.0271, 3.02127, 4.96921),
        rotation=(0.0, 0.0, 0.0),
        intensity=100000,
        light_type="sphere"
    )

    sphereLight2 = rep.create.light(
        position=(-5.07079, 3.09849, 4.96921),
        rotation=(0.0, 0.0, 0.0),
        intensity=100000,
        light_type="sphere"
    )

    sphereLight3 = rep.create.light(
        position=(-0.03847, 3.09849, 4.96921),
        rotation=(0.0, 0.0, 0.0),
        intensity=100000,
        light_type="sphere"
    )

    sphereLight4 = rep.create.light(
        position=(5.02058, 3.02127, 4.96921),
        rotation=(0.0, 0.0, 0.0),
        intensity=100000,
        light_type="sphere"
    )

    sphereLight5 = rep.create.light(
        position=(10.00023, 3.02127, 4.96921),
        rotation=(0.0, 0.0, 0.0),
        intensity=100000,
        light_type="sphere"
    )

    rep.randomizer.register(get_props1)
    rep.randomizer.register(get_props2)
    rep.randomizer.register(sphere_lights)

    num_frames = 100

    # 기존 카메라 위치 = (1.5, 5.5, -1.6)
    with rep.trigger.on_frame(num_frames=num_frames):
        with camera: # 카메라 랜덤!
            rep.modify.pose(position=rep.distribution.uniform((1, 2.5, -3.6), (1.6, 5.6, -1.5)), look_at=(0.085, 1.38, 3.62))
        rep.modify.timeline(5, "frame")
        for n in list(Objects.keys()):
            get_props1(n,15)
            get_props2(n,30)
        rep.randomizer.sphere_lights(5)

    # 렌더 제품 생성
    render_product = rep.create.render_product(camera, (1024, 1024))

    # from os.path import expanduser
    # home = expanduser("~")

    # writer 정의 및 초기화
    writer = rep.WriterRegistry.get("BasicWriter")

    # now=now.strftime("%Y-%m-%d_%H:%M:%S")
    # output_dir = home+"/Documents/fruit_data_"+now
    
    writer.initialize(
        output_dir=base_path + "/OutPut/",
        rgb=True,
        bounding_box_2d_tight=True
        # TODO: Select your preferred data types
    )

    # writer에 렌더 제품 연결
    writer.attach([render_product])

    # Replicator 실행
    rep.orchestrator.run()
