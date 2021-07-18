from random import gauss
from math import sin, cos
import os
import shutil
import unittest
import tempfile

from canvas import Canvas


class CavasTestes(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.folder)

    def test_canvas(self):

        gaussian = [gauss(0, 1) for i in range(1000)]
        filename = os.path.join(self.folder, "img1.png")
        Canvas("My First Image").hist(gaussian).save(filename)

        spiral = [(x * cos(0.1 * x), x * sin(0.1 * x)) for x in range(0, 300)]
        filename = os.path.join(self.folder, "img2.png")
        Canvas("My Second Image").plot(spiral).save(filename)

        points = [(x, x + gauss(0, 1), 0.5) for x in range(20)]
        filename = os.path.join(self.folder, "img1.png")
        Canvas("My Third Image").errorbar(points).plot(points).save(filename)

        blobs = [(gauss(0, 1), gauss(0, 1), 0.01, 0.01) for i in range(100)]
        filename = os.path.join(self.folder, "img1.png")
        Canvas("My Fourth Image").ellipses(blobs).save(filename)

        waves = [
            [sin(0.1 * x) * cos(0.1 * x * y) for x in range(20)] for y in range(20)
        ]
        filename = os.path.join(self.folder, "img1.png")
        Canvas("My Fifth Image").imshow(waves).save(filename)
