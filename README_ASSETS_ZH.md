# 资源文件结构（用于后续新增轮播图/图片）

本项目用两套图片资源：

## 1. 原图（全尺寸）
目录：`example pictures/`

放所有你在“Lightbox 打开的大图”里要用的原始 JPG/PNG 图片。  
文件名保持你在 `TEMPLATES` 里写的那一串（例如：`01 · iPhone Notes 01.jpg`）。

## 2. 缩略图（用于轮播）
目录：`thumbs/`

放由脚本自动生成的 WebP 缩略图（体积更小、轮播更快）。  

### 生成方式
脚本：`scripts/generate-thumbs.py`

在本地运行（需要安装 Pillow）：
```bash
pip install pillow
python3 scripts/generate-thumbs.py --src "example pictures" --out thumbs --width 520 --quality 75
```

或在已安装环境下直接运行（只要 `thumbs/` 里缺图就会自动生成）。

## 3. 如何新增一个“轮播图 Variation”
1. 把新图片放到 `example pictures/`，并使用跟现有命名风格一致的文件名（确保在对应模板的 `exampleImages` 列表里配置到它）。
2. 运行上面的 `generate-thumbs.py` 生成对应的 WebP 缩略图。
3. 不需要改 UI：代码会自动把 `exampleImages` 对应到轮播的缩略图，并在 Lightbox 打开全尺寸图。

