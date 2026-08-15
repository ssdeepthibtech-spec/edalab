Program 1:
import pandas as pd
# Load the dataset
df = pd.read_csv("hospital.csv")
# Display first five records
print("Hospital Dataset")
print(df.head())
# Display dataset information
print("\nDataset Information")
print(df.info())

Program 2:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv("hospital.csv")
# Create Pair Plot
sns.pairplot(
    df,
    vars=["Age", "Cost"],
    hue="Outcome",
    diag_kind="hist"
)
# Display the plot
plt.show()
