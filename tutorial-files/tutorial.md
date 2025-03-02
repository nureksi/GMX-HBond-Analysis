# Hydrogen Bond Analysis Pipeline Tutorial 

This tutorial provides a step-by-step guide to performing hydrogen bond analysis between residue pairs in a protein structure. The analysis is based on the 1AKI protein structure (PDB ID: 1AKI), which corresponds to lysozyme, derived from a 1 ns molecular dynamics simulation.

You will use the following example files, available in the `tutorial-files/` directory:

- **1AKI.pdb**: The protein structure file.
- **1AKI.xtc**: The trajectory file from the simulation.
- **1AKI.tpr**: The topology file.

These files will be utilized to identify and analyze hydrogen bonds between residue pairs.

---

## Create the Index File 

Before the first step, you need to create an index file from the PDB structure. 

To create the index file, run the following command:

```bash
gmx make_ndx -f 1AKI.pdb -o index.ndx
```
## Step 1: Update the Index File

In this step, we will update an existing index file by adding residue groups from the PDB file. The `pdb_to_index.py` script processes the PDB file and adds predefined residue groups to the existing **index.ndx** file.

1. Open the `pdb_to_index.py` script in your preferred code editor.
2. In the script, find the following lines and update the `pdb_file` and `index_file` variables to match the names of your **PDB** and **index** files:

```python
def main():
  pdb_file = "1AKI.pdb"  # Specify your PDB file name
  index_file = "index.ndx"  # Specify your existing index file name
```
3. Save the changes to the script after updating the file names.
4. Run the script with the following command in your terminal:

```bash
python pdb_to_index.py
```

## Step 2: Perform Hydrogen Bond Analysis 

In this step, we will use the `hbond_analysis.py` script to calculate hydrogen bonds between residue pairs defined in the updated **index.ndx** file.

Before running the script, you need to specify the correct file names for the **index**, **xtc**, and **tpr** files in the Python script.

1. Open the `hbond_analysis.py` script in your code editor.
2. Find the section where the file names are specified:

```python
# Please specify your own files here
index_file = "index.ndx"
xtc_file = "protein.xtc"
tpr_file = "topol.tpr"
```
3. Replace the placeholders with your own file names, as shown below:
 
   index_file = "index.ndx"   
   xtc_file = "1AKI.xtc"      
   tpr_file = "1AKI.tpr"    

4. Run the script with the following command:

```bash
python hbond_analysis.py
```
## Step 3: Filter Hydrogen Bonds 

In this step, we will filter the hydrogen bonds based on a defined threshold using the `hbond_threshold_filter.py` script. This allows us to keep only the most significant hydrogen bonds based on the occupancy percentage.

Make sure the `.xvg` files generated in **Step 2** are located in a folder. 

1. To run the script, use the following command:

```bash
python hbond_threshold_filter.py
```
2. When you run the `hbond_threshold_filter.py` script, it will prompt you to enter the folder path where the `.xvg` files are stored. For example:

```bash
Please enter the folder path where the .xvg files are located (e.g., '/path/to/folder'):
```
3. The script will then ask for a threshold value. In this tutorial, we will use a threshold of 50%. Enter 50 when prompted:

This means that only hydrogen bonds with an occupancy greater than 50% will be retained.

4. The script will then filter the bonds based on the threshold and save the results to a results.txt file.

## Step 4: Visualize Hydrogen Bonds 

In this final step, we will generate line plots to visualize the hydrogen bonds over time. These plots will help us observe how the hydrogen bonds between residue pairs evolve during the simulation.

1. Before running the `hbond_visualization.py` script, you need to specify the path to the folder where the **.xvg** files are located. In the script, look for the following line:

```python
xvg_folder = "/path/to/your/xvg/folder"  # Please specify the folder where your .xvg files are located
```
2. To run the script, use the following command in your terminal:

```bash
python hbond_visualization.py
```

3. The script will generate line plots showing the bond counts over time for each pair of hydrogen bonds in the results.txt file.


### Example Plot:
Here's an example of the plot for the hydrogen bonds between ASP_119 and ARG_125:
<img src="ASP_119%20-%20ARG_125.png" width="500" />
 
---

## Contact

We welcome your questions and feedback via email (hnureksi@gmail.com) or GitHub issues.

---

## Happy analyzing! 🎉
