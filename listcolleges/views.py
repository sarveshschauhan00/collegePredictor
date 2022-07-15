from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView
from .models import RankTable
from .forms import RankForm
import csv


# def index(request):
#     rank_form = None
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = request.POST
#     return render(request, 'index.html', {})

def filturing_college(filt, file_path):
    ls_dict = {}
    rank = 872432 * (100 - filt['percentile']) // 100
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[-4] == filt['catagory'] and row[-4]!='OPEN':
                if (filt['gender'] == row[-3] or row[-3] == 'Gender-Neutral'):
                    try:
                        if int(row[-2]) - int(filt['main_catagory_rank']) * 0.01 <= int(filt['main_catagory_rank']) <= int(
                                row[-1]) + int(filt['main_catagory_rank']) * 0.01:
                            if row[0] not in ls_dict:
                                ls_dict[row[0]] = []
                            ls_dict[row[0]].append((row[2], row[1], row[3], row[4], row[5], row[6]))
                    except:
                        continue

            elif row[-4] == 'OPEN':
                if (filt['gender'] == row[-3] or row[-3] == 'Gender-Neutral'):
                    try:
                        if int(row[-2]) - rank * 0.01 <= rank <= int(row[-1]) + rank * 0.01:
                            if row[0] not in ls_dict:
                                ls_dict[row[0]] = []
                            ls_dict[row[0]].append((row[2], row[1], row[3], row[4], row[5], row[6]))
                    except:
                        continue
    for coll in ls_dict:
        ls_dict[coll].sort(reverse=True)
    return ls_dict

def filturing_iit_college(filt, file_path):
    ls_dict = {}
    rank = filt['advanced_general_rank']
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[-4] == filt['catagory'] and row[-4]!='OPEN':
                if (filt['gender'] == row[-3] or row[-3] == 'Gender-Neutral'):
                    try:
                        if int(row[-2]) - int(filt['advanced_catagory_rank']) * 0.01 <= int(filt['advanced_catagory_rank']) <= int(
                                row[-1]) + int(filt['advanced_catagory_rank']) * 0.01:
                            if row[0] not in ls_dict:
                                ls_dict[row[0]] = []
                            ls_dict[row[0]].append((row[2], row[1], row[3], row[4], row[5], row[6]))
                    except:
                        continue

            elif row[-4] == 'OPEN':
                if (filt['gender'] == row[-3] or row[-3] == 'Gender-Neutral'):
                    try:
                        if int(row[-2]) - rank * 0.01 <= rank <= int(row[-1]) + rank * 0.01:
                            if row[0] not in ls_dict:
                                ls_dict[row[0]] = []
                            ls_dict[row[0]].append((row[2], row[1], row[3], row[4], row[5], row[6]))
                    except:
                        continue
    for coll in ls_dict:
        ls_dict[coll].sort(reverse=True)
    return ls_dict




def print_list(args):
    ls_nit = []
    ls_iit = []
    ls_iiit = []
    ls_govt_funded = []

    ls_nit.append(filturing_college(args, 'listcolleges/dataset/nit_list.csv'))
    ls_iiit.append(filturing_college(args, 'listcolleges/dataset/iiit_list.csv'))
    ls_govt_funded.append(filturing_college(args, 'listcolleges/dataset/govt_funded_list.csv'))

    ls_iit.append(filturing_iit_college(args, 'listcolleges/dataset/iit_list.csv'))

    # for ls in ls_all:
    #     for ele in ls:
    #         print(ele, " :- ")
    #         for ele1 in ls[ele]:
    #             print(" " * 8, ele1)
    #         print()
    return {'N.I.T.':ls_nit, 'I.I.T.':ls_iit, 'I.I.I.T.':ls_iiit, 'Government Funded Colleges':ls_govt_funded}



def index(request):
    ls_total=[]
    args = None
    if request.method == 'POST':
        rank_form = RankForm(request.POST)
        if rank_form.is_valid():
            args = {
                'gender': rank_form.cleaned_data['gender'],
                'percentile': rank_form.cleaned_data['percentile'],
                'catagory': rank_form.cleaned_data['catagory'],
                'main_catagory_rank': rank_form.cleaned_data['main_catagory_rank'],
                'advanced_general_rank': rank_form.cleaned_data['advanced_general_rank'],
                'advanced_catagory_rank': rank_form.cleaned_data['advanced_catagory_rank']
            }
            # print(args)
            # print("Rank:-", 872432 * (100 - args['percentile']) // 100)
            ls_total = print_list(args)
    else:
        rank_form = RankForm()

    if args!=None:
        cal_rank = 872432 * (100 - args['percentile']) // 100
        # q = RankTable(gender=args['gender'], percentile=args['percentile'], catagory=args['catagory'], main_catagory_rank=args['main_catagory_rank'], advanced_catagory_rank=args['advanced_catagory_rank'], advanced_general_rank=args['advanced_general_rank'])
        # q.save()
    else:
        cal_rank = "Null"

    return render(request, 'index.html', {'form': rank_form, 'ls_total':ls_total, 'rank':cal_rank})



