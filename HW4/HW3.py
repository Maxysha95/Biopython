{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "import sys\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'A'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "print(random.randint(0, 2))\n",
    "random.choice([\"A\" , \"T\", \"C\", \"G\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "filename = 'prom.txt'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_snp(n, seq):\n",
    "    if n > len(seq):\n",
    "        print(\"Number of SNP is longer than length of seq\")\n",
    "        n = len(seq)\n",
    "    snp_pos = random.sample(range(0, len(seq)), 3)\n",
    "    answer = []\n",
    "    for pos in snp_pos:\n",
    "        answer.append([seq[pos], random.choice(('A', 'C', 'G', 'T'))])\n",
    "        return answer\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "def process_file(filename, n):\n",
    "    print(\"SEQ_ID  |  MUTATION  |  POSITION-OF-MUTATION\")\n",
    "    \n",
    "    with open(filename) as f:\n",
    "        for line in f:\n",
    "            seq_id, seq = re.split(r'\\s+', line.strip())\n",
    "            \n",
    "            mutations = create_snp(n, seq)\n",
    "            for mutation in mutations:\n",
    "                print(f\"{seq_id: <22}{mutation[0]: >10}->{mutation[1]}\\t{mutation[2]}\")\n",
    "                \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SEQ_ID  |  MUTATION  |  POSITION-OF-MUTATION\n",
      "No such file: -f\n"
     ]
    }
   ],
   "source": [
    "def main():\n",
    "    \n",
    "    if len(sys.argv) < 3:\n",
    "        print(\"Usage: Task_1.ipynb <path_to_seq> <SNP#>\")\n",
    "        exit()\n",
    "    \n",
    "    \n",
    "    filename = sys.argv[1]\n",
    "    n = sys.argv[2][3:]\n",
    "    \n",
    "    \n",
    "    try:\n",
    "        process_file(filename, n)\n",
    "    \n",
    "    except FileNotFoundError as error:\n",
    "        print(f\"No such file: {filename}\")\n",
    "        \n",
    "if __name__ == '__main__':\n",
    "    main()\n",
    "    \n",
    "    \n",
    "        \n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
