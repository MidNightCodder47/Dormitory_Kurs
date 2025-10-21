from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem
from PyQt6.QtCore import Qt


class TextItemWidget(QWidget):
    def __init__(self, text):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 5, 10, 5)

        # Создаем QLabel с переносом слов
        self.label = QLabel(text)
        self.label.setWordWrap(True)

        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.list_widget = QListWidget()

        # Примеры текстов разной длины
        texts = [
            "Короткий текст",
            "Средний текст, который уже занимает несколько слов",
            "Очень длинный текст, который должен занимать несколько строк и автоматически подстраиваться под ширину виджета списка. Этот текст демонстрирует, как работает автоматический перенос слов.",
            "Еще один пример текста с средней длиной для тестирования"
        ]

        for text in texts:
            widget = TextItemWidget(text)
            item = QListWidgetItem()

            # Устанавливаем размер элемента на основе содержимого
            item.setSizeHint(widget.sizeHint())

            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, widget)

        layout.addWidget(self.list_widget)
        self.setLayout(layout)
        self.setWindowTitle("Адаптивный список")
        self.resize(400, 300)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()