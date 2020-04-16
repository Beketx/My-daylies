                                                        #so this is a implement of APIView
                                                        '''
                                                        from django.shortcuts import render
                                                        from rest_framework.views import APIView
                                                        from delivery.serializers import ConsumerSerializer
                                                        from rest_framework.response import Response
                                                        from delivery.models import *
                                                        # Create your views here.


                                                        class ConsumerView(APIView):
                                                            def get(self,request):
                                                                consumer = Consumer.objects.all()
                                                                serializer = ConsumerSerializer(consumer, many=True)
                                                                return Response(serializer.data)
                                                            def post(self, request):
                                                                data = request.data
                                                                serializer = ConsumerSerializer(data=data)
                                                                if serializer.is_valid(raise_exception=True):
                                                                    saved_consumer = serializer.save()
                                                                return Response({"success":"Consumer created {}"}.format(self.name))
                                                            def put(self, request, pk):
                                                                consumer = Consumer.objects.get(pk=pk)
                                                                data = request.data
                                                                serializer = ConsumerSerializer(instance=consumer, data=data,partial=True)
                                                                if serializer.is_valid():
                                                                    saved_con = serializer.save()
                                                                return Response(saved_con)
                                                            def delete(self,request,pk):
                                                                consumer = Consumerobjects.get(pk=pk)
                                                                consumer.delete()
                                                                return Response({"successfully deleted"})
                                                        '''


#so this is a implement of GenericAPIView with MIXIN LISTModelMixin which does action
'''
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from .models import Consumer
from .serializers import ConsumerSerializer

class ConusmerView(ListModelMixin,GenericAPIView):
    queryset = Consumer.objects.all()
    serializers_class = ConsumerSerializer

    #list of consumers
    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)

    #create consumer pk
    def perform_create(self,serializer):
        consumer = get_object_or_404(Author,id=self.request.data.get('consumer_id'))
        return serializer.save(consumer=consumer)

    #create consumer 
    def post(self,request,*args,**kwargs):  
        return self.create(request,*args,**kwargs)
'''

                                                                                                    '''
                                                                                                    from rest_framework.generics import get_object_or_404
                                                                                                    from rest_framework.generics import GenericAPIView
                                                                                                    from rest_framework.mixin import ListModelMixin, CreateModelMixin
                                                                                                    from .models import *
                                                                                                    from .serializers import *

                                                                                                    class ConsumerView(ListModelMixin,CreateModelMixin, GenericAPIView):
                                                                                                        def get(self,request,*args,**kwargs):
                                                                                                            return self.list(request,*args, **kwargs)

                                                                                                        def perform_create(self,serializer):
                                                                                                            # consumer = Consumer.objects.get(id = request.data.get('id'))
                                                                                                            # return serializer.save(consumer=consumer)
                                                                                                            author = get_object_or_404(Author, id = self.request.data.get('author_id'))
                                                                                                            return serializer.save(author=author)

                                                                                                        def post(self,request,*args,**kwargs):
                                                                                                            return self.create(requet,*args,**kwargs)
                                                                                                    '''

#ListApiView CreateApiView
'''
from rest_framework.generics import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import *
from .serializers import ConsumerSerializer
class ConsumerView(ListAPIView,CreateAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer
    def perform_create(self,serializer):
        author = get_object_or_404(Author,id=self.request.data.get('author_id'))
        return serializer.save(author=author) 
'''

                                                                                        #ListCreateAPIView
                                                                                        '''
                                                                                        from rest_framework.generics import get_object_or_404
                                                                                        from rest_framework.generics import ListCreateAPIView

                                                                                        from .models import *
                                                                                        from .serializers import *
                                                                                        class ConsumerView(ListCreateAPIView):
                                                                                            queryset = Consumer.objects.all()
                                                                                            serializer_class = ConsumerSerializer
                                                                                            def perform_create(self,serializer):
                                                                                                author = get_object_or_404(Author, id = self.request.data.get('author_id'))
                                                                                                return serializer.save(author=author)
                                                                                        '''
#RetrieveAPIView for single watching by detail
'''
from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView

from .models import *
from .serializers import *
class ConsumerView(ListCreateAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer
    def perform_create(self,serializer):
        author = get_object_or_404(Author, id = self.request.data.get('author_id'))
        return serializer.save(author=author)
class SingleConsumerView(RetrieveAPIView):
    queryset = Consumer.objects.all()
    serializer = ConsumerSerializer
'''
#RetrieveAPIView for single updating by detail
'''
from rest_framework.generics import RetrieveUpdateAPIView
class SingleArticleView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
'''
                                                                            #RetrieveAPIView for single updating delete by detail
                                                                            '''
                                                                            from rest_framework.generics import RetrieveUpdateDestroyAPIView
                                                                            class SingleArticleView(RetrieveUpdateDestroyAPIView):
                                                                                queryset = Article.objects.all()
                                                                                serializer_class = ArticleSerializer
                                                                            '''

#VIEWSET list retrieve just watching
'''
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer

class ConsumerView(viewsets.ViewSet):
    def list(self,request):
        queryset = Consumer.objects.all()
        serializer = ConsumerSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self ,request, pk=None):
        queryset = Consumer.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        serializer = ConsumerSerializer(user)
        return Response(serializer.data)
'''

                                                                        #VIEWSET list retrieve deleting updating creating destroying
                                                                        '''
                                                                        from rest_framework import viewsets
                                                                        from .models import Consumer
                                                                        from .serializers import ConsumerSerializer

                                                                        class ConsumerViewSet(viewsets.ModelViewSet):
                                                                            serializer_class = ConsumerSerializer
                                                                            queryset = Consumer.objects.all()
                                                                        '''