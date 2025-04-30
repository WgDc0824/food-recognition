# Food Recognition Benchmark 2022

## Project Overview
This is a food recognition project participating in the Food Recognition Benchmark 2022 challenge. The project uses deep learning technology to achieve instance segmentation of food items, enabling precise recognition and segmentation of food in images.

### Project Background
Food recognition is an important research direction in the field of computer vision, with broad application prospects in intelligent catering, health management, smart shopping, and other areas. This project aims to provide technical support for related applications by achieving precise recognition and segmentation of food images through deep learning technology.

### Technical Features
- Utilizes advanced deep learning frameworks (MMDetection and Detectron2)
- Supports multiple instance segmentation model architectures
- Provides complete training, evaluation, and prediction pipelines
- Supports multi-GPU parallel training
- Offers Docker containerization deployment solution

### Main Features
1. **Food Recognition**: Identify food categories in images
2. **Instance Segmentation**: Precisely segment the boundaries of each food instance
3. **Multi-category Support**: Support recognition of multiple food categories
4. **Real-time Inference**: Support real-time food recognition and segmentation
5. **Batch Processing**: Support batch image processing

### Application Scenarios
- Smart Restaurants: Automatic dish recognition and nutrition information calculation
- Health Management: Help users track dietary habits
- Smart Shopping: Assist users in identifying and purchasing food items
- Food Classification: Automatic classification and organization of food images
- Nutrition Analysis: Analyze food nutritional components

### Project Advantages
1. **High Accuracy**: Uses advanced deep learning models with high recognition accuracy
2. **User-friendly**: Provides complete deployment solutions and detailed documentation
3. **Extensible**: Supports multiple model architectures, easy to extend
4. **Efficient**: Supports GPU acceleration for fast processing
5. **Open Source**: Completely open source, free to use and modify

## Project Structure
```
food/
├── data/                    # Data directory
├── Detic/                   # Detic model related code
├── QueryInst/              # QueryInst model related code
├── food_recognition_project/ # Main project code
├── detectron2/             # Detectron2 framework code
├── evaluator/              # Evaluator code
├── models/                 # Model files
├── utils/                  # Utility functions
├── weights/                # Weight files
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
├── predict.py            # Main prediction script
└── Other configuration files...
```

## System Requirements
- Operating System: Ubuntu 18.04 or higher
- GPU: NVIDIA GPU with CUDA 10.1 support
- Memory: 16GB or more recommended
- Storage: 50GB or more recommended

## Installation Guide

### 1. Basic Environment Setup
```bash
# Install Python 3.7
sudo apt-get update
sudo apt-get install python3.7 python3.7-dev

# Install pip
sudo apt-get install python3-pip

# Install CUDA 10.1
# Please refer to NVIDIA official documentation for CUDA installation
```

### 2. Install Dependencies
```bash
# Clone the project
git clone [project-url]

# Enter project directory
cd food

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Docker Installation (Optional)
```bash
# Build Docker image
docker build -t food-recognition .

# Run Docker container
docker run --gpus all food-recognition
```

## Usage Guide

### 1. Data Preparation
- Place training data in the `data/` directory
- Ensure data format meets requirements (COCO format)

### 2. Model Training
```bash
# Train with MMDetection
python train_mmdetection.py

# Train with Detectron2
python train_detectron2.py
```

### 3. Model Prediction
```bash
# Predict with default configuration
python predict.py

# Predict with MMDetection
python predict_mmdetection.py

# Predict with Detectron2
python predict_detectron2.py
```

### 4. Model Evaluation
```bash
# Run evaluation script
python evaluator/evaluate.py
```

## Supported Models
- HTC (Hybrid Task Cascade)
- Mask R-CNN
- QueryInst
- Detic

## Configuration
Main configuration files:
- `configs/`: Model configuration files
- `aicrowd.json`: Project configuration file
- `requirements.txt`: Python dependencies configuration

## FAQ

### 1. GPU Related Issues
Q: How to check if GPU is available?
A: Run the following command:
```python
import torch
print(torch.cuda.is_available())
```

### 2. Memory Issues
Q: Getting out of memory error during training?
A: Try:
- Reduce batch size
- Use smaller model
- Increase virtual memory

### 3. Dependency Issues
Q: Getting errors during dependency installation?
A: Ensure:
- Correct Python version (3.7)
- Correct CUDA version (10.1)
- Correct pip version

## Performance Metrics
- mAP (mean Average Precision) on validation set
- Inference speed (FPS)
- Memory usage

## Contributing
1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments
- AIcrowd Platform
- MMDetection Team
- Detectron2 Team
- All Contributors

## Contact
For questions, please contact:
- Project Issues
- Email: [c08241014@163.com]
  
## Changelog
### v1.0.0 (2022-01-01)
- Initial release
- Basic functionality support
- Example code provided

### v1.1.0 (2022-02-01)
- Added new model support
- Performance optimization
- Bug fixes

## Resources
- [Project Documentation](docs/)
- [API Reference](docs/api.md)
- [Example Code](examples/)
- [FAQ](docs/faq.md)

## Citation
If you use this project in your research, please cite:
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
