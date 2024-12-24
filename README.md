# ResTransfer: Predicting Horizontal Gene Transfer of Resistance Genes in Microbes

**ResTransfer** is a bioinformatics pipeline designed to predict the likelihood of horizontal gene transfer (HGT) of antibiotic resistance genes in microbial strains. This tool leverages BLAST for sequence alignment and a categorization system to assess gene transfer potential based on identity, query coverage, and other criteria. The results are scored and categorized into three levels of resistance transfer likelihood.

---

## Features

- **BLAST Integration**: Uses BLAST for sequence alignment between query genomes and reference databases.
- **Gene Categorization**: Categorizes matches into predefined groups, including Resistance, T4SS, Integrative Conjugative Element (ICE), and Adherence.
- **Scoring System**: Assigns scores to gene categories based on their contribution to resistance gene transfer likelihood.
- **Excel Output**: Outputs results in a structured Excel file, including total scores and resistance transfer likelihood categories.



## Prerequisites

Ensure the following software and packages are installed:

1. **BLAST**: Download and configure from [NCBI BLAST+](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/).
2. **Python**: Version 3.8 or higher.
3. **Python Libraries**:
   - `pandas`
   - `openpyxl`


**Install the required Python libraries using**:


`pip install pandas openpyxl`


Installation

Clone the repository:


Copy code

`git clone https://github.com/Umeshkumarku1/ResTransfer.git`


`cd ResTransfer`


Ensure BLAST executables are added to your system PATH.


The reference_db.nsq file can be accessed from this link.


Here is the direct link to access the reference_db.nsq file: https://drive.google.com/file/d/1Tw67zxHtDQePQsi3ZtrZQoB9sqc9NFk-/view?usp=drive_link.

---


## Usage

**Step 1: Input Preparation**

Prepare the input files:

Query genome in FASTA format (e.g., Query_Genome.fasta).

Reference database for BLAST (e.g., reference_db).


**Step 2: Running the Pipeline**

Run the pipeline using the script:


Copy code

`python ResTransfer.py`


Script Workflow

Run BLAST:

The script executes a blastn search against the reference database.

Results are saved in a TSV file (blast_output.tsv).


**Parse BLAST Results:**

Filters BLAST results based on identity, query coverage, and e-value thresholds.

Categorizes gene matches into predefined groups.


**Score and Categorize:**

Computes a total score for each query based on gene categories.


**Classifies results into:**

 - High chance for antibiotic resistance gene transfer.

 - Moderate chance for antibiotic resistance gene transfer.

 - Low chance for antibiotic resistance gene transfer.


**Export Results:**

Saves results, scores, and categories to an Excel file (Gene_Counts.xlsx).


**Example Workflow**

-Prepare the Query Genome and Reference Database:

-Place your genome FASTA file in the appropriate location.

-Configure the reference database using makeblastdb:


Copy code

`makeblastdb -in reference.fasta -dbtype nucl -out reference_db`

Run the Script:


Copy code

`python ResTransfer.py`

***View Results:**


Check the generated Gene_Counts.xlsx for scores and resistance gene transfer categories.


**Outputs**

The pipeline generates the following outputs:

- BLAST Output (blast_output.tsv): Tabular format of BLAST results.
  
- Final Results (Gene_Counts.xlsx).
  
- Gene counts for each category.
  
- Total score for each query.
  
- Resistance transfer likelihood category.
  


## Troubleshooting

-BLAST Errors: Ensure BLAST is installed and added to the system PATH.
-Missing Output File: Check input file paths and permissions.
-Excel Not Generated: Verify input data meets filter criteria.


## License
This project is licensed under the MIT License. See the LICENSE file for details.


## Contact
For issues or feedback, please reach out to:

**Name: Umeshkumar KU**

**Email: Research.umeshkumarku@gmail.com**

**GitHub: https://github.com/Umeshkumarku1**
