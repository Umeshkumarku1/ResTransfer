import os
import pandas as pd
import subprocess

# Define paths
fasta_file = r"C:\Users\Lenovo\Desktop\1\Query_Genome.fasta"
reference_db = r"C:\Users\Lenovo\Desktop\1\reference_db"
blast_output_file = r"C:\Users\Lenovo\Desktop\1\blast_output.tsv"
output_excel_path = r"C:\Users\Lenovo\Desktop\1\Gene_Counts.xlsx"

# Define gene categories and mappings (limited to specified genes)
gene_categories = {
    'Adherence': 'Adherence',
    'ICEberg': 'Integrative_Conjugative_Element',
    'resfinder': 'Resistance',
    'PID': 'T4SS'
}

# Define scores for each category
category_scores = {
    'Resistance': 5,
    'T4SS': 4,
    'Integrative_Conjugative_Element': 4,
    'Adherence': 2
}

def run_blast():
    """Runs BLAST using the provided FASTA file and reference database."""
    try:
        blast_command = [
            "blastn",  # Change to blastp, tblastn, etc., based on your use case
            "-query", fasta_file,
            "-db", reference_db,
            "-out", blast_output_file,
            "-outfmt", "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore"
        ]
        subprocess.run(blast_command, check=True)
        print(f"BLAST results saved to {blast_output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error running BLAST: {e}")

def parse_blast_tsv(file_path):
    """Parses the BLAST TSV results and categorizes gene matches."""
    gene_counts = {}

    with open(file_path, encoding='utf-8', errors='replace') as file:
        for line in file:
            try:
                # Strip whitespace and ensure line is not empty
                line = line.strip()
                if not line:
                    continue

                # Split line into columns
                columns = line.split('\t')

                # Check for sufficient columns (at least 12)
                if len(columns) < 12:
                    continue

                # Extract relevant fields
                query_id = columns[0]
                identity = float(columns[2])
                alignment_length = int(columns[3])
                query_start = int(columns[6])
                query_end = int(columns[7])
                query_length = abs(query_end - query_start) + 1  # Calculate query length dynamically
                e_value = float(columns[10])
                gene_header = columns[1]

                # Calculate query coverage
                query_coverage = (alignment_length / query_length) * 100

                # Filter valid rows
                if 95 <= identity <= 100 and e_value == 0.0 and 80 <= query_coverage <= 100:
                    if query_id not in gene_counts:
                        gene_counts[query_id] = set()  # Use a set to track unique matches
                    for gene, category in gene_categories.items():
                        if gene in gene_header:
                            gene_counts[query_id].add(category)  # Add category to the set

            except Exception as e:
                print(f"Error processing line: {line} - {e}")

    # Convert sets to counts
    gene_counts_final = {query: {cat: 1 for cat in categories} for query, categories in gene_counts.items()}
    return gene_counts_final

def main():
    # Run BLAST
    run_blast()

    # Parse BLAST results
    if not os.path.exists(blast_output_file):
        print(f"BLAST output file not found: {blast_output_file}")
        return

    gene_counts = parse_blast_tsv(blast_output_file)
    all_data = {}

    for query_id, counts in gene_counts.items():
        if query_id not in all_data:
            all_data[query_id] = {gene: 0 for gene in gene_categories.values()}
        for gene, count in counts.items():
            all_data[query_id][gene] += count

    if all_data:
        # Calculate scores and categorize
        final_data = {}
        for query_id, counts in all_data.items():
            total_score = sum(count * category_scores[gene] for gene, count in counts.items())
            if total_score >= 15:
                category = "High chance for antibiotic resistance gene transfer"
            elif 8 <= total_score < 15:
                category = "Moderate chance for antibiotic resistance gene transfer"
            else:
                category = "Low chance for antibiotic resistance gene transfer"

            final_data[query_id] = {**counts, 'Total_Score': total_score, 'Category': category}

        # Convert to DataFrame and save
        df = pd.DataFrame.from_dict(final_data, orient='index').fillna(0)
        df.to_excel(output_excel_path)
        print(f"Excel file saved at {output_excel_path}")
    else:
        print("No data to save.")

if __name__ == "__main__":
    main()