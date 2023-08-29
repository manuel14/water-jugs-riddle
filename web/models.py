from .helpers import division_remainder


class Jug():
    """
    Represents a a jug object
    """

    def __init__(self, capacity: int, name: str) -> None:
        self.capacity = capacity
        self.name = name
        self.state = 0

    def fill(self) -> None:
        self.state = self.capacity

    def empty(self) -> None:
        self.state = 0


class Solution():
    """
    Class to represent the solution entity that holds the steps information
    """

    def __init__(self, j1: int, j2: int, z: int) -> None:
        self.j1 = j1
        self.j2 = j2
        self.z = z
        self.steps_j1 = []
        self.steps_j2 = []

    def minSteps(self):
        # time complexity is O(n) where n is the greater value between j1 and j2
        # space complexity O(n) where n is the length of steps
        j1 = self.j1
        j2 = self.j2
        if j2 > j1:
            temp = j2
            j2 = j1
            j1 = temp
        if (self.z % (division_remainder(j1, j2)) != 0):
            # if this condition is not met it means there is a division remainder between j1 and j1
            # that will be equal to z eventually, aka there is a solution possible
            return []
        self.steps_j1 = self._steps(Jug(capacity=self.j1, name="x"), Jug(
            capacity=self.j2, name="y"), self.z)
        self.steps_j2 = self._steps(Jug(capacity=self.j2, name="y"),
                                    Jug(capacity=self.j1, name="x"), self.z)
        # return most efficient solution
        if len(self.steps_j1) <= len(self.steps_j2):
            return self.steps_j1
        return self.steps_j2

    def _steps(self, toJugCap: Jug, fromJugCap: Jug, amountToMeassure: int):
        """
        This method pours water always from FromJugCap into toJugCap
        until one of the two jugs is equal to amountToMeassure
        """
        fromJugCap.fill()
        steps = []
        steps.append(
            {"operation": "fill",
             "jug": fromJugCap.name,
             "amount": fromJugCap.capacity,
             toJugCap.name: toJugCap.state,
             fromJugCap.name: fromJugCap.state
             }
        )
        while ((fromJugCap.state != amountToMeassure) and (toJugCap.state != amountToMeassure)):
            # this min assures recipient jug will never be transferred with more than it's capacity
            temp = min(fromJugCap.state, toJugCap.capacity - toJugCap.state)
            steps.append({"operation": "transfer", "from": fromJugCap.name, "amount": fromJugCap.state,
                          "to": toJugCap.name})
            toJugCap.state = toJugCap.state + temp
            fromJugCap.state = fromJugCap.state - temp
            steps[-1][fromJugCap.name] = fromJugCap.state
            steps[-1][toJugCap.name] = toJugCap.state
            if ((fromJugCap.state == amountToMeassure) or (toJugCap.state == amountToMeassure)):
                break
            # If fromJugCap is empty fill it
            if fromJugCap.state == 0:
                fromJugCap.fill()
                steps.append(
                    {"operation": "fill", "jug": fromJugCap.name, "amount": fromJugCap.capacity, toJugCap.name: toJugCap.state,
                     fromJugCap.name: fromJugCap.state})
            # If toJugCap is full empty it
            if toJugCap.state == toJugCap.capacity:
                toJugCap.empty()
                steps.append({"operation": "empty", "jug": toJugCap.name, toJugCap.name: toJugCap.state,
                              fromJugCap.name: fromJugCap.state})
        return steps
