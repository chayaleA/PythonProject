import penguins
import seaborn as sns
import matplotlib.pyplot as plt

class seaborn:
    @staticmethod
    def seaborn_line_plot(x, y, title="Line Plot", xlabel="X", ylabel="Y", color='blue', marker=None):
        sns.lineplot(x=x, y=y, color=color, marker=marker)
        plt.title(title, fontsize=16, color='navy')
        plt.xlabel(xlabel, fontsize=14, color='darkgreen')
        plt.ylabel(ylabel, fontsize=14, color='darkgreen')
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
        plt.show()

    @staticmethod
    def seaborn_scatter_plot(x, y, title="Scatter Plot", xlabel="X", ylabel="Y", color='red', marker='o'):
        sns.scatterplot(x=x, y=y, color=color, marker=marker)
        plt.title(title, fontsize=16, color='navy')
        plt.xlabel(xlabel, fontsize=14, color='darkgreen')
        plt.ylabel(ylabel, fontsize=14, color='darkgreen')
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
        plt.show()

    @staticmethod
    def seaborn_bar_plot(x, y, title="Bar Plot", xlabel="X", ylabel="Y", color='green'):
        sns.barplot(x=x, y=y, color=color)
        plt.title(title, fontsize=16, color='navy')
        plt.xlabel(xlabel, fontsize=14, color='darkgreen')
        plt.ylabel(ylabel, fontsize=14, color='darkgreen')
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
        plt.show()

    @staticmethod
    def seaborn_box_plot(x, y, title="Box Plot", xlabel="X", ylabel="Y", color='orange'):
        sns.boxplot(x=x, y=y, color=color)
        plt.title(title, fontsize=16, color='navy')
        plt.xlabel(xlabel, fontsize=14, color='darkgreen')
        plt.ylabel(ylabel, fontsize=14, color='darkgreen')
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
        plt.show()

    @staticmethod
    def seaborn_violin_plot(x, y, title="Violin Plot", xlabel="X", ylabel="Y", color='purple'):
        sns.violinplot(x=x, y=y, hue=y, palette='coolwarm')
        plt.title(title, fontsize=16, color='navy')
        plt.xlabel(xlabel, fontsize=14, color='darkgreen')
        plt.ylabel(ylabel, fontsize=14, color='darkgreen')
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
        plt.show()
