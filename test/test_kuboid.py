import kuboid
import pytest

def test_kira_kuboid():
    isipadu = kuboid.kira_kuboid(3, 4, 6)
    assert isipadu == 72.0

def test_cetak_kuboid(monkeypatch, capsys):
    # Define a function to simulate multiple user inputs
    user_inputs = ["3.4", "4.5", "6.7"]

    def mock_input(_):
        return user_inputs.pop(0)

    # Use the function to simulate user input
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the main function, which uses input() and prints the result
    kuboid.cetak_kuboid()

    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == "Isipadu kuboid = 102.51"