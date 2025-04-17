from itertools import combinations
from typing import List, Tuple
import sys

class Element:
    """Модель: один елемент з двома типами відмов.."""
    def __init__(self, id: int, qkz: float, qo: float):
        self.id = id
        self.qkz = qkz
        self.qo  = qo

class Configuration:
    """Список з трьох ланцюжків, кожен — список Element."""
    def __init__(self, chains: List[List[Element]]):
        self.chains = chains

class ReliabilityCalculator:
    """Обчислює надійність конфігурації за формулою (2)."""
    @staticmethod
    def compute(config: Configuration) -> float:
        prod_no_short = 1.0
        prod_no_open  = 1.0
        for chain in config.chains:
            # вероятность короткого замыкания всей цепочки
            p_kz_chain   = 1.0
            # вероятность нигде не произошло «обрыва» в цепочке
            p_no_qo_chain = 1.0
            for elem in chain:
                p_kz_chain   *= elem.qkz
                p_no_qo_chain *= (1 - elem.qo)
            prod_no_short *= (1 - p_kz_chain)
            prod_no_open  *= (1 - p_no_qo_chain)
        return prod_no_short - prod_no_open

class ConfigGenerator:
    """Генерація всіх конфігурацій: вибір k1 з K, потім k2 з залишку, потім k3."""
    @staticmethod
    def generate(elems: List[Element], k1: int, k2: int, k3: int):
        n = len(elems)
        idxs = list(range(n))
        for c1 in combinations(idxs, k1):
            rem1 = set(idxs) - set(c1)
            for c2 in combinations(rem1, k2):
                rem2 = rem1 - set(c2)
                for c3 in combinations(rem2, k3):
                    yield Configuration([
                        [elems[i] for i in c1],
                        [elems[i] for i in c2],
                        [elems[i] for i in c3],
                    ])


class FileIO:
    @staticmethod
    def read_input(path: str) -> Tuple[Tuple[int,int,int], List[Element]]:
        with open(path, 'r') as f:
            k1, k2, k3 = map(int, f.readline().split())
            K = int(f.readline())
            elems = []
            for _ in range(K):
                id_j, qkz_j, qo_j = f.readline().split()
                elems.append(Element(int(id_j), float(qkz_j), float(qo_j)))
        return (k1, k2, k3), elems

    @staticmethod
    def write_output(path: str,
                     struct: Tuple[int,int,int],
                     K: int,
                     total_cfg: int,
                     max_rel: float,
                     best_cfg: Configuration):
        with open(path, 'w') as f:
            f.write(f"Structure: k1={struct[0]}, k2={struct[1]}, k3={struct[2]}\n")
            f.write(f"Element types: {K}\n")
            f.write(f"Configurations: {total_cfg}\n")
            f.write(f"Max reliability: {max_rel:.6f}\n")
            f.write("Best configuration (IDs by chain):\n")
            for i, chain in enumerate(best_cfg.chains, 1):
                ids = ','.join(str(e.id) for e in chain)
                f.write(f" Chain {i} ({len(chain)}): {ids}\n")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <input_file>")
        sys.exit(1)

    infile = sys.argv[1]
    outfile = "result.txt"

    (k1, k2, k3), elements = FileIO.read_input(infile)
    calc  = ReliabilityCalculator()
    best_rel = -1.0
    best_cfg = None
    count = 0

    for cfg in ConfigGenerator.generate(elements, k1, k2, k3):
        count += 1
        rel = calc.compute(cfg)
        if rel > best_rel:
            best_rel, best_cfg = rel, cfg

    # вывод
    FileIO.write_output(outfile, (k1,k2,k3), len(elements), count, best_rel, best_cfg)
    print(f"Structure: {k1},{k2},{k3}")
    print(f"Types: {len(elements)}, Configs: {count}")
    print(f"Max reliability: {best_rel:.6f}")
    for i, chain in enumerate(best_cfg.chains, 1):
        print(f" Chain {i}: " + ", ".join(str(e.id) for e in chain))

if __name__ == "__main__":
    main()
