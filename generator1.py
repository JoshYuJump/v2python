def generate_number(base_number):
	while True:
		base_number += 1
		if base_number < 10:
			yield base_number, 'test'


g = generate_number(5)
print g.next()
print g.next()
