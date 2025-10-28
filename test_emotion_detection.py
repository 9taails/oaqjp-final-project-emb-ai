from EmotionDetection.emotion_detection import emotion_detector
import unittest

class EmotionUnitTest(unittest.TestCase):
    
    def test_emotion_detector(self):

        # Test case 1 - joy
        result_1 = emotion_detecor("I am glad this happened")
        self.assertEqual(result_1["dominant_emotion"], "SENT_joy")

        # Test case 2 - anger
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2["dominant_emotion"], "SENT_anger")

        # Test case 3 - disgust
        result_3 = emotion_detecor("I feel disgusted just hearing about this")
        self.assertEqual(result_3["dominant_emotion"], "SENT_disgust")
        
        # Test case 4 - sadness
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4["dominant_emotion"], "SENT_sadness")

        # Test case 5 - fear
        result_5 = emotion_detecor("I am really afraid that this will happen")
        self.assertEqual(result_5["dominant_emotion"], "SENT_fear")

unittest.main()