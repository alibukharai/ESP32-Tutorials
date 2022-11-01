########################                     Import libraries                   ########################################
import pickle
from optimizer import *
from calibrator import *
import onnx

######################                       Load onnx Model                         #####################################

onnx_model = onnx.load("Model.onnx")


#####################                       Optimization                        #####################################

optimized_model_path = optimize_fp_model("Model.onnx")


######################################        Calibration datset                      #####################################
with open('X_test.pkl', 'rb') as f:
    (test_images) = pickle.load(f)
with open('y_test.pkl', 'rb') as f:
    (test_labels) = pickle.load(f)


# Prepare the calibration dataset
calib_dataset = test_images[0:500:50]
pickle_file_path = 'Model_calib.pickle'


######################                       Load optimize model                        #####################################

model_proto = onnx.load(optimized_model_path)


print('Generating the quantization table:')

calib = Calibrator('int16', 'per-tensor', 'minmax')
calib.set_providers(['CPUExecutionProvider'])
calib.generate_quantization_table(model_proto,calib_dataset, pickle_file_path)

######################                      Saving coefficients                        #####################################


calib.export_coefficient_to_cpp(model_proto,  pickle_file_path, 'esp32s3', '.', 'Model_coefficient', True)
