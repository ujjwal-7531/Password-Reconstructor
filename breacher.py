# O(N^2) with steps
def breach_n2_show(password):
    print('\nReconstructing Password....')
    char="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_+=[]{}|\\:;\"'.,/?~"
    lt=len(password)
    itr=0
    pwd=''
    for i in range(lt):
        j=0
        while password[i]!=char[j]:
            print(pwd+char[j],itr)
            j+=1
            itr+=1
        else:
            itr+=1
            pwd+=char[j]
            print(pwd,itr)
    print('\n')
    print('Reconstructed: ',pwd)
    print(f"Total Iterations for n^2: {itr}\n")

#O(NlonN) with steps
def breach_nln_show(password):
    print('\nReconstructing Password....')
    char="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_+=[]{}|\\:;\"'.,/?~"
    char=''.join(sorted(char))
    lt=len(password)
    itr=0
    pwd=''
    for i in range(lt):
        l=0
        h=len(char)-1
        while(l<=h):
            mid=l+(h-l)//2
            if ord(char[mid])==ord(password[i]):
                pwd+=char[mid]
                print(pwd,itr)
                itr+=1
                break
            elif ord(char[mid])>ord(password[i]):
                h=mid-1
            else:
                l=mid+1
            print(pwd+char[mid],itr)
            itr+=1
    itr-=1
    print('\n')
    print('Reconstructed: ',pwd)
    print(f"Total Iterations for nlog(n): {itr}\n")
    
# O(N^2) without steps
def breach_n2_hide(password):
    print('\nReconstructing Password....\n')
    char="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_+=[]{}|\\:;\"'.,/?~"
    lt=len(password)
    itr=0
    pwd=''
    for i in range(lt):
        j=0
        while password[i]!=char[j]:
            j+=1
            itr+=1
        else:
            itr+=1
            pwd+=char[j]
    print('Reconstructed: ',pwd)
    print(f"Total Iterations for n^2: {itr}\n")

#O(NlonN) without steps
def breach_nln_hide(password):
    print('\nReconstructing Password....\n')
    char="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_+=[]{}|\\:;\"'.,/?~"
    char=''.join(sorted(char))
    lt=len(password)
    itr=0
    pwd=''
    for i in range(lt):
        l=0
        h=len(char)-1
        while(l<=h):
            mid=l+(h-l)//2
            if ord(char[mid])==ord(password[i]):
                pwd+=char[mid]
                itr+=1
                break
            elif ord(char[mid])>ord(password[i]):
                h=mid-1
            else:
                l=mid+1
            itr+=1
    itr-=1
    print('Reconstructed: ',pwd)
    print(f"Total Iterations for nlog(n): {itr}\n")

print('Enter any password: ',end='')
password=input()

print('\nOptions: \n1. n^2 with steps.\n2. nlon(n) with steps.\n3. n^2 without steps.\n4. nlon(n) without steps.')
print('Choose option: ',end='')
opt=int(input())
if(opt==1):
    breach_n2_show(password)
if(opt==2):
    breach_nln_show(password)
if(opt==3):
    breach_n2_hide(password)
if(opt==4):
    breach_nln_hide(password)