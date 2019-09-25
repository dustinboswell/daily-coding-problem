from collections import defaultdict

class AutoComplete:
    def __init__(self, queries):
        self.prefix_to_queries = defaultdict(list)
        for query in queries:
            for j in range(1, len(query)):
                self.prefix_to_queries[query[0:j]].append(query)

    def suggest(self, prefix):
        return self.prefix_to_queries.get(prefix, [])

ac = AutoComplete(["dog", "deer", "deal"])
assert sorted(ac.suggest("de")) == ["deal", "deer"]
assert sorted(ac.suggest("z")) == []
