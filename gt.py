import seaborn as sns
import matplotlib.pyplot as plt

# Load a sample dataset
iris = sns.load_dataset("iris")

# Create a pair plot
sns.pairplot(iris, hue="species", markers=["o", "s", "D"])

# Show the plot
plt.show()
