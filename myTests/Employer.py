from PhysicalPerson import PhysicalPerson


class Employer(PhysicalPerson):
    def __init__(self, name, cpf, birthday, rg, vaccinationStatus, monthlyIncome, jobRole):
        self.monthlyIncome = monthlyIncome
        self.jobRole = jobRole
