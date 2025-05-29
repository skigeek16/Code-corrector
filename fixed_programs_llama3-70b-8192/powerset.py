def powerset(arr):
    if arr:
        first, *rest = arr 
        rest_subsets = powerset(rest)
        return [subset for subset in rest_subsets] + [[first] + subset in rest_subsets]
    else:
        return [[]]