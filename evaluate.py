import sys
import codecs
import uuid
import json
import math


answer_list=[]


predict_list=[]

answer_index=int(sys.argv[2])
predict_index=int(sys.argv[3])


with codecs.open(sys.argv[1],'r','utf-8') as f:
    for line in f:
        ss = line.strip().split('\t')
        answer = ss[answer]
        answer_list.append(answer)
        predict = ss[predict_index]
        predict_list.append(predict)



def cal_correct(answer,predict,fdebug=None):
    if predict is None or predict == "None":
        return False
    tmp_answer=answer.replace(' ','').lower().strip()
    tmp_predict=predict.replace(' ','').lower().strip()
    tmp_answer = tmp_answer.replace('->','=')
    if tmp_answer == tmp_predict:
        return True
    answer=answer.split(' ')
    unit_index=len(answer)
    answer_unit=None
    answer_value=0
    while unit_index > 0:
        answer_value=''.join(answer[:unit_index])
        flag=True
        try:
            answer_value=float(answer_value)
        except:
            flag=False
        if flag:
            answer_unit=''.join(answer[unit_index:])
            break
        unit_index-=1
    if answer_unit is not None:
        predict = predict.split(' ')
        unit_index = len(predict)
        predict_unit = None
        predict_value = 0
        while unit_index > 0:
            predict_value = ''.join(predict[:unit_index])
            flag = True
            try:
                predict_value = float(predict_value)
            except:
                flag = False
            if flag:
                predict_unit = ''.join(predict[unit_index:])
                break
            unit_index-=1
        #if predict_unit == answer_unit and math.fabs(answer_value-predict_value)<math.fabs(answer_value)*0.05:
        #    return True
        if flag and math.fabs(answer_value - predict_value) < math.fabs(answer_value) * 0.1:
            return True
        else:
            flag=False
    if flag is False:
        print('answer:{}\tpredict:{}'.format(answer,predict))
        #fdebug.write('{}\t{}\n'.format(tmp_answer,tmp_predict))
        #fdebug.write('answer:{}\tpredict:{}\n'.format(answer, predict))

    return False


correct_count=0
total_count=0


for i in range(len(answer_list)):
    total_count+=1
    flag=cal_correct(answer_list[i],predict_list[i],fdebug)
    if flag:
        correct_count+=1
print('precision = {}'.format(correct_count/total_count))


