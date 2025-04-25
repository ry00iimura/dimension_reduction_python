#correspondence analysis MCA
import pandas as pd
import numpy as np
import mca
import matplotlib.pyplot as plt
import random as rnd

class MCA:
    'MCA'

    def __init__(self,dataset):
        'initialize the parameters'
        self.dataset = dataset
        self.mca = mca.MCA(self.dataset, ncols=len(self.dataset.columns))

    def vizMCA(self):
        'visualize the MCA'
        # 表頭の座標を書き出す
        result_row = pd.DataFrame(self.mca.fs_r(N=2)) # N = the number of dimention
        result_row.index = list(dataset.index) # row index

        # 表側の座標を書き出す
        result_col = pd.DataFrame(self.mca.fs_c(N=2))
        result_col.index = list(self.dataset.columns)
  
        # 図の設定（任意）
        plt.figure(figsize=(10,10))
        plt.rcParams["font.size"] = 15

        # 表頭をプロット
        plt.scatter(result_col[0], result_col[1], s=100, marker="x")
        # ラベル付け
        cnt = 0
        for label in list(result_col.index):
            r = rnd.random() * 0.1
            plt.text(result_col.iloc[cnt, 0]+r, result_col.iloc[cnt, 1]+r, label)
            plt.plot(
                [result_col.iloc[cnt, 0]+r, result_col.iloc[cnt, 0]]
                ,[result_col.iloc[cnt, 1]+r, result_col.iloc[cnt, 1]])
            cnt += 1

        # スコア確認
        result_col5

        # 表側をプロット
        plt.scatter(result_row[0], result_row[1], s=100, marker="x")
        # ラベル付け
        cnt = 0
        for label in list(result_row.index):
            r = rnd.random() * 0.1
            plt.text(result_row.iloc[cnt, 0]+r, result_row.iloc[cnt, 1]+r, label)
            plt.plot(
                [result_row.iloc[cnt, 0]+r, result_row.iloc[cnt, 0]]
                ,[result_row.iloc[cnt, 1]+r, result_row.iloc[cnt, 1]])
            cnt += 1

        # スコア確認
        result_row5

# MCA
# n_pc = 8
# mca = prince.MCA(n_components=n_pc,random_state=40,n_iter =3)
# mca.fit(family_blood_table)
# family_blood_reduction = pd.DataFrame(mca.U_,columns = ['pc{}'.format(i+-1) for i in range(n_pc)])
# sns.barplot(data = horse_profile_combined, x= "owner",y = "wp")
# grouped_wp = horse_profile_combined[['owner','wp']].groupby('owner').mean()
# third_parcentile = grouped_wp.describe().iloc[-4,:] # 75%
# for k in grouped_wp:
#     print(k)


# for debugging
# index = ['students','workers','households','sum']
# cols = ['uniqulo','GU','Beams','sum']
# values = np.array([10,25,30,65,35,25,15,75,10,35,10,55,55,85,55,195])
# dataset = pd.DataFrame(index = index,columns = cols ,data = values.reshape(4,4))
# dataset = dataset.iloc[:-1,:-1]

if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import mca
    import matplotlib.pyplot as plt
    import random as rnd

            