def fuzzy_union(a, b):
    elements = set(a.keys()) | set(b.keys())
    return {e: max(a.get(e, 0), b.get(e, 0)) for e in elements}

def fuzzy_intersection(a, b):
    elements = set(a.keys()) | set(b.keys())
    return {e: min(a.get(e, 0), b.get(e, 0)) for e in elements}

def fuzzy_complement(a):
    return {k: 1 - v for k, v in a.items()}

def fuzzy_difference(a, b):
    universe = set(a.keys()) | set(b.keys())
    return {e: min(a.get(e, 0), 1 - b.get(e, 0)) for e in universe}

def cartesian_product(a, b):
    product = {}
    for x in a:
        for y in b:
            product[(x, y)] = min(a[x], b[y])
    return product

def max_min_composition(r1, r2):
    composition = {}
    for (x, y1) in r1:
        for (y2, z) in r2:
            if y1 == y2:
                current_min = min(r1[(x, y1)], r2[(y2, z)])
                if (x, z) in composition:
                    if current_min > composition[(x, z)]:
                        composition[(x, z)] = current_min
                else:
                    composition[(x, z)] = current_min
    return composition

# Example usage
if __name__ == "__main__":
    # Example fuzzy sets
    A = {'x1': 0.2, 'x2': 0.5, 'x3': 0.9}
    B = {'x1': 0.6, 'x2': 0.4, 'x3': 0.7}
    print("Union:", fuzzy_union(A, B))
    print("Intersection:", fuzzy_intersection(A, B))
    print("Complement of A:", fuzzy_complement(A))
    print("Difference A - B:", fuzzy_difference(A, B))
    
    # Cartesian product example
    set1 = {'x': 0.5, 'y': 0.7}
    set2 = {'a': 0.3, 'b': 0.6}
    cart = cartesian_product(A, B)
    print("Cartesian product:", cart)
    
    # Max-min composition example
    R = {('x', 'a'): 0.5, ('x', 'b'): 0.7, ('y', 'a'): 0.8}
    S = {('a', 'm'): 0.3, ('a', 'n'): 0.6, ('b', 'm'): 0.9}
    comp = max_min_composition(R, S)
    print("Max-min composition:", comp)