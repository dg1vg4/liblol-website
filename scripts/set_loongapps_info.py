# coding=utf-8
import pandas as pd
import json

def appmd():
    df = pd.read_csv(
        "../static/data/loongapplist-latest.csv", engine="python", encoding="utf-8-sig"
    )
    for name in df["应用名称"]:
        a = "3A4000"
        if a in name:
            df.drop((df[df["应用名称"] == name]).index, inplace=True)
        else:
            continue
    df.drop(columns="图片链接", axis=1, inplace=True)
    df.sort_values("应用编号", ascending=True, inplace=True)
    # 删除开源软件
    df.drop((df[df["开发者"] == "开源软件"]).index, inplace=True)
    # 删除二进制翻译软件
    df.drop((df[df["开发者"] == "二进制翻译软件"]).index, inplace=True)
    # 删除开源软件（云顶书院迁移）
    df.drop((df[df["开发者"] == "开源软件（云顶书院迁移）"]).index, inplace=True)
    df.rename(
        columns={
            "应用编号": "编号",
            # "安装教程": "详细信息",
            "版本号": "版本",
        },
        inplace=True,
    )
    # df = df.assign(兼容性="")
    # 添加liblol版本
    # df = df.assign(liblol版本="最新")
    # 编辑页面链接
    # for url in df["页面链接"]:
    #     url_new = "[跳转](" + str(url) + ")"
    #     df.loc[df["页面链接"] == url, "页面链接"] = url_new
    # 编辑下载链接
    # for url in df["下载链接"]:
    #     url_new = "[下载](" + str(url) + ")"
    #     df.loc[df["下载链接"] == url, "下载链接"] = url_new
    # 以appid生成文件名
    for id in df["编号"]:
        filename = "../content/docs/apps/loongapps/" + str(id) + ".md"
        title = str(df.loc[df["编号"] == id, "应用名称"].values)
        title = title[2:-2]
        version = str(df.loc[df["编号"] == id, "版本"].values)[2:-2]
        update_time = str(df.loc[df["编号"] == id, "更新时间"].values)[2:-2]
        package_url = str(df.loc[df["编号"] == id, "下载链接"].values)[2:-2]
        deb_size = str(df.loc[df["编号"] == id, "文件大小"].values)[2:-2]
        command = str(df.loc[df["编号"] == id, "可执行文件"].values)[2:-2]
        head = (
            "---\n" +
            "id: " + json.dumps(id, ensure_ascii=False) + "\n" +
            "title: " + json.dumps(title, ensure_ascii=False) + "\n" +
            "weight: " + json.dumps(id, ensure_ascii=False) + "\n" +
            "version: " + json.dumps(version, ensure_ascii=False) + "\n" +
            "updateTime: " + json.dumps(update_time, ensure_ascii=False) + "\n" +
            "debName: " + json.dumps(package_url, ensure_ascii=False) + "\n" +
            "debSize: " + json.dumps(deb_size, ensure_ascii=False) + "\n" +
            "command: " + json.dumps(command, ensure_ascii=False) + "\n" +
            "---\n"
        )
        with open(filename, "w", encoding="utf-8-sig") as file:
            file.write(head)


appmd()
