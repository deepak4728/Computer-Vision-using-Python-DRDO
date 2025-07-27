# 🧠 Computer Vision with Django – Face Detection & Image Classification

A full-stack web application that integrates **Face Detection** and **Image Classification** using state-of-the-art computer vision techniques powered by **OpenCV** and **TensorFlow's Inception Model**. The project is built using **Python** and the **Django** framework.

---

## 🚀 Features

- 📷 Capture images directly from webcam or upload via file
- 👁️ Real-time **Face Detection** with bounding boxes
- 🧩 Image classification using a pretrained **Inception Model**
- 📂 User-friendly interface with modern UI
- 💾 Automatically saves detected faces in the `/media/detected_faces/` directory

---

## 📸 Tech Stack

| Category           | Tools / Libraries                         |
|--------------------|--------------------------------------------|
| **Frontend**       | HTML, CSS, JavaScript                      |
| **Backend**        | Python, Django                             |
| **Computer Vision**| OpenCV                                     |
| **Image Classifier**| TensorFlow, Keras, Inception V3           |
| **Database**       | SQLite (default Django database)           |
| **Environment**    | Virtualenv (recommended)                   |

---

## 📁 Project Structure


face\_detection/
├── detector/              # App for face detection
├── classifier/            # App for image classification
├── media/                 # Stores uploaded and processed images
├── templates/             # HTML Templates
├── static/                # Static files (CSS, JS)
├── manage.py
└── requirements.txt



---

## 🛠️ Installation

1. **Clone the repository**

```
git clone https://github.com/yourusername/computer-vision-django.git
cd computer-vision-django
````

2. **Create and activate a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Linux/Mac
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the server**

```bash
python manage.py runserver
```

5. **Open in browser**

```
http://127.0.0.1:8000/
```

---

## 📷 Screenshots

| Upload Page                       | Detection Output                   | Classification Result                 |
| --------------------------------- | ---------------------------------- | ------------------------------------- |
| ![Upload](face_detection/project%20code%20screenshots/home.png) | ![Faces](face_detection/project%20code%20screenshots/edge_detection_result.png) | ![Classify](face_detection/project%20code%20screenshots/classifier_result.png) |

---

## ✅ Results / Accuracy

* 👥 Face Detection: Detects multiple faces with bounding boxes
* 🧠 Inception Model: Achieves high classification accuracy for known categories
* ⚡ Optimized preprocessing for faster runtime and responsiveness

---

## 📌 Future Work

* Add support for multiple classification models
* Improve face detection with deep learning-based detectors (e.g., MTCNN)
* Export results as downloadable reports

---

## 📚 References

* [OpenCV Documentation](https://docs.opencv.org/)
* [TensorFlow Inception Model](https://www.tensorflow.org/tutorials/images/transfer_learning)
* [Django Docs](https://docs.djangoproject.com/)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

