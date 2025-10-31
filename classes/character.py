class Character:
    def __init__(self, name, dext, strn, body, intl, will, mind, infl, aura, spir, max_initiative, max_hero_points, **kwargs):
        self.name = name
        self.dext = dext
        self.strn = strn
        self.body = body
        self.intl = intl
        self.will = will
        self.mind = mind
        self.infl = infl
        self.aura = aura
        self.spir = spir
        self.max_initiative = max_initiative
        self.cur_initiative = max_initiative
        self.max_hero_points = max_hero_points
        self.cur_hero_points = max_hero_points