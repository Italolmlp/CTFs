from z3 import *

def rotl(x, n):
    tamanho = 32
    x = ((x << n) | LShR(x, (tamanho - n)))
    return x
def rotr(x, n):
    tamanho = 32
    x = (LShR(x, n) | x << (tamanho - n))
    return x
def main():
    print('[+] Creating Z3 model')

    flag = [BitVec(f'X_{i:2}', 32) for i in range(40)]
    s = Solver()

    for i in flag:
        s.add(i >= 0)
        s.add(i < 128)
  
    for i, c in enumerate('HTB{'):
        s.add(flag[i] == ord(c))
    s.add(flag[-1] == ord('}'))

    regs = [BitVecVal(0, 32) * 0  for i in range(15)]
    
    regs[13] *= 10
    regs[0] = regs[0] = BitVecVal(0, 32) * 0 
    regs[13] = flag[13]
    regs[14] = flag[0]
    regs[14] <<= 0
    regs[0] |= regs[14]
    regs[14] = flag[1]
    regs[11] &= regs[11]
    regs[14] <<= 8
    regs[0] |= regs[14]
    regs[14] = flag[2]
    regs[10] ^= 11
    regs[14] <<= 16
    regs[12] = rotl(regs[12], 11)
    regs[0] |= regs[14]
    regs[14] = flag[3]
    regs[11] = flag[11]
    regs[14] <<= 24
    regs[10] *= regs[10]
    regs[0] |= regs[14]
    regs[11] ^= 13
    regs[1] = regs[1] = BitVecVal(0, 32) * 0 
    regs[14] = flag[4]
    regs[14] <<= 0
    regs[1] |= regs[14]
    regs[11] &= 12
    regs[14] = flag[5]
    regs[10] += 10
    regs[14] <<= 8
    regs[12] -= regs[11]
    regs[1] |= regs[14]
    regs[14] = flag[6]
    regs[12] = flag[10]
    regs[14] <<= 16
    regs[10] += regs[13]
    regs[1] |= regs[14]
    regs[14] = flag[7]
    regs[12] *= regs[12]
    regs[14] <<= 24
    regs[1] |= regs[14]
    regs[2] = regs[2] = BitVecVal(0, 32) * 0 
    regs[13] = regs[13] = regs[13]
    regs[14] = flag[8]
    regs[14] <<= 0
    regs[10] = rotl(regs[10], regs[11])
    regs[2] |= regs[14]
    regs[12] &= 10
    regs[14] = flag[9]
    regs[11] += 11
    regs[14] <<= 8
    regs[2] |= regs[14]
    regs[14] = flag[10]
    regs[11] |= 12
    regs[14] <<= 16
    regs[2] |= regs[14]
    regs[14] = flag[11]
    regs[14] <<= 24
    regs[13] |= 12
    regs[2] |= regs[14]
    regs[3] = regs[3] = BitVecVal(0, 32) * 0 
    regs[14] = flag[12]
    regs[10] *= regs[11]
    regs[14] <<= 0
    regs[10] = rotr(regs[10], 10)
    regs[3] |= regs[14]
    regs[11] |= regs[12]
    regs[14] = flag[13]
    regs[10] *= 13
    regs[14] <<= 8
    regs[10] ^= 13
    regs[3] |= regs[14]
    regs[11] = regs[11] = regs[11]
    regs[14] = flag[14]
    regs[14] <<= 16
    regs[13] = rotl(regs[13], 11)
    regs[3] |= regs[14]
    regs[11] &= 13
    regs[14] = flag[15]
    regs[14] <<= 24
    regs[11] |= 10
    regs[3] |= regs[14]
    regs[4] = regs[4] = BitVecVal(0, 32) * 0 
    regs[14] = flag[16]
    regs[10] &= 10
    regs[14] <<= 0
    regs[4] |= regs[14]
    regs[14] = flag[17]
    regs[13] *= 13
    regs[14] <<= 8
    regs[11] = rotl(regs[11], regs[10])
    regs[4] |= regs[14]
    regs[14] = flag[18]
    regs[13] = rotr(regs[13], regs[12])
    regs[14] <<= 16
    regs[4] |= regs[14]
    regs[14] = flag[19]
    regs[14] <<= 24
    regs[12] = regs[12] = BitVecVal(0, 32) * 0 
    regs[4] |= regs[14]
    regs[13] *= regs[10]
    regs[5] = regs[5] = BitVecVal(0, 32) * 0 
    regs[14] = flag[20]
    regs[10] = rotl(regs[10], regs[13])
    regs[14] <<= 0
    regs[5] |= regs[14]
    regs[14] = flag[21]
    regs[14] <<= 8
    regs[13] += 13
    regs[5] |= regs[14]
    regs[14] = flag[22]
    regs[13] = rotr(regs[13], 11)
    regs[14] <<= 16
    regs[10] -= 13
    regs[5] |= regs[14]
    regs[10] &= regs[12]
    regs[14] = flag[23]
    regs[13] = rotl(regs[13], regs[10])
    regs[14] <<= 24
    regs[5] |= regs[14]
    regs[12] = rotr(regs[12], regs[10])
    regs[6] = regs[6] = BitVecVal(0, 32) * 0 
    regs[11] = rotr(regs[11], 10)
    regs[14] = flag[24]
    regs[14] <<= 0
    regs[11] -= 10
    regs[6] |= regs[14]
    regs[14] = flag[25]
    regs[14] <<= 8
    regs[10] &= regs[12]
    regs[6] |= regs[14]
    regs[14] = flag[26]
    regs[12] = rotr(regs[12], 11)
    regs[14] <<= 16
    regs[11] ^= regs[10]
    regs[6] |= regs[14]
    regs[14] = flag[27]
    regs[12] |= 13
    regs[14] <<= 24
    regs[6] |= regs[14]
    regs[7] = regs[7] = BitVecVal(0, 32) * 0 
    regs[14] = flag[28]
    regs[13] = regs[13] = BitVecVal(0, 32) * 0 
    regs[14] <<= 0
    regs[12] &= regs[11]
    regs[7] |= regs[14]
    regs[11] = rotr(regs[11], regs[10])
    regs[14] = flag[29]
    regs[14] <<= 8
    regs[7] |= regs[14]
    regs[14] = flag[30]
    regs[10] *= 10
    regs[14] <<= 16
    regs[7] |= regs[14]
    regs[14] = flag[31]
    regs[10] = regs[10] = regs[10]
    regs[14] <<= 24
    regs[7] |= regs[14]
    regs[8] = regs[8] = BitVecVal(0, 32) * 0 
    regs[10] = rotl(regs[10], 12)
    regs[14] = flag[32]
    regs[11] += regs[11]
    regs[14] <<= 0
    regs[12] = regs[12] = BitVecVal(0, 32) * 0 
    regs[8] |= regs[14]
    regs[14] = flag[33]
    regs[14] <<= 8
    regs[10] = rotl(regs[10], regs[13])
    regs[8] |= regs[14]
    regs[12] += 13
    regs[14] = flag[34]
    regs[14] <<= 16
    regs[8] |= regs[14]
    regs[10] += 10
    regs[14] = flag[35]
    regs[14] <<= 24
    regs[13] = regs[13] = BitVecVal(0, 32) * 0 
    regs[8] |= regs[14]
    regs[12] = flag[10]
    regs[9] = regs[9] = BitVecVal(0, 32) * 0 
    regs[14] = flag[36]
    regs[14] <<= 0
    regs[9] |= regs[14]
    regs[11] = rotr(regs[11], regs[11])
    regs[14] = flag[37]
    regs[14] <<= 8
    regs[9] |= regs[14]
    regs[10] |= 11
    regs[14] = flag[38]
    regs[11] *= regs[13]
    regs[14] <<= 16
    regs[9] |= regs[14]
    regs[14] = flag[39]
    regs[11] -= 10
    regs[14] <<= 24
    regs[13] = regs[13] = regs[13]
    regs[9] |= regs[14]
    regs[12] &= 11
    regs[14] = regs[14] = BitVecVal(0, 32) * 0 
    regs[0] += 2769503260
    regs[0] -= 997841014
    regs[12] = rotl(regs[12], regs[11])
    regs[0] ^= 4065997671
    regs[13] |= regs[11]
    regs[0] += 690011675
    regs[0] += 540576667
    regs[0] ^= 1618285201
    regs[0] += 1123989331
    regs[0] += 1914950564
    regs[0] += 4213669998
    regs[13] = regs[13] = BitVecVal(0, 32) * 0 
    regs[0] += 1529621790
    regs[0] -= 865446746
    regs[10] ^= 11
    regs[0] += 449019059
    regs[13] = rotr(regs[13], 11)
    regs[0] += 906976959
    regs[10] &= 10
    regs[0] += 892028723
    regs[0] -= 1040131328
    regs[0] ^= 3854135066
    regs[0] ^= 4133925041
    regs[0] ^= 1738396966
    regs[12] ^= 12
    regs[0] += 550277338
    regs[0] -= 1043160697
    regs[1] ^= 1176768057
    regs[1] -= 2368952475
    regs[12] += 11
    regs[1] ^= 2826144967
    regs[1] += 1275301297
    regs[1] -= 2955899422
    regs[1] ^= 2241699318
    regs[11] *= 10
    regs[1] += 537794314
    regs[13] -= regs[10]
    regs[1] += 473021534
    regs[12] = rotr(regs[12], regs[13])
    regs[1] += 2381227371
    regs[1] -= 3973380876
    regs[1] -= 1728990628
    regs[11] &= 13
    regs[1] += 2974252696
    regs[11] = flag[11]
    regs[1] += 1912236055
    regs[1] ^= 3620744853
    regs[10] ^= regs[13]
    regs[1] ^= 2628426447
    regs[13] -= regs[12]
    regs[1] -= 486914414
    regs[11] = rotr(regs[11], 12)
    regs[1] -= 1187047173
    regs[2] ^= 3103274804
    regs[10] *= regs[10]
    regs[2] += 3320200805
    regs[2] += 3846589389
    regs[13] = BitVecVal(13, 32) * 1
    regs[2] ^= 2724573159
    regs[2] -= 1483327425
    regs[2] ^= 1957985324
    regs[2] -= 1467602691
    regs[2] += 3142557962
    regs[13] ^= 12
    regs[2] ^= 2525769395
    regs[2] += 3681119483
    regs[12] += 11
    regs[2] -= 1041439413
    regs[2] -= 1042206298
    regs[2] ^= 527001246
    regs[10] = regs[10] = regs[13]
    regs[2] -= 855860613
    regs[10] += 10
    regs[2] += 1865979270
    regs[13] = BitVecVal(10, 32) * 1
    regs[2] += 2752636085
    regs[2] ^= 1389650363
    regs[2] -= 2721642985
    regs[10] = rotl(regs[10], 11)
    regs[2] += 3276518041
    regs[2] ^= 1965130376
    regs[3] ^= 3557111558
    regs[3] ^= 3031574352
    regs[12] = rotr(regs[12], 10)
    regs[3] -= 4226755821
    regs[3] += 2624879637
    regs[3] += 1381275708
    regs[3] ^= 3310620882
    regs[3] ^= 2475591380
    regs[3] += 405408383
    regs[3] ^= 2291319543
    regs[12] = flag[12]
    regs[3] += 4144538489
    regs[3] ^= 3878256896
    regs[11] &= 10
    regs[3] -= 2243529248
    regs[3] -= 561931268
    regs[11] -= regs[12]
    regs[3] -= 3076955709
    regs[12] = rotl(regs[12], 13)
    regs[3] += 2019584073
    regs[13] -= 12
    regs[3] += 1712479912
    regs[11] = rotl(regs[11], 11)
    regs[3] ^= 2804447380
    regs[10] = rotr(regs[10], regs[10])
    regs[3] -= 2957126100
    regs[13] = rotl(regs[13], 13)
    regs[3] += 1368187437
    regs[10] = rotr(regs[10], regs[12])
    regs[3] += 3586129298
    regs[4] -= 1229526732
    regs[11] = rotl(regs[11], regs[11])
    regs[4] -= 2759768797
    regs[10] = BitVecVal(13, 32) * 1
    regs[4] ^= 2112449396
    regs[4] -= 1212917601
    regs[4] ^= 1524771736
    regs[4] += 3146530277
    regs[4] ^= 2997906889
    regs[12] = rotr(regs[12], 10)
    regs[4] += 4135691751
    regs[4] += 1960868242
    regs[12] &= 12
    regs[4] -= 2775657353
    regs[10] = rotr(regs[10], 13)
    regs[4] += 1451259226
    regs[4] += 607382171
    regs[13] *= regs[13]
    regs[4] -= 357643050
    regs[4] ^= 2020402776
    regs[5] += 2408165152
    regs[12] *= regs[10]
    regs[5] ^= 806913563
    regs[5] -= 772591592
    regs[13] = regs[13] = regs[11]
    regs[5] ^= 2211018781
    regs[5] -= 2523354879
    regs[5] += 2549720391
    regs[5] ^= 3908178996
    regs[5] ^= 1299171929
    regs[5] += 512513885
    regs[5] -= 2617924552
    regs[12] = BitVecVal(13, 32) * 1
    regs[5] += 390960442
    regs[11] *= 13
    regs[5] += 1248271133
    regs[5] += 2114382155
    regs[10] = BitVecVal(13, 32) * 1
    regs[5] -= 2078863299
    regs[12] = regs[12] = regs[12]
    regs[5] += 2857504053
    regs[5] -= 4271947727
    regs[6] ^= 2238126367
    regs[6] ^= 1544827193
    regs[6] += 4094800187
    regs[6] ^= 3461906189
    regs[6] -= 1812592759
    regs[6] ^= 1506702473
    regs[6] += 536175198
    regs[6] ^= 1303821297
    regs[6] += 715409343
    regs[6] ^= 4094566992
    regs[6] ^= 1890141105
    regs[13] = flag[13]
    regs[6] ^= 3143319360
    regs[7] -= 696930856
    regs[7] ^= 926450200
    regs[7] += 352056373
    regs[13] = regs[13] = regs[11]
    regs[7] -= 3857703071
    regs[7] += 3212660135
    regs[12] |= regs[10]
    regs[7] -= 3854876250
    regs[12] = regs[12] = BitVecVal(0, 32) * 0 
    regs[7] += 3648688720
    regs[7] ^= 2732629817
    regs[10] |= 12
    regs[7] -= 2285138643
    regs[10] = rotl(regs[10], 13)
    regs[7] ^= 2255852466
    regs[7] ^= 2537336944
    regs[10] ^= regs[13]
    regs[7] ^= 4257606405
    regs[8] -= 3703184638
    regs[11] &= regs[10]
    regs[8] -= 2165056562
    regs[8] += 2217220568
    regs[10] = rotl(regs[10], regs[12])
    regs[8] += 2088084496
    regs[8] += 443074220
    regs[13] = rotr(regs[13], 12)
    regs[8] -= 1298336973
    regs[13] ^= 11
    regs[8] += 822378456
    regs[11] = rotl(regs[11], regs[12])
    regs[8] += 2154711985
    regs[11] = flag[12]
    regs[8] -= 430757325
    regs[12] ^= 10
    regs[8] ^= 2521672196
    regs[9] -= 532704100
    regs[9] -= 2519542932
    regs[9] ^= 2451309277
    regs[9] ^= 3957445476
    regs[10] |= regs[10]
    regs[9] += 2583554449
    regs[9] -= 1149665327
    regs[13] *= 12
    regs[9] += 3053959226
    regs[10] = flag[10]
    regs[9] += 3693780276
    regs[9] ^= 609918789
    regs[9] ^= 2778221635
    regs[13] = rotr(regs[13], 10)
    regs[9] += 3133754553
    regs[11] += 13
    regs[9] += 3961507338
    regs[9] ^= 1829237263
    regs[11] = rotr(regs[11], 13)
    regs[9] ^= 2472519933
    regs[12] &= 12
    regs[9] += 4061630846
    regs[9] -= 1181684786
    regs[10] *= regs[11]
    regs[9] -= 390349075
    regs[9] += 2883917626
    regs[9] -= 3733394420
    regs[12] -= 12
    regs[9] ^= 3895283827
    regs[10] = regs[10] = regs[11]
    regs[9] ^= 2257053750
    regs[9] -= 2770821931
    regs[10] = rotl(regs[10], 13)
    regs[9] ^= 477834410
    regs[13] = rotl(regs[13], regs[12])
    regs[0] ^= regs[1]
    regs[12] *= 12
    regs[1] ^= regs[2]
    regs[13] -= regs[11]
    regs[2] ^= regs[3]
    regs[3] ^= regs[4]
    regs[4] ^= regs[5]
    regs[13] = BitVecVal(13, 32) * 1
    regs[5] ^= regs[6]
    regs[11] &= regs[11]
    regs[6] ^= regs[7]
    regs[10] |= 12
    regs[7] ^= regs[8]
    regs[12] = rotl(regs[12], 12)
    regs[8] ^= regs[9]
    regs[12] = regs[12] = BitVecVal(0, 32) * 0 
    regs[9] ^= regs[10]   
    for i in range(15):
        print("Expressao", i)
        print(regs[i])
    
    s.add(regs[0] == 0x3ee88722)
    s.add(regs[1] == 0xecbdbe2)
    s.add(regs[2] == 0x60b843c4)
    s.add(regs[3] == 0x5da67c7)
    s.add(regs[4] == 0x171ef1e9)
    s.add(regs[5] == 0x52d5b3f7)
    s.add(regs[6] == 0x3ae718c0)
    s.add(regs[7] == 0x8b4aacc2)
    s.add(regs[8] == 0xe5cf78dd)
    s.add(regs[9] == 0x4a848edf)
    s.add(regs[10] == 0x8f)
    s.add(regs[11] == 0x4180000)
    s.add(regs[12] == 0x0)
    s.add(regs[13] == 0xd)
    s.add(regs[14] == 0x0)
    print('[+] Verifying model satisfiability')
    if s.check() == sat:
        print("Satisfiable")

    print('[*] Running model')
    
    print(s.check())

    if s.check() == sat:
        m = s.model()
        print(m)

if __name__ == '__main__':
    main()
