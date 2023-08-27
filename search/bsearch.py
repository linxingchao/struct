class Search:
    @staticmethod
    def bsearch(arr,value):
        n = len(arr)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) /2
            if arr[mid] == value:
                return mid
            elif arr[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    @staticmethod
    def bsearch2(arr,value):
        n = len(arr)
        return Search._bsearch_internally(arr,0,n-1,value)
    
    @staticmethod
    def _bsearch_internally(arr,low,high,value):
        if low > high:
            return -1
        
        mid = low + ((high-low >> 1))
        if arr[mid] == value:
            return mid;
        elif arr[mid] < value:
            return Search._bsearch_internally(arr,mid + 1,high,value)
        else:
            return Search._bsearch_internally(arr,low,mid-1,value)
        
    '''
    查找第一个等值
    ''' 
    @staticmethod
    def bsearch3(arr,value):
        n = len(arr)
        low = 0
        high = n - 1
        while low <= high:
            mid = int((low + high) / 2)
            if arr[mid] > value:
                high = mid - 1
            elif arr[mid] < value:
                low = mid + 1
            else:
                if mid == 0 or arr[mid-1] != value:
                    return mid
                else:
                    high = mid - 1
        return -1
    '''
    查找第一个大于等于value的元素
    '''
    @staticmethod
    def bsearch4(arr,value):
        n = len(arr)
        low = 0
        high = n - 1
        while low <= high:
            mid = int((low + high) / 2)
            if arr[mid] >= value:
                if mid == 0 or arr[mid - 1] < value:
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1
        return -1
    
    '''
    查找最后一个小于或等于value的元素
    '''
    @staticmethod
    def bsearch5(arr,value):
        n = len(arr)
        low = 0
        high = n - 1
        while low <= high:
            mid = int((low + high) / 2)
            if arr[mid] <= value:
                if mid == n-1 or arr[mid+1]>value:
                    return mid
                else:
                    low = mid + 1
                    
        return -1
        