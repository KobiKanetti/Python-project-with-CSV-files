

class Professions_in_academic(object):

    def __init__(self,profession_id,academic_id,organization_size):
        self.profession_id = profession_id
        self.academic_id = academic_id
        self.organization_size = organization_size

    def __str__(self):
        return ("Profession id: "+self.profession_id+", Academic id: "+
                self.academic_id+", Organization size: "+self.organization_size)

