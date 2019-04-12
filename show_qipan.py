#coding:utf-8
def sqipan(qipan):
    maxx=10
    maxy=10
    print("   O  一  二  三  四   五  六  七  八  九")
    for i in range(maxx):
        print(i, " ", end="")
        for j in range(maxy):
            if qipan[i][j] == 0:
                print("+", "  ", end="")  # 无棋子
            elif qipan[i][j] == 1:
                print("O", "  ", end="")  # 白色
            elif qipan[i][j] == 2:
                print("X", "  ", end="")  # 黑色
        print("\n")
