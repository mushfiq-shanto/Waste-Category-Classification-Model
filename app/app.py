from fastai.vision.all import load_learner
import gradio as gr

waste_labels = [
    'Batteries Waste', 
    'Cardboard Waste', 
    'Electronics Waste', 
    'Glass Waste', 
    'Metal Waste', 
    'Organic Waste', 
    'Paper Waste', 
    'Plastic Waste', 
    'Rubber Waste', 
    'Textiles Waste', 
    'Wood Waste'
    ]

def recognize_image(image):
  pred, idx, probs = model.predict(image)
  return dict(zip(waste_labels, map(float, probs)))

model = load_learner(f'models/waste_classifier_v0.pkl')

image = gr.Image()
label = gr.Label()
examples = ['test_images/01.jpg', 'test_images/02.jpg', 'test_images/03.jpg']

demo = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
demo.launch()