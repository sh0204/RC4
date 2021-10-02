def KSA(key): #KSA를 통해 배열S를 구성 = 키스트림 초기화 단계
    key = key.encode()
    j = 0
    S = []
    for i in range(0,256): #S배열에 0부터 255까지의 숫자를 넣음
        S.append(i)
    for i in range(0,256): #입력받은 키값을 이용하여 이 값들을 섞음
        j=(j + S[i] + key[i%len(key)]) %256 
        S[i],S[j] = S[j],S[i]
    return S

def encryption(plain,S): #암호화
    i=0
    j=0
    stream_key= [] 
    plain=plain.encode() 
    enc=bytearray() #빈 바이트 배열 객체 생성

    #PRGA를 통해 키 스트림을 구성, 평문을 암호화
    for k in range(len(plain)): #for문을 평문 길이 만큼 돌면서 swap 진행
        i=(i+1) % 256
        j = (j+S[i]) % 256
        S[i],S[j]=S[j],S[i]
        stream_key.append(S[(S[i] + S[j])%256])
        enc.append( plain[k] ^ stream_key[k]) 
    return enc

def decryption(enc,S): #복호화
    i=0
    j=0
    stream_key =[]  
    dec = bytearray() #빈 바이트 배열 객체 생성

    for k in range(len(enc)): #암호화에 사용된 똑같은 키 스트림을 사용, 암호문과 XOR 연산 
        i=(i+1) % 256
        j=(j+S[i]) % 256
        S[i],S[j]=S[j],S[i]
        stream_key.append(S[(S[i] + S[j])%256])
        dec.append(enc[k] ^ stream_key[k]) #평문으로 다시
    return dec

#출력형태
plain = input("Plain Text: ") 
key = input("Key: ") 

stream= KSA(key) 
enc=encryption(plain,stream) 

print("Encryption: ",enc) 
dec=decryption(enc,KSA(key)) 
print("Decryption: ",dec) 



