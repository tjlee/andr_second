# Task 2
# Function checks first list of filling and sorts it for next oprations.
def check_fill_sort(s1, full_count):
    if len(s1) == full_count:
        s1.sort()
        return True
    else:
        return False

def output_complex_list(complex_list, number):
    output_string = ''
    for i in range(len(complex_list)):
        output_string = output_string + complex_list[i][number]
    return output_string
        
        
log_file = 'log.txt'
count = -1  # First line of file doesn't contain request, so it doesn't need.
s = []
s_min_brow = []  # List of requests with fastest time of loading trough the browser.
s_max_brow = []  # List of requests with slowest time of loading trough the browser.
s_min_brow_count = 10  # The count of fastest requests for point 4) in the task. 
curl_sum = 0
brow_sum = 0
curl_max = 0
curl_min = 0
brow_max = 0
brow_min = 0
curl_min_line = ''
curl_max_line = ''
brow_min_line = ''
brow_max_line = ''

pct_max_brow = 5  # Percent of slowest requests for point 2) in the task.

for line in open(log_file).xreadlines():
    count = count + 1
#  The count of slowest requests fo point 2) in the task.
s_max_brow_count = int(round(count*pct_max_brow*0.01))

for line in open(log_file).xreadlines():
    s = line.split(',')
    if len(s) == 6:
        curl = float(s[2])  # Time of curl loading in current request
        brow = float(s[3])  # Time of browser loading in current request

        # For point 1)
        curl_sum = curl_sum + curl
        brow_sum = brow_sum + brow

        # Solving 3)
        if curl < curl_min or curl_min_line == '':
            curl_min = curl
            curl_min_line = line
        if curl > curl_max or curl_max_line == '':
            curl_max = curl
            curl_max_line = line
        if brow < brow_min or brow_min_line == '':
            brow_min = brow
            brow_min_line = line
        if brow > brow_max or brow_max_line == '':
            brow_max = brow
            brow_max_line = line

        # Solving 4): 10 minimal brow times for www.somesite/shop/...
        if len(s_min_brow) < s_min_brow_count and line.find('www.somesite.ru/shop/') != -1:
            s_min_brow.append([float(s[3]), line])

        if check_fill_sort(s_min_brow, s_min_brow_count) and line.find('www.somesite.ru/shop/') != -1:
            for i in range(s_min_brow_count - 1):
                if brow < s_min_brow[0][0]:  # esli minimal'nii
                    s_min_brow.insert(0, [brow, line])
                    s_min_brow.pop()
                    break
                if s_min_brow[i][0] <= brow <= s_min_brow[i+1][0]:
                    s_min_brow.insert(i+1, [brow, line])
                    s_min_brow.pop()
                    break
        # Solving 3): 5 percent of slowest loading times through the browser
        if len(s_max_brow) < s_max_brow_count:
            s_max_brow.append([float(s[3]), line])
        if check_fill_sort(s_max_brow, s_max_brow_count):
            for i in range(s_max_brow_count - 1):
                if brow >= s_max_brow[-1][0]:
                    s_max_brow.append([brow, line])
                    s_max_brow.remove(s_max_brow[0])
                    break
                if s_max_brow[i][0] <= brow < s_max_brow[i+1][0]:
                    s_max_brow.insert(i+1, [brow, line])
                    s_max_brow.remove(s_max_brow[0])
                    break
                    
print '1) curl_average = '+str(round(curl_sum/count, 3)) +', browser_average = ' + str(round(brow_sum/count, 6))+'\n'
print '2) 5% of slowest loading requests through the browser:\n' + output_complex_list(s_max_brow, 1)
print '3) curl_max_drop:\n' +str(curl_min_line) + str(curl_max_line) + '   browser_max_drop:\n' + str(brow_min_line) + brow_max_line
print '4) 10 fastest loading pages of shops:\n' + output_complex_list(s_min_brow, 1)

