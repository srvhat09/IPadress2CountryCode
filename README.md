# IPadress2CountryCode

IPアドレスから割当国名を取得する方法としては、ARIN,APNIC,LACNIC,RIPE,AFRINICの公開しているIPアドレスの割り当て一覧表から検索する方法しか知りませんでした。

ある時、DNSサービスとしてこれを運営して下さっている内容を見つけ、これを呼び出すだけの簡単なPyhtonスクリプトを作成しました。
> http://cc.wariate.jp/

※定期的に更新されているようで、感謝しております。

> python3 AE_getIP2CC.py -h
>
> Usage:
>     AE_getIP2CC.py [-i | --ip <ip address string> ]
>     AE_getIP2CC.py -h | --help
> 
> Options:
>     IPアドレスから割当Country Code取得機能
>     -i --ip <ip address string> ip address
>     -h --help                   当ヘルプを表示
> 
>     ex) AE_getIP2CC.py -i xx.xx.xx.xx
>         → DE

動作環境としては、nslookupとgrepがLinuxと同じ出力ができれば、Windowsでも可能だと思います。（未検証）
私は、WSL1のUbuntu 18.04で動作検証済です。勿論、Ubuntu本体でも問題ないかと思います。

Pythonのnslookup系ライブラリを試したのですが、TXTの扱いが無い等があり結局はOSコマンドを投げて対応しています。

Python3.x系でしか動作しないかとは思いますが、2.x系は未検証です。
