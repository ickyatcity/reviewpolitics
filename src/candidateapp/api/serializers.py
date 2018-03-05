from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from candidateapp.models import CandidatesWiki



class CandidateModelSerializer(serializers.ModelSerializer):

         upvotes = serializers.SerializerMethodField()
         downvotes = serializers.SerializerMethodField()
         

	 class Meta:
	        model = CandidatesWiki
	        fields = [
	            'candidate_id',
	            'candiate_name',
	            'title_wiki',
	            'content_wiki',
	            'references_wiki',
	            'links_wiki',
	            'sections_wiki',
	            'summary_wiki',
	            'fecha_ini_det',
	            'fecha_ini_f',
	            'upvotes',
	            'downvotes',
	        ]

	 def get_upvotes(self, obj):
	 	return 0

	 def get_downvotes(self, obj):
	 	return 0