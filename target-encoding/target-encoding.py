def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    category_sums = {}
    category_counts = {}

    for cat, target in zip(categories, targets):
        if cat not in category_sums:
            category_sums[cat] = 0.0
            category_counts[cat] = 0
        category_sums[cat] += target
        category_counts[cat] += 1

    category_means = {
        cat: category_sums[cat] / category_counts[cat] 
        for cat in category_sums
    }
    
    return [category_means[cat] for cat in categories]
    pass