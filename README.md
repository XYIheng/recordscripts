
Now, we have two phases:

## 1. record trace

```
python AndroidViewClient/tools/culebra --scale=0.5 -uUG -o /path/to/record/result/file
```

Here, we have to use python2, And for more usage about AndroidViewClient's culebra, check [culebra](https://github.com/dtmilano/AndroidViewClient/wiki/culebra).

"-u": do not verify screen state after dump;

"-U": generates unit test class and script;

"-G": presents the GUI;

"-o': output filename.

## 2. transfer to json

```
python3 transfer_2json.py arg1 arg2
```

arg1 是需要转换的python 脚本， arg2 是得到的输出：txt文件

"arg1":  比如 sample/result.py ;

"arg2": 比如  sample/output.txt; 

举个例子，sample/result.py是使用culebra记录的trace，output 是根据trace转换得到的相应的输出


