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