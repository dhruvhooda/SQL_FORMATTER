from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from formatter.serializers import QuerySerializer
from formatter.models import Query
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from django.shortcuts import render
import ollama

# Create your views here
"""Formats the Query using SQL"""
def llm_format(raw_Query):
    client = ollama.Client(host='http://ollama:11434')
    prompt = f"Correctly format this SQL Query without saying anything else: {raw_Query}"
    response = client.generate(model='llama3:8b',prompt=prompt)
    formatted_Query = response.get('response','Ollama provided no response, try again')
    return formatted_Query



"""Takes in a Post or Get request, and returns a formatted query, or all previous queries"""
@extend_schema(
        request = QuerySerializer,
        responses = QuerySerializer
)
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def format_query_view(request):
    if request.method == 'POST':
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            raw_Query = serializer.validated_data['raw_Query']
            formatted_Query = llm_format(raw_Query)
            query_instance = Query(raw_Query=raw_Query,formatted_Query=formatted_Query,user=request.user)
            query_instance.save()
            if "text/html" in request.META.get("HTTP_ACCEPT", ""):
                return render(request, 'formatter/result_snippet.html', {'formatted_Query': formatted_Query})
            return Response({'formatted_Query': formatted_Query, 'id': query_instance.id})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    elif request.method == 'GET':
        queries = Query.objects.filter(user=request.user)
        serializer = QuerySerializer(queries, many=True)
        if "text/html" in request.META.get("HTTP_ACCEPT", ""):
            return render(request, 'formatter/format_query.html', {'queries': queries})
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)




