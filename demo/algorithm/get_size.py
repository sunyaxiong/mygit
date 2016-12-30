#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pympler import tracker
import random


tr = tracker.SummaryTracker()
a = [[random.random() for i in range(2000)] for i in range(2000)]
# dic = {"name": "syx", "age": 30}
# dic1 = {"name": "sun", "age": 32, "country": "cn"}
tr.print_diff()
