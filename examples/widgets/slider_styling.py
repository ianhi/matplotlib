"""
==========================================
Slider customization and styling reference
==========================================

This example demonstrates different ways to style the appearance of Sliders,
as well as how to have the Slider snap to discrete values.

See :doc:`/gallery/widgets/slider_demo` for an example of using
a ``Slider`` to control the parameter to a line.

See :doc:`/gallery/widgets/range_slider` for an example of using
a ``RangeSlider`` to define a range of values.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig = plt.figure(figsize=(8, 6))

x = 0.2
slider_length = 0.6
slider_width = 0.03

ax0 = fig.add_axes([x, 0.9, slider_length, slider_width])
slider0 = Slider(
    ax0,
    label="Unmodified",
    valmin=0,
    valmax=1,
)

# Removing the line marking the initial position
ax1 = fig.add_axes([x, 0.8, slider_length, slider_width])
slider1 = Slider(
    ax1,
    label="No init line",
    valmin=0,
    valmax=1,
    initcolor="none",  # Set color to 'none' to make invisible
)


# to modify the color of the lefthand rectangle use **kwargs
# as these are all passed on to `ax.ax{v,h}span` which
# generates a Polygon patch.
ax2 = fig.add_axes([x, 0.7, slider_length, slider_width])
slider2 = Slider(
    ax2,
    label="Lefthand rectangle",
    valmin=0,
    valmax=1,
    initcolor="none",
    facecolor="green",
)


# modifying the slider track and handle
ax3 = fig.add_axes([x, 0.6, slider_length, slider_width])
slider3 = Slider(
    ax3,
    label="Track and Handle",
    valmin=0,
    valmax=1,
    initcolor="none",
    handle_facecolor="black",
    handle_edgecolor="pink",
    handle_size=20,
    track_color="red",
)

# Formatting the readout
# The slider readout can be formatted using the *valfmt* argument
# This argument accepts %-style format strings
ax4 = fig.add_axes([x, 0.5, slider_length, slider_width])
slider4 = Slider(
    ax4,
    label="Formatting\nthe readout",
    valmin=0,
    valmax=1,
    valfmt="%.5f Units!",  # Show 5 digits after the dot
)

# Snapping the slider to discrete values in uniform steps
ax5 = fig.add_axes([x, 0.4, slider_length, slider_width])
slider5 = Slider(
    ax5,
    label="Value snapping\n(uniform)",
    valmin=0,
    valmax=1,
    valstep=0.1,
)

# Snapping the slider to discrete values in non-uniform steps
allowed_values = np.concatenate(
    [np.linspace(0.1, 0.5, 100), [0.6, 0.7, 0.8, 0.9]]
)

ax6 = fig.add_axes([x, 0.3, slider_length, slider_width])
slider6 = Slider(
    ax6,
    label="Value snapping\n(non-uniform)",
    valmin=0,
    valmax=1,
    valstep=allowed_values,
)


plt.show()

#############################################################################
#
# ------------
#
# References
# """"""""""
#
# The use of the following functions, methods, classes and modules is shown
# in this example:

import matplotlib

matplotlib.widgets.Slider
