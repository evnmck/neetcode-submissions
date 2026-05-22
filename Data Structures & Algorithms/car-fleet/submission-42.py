class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        for i in range(len(cars)):
            
            pos, sp = cars[i]
            time = (target - pos) / sp 
            '''
            if time in front is greater dont do anything
            if time in front is smaller add this time
            '''

            if not res or time > res[-1]:
                res.append(time)

        return len(res) 