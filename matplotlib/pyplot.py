class DummyPlt:
    def __init__(self):
        self._saved = []

    def figure(self, figsize=(6, 4)):
        return self

    def hist(self, data, bins=10):
        # no-op in stub
        return None

    def title(self, t):
        self._title = t

    def tight_layout(self):
        pass

    def savefig(self, path):
        # create an empty file to simulate saving
        with open(path, "wb") as f:
            f.write(b"")

# Provide module-level API
plt = DummyPlt()


def figure(*args, **kwargs):
    return plt.figure(*args, **kwargs)


def hist(*args, **kwargs):
    return plt.hist(*args, **kwargs)


def title(*args, **kwargs):
    return plt.title(*args, **kwargs)


def tight_layout(*args, **kwargs):
    return plt.tight_layout(*args, **kwargs)


def savefig(*args, **kwargs):
    return plt.savefig(*args, **kwargs)
