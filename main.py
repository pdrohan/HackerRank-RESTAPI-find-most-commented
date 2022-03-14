#This is a remake of a question that I read wrong during a timed technical assignment
#Enumerate ! Such a helpful tool i seem to always forget

data = {'num pages': 1, 'data':[
    {'title': 'Outside 1',
    'num_comments': 3100},
    {'title': 'Mind the Gap',
    'num_comments': 2500},
    {'title': 'A Tiger King',
    'num_comments': 2500},
    {'title': 'Lost at Sea',
    'num_comments': 2700},
    {'title': 'Routes',
    'num_comments': 2700},
        {'title': 'Lets go!',
    'num_comments': 2500},
        {'title': 'Yes Men',
    'num_comments': 2500},
    {'title': 'A Yes man 2',
    'num_comments': 2500}
]}


limit = 3
output_list = []
result = data['data']

for i in range(0, len(result)):
    if len(output_list) < limit:
        output_list.append([result[i]['title'], result[i]['num_comments']])
    else:
        all_titles = [x[0] for x in output_list]

        for index, inlists in enumerate(output_list):
            all_titles = [x[0] for x in output_list]
            if inlists[1] < result[i]['num_comments'] and result[i]['title'] not in all_titles:
                output_list[index][0] = result[i]['title']
                output_list[index][1] = result[i]['num_comments']
                break
            if inlists[1] == result[i]['num_comments'] and result[i]['title'] not in all_titles:
                if inlists[0] > result[i]['title']:
                    output_list[index][0] = result[i]['title']
                    output_list[index][1] = result[i]['num_comments']

output_list.sort(key=lambda output_list: (output_list[1], output_list[0]))

print(output_list)

