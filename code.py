from typing import Dict


def count_freq(seq: str) -> Dict[str:int]:
    counts = {c: 0 for c in set(seq)}
    for c in seq:
        counts[c] += 1
    return counts


def print_freq(freq_dict: Dict[str:int]) -> None:
    print('freqs')
    total = float(sum([freq_dict[k] for k in freq_dict.keys()]))
    for k in freq_dict.keys():
        print(k + ':' + str(freq_dict[k] / total))


print_freq(count_freq('ATCTGACGCGCGCCGC'))
