def calculate_discount(age_group, claims_history, policy_type):
    rules = {
        ("Under 25", "None", "Standard"): 10,
        ("25-65", "None", "Premium"): 20,
        ("25-65", "One", "Standard"): 5,
        ("Over 65", "2+", "Premium"): 0,
    }

    key = (age_group, claims_history, policy_type)

    if key not in rules:
        raise ValueError("No decision-table rule defined")

    return rules[key]