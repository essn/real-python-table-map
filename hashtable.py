from typing import NamedTuple, Any


class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:
    def __init__(self, capacity):
        self._pairs = capacity * [None]

    @property
    def values(self):
        return [pair.value for pair in self.pairs]

    @property
    def pairs(self):
        return {pair for pair in self._pairs if pair}
    
    @property
    def keys(self):
        return {pair.key for pair in self.pairs}

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def _index(self, key):
        return hash(key) % len(self)

    def __delitem__(self, key):
        if key in self:
            self[key] = None
        else:
            raise KeyError(key)

    def __len__(self):
        return len(self._pairs)

    def __setitem__(self, key, value):
        self._pairs[self._index(key)] = Pair(key, value)

    def __getitem__(self, key):
        pair = self._pairs[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair.value

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True
