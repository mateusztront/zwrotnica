class User:
    def __init__(self, mail, name, surname):
        self.mail = mail
        self.name = name
        self.surname = surname

    def say_hello(self):
        return "User %(name)s %(surname)s says hello." % {
            "name": self.name,
            "surname": self.surname
        }

class VIPUser(User):
    def __init__(self, mail, name, surname, _vip_card_number):
        self._vip_card_number = _vip_card_number if self._check_card(_vip_card_number) else None
        super().__init__(name=name, mail=mail, surname=surname)


    @staticmethod
    def _check_card(_vip_card_number):
        if _vip_card_number > 999 and _vip_card_number % 2 == 0:
            return True
        else:
            return False

    @staticmethod
    def use_vip_card():
        pass

    @property
    def vip_card_number(self):
        return self._vip_card_number

    @vip_card_number.setter
    def vip_card_number(self, vip_card_number):
        if self._check_card(vip_card_number):
            self._vip_card_number = vip_card_number
        else:
            raise ValueError("Incorrect vip number address.")

if __name__ == '__main__':
    user = VIPUser("Brajanusz", "Kowalski", "Kowalski@mail.pl", 1999)
    print(user.vip_card_number)
    user.vip_card_number = 9998
    print(user.vip_card_number)