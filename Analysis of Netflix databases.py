import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv('Netflix.csv')

# 1. Стовпчикова діаграма розподілу кількості проектів за телевізійним рейтингом
rating_counts = df['rating'].value_counts()
rating_counts.plot(kind='bar', xlabel='TV Rating', ylabel='Number of Projects', title='Distribution of Projects by TV Rating')
plt.show()

# 2. Аналіз фокусування Netflix на серіалах та фільмах останніми роками
print("--------------------------------------------------------------------------------------")
df['date_added'] = pd.to_datetime(df['release_year']).dt.year
last_5_years = df[df['date_added'] >= df['date_added'].max() - 5]
project_types_counts = last_5_years['type'].value_counts()
print("Фокус на серіалах (TV Show) порівняно з фільмами:")
print(project_types_counts)
print("Netflix сфокусовані більш на філмах.")
print("--------------------------------------------------------------------------------------")

# 3. Країна, яка випустила найбільше та найменше проектів у 2021 році
year_2023 = df[df['release_year'] == 2021]
most_projects_country = year_2023['country'].value_counts().idxmax()
least_projects_country = year_2023['country'].value_counts().idxmin()
print(f"Kpaїнa, яка випустила найбільше проектів y 2021 році: {most_projects_country}")
print(f"Країна, яка випустила найменше проектів y 2021 році: {least_projects_country}")
print("--------------------------------------------------------------------------------------")

# 4. Рік, коли виходить найбільше серіалів
df['release_year'] = pd.to_datetime(df['date_added']).dt.month
most_released_year = df[df['type'] == 'TV Show']['date_added'].mode().values[0]
print(f"Рік, коли виходить найбільше серіалів: {most_released_year}")
print("--------------------------------------------------------------------------------------")

# 5. Топ-5 популярних жанрів та кругова діаграма
top_genres = df['listed_in'].str.split(', ', expand=True).stack().value_counts().head(5)
top_genres.plot.pie(autopct='%1.1f%%', startangle=90, title='Top 5 Genres on Netflix')
plt.show()