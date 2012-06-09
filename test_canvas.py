#!/usr/bin/python
# -*- coding:Utf-8 -*-


import unittest
from random import gauss
from math import sin, cos
from canvas import Canvas


class MaTest(unittest.TestCase):
    def test_hist(self):
        gaussian = [gauss(0,1) for i in range(1000)]
        Canvas('My First Image').hist(gaussian).save('/dev/null')

    def test_plot(self):
        spiral = [(x*cos(0.1*x),x*sin(0.1*x)) for x in range(0,300)]
        Canvas('My Second Image').plot(spiral).save('/dev/null')

    def test_errorbar(self):
        points = [(x,x+gauss(0,1),0.5) for x in range(20)]
        Canvas('My Third Image').errorbar(points).plot(points).save('/dev/null')

    def test_ellipses(self):
        blobs = [(gauss(0,1),gauss(0,1),0.05,0.05) for i in range(100)]
        Canvas('My Fourth Image').ellipses(blobs).save('/dev/null')

    def test_imshow(self):
        waves = [[sin(0.1*x)*cos(0.1*x*y) for x in range(20)] for y in range(20)]
        Canvas('My Fifth Image').imshow(waves).save('/dev/null')


if __name__ == "__main__":
   unittest.main()
