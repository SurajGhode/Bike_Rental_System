def find_synonym_groups(synonyms):
    groups = []
    visited = set()
    for syn_map in synonyms:
        for word1, word2 in syn_map.items():
            if word1 in visited or word2 in visited:
                continue
            group = [word1, word2]
            visited.add(word1)
            visited.add(word2)
            for syn_map2 in synonyms:
                for word3, word4 in syn_map2.items():
                    if word3 in group or word4 in group:
                        group.append(word3)
                        group.append(word4)
                        visited.add(word3)
                        visited.add(word4)
            groups.append(list(set(group)))
    return groups

synonyms = [{"Dg set": "Diesel generator"}, {"Organization": "Organisation"}, {"Group": "Organization"}, {"Orange": "Kinnu"}, {"Orange": "narangi"}]

print(find_synonym_groups(synonyms))
