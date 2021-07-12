# -*- coding: utf-8 -*-

# AE_getIP2CC.py
# 
# Created on: 2021/05/27
# AUTHOR:	Reiki Hattori - http://www.anaheim-eng.co.jp/
# Copyright (c) 2021, Anaheim Engineering Co.,LTD. All rights reserved.
# 
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  
# http://www.apache.org/licenses/LICENSE-2.0
#  
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
 
import sys
import subprocess

TAG = __name__ + ' {}:'


def parser():
    """
    依頼パラメタをパースする
    """

    argDict = {}
    usage = """
Usage:
    AE_getIP2CC.py [-i | --ip <ip address string> ]
    AE_getIP2CC.py -h | --help

Options:
    IPアドレスから割当Country Code取得機能
    -i --ip <ip address string> ip address
    -h --help                   当ヘルプを表示

    ex) AE_getIP2CC.py -i xx.xx.xx.xx
        → DE
""".format(__file__)
    arguments = sys.argv
    if len(arguments) == 1:
        # 引数が無いため終了
            print(usage)
            sys.exit()              #強制終了
    # ファイル自身を指す最初の引数を除去
    arguments.pop(0)
    # 引数として与えられたoption check
    if len(arguments) >= 2:
        opt = arguments[1]
        if opt.startswith('-'):     #2個目は必ず[-]では始まらない
            print(usage)
            sys.exit()              #強制終了

    # - で始まるoption
    options = [option for option in arguments if option.startswith('-')]

    if '-h' in options or '--help' in options:
        print(usage)
        sys.exit()              #強制終了

    if '-i' in options or '--ip' in options:
        type_position = arguments.index('-i') \
            if '-i' in options else arguments.index('--ip')
        argDict["ip"] = arguments[type_position + 1]

    return argDict


# 入力パラメタチェック: argチェック
class ParamCheck():
    def chk_param(self, dic: dict):
        num = len(dic)
        if num == 0:
            return False

        if 'ip' in dic:
            return True

        return False


# メイン処理
def main():
    cmd = 'nslookup -type=txt {}.cc.wariate.jp | grep text'
    try:
        argDict = parser()
        mc = ParamCheck()
        if not mc.chk_param(argDict):
            raise ValueError(TAG.format('main') + 'param error')
            sys.exit()              #強制終了

        ipList = argDict['ip'].split(".")
        reverseIP = ipList[3] + "." + ipList[2] + "." + ipList[1] + "." + ipList[0]
        cmd = cmd.format(reverseIP)
        process = (subprocess.Popen(cmd, stdout=subprocess.PIPE,
                           shell=True).communicate()[0]).decode('utf-8')
        processList = process.split('"')
        print(processList[1])

    except Exception as e:
        print('Error:' + e.args[0])


if __name__ == '__main__':
    main()
