import tensorflow as tf

time_steps = None
batch_size = None
num_feat = None
lstm_size = None

timeseries = tf.placeholder(tf.float32,[time_steps,batch_size,num_feat])

lstm = tf.contrib.rnn.BasicLSTMCell(lstm_size)

state = lstm.zero_state(batch_size,dtype=tf.float32)

probabilities = []
loss = 0.0

for current_batch_of_input_data in timeseries:
    output, state = lstm(current_batch_of_input_data,state)
    logits = tf.matmul(output,softmax_w+softmax_b)
    probabilities.append(tf.nn.softmax(logits))
    loss += loss_function
# def model_fn():
#
#     layer1 = tf.keras.layers.LSTM()
#     layer2 =