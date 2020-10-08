#!/usr/bin/env python3

import builder.Rbuilder
from builder.interface import WalkingRobot, AutonomusAerialPicking, AutonomusMetalDetector

b = WalkingRobot()
b.build_movement()
b.build_detection_sm()
print(b.get_product().__str__())

c = AutonomusAerialPicking()
c.build_movement()
c.build_detection_sm()
print(c.get_product().__str__())

d = AutonomusMetalDetector()
d.build_movement()
d.build_detection_sm()
print(d.get_product().__str__())
