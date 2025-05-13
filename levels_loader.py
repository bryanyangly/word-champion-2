import os
import pandas as pd

class LevelLoadingError(Exception):
    """Custom exception for level loading errors."""
    pass

def try_load(root_folder):
    """Attempts to load levels from the given root folder and returns a DataFrame.
    If an error occurs during the process, it raises a LevelLoadingError exception.

    Args:
        root_folder: The path to the root folder.

    Returns:
        A pandas DataFrame with columns 'level' and 'image_name'.
    """
    data = []
    try:
        for level in os.listdir(root_folder):
            try:
                level_path = os.path.join(root_folder, level)
                if os.path.isdir(level_path):
                    try:
                        for image_name in os.listdir(level_path):
                            data.append({'level': level, 'image_name': image_name})
                    except OSError as e:
                        raise LevelLoadingError(f"Error listing images in level {level}: {e}")
            except OSError as e:
                raise LevelLoadingError(f"Error joining path for level {level}: {e}")
    except OSError as e:
        raise LevelLoadingError(f"Error listing levels in {root_folder}: {e}")
    return pd.DataFrame(data)

if __name__ == '__main__':
    # Example usage:
    root_folder = "input"
    try:
        df = try_load(root_folder)
        print(df)
    except LevelLoadingError as e:
        print(f"Error loading levels: {e}")
