import pytest
from main import calcular_area_triangulo


def test_calcular_area_triangulo():
    # Resultado obtenido (real)
    actual_result = calcular_area_triangulo(13, 6)

    # Resultado esperado
    # assert (estamos asegurando o verificando) que el 'actual result' sea igual que el 'expected result'
    assert actual_result == pytest.approx(19.5, abs=0.01)
