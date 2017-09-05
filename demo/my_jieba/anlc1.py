#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from bad_demo_big_block1 import content, content_after
from difflib import Differ, SequenceMatcher
import pprint
import json


text1 = '''  1. Beautiful is better than ugly.
             2. Explicit is better than implicit.
             3. Simple is better than complex.
             4. Complex is better than complicated.
        '''.splitlines(1)
text2 = '''  1. Beautiful is better than ugly.
             3.   Simple is better than complex.
             4. Complicated is better than complex.
             5. Flat is better than nested.
        '''.splitlines(1)

d = Differ()
res = d.compare(content_after.split("。"), content.split("。"))
con = SequenceMatcher(None, content, content_after)
print json.dumps([i for i in con.get_opcodes() if i[0] == "equal"], indent=4, ensure_ascii=False)
# pprint.pprint(list(res))
# f = open("./compare_res.txt", "a")
print json.dumps(list(res), indent=4, ensure_ascii=False)
# res = SequenceMatcher(None, content, content_after)
# print res.ratio()
# print res.quick_ratio()
# print res.real_quick_ratio()
# lst = res.get_matching_blocks()
# lst1 = res.matching_blocks
# print "sss: ", res.find_longest_match()
# for j in lst1:
#     print j
# for i in lst:
#     print i