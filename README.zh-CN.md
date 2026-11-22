<p align="center">
  <a href="README.md">English</a> | 简体中文
</p>

# 吉凶占

> <sub>本文档由 Anthropic 的 Claude Fable 5.2 生成。</sub>

这是 Miyu 的一个脚本软件包，提供一件工具 `fortune`。它从七档里等概率抽出一档，并附上一句释义。工具只负责抽签，解读由 AI 完成。

七档是：大吉、吉、中吉、小吉、末吉、凶、大凶。

| 参数 | 说明 |
|---|---|
| `question` | 要问的事，工具会原样带回，不参与抽签 |

脚本开头的声明里写着 `Clicall: no`，所以这件工具只能由 AI 直接调用，不能通过 `miyu call` 反复抽取。随机数取自系统熵源，没有种子参数。
