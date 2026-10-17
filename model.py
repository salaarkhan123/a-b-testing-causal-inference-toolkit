"""
A/B Testing & Causal Inference Toolkit

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - standard_normal_cdf
import math
import numpy as np

def standard_normal_cdf(z):
    erf_values = np.vectorize(math.erf)(z / math.sqrt(2))
    cdf = (1 + erf_values) * 0.5
    return cdf

