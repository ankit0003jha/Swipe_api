from django.shortcuts import render
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import phoneModel, Profile, Like_dislike
import base64


## Register and login section


# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"



class getPhoneNumberRegistered(APIView):

    # Get to Create a call for OTP
    @staticmethod
    def get(request, phone):
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            phoneModel.objects.create(
                Mobile=phone,
            )
            Mobile = phoneModel.objects.get(Mobile=phone)  # user Newly created Model
        Mobile.counter += 1  # Update Counter At every Call
        Mobile.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        print(OTP.at(Mobile.counter))
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return Response({"OTP": OTP.at(Mobile.counter)}, status=200)  # Just for demonstration

    # This Method verifies the OTP
    @staticmethod
    def post(request, phone):
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        if OTP.verify(request.data["otp"], Mobile.counter):  # Verifying the OTP
            Mobile.isVerified = True
            Mobile.name = request.data["name"]  # User can enter their name
            Name = Mobile.name
            Mobile.save()
            return Response("Welcome", Name ,  "You are authorised", status=200)
        return Response("OTP is wrong", status=400)


class getPhoneNumberLogin(APIView):

    # Get to Create a call for OTP
    @staticmethod
    def get(request, phone):
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            phoneModel.objects.create(
                Mobile=phone,
            )
            Mobile = phoneModel.objects.get(Mobile=phone)  # user Newly created Model
        Mobile.counter += 1  # Update Counter At every Call
        Mobile.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        print(OTP.at(Mobile.counter))
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return Response({"OTP": OTP.at(Mobile.counter)}, status=200)  # Just for demonstration

    # This Method verifies the OTP
    @staticmethod
    def post(request, phone):
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        if OTP.verify(request.data["otp"], Mobile.counter):  # Verifying the OTP
            Mobile.isVerified = True
            Mobile.save()
            return Response("You are authorised", status=200)
        return Response("OTP is wrong", status=400)



## Like dislike section


class LikeView(APIView):
    @staticmethod
    def get(request, id=None):
        member = phoneModel.objects.get(id=id)
        user = request.user
        vote = "like"
        like = Like_dislike(member=member, user=user, vote=vote)
        like.save()
        return Response({"You have selected image"}, status=200)
        

class dislikeView(APIView):
    @staticmethod
    def get(request, id=None):
        member = phoneModel.objects.get(id=id)
        user = request.user
        like = Like_dislike.objects.filter(member=member, user=user)
        if like:
            like.delete()
        vote = "dislike"
        Like = Like_dislike(member=member, user=user, vote=vote)
        Like.save()
        return Response({"You have rejected image"}, status=200)



## History Section

class HistoryListView(APIView):
    @staticmethod
    def get(request):
        query = Like_dislike.objects.filter(user_id=request.user.id, vote="like" and "dislike")
        return Response({"query":query}, status=200)


class LikedMeListView(APIView):
    @staticmethod
    def get(request):
        result = Like_dislike.objects.filter(member_id=request.user.id)
        return Response({"Result":result}, status=200)


class WhomILikedListView(APIView):
    @staticmethod
    def get(request):
        result = Like_dislike.objects.filter(user_id=request.user.id)
        return Response({"Result":result}, status=200)