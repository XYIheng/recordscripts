import ast
import collections
import json
import os
import sys

from pprint import pprint


def main():
    script_file = sys.argv[1] #要转换的py脚本
    output_name = sys.argv[2] #转换后的txt文件

    with open(script_file, "r", encoding='UTF-8') as source:  # 硬编码
        tree = ast.parse(source.read())
    source.close()

    pprint(ast.dump(tree))
    visitor = CodeVisitor()
    visitor.visit(tree)   # 解析py脚本
    steps = visitor.step
    pprint(steps)
    print(len(steps))  # 每个step代表app的一个trace
    print("------------------------------------ separating line -------------------------------------")
    
    process_steps(steps,output_name)  # 将steps 转化为txt文件输出

class CodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.node_count = 0
        self.call_node = 0
        self.func_node = 0
        self.step = []  # 每个py脚本对应的trace，列表每个元素是一个字典，即self.step_dict
        self.step_dict = {}  # {'key': , 'locate': , 'method': }或者{'in_coordinates': , 'method': }用来匹配view

    def generic_visit(self, node):
        self.node_count += 1
        pprint(node)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Call(self, node):
        self.node_count += 1
        self.call_node += 1
        pprint(node.args)
        for each in node.args:
            if hasattr(each, "s") and isinstance(each.n,str):
                print(str(72)+each.s)
        print(str(73)+node.func.attr)
        if not "method" in self.step_dict:
            if not node.func.attr == "dump" and not node.func.attr == "sleep" and not node.func.attr == "main":
                self.step_dict["method"] = node.func.attr
                if node.func.attr == "setText":
                    self.step_dict["value"] = node.args[0].s
                    self.step_dict["view"] = node.args[1].s
                    self.step.append(self.step_dict)
                    self.step_dict = {}
                    return
        if "method" in self.step_dict and "touch" in self.step_dict["method"]:   # 如果是touch方法
            if "find" in node.func.attr:    # 有定位元素
                print("----------- here in find --------------")
                return
                self.step_dict["method"] = "touch"
                self.step_dict["locate"] = node.func.attr
                self.step_dict["key"] = node.args[0].s
                self.step.append(self.step_dict)
                self.step_dict = {}
                return
            else:                           # 无定位元素 坐标单击
                #self.step_dict["method"] = "coordinate_touch"
                
                temp_xy = []
                for each in node.args:
                    if hasattr(each, "n") and not isinstance(each.n,str):
                        print(str(93)+str(each.n))
                        temp_xy.append(int(each.n))
                    else:
                        self.step_dict["view"] = str(each.s)
                if len(temp_xy) > 0:
                    in_coordinates = [str((temp_xy[0], temp_xy[1]))]
                    # print(in_coordinates)
                    self.step_dict["in_coordinates"] = in_coordinates
                    self.step.append(self.step_dict)
                    self.step_dict = {}
                    return
                else:
                    self.step.append(self.step_dict)
                    self.step_dict = {}
                    return
            ast.NodeVisitor.generic_visit(self, node)
        elif "method" in self.step_dict and "longTouch" in self.step_dict["method"]:  # 如果是longTouch方法
            print("here in longTouch")
            if "find" in node.func.attr:
                return
                self.step_dict["method"] = "longTouch"
                self.step_dict["locate"] = node.func.attr
                self.step_dict["key"] = node.args[0].s
                self.step.append(self.step_dict)
                self.step_dict = {}
                return
            else:                           # 无定位元素 坐标长按
                #self.step_dict["method"] = "coordinate_longTouch"
                temp_xy = []
                for each in node.args:
                    if hasattr(each, "n") and not isinstance(each.n,str):
                        print(str(93)+int(each.n))
                        temp_xy.append(int(each.n))
                    else:
                        self.step_dict["view"] = str(each.s)
                if len(temp_xy) > 0:
                    in_coordinates = [str((temp_xy[0], temp_xy[1]))]
                    # print(in_coordinates)
                    self.step_dict["in_coordinates"] = in_coordinates
                    self.step.append(self.step_dict)
                    self.step_dict = {}
                    return
                else:
                    self.step.append(self.step_dict)
                    self.step_dict = {}
                    return
            ast.NodeVisitor.generic_visit(self, node)

        elif "method" in self.step_dict and self.step_dict["method"] == "setText":  #如果是setText方法
            return
            if "find" in node.func.attr:
                self.step_dict["locate"] = node.func.attr
                self.step_dict["key"] = node.args[0].s
                self.step.append(self.step_dict)
                self.step_dict = {}
                return
            ast.NodeVisitor.generic_visit(self, node)
        elif "method" in self.step_dict and (self.step_dict["method"] == "drag" or self.step_dict["method"] == "dragDip"):  # 如果是drag方法
            temp = []
            for each in node.args:
                temp_xy = []
                if hasattr(each, "elts"):
                    for item in each.elts:
                        if hasattr(item, "n"):
                            print(int(item.n))
                            temp_xy.append(int(item.n))
                    if len(temp_xy) > 0:
                        in_coordinates = [str((temp_xy[0], temp_xy[1]))]
                        # print(in_coordinates)                        
                        temp.append(in_coordinates)
            self.step_dict["in_coordinates"] = temp
            self.step.append(self.step_dict)
            self.step_dict = {}
            return

        elif "method" in self.step_dict and self.step_dict["method"] == "press":  # 如果是HOME等宏键
            self.step_dict["key"] = node.args[0].s
            self.step.append(self.step_dict)
            self.step_dict = {}
            return
        elif "method" in self.step_dict:
            self.step.append(self.step_dict)
            self.step_dict = {}
    def visit_Expr(self, node):
        if hasattr(node, "value"):
            if isinstance(node.value, ast.Call):
                pprint(node.value)
                self.visit_Call(node.value)

    def visit_FunctionDef(self, node):
        self.node_count += 1
        self.func_node += 1
        pprint(node.name)
        if node.name == "testSomething":
            for each in node.body:
                self.visit_Expr(each)

    def report(self):
        print("node_count: " + str(self.node_count))
        print("call_node: " + str(self.call_node))
        print("func_node: " + str(self.func_node))
        pprint(self.step_dict)

def process_steps(steps,output_name):
    f = open(output_name,"w")
    for step in steps:
        for key,value in step.items():          
            f.write(str(key)+':'+str(value)+" ")
        f.write("\n")
    f.close()

if __name__ == '__main__':
    main()
