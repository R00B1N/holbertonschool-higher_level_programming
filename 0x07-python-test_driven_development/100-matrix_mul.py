#!/usr/bin/python3
"""
This module contains one function:
matrix_mul(m_a, m_b): -> returns the product of multiplication: a new matrix
"""


def matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices
    """
    msgT1 = "m_a must be a list"
    msgT2 = "m_b must be a list"
    msgL1 = "m_a must be a list of lists"
    msgL2 = "m_b must be a list of lists"
    msgE1 = "m_a can't be empty"
    msgE2 = "m_b can't be empty"
    msgI1 = "m_a should contain only integers or floats"
    msgI2 = "m_b should contain only integers or floats"
    msgR1 = "each row of m_a must be of the same size"
    msgR2 = "each row of m_b must be of the same size"
    msgMul = "m_a and m_b can't be multiplied"
    if type(m_a) is not list:
        raise TypeError(msgT1)
        return
    if type(m_b) is not list:
        raise TypeError(msgT2)
        return
    for i in m_a:
        if type(i) is not list:
            raise TypeError(msgL1)
            return
    for i in m_b:
        if type(i) is not list:
            raise TypeError(msgL2)
            return
    if m_a == [] or m_a == [[]]:
        raise ValueError(msgE1)
        return
    if m_b == [] or m_b == [[]]:
        raise ValueError(msgE2)
        return
    for i in m_a:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError(msgI1)
                return
    for i in m_b:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError(msgI2)
                return
    rect = len(m_a[0])
    for i in m_a:
        if len(i) is not rect:
            raise TypeError(msgR1)
            return
    rect = len(m_b[0])
    for i in m_b:
        if len(i) is not rect:
            raise TypeError(msgR2)
            return
    if len(m_a[0]) is not len(m_b):
        raise ValueError(msgMul)
        return
    product = []
    for i in range(0, len(m_a)):
        row = []
        for z in range(0, len(m_b[0])):
            somme = 0
            j = 0
            for x in m_a[i]:
                somme += x * m_b[j][z]
                j += 1
            row.append(somme)
        product.append(row)
    return product
