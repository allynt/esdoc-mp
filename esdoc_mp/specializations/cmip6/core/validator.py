from model import Specialization



s = Specialization()

# print s.__dict__

for r in s.realms:
	# print r.__dict__

	for p in r.processes:
		print p.__dict__
		break

