class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:

        lis = mat

        fraca = {i: sum(j)  for i , j in enumerate(lis)}
        fraca =  sorted(fraca, key=fraca.get)#ordena pelos valores

        return fraca[:k]




