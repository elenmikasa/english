from accounts.models import CustomUser
from django.db import models

class Vocabulary(models.Model):
    word = models.CharField(verbose_name='単語')
    meaning = models.TextField(verbose_name='意味')
    yomikatakana = models.CharField(verbose_name='読みカタカナ', blank=True)
    pronunciation = models.CharField(verbose_name='発音', blank=True)
    part_of_speech = models.CharField(verbose_name='品詞', blank=True)
    sentence_eng = models.TextField(verbose_name='例文', blank=True)
    sentence_jpn = models.TextField(verbose_name='例文訳', blank=True)
    category = models.CharField(verbose_name='カテゴリー', blank=True)
    """auto_now_addはインスタンスの作成(DBにINSERT)する度に更新される。"""
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    """auto_now=Trueの場合はモデルインスタンスを保存する度に現在の時間で更新される。"""
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Vocabulary'

    def __str__(self):
        return self.word