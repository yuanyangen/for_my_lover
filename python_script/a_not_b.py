#使用方法： python a_not_b.python fileA fileB

import sys
fileObjectA = open(sys.argv[1]);
fileObjectB = open(sys.argv[2]);
try:
    allTextA = fileObjectA.read();
    allTextB = fileObjectB.read();
    allLineA = allTextA.split();
    allLineB = allTextB.split();
    count = 0;

    for b in allLineB :
        if b not in allLineA:
            print(b);
            count = count + 1;
finally:
    fileObjectA.close();
    fileObjectB.close();


