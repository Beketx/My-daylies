from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from article.models import Article, Author
from article.serializers import ArticleSerializer
# Create your views here.

class ArticleView(APIView):
    def get(self,request):
        articles = Article.objects.all()
        serializers = ArticleSerializer(articles,many=True)
        return Response({"articles":serializers.data})
    def post(self,request):
        article = request.data
        serializers = ArticleSerializer(data=article)
        if serializers.is_valid(raise_exception=True):
            article_saved=serializers.save()
        return Response({"success":"serializers data {}".format(article_saved.title)})
    def put(self, request,pk):
        article = Article.objects.get(pk=pk)
        data = request.data
        serializers = ArticleSerializer(instance=article,data=data,partial=True)
        if serializers.is_valid(raise_exception=True):
            save_article = serializers.save()
        return Response({"success":"{}".format(save_article.title)})

    def delete(self,request,pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({
            "success":"{}".format(article.title)},status=204
        )