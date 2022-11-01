# **To Convert your model to ESP-DL Formate** 

1. Import required libraries 
   * Download these files "calibrator.pyd", "calibrator_acc.pyd", "optimizer.py"
   from "[esp-dl/tools/quantization_tool/](https://github.com/espressif/esp-dl/tree/master/tools/quantization_tool)" and placed in your working directory.
2. Load your ONNX model 
3. Optimize your model using optimizer 
4. Prepare or load your calibration dataset
5. Load optimize model 
6. Quantization
7. Saving coefficients

_Note: For calibration dataset I am using X_test and y_test_