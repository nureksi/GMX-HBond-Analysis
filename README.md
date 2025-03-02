# **Hydrogen Bond Analysis** 🚀

This pipeline performs hydrogen bond analysis on a protein structure using GROMACS. It processes residue pairs from a PDB file, calculates hydrogen bonds, filters them based on a threshold, and visualizes the results through line plots.

---

## **Requirements**

 ![Static Badge](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge)  ![Static Badge](https://img.shields.io/badge/Gromacs-2021.4-yellow?style=for-the-badge) or compatible version  
  
 Dependencies:
  
 ![Static Badge](https://img.shields.io/badge/Matplotlib-white?style=for-the-badge)  ![Static Badge](https://img.shields.io/badge/numpy-738A94?style=for-the-badge) 


---

## **How to Use the Pipeline**

   **Step1: Update the Index File**
   - Run `pdb_to_index.py` to update the existing index file with residue groups from the PDB file.
   - Use the following command:
    
     ```bash
     python pdb_to_index.py
     ```

   **Step 2: Perform Hydrogen Bond Analysis** 
   - Run `hbond_analysis.py` to analyze hydrogen bonds between residue pairs.
   - This will generate `.xvg` files for each pair with bond data.
   - Use the following command:
     ```bash
     python hbond_analysis.py
     ```

   **Step 3: Filter Hydrogen Bonds** 
   - Run `hbond_threshold_filter.py` to filter hydrogen bonds based on a defined threshold.
   - Pairs with hydrogen bonds above the threshold will be saved to `result.txt`.
   - Use this command:
     ```bash
     python hbond_threshold_filter.py
     ```

   **Step 4: Visualize Hydrogen Bonds** 
   - Run `hbond_visualization.py` to generate line plots for each filtered pair.
   - The plots will visualize hydrogen bond counts over time.
   - Use this command:
     ```bash
     python hbond_visualization.py
     ```

---

## Detailed Tutorial

For a more detailed step-by-step tutorial on how to use the Hydrogen Bond Analysis Pipeline, please refer to the [tutorial.md](tutorial-files/tutorial.md) file located in the `tutorial-files/` directory.
