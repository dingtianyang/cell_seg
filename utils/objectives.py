import keras.metrics
import tensorflow as tf


def weighted_crossentropy(y_true, y_pred, weight=[1., 5., 25.]):
    """
    weight is for channel axis
    can be [1., 5., 0.] [1., 5., 10.]
    """

    class_weights = tf.constant([[[weight]]]) 
    weights = tf.reduce_sum(class_weights * y_true, axis=-1)

    unweighted_losses = tf.nn.softmax_cross_entropy_with_logits_v2(labels=y_true, logits=y_pred)
    weighted_losses = weights * unweighted_losses
    loss = tf.reduce_mean(weighted_losses)
    return loss

