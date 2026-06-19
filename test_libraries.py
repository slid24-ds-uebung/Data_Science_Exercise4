"""Zeigt, dass die Libraries aus dem Dockerfile installiert sind."""


def test_benoetigte_libraries_installiert():
    # Wenn ein Import fehlschlaegt, schlaegt der Test fehl.
    import numpy
    import pandas
    import matplotlib
    import seaborn

    assert numpy.__version__
    assert pandas.__version__
    assert matplotlib.__version__
    assert seaborn.__version__


def test_libraries_funktionieren_zusammen():
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")  # headless, kein Display noetig
    import matplotlib.pyplot as plt
    import seaborn as sns

    data = pd.DataFrame({"x": np.arange(5), "y": np.arange(5) ** 2})
    ax = sns.lineplot(data=data, x="x", y="y")
    assert ax is not None
    plt.close("all")