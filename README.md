# Food Recognition Benchmark 2022 第三名解决方案

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

本项目是 [Food Recognition Benchmark 2022](https://www.aicrowd.com/challenges/food-recognition-benchmark-2022) 比赛的第三名解决方案。该比赛旨在开发一个能够准确识别食品图像中各种食品的计算机视觉系统。

## 目录
- [解决方案概述](#解决方案概述)
- [技术细节](#技术细节)
- [环境要求](#环境要求)
- [安装指南](#安装指南)
- [使用方法](#使用方法)
- [项目结构](#项目结构)
- [实验结果](#实验结果)
- [许可证](#许可证)
- [致谢](#致谢)
- [Docker 使用说明](#docker-使用说明)

## 解决方案概述

我们的解决方案主要基于以下两个关键步骤：

1. **数据标注修复**
   - 使用掩码标注的边界框坐标 [min_x, min_y, max_x, max_y] 来修正原始边界框标注
   - 这一步骤解决了原始数据集中存在的大量标注噪声问题
   - 通过精确的边界框标注，显著提高了模型的训练效果

2. **模型训练**
   - 采用 [QueryInst](https://github.com/hustvl/QueryInst) 作为基础模型
   - 使用修复后的标注数据进行训练
   - 训练命令：`python tools/train.py configs/exp002.py`

## 技术细节

### 数据预处理
- 原始数据集中存在大量不准确的边界框标注
- 通过掩码标注提取准确的边界框坐标
- 这一步骤显著提高了训练数据的质量
- 数据清洗流程：
  1. 加载原始标注文件
  2. 提取掩码标注的边界框坐标
  3. 替换不准确的边界框标注
  4. 保存修正后的标注文件

### 模型选择
- 选择 QueryInst 作为基础模型
- QueryInst 是一个基于 Transformer 的实例分割模型
- 该模型在 COCO 数据集上表现出色，适合迁移到食品识别任务
- 模型特点：
  - 端到端的实例分割框架
  - 基于 Transformer 的查询机制
  - 动态掩码预测头
  - 多尺度特征融合

## 环境要求

- Python 3.9
- PyTorch 1.9.0+
- CUDA 11.1+
- mmcv-full
- mmdetection
- 其他依赖请参考 requirements.txt

## 安装指南

1. 克隆本仓库：
```bash
git clone https://github.com/your-username/food-recognition-challenge.git
cd food-recognition-challenge
```

2. 创建并激活虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 安装 mmcv-full：
```bash
pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.9.0/index.html
```

## 使用方法

### 数据准备
1. 下载比赛数据集
2. 运行数据预处理脚本：
```bash
python tools/preprocess_data.py
```

### 训练模型
```bash
python tools/train.py configs/exp002.py
```

### 推理
```bash
python tools/test.py configs/exp002.py work_dirs/exp002/latest.pth --show
```

## 项目结构
```
food-recognition-challenge/
├── configs/              # 配置文件目录
├── data/                 # 数据目录
├── tools/                # 工具脚本
├── work_dirs/            # 工作目录
├── requirements.txt      # 依赖文件
└── README.md            # 项目说明
```

## 实验结果
- 在验证集上的 mAP: 0.xxx
- 在测试集上的 mAP: 0.xxx
- 推理速度: xx FPS

## 许可证
本项目采用 MIT 许可证发布，与 AICrowd 比赛仓库和 QueryInst 仓库保持一致。

## 致谢
- 感谢 AICrowd 组织本次比赛
- 感谢 QueryInst 团队提供优秀的开源模型
- 感谢所有参与比赛和提供帮助的社区成员

## 联系方式
如有任何问题或建议，请通过以下方式联系：
- 邮箱：your-email@example.com
- GitHub Issues

## Docker 使用说明

### Mac 用户快速开始（仅生成预测结果）

如果您使用的是 Mac 电脑，并且只需要生成预测结果，可以按照以下步骤操作：

1. **构建 Docker 镜像**
```bash
docker build -t food-recognition:latest .
```

2. **准备数据**
- 将测试图片放在 `./data/test_images` 目录下
- 确保 `./work_dirs/exp002/latest.pth` 中有预训练模型权重文件

3. **运行推理**
```bash
docker run -it \
  -v $(pwd)/data:/workspace/data \
  -v $(pwd)/work_dirs:/workspace/work_dirs \
  food-recognition:latest \
  python tools/test.py configs/exp002.py work_dirs/exp002/latest.pth --format-only --options "jsonfile_prefix=./work_dirs/exp002/test_results"
```

4. **获取结果**
- 预测结果将保存在 `./work_dirs/exp002/test_results.bbox.json` 文件中

> 注意：由于使用 CPU 进行推理，处理速度会比 GPU 版本慢。建议使用小批量图片进行测试。
