import pandas as pd
import matplotlib.pyploy as plt

def plot_genres(input_path, output_path):
	df = pd.read_csv(input_path)
	genre_counts = df['genre'].value_counts()
	plt.figure(figsize=(8,6)) #a tuple
	genre_counts.plot(kind='bar')
	plt.bar(genre_counts.index, genre_counts.values, color='skyblue')
	plt.title('Number Movies per Genre')
	plt.xlabel('Genre')
	plt.ylabel('Quantity')
	plt.savefig(output_path)
	plt.close()

if __name__ == "__main__":
	plot_genres("data/movies_clean.csv", "output/genres_bar.png")