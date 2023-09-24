
import matplotlib.pyplot as plt
import numpy as np
import math

#video
data = {'cpu': [0.0, 0.0, 100.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 102.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 104.4, 0.0, 0.0, 0.0, 102.6, 0.0, 0.0, 0.0, 0.0, 101.9, 0.0, 0.0, 0.0, 0.0, 205.4, 0.0, 102.1, 0.0, 0.0, 0.0, 0.0, 102.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 99.9, 0.0, 0.0, 0.0, 99.4, 103.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 102.9, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 103.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 99.9, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 99.7, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 101.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.9, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 204.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.9, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.9, 0.0, 0.0, 0.0, 0.0, 0.0, 102.7, 102.1, 0.0, 98.4, 0.0, 102.4, 0.0, 0.0, 0.0, 101.8, 0.0, 0.0, 0.0, 101.4, 206.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 103.5, 100.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.7, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.3, 0.0, 0.0, 0.0, 0.0, 0.0, 101.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 101.2, 0.0, 0.0, 0.0, 101.6, 101.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.4, 100.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 102.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 101.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 101.0, 101.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.4, 103.5, 0.0, 0.0, 0.0, 101.0, 100.8, 0.0, 0.0, 307.70000000000005, 0.0, 0.0, 0.0, 0.0, 204.10000000000002, 0.0, 0.0], 'network': [483466, 0, 0, 0, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2612, 275966, 159008, 497, 1580, 580, 0, 0, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 33816, 403430, 756675, 539329, 218428, 3257, 219405, 857296, 218776, 0, 2128, 82716, 361648, 186572, 0, 1717, 1786, 3254, 4955, 965740, 138700, 590949, 658601, 42340, 0, 0, 0, 0, 0, 0, 1832, 580, 0, 0, 1096, 1972, 418, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 943, 0, 1945, 0, 0, 15027, 131330, 46068, 0, 188915, 522408, 457012, 457012, 522224, 456946, 456946, 522224, 457078, 456946, 522224, 457078, 456946, 522290, 457078, 456946, 522224, 457012, 456946, 522290, 456946, 457012, 522290, 457078, 457012, 522290, 457144, 456946, 522356, 456946, 457012, 522290, 456946, 522158, 457012, 456946, 522158, 457012, 457012, 522224, 457012, 457012, 65440, 0, 0, 0, 910, 1438, 0, 0, 2419, 0, 0, 850, 1687, 0, 0, 853, 1821, 0, 0, 2795, 0, 0, 1791, 1311, 1341, 2330, 4021, 649397, 858738, 547098, 649050, 673720, 681912, 641240, 657822, 592478, 593874, 582772, 584168, 600788, 592426, 592478, 592478, 600788, 600788, 575858, 587116, 589582, 600788, 592478, 592478, 592478, 592478, 609098, 600788, 584168, 584168, 600788, 592478, 477366, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15411, 458258, 522158, 457210, 456946, 522224, 456946, 457012, 141850, 0, 0, 795, 393634, 456946, 456946, 522224, 457078, 456946, 522224, 456946, 457012, 522356, 456946, 317003, 0, 0, 486, 133041, 326376, 457012, 522290, 456946, 456946, 522224, 456946, 457144, 522224, 457012, 456946, 251976, 0, 0, 795, 263300, 261230, 522290, 456946, 456946, 522224, 456946, 457012, 522356, 456946, 456946, 522290, 120775, 0, 0, 795, 4754, 0, 0, 0, 2089, 2334, 8831, 6821, 4976, 1322616, 3232462, 2474910, 2307164, 2461288, 2297422, 1758750, 1882980, 1735611, 594265, 0, 0, 0, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16168, 327806, 93376, 0, 0, 549, 1581, 580, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45839, 517870, 917881, 333602, 137156, 0, 0, 2128, 2904, 161258, 554412, 576726, 0, 0, 0, 3428, 103075, 428592, 132914, 0, 0, 0, 2126, 3561, 1718, 2976, 449359, 565417, 101092, 565941, 638873, 88072, 0, 0, 0, 0, 52, 0, 1832, 580, 0, 0, 3057, 0, 0, 209, 418, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1330, 0, 2077, 192241, 0, 290761, 456946, 522224, 457012, 456946, 522224, 456946, 456946, 522224, 456946, 456946, 522224, 456946, 456946, 522224, 456946, 457078, 522224, 456946, 456946, 522290, 457012, 456946, 522224, 457012, 456946, 522356, 457012, 457012, 522356, 456946, 456946, 522224, 457012, 456946, 522224, 456946, 456946, 522290, 457078, 456946, 486134, 0, 0, 0, 1745, 471, 2353, 0, 2405, 66, 2608, 0, 2663, 66, 1551, 1433, 2990, 529379, 852594, 583102, 582998, 607772, 558620, 575512, 591704, 534632, 509910, 518168, 518116, 526426, 509858, 518168, 526426, 477202, 526544, 542994, 534684, 501548, 518168, 502028, 526374, 518064, 485084, 518492, 509910, 526374, 526374, 501600, 518168, 518168, 526478, 543046, 526426, 534750, 136092, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15411, 458022, 522408, 457012, 457012, 522290, 456946, 456946, 141850, 0, 133501, 456880, 522224, 456946, 456946, 522224, 457012, 456946, 522224, 456946, 456946, 522290, 55891, 0, 68315, 457064, 522224, 456946, 457012, 522224, 456946, 457012, 522290, 456946, 456946, 522356, 121354, 0, 795, 394106, 522224, 456946, 456946, 522224, 456946, 456946, 522224, 456946, 456946, 522224, 251265, 0, 0, 5483, 66, 0, 2090, 1980, 10603, 26267, 1375488, 3226522, 2255844, 2072362, 2248152, 2207170, 1698128, 1670246, 1656302, 1265673, 351007, 0, 0, 0]}

#wc
data = {'cpu': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 101.1, 0.0, 0.0, 0.0, 0.0, 315.9, 525.5999999999999, 628.1, 406.1, 511.3, 202.3, 510.8, 103.3, 201.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 101.7, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.9, 0.0, 101.2, 100.6, 0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 212.0, 309.3, 512.1, 719.9, 517.4, 315.7, 407.70000000000005, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 99.9, 0.0, 101.5, 100.3, 101.5, 0.0, 0.0, 101.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.9, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 513.9, 609.3000000000001, 409.79999999999995, 515.7, 304.8, 306.8, 105.9, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 101.6, 0.0, 103.7, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.9, 101.2, 100.8, 0.0, 0.0, 0.0, 101.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 308.90000000000003, 514.9, 308.5, 823.5, 425.4, 299.6, 207.2, 100.9, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 98.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 101.0, 99.9, 0.0, 0.0, 0.0, 0.0, 101.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.3, 101.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.8, 0.0, 0.0, 100.7, 102.4, 491.90000000000003, 417.7, 615.5, 314.7, 603.6, 205.9, 100.7, 97.6, 0.0, 104.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.9, 99.9, 101.4, 0.0, 0.0, 0.0, 0.0, 100.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 202.7, 414.2, 631.0000000000001, 628.6, 422.69999999999993, 407.8, 413.4, 409.40000000000003, 102.5, 0.0, 0.0, 0.0, 0.0, 103.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.9, 101.2, 101.5, 0.0, 0.0, 0.0, 100.8, 0.0, 0.0, 0.0, 0.0, 0.0, 101.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 205.89999999999998, 209.10000000000002, 417.5, 411.3, 624.4, 199.3, 309.9, 101.6, 0.0, 106.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 103.3, 0.0, 105.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.9, 101.7, 101.3, 0.0, 0.0, 0.0, 0.0, 101.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 204.1, 202.60000000000002, 103.0, 516.1, 623.0999999999999, 428.5, 408.4, 518.5, 312.90000000000003, 101.4, 0.0, 97.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 106.1, 0.0, 100.0, 101.4, 101.0, 0.0, 0.0, 0.0, 100.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'network': [329, 66, 67856, 249387, 142696, 103538, 43121, 66, 68060, 77612, 1343, 6086, 905779, 927130, 1584522, 61915, 246516, 146510, 157258, 283523, 45840, 99167, 348427, 172368, 39486, 83171, 366587, 28335, 1693, 346627, 18246, 132, 52950, 203827, 132, 1560, 130164, 66, 66, 1570, 11253, 744675, 0, 1161, 0, 1097, 2181, 40984, 287834, 121852, 20144, 66, 148546, 245330, 35128, 66, 66, 313215, 113528, 92426, 96664, 132, 66, 144222, 132, 242765, 149946, 61268, 66, 66, 312998, 78808, 105268, 58543, 66, 66, 133200, 261633, 90046, 117310, 4357, 0, 145672, 66, 1345, 86488, 1326336, 1077980, 993460, 41065, 242687, 160225, 36827, 300004, 334619, 1814, 222210, 216717, 154472, 106108, 52685, 328393, 1825, 66, 297764, 74258, 66, 4062, 245245, 132, 557, 131315, 132, 0, 1568, 10617, 746449, 0, 1161, 0, 1045, 2181, 2977, 333495, 120316, 14092, 66, 132546, 244368, 52142, 66, 66, 313215, 78808, 127080, 83210, 13652, 66, 67444, 76844, 132993, 241680, 79424, 66, 66, 253636, 137976, 70354, 93571, 132, 66, 799, 318170, 139696, 100414, 47217, 66, 2554, 143118, 1412, 5919, 906474, 1180630, 1391109, 4856, 363586, 120158, 32102, 351295, 235603, 54250, 61133, 290408, 242532, 1703, 205391, 263885, 15862, 2374, 207263, 164315, 198, 2744, 246520, 132, 66, 131478, 132, 66, 1569, 2929, 753717, 52, 1161, 0, 209, 3017, 1431, 318759, 100420, 50204, 66, 857, 317581, 110010, 726, 66, 207869, 183524, 90620, 110204, 23564, 66, 810, 143478, 132927, 212592, 108762, 132, 66, 253764, 137976, 89212, 74599, 132, 66, 2281, 316754, 141938, 103292, 42097, 66, 68126, 77546, 1344, 8360, 1233605, 1155124, 1086415, 58689, 228362, 134333, 324761, 236960, 39500, 105829, 476707, 10834, 2301, 210897, 274427, 198, 2813, 349387, 21440, 66, 186597, 70066, 132, 19456, 112030, 66, 1399, 2943, 654039, 99470, 1162, 0, 209, 3017, 1431, 273375, 115386, 80556, 132, 0, 316902, 101178, 11160, 66, 148671, 226080, 109170, 95176, 36854, 66, 0, 144288, 2077, 316498, 135574, 198, 66, 179560, 165903, 116053, 79432, 14721, 66, 0, 314160, 101700, 126891, 63611, 66, 66, 145606, 1411, 5919, 982852, 1143292, 1350521, 29283, 257325, 1577, 1458, 425139, 135689, 2073, 126331, 462749, 2672, 2208, 305104, 175618, 264, 43749, 305860, 24522, 1624, 129307, 118426, 132, 2801, 128861, 66, 0, 2965, 248188, 506564, 0, 1160, 0, 209, 3017, 1431, 327733, 119866, 21770, 66, 67254, 251184, 110670, 132, 0, 242909, 150714, 97660, 115570, 9046, 66, 67444, 76844, 132993, 241038, 80250, 66, 66, 253636, 137976, 69970, 93118, 969, 66, 67856, 250345, 143080, 101874, 43377, 66, 133338, 12334, 1345, 144656, 1267700, 892728, 1179704, 104770, 181734, 1695, 62232, 426992, 88857, 93387, 241877, 261626, 60025, 2735, 386264, 93421, 198, 43809, 322127, 198, 66, 240330, 16248, 132, 2744, 128861, 66, 0, 2736, 18232, 737196, 0, 1161, 0, 209, 3017, 1996, 338444, 116410, 14030, 66, 67150, 250222, 111514, 66, 66, 291539, 101520, 125416, 83338, 14100, 66, 67510, 76778, 132993, 242064, 79106, 66, 66, 254020, 140526, 88254, 73001, 66, 66, 2281, 315986, 139762, 102230, 46169, 66, 68126, 77612, 1345, 7996, 1067261, 1082188, 1042742, 316268, 342533, 1918, 198512, 264751, 205378, 145642, 50796, 297051, 52107, 237361, 124591, 113558, 84572, 140679, 124789, 2875, 112432, 124880, 1628, 0, 125084, 66, 0, 2726, 18232, 736950, 0, 1162, 0, 209, 3017, 1431, 325847, 100932, 42788, 66, 923, 316505, 111576, 132, 66, 242857, 150970, 87942, 117874, 16086, 66, 67444, 76844, 132993, 242508, 78596, 66, 66, 295406, 96272, 89914, 73108, 969, 66, 133134, 224599, 102078, 124714, 22073, 66, 133404, 12268, 1346, 86908, 1443382, 1050871, 901829, 94282, 128720, 65055, 129379, 356663, 76659, 127797, 260011, 277077, 198, 84732, 354580, 47926, 198, 84754, 277537, 198, 2865, 242255, 198, 556, 130983, 132, 66, 1569, 8156, 747824, 0, 1161, 0, 209, 3017, 1431, 291313, 95376, 82628, 132, 0, 317618, 103738, 7832, 66, 178881, 195498, 107634, 99400, 34434, 66, 810, 143478, 67649, 243564, 142766, 132, 66, 208614, 165600, 88264, 93059, 132, 66, 799, 318170, 127740]}

#IR
# data = {'cpu': [204.8, 310.29999999999995, 100.1, 203.4, 101.0, 203.8, 403.9, 204.9, 100.7, 204.10000000000002, 201.9, 202.0, 306.3, 203.7, 202.3, 101.0, 100.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 199.9, 102.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 201.2, 0.0, 101.6, 0.0, 0.0, 0.0, 0.0, 0.0, 100.7, 100.4, 100.8, 100.5, 102.1, 100.9, 100.9, 100.4, 100.7, 100.6, 101.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 101.5, 202.5, 201.6, 201.3, 201.9, 201.3, 202.3, 201.5, 201.5, 201.2, 203.0, 201.4, 201.3, 201.9, 201.2, 201.8, 201.4, 201.7, 201.9, 202.0, 201.3, 100.7, 200.6, 100.7, 301.0, 99.8, 202.7, 202.8, 100.7, 301.79999999999995, 202.5, 201.6, 201.89999999999998, 201.2, 201.5, 202.2, 100.2, 303.5, 100.0, 202.5, 202.8, 200.4, 203.8, 505.2, 101.2, 100.3, 201.8, 201.2, 302.29999999999995, 201.39999999999998, 203.2, 200.8, 305.1, 201.5, 0.0, 0.0, 200.8, 203.2, 202.1, 202.0, 100.5, 403.0, 302.7, 100.8, 0.0, 102.0, 101.3, 202.5, 302.5, 203.60000000000002, 201.8, 301.8, 505.9, 0.0, 0.0, 201.7, 304.2, 715.9000000000001, 200.6, 407.6, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 698.5, 307.4, 401.4, 304.2, 402.3, 0.0, 0.0, 0.0, 0.0, 400.59999999999997, 305.4, 405.09999999999997, 200.8, 202.89999999999998, 201.39999999999998, 101.2, 100.4, 0.0, 0.0, 0.0, 203.1, 201.6, 202.9, 201.89999999999998, 201.2, 201.2, 101.9, 304.0, 102.2, 404.8, 102.0, 202.9, 202.7, 198.7, 102.7, 302.9, 101.6, 202.1, 202.4, 203.0, 201.5, 202.60000000000002, 100.4, 0.0, 0.0, 0.0, 101.6, 304.70000000000005, 101.5, 303.7, 101.4, 303.2, 101.2, 303.29999999999995, 100.6, 304.5, 100.9, 303.4, 99.8, 302.5, 100.5, 303.3, 100.3, 302.9, 202.2, 201.4, 100.0, 305.8, 99.9, 304.3, 100.2, 303.1, 100.4, 303.7, 100.2, 302.0, 101.3, 301.8, 101.1, 304.4, 99.8, 302.9, 100.7, 301.70000000000005, 100.9, 303.5, 99.9, 304.79999999999995, 99.7, 304.6, 100.3, 304.2, 100.2, 302.29999999999995, 100.2, 302.6, 99.7, 304.8, 100.3, 304.0, 100.0, 301.6, 101.5, 300.79999999999995, 100.3, 305.0, 100.3, 302.4, 99.8, 302.5, 101.3, 302.8, 202.2, 302.7, 304.2, 304.6, 201.0, 203.8, 101.1, 101.1, 102.0, 201.8, 103.3, 200.8, 203.5, 202.6, 203.7, 201.4, 203.8, 303.3, 302.79999999999995, 102.0, 98.2, 102.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.4, 100.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.5, 0.0, 100.7, 0.0, 0.0, 0.0, 0.0, 0.0, 101.0, 203.1, 101.9, 98.9, 102.2, 98.8, 101.7, 101.0, 101.6, 101.2, 99.7, 0.0, 0.0, 100.7, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.9, 102.7, 201.2, 202.8, 203.2, 201.39999999999998, 200.5, 201.9, 203.1, 200.5, 202.6, 201.7, 200.8, 203.3, 200.5, 201.5, 201.7, 200.8, 202.2, 200.89999999999998, 201.1, 201.3, 201.7, 201.4, 201.5, 302.4, 100.8, 201.7, 101.3, 201.39999999999998, 301.5, 202.5, 201.8, 100.3, 302.8, 202.5, 101.2, 100.6, 303.4, 200.60000000000002, 202.8, 297.8, 204.9, 405.9, 204.2, 0.0, 0.0, 202.8, 303.2, 204.1, 304.8, 200.60000000000002, 305.6, 99.3, 203.9, 0.0, 100.2, 202.2, 303.7, 303.2, 305.7, 201.10000000000002, 304.5, 202.8, 100.2, 0.0, 0.0, 202.60000000000002, 201.4, 203.4, 303.4, 304.3, 407.6, 303.0, 0.0, 0.0, 101.0, 469.5, 629.5, 100.8, 203.3, 200.3, 0.0, 0.0, 0.0, 0.0, 99.5, 407.8, 502.5, 304.0, 503.29999999999995, 403.20000000000005, 101.4, 0.0, 0.0, 0.0, 200.89999999999998, 309.20000000000005, 303.4, 202.6, 201.7, 200.89999999999998, 202.5, 201.7, 0.0, 0.0, 0.0, 201.1, 202.2, 202.0, 201.60000000000002, 201.9, 201.6, 201.9, 202.5, 202.7, 201.39999999999998, 202.1, 204.10000000000002, 99.8, 305.5, 303.4, 100.6, 299.7, 101.5, 300.1, 101.2, 300.3, 0.0, 0.0, 100.4, 100.2, 0.0, 201.4, 100.5, 201.0, 100.7, 201.5, 100.4, 202.7, 100.6, 300.2, 100.3, 201.39999999999998, 100.2, 201.6, 100.3, 201.60000000000002, 201.5, 201.3, 202.0, 201.8, 200.7, 202.1, 201.5, 201.8, 201.5, 202.0, 200.4, 202.7, 200.9, 201.8, 201.3, 200.60000000000002, 201.8, 201.5, 201.4, 202.2, 200.5, 201.8, 202.7, 200.5, 202.60000000000002, 200.39999999999998, 202.3, 199.6, 201.8, 201.3, 201.6, 202.3, 203.3, 202.8, 201.5, 202.7, 201.2, 202.39999999999998, 202.0, 200.7, 202.0, 200.60000000000002, 201.7, 201.3, 201.89999999999998, 201.3, 201.60000000000002, 201.2, 201.10000000000002, 202.0, 201.9, 201.60000000000002, 304.6, 406.79999999999995, 102.0, 305.9, 200.6, 0.0, 100.6, 304.5, 204.39999999999998, 101.4, 201.3, 199.6, 302.2, 103.0, 302.1, 202.3, 202.2, 203.39999999999998, 203.1, 102.1, 100.5, 102.1, 0.0, 0.0, 0.0, 0.0, 0.0], 'network': [0, 0, 0, 3262, 2187, 2633, 3026, 593485, 690806, 588234, 434675, 52, 580, 0, 580, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1651, 2096, 2670, 2224, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1851, 1962, 4993, 3949, 2134, 306296, 886992, 549094, 557690, 8441, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1515, 580, 0, 209, 4493, 104716, 500858, 457012, 522224, 456946, 253361, 2102, 6265, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1833, 912259, 1558124, 1165784, 975678, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2457, 5455, 2114, 594097, 719308, 637674, 356027, 0, 0, 1160, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2274, 4038, 2120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 267, 3442, 3630, 5103, 1103, 12161, 610278, 604588, 541174, 541239, 52, 0, 0, 0, 0, 0, 0, 0, 0, 1029, 486, 580, 209, 4337, 2707, 472103, 456946, 456946, 522290, 383917, 1562, 6699, 0, 0, 0, 52, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 278, 908296, 1558514, 1228352, 902351, 16751, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1635, 2381, 4002, 2748, 586391, 728456, 611156, 382405, 52, 580, 0, 580, 0, 0, 0, 0, 0, 0, 0]}



cutting_period = 1000
def smoother(data_list):
    delta = 0
    out_list = []
    for i in range(len(data_list)):
        if i - delta >= 0 and i + delta < len(data_list):
            out_list.append(sum(data_list[(i-delta):(i+delta+1)]) / len(data_list[(i-delta):(i+delta+1)]))
        else:
            out_list.append(data_list[i])
    return out_list
# data['cpu'] = smoother(data['cpu'])
# data['network'] = smoother(data['network'])
data_size = len(data['cpu'])
assert len(data['network']) == data_size
x = range(data_size)[:cutting_period]
fig = plt.figure(figsize=(16, 4))

ax1 = fig.add_subplot(111)
ax1.plot(x, data['cpu'][:cutting_period], linewidth=1)
# ax1.set_ylabel('Y values for exp(-x)')
ax1.set_title("Double Y axis")

ax2 = ax1.twinx()  # this is the important function
ax2.plot(x, data['network'][:cutting_period], 'r', linewidth=1)
# ax2.set_xlim([0, np.e])
# ax2.set_ylabel('Y values for ln(x)')
# ax2.set_xlabel('Same X for both exp(-x) and ln(x)')

plt.savefig('res.pdf')