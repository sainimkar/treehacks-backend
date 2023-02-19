# todo/todo_api/views.py
import cv2
import numpy as np
from skimage import io
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Photo, PhotoResponse
from .serializers import PhotoSerializer, ResponseSerializer

class TreehacksApiView(APIView):
    # add permission to check if user is authenticated

    '''
    def get(self, request, *args, **kwargs):

        todos = Todo.objects.filter(user = request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    '''

    # download the image using scikit-image	
    # def urlRead():
    #     print "downloading %s" % (url)	
    #     image = io.imread(url)	
    #     cv2.imshow("Incorrect", image)	
    #     cv2.imshow("Correct", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))	
    #     cv2.waitKey(0)
    #     return 

    def simcal(ImgUrl):
        img1 = io.imread(ImgUrl)
        img2 = io.imread(ImgUrl)

        # convert the images to grayscale
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        # define the function to compute MSE between two images
        def mse(img1, img2):
            h, w = img1.shape
            diff = cv2.subtract(img1, img2)
            err = np.sum(diff**2)
            mse = err/(float(h*w))
            return mse, diff

        error, diff = mse(img1, img2)
        if error !=0.0:
            return 0
        else:
            return 1


    # 2. Create
    def post(self, request, *args, **kwargs):
        print(request)
        request_data = {
            'imgUrl': request.imgUrl
        }

        response_data = {
            'status': 'Found',
            'name': 'Sai',
            'imgUrl': 'https://firebasestorage.googleapis.com/v0/b/treehacks-d4370.appspot.com/o/files%2FIMG-20230217-WA0040.jpg?alt=media&token=66dfc586-d2fd-4893-ab2f-00bba5e0653b',
            'location': 'India'
        }
        request_serializer = PhotoSerializer(data=request_data)
        response_serializer = ResponseSerializer(data=response_data)

        result = simcal(request.imgUrl)

        if result == 0:
            status = 'Missing',
            name =  'Not Found'
            
        if request_serializer.is_valid() and response_serializer.is_valid():
            request_serializer.save()
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)




        return Response(response_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



