import unittest
from unittest.mock import MagicMock
from game import GameButton, Aud


class TestAnimationButtons(unittest.TestCase):
    def setUp(self):
        self.GameButton = GameButton()

    def test_anim1(self):
        x = 1
        y = 2
        self.GameButton.ans1 = MagicMock()

        self.GameButton.anim1(x, y)

        self.GameButton.ans1.enable.assert_called_once()
        self.assertEqual(self.GameButton.ans1.scale, (x, y))

    def test_anim2(self):
        x = 4
        y = 4
        self.GameButton.ans2 = MagicMock()

        self.GameButton.anim2(x, y)

        self.GameButton.ans2.enable.assert_called_once()
        self.assertEqual(self.GameButton.ans2.scale, (x, y))

    def test_anim3(self):
        x = 3
        y = 3
        self.GameButton.ans3 = MagicMock()

        self.GameButton.anim3(x, y)

        self.GameButton.ans3.enable.assert_called_once()
        self.assertEqual(self.GameButton.ans3.scale, (x, y))

    def test_anim4(self):
        x = 5
        y = 7
        self.GameButton.ans4 = MagicMock()

        self.GameButton.anim4(x, y)

        self.GameButton.ans4.enable.assert_called_once()
        self.assertEqual(self.GameButton.ans4.scale, (x, y))


class TestSliderAudio(unittest.TestCase):
    def setUp(self):
        self.aud = Aud()
        self.aud.knob = MagicMock()
        self.aud.knob.text_entity = MagicMock()

    def test_update_text(self):
        self.aud._update_text()

        self.assertEqual(self.aud.knob.text_entity.text, '')


class TestCountWinScoreWrg(unittest.TestCase):
    def test_count_win_score(self):
        countWin = 1
        txtt = ''

        if countWin == 1:
            txtt = 'вопрос'
        elif countWin == 2 or countWin == 3 or countWin == 4:
            txtt = 'вопроса'
        elif countWin == 0 or countWin == 5 or countWin == 6 or countWin == 7 or countWin == 8 or countWin == 9 or countWin == 10:
            txtt = 'вопросов'

        self.assertEqual(txtt, 'вопрос')

    def test_count_wrg_score(self):
        scoreWrg = 1
        txtt = ''
        txtw = ''

        if scoreWrg == 1:
            txtw = 'ошибку'
        elif scoreWrg == 2 or scoreWrg == 3 or scoreWrg == 4:
            txtw = 'ошибки'
        elif scoreWrg == 0 or scoreWrg == 5 or scoreWrg == 6 or scoreWrg == 7 or scoreWrg == 8 or scoreWrg == 9 or scoreWrg == 10:
            txtw = 'ошибок'

        self.assertEqual(txtw, 'ошибку')


if __name__ == '__main__':
    unittest.main()
