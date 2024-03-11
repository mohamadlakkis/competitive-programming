#https://leetcode.com/problems/custom-sort-string/
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ORD = {}
        for i,c in enumerate(list(order)):
            ORD[c] = i
        #Now we will do merge sort but the comparison will be based on ORD and not on the actual value 

        arr = list(s)
        def mergeSort(arr):
            if len(arr) > 1:
                mid = len(arr)//2
                L = arr[:mid]
                R = arr[mid:]
                mergeSort(L)
                mergeSort(R)
                #Merge Step 
                # k holds the pos of the arr where we need now to insert !
                i = j = k = 0
                while i < len(L) and j < len(R):
                    if L[i] in ORD and R[j] in ORD and ORD[L[i]] < ORD[R[j]]:
                        arr[k] = L[i]
                        i += 1
                    elif L[i] in ORD and R[j] not in ORD:
                        arr[k] = R[j]
                        j+=1
                    elif R[j] in ORD and L[i] not in ORD:
                        arr[k] = L[i]
                        i+=1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1
        
                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1
        mergeSort(arr)
        return "".join(arr)
        
