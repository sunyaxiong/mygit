#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import jieba.analyse
from bad_demo1 import content, content_after


class ContentSimilarity(object):

    def __init__(self, source, to):
        self.source = source
        self.to = to

    def cut_word(self, article):
        # 这里使用了TF-IDF算法，所以分词结果会有些不同->https://github.com/fxsjy/jieba#3-关键词提取
        res = jieba.analyse.extract_tags(
            sentence=article, topK=20, withWeight=True)
        return res

    def tf_idf(self, res1=None, res2=None):
        # 向量，可以使用list表示
        vector_1 = []
        vector_2 = []
        # 词频，可以使用dict表示
        tf_1 = {i[0]: i[1] for i in res1}
        tf_2 = {i[0]: i[1] for i in res2}
        res = set(list(tf_1.keys()) + list(tf_2.keys()))

        # 填充词频向量
        for word in res:
            if word in tf_1:
                vector_1.append(tf_1[word])
            else:
                vector_1.append(0)
                if word in tf_2:
                    vector_2.append(tf_2[word])
                else:
                    vector_2.append(0)

        return vector_1, vector_2

    def numerator(self, vector1, vector2):
        # 分子
        return sum(a * b for a, b in zip(vector1, vector2))

    def denominator(self, vector):
        # 分母
        return math.sqrt(sum(a * b for a,b in zip(vector, vector)))

    def run(self, vector1, vector2):
        return self.numerator(
            vector1, vector2) / (self.denominator(vector1) * self.denominator(vector2)
        )

if __name__ == "__main__":
    runner = ContentSimilarity(content, content_after)

    vectors = runner.tf_idf(
        res1=runner.cut_word(article=runner.source), res2=runner.cut_word(article=runner.to)
    )
    # 相似度
    similarity = runner.run(vector1=vectors[0], vector2=vectors[1])
    # 使用arccos计算弧度

    rad = math.acos(similarity)

    print len(content), len(content_after)
    lenth_rate = float(len(content)) / float(len(content_after))
    if 0.93 < lenth_rate < 1.06:
        print "ok"

    print(similarity, rad)





