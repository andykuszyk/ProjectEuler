import abc

class ProblemBase:
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def GetAttempts(this):
		return

	def Run(this):
		print "Please choose from the following attempts to run:"
		for attempt in this.GetAttempts().keys():
			print attempt
		attemptSelection = input("Attempt to run: ")
		this.RunAttempt(attemptSelection)	

	def RunAttempt(this, attemptNumber):
		this.GetAttempts()[attemptNumber]()
