# from predict_detectron2 import Detectron2Predictor
# submission = Detectron2Predictor()

from predict_mmdetection import MMDetectionPredictor
submission = MMDetectionPredictor()



submission.run()
# import os
# submission.scoring(
#     '../input/public_validation_set_release_2.1/annotations.json',
#     os.path.join(submission.results_data_path, 'predictions.json')
#     )
print("Successfully generated predictions...")
