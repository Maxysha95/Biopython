import re
import sys
import random

print(random.randint(0, 2))
random.choice(["A" , "T", "C", "G"])


def create_snp(n, seq):
    assert "Number of SNP is longer than length of seq", n < len(seq);

    n = len(seq)
    snp_pos = random.sample(range(0, len(seq)), 3)
    answer = []
    for pos in snp_pos:
        answer.append([seq[pos], random.choice(('A', 'C', 'G', 'T'))])
        return answer


def process_file(filename, n):
    print("SEQ_ID  |  MUTATION  |  POSITION-OF-MUTATION")

    with open(filename) as f:
        for line in f:
            seq_id, seq = re.split(r'\s+', line.strip())

            mutations = create_snp(n, seq)
            for mutation in mutations:
                print(f"{seq_id: <22}{mutation[0]: >10}->{mutation[1]}\t{mutation[2]}")


def main():
    if len(sys.argv) < 3:
        print("Usage: Task_1.ipynb <path_to_seq> <SNP#>")
        exit()

    filename = sys.argv[1]
    n = sys.argv[2]

    try:
        process_file(filename, n)

    except FileNotFoundError as error:
        print(f"No such file: {filename}")


if __name__ == '__main__':
    main()
