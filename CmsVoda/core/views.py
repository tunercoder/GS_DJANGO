from django.shortcuts import render,HttpResponse
from .models import Human,TblSmsq
from django.db.models import Q
from django.http import JsonResponse
from datetime import datetime
import re
# Create your views here.
# def home(request,msisdn,startdate,enddate):
#     diff_in_days = (enddate-startdate).days
#     # print('difference between startdate and end date is :::',diff_in_days)

#     startdate_currdate_diff = (datetime.now().date() - startdate).days
#     # print('difference between current date and startdate is :::',startdate_currdate_diff)

#     if diff_in_days > 7: #Invalid date range – in case date range is more than 7 day period
#         response = 'Invalid date range as endate and start date difference should be  <= 7 days'
#     elif startdate_currdate_diff > 90: # Current Day - 90 days check
#         response = 'Invalid search period as difference between current date and startdate is > 90 days'
#     else:
#         #getting data for msisdn within date range startdate and enddate
#         data = Human.objects.filter(Q(msisdn=msisdn) & Q(requestdatetime__date__range=(startdate, enddate))).values('msisdn','requestdatetime','smstext')
#         # data = Human.objects.filter(Q(msisdn=msisdn) & Q(requestdatetime__date__gte=startdate, requestdatetime__date__lte=enddate)).values('msisdn','requestdatetime','smstext')
       
#         #regex pattern to search mobile number with 10 digits in smstext
#         string_pattern = r"[98765]{1}[0-9]{9}"
#         regex_pattern = re.compile(string_pattern)
#         if data.exists():
#             for dic in data:
#                 for ky in dic: 
#                     if ky == 'requestdatetime':
#                         dic[ky]=dic[ky].strftime('%Y-%m-%d %H:%M:%S')
#                     if ky == 'smstext':
#                         matchobj=re.search(regex_pattern, dic[ky])
#                         if matchobj:
#                             mobile_number=matchobj.group()
#                             if mobile_number:
#                                 dic[ky]=re.sub(mobile_number[0:6], '******', dic[ky])                       
#                     # print(ky,dic[ky],type(dic[ky]),sep=' :after is : ')
#             response = list(data[:140])  # wrap in list(), because QuerySet is not JSON serializable and return 140 records only
#         else:
#             response = 'No data found'

#     return JsonResponse(response, safe=False)  # or JsonResponse({'data': data}) in case of dictionary else we have to use safe-False for other data structures
    
def home(request,msisdn,startdate,enddate):
    diff_in_days = (enddate-startdate).days
    # print('difference between startdate and end date is :::',diff_in_days)

    startdate_currdate_diff = (datetime.now().date() - startdate).days
    # print('difference between current date and startdate is :::',startdate_currdate_diff)

    if diff_in_days > 7: #Invalid date range – in case date range is more than 7 day period
        response = 'Invalid date range as endate and start date difference should be  <= 7 days'
    elif startdate_currdate_diff > 90: # Current Day - 90 days check
        response = 'Invalid search period as difference between current date and startdate is > 90 days'
    else:
        #getting data for msisdn within date range startdate and enddate
        data = TblSmsq.objects.filter(Q(smsq_int_msisdn=msisdn) & Q(smsq_dtm_request_time__date__range=(startdate, enddate))).values('smsq_int_msisdn','smsq_dtm_request_time','smsq_str_smstext')
        print(data.query)
        #regex pattern to search mobile number with 10 digits in smstext
        string_pattern = r"[98765]{1}[0-9]{9}"
        regex_pattern = re.compile(string_pattern)
        if data.exists():
            for dic in data:
                for ky in dic: 
                    if ky == 'smsq_dtm_request_time':
                        dic[ky]=dic[ky].strftime('%Y-%m-%d %H:%M:%S')
                    if ky == 'smsq_str_smstext':
                        matchobj=re.search(regex_pattern, dic[ky])
                        if matchobj:
                            mobile_number=matchobj.group()
                            if mobile_number:
                                dic[ky]=re.sub(mobile_number[0:6], '******', dic[ky])                       
                    # print(ky,dic[ky],type(dic[ky]),sep=' :after is : ')
            response = list(data[:140])  # wrap in list(), because QuerySet is not JSON serializable and return 140 records only
        else:
            response = 'No data found'

    return JsonResponse(response, safe=False)  # or JsonResponse({'data': data}) in case of dictionary else we have to use safe-False for other data structures
