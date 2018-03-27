"""Serializers for Body and BodyChildRelation."""
from rest_framework import serializers
from events.prioritizer import get_r_fresh_prioritized_events
from bodies.models import Body
from bodies.serializer_min import BodySerializerMin

class ChildrenSerializer(serializers.Serializer):   # pylint: disable=W0223
    """Serializes children of the body from BodyChildRelation."""
    def to_representation(self, instance):
        return BodySerializerMin(instance.child, context=self.context).data

class BodySerializer(serializers.ModelSerializer):
    """Serializer for Body."""

    from roles.serializers import RoleSerializerMin

    followers_count = serializers.IntegerField(
        source='followers.count',
        read_only=True)

    parents = serializers.SerializerMethodField()
    children = ChildrenSerializer(many=True, read_only=True)

    events = serializers.SerializerMethodField()
    roles = RoleSerializerMin(many=True, read_only=True)

    class Meta:
        model = Body
        fields = ('id', 'name', 'short_description', 'description', 'image_url',
                  'children', 'parents', 'events', 'followers_count',
                  'roles', 'website_url')

    @classmethod
    def get_parents(cls, obj):
        """Gets a list of ids of parents of a Body."""
        return [x.parent.id for x in obj.parents.all()]

    def get_events(self, obj):
        """Gets filtred events."""
        from events.serializers import EventSerializer
        return EventSerializer(get_r_fresh_prioritized_events(
            obj.events, self.context['request']), many=True, read_only=True).data