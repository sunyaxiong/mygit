#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
import difflib
from good_demo2 import content, content_after


class ContentDiff(object):

    def __init__(self, before, after):
        self.before = before
        self.after = after

    def with_jieba(self):
        """
        after jieba cut
        :return:
        """
        self.before = jieba.cut(before, cut_all=False)
        self.after = jieba.cut(after, cut_all=False)
        rat = difflib.SequenceMatcher(None, str(before), str(after))

        return rat.ratio()

    def with_not_jieba(self):
        """
        before jieba cut
        :return:
        """
        rat = difflib.SequenceMatcher(None, str(before), str(after))

        return rat.ratio()

before = jieba.cut(content, cut_all=False)
print("Full Mode: " + "/ ".join(before))

after = jieba.cut(content_after, cut_all=False)
print("Full Mode: " + "/ ".join(after))

rat = difflib.SequenceMatcher(None, str(before), str(after))
print "分词后： ", rat.ratio()

rat1 = difflib.SequenceMatcher(None, content, content_after)
print "分词前： ", rat1.ratio()