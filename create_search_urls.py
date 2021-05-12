f = open('search_urls.txt', 'w+')
url = 'https://www.amazon.com/s?k=processor&i=computers&ref=nb_sb_noss_1'

f.write(url)
f.write('\n')

for i in range(2,401):
    url = 'https://www.amazon.com/s?k=processor&i=computers&page=2' + str(i) + '&qid=1617019761&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()