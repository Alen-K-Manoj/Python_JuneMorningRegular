Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = []
>>> for i in range(1,1001):
	if i % 2 == 0:
		a.append(i)

		
>>> a
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 256, 258, 260, 262, 264, 266, 268, 270, 272, 274, 276, 278, 280, 282, 284, 286, 288, 290, 292, 294, 296, 298, 300, 302, 304, 306, 308, 310, 312, 314, 316, 318, 320, 322, 324, 326, 328, 330, 332, 334, 336, 338, 340, 342, 344, 346, 348, 350, 352, 354, 356, 358, 360, 362, 364, 366, 368, 370, 372, 374, 376, 378, 380, 382, 384, 386, 388, 390, 392, 394, 396, 398, 400, 402, 404, 406, 408, 410, 412, 414, 416, 418, 420, 422, 424, 426, 428, 430, 432, 434, 436, 438, 440, 442, 444, 446, 448, 450, 452, 454, 456, 458, 460, 462, 464, 466, 468, 470, 472, 474, 476, 478, 480, 482, 484, 486, 488, 490, 492, 494, 496, 498, 500, 502, 504, 506, 508, 510, 512, 514, 516, 518, 520, 522, 524, 526, 528, 530, 532, 534, 536, 538, 540, 542, 544, 546, 548, 550, 552, 554, 556, 558, 560, 562, 564, 566, 568, 570, 572, 574, 576, 578, 580, 582, 584, 586, 588, 590, 592, 594, 596, 598, 600, 602, 604, 606, 608, 610, 612, 614, 616, 618, 620, 622, 624, 626, 628, 630, 632, 634, 636, 638, 640, 642, 644, 646, 648, 650, 652, 654, 656, 658, 660, 662, 664, 666, 668, 670, 672, 674, 676, 678, 680, 682, 684, 686, 688, 690, 692, 694, 696, 698, 700, 702, 704, 706, 708, 710, 712, 714, 716, 718, 720, 722, 724, 726, 728, 730, 732, 734, 736, 738, 740, 742, 744, 746, 748, 750, 752, 754, 756, 758, 760, 762, 764, 766, 768, 770, 772, 774, 776, 778, 780, 782, 784, 786, 788, 790, 792, 794, 796, 798, 800, 802, 804, 806, 808, 810, 812, 814, 816, 818, 820, 822, 824, 826, 828, 830, 832, 834, 836, 838, 840, 842, 844, 846, 848, 850, 852, 854, 856, 858, 860, 862, 864, 866, 868, 870, 872, 874, 876, 878, 880, 882, 884, 886, 888, 890, 892, 894, 896, 898, 900, 902, 904, 906, 908, 910, 912, 914, 916, 918, 920, 922, 924, 926, 928, 930, 932, 934, 936, 938, 940, 942, 944, 946, 948, 950, 952, 954, 956, 958, 960, 962, 964, 966, 968, 970, 972, 974, 976, 978, 980, 982, 984, 986, 988, 990, 992, 994, 996, 998, 1000]
>>> a = [i for i in range(1,51)]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
>>> a = [i for i in range(1,51) if i % 2 == 0]
>>> a
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> import time
>>> a = []
>>> temp_conv = lambda c : 9/5 * c + 32
>>> temp_conv(34.5)
94.1
>>> import os
>>> os.getcwd()
'C:\\Python36'
>>> os.chdir('C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\June_2018\Python_MorningRegular')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.chdir(r'C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\June_2018\Python_MorningRegular')
>>> os.getcwd()
'C:\\Users\\asus\\Documents\\Data\\DataTransfer\\BMPL_Batches\\June_2018\\Python_MorningRegular'
>>> import pandas
>>> dataset = pandas.read_csv('matches.csv')
>>> dataset.shape
(577, 18)
>>> dataset.head()
   id  season        city        date                  team1  \
0   1    2008   Bangalore  2008-04-18  Kolkata Knight Riders   
1   2    2008  Chandigarh  2008-04-19    Chennai Super Kings   
2   3    2008       Delhi  2008-04-19       Rajasthan Royals   
3   4    2008      Mumbai  2008-04-20         Mumbai Indians   
4   5    2008     Kolkata  2008-04-20        Deccan Chargers   

                         team2                  toss_winner toss_decision  \
0  Royal Challengers Bangalore  Royal Challengers Bangalore         field   
1              Kings XI Punjab          Chennai Super Kings           bat   
2             Delhi Daredevils             Rajasthan Royals           bat   
3  Royal Challengers Bangalore               Mumbai Indians           bat   
4        Kolkata Knight Riders              Deccan Chargers           bat   

   result  dl_applied                       winner  win_by_runs  \
0  normal           0        Kolkata Knight Riders          140   
1  normal           0          Chennai Super Kings           33   
2  normal           0             Delhi Daredevils            0   
3  normal           0  Royal Challengers Bangalore            0   
4  normal           0        Kolkata Knight Riders            0   

   win_by_wickets player_of_match                                       venue  \
0               0     BB McCullum                       M Chinnaswamy Stadium   
1               0      MEK Hussey  Punjab Cricket Association Stadium, Mohali   
2               9     MF Maharoof                            Feroz Shah Kotla   
3               5      MV Boucher                            Wankhede Stadium   
4               5       DJ Hussey                                Eden Gardens   

     umpire1         umpire2  umpire3  
0  Asad Rauf     RE Koertzen      NaN  
1  MR Benson      SL Shastri      NaN  
2  Aleem Dar  GA Pratapkumar      NaN  
3   SJ Davis       DJ Harper      NaN  
4  BF Bowden     K Hariharan      NaN  
>>> dataset[dataset['player_of_match'] == 'BB McCullum']
      id  season       city        date                  team1  \
0      1    2008  Bangalore  2008-04-18  Kolkata Knight Riders   
187  188    2011     Mumbai  2011-04-15         Mumbai Indians   
192  193    2011      Kochi  2011-04-18    Chennai Super Kings   
461  462    2015    Chennai  2015-04-11    Chennai Super Kings   
482  483    2015    Chennai  2015-04-25    Chennai Super Kings   

                           team2                  toss_winner toss_decision  \
0    Royal Challengers Bangalore  Royal Challengers Bangalore         field   
187         Kochi Tuskers Kerala         Kochi Tuskers Kerala         field   
192         Kochi Tuskers Kerala         Kochi Tuskers Kerala         field   
461          Sunrisers Hyderabad          Chennai Super Kings           bat   
482              Kings XI Punjab          Chennai Super Kings           bat   

     result  dl_applied                 winner  win_by_runs  win_by_wickets  \
0    normal           0  Kolkata Knight Riders          140               0   
187  normal           0   Kochi Tuskers Kerala            0               8   
192  normal           1   Kochi Tuskers Kerala            0               7   
461  normal           0    Chennai Super Kings           45               0   
482  normal           0    Chennai Super Kings           97               0   

    player_of_match                            venue         umpire1  \
0       BB McCullum            M Chinnaswamy Stadium       Asad Rauf   
187     BB McCullum                 Wankhede Stadium     BR Doctrove   
192     BB McCullum                    Nehru Stadium     K Hariharan   
461     BB McCullum  MA Chidambaram Stadium, Chepauk  RK Illingworth   
482     BB McCullum  MA Chidambaram Stadium, Chepauk       JD Cloete   

           umpire2  umpire3  
0      RE Koertzen      NaN  
187     PR Reiffel      NaN  
192        AL Hill      NaN  
461    VA Kulkarni      NaN  
482  C Shamshuddin      NaN  
>>> 
