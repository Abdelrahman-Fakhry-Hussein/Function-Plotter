import pytest
import function_plotter

@pytest.fixture
def test_plot(qtbot):
    # Create a new FunctionPlotter instance and add it to the qtbot widget registry
    plotter = function_plotter.FunctionPlotter()
    qtbot.addWidget(plotter)

    plotter.plot()
    return plotter


def test_valid_inputs1(test_plot):
    # Set the function, minimum, and maximum values
    print("Running test_valid_inputs...")
    test_plot.textbox.setText("x**2+cos(x)")
    test_plot.textbox1.setText("-5")
    test_plot.textbox2.setText("5")
    test_plot.plot()
    assert len(test_plot.figure.axes) == 1
    assert len(test_plot.figure.axes[0].lines) == 1
    print("test_valid_inputs passed.")

def test_valid_inputs2(test_plot):
    # Set the function, minimum, and maximum values
    print("Running test_valid_inputs...")
    test_plot.textbox.setText("6*log(x,10)+2*x*cos(x)+3*e^x")
    test_plot.textbox1.setText("5")
    test_plot.textbox2.setText("100")
    test_plot.plot()
    assert len(test_plot.figure.axes) == 1
    assert len(test_plot.figure.axes[0].lines) == 1
    print("test_valid_inputs passed.")

def test_invalid_function1(test_plot):
    print("Running test_invalid_function...")
    test_plot.textbox.setText("invalid function")
    test_plot.textbox1.setText("-5")
    test_plot.textbox2.setText("5")
    test_plot.plot()
    assert test_plot.error_label.text() == "Please Enter valid Function."
    print("test_invalid_function passed.")


def test_invalid_function2(test_plot):
    print("Running test_invalid_function...")
    test_plot.textbox.setText("x**2")
    test_plot.textbox1.setText("-5")
    test_plot.textbox2.setText("")
    test_plot.plot()
    assert test_plot.error_label.text() == "Please Enter Minimum and Maximum values of x."
    print("test_invalid_function passed.")

def test_invalid_function3(test_plot):
    print("Running test_invalid_function...")
    test_plot.textbox.setText("log hello")
    test_plot.textbox1.setText("-5")
    test_plot.textbox2.setText("100")
    test_plot.plot()
    assert test_plot.error_label.text() == "Please Enter valid Function."
    print("test_invalid_function passed.")

def test_invalid_function4(test_plot):
    print("Running test_invalid_function...")
    test_plot.textbox.setText("")
    test_plot.textbox1.setText("")
    test_plot.textbox2.setText("")
    test_plot.plot()
    assert test_plot.error_label.text() == "Please Enter valid Function."
    print("test_invalid_function passed.")