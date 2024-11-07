import os

def get_csv_paths(csv_dir):

    if not os.path.exists(csv_dir):
        raise ValueError(f"The path {csv_dir} doesn't exist")

    csv_paths = [os.path.join(csv_dir, file) for file in os.listdir(csv_dir) if file.endswith('.csv')]
    csv_paths.sort()
    return csv_paths
