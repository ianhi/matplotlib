import os
import sys
import pytest
from unittest import mock

import matplotlib.pyplot as plt
from matplotlib.backends.backend_webagg_core import FigureCanvasWebAggCore

import matplotlib.backends.backend_webagg_core
from matplotlib.testing import subprocess_run_for_testing


@pytest.mark.parametrize("backend", ["webagg", "nbagg"])
def test_webagg_fallback(backend):
    pytest.importorskip("tornado")
    if backend == "nbagg":
        pytest.importorskip("IPython")
    env = dict(os.environ)
    if sys.platform != "win32":
        env["DISPLAY"] = ""

    env["MPLBACKEND"] = backend

    test_code = (
        "import os;"
        + f"assert os.environ['MPLBACKEND'] == '{backend}';"
        + "import matplotlib.pyplot as plt; "
        + "print(plt.get_backend());"
        f"assert '{backend}' == plt.get_backend().lower();"
    )
    subprocess_run_for_testing([sys.executable, "-c", test_code], env=env, check=True)


def test_webagg_core_no_toolbar():
    fm = matplotlib.backends.backend_webagg_core.FigureManagerWebAgg
    assert fm._toolbar2_class is None


def test_scroll_capture_functionality():
    """Test the scroll capture functionality in WebAgg backend."""
    pytest.importorskip("tornado")
    
    # Create a figure with WebAggCore canvas
    fig, ax = plt.subplots()
    canvas = FigureCanvasWebAggCore(fig)
    
    # Test initial state
    assert canvas.get_capture_scroll() is False
    assert canvas._capture_scroll is False
    
    # Mock send_event to verify it's called when setting capture_scroll
    with mock.patch.object(canvas, 'send_event') as mock_send:
        # Test enabling scroll capture
        canvas.set_capture_scroll(True)
        assert canvas.get_capture_scroll() is True
        assert canvas._capture_scroll is True
        mock_send.assert_called_with('capture_scroll', capture_scroll=True)
        
        # Test disabling scroll capture
        mock_send.reset_mock()
        canvas.set_capture_scroll(False)
        assert canvas.get_capture_scroll() is False
        assert canvas._capture_scroll is False
        mock_send.assert_called_with('capture_scroll', capture_scroll=False)
        
        # Test setting the same value doesn't trigger send_event
        mock_send.reset_mock()
        canvas.set_capture_scroll(False)
        mock_send.assert_not_called()


def test_scroll_capture_refresh_sends_state():
    """Test that capture_scroll state is sent during refresh."""
    pytest.importorskip("tornado")
    
    fig, ax = plt.subplots()
    canvas = FigureCanvasWebAggCore(fig)
    
    # Enable scroll capture
    canvas.set_capture_scroll(True)
    
    # Mock send_event to verify refresh sends capture_scroll state
    with mock.patch.object(canvas, 'send_event') as mock_send:
        # Simulate refresh event (like when a new client connects)
        canvas.handle_refresh({})
        
        # Check that capture_scroll was sent among other events
        capture_scroll_calls = [
            call for call in mock_send.call_args_list
            if call[0][0] == 'capture_scroll'
        ]
        assert len(capture_scroll_calls) == 1
        assert capture_scroll_calls[0] == mock.call('capture_scroll', capture_scroll=True)


