import subprocess
import itertools
import re

# Please specify your own files here
index_file = "index.ndx"  
xtc_file = "protein.xtc"  
tpr_file = "topol.tpr" 
   
exclude_groups = {"System", "Protein", "Water", "Non-Protein", "IONs"}  # Groups to exclude (general system groups in the index file)

def parse_index_file(index_filename):
    residues = []
    with open(index_filename, "r") as f:
        for line in f:
            match = re.match(r"\[(\S+)\]", line)  
            if match:
                residue_name = match.group(1)
                if residue_name.lower() not in exclude_groups:  
                    residues.append(residue_name)
    return residues

residues = parse_index_file(index_file)

residue_pairs = list(itertools.combinations(residues, 2)) # This code creates all possible residue pairs for analysis (e.g., MET_1-ASP_2, MET_1-THR_3 ...)

for res1, res2 in residue_pairs:
    output_xvg = f"hbond_{res1}_{res2}.xvg"

    command = f"echo {res1} {res2} | gmx hbond -f {xtc_file} -s {tpr_file} -n {index_file} -num {output_xvg}"
    
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"{output_xvg} was generated!")
    except subprocess.CalledProcessError as e:
        print(f"Error: Issue calculating hbond for {res1}-{res2}!\n{e}")

