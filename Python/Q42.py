import statistics
try:
    with open('sales.txt') as f:
        nums=[float(x.strip()) for x in f if x.strip()]
    print('Mean:',statistics.mean(nums))
    print('Median:',statistics.median(nums))
except Exception as e:
    print('Error:',e)
