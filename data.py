import hw3_tests



class CountyDemographics:
    # Initialize a new CountyDemographics object.
    # input: the county's age demographics data as a dictionary
    # input: the county's name as a string
    # input: the county's education demographics data as a dictionary
    # input: the county's ethnicities demographics data as a dictionary
    # input: the county's income demographics data as a dictionary
    # input: the county's population demographics data as a dictionary
    # input: the county's state as a string
    def __init__(self,
                  age: dict[str,float],
                  county: str,
                  education: dict[str,float],
                  ethnicities: dict[str,float],
                  income: dict[str,float],
                  population: dict[str,float],
                  state: str):
        self.age = age
        self.county = county
        self.education = education
        self.ethnicities = ethnicities
        self.income = income
        self.population = population
        self.state = state


    # Provide a developer-friendly string representation of the object.
    # input: CountyDemographics for which a string representation is desired. 
    # output: string representation
    def __repr__(self):
        return 'CountyDemographics({}, {}, {}, {}, {}, {}, {})'.format(
                self.age,
                self.county,
                self.education,
                self.ethnicities,
                self.income,
                self.population,
                self.state
            )

def population_total(listy: list[CountyDemographics]) -> int:
    totalpop = 0
    for x in listy:
       totalpop += x.population['2014 Population']
    return totalpop

def filter_by_state(listy: list[CountyDemographics], st: str) -> list[CountyDemographics]:
    filtered = []
    for x in listy:
        if x.state == st:
            filtered.append(x)
    return filtered

def population_by_education(listy: list[CountyDemographics])->int:
    totaleduc = 0
    for x in listy:
        try:
            totaleduc += (x.population["2014 Population"] * (x.education["Bachelor's Degree or Higher"] / 100))
        except KeyError:
            totaleduc += 0
    return int(totaleduc)

def population_by_ethnicity(listy: list[CountyDemographics], eth: str ) -> int:
    totaleth = 0
    for x in listy:
        try:
            totaleth += (x.population["2014 Population"] * (x.ethnicities[eth] / 100))
        except KeyError:
            totaleth += 0
    return int(totaleth)

def population_below_poverty(listy: list[CountyDemographics],) -> int:
    totalpov = 0
    for x in listy:
        try:
            totalpov += (x.population["2014 Population"] * (x.income['Persons Below Poverty Level'] / 100))
        except KeyError:
            totalpov += 0
    return int(totalpov)

def percent_by_education(listy: list[CountyDemographics]) -> float:
    totalpop = population_total(listy)
    totaledu = population_by_education(listy)
    totperc = (float(totaledu) / float(totalpop))*100
    return totperc

def percent_by_ethnicity(listy: list[CountyDemographics], eth: str) -> float:
    totalpop = population_total(listy)
    totaleth = population_by_ethnicity(listy, eth)
    totperc = (float(totaleth) / float(totalpop)) * 100
    return totperc

def percent_below_poverty_level(listy: list[CountyDemographics]) -> float:
    totalpop = population_total(listy)
    totalpov = population_below_poverty(listy)
    totperc = (float(totalpov) / float(totalpop)) * 100
    return totperc

def education_greater_than(listy: list[CountyDemographics], edu:str, num:float) -> list[CountyDemographics]:
    alist = []
    for coun in listy:
        if coun.education[edu] > num:
            alist.append(coun)
        else:
            pass
    return alist

def education_less_than(listy: list[CountyDemographics], edu:str, num:float) -> list[CountyDemographics]:
    alist = []
    for coun in listy:
        if coun.education[edu] < num:
            alist.append(coun)
        else:
            pass
    return alist

def ethnicity_greater_than(listy: list[CountyDemographics], eth:str, num:float) -> list[CountyDemographics]:
    blist = []
    for coun in listy:
        if coun.ethnicities[eth] > num:
            blist.append(coun)
        else:
            pass
    return blist

def ethnicity_less_than(listy: list[CountyDemographics], eth:str, num:float) -> list[CountyDemographics]:
    blist = []
    for coun in listy:
        if coun.ethnicities[eth] < num:
            blist.append(coun)
        else:
            pass
    return blist
def below_poverty_level_greater_than(listy: list[CountyDemographics], num: float) -> list[CountyDemographics]:
    clist=[]
    for coun in listy:
        if coun.income['Persons Below Poverty Level'] > num:
            clist.append(coun)
        else:
            pass
    return clist

def below_poverty_level_less_than(listy: list[CountyDemographics], num: float) -> list[CountyDemographics]:
    clist=[]
    for coun in listy:
        if coun.income['Persons Below Poverty Level'] < num:
            clist.append(coun)
        else:
            pass
    return clist
