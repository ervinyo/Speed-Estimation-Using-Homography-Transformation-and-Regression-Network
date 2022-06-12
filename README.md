# Speed-Estimation-Using-Homography-Transformation-and-Regression-Network
This work includes homography transformation which is change monocular view into bird eye view and calculate each of vehicel speed in the videos using regression network. 
# Requirements
To run the training or testing step, you must installed library as follow:
1. Tensorflow-gpu = 1.14.0
2. keras = 2.2.4
3. opencv-contrib-python = 3.2.0.8
# How to Training
1. Download and generate the datasets
The datasets based on the <a href="https://carla.org/">carla dataset</a> and to generate datasets directly using 
"generate_raw_carla_van_dataset.py"
if you want to use directly without do preprocessing first can be downloaded in <a href="">here</a>
2. Convert dataset into generator
If you already download the dataset, run convert_raw_carla_van_to_tfrecords.py to create one file contains parameter to compute homography matriks
3. Training process
After we put dataset into generator, datasets ready to train. Run train_carla_van_horizon_vpz.py to start training process and set epoch, learning_rate, and batch_size as you desired.
4. Finish. You got checkpoint and choose the better checkpoint based on minimum loss will be used as pretrained model in new images.
# How to Testing
1. To run the testing, you can choose single images or video files run "run_image.py" or "run_video.py", respectively.
2. Wait until testing finish, and you got the bird eye view results.
