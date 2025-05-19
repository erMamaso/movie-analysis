from src.preprocess import clean_data
from src.analysis import analyze_data
from src.visualize import plot_genres, plot_ratings

def main():
	#Cleaning
	df = clean_data("data/movies.csv", "data/movies_clean.csv")
	#Analysis
	stats = analyze_data("data/movies_clean.csv", "output/summary.txt")
	print("STATS:", stats)
	#Visualization
	plot_genres("data/movies_clean.csv", "output/genres_bar.png")
	plot_ratings("data/movies_clean.csv", "output/ratings_hist.png")


if __name__ == "__main__":
	main()