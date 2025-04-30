# Food Recognition Benchmark 2022

## 项目概述
这是一个参与Food Recognition Benchmark 2022挑战赛的食品识别项目。项目使用深度学习技术实现食品的实例分割（Instance Segmentation），可以精确识别和分割图像中的食品。

### 项目背景
食品识别是计算机视觉领域的一个重要研究方向，在智能餐饮、健康管理、智能购物等领域有着广泛的应用前景。本项目旨在通过深度学习技术，实现对食品图像的精确识别和分割，为相关应用提供技术支持。

### 技术特点
- 采用先进的深度学习框架（MMDetection和Detectron2）
- 支持多种实例分割模型架构
- 提供完整的训练、评估和预测流程
- 支持多GPU并行训练
- 提供Docker容器化部署方案

### 主要功能
1. **食品识别**：识别图像中的食品类别
2. **实例分割**：精确分割每个食品实例的边界
3. **多类别支持**：支持多种食品类别的识别
4. **实时推理**：支持实时食品识别和分割
5. **批量处理**：支持批量图像处理

### 应用场景
- 智能餐厅：自动识别菜品和计算营养信息
- 健康管理：帮助用户记录饮食情况
- 智能购物：辅助用户识别和购买食品
- 食品分类：自动分类和整理食品图片
- 营养分析：分析食品的营养成分

### 项目优势
1. **高精度**：采用先进的深度学习模型，识别精度高
2. **易用性**：提供完整的部署方案和详细的文档
3. **可扩展**：支持多种模型架构，易于扩展
4. **高效性**：支持GPU加速，处理速度快
5. **开源**：完全开源，可自由使用和修改

## 项目特点
- 支持多种深度学习框架（MMDetection和Detectron2）
- 提供完整的Docker环境配置
- 支持多GPU训练和推理
- 包含多种先进的实例分割模型
- 提供完整的评估和预测流程

## 目录结构
```
food/
├── data/                    # 数据目录
├── Detic/                   # Detic模型相关代码
├── QueryInst/              # QueryInst模型相关代码
├── food_recognition_project/ # 主项目代码
├── detectron2/             # Detectron2框架代码
├── evaluator/              # 评估器代码
├── models/                 # 模型文件
├── utils/                  # 工具函数
├── weights/                # 权重文件
├── Dockerfile             # Docker配置文件
├── requirements.txt       # Python依赖
├── predict.py            # 主预测脚本
└── 其他配置文件...
```

## 环境要求
- 操作系统：Ubuntu 18.04或更高版本
- GPU：支持CUDA 10.1的NVIDIA GPU
- 内存：建议16GB或以上
- 存储空间：建议50GB或以上

## 安装指南

### 1. 基础环境安装
```bash
# 安装Python 3.7
sudo apt-get update
sudo apt-get install python3.7 python3.7-dev

# 安装pip
sudo apt-get install python3-pip

# 安装CUDA 10.1
# 请参考NVIDIA官方文档安装CUDA
```

### 2. 安装依赖
```bash
# 克隆项目
git clone [项目地址]

# 进入项目目录
cd food

# 安装Python依赖
pip install -r requirements.txt
```

### 3. Docker安装（可选）
```bash
# 构建Docker镜像
docker build -t food-recognition .

# 运行Docker容器
docker run --gpus all food-recognition
```

## 使用方法

### 1. 数据准备
- 将训练数据放在`data/`目录下
- 确保数据格式符合要求（COCO格式）

### 2. 模型训练
```bash
# 使用MMDetection训练
python train_mmdetection.py

# 使用Detectron2训练
python train_detectron2.py
```

### 3. 模型预测
```bash
# 使用默认配置进行预测
python predict.py

# 使用MMDetection进行预测
python predict_mmdetection.py

# 使用Detectron2进行预测
python predict_detectron2.py
```

### 4. 模型评估
```bash
# 运行评估脚本
python evaluator/evaluate.py
```

## 支持的模型
- HTC (Hybrid Task Cascade)
- Mask R-CNN
- QueryInst
- Detic

## 配置说明
项目的主要配置文件：
- `configs/`: 模型配置文件
- `aicrowd.json`: 项目配置文件
- `requirements.txt`: Python依赖配置

## 常见问题

### 1. GPU相关问题
Q: 如何检查GPU是否可用？
A: 运行以下命令：
```python
import torch
print(torch.cuda.is_available())
```

### 2. 内存问题
Q: 训练时出现内存不足错误？
A: 可以尝试：
- 减小batch size
- 使用更小的模型
- 增加虚拟内存

### 3. 依赖问题
Q: 安装依赖时出现错误？
A: 确保：
- Python版本正确（3.7）
- CUDA版本正确（10.1）
- 使用正确的pip版本

## 性能指标
- 模型在验证集上的mAP（mean Average Precision）
- 推理速度（FPS）
- 内存使用情况

## 贡献指南
1. Fork项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

## 许可证
本项目采用MIT许可证 - 详见[LICENSE](LICENSE)文件

## 致谢
- AIcrowd平台
- MMDetection团队
- Detectron2团队
- 所有贡献者

## 联系方式
如有问题，请通过以下方式联系：
- 项目Issues
- 邮件：[联系邮箱]
- 论坛：[论坛地址]

## 更新日志
### v1.0.0 (2022-01-01)
- 初始版本发布
- 支持基本功能
- 提供示例代码

### v1.1.0 (2022-02-01)
- 添加新模型支持
- 优化性能
- 修复已知问题

## 相关资源
- [项目文档](docs/)
- [API参考](docs/api.md)
- [示例代码](examples/)
- [常见问题](docs/faq.md)

## 引用
如果您在研究中使用了本项目，请引用：
```bibtex
@misc{food_recognition_2022,
  author = {AIcrowd},
  title = {Food Recognition Benchmark 2022},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/your-repo}}
}
``` 