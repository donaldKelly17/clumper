class Clumper:
    """
    This object adds methods to a list of dictionaries that make
    it nicer to explore.

    Usage:
    ```python
    from clumper import Clumper

    list_dicts = [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}]

    c = Clumper(list_dicts)
    assert len(c) == 4
    ```
    """

    def __init__(self, blob):
        self.blob = blob

    def __len__(self):
        return len(self.blob)

    def keep(self, *funcs):
        """
        Allows you to select which items to keep and which items to remove.

        ![](../img/keep.png)

        Arguments:
            funcs: functions that indicate which items to keep

        Usage:
        ```python
        from clumper import Clumper

        list_dicts = [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}]

        clump = Clumper(list_dicts).keep(lambda d: d['a'] >= 3)
        expected = [{'a': 3}, {'a': 4}]
        assert clump.equals(expected)
        ```
        """
        data = self.blob
        for func in funcs:
            data = [d for d in data if func(d)]
        return Clumper(data)

    def head(self, n=5):
        """
        Selects the top `n` items from the collection.

        ![](../img/head.png)

        Arguments:
            n: the number of items to grab

        Usage:
        ```python
        from clumper import Clumper

        list_dicts = [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}]

        result = Clumper(list_dicts).head(2)
        expected = [{'a': 1}, {'a': 2}]

        assert result.equals(expected)
        ```
        """
        if not isinstance(n, int):
            raise ValueError(f"`n` must be a positive integer, got {n}")
        if n < 0:
            raise ValueError(f"`n` must be a positive integer, got {n}")
        n = min(n, len(self))
        return Clumper([self.blob[i] for i in range(n)])

    def tail(self, n):
        """
        Selects the bottom `n` items from the collection.
        ![](../img/tail.png)

        Arguments:
            n: the number of items to grab

        Usage:
        ```python
        from clumper import Clumper

        list_dicts = [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}]

        result = Clumper(list_dicts).tail(2)
        expected = [{'a': 3}, {'a': 4}]

        assert result.equals(expected)
        ```
        """
        if not isinstance(n, int):
            raise ValueError(f"`n` must be a positive integer, got {n}")
        if n < 0:
            raise ValueError(f"`n` must be positive, got {n}")
        n = min(n, len(self))
        return Clumper([self.blob[-i] for i in range(1, n + 1)])

    def select(self, *keys):
        """
        Selects a subset of the keys in each item in the collection.

        ![](../img/select.png)

        Arguments:
            keys: the keys to keep

        Usage:
        ```python
        from clumper import Clumper

        list_dicts = [
            {'a': 1, 'b': 2},
            {'a': 2, 'b': 3, 'c':4},
            {'a': 1, 'b': 6}]

        clump = Clumper(list_dicts).select('a', 'b')

        assert all(["c" not in d.keys() for d in clump])
        ```
        """
        return Clumper([{k: d[k] for k in keys} for d in self.blob])

    def mutate(self, **kwargs):
        data = self.blob
        for key, func in kwargs.items():
            for i in range(len(data)):
                data[i][key] = func(data[i])
        return Clumper(data)

    def sort(self, key, reverse=False):
        return Clumper(sorted(self.blob, key=key, reverse=reverse))

    def collect(self):
        """
        Returns a list instead of a `Clumper` object.

        ![](../img/collect.png)
        """
        return self.blob
