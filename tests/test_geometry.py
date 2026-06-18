import pytest

from coach_knux.biomechanics.geometry import (
    Point2D,
    angle_between_points,
    distance_2d,
    midpoint_2d,
    slope_angle_degrees,
)


def test_distance_2d():
    assert distance_2d(Point2D(0, 0), Point2D(3, 4)) == pytest.approx(5.0)


def test_midpoint_2d():
    assert midpoint_2d(Point2D(0, 0), Point2D(2, 4)) == Point2D(1, 2)


def test_angle_between_points_right_angle():
    assert angle_between_points(
        Point2D(0, 1),
        Point2D(0, 0),
        Point2D(1, 0),
    ) == pytest.approx(90.0)


def test_slope_angle_degrees_horizontal():
    assert slope_angle_degrees(Point2D(0, 0), Point2D(1, 0)) == pytest.approx(0.0)