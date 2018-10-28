

class Professions(object):

    def __init__(self,profession_id,profession_name):
        self.profession_id = profession_id
        self.profession_name = profession_name

    def __str__(self):
        return ( "Profession id: "+self.profession_id+", Profession name: "+self.profession_name)