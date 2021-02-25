import random
import matplotlib.pyplot as plt
import math


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Customers_to_be_Served:
    def __init__(self, time):
        self.Customer_arrival_time = time
        self.item = random.randrange(1, 11)

    def getTime(self):
        return self.Customer_arrival_time

    def getItem(self):
        return self.item

    def waitTime(self, Serve_Time):
        return Serve_Time - self.Customer_arrival_time


class Cashier_serving_Customer:
    def __init__(self, itemspm):
        self.rate = itemspm
        self.currentCustomer = None
        self.timeRemaining = 0

    def setIdle(self):
        if self.currentCustomer != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentCustomer = None

    def busy(self):
        if self.currentCustomer != None:
            return True
        else:
            return False

    def Next(self, newCustomer):
        self.currentCustomer = newCustomer
        self.timeRemaining = newCustomer.getItem() * 60 / self.rate


def new_Customer():
    Cust = random.randrange(1, 21)

    if Cust == 20:
        return True
    else:
        return False


def simulation(numSec, itemsPermin):
    restCashier = Cashier_serving_Customer(itemsPermin)
    waitingTimes = []
    q = Queue()

    for currentSec in range(numSec):

        if new_Customer():
            serving = Customers_to_be_Served(currentSec)
            q.enqueue(serving)

        if (not restCashier.busy()) and (not q.isEmpty()):
            nextCust = q.dequeue()
            waitingTimes.append(nextCust.waitTime(
                currentSec))
            restCashier.Next(nextCust)
        restCashier.setIdle()

    averageWaitingTime = sum(waitingTimes) / len(waitingTimes)

    return averageWaitingTime


def main():
    time_frame = 600

    maxTime = []
    minTime = []
    avgTime = []
    for itemsPerMinute in range(10, 51, 1):
        maxWaitTime = 0
        minWaitTime = math.inf

        totalWaitTime = 0
        for i in range(10):
            waitingTime = simulation(time_frame, itemsPerMinute)
            maxWaitTime = max(maxWaitTime, waitingTime)
            minWaitTime = min(minWaitTime, waitingTime)
            totalWaitTime += waitingTime
        maxTime.append(maxWaitTime)
        minTime.append(minWaitTime)
        avgTime.append(totalWaitTime / 10)
        print(
            "On running 10 simulations for time frame of 600 seconds and %d items per min (entered by the cashier):" % (
                itemsPerMinute))
        print("The maximum, minimum and the average case among those 10 simulation outputs are:")
        print("Maximum Average Waiting Time for the customer (in seconds) : %3.2f" % maxWaitTime)
        print("Minimum Average Waiting Time for the customer (in seconds)  : %10.10f " % minWaitTime)
        print("Average of all the outputs from 10 simulations (in seconds) : %3.2f" % (totalWaitTime / 10))
        print("\n")
    plt.plot(range(10, 51, 1), maxTime, label='Best case (Maximum) Average waiting time')
    plt.plot(range(10, 51, 1), avgTime, label='Average case for the simulation')
    plt.plot(range(10, 51, 1), minTime, label='Worst case (Minimum) Average waiting time')
    plt.legend(loc='upper right')
    # Plot labeling
    plt.xlabel('Items entered by the cashier per min')
    plt.ylabel('Average wait time for the customer (in sec)')
    plt.title("Plot visualizing the comparison between the best, average and worst case of simulation results")
    # 10 simulations every time on changing the number of items entered per min, for time frame of 600 seconds"
    plt.show()


if __name__ == "__main__":
    main()