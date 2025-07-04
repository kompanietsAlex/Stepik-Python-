class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = self._verify_model_str(model)
        self._mass = self._verify_num(mass)
        self._speed = self._verify_num(speed)
        self._top = self._verify_num(top)

    def _verify_model_str(self, arg):
        if type(arg) != str:
            raise TypeError('неверный тип аргумента')
        return arg

    def _verify_num(self, arg):
        if not isinstance(arg, (float, int)) or arg < 0:
            raise TypeError('неверный тип аргумента')
        return arg

class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = self._verify_chairs(chairs)

    def _verify_chairs(self, arg):
        if not isinstance(arg, int) or arg < 0:
            raise TypeError('неверный тип аргумента')
        return arg

class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self.weapons = self._verify_weapons(weapons)

    def _verify_weapons(self, arg):
        if not isinstance(arg, dict):
            raise TypeError('неверный тип аргумента')
        return arg

planes = [PassengerAircraft("МС-21", 1250, 8000, 12000.5, 140),
          PassengerAircraft("SuperJet", 1145, 8640, 11034, 80),
          WarPlane("Миг-35", 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane("Су-35", 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]