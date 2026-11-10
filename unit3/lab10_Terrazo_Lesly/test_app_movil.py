import pytest
from app_movil import (
    PerfilMovil,
    PerfilPro,
    PuntosInsuficientesError,
    SuscripcionExpiradaError,
)


@pytest.fixture
def perfil():
    return PerfilMovil("ana")


@pytest.fixture
def perfil_pro():
    return PerfilPro("beto", meses_suscripcion=3)


def test_atributos_iniciales(perfil):
    assert perfil.username == "ana"
    assert perfil.gemas == 50
    assert perfil.racha_dias == 1
    assert perfil.notificaciones_activas is True


def test_ganar_gemas_suma_y_retorna_balance(perfil):
    assert perfil.ganar_gemas(25) == 75
    assert perfil.gemas == 75


def test_gastar_gemas_resta_y_retorna_balance(perfil):
    assert perfil.gastar_gemas(20) == 30
    assert perfil.gemas == 30


def test_ganar_y_gastar_son_consistentes(perfil):
    perfil.ganar_gemas(30)
    perfil.gastar_gemas(30)
    assert perfil.gemas == 50


def test_gastar_todo_el_balance_deja_cero(perfil):
    assert perfil.gastar_gemas(50) == 0


def test_instancias_estan_aisladas(perfil):
    assert perfil.gemas == 50


def test_gemas_iniciales_negativas_lanzan_value_error():
    with pytest.raises(ValueError):
        PerfilMovil("ana", gemas=-1)


def test_asignar_gemas_negativas_lanza_value_error(perfil):
    with pytest.raises(ValueError):
        perfil.gemas = -10


def test_gastar_mas_de_lo_disponible_lanza_puntos_insuficientes(perfil):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(51)


def test_balance_no_cambia_si_la_transaccion_falla(perfil):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(999)
    assert perfil.gemas == 50


def test_perfil_pro_con_meses_cero_lanza_value_error():
    with pytest.raises(ValueError):
        PerfilPro("beto", meses_suscripcion=0)


def test_perfil_pro_con_meses_negativos_lanza_value_error():
    with pytest.raises(ValueError):
        PerfilPro("beto", meses_suscripcion=-2)


def test_descargar_con_suscripcion_expirada_lanza_error(perfil_pro):
    perfil_pro.meses_suscripcion = 0
    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()


@pytest.mark.parametrize(
    "cantidad, esperado",
    [
        (1, 51),
        (10, 60),
        (50, 100),
        (1000, 1050),
    ],
)
def test_ganar_gemas_valores_validos(perfil, cantidad, esperado):
    assert perfil.ganar_gemas(cantidad) == esperado


@pytest.mark.parametrize("cantidad", [0, -1, -50, -1000])
def test_ganar_gemas_valores_invalidos(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.ganar_gemas(cantidad)


@pytest.mark.parametrize("cantidad", [0, -1, -50])
def test_gastar_gemas_valores_no_positivos(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.gastar_gemas(cantidad)


@pytest.mark.parametrize(
    "cantidad, esperado",
    [(1, 49), (49, 1), (50, 0)],
)
def test_gastar_gemas_limites_validos(perfil, cantidad, esperado):
    assert perfil.gastar_gemas(cantidad) == esperado


@pytest.mark.parametrize("cantidad", [51, 100, 10_000])
def test_gastar_gemas_por_encima_del_balance(perfil, cantidad):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(cantidad)


def test_perfil_pro_hereda_de_perfil_movil(perfil_pro):
    assert isinstance(perfil_pro, PerfilPro)
    assert isinstance(perfil_pro, PerfilMovil)
    assert issubclass(PerfilPro, PerfilMovil)


def test_perfil_movil_no_es_perfil_pro(perfil):
    assert not isinstance(perfil, PerfilPro)


def test_perfil_pro_hereda_atributos_y_metodos(perfil_pro):
    assert perfil_pro.gemas == 50
    assert perfil_pro.ganar_gemas(10) == 60
    assert perfil_pro.gastar_gemas(60) == 0


def test_perfil_pro_atributos_propios(perfil_pro):
    assert perfil_pro.meses_suscripcion == 3
    assert perfil_pro.es_pro is True


def test_descargar_contenido_con_suscripcion_activa(perfil_pro):
    resultado = perfil_pro.descargar_contenido_offline()
    assert isinstance(resultado, str)
    assert "successfully" in resultado
    assert perfil_pro.es_pro is True


def test_ciclo_de_vida_de_la_suscripcion(perfil_pro):
    perfil_pro.consumir_mes()
    perfil_pro.consumir_mes()
    assert perfil_pro.descargar_contenido_offline()
    perfil_pro.consumir_mes()
    assert perfil_pro.meses_suscripcion == 0

    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()
    assert perfil_pro.es_pro is False


def test_error_de_expiracion_es_una_excepcion():
    assert issubclass(SuscripcionExpiradaError, Exception)
    assert issubclass(PuntosInsuficientesError, Exception)
