class School:
    def __init__(self, name, roster = {}):
        self.name = name
        self.roster = roster

    def add_student (self,full_name, grade):
        if grade not in self.roster.keys():
            self.roster.update({grade:[full_name]})
        else:
            self.roster.update({grade: self.roster[grade]+[full_name]})

    def grade(self,grade):
        return self.roster[grade]

    def sort_roster(self):
        for key in self.roster.keys():
            self.roster[key] = sorted(self.roster[key])
        return self.roster



