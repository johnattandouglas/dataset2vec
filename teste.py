import tensorflow as tf

# Verificar se o TensorFlow está carregado
print("TensorFlow version:", tf.__version__)

# Criar um tensor de entrada
try:
    x = tf.keras.Input(shape=(2,), dtype=tf.float32)
    print("Input tensor created successfully.")
    print("Input tensor shape:", x.shape)
except Exception as e:
    print("Error:", e)