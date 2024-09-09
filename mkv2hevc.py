import sys
import cv2
import time
import argparse


def parse_args():
    # Parse input arguments
    desc = 'Capture and record live camera video on Jetson TX2/TX1'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--width', dest='image_width',
                        help='image width [1224]',
                        default=1224, type=int)
    parser.add_argument('--height', dest='image_height',
                        help='image height [1024]',
                        default=1024, type=int)
    parser.add_argument('--input', dest='input_file',
                        help='input file name ["output"]',
                        default='0548207774487603-1564435253804-20190729-down-212524.mkv', type=str)
    parser.add_argument('--fps', dest='fps',
                        help='fps of the output video [10]',
                        default=10, type=int)
    parser.add_argument('--output', dest='output_file',
                        help='input file name ["output"]',
                        default='output', type=str)
    args = parser.parse_args()
    return args


def main():


    args = parse_args()
    print('Called with args:')
    print(args)

    video_file = args.input_file

    cap = cv2.VideoCapture(video_file)

    fps_video = cap.get(cv2.CAP_PROP_FPS)
    print("frame rate: ", fps_video)

    total_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print("total frame: ", total_frame)

    if total_frame <=5 :
        raise ValueError("no frame in the video or the video is too short.")


    gst_str = ('appsrc ! videoconvert ! omxh265enc ! mpegtsmux ! '
                'filesink location={}.avi').format(args.output_file)


    writer = cv2.VideoWriter(gst_str, cv2.CAP_GSTREAMER, 0, args.fps, (args.image_width, args.image_height))


    start = time.time()

    while True:

        ret, frame = cap.read()

        if ret !=True:
            break

        #cv2.imshow('REC', frame)
        #cv2.waitKey(0)
        #if cv2.waitKey(1) == 27: # ESC key: quit program
          #     break
        writer.write(frame)


    total_time = time.time() - start

    print("total processing time: ", total_time)

    writer.release()
    cap.release()


if __name__ == '__main__':
    main()

    