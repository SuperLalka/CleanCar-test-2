import datetime
from urllib.parse import urlparse
from uuid import uuid4

from channels.testing import WebsocketCommunicator
from django.conf import settings
from django.shortcuts import get_object_or_404
from minio import Minio
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.request import Request

from app.ws.b_tasks import websocket_group_send
from app.ws.consumers import UploadingLogsConsumer
from app.ws.models import Image
from app.ws.serializers import (
    ImageSerializer,
    CreateImageSerializer,
    RetrieveImageSerializer,
)


class ImagesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    lookup_field = 'uuid'
    lookup_value_converter = 'uuid'
    lookup_value_regex = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

    action_serializers = {
        'list': RetrieveImageSerializer,
        'create': CreateImageSerializer,
        'retrieve': RetrieveImageSerializer,
        'destroy': None,
    }

    def get_serializer_class(self):
        return self.action_serializers.get(self.action, self.serializer_class)

    def list(self, request: Request, *args, **kwargs) -> Response:
        self.serializer_class = self.get_serializer_class()
        return super().list(self, request, *args, **kwargs)

    def create(self, request: Request) -> Response:
        now = datetime.datetime.now()
        image_obj = Image()

        file_name = request.data.get('file_name', f'file_t_{now:%s}')
        file_obj = request.FILES.get('file', None)

        if not file_obj:
            return Response(
                {'detail': 'Requires attached file.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            file_name += f".{str(file_obj).rsplit('.', 1)[-1]}"
            image_obj.file.save(file_name, file_obj)

            image_obj.save()

        except Exception as err:
            return Response({'detail': str(err)}, status=status.HTTP_400_BAD_REQUEST)

        # websocket_group_send.enqueue(
        #     settings.CHANNELS['uploading_logs_channel'],
        #     {
        #         'uuid': image_obj.uuid,
        #         'url': image_obj.file.url,
        #     }
        # )
        websocket_group_send(
            settings.CHANNELS['uploading_logs_channel'],
            {
                'uuid': image_obj.uuid,
                'url': image_obj.file.url,
            }
        )
        return Response(status=status.HTTP_201_CREATED)

    def retrieve(self, request: Request, uuid: uuid4 = None) -> Response:
        layout = get_object_or_404(self.get_queryset(), uuid=uuid)
        response_data = self.get_serializer_class()(layout).data
        return Response(response_data, status=status.HTTP_200_OK)

    def destroy(self, request: Request, uuid: uuid4 = None) -> Response:
        instance = get_object_or_404(self.get_queryset(), uuid=uuid)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # @action(methods=['post'], detail=False)
    # def upload_file(self, request: Request) -> Response:
    #     now = datetime.datetime.now()
    #     image_obj = Image()
    #
    #     file_name = request.data.get('file_name', f'file_t_{now:%s}')
    #     file_obj = request.FILES.get('file', None)
    #
    #     if not file_obj:
    #         return Response(
    #             {'detail': 'Requires attached file.'},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #
    #     try:
    #         file_name += f".{str(file_obj).rsplit('.', 1)[-1]}"
    #         image_obj.file.save(file_name, file_obj)
    #
    #         image_obj.save()
    #
    #     except Exception as err:
    #         return Response({'detail': str(err)}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     # websocket_group_send.enqueue(
    #     #     settings.CHANNELS['uploading_logs_channel'],
    #     #     {
    #     #         'uuid': image_obj.uuid,
    #     #         'url': image_obj.file.url,
    #     #     }
    #     # )
    #     websocket_group_send(
    #         settings.CHANNELS['uploading_logs_channel'],
    #         {
    #             'uuid': image_obj.uuid,
    #             'url': image_obj.file.url,
    #         }
    #     )
    #
    #     return Response(status=status.HTTP_200_OK)
