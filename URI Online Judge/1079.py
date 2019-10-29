# -*- coding: utf-8 -*-

def Media(nums):
    aux = ((nums[0] * 2) + (nums[1] * 3) + (nums[2] * 5)) / 10
    return aux


n = int(input())
medias = []

while n != 0:
    entrada = list(map(float, input().strip().split()))
    medias.append(Media(entrada))
    n -= 1

for media in medias:
    print('%.1f' % media)
