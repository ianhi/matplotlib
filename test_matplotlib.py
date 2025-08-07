#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def test_matplotlib():
    print('✅ matplotlib imported successfully')
    print('matplotlib version:', matplotlib.__version__)
    print('backend:', matplotlib.get_backend())

    # Test basic plotting functionality
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y)
    ax.set_title('Test Plot')
    print('✅ Basic plotting works')

    # Save to verify it's working
    plt.savefig('/tmp/test_plot.png', dpi=50)
    print('✅ Plot saved successfully')

    print('🎉 matplotlib build from pixi is fully working!')

if __name__ == '__main__':
    test_matplotlib()