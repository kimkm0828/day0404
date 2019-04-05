import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


def getSubjectScore(name):
    rc("font", family=font_manager.FontProperties(fname="C:\Windows\Fonts/H2GTRE.TTF").get_name())

    data = pd.read_csv("./Data/scores.csv")
    data.index = data['name']
    del data['name']

    try:

        sco = data.loc[:,name]
        subject = data.columns

        plt.bar(range(len(sco)), sco)
        plt.title(name)
        plt.xticks(range(len(sco)), data.index, rotation="40")

        fname = 'static/'+name+'.png'


        plt.savefig(fname)
        plt.close()
        print("차드를 생성하였습니다.")
    except KeyError:
        fname = 'no'

    return fname






def getStudentScore(name):
    rc("font", family=font_manager.FontProperties(fname="C:\Windows\Fonts/H2GTRE.TTF").get_name())

    data = pd.read_csv("./Data/scores.csv")
    data.index = data['name']
    del data['name']

    try:

        ben_sco = data.loc[name].values[1:]
        subject = data.columns

        plt.bar(range(len(ben_sco)), ben_sco)
        plt.xticks(range(len(ben_sco)), subject[1:])
        plt.title(name)

        fname = 'static/'+name+'.png'


        plt.savefig(fname)
        plt.close()
        print("차드를 생성하였습니다.")
    except KeyError:
        fname = 'no'

    return fname








def irisT(SepalLength,SepalWidth,PetalLength,PetalWidth):
    import pandas as pd
    from sklearn import svm, metrics
    from sklearn.model_selection import train_test_split

    csv = pd.read_csv('iris.txt')
    csv_data = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
    csv_label = csv['Name']

    train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)

    clf = svm.SVC()
    clf.fit(train_data, train_label)
    pre = clf.predict(test_data)

    ac = metrics.accuracy_score(test_label, pre)  # 정답률 검증해보는것

    real = [[SepalLength, SepalWidth, PetalLength, PetalWidth]]
    r2 = clf.predict(real)
    return r2