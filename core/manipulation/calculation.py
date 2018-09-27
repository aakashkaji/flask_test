# from core.myspreadsheet.google_sheet import SpreadSheet
#
# ls = ['int', 'interested']
#
#
# def make_data(sheet_range='A22:E27', r=1):
#     total=0
#     form_data = []
#     result = SpreadSheet().get_data(sheet_range)
#     values = result.get('values')
#     ra= result.get('range')
#     for j in range(1, len(values)):
#         col = 'G' + str(r + j)
#
#         if [i for i in ls if i in values[j][2].lower()]:
#             total += 1
#             va = dict(enumerate(values[j]))
#             d = {}
#             d.update(name=va.get(0), phone=va.get(1), email=va.get(4), location=col)
#             form_data.append(d)
#
#             # print(values[j])
#             # print('found')
#         else:
#             pass
#         #     print('no..')
#         # print(type(j), j)
#     return form_data


def make_data_set(result, r):
    form_data = []
    total = 0
    ls = ['int', 'interested']
    values = result.get('values')
    # ra = result.get('range')
    for j in range(0, len(values)):
        col = 'H' + str(r + j)
        va = dict(enumerate(values[j]))
        if bool(va.get(6)):
            if [i for i in ls if i in va.get(6).lower()]:
                total += 1
                d = {}
                d.update(name=va.get(0), phone=va.get(1)[-10:], email=va.get(2), message=va.get(3),
                         from_company=va.get(4), flat_size=va.get(5), location=col)
                form_data.append(d)

                # print(values[j])
                # print('found')
            else:
                pass
            #     print('no..')
            # print(type(j), j)
    print(total)
    return form_data


# def make_update_data(dict_data):
#     """
#     this dict contains time_stamp, locations(i.e range)
#     this function basically update data in google sheet
#
#     :param list_data:
#     :return:
#
#     """
#     value = []
#     if dict_data.get('status') == 200 or 201:
#         value.append(dict_data.get('time_stamp'))
#         value.append('done')
#
#     else:
#
#         pass
#     return value
