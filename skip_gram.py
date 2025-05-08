def skip_grams(tokens, window_size=2):
    pairs = []
    for i, target in enumerate(tokens):
        for j in range(max(0, i - window_size), min(len(tokens), i + window_size + 1)):
            if i != j:
                pairs.append((target, tokens[j]))
    return pairs

tokens = ["Azərbaycan", "dili", "zəngin", "və", "ifadəli", "bir", "dildir", ",", "onu", "öyrənmək", "maraqlıdır", "."]
pairs = skip_grams(tokens, window_size=2)
for pair in pairs:
    print(pair)
