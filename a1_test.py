import numpy as np
import torch
import torch.nn as nn
import unittest

import a1

class TestBasic(unittest.TestCase):
    def test_light_pixels(self):
        image = np.array([[[250,   2,   2], [  0,   2, 255], [  0,   0, 255]], \
                          [[  2,   2,  20], [250, 255, 255], [127, 127, 127]]])
        self.assertEqual(a1.light_pixels(image, 200, 'red'), 2)
        self.assertEqual(a1.light_pixels(image, 200, 'green'), 1)
        self.assertEqual(a1.light_pixels(image, 200, 'blue'), 3)
 


if __name__ == "__main__":
    unittest.main()

