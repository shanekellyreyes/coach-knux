from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Point2D:
    x: float
    y: float


def distance_2d(a: Point2D, b: Point2D) -> float:
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def midpoint_2d(a: Point2D, b: Point2D) -> Point2D:
    return Point2D(x=(a.x + b.x) / 2.0, y=(a.y + b.y) / 2.0)


def angle_between_points(a: Point2D, b: Point2D, c: Point2D) -> float:
    ba_x = a.x - b.x
    ba_y = a.y - b.y
    bc_x = c.x - b.x
    bc_y = c.y - b.y

    dot = ba_x * bc_x + ba_y * bc_y
    mag_ba = math.sqrt(ba_x**2 + ba_y**2)
    mag_bc = math.sqrt(bc_x**2 + bc_y**2)

    if mag_ba == 0 or mag_bc == 0:
        return 0.0

    cosine = dot / (mag_ba * mag_bc)
    cosine = max(-1.0, min(1.0, cosine))

    return math.degrees(math.acos(cosine))


def slope_angle_degrees(a: Point2D, b: Point2D) -> float:
    return math.degrees(math.atan2(b.y - a.y, b.x - a.x))