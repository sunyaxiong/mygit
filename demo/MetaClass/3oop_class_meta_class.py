class UpperAttrMetaclass(type): 

    def __new__(upperattr_metaclass, future_class_name, 
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        # reuse the type.__new__ method   # 复用type的__new__方法
        # this is basic OOP, nothing magic in there  # 最基本的面向对象
        return type.__new__(upperattr_metaclass, future_class_name, 
                            future_class_parents, uppercase_attr)