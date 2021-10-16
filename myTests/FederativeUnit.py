class FederativeUnit:
    def __init__(self, stateName, region, acronym):
        self.stateName = stateName
        self.region = region
        self.acronym = acronym

    def __str__(self):
        return f'{self.stateName} ({self.acronym}), {self.region}'

    def isRegionNorthwest(self):
        if(self.region == 'Nordeste'):
            return 'Nordestino é um povo arretado'
        else:
            return 'Vocês são um povo legal'
