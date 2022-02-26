# Princple component analysis
# quote https://qiita.com/maskot1977/items/082557fcda78c4cdb41f
import numpy as np
import pandas as pd
import urllib.request 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sklearn #機械学習のライブラリ
from sklearn.decomposition import PCA #主成分分析器

class PCA:
    'PCA class'

    def __init__(self,dataset):
        'initialize the dataset'
        self.dataset = dataset

    def std(self,colLst):
        func = lambda x: (x-x.mean())/x.std()
        self.dataset[:,colLst] = self.dataset.loc[:,colLst].apply(func,axis = 0)

    def fit(self):
        """
        主成分分析の実行

        PCAの引数
        • n_components
        • 主成分を幾つ求めるか（個数：上の例では2）
        • 'mle' を指定すると最尤推定により個数を⾃動的に求める
        • 0〜1の間の実数を指定すると累積寄与率がその値になるまで主成分を求める
        • whiten
        • ⽩⾊化を⾏うかどうか（True|False）
        """
        self.pca = PCA()
        self.pca.fit(self.dataset)
        # データを主成分空間に写像
        self.feature = self.pca.transform(self.dataset)

    def score(self):
        '''
        return the score
        主成分得点
        '''
        return pd.DataFrame(
            self.feature
            ,columns=["PC{}".format(x + 1) for x in range(len(self.dataset.columns))]
            )

    def viz2d(self):
        """
        visualize the principal components in 2d
        第一主成分と第二主成分でプロットする
        この図を使って、主成分の意味付けを行う。
        """
        plt.figure(figsize=(6, 6))
        plt.scatter(self.feature[:, 0], self.feature[:, 1], alpha=0.8, c=list(self.datasetd.iloc[:, 0]))
        plt.grid()
        plt.xlabel("PC1")
        plt.ylabel("PC2")
        plt.show()

    def commit(self):
        """
        寄与率
        次元削減する場合は、この寄与率の累積率みて、決めるとよい
        """
        return pd.DataFrame(
            self.pca.explained_variance_ratio_
            ,index=["PC{}".format(x + 1) for x in range(len(self.dataset.columns))]
            )

    def vizCommitAccum(self):
        '''
        累積寄与率を図示する
        '''
        plt.gca().get_xaxis().set_major_locator(ticker.MaxNLocator(integer=True))
        plt.plot([0] + list( np.cumsum(self.pca.explained_variance_ratio_)), "-o")
        plt.xlabel("Number of principal components")
        plt.ylabel("Cumulative contribution rate")
        plt.grid()
        plt.show()
        
    def components(self):
        """
        因子負荷量
        主成分がどんな方向をもった情報なのかを知るときに使う。
        -1から１の値を取る。
        負の値を取るのは、主成分が大きくなるときに、その値は小さくなることを示す。
        """
        return pd.DataFrame(
            self.pca.components_
            ,index=["PC{}".format(x + 1) for x in range(len(self.dataset.columns))]
            ,columns = [i for i in self.dataset.columns])

    def eigenvalue(self):
        '''
        PCA の固有値
        '''
        return pd.DataFrame(
            self.pca.explained_variance_
            ,index=["PC{}".format(x + 1) for x in range(len(self.dataset.columns))]
            )

    def eigenvector(self):
        '''
        PCA の固有ベクトル
        '''
        return pd.DataFrame(
            self.pca.components_
            ,columns=self.dataset.columns[1:]
            ,index=["PC{}".format(x + 1) for x in range(len(self.dataset.columns))]
            )

    def vizCommit(self):        
        """
        第一主成分と第二主成分における観測変数の寄与度をプロットする
        第一主成分と第二主成分における観測変数の寄与度をプロットすることにより、各成分が何を考慮した値なのかのヒントが得られます。
        """
        plt.figure(figsize=(6, 6))
        for x, y, name in zip(self.pca.components_[0], self.pca.components_[1], self.dataset.columns[1:]):
            plt.text(x, y, name)
        plt.scatter(self.pca.components_[0], self.pca.components_[1], alpha=0.8)
        plt.grid()
        plt.xlabel("PC1")
        plt.ylabel("PC2")
        plt.show()