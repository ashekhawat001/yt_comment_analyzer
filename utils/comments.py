import csv
from datetime import datetime as dt

comments = []
today = dt.today().strftime('%d-%m-%Y')

def process_comments(response_items, csv_output=False):

    for res in response_items:

        # loop through the replies
        if 'replies' in res.keys():
            for reply in res['replies']['comments']:
                comment = reply['snippet']
                comment['commentId'] = reply['id']
                comments.append(comment)
        else:
            comment = {}
            comment['snippet'] = res['snippet']['topLevelComment']['snippet']
            comment['snippet']['parentId'] = None
            comment['snippet']['commentId'] = res['snippet']['topLevelComment']['id']

            comments.append(comment['snippet'])

    if csv_output:
         make_csv(comments)
    
    print(f'Finished processing {len(comments)} comments.')
    return comments

def make_csv(comments, videoId=None):
    header = ['index', 'videoId', 'comment', 'likes']

    if videoId:
        filename = f'comments_{videoId}_{today}.csv'
    else:
        filename = f'comments_{today}.csv'

    with open(filename, 'w', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header, extrasaction='ignore')
        writer.writeheader()
        for i, comment in enumerate(comments, start=1):
            writer.writerow({
                'index': i,
                'videoId': videoId,
                'comment': comment['textOriginal'],
                'likes': comment['likeCount']
            })
