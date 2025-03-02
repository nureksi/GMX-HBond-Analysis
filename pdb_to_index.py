import re

def parse_pdb(pdb_file):
    residues = {}
    
    with open(pdb_file, 'r') as f:
        for line in f:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                atom_id = int(line[6:11].strip())
                res_name = line[17:20].strip()
                res_num = int(line[22:26].strip())
                
                res_key = f"{res_name}_{res_num}"
                if res_key not in residues:
                    residues[res_key] = []
                residues[res_key].append(atom_id)
    
    return residues

def read_index_file(index_file):
    with open(index_file, 'r') as f:
        return f.readlines()

def update_index_file(index_file, residues):
    lines = read_index_file(index_file)
    
    with open(index_file, 'w') as f:
        f.writelines(lines)
        f.write("\n")
        
        for res_key, atom_ids in residues.items():
            f.write(f"[{res_key}]\n")
            atom_lines = ' '.join(map(str, atom_ids))
            for i in range(0, len(atom_lines), 80):
                f.write(atom_lines[i:i+80] + "\n")
def main():
    pdb_file = "protein.pdb" # Specify your PDB file name
    index_file = "index.ndx" # Specify your index file name
    
    residues = parse_pdb(pdb_file)
    update_index_file(index_file, residues)
    print("Index file updated")

if __name__ == "__main__":
    main()
