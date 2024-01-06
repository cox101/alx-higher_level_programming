#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy."""
    try:
        result = np.dot(m_a, m_b)
        return result.tolist()
    except ValueError as e:
        raise ValueError(f"NumPy Error: {e}")
