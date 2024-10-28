from django.db.models import CASCADE, DO_NOTHING
from django.db import models

from django_boost.models.mixins import LogicalDeletionMixin

from apiv1.models.album import Album
from apiv1.models.artist import Artist


class Song(LogicalDeletionMixin):
    """歌モデル"""

    class Meta:
        db_table = "songs"
        verbose_name = verbose_name_plural = "歌"

    artist = models.ForeignKey(Artist, on_delete=CASCADE)
    album = models.ForeignKey(Album, on_delete=DO_NOTHING)
    title = models.CharField(verbose_name="タイトル", max_length=20)
    release_year = models.CharField("制作年", max_length=4)
    created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日時", blank=True, null=True)

    def __str__(self):
        return self.pk
