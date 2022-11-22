#15个特征，7类动物
animal = ['鸡','鸭','鱼','狗','虎','斑马','长颈鹿']
dict_feature = {'1':'有羽毛','2':'不会飞','3':'会下蛋','4':'吃肉','5':'有犬齿','6':'有爪','7':'有鱼鳞','8':'会游泳','9':'有鳃','10':'跑得快','11'
                :'黄褐色','12':'有蹄','13':'有黑色条纹','14':'长腿','15':'长脖'}
dog_fea = ['吃肉','有犬齿','跑得快'] 
fish_fea = ['有鱼鳞','会游泳','有鳃' ]
yazi_fea = ['有羽毛','有爪','会游泳']
chick_fea = ['有羽毛','有爪','会下蛋']
zebra_fea = ['有蹄','有黑色条纹','跑得快']
tiger_fea = ['黄褐色','吃肉','有爪']
giraffa_fea = ['长腿','有蹄','长脖']
fea = []
now_feature = []
print('************************************')
print('*********ALL FEATURE HERE********')
print('************************************')
print(dict_feature )
print('*********ALL CLASSIAL HERE********')
print('**************************************')
print('狗:{},鱼:{},鸭:{},鸡:{},虎:{},斑马:{},长颈鹿:{}'.format(dog_fea,fish_fea,yazi_fea,chick_fea,tiger_fea,zebra_fea,giraffa_fea))
print('**************************************')
print('********请输入3个特征:*********')
print('**************************************')
curr = 1
while curr:
    now_feature=[]
    fea = []
    for i in range(0,3):
        feature = input('请依次输入特征的数字序号: (输入"exit()"可以退出) ')
        if feature == 'exit()':
            curr = 0
            break
        fea.append(feature)
        now_feature.append(dict_feature[fea[i]])
        print(now_feature[i])
    if curr == 0:
        break
    print('您输入的特征是: {}'.format(now_feature))
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    flag = 0
    for i in range(0,3):
        if now_feature[i] in dog_fea:
            a = a+1
            if a>2:
                print('是狗' )
                a=0
                flag =1
        if now_feature[i] in fish_fea:
            #print(now_ feature[i])
            b=b+1
            if b>2:
                print('是鱼')
                b=0
                flag =1
        if now_feature[i] in yazi_fea:
            #print(now_feature[i])
            c=c+1
            if c>2:
                print('是鸭')
                c=0
                flag =1
        if now_feature[i] in tiger_fea:
            d = d+1
            if d>2:
                print('是虎' )
                d=0
                flag =1
        if now_feature[i] in zebra_fea:
            e = e+1
            if e>2:
                print('是斑马' )
                e=0
                flag =1
        if now_feature[i] in giraffa_fea:
            f = f+1
            if f>2:
                print('是长颈鹿' )
                f=0
                flag =1
        if now_feature[i] in chick_fea:
            g = g+1
            if g>2:
                print('是鸡' )
                g=0
                flag =1
    if flag==0:
        print('无法准确判断')
        if a>1:
            print("狗的概率是66%")
        if b>1:
            print('鱼的概率是66%')
        if c>1:
            print('鸭的概率是66%')
        if d>1:
            print('虎的概率是66%')
        if e>1:
            print('斑马的概率是66%')
        if f>1:
            print('长颈鹿的概率是66%')
        if g>1:
            print('鸡的概率是66%')
