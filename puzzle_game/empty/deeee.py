import numpy as np
#  Use scipy.stats because it includes the Erlang distribution
from scipy.stats import expon, erlang
import matplotlib.pyplot as plt
def lindley(m=55000, d = 5000):
’’’ Estimates waiting time with m customers, discarding the first d
Lindley approximation for waiting time in a M/G/1 queue
’’’
replications = 10
lindley = []
for rep in range(replications):
y = 0
SumY = 0
for i in range(1, d):
# Random number variable generation from scipy.stats
# shape = 0, rate =1, 1 value
a = expon.rvs(0, 1)
# rate = .8/3, shape = 3
x = erlang.rvs(3, scale = 0.8/3, size=1)
y = max(0, y + x - a)
for i in range(d, m):
a = expon.rvs(0, 1)
# rate = .8/3, shape = 3
x = erlang.rvs(3, scale = 0.8/3, size=1)
y = max(0, y + x - a)
SumY += y
result = SumY / (m - d)
lindley.append(result)
return lindley
Figure 4.14:  Simulation of the
M/G/
1 queue using Lindley’s equation.
18
CHAPTER 4.  SIMULATION PROGRAMMING WITH PYTHON
import csv
with open("lindley.csv"), "rb") as myFile:
lindleyout = csv.writer(myFile)
lindleyout.writerow("Waitingtime")
for row in result:
print row
for i in range(len(result)):
print ("%1d & %11.9f " % (i+1, result[i]))
print("average & %11.9f" % (mean(result)))
print("std dev & %11.9f" % (std(result)))
Figure 4.15:  Simulation of the
M/G/
1 queue using Lindley’s equation.
import SimPy.Simulation as Sim
import numpy as np
from scipy.stats import expon, erlang
from random import seed
class G:
maxTime = 55000.0    # minutes
warmuptime = 5000.0
timeReceptionist = 0.8  # mean, minutes
phases = 3
ARRint = 1.0      # mean, minutes
theseed = 99999
\textbf
Figure 4.16:  Declarations for the hospital simulation.
either from observational data or a simulation of the current system.  Statistical
comparison of alternatives is a topic of Chap. 8.
4.3.2  Event-based Simulation of the
M/G/
1
Queue
The simulation program consists of some global declarations (Fig. 4.16), declara-
tions (Fig. 4.17), the main program (Fig. 4.18), some event routines (Fig. 4.19),
running the simulation and reporting provided by SimPy.
This model will illustrate the
Process
,
Resource
,  and
Monitor
classes.
At a high level, here is what they do:
•
Process
objects are used to generate entities or to govern the behavior of
entities in the system.
•
Resource
objects including
Level
and
Store
are used to designate re-
4.3.  SIMULATING THE
M/G/
1
QUEUE
19
class Hospitalsim(Sim.Simulation):
def run(self, theseed):
np.random.seed(theseed)
self.receptionist = Sim.Resource(name="Reception", capacity=1,
unitName="Receptionist", monitored=True, sim=self)
s = Arrivals(’Source’, sim=self)
self.initialize()
self.activate(s, s.generate(meanTBA=G.ARRint,
resource=self.receptionist), at=0.0)
self.simulate(until=G.maxTime)
avgutilization = self.receptionist.actMon.timeAverage()[0]
avgwait = self.receptionist.waitMon.mean()
avgqueue = self.receptionist.waitMon.timeAverage()[0]
leftinqueue= mg1.receptionist.waitMon.yseries()[-1:][0]
return [avgwait, avgqueue, leftinqueue,avgutilization]
Figure 4.17:  Main program for the hospital simulation.
sources that are required by a
Process
over the course of the simulation.
Any  of  these  can  have  a
Process
utilizing  a  unit  of  resource,  or  there
could be
Process
in a queue waiting for a resource to be available.
–
A
Resource
has units that are required by a
Process
.
–
A
Level
is an undifferentiated item that can be taken or produced
by a
Process
.
–
A
Store
is an inventory of heterogeneous items where a
Process
will
require a specific type of item from the
Store
.
•
Monitor
objects  are  used  to  record  observations  so  that  they  may  be
analyzed later.  In particular,  a
Resource
can also have a
Monitor
to
observe
Process
that are utilizing or waiting in a queue to utilize a unit
of a
Resource
.
Figure 4.17 shows the declarations of the
Process
and
Resource
objects,
specifically:
self.receptionist = Sim.Resource(name="Reception", capacity=1,
unitName="Receptionist", monitored=True, sim=self)
s = Arrivals(’Source’, sim=self)
These  are  both  declared  within  the  Simulation  object
Hospitalsim
,  and
both specify that they are a part of the current simulation (
sim=self
).  While
these could be declared as a local variable, the
Resource
self.receptionist
is declared as part of the simulation object
self
.  When it is declared, it can
be  given  a
capacity
,  a
qtype
(queue  type,  FIFO,  LIFO,  or  priority),  if  it
