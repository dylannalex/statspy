import numpy as np
from collections import Counter
from matplotlib import pyplot as plt
from tools import number


class FrequencyChart:

    LABELS = ("xi", "fi", "fri", "Fi", "Fri")
    LABEL_BACKROUND_COLOR = "#BFBFBF"
    DATA_BACKGROUND_COLOR = "#E6E6E6"

    def __init__(self, x):
        print(x)
        self.x = sorted(x)
        self.x_counter = Counter(self.x)

    @property
    def xi(self):
        return list(self.x_counter.keys())

    @property
    def fi(self):
        return [self.x_counter[x_i] for x_i in self.xi]

    @property
    def fri(self):
        return [f_i / len(self.x) for f_i in self.fi]

    @property
    def Fi(self):
        fi_reversed = self.fi[::-1]
        return [sum(fi_reversed[i:]) for i in range(len(fi_reversed) - 1, -1, -1)]

    @property
    def Fri(self):
        return [F_i / len(self.x) for F_i in self.Fi]

    @property
    def text(self):
        rows = len(self.xi)
        text = []
        for row in range(rows):
            text.append(
                [
                    number.truncate(self.xi[row], 2),
                    number.truncate(self.fi[row], 2),
                    number.truncate(self.fri[row], 2),
                    number.truncate(self.Fi[row], 2),
                    number.truncate(self.Fri[row], 2),
                ]
            )
        return text

    @property
    def col_colors(self):
        return [
            FrequencyChart.LABEL_BACKROUND_COLOR
            for _ in FrequencyChart.LABEL_BACKROUND_COLOR
        ]

    def draw(self):
        fig, ax = plt.subplots()
        ax.axis("tight")
        ax.axis("off")
        plt.table(
            cellText=self.text,
            colLabels=FrequencyChart.LABELS,
            colColours=self.col_colors,
            loc="center",
        )
        plt.show()


class Ogive:
    COLOR = "#7461A8"
    MARKER = "o"
    LINE_TYPE = "-"
    FRI_YLABEL = "Relative Cumulative Frequency (Fri)"
    FI_YLABEL = "Cumulative Frequency (Fi)"

    def __init__(self, class_interval, cumulative_frequency, x_label=None):
        self.class_interval = class_interval
        self.Fi = cumulative_frequency
        self.class_interval_length = class_interval[1] - class_interval[0]
        self.x_label = x_label

    @property
    def Fri(self):
        observations = self.Fi[-1]
        return [cf / observations for cf in self.Fi]

    def draw(self, relative_cumulative_frequency=True):
        plt.plot(
            self.class_interval[1:],
            self.Fri if relative_cumulative_frequency else self.Fi,
            color=Ogive.COLOR,
            marker=Ogive.MARKER,
            linestyle=Ogive.LINE_TYPE,
        )
        plt.xticks(
            np.arange(
                self.class_interval[1],
                self.class_interval[-1] + self.class_interval_length,
                self.class_interval_length,
            )
        )
        if self.x_label:
            plt.xlabel(self.x_label)
        if relative_cumulative_frequency:
            plt.ylabel(Ogive.FRI_YLABEL)
        else:
            plt.ylabel(Ogive.FI_YLABEL)

        plt.show()
