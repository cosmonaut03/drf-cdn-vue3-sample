from django.db import models
from django.db.models import DO_NOTHING
from django_boost.models.mixins import LogicalDeletionMixin
from apiv1.models import Artist


class Album(LogicalDeletionMixin):
    """アルバムモデル"""

    artist = models.ForeignKey(Artist, on_delete=DO_NOTHING)
    album_title = models.CharField("アルバムタイトル", max_length=255)
    release_year = models.CharField("制作年", max_length=4)

    class Meta:
        db_table = "albums"

    def __str__(self):
        return self.pk
