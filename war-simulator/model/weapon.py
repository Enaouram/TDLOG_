from model.exceptions import NoAmmunitionError


class Weapon:
    def __init__(self, id, ammunitions: int, range: int):
        self.id = id
        self.ammunitions = ammunitions
        self.range = range

    def get_id(self) -> int:
        return self.id

    def fire_at(self, x, y, z):
        if self.ammunitions == 0:
            raise NoAmmunitionError("Vous n'avez plus de munitions !")

        self.check_target_position(x, y, z)

        self.ammunitions = self.ammunitions - 1

    def get_ammunitions(self):
        return self.ammunitions

    def get_range(self):
        return self.range

    def check_target_position(self, x, y, z):
        raise NotImplementedError("Vous n'avez pas encore choisi ma destination de votre projectile!")
