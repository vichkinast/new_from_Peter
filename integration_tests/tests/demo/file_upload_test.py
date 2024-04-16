import pytest

import os

from integration_tests.pages.demo.file_upload_page import FileUploadPage


# @pytest.mark.deep
class TestFileUpload():

    @pytest.fixture
    def file_upload(self, driver):
        return FileUploadPage(driver)
    cwd_ = os.getcwd()
    path_to_file_ = os.path.join(cwd_, "resources/") if "integration_tests" in cwd_ else os.path.join(cwd_, "integration_tests/resources/")
    filename = "somefile.txt"
    file = os.path.join(path_to_file_ + filename)

    def test_file_upload(self, file_upload):
        file_upload.upload_file(self.file)
        assert(file_upload.file_is_uploaded(self.filename))

