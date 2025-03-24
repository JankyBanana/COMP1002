#
# Algorithm to solve the towers of Hanoi problem with n disks
#

class Hanoi():
    recursionLvl = 0
    moves = 0

    def towers(n, src, dest):
        if n < 0:
            raise ValueError("Number of disks cannot be negative")
        elif n == 1:
            Hanoi.moveDisk(n, src, dest)
        else:
            tmp = 6 - src - dest
            Hanoi.recursionLvl += 1
            Hanoi.towers(n-1, src, tmp)

            Hanoi.moveDisk(n, src, dest)
            Hanoi.towers(n-1, tmp, dest)

            Hanoi.recursionLvl -= 1


    def moveDisk(n, src, dest):
        Hanoi.moves += 1
        tabIndent = Hanoi.recursionLvl-1
        print(f'{'\t'*tabIndent}Recursion level = {Hanoi.recursionLvl}\n'
              f'{'\t'*tabIndent}Moving {n} disks from peg {src} to peg {dest}\n'
              f'{'\t'*tabIndent}n = {n}, src = {src}, dest = {dest}\n')

def main():
    Hanoi.towers(3, 1, 3)
    print(f'Required {Hanoi.moves} moves to solve')
main()