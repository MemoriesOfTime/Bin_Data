# Bin_Data Resources (Required for Custom Blocks)

<p align="center">
  <a href="/README.md"><img alt="English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="/README_zh.md"><img alt="中文" src="https://img.shields.io/badge/中文-d9d9d9"></a>
</p>

------

## Introduction

If you use custom blocks in Nukkit-MOT, you **must** download and keep the resources in this folder.
The server builds the runtime block palette from these files and syncs it to clients during startup/handshake.
Missing or mismatched versions can cause custom blocks to render incorrectly, fail to place, or produce network ID mismatches.

## How to Place

1. Keep filenames unchanged (e.g., `vanilla_palette_*.nbt`).
2. Put the contents of this folder into Nukkit-MOT's **core bin resource directory** (same level as other server folders).
   - Example path: `Nukkit-MOT/bin/` resource directory
3. When upgrading or adding protocol versions, add the matching `vanilla_palette_*.nbt` files.

## File Description

### `vanilla_palette_*.nbt`

- **Purpose**: Vanilla Block State Palette
- **Format**: NBT format containing complete list of all vanilla blocks and their states
- **Naming Convention**: Numbers in filename correspond to specific protocol versions
  - Example: `vanilla_palette_671.nbt` corresponds to protocol 671 (Minecraft 1.21.70)
  - Example: `vanilla_palette_686.nbt` corresponds to protocol 686 (Minecraft 1.21.80)
