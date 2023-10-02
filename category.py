from question import Question
class Category(object):
    def __init__(self, title: str, questions: [Question] = []):
        """

        :param title: The category's title (e.g. sports)
        :param questions: The questions of the category, optional for init, can be added later with :func:`add_question <category.Category.add_question>`
        """
        self.title = title
        self.questions = questions
        self._currentQuestion = 0

    def add_question(self, question: Question):
        """
        Adds the question to the category
        :param question: the question to add
        :return:
        """
        self.questions.append(question)