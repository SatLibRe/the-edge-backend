from django.db import models

class Post(models.Model):
    title = models.TextField(null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date_bet_placed = models.DateTimeField()
    payout = models.BigIntegerField()
    net_pl = models.BigIntegerField()
    odds = models.IntegerField()
    amount_bet = models.BigIntegerField()
    team_for = models.TextField()
    team_against = models.TextField()
    bet_placed = models.TextField()


    def __str__(self):
        return self.title
