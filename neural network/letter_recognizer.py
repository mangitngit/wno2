from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# tf.logging.set_verbosity(tf.logging.INFO)

test_image = "sroda_rano/test2.npy"
test_label = "sroda_rano/testk2.npy"

if_train = False

def cnn_model_fn(features, labels, mode):

    input_layer = tf.reshape(features["x"], [-1, 28, 28, 1])

    conv1 = tf.layers.conv2d(
        inputs=input_layer,
        filters=32,
        kernel_size=[5, 5],
        padding="same",
        activation=tf.nn.relu)

    pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)

    conv2 = tf.layers.conv2d(
        inputs=pool1,
        filters=64,
        kernel_size=[5, 5],
        padding="same",
        activation=tf.nn.relu)

    pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)

    pool2_flat = tf.reshape(pool2, [-1, 7 * 7 * 64])

    dense = tf.layers.dense(inputs=pool2_flat, units=1024, activation=tf.nn.relu)

    # Add dropout operation; 0.6 probability that element will be kept
    dropout = tf.layers.dropout(
      inputs=dense, rate=0.4, training=mode == tf.estimator.ModeKeys.TRAIN)

    logits = tf.layers.dense(inputs=dropout, units=10)

    predictions = {
      "classes": tf.argmax(input=logits, axis=1),
      "probabilities": tf.nn.softmax(logits, name="softmax_tensor")
    }
    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)

    # Calculate Loss (for both TRAIN and EVAL modes)
    loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

    # Configure the Training Op (for TRAIN mode)
    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
        train_op = optimizer.minimize(
        loss=loss,
        global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op)

    # Add evaluation metrics (for EVAL mode)
    eval_metric_ops = {
      "accuracy": tf.metrics.accuracy(
        labels=labels, predictions=predictions["classes"])}
    return tf.estimator.EstimatorSpec(
        mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)


def dane(nazwa):
    data_path = nazwa  # address to save the hdf5 file

    with tf.Session() as sess:
        feature = {'train/image': tf.FixedLenFeature([], tf.string),
                   'train/label': tf.FixedLenFeature([], tf.int64)}
        filename_queue = tf.train.string_input_producer([data_path], num_epochs=1)
        reader = tf.TFRecordReader()
        _, serialized_example = reader.read(filename_queue)
        features = tf.parse_single_example(serialized_example, features=feature)

        image = tf.decode_raw(features['train/image'], tf.float32)

        label = tf.cast(features['train/label'], np.int32)
        print(image)

        image = tf.reshape(image, [28, 28, 1])
        images, labels = tf.train.shuffle_batch([image, label], batch_size=10, capacity=30, num_threads=1,
                                                min_after_dequeue=10)
        return images, labels


def recognition(x):
    letter = ""

    if x == 0:
        letter = "m"
    elif x == 1:
        letter = "o"
    elif x == 2:
        letter = "r"
    elif x == 3:
        letter = "s"
    elif x == 4:
        letter = "w"
    elif x == 5:
        letter = "b"
    elif x == 6:
        letter = "c"
    elif x == 7:
        letter = "f"
    elif x == 8:
        letter = "i"
    elif x == 9:
        letter = "p"

    return letter


def finals(eval_predict, eval_labels, eval_data):
    good, alll = 0, 0

    for pred_dict, expec, data in zip(eval_predict, eval_labels, eval_data):

        alll += 1
        class_id = pred_dict['classes']
        probability = pred_dict['probabilities'][class_id]

        if class_id == expec:
            good += 1
            if good % 137 == 0:
                print('{:6.4}'.format(probability * 100) + "%", recognition(expec) + " as " + recognition(class_id))
                plt.figure(recognition(class_id))
                plt.imshow(data)
                plt.axis('off')
                plt.show()

    print('{:6.4}'.format(100 * good / alll)+"% recognized")


def main(nevermind):
    train_data = np.load("sroda_rano/save.npy")
    train_labels = np.load("sroda_rano/savek.npy")
    eval_data = np.load(test_image)
    eval_labels = np.load(test_label)

    # Create the Estimator
    mnist_classifier = tf.estimator.Estimator(
        model_fn=cnn_model_fn, model_dir="model")

    tensors_to_log = {"probabilities": "softmax_tensor"}
    logging_hook = tf.train.LoggingTensorHook(
        tensors=tensors_to_log, every_n_iter=50)

    # # Train the model
    # train_input_fn = tf.estimator.inputs.numpy_input_fn(
    #     x={"x": train_data},
    #     y=train_labels,
    #     batch_size=50,
    #     num_epochs=None,
    #     shuffle=True)
    # mnist_classifier.train(
    #     input_fn=train_input_fn,
    #     steps=1000,
    #     hooks=[logging_hook])

    # Evaluate the model and print results
    eval_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": eval_data},
        y=eval_labels,
        num_epochs=1,
        shuffle=False)
    eval_results = mnist_classifier.evaluate(input_fn=eval_input_fn)

    eval_predict_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": eval_data},
        num_epochs=1,
        shuffle=False
    )

    eval_predict = mnist_classifier.predict(input_fn=eval_predict_fn)

    finals(eval_predict, eval_labels, eval_data)
    print(eval_results)

if __name__ == "__main__":
    tf.app.run()
