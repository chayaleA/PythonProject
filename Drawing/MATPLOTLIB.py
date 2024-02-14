import matplotlib.pyplot as plt

class matplotlib:
    @staticmethod
    def bar_plot(x, y, title="bar", xlable="x", ylable="y"):
        """
            Create a bar plot.
        """
        colors = ['skyblue', 'salmon', 'limegreen', 'gold', 'purple']
        plt.figure(figsize=(10, 6))
        bars = plt.bar(x, y, color=colors)
        plt.xlabel(xlable)
        plt.ylabel(ylable)
        plt.title(title)
        plt.xticks(rotation=45)
        plt.legend(bars, [xlable, ylable])
        plt.tight_layout()
        # plt.savefig("../Drawing/figure11.png")
        plt.show()

    @staticmethod
    def barh_plot(x, y, title="barh", xlable="x", ylable="y"):
        """
            Create a barh plot.
        """
        colors = ['skyblue', 'salmon', 'limegreen', 'gold', 'purple']
        plt.figure(figsize=(10, 6))
        bars = plt.barh(list(x), list(y), color=colors)
        plt.xlabel(xlable)
        plt.ylabel(ylable)
        plt.title(title)
        plt.xticks(rotation=45)
        plt.legend(bars, [xlable, ylable])
        plt.tight_layout()
        # plt.savefig("../Drawing/figure12.png")
        plt.show()

    @staticmethod
    def pie_plot(x, y, title="pie"):
        """
            Create a pie plot.
        """
        plt.figure(figsize=(10, 6))
        plt.pie(y, labels=x, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.axis('equal')
        # plt.savefig("../Drawing/figure13.png")
        plt.show()

    @staticmethod
    def scatter_plot(x, y, title="Scatter Plot", xlabel="X", ylabel="Y"):
        """
            Create a scatter plot.
        """
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, marker="o", color="red")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        # plt.savefig("../Drawing/figure14.png")
        plt.show()

    @staticmethod
    def line_plot(x, y, title="Line Plot", xlabel="X", ylabel="Y"):
        """
            Create a scatter plot.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, marker="o", color="red")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        # plt.savefig("../Drawing/figure15.png")
        plt.show()

    @staticmethod
    def violin_plot(data, title="Violin Plot", ylabel="Value"):
        """
            Create a violin plot.
        """
        plt.figure(figsize=(10, 6))
        plt.violinplot(data)
        plt.title(title)
        plt.ylabel(ylabel)
        # plt.savefig("../Drawing/figure16.png")
        plt.show()

    @staticmethod
    def fill_between_plot(x, y1, y2, title="Fill Between Plot", xlabel="X", ylabel="Y", save_path=None):
        """
            Create a fill between plot.
        """
        plt.figure(figsize=(10, 6))
        plt.fill_between(x, y1, y2)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        if save_path:
            plt.savefig(save_path)
        # plt.savefig("../Drawing/figure17.png")
        plt.show()

    @staticmethod
    def histogram(data, bins=10, title="Histogram", xlabel="Value", ylabel="Frequency"):
        """
            Create a histogram.
        """
        plt.figure(figsize=(10, 6))
        plt.hist(data, bins=bins)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        # plt.savefig("../Drawing/figure18.png")
        plt.show()