#!/usr/bin/env python3
from abc import ABCMeta, abstractmethod
from builder.Rbuilder import *



class RobotBuilder(metaclass=ABCMeta):
    @abstractmethod
    def reset(self):
        pass
    @abstractmethod
    def build_movement(self):
        pass
    @abstractmethod
    def build_detection_sm(self):
        pass
#................................................................................................
class WalkingRobot(RobotBuilder):
    def __init__(self):
        self.product = Robot()
    def reset(self):
        self.product = Robot()
    def get_product(self):
        return self.product
    def build_movement(self):
        self.product.bipedal = True
        self.product.movement.append(BipedalLegs())
        self.product.movement.append(Arms())
    def build_detection_sm(self):
        self.product.detection_sm.append(CameraDetectionSystem())
#......................................................................................
class AutonomusMetalDetector(RobotBuilder):
    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    def get_product(self):
        return self.product

    def build_movement(self):
        self.product.quadrapedal = True
        self.product.movement.append(FourWheels())


    def build_detection_sm(self):
        self.product.detection_sm.append(InfraredDetectionSystem())
#.............................................................................................
class AutonomusAerialPicking(RobotBuilder):
    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    def get_product(self):
        return self.product

    def build_movement(self):
        self.product.flying = True
        self.product.movement.append(Wings())


    def build_detection_sm(self):
        self.product.detection_sm.append(SonarWaveDetectionSystem())


def main():
    b= WalkingRobot()
    b.build_movement()
    b.build_detection_sm()
    print(b.get_product().__str__())
if __name__ == "__main__":
    main()
