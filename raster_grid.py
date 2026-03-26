# The `RasterGrid` represents a structured, rectangular grid in 2d space.
# Each cell of the grid is identified by its column/row index pair:
#
#  ________ ________ ________
# |        |        |        |
# | (0, 1) | (1, 1) | (2, 2) |
# |________|________|________|
# |        |        |        |
# | (0, 0) | (1, 0) | (2, 0) |
# |________|________|________|
#
#
# One can construct a `RasterGrid` by specifying the lower left and upper right
# corners of a domain and the number of cells one wants to use in x- and y-directions.
# Then, `RasterGrid` allows to iterate over all cells and retrieve the center point
# of that cell.
#
# This class can be significantly cleaned up, though. Give it a try, and if you need
# help you may look into the file `raster_grid_hints.py`.
# Make sure to make small changes, verifying that the test still passes, and put
# each small change into a separate commit.
from typing import Tuple
from math import isclose
from dataclasses import dataclass


class RasterGrid:
    @dataclass
    class Cell:
        ix: int
        iy: int

    def __init__(self,
                 lower_left_x: float,
                 lower_left_y: float,
                 upper_right_x: float,
                 upper_right_y: float,
                 number_of_cells_in_x_direction: int,
                 number_of_cells_in_y_direction: int) -> None:
        self._lower_left_x = lower_left_x
        self._lower_left_y = lower_left_y
        self._upper_right_x = upper_right_x
        self._upper_right_y = upper_right_y
        self._number_of_cells_in_x_direction = number_of_cells_in_x_direction
        self._number_of_cells_in_y_direction = number_of_cells_in_y_direction
        
    def __len__(self) -> int:
        return self._number_of_cells_in_x_direction * self._number_of_cells_in_y_direction
    
    def __iter__(self):
        return iter(self.Cell(i, j) for i in range(self._number_of_cells_in_x_direction) for j in range(self._number_of_cells_in_y_direction))

    def compute_center_point_of_cell(self, cell: Cell) -> Tuple[float, float]:
        return (
            self._lower_left_x + (float(cell.ix) + 0.5)*(self._upper_right_x - self._lower_left_x)/self._number_of_cells_in_x_direction,
            self._lower_left_y + (float(cell.iy) + 0.5)*(self._upper_right_y - self._lower_left_y)/self._number_of_cells_in_y_direction
        )


def test_number_of_cells():
    x0 = 0.0
    y0 = 0.0
    dx = 1.0
    dy = 1.0
    assert len(RasterGrid(x0, y0, dx, dy, 10, 10)) == 100
    assert len(RasterGrid(x0, y0, dx, dy, 10, 20)) == 200
    assert len(RasterGrid(x0, y0, dx, dy, 20, 10)) == 200
    assert len(RasterGrid(x0, y0, dx, dy, 20, 20)) == 400


def test_cell_center():
    grid = RasterGrid(0.0, 0.0, 2.0, 2.0, 2, 2)
    expected_centers = {
        (0.5, 0.5),
        (1.5, 0.5),
        (0.5, 1.5),
        (1.5, 1.5)
    }

    for cell in grid:
        centers = {grid.compute_center_point_of_cell(cell) for cell in grid}
        assert centers == expected_centers


if __name__ == "__main__":
    test_number_of_cells()
    test_cell_center()
    print("All tests passed")
