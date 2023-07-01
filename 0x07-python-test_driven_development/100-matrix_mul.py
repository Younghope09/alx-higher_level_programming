#!/usr/bin/python3
"""
Return a multiplying matrix function
"""


def matrix_mul(m_a, m_b):
    """
    function that divides all elements of a matrix.
    arguments: m_a, m_b
    returns a multiplied matrix of m_a and m_b
    """

    multiplied_matrix = []

    if not (isinstance(m_a, list)):
        raise TypeError("m_a must be a list")
    if not (isinstance(m_b, list)):
        raise TypeError("m_b must be a list")
    
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if (m_a == [] or m_a == [[]]):
        raise ValueError("m_a can't be empty")
    if (m_b == [] or m_b == [[]]):
        raise ValueError("m_b can't be empty")
    
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")
    
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")
    
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    inverting_m_b = []
    for row in range(len(m_b[0])):
        generated_row = []
        for column in range(len(m_b)):
            generated_row.append(m_b[column][row])
        inverting_m_b.append(generated_row)

    for row in m_a:
        generated_row = []
        for column in inverting_m_b:
            multiplication = 0
            for i in range(len(inverting_m_b[0])):
                multiplication += row[i] * column[i]
            generated_row.append(multiplication)
        multiplied_matrix.append(generated_row)

    return multiplied_matrix
