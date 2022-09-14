import heapq


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        
        fuelMissed = [] # we will save the gas we can get
        
        fuel = startFuel
        numOfStops = 0
        i = 0
        
        while fuel < target:
            
            while i < len(stations) and fuel >= stations[i][0]:
                heapq.heappush(fuelMissed, -stations[i][1])
                i += 1
                
            if not fuelMissed:
                return -1
            
            fuel += -heapq.heappop(fuelMissed)
            numOfStops += 1
    
        return numOfStops


target = 1
startFuel = 1
stations = []
expected = 0
print("Solution {} - Expected {}".format(Solution.minRefuelStops(Solution,target,startFuel,stations),expected))

target = 100
startFuel = 1
stations = [[10, 100]]
expected = -1
print("Solution {} - Expected {}".format(Solution.minRefuelStops(Solution,target,startFuel,stations),expected))

target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]
expected = 2
print("Solution {} - Expected {}".format(Solution.minRefuelStops(Solution,target,startFuel,stations),expected))

target = 100
startFuel = 50
stations = [[25,50],[50,25]]
expected = 1
print("Solution {} - Expected {}".format(Solution.minRefuelStops(Solution,target,startFuel,stations),expected))

target = 1000
startFuel = 83
stations = [[15,457],[156,194],[160,156],[230,314],[390,159],[621,20],[642,123],[679,301],[739,229],[751,174]]
expected = 3
print("Solution {} - Expected {}".format(Solution.minRefuelStops(Solution,target,startFuel,stations),expected))

target = 1000
startFuel = 83
stations = [[47,220],[65,1],[98,113],[126,196],[186,218],[320,205],[686,317],[707,325],[754,104],[781,105]]
expected = 4
print("Solution {} - Expected {}".format(Solution.minRefuelStops(Solution,target,startFuel,stations),expected))
