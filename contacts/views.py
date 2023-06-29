from django.shortcuts import render
from models import Contact
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response

# Create your views here.

class ContactView(APIView):
    def post(self,request):
        email = request.data.get('email')
        phoneNumber = request.data.get('phoneNumber')
        query = Q()
        if phoneNumber:
            query |= Q(phoneNumber=phoneNumber)
        if email:
            query |= Q(email=email)
        
        contacts = Contact.objects.filter((query))
        new_contact = dict()
        if not primary_contact:
            new_contact = {
                'phoneNumber' : request.data['phoneNumber'] if 'phoneNumber' in request.data else None,
                'email': request.data['email'] if 'email' in request.data else None,
                'linkPrecedence':'primary'
            }
        else:
            
            for contact in contacts:
                if contact.linkPrecedence == 'primary':
                    primary_contact = contact
                    break
            new_contact = {
                'phoneNumber' : request.data['phoneNumber'] if 'phoneNumber' in request.data else None,
                'email': request.data['email'] if 'email' in request.data else None,
                'linkedId':primary_contact.id,
            }
        contact = Contact.objects.create(**new_contact)
        contacts.append(contact)
        data = dict()
        primaryContatctId,emails,phoneNumbers,secondaryContactIds = None,list(),list(),list()
        for contact in contacts:
            if contact.linkPrecedence == "primary":
                primaryContatctId = contact.id
                emails.insert(0,contact.email)
                phoneNumbers.insert(0,contact.phoneNumber)
                continue
            else:
                secondaryContactIds.append(contact.id)
                emails.append(contact.email)
                phoneNumbers.append(contact.phoneNumber)
                secondaryContactIds.append(contact.id)
        data = {
            'primaryContatctId' : primaryContatctId,
            'emails' : emails,
            'phoneNumbers' : phoneNumbers,
            'secondaryContactIds':secondaryContactIds
        }
        
        
            
            
                
                
            
            
        
        
            
        







# class ContactView(APIView):
#     def post(self, request):
#         kwargs = dict()
#         if 'email' in request.data:
#             kwargs['email'] = request.data['email']
#         if 'phoneNumber' in request.data:
#             kwargs['phoneNumber'] = request.data['phoneNumber']
#         kwargs['linkPrecedence'] = 'primary'
#         contacts = Contact.objects.filter(**kwargs) # primary_contact
#         if not contacts:
#             contact = Contact()
#             if 'email' in request.data:
#                 contact.email = request.data['email']
#             if 'phoneNumber' in request.data:
#                 contact.phoneNumber = request.data['phoneNumber']
#             contact.linkPrecedence = 'primary'
#             new_contact = contact.save()
#         else: # seconday
#             contact = Contact()
#             if 'email' in request.data:
#                 contact.email = request.data['email']
#             if 'phoneNumber' in request.data:
#                 contact.phoneNumber = request.data['phoneNumber']
#             contact.linkedId = contacts[0].id
#             new_contact = contact.save()
#         all_contacts = Contact.objects.all()
#         primaryContatctId,secondaryContactIds = None,list()
#         emails,phoneNumbers = list(),list()
#         for contact in all_contacts:
#             if contact.linkPrecedence == 'primary':
#                 primaryContatctId = contact.id
#             if contact.linkPrecedence == 'secondary':
#                 secondaryContactIds.append(contact.id)
#             if contact.email:
#                 emails.append(contact.email)
#             if contact.phoneNumber:
#                 phoneNumbers.append(contact.phoneNumber)
#         data = {
#             "primaryContatctId" : primaryContatctId,
#             "emails" : emails,
#             "phoneNumbers" : phoneNumbers,
#             "secondaryContactIds":secondaryContactIds
#         }
#         return {"data": {"contact":data}}
            
                
            
            
            
            
            
            
        
        
            
            