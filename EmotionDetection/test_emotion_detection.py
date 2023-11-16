import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy_emotion(self):
        text = "I am glad this happened"
        result = emotion_detector(text)
        print("test text - "+text)
        print("test emotion - "+"joy")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_emotion(self):
        text = "I am really mad about this"
        result = emotion_detector(text)
        print("test text - "+text)
        print("test emotion - "+"anger")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        print("test text - "+text)
        print("test emotion - "+"disgust")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        text = "I am so sad about this"
        result = emotion_detector(text)
        print("test text - "+text)
        print("test emotion - "+"sadness")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        print("test text - "+text)
        print("test emotion - "+"fear")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
