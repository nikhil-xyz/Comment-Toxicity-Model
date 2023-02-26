import gradio as gr
import pickle
import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.layers import TextVectorization

#   Loading model....
model = load_model('model.h5')

#   loading vectorizer (Bag of Words) .....
from_disk = pickle.load(open("vocabulary.pkl", "rb"))
vectorizer = TextVectorization.from_config(from_disk['config'])
vectorizer.set_weights(from_disk['weights'])

columns = ['toxic',	'severe_toxic',	'obscene', 'threat', 'insult', 'identity_hate']

def score_comment(comment):
  vectorized_comment = vectorizer([comment])
  result = model.predict(vectorized_comment)

  text = ''
  for index, col in enumerate(columns):
    text += '{}: {}\n'.format(col, result[0][index] > 0.5)
  return text

interface = gr.Interface(fn=score_comment,
                inputs=gr.inputs.Textbox(lines=2, placeholder='comment somenthing'),
                outputs='text')
interface.launch()