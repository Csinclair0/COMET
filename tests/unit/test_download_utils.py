# -*- coding: utf-8 -*-
import unittest
import os
import shutil
from tests.data import DATA_PATH
from comet.download_utils import download_model
from comet.models import load_from_checkpoint


class TestDownloadModel(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(os.path.join(DATA_PATH, "wmt21-small-da-152012"))

    def test_download_from_s3(self):
        data_path = download_model("wmt21-small-da-152012", saving_directory=DATA_PATH)
        self.assertTrue(
            os.path.exists(
                os.path.join(DATA_PATH, "wmt21-small-da-152012/hparams.yaml")
            )
        )
        self.assertTrue(
            os.path.exists(
                os.path.join(DATA_PATH, "wmt21-small-da-152012/checkpoints/")
            )
        )
        load_from_checkpoint(data_path)
