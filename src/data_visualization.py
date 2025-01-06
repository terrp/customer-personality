import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import colors

# Default theme
sns.set_theme(rc={"axes.facecolor":"#FFF9ED","figure.facecolor":"#FFF9ED"})
pallet = ["#682F2F", "#9E726F", "#D6B2B1", "#B9C0C9", "#9F8A78", "#F3AB60"]
cmap = colors.ListedColormap(["#682F2F", "#9E726F", "#D6B2B1", "#B9C0C9", "#9F8A78", "#F3AB60"])

# Plot Income, Age, Recency, Spent, Family_Size, Is_Parent and Shopper_Length
def relative_plot(data):
    data["Is_Parent"] = data["Is_Parent"].astype("category")
    To_Plot = ["Income", "Recency", "Family_Size", "Age", "Spent", "Shopper_Length", "Is_Parent"]
    print("Relative mapping of possibly related features: Data Subset")
    plt.figure()
    sns.pairplot(data[To_Plot], hue= "Is_Parent",palette= (["#682F2F","#F3AB60"]))
    
    # Save and display plot to png
    plt.savefig("relative_plot.png", dpi=300, bbox_inches="tight")
    print("Plot saved as 'relative_plot.png'.") 
    plt.show()
