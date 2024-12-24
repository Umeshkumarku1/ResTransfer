# ResTransfer: Predicting Horizontal Gene Transfer of Resistance Genes in Microbes

**ResTransfer** is a bioinformatics pipeline designed to predict the likelihood of horizontal gene transfer (HGT) of antibiotic resistance genes in microbial strains. This tool leverages BLAST for sequence alignment and a categorization system to assess gene transfer potential based on identity, query coverage, and other criteria. The results are scored and categorized into three levels of resistance transfer likelihood.

---

## Features

- **BLAST Integration**: Uses BLAST for sequence alignment between query genomes and reference databases.
- **Gene Categorization**: Categorizes matches into predefined groups, including Resistance, T4SS, Integrative Conjugative Element (ICE), and Adherence.
- **Scoring System**: Assigns scores to gene categories based on their contribution to resistance gene transfer likelihood.
- **Excel Output**: Outputs results in a structured Excel file, including total scores and resistance transfer likelihood categories.

---

## Prerequisites

Ensure the following software and packages are installed:

1. **BLAST**: Download and configure from [NCBI BLAST+](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/).
2. **Python**: Version 3.8 or higher.
3. **Python Libraries**:
   - `pandas`
   - `openpyxl`


**Install the required Python libraries using**:

```bash

pip install pandas openpyxl

Installation

Clone the repository:



Copy code

git clone https://github.com/Umeshkumarku1/ResTransfer.git

cd ResTransfer

Ensure BLAST executables are added to your system PATH.


Usage

Step 1: Input Preparation

Prepare the input files:

Query genome in FASTA format (e.g., Query_Genome.fasta).

Reference database for BLAST (e.g., reference_db).

Step 2: Running the Pipeline

Run the pipeline using the script:


Copy code

python ResTransfer.py

Script Workflow

Run BLAST:

The script executes a blastn search against the reference database.

Results are saved in a TSV file (blast_output.tsv).

Parse BLAST Results:

Filters BLAST results based on identity, query coverage, and e-value thresholds.

Categorizes gene matches into predefined groups.

Score and Categorize:

Computes a total score for each query based on gene categories.

Classifies results into:

High chance for antibiotic resistance gene transfer.

Moderate chance for antibiotic resistance gene transfer.

Low chance for antibiotic resistance gene transfer.

Export Results:

Saves results, scores, and categories to an Excel file (Gene_Counts.xlsx).
