import pandas as pd

def analyze_data(input_path, output_path):
	df = pd.read_csv(input_path)
	stats = df.groupby('genre')['rating'].mean().to_dict()
	with open(output_path, 'w') as f:
		for genre, rating in stats.items():
			f.write(f"{genre}: {rating:.2f}\n")
	return stats

if __name__ == "__main__":
	analyze_data("data/movies_clean.csv", "output/summary.txt")
	