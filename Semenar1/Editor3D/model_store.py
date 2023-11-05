from .service import Point3D, Angle3D, Color


class Texture:
    pass


class Polygon:
    points: Point3D = []


class PolygonalModel:
    textures: [Texture]
    polygons: [Polygon]


    def __init__(self, textures: list[Texture]):
        self.textures = textures
        self.polygons = []


class Flash:
    location: Point3D
    angle: Angle3D
    color: Color
    power: float

    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass


class Camera:  
    location: Point3D
    angle: Angle3D

    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass


class Scene:
    
    id: int
    models: list[PolygonalModel]
    flashes: list[Flash]
    cameras: list[Camera]
   
    def __init__(self, id, models: list[PolygonalModel], flashes: list[Flash], cameras: list[Camera]):
        self.id_ = id
        self.models = models
        self.flashes = flashes
        self.cameras = cameras



    def method1(flash):
        pass

    def method2(model, flash):
        pass