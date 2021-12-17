from itertools import chain, compress
from pathlib import Path
import operator


def parse_input(file_path: Path):
    def readboard(f):
        board = []
        for i in range(5):
            row = [n for n in f.readline().strip().split(' ') if n != '']
            numbers = list(map(int, row))
            board.append(numbers)
        return board

    with open(file_path, 'r') as f:
        winners = list(map(int, f.readline().strip().split(',')))
        boards = []
        l = f.readline()
        while l != '':
            boards.append(readboard(f))
            l = f.readline()
        return [winners, boards]


def create_masks(count):
    masks = []
    for i in range(count):
        mask = []
        for j in range(5):
            mask.append([False] * 5)
        masks.append(mask)
    return masks


def mark_board(mask, board, number):
    for r in range(5):
        for c in range(5):
            if board[r][c] == number:
                mask[r][c] = True


def mark_boards(masks, boards, number):
    for m, b in zip(masks, boards):
        mark_board(m, b, number)


def winner(mask, board):
    if any([all(row) for row in mask]):
        return True

    mask_t = zip(*mask)
    if any([all(row) for row in mask_t]):
        return True

    return False


def score(mask, board):
    if not winner(mask, board):
        return -1

    remaining_numbers = compress(chain(*board), map(operator.not_,
                                                    chain(*mask)))
    return sum(remaining_numbers)


def highest_score(masks, boards):
    return max([score(m, b) for (m, b) in zip(masks, boards)])


def solve1(numbers, boards) -> None:
    masks = create_masks(len(boards))
    for n in numbers:
        mark_boards(masks, boards, n)
        s = highest_score(masks, boards)
        if s > -1:
            print(s * n)
            return


def solve2(numbers, boards) -> None:
    masks = create_masks(len(boards))
    winners = set()
    for n in numbers:
        mark_boards(masks, boards, n)
        for i in range(len(boards)):
            last_one = (len(winners) == len(boards) - 1)
            if winner(masks[i], boards[i]):
                if last_one and i not in winners:
                    print(score(masks[i], boards[i]) * n)
                    return
                winners.add(i)


if __name__ == '__main__':
    input = parse_input('2021/04.txt')
    # print(input)
    solve1(*input)
    solve2(*input)
