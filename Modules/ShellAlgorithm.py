import math

class ShellAlgorithm(object):
	def __init__(self):
		pass



	def calThirdCircleCord(self, circleST, circleED, radiusRD):
		x1 = circleST[0]
		y1 = circleST[1]
		r1 = circleST[2]
		x2 = circleED[0]
		y2 = circleED[1]
		r2 = circleED[2]
		C = r1 + r2
		B = r1 + radiusRD
		A = r2 + radiusRD

		x3 = y3 = r3 = 0

		cosA = (C*C + B*B - C*C) / (2 * B * C)
		width = x2 - x1
		if width > 0:
			degreeAm = acos((x2 - x1) / C)
		else:
			degreeAm = math.pi - acos((x2 - x2)) / C)