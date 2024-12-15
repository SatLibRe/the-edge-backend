from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    net_pl = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'date_bet_placed',
            'payout',
            'odds',
            'amount_bet',
            'team_for',
            'team_against',
            'bet_placed',
            'title',
            'content',
            'net_pl',  # This is now read-only
        ]
        read_only_fields = ['net_pl']  # Prevent net_pl from being sent in input

    def get_net_pl(self, obj):
        return obj.net_pl
