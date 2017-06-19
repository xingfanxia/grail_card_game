class Card:
    def __init__(self, element_type, card_type):
        self.element_type = element_type
        self.card_type = card_type

class Attack_Card(Card):

    def __init__(self, element_type):
        self.exSpells = []
        self.card_type = "Attack"
        self.attack_type = self.element_type = element_type
        self.dmg = 2 #damage
        if self.attack_type == "wind":
            self.name = "风神斩"
        elif self.attack_type == "fire":
            self.name = "火焰斩"
        elif self.attack_type == "water":
            self.name = "水涟斩"
        elif self.attack_type == "elec":
            self.name = "雷光斩"
        elif self.attack_type == "earth":
            self.name = "地裂斩"
        elif self.attack_type == "dark":
            self.name = "黯灭"

    def descriptor(self):
        return self.name

    def associate_exSpells(self, spell):
        if len(self.exSpells) < 2:
            self.exSpells.append(spell)
            return True
        else:
            return False

    def attach_exSpells(self, spells):
        self.exSpells.extend(spells)

    def show_exSpells(self):
        return self.exSpells

class Magic_Card(Card):
    def __init__(self, element_type, magic_type):
        self.card_type = "Magic"
        self.element_type = element_type
        self.magic_type = magic_type
        if self.magic_type == "invincible":
            self.name = "别搞我（圣光）"
        elif self.magic_type == "exhaust":
            self.name = "虚弱"
        elif self.magic_type == "shield":
            self.name = "圣盾"
        elif self.magic_type == "boom":
            self.name = "魔弹"
        elif self.magic_type == "poison":
            self.name = "毒一哈"

    def descriptor(self):
        return self.name

def main():
    wind_1 = Attack_Card("wind")
    wind_1.associate_exSpells("别搞我")
    print(wind_1.descriptor())
    print(wind_1.show_exSpells())
if __name__ == '__main__':
    main()