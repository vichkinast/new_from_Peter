from selenium.webdriver.common.by import By
from integration_tests.pages.base_page import BasePage


class FileUploadPage(BasePage):
    _upload_file = {"by": By.ID, "value": "file-upload"}
    _file_submit = {"by": By.ID, "value": "file-submit"}
    _uploaded_files = {"by": By.ID, "value": "uploaded-files"}


    def ___init___(self, driver):
        self.driver = driver

    def upload_file(self, file):
        self._load("/upload")
        self._type(self._upload_file, file)
        self._click(self._file_submit)

    def file_is_uploaded(self, filename):
        upload_file = self._find(self._uploaded_files).text
        return upload_file == filename, "uploaded file should be %s" % filename
