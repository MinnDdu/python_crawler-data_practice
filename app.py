# making new file - open('path', 'w')
# making new binary file - open('path', 'wb')
file = open('a.txt', 'w')
file.write('Hello guys!')
file.close()

# appending sth - open('path', 'a')
file = open('a.txt', 'a')
file.write('\nNice to meet you')
file.close()

# reading file - open('path', 'r')
file = open('a.txt', 'r')
print(file.read())
file.close()

# CSV file
f = open('data.csv', 'w')


list = ['Samsung', 'Kakao', 'Naver', 'Sinpoong']

for i in range(len(list)):
    f.write('\n' + list[i])

for i in range(2, 10):
    f.write('\n')
    for j in range(1, 10):
        f.write('\n')
        f.write(str(i*j))


f.close()
