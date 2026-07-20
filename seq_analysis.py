def read_fasta(filename):
    file = open(filename, "r")

    sequence = ""

    for line in file:
        if not line.startswith(">"):
            sequence += line.strip().upper()

    file.close()
    return sequence


def calculate_gc(sequence):
    G_count = sequence.count("G")
    C_count = sequence.count("C")

    GC_percentage = ((G_count + C_count) / len(sequence)) * 100

    return GC_percentage


sequence = read_fasta("sequence.fasta")

gc = calculate_gc(sequence)

print("Sequence length:", len(sequence))
print("GC percentage:", gc)


def validate_dna(sequence):
    valid_bases = "ATGC"

    for base in sequence:
        if base not in valid_bases:
            return False

    return True


is_valid = validate_dna(sequence)

print("Valid DNA:", is_valid)


def find_invalid_bases(sequence):
    valid_bases = "ATGC"

    for base in sequence:
        if base not in valid_bases:
            print("Invalid character found:", base)


find_invalid_bases(sequence)
