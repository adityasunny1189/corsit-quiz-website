from flask import Flask, render_template
from data import question_data
from question import Question
from quiz_brain import QuizBrain


app = Flask(__name__)


question_bank = []
for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))


quiz_brain = QuizBrain(question_bank)


@app.route('/')
def home():
    return render_template('index.html', question=quiz_brain.next_question(), score=quiz_brain.score)


@app.route('/<user_ans>')
def check_answer(user_ans):
    quiz_brain.check_answer(user_ans)
    if quiz_brain.still_has_question():
        return render_template('index.html', question=quiz_brain.next_question(), score=quiz_brain.score)
    else:
        quiz_brain.reset()
        return render_template('quiz_over.html', score=quiz_brain.score)


if __name__ == '__main__':
    app.run(debug=True)
