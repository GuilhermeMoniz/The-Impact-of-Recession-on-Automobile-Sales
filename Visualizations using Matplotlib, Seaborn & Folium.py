# Import the required libraries
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# Importing the data
data = "C://Users/guimo/datasets/historical_automobile_sales.csv"

df = pd.read_csv(data)
print(df.head())
print(df.describe())
print(df.columns)

df["Recession"].value_counts()


### Create Visualizations for Data Analysis ###

### TASK 1.1 - Develop a Line chart using the functionality of pandas to show how automobile sales fluctuate from year to year
# fig, ax = plt.subplots(figsize=(10, 6))

ax.set_xticks(df[df["Recession"] == 1]["Year"].unique())

df[["Year", "Automobile_Sales"]].groupby("Year").sum().reset_index().plot(
    kind="line",
    x="Year",
    y="Automobile_Sales",
    title="Automobile Sales per Year",
    ylabel="Total Yearly Sales",
    ax=ax,
    rot=90,
)
ax.annotate(
    "Recession 1980-1982",
    xy=(1981, 10000),
    xytext=(1980, 40000),
    xycoords="data",
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="blue", lw=2),
)

ax.annotate(
    "Recession 2000-2001",
    xy=(2001, 10000),
    xytext=(1997, 40000),
    xycoords="data",
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="blue", lw=2),
)

"""
Include the following on the plot
ticks on x- axis with all the years, to identify the years of recession
annotation for at least two years of recession
Title as Automobile Sales during Recession
"""

fig, ax = plt.subplots(figsize=(10, 6))

ax.set_xticks(df["Year"].unique())

df[["Year", "Automobile_Sales"]].groupby("Year").sum().reset_index().plot(
    kind="line",
    x="Year",
    y="Automobile_Sales",
    title="Automobile Sales per Year",
    ylabel="Total Yearly Sales",
    ax=ax,
    rot=90,
)
ax.annotate(
    "Recession 1980-1982",
    xy=(1981, 10000),
    xytext=(1980, 40000),
    xycoords="data",
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="blue", lw=2),
)

ax.annotate(
    "Recession 2000-2001",
    xy=(2001, 10000),
    xytext=(1997, 40000),
    xycoords="data",
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="blue", lw=2),
)



### TASK 1.2 - Plot different lines for categories of vehicle type and analyse the trend 
### Is there a noticeable difference in sales trends between different vehicle types during recession periods?
t_df = (
    df[df["Recession"] == 1][["Year", "Vehicle_Type", "Automobile_Sales"]]
    .groupby(["Vehicle_Type", "Year"])
    .sum()
    .reset_index()
)

sns.lineplot(data=t_df, x="Year", y="Automobile_Sales", hue="Vehicle_Type")


# There are no exeutive car sales during recessions.



### TASK 1.3 - Use the functionality of Seaborn Library to create a visualization to compare the sales trend per vehicle type for a recession period with a non-recession period
t_df = (
    df[df["Recession"] == 0][["Year", "Vehicle_Type", "Automobile_Sales"]]
    .groupby(["Vehicle_Type", "Year"])
    .sum()
    .reset_index()
)

sns.lineplot(data=t_df, x="Year", y="Automobile_Sales", hue="Vehicle_Type")
plt.show()

### 1.3.1 Now you want to compare the sales of different vehicle types during a recession and a non-recession period
new_df = df.groupby(['Recession', "Year", "Vehicle_Type"])['Automobile_Sales'].mean().reset_index()

sns.barplot(x='Vehicle_Type', y='Automobile_Sales', hue='Recession',  data=new_df)
plt.xticks(rotation=20)
plt.ylabel('Avg Automobile Sales')
plt.title('Average Automobile Sales during Recession and Non-Recession')
plt.show()

### From the above chart what insights have you gained on the overall sales of automobiles during recession?

# There are far fewer recession periods than non-recession so we would first have to normalize the data to make an accurate insight.



### TASK 1.4 - Use sub plotting to compare the variations in GDP during recession and non-recession period by developing line plots for each period
# ### How did the GDP vary over time during recession and non-recession periods?
fig, axs = plt.subplots(1, 2, sharey=True, figsize=(10, 6))

df_rec = df[df["Recession"] == 1]
df_no_rec = df[df["Recession"] == 0]

df_rec[["GDP", "Year"]].groupby("Year").mean().reset_index().plot(
     kind="line",
     x="Year",
     y="GDP",
     ax=axs[0],
     ylabel="Average GDP",
     title="Average GDP per Year in recession periods",
 )
df_no_rec[["GDP", "Year"]].groupby("Year").mean().reset_index().plot(
     kind="line",
     x="Year",
     y="GDP",
    ax=axs[1],
     title="Average GDP per Year in non-recession periods",
 )

fig.suptitle("Comparing GDP in Recession and Non-recession periods", fontsize=15)
plt.show()

# During recession, the GDP of the country was in a low range, might have afected the overall sales of the company



### TASK 1.5 - Develop a Bubble plot for displaying the impact of seasonality on Automobile Sales
month_order = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

df_seas = (
    df_no_rec[["Seasonality_Weight", "Automobile_Sales", "Month"]]
    .groupby("Month")
    .mean()
    .reindex(month_order, axis=0)
    .reset_index()
)
sns.scatterplot(
    data=df_seas, x="Month", y="Automobile_Sales", size="Seasonality_Weight"
).set_title("Seasonality impact on Automobile Sales")

# Is evident that seasonality has not affected on the overall sales. However, there is a drastic raise in sales in the month of April



### TASK 1.6 - Use the functionality of Matplotlib to develop a scatter plot to identify the correlation between average vehicle price relate to the sales volume during recessions
df_rec = df[df["Recession"] == 1]
df_rec.plot(
    kind="scatter",
    x="Consumer_Confidence",
    y="Automobile_Sales",
    title="Consumer Confidence and Automobile Sales during Recessions",
)

### How does the average vehicle price relate to the sales volume during recessions?
df_rec = df[df["Recession"] == 1]
df_rec.plot(
    kind="scatter",
    x="Price",
    y="Automobile_Sales",
    title="Relationship between Average Vehicle Price and Sales during Recessions",
)

# There is not much relation



### TASK 1.7 - Create a pie chart to display the portion of advertising expenditure of XYZAutomotives during recession and non-recession periods
pie_df = df[["Advertising_Expenditure", "Recession"]].groupby("Recession").sum()
pie_df["Advertising_Expenditure"].plot(
    kind="pie",
    labels=["Non-recession", "Recession"],
    autopct="%.0f%%",
    ylabel="",
    title="Advertising Expenditure During Recession and Non-recession Periods",
)


### From the above plot, what insights do you find on the advertisement expenditure during recession and non recession periods?
# There are far more non-recession periods than recession, we would need to normalize the data for a more accurate inference



### TASK 1.8 - Develop a pie chart to display the total Advertisement expenditure for each vehicle type during recession period
df_rec = df[df["Recession"] == 1]


type_pie = (
    df_rec[["Vehicle_Type", "Advertising_Expenditure"]].groupby("Vehicle_Type").sum()
)

type_pie.plot(
    kind="pie",
    y="Advertising_Expenditure",
    ylabel="",
    figsize=(10, 6),
    autopct="%.0f%%",
    title="Advertisement Expenditure per Vehicle Type During Recession Periods",
).legend(loc="upper left")


# During recession the advertisements were mostly focued on low price range vehicle. A wise decision



### TASK 1.9 - Develop a lineplot to analyse the effect of the unemployment rate on vehicle type and sales during the Recession Period
df_rec = df[df["Recession"] == 1]

sns.lineplot(
    df_rec,
    x="unemployment_rate",
    y="Automobile_Sales",
    hue="Vehicle_Type",
    err_style=None,
).set_title("Effect of Unemployment Rate on Vehicle Type and Sales")
plt.show()

### From the above plot, what insights have you gained on the sales of superminicar, smallfamilycar, mediumminicar?
# Doesn't seem like unemployment_rate has a clear relationship with automobile sales. We can see a big dip right before 6.0 for super mini car and then it shoot back up at 6.0


""""""


### !OPTIONAL! TASK 1.10 - Create a map on the hightest sales region/offices of the company during recession period
import urllib.request
path = "C://Users/guimo/datsets/us-states.json"

filename = "us-states.json"
urllib.request.urlretrieve(path, filename)

geo_data = "C://Users/guimo/data-visualization-with-python/us-states.json"
us_map = folium.Map(location=[38.4999425, -97.9521519], zoom_start=4)
folium.Choropleth(
    geo_data=geo_data,
    data=df_rec[["Automobile_Sales", "City"]].groupby("City").sum().reset_index(),
    columns=["City", "Automobile_Sales"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Automobile sales by State",
    highlight=True,
).add_to(us_map).geojson.add_child(
    folium.features.GeoJsonTooltip(["name"], labels=True)
)
us_map