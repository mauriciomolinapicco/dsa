class Solution(object):

    def carFleet(self, target, position, speed):
        arrivals = []
        result = 0

        position, speed = zip(*sorted(zip(position, speed), key=lambda x: x[0]))

        n = len(position)
        for i in range(n):
            to_go = target - position[i]
            steps = to_go / float(speed[i])
            arrivals.append(steps)

        arrivals = arrivals[::-1]
        current = 0
        for i in range(n):
            if arrivals[i] > current: 
                result += 1
                current = arrivals[i]
                
        return result