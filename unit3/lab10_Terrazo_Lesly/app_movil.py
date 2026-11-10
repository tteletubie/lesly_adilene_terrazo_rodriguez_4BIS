class AppMovilError(Exception):
    pass


class SuscripcionExpiradaError(AppMovilError):
    # It will be launched when a user tries to a function
    # without an active subscription
    pass


class PuntosInsuficientesError(AppMovilError):
    pass


class PerfilMovil:
    def __init__(
        self,
        username: str,
        gemas: int = 50,
        racha_dias: int = 1,
        notificaciones_activas: bool = True,
    ):
        self.username = username
        self.gemas = gemas
        self.racha_dias = racha_dias
        self.notificaciones_activas = notificaciones_activas

    @property
    def gemas(self) -> int:
        return self._gemas

    @gemas.setter
    def gemas(self, valor: int) -> None:
        if not isinstance(valor, int) or isinstance(valor, bool):
            raise ValueError("gemas must be an integer")
        if valor < 0:
            raise ValueError("gemas cannot be negative")
        self._gemas = valor

    @staticmethod
    def _validar_cantidad(cantidad: int) -> None:
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise ValueError("cantidad must be an integer")
        if cantidad <= 0:
            raise ValueError("cantidad must be strictly positive")

    def ganar_gemas(self, cantidad: int) -> int:
        self._validar_cantidad(cantidad)
        self.gemas += cantidad
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:
        self._validar_cantidad(cantidad)
        if cantidad > self.gemas:
            raise PuntosInsuficientesError(
                f"Tried to spend {cantidad} gems but only {self.gemas} available"
            )
        self.gemas -= cantidad
        return self.gemas


class PerfilPro(PerfilMovil):
    def __init__(
        self,
        username: str,
        meses_suscripcion: int,
        gemas: int = 50,
        racha_dias: int = 1,
        notificaciones_activas: bool = True,
    ):
        if (
            not isinstance(meses_suscripcion, int)
            or isinstance(meses_suscripcion, bool)
            or meses_suscripcion <= 0
        ):
            raise ValueError("meses_suscripcion must be greater than zero")
        super().__init__(username, gemas, racha_dias, notificaciones_activas)
        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def consumir_mes(self) -> int:
        if self.meses_suscripcion > 0:
            self.meses_suscripcion -= 1
        return self.meses_suscripcion

    def descargar_contenido_offline(self) -> str:
        if self.meses_suscripcion <= 0 or not self.es_pro:
            self.es_pro = False
            raise SuscripcionExpiradaError(f"{self.username}: subscription expired")
        return f"Offline content downloaded successfully for {self.username}"
