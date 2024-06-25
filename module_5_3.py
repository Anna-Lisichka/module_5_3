class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


office_building = Building(18, "Монолит")
house = Building(18, 'Панельный')

print(office_building == house)

house.buildingType = 'Монолит'
print(office_building == house)
