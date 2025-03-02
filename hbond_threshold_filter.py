import os
import numpy as np

def read_xvg(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            if not line.startswith(('#', '@')):  
                values = line.split()
                if values:
                    data.append(float(values[1]))  # Extract the bond count from the second column
    return data  

def analyze_hbonds(folder, threshold):
    results = []
    total_files = 0
    
    for file in os.listdir(folder):
        if file.endswith('.xvg'):
            total_files += 1
            file_path = os.path.join(folder, file)
            data = read_xvg(file_path)
            
            if not data:  
                continue  
            
            bound_percentage = np.sum(np.array(data) >= 1) / len(data)  
            if bound_percentage >= threshold:
                results.append((file, bound_percentage * 100))  
    
    return results, total_files

def main():
    folder = input("Please enter the folder path where the .xvg files are located (e.g., '/path/to/folder'): ").strip()
    
    if not os.path.isdir(folder):
        print("Error: The specified folder does not exist.")
        return

    try:
        threshold = float(input("Enter the threshold value as a percentage (e.g., for 50, enter 50): ").strip()) / 100
    except ValueError:
        print("Error: Please enter a valid numerical threshold.")
        return
    
    results, total_files = analyze_hbonds(folder, threshold)
    
    output_file = os.path.join(folder, "results.txt")
    with open(output_file, 'w') as f:
        f.write(f"Total scanned files: {total_files}\n")
        f.write(f"Threshold: {threshold * 100}%\n\n")
        f.write("Selected hydrogen bond pairs:\n")
        for file, percentage in results:
            f.write(f"{file}: {percentage:.2f}%\n")
    
    print(f"Results have been saved to 'results.txt'.")

if __name__ == "__main__":
    main()

