import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator  

def plot_hbond_graphs(result_file, xvg_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    with open(result_file, 'r') as f:
        lines = f.readlines()[4:]  
        pairs = []
        for line in lines:
            line = line.strip()
            if line: 
                pair = line.split(':')[0]  
                pairs.append(pair)

    for pair in pairs:
        pair_name = pair.replace("hbond_", "").replace(".xvg", "")
        
        residues = pair_name.split("_")

        if len(residues) == 4:  
            residue_pair = f"{residues[0]}_{residues[1]} - {residues[2]}_{residues[3]}"
        else:
            print(f"Skipping invalid pair: {pair_name}, not enough residue information.")
            continue 

        xvg_file_path = os.path.join(xvg_folder, pair)  
        
        if os.path.exists(xvg_file_path):
            times, values = [], []
            with open(xvg_file_path, 'r') as f:
                for line in f:
                    if line.startswith("#") or line.startswith("@"):  
                        continue
                    parts = line.split()
                    if len(parts) >= 2:
                        times.append(float(parts[0])) 
                        values.append(float(parts[1])) 
            
       
            plt.figure()
            plt.plot(times, values, label=residue_pair, color='b')  
            plt.xlabel("Time (ps)")
            plt.ylabel("Hydrogen Bond Count")
            plt.title(f"Hydrogen Bonds - {residue_pair}") 
            plt.legend()
            plt.grid()
            plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

            output_path = os.path.join(output_folder, f"{residue_pair}.png")
            plt.savefig(output_path, dpi=300)
            plt.close()
            print(f"Graph saved: {output_path}")
        else:
            print(f"Warning: {pair} file not found in the folder!")

result_file = "results.txt"  
xvg_folder = "/path/to/your/xvg/folder" # Please specify the folder where your .xvg files are located
output_folder = "hbond_graphs" 

plot_hbond_graphs(result_file, xvg_folder, output_folder)

