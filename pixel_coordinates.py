import logging
import numpy as np

def check_args(img_dim, corner_pts):
    """ Check all the arguments for make_grid

    Parameters
    ----------
    img_dim : Tuple
        Height and width of the image
    corner_pts : List of Tuples
        Contains 4 corner points (x, y)

    Returns
    -------
    bool
        Whether check passed or not
    """
    logging.basicConfig(format='%(name)s: %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    if type(img_dim) != tuple:
        logger.error(f"Expected img_dim to be a tuple, got {type(img_dim)}")
        return False
    elif len(img_dim) != 2:
        logger.error(f"Expected length of img_dim to be 2, got {len(img_dim)}")
        return False
    elif type(img_dim[0]) != int or type(img_dim[1]) != int:
        logger.error("Expected height and width to be integers")
        return False
    elif img_dim[0] < 2 or img_dim[1] < 2:
        logger.error("Expected height and width greater than or equal to 2")
        return False
    
    if type(corner_pts) != list:
        logger.error(f"Expected corner_pts to be a list, got {type(corner_pts)}")
        return False
    elif len(corner_pts) != 4:
        logger.error(f"Expected length of corner_pts to be 4, got {len(corner_pts)}")
        return False
    elif not all(isinstance(pt, tuple) for pt in corner_pts):
        logger.error("Expected all elements of corner_pts to be tuple")
        return False
    elif not all(len(pt) == 2 for pt in corner_pts):
        logger.error("Expected length of all elements in corner_pt to be 2")
        return False
    return True

def make_grid(img_dim, corner_pts):
    """Returns all the points on a grid

    Parameters
    ----------
    img_dim : Tuple
        Height and width of the image
    corner_pts : List of Tuples
        Contains 4 corner points (x, y)

    Returns
    -------
    grid : List
        List of all evenly spaced points on the grid
    """
    if not check_args(img_dim, corner_pts):
        return []

    height, width = img_dim
    corner_pts = np.asarray(corner_pts, dtype=float)

    # Find boundary of the rectangle
    x_min, x_max = corner_pts[:, 0].min(), corner_pts[:, 0].max()
    y_min, y_max = corner_pts[:, 1].min(), corner_pts[:, 1].max()

    # Get all possible x and y values for the grid, evenly spaced
    x = np.linspace(start=x_min, stop=x_max, num=width)
    y = np.linspace(start=y_min, stop=y_max, num=height)

    # Meshgrid to return all possible points
    grid_x, grid_y = np.meshgrid(x, y[::-1]) # Reverse y to have points in order
    grid = np.array((grid_x.ravel(), grid_y.ravel())).T # Flatten and combine x and y coords

    grid = grid.reshape(height, width, 2) # Get the desired shape
    grid = grid.tolist() # Convert to list

    return grid # Return list of list of points

# Check Implementation
if __name__ == "__main__":
    corner_points = [
        (1.5, 1.5),
        (4.0, 1.5),
        (1.5, 8.0),  
        (4.0, 8.0)
        ]
    
    img_dim = (3, 3)

    print(make_grid(img_dim, corner_points))