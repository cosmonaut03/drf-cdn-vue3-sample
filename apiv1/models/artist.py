from django.db import models
from django_boost.models.mixins import LogicalDeletionMixin


class Artist(LogicalDeletionMixin):
    """アーティストモデル"""

    RATE_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]

    name = models.CharField("アーティスト名", max_length=255)
    member_count = models.IntegerField("メンバー数", default=4)
    favorite = models.BooleanField("お気に入り", default=False)
    rate = models.SmallIntegerField("評価", choices=RATE_CHOICES, default=1)

    class Meta:
        db_table = "artists"

    def __str__(self):
        return self.pk
