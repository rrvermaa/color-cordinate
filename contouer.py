


# def interpolate_x(x1, y1, x2, y2, y):
#     x = x1 + ((y - y1) * (x2 - x1)) / (y2 - y1)
#     return x

# def calculate_slope(x1, y1, x2, y2):
#     slope = (y2 - y1) / (x2 - x1)
#     return slope



# x1 = 1659
# y1 = 434
# x2 = 2494
# y2 = 1286
# y = 0

# x_at_y0 = calculate_slope(x1, y1, x2, y2)
# print(x_at_y0)
 

slope = 1.0203592814371258
x1 = 2494
y1 = 1286

# Calculate y-intercept (b)
b = y1 - slope * x1

# Calculate x-coordinate where the line intersects Y = 0
x_at_y0 = (0 - b) / slope

print("x-coordinate where the line intersects Y = 0:", x_at_y0)