# Bin_Data 资源（自定义方块必需）

<p align="center">
  <a href="/README.md"><img alt="English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="/README_zh.md"><img alt="中文" src="https://img.shields.io/badge/中文-d9d9d9"></a>
</p>

------

## 介绍

如果你在 Nukkit-MOT 中使用自定义方块，**必须**下载并保留本目录的资源文件。
服务器会使用这些文件构建运行时方块调色板，并在启动/握手时同步给客户端。
缺失或版本不匹配会导致自定义方块显示错误、无法放置或网络 ID 不一致。

## 如何放置

1. 保持文件名不变（例如 `vanilla_palette_*.nbt`）。
2. 将本目录内容放置到 Nukkit-MOT 的**核心 bin 资源目录**（与服务器其他文件夹同级）。
   - 路径示例：`Nukkit-MOT/bin/` 资源目录
3. 升级或新增协议版本时，补齐对应版本的 `vanilla_palette_*.nbt`。

## 文件说明

### `vanilla_palette_*.nbt`

- **用途**：原版方块状态调色板（Vanilla Block State Palette）
- **格式**：NBT 格式，包含所有原版方块及其状态的完整列表
- **命名规则**：文件名中的数字对应特定协议版本号
  - 例如：`vanilla_palette_671.nbt` 对应协议版本 671（Minecraft 1.21.70）
  - 例如：`vanilla_palette_686.nbt` 对应协议版本 686（Minecraft 1.21.80）