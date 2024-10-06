import numpy, random

def bezier_curve(x1, y1, x2, y2):
    """
    Returns a list of tuples in the form (x, y) that are positions along the curve
    """
    t_values = numpy.linspace(0, 1, 1000)
    positions = []
    
    control_1x, control_1y = random.randint(min(x1, x2), max(x1,x2)), random.randint(min(y1, y2), max(y1,y2))
    control_2x, control_2y = random.randint(min(x1, x2), max(x1,x2)), random.randint(min(y1, y2), max(y1,y2))

    prev_x, prev_y = x1, y1
    for t in t_values:
        # B(t) = (1-t)^3 * P0 + 3 * (1-t)^2 * t * P1 + 3*(1-t)^2 * P2 + t^3 * P3 (2 control points)
        x = (1 - t) ** 3 * x1 + 3 * (1 - t) ** 2 * t * control_1x + 3 * (1 - t) * t ** 2 * control_2x + t ** 3 * x2
        y = (1 - t) ** 3 * y1 + 3 * (1 - t) ** 2 * t * control_1y + 3 * (1 - t) * t ** 2 * control_2y + t ** 3 * y2
        x, y = int(round(x)), int(round(y))

        # Ensure same pixel isn't added twice
        if abs(x1-prev_x) + abs(y-prev_y):
            positions.append((x, y))
            prev_x, prev_y = x, y
    
    return positions
