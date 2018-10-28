

class Academic_institutions(object):

    def __init__(self,academic_id,academic_name):
        self.academic_id = academic_id
        self.academic_name = academic_name


    def __str__(self):
        return ("Academic id: "+self.academic_id+", Academic name: "+self.academic_name)
