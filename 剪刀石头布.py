#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
while 1:
    s = int(random.randint(1, 3))
    if s == 1:
        ind = "ʯͷ"
    elif s == 2:
        ind = "����"
    elif s == 3:
        ind = "��"
    m = raw_input('���� ʯͷ�����ӡ���,����"end"������Ϸ:')
    blist = ['ʯͷ', "����", "��"]
    if (m not in blist) and (m != 'end'):
        print "����������������룡"
    elif (m not in blist) and (m == 'end'):
        print "\n��Ϸ�˳���..."
        break
    elif m == ind :
        print "���Գ��ˣ� " + ind + "��ƽ�֣�"
    elif (m == 'ʯͷ' and ind =='����') or (m == '����' and ind =='��') or (m == '��' and ind =='ʯͷ'):
        print "���Գ��ˣ� " + ind +"����Ӯ�ˣ�"
    elif (m == 'ʯͷ' and ind =='��') or (m == '����' and ind =='ʯͷ') or (m == '��' and ind =='����'):
        print "���Գ��ˣ� " + ind +"�������ˣ�"