import seaborn as sns
import matplotlib as plt
from matplotlib import colors

# Default theme
sns.set_theme(rc={"axes.facecolor":"#FFF9ED","figure.facecolor":"#FFF9ED"})
pallet = ["#682F2F", "#9E726F", "#D6B2B1", "#B9C0C9", "#9F8A78", "#F3AB60"]
cmap = colors.ListedColormap(["#682F2F", "#9E726F", "#D6B2B1", "#B9C0C9", "#9F8A78", "#F3AB60"])

# Plot Income, Age, Recency, Spent, Family_Size, and Shopper_Length
def relative_plot(data):
    To_Plot = ["Income", "Recency", "Family_Size", "Age", "Spent", "Shopper_Length"]
    plt.figure()
