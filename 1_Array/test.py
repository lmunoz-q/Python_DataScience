def rgb(r, g, b):
	"""
	Print in this format "FFFFFF"

	Args:
		r (int): red value
		g (int): green value
		b (int): blue value

	Returns:
		nothing
	"""
	r = hex(r)[2:].upper()
	g = hex(g)[2:].upper()
	b = hex(b)[2:].upper()
	print(f"{r:0>2}{g:0>2}{b:0>2}")