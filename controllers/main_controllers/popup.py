from PyQt5.QtWidgets import QMessageBox


class PopUp:
    def __int__(self):
        self.message_box = QMessageBox()

    def question(self, msg: str) -> bool:
        result = self.message_box.question(None, "Confirmation Window",
                                  msg, self.message_box.Ok | self.message_box.Cancel)

        return result

    def warning(self, msg: str) -> None:
        self.message_box.warning(None, "Warning", msg)
