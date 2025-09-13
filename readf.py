with open('текстовый файл.txt','r',encoding='utf-8') as file:
    content = file.read()
    print(content)


with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(content)
    file.write("\n") 
    file.write("\n")
    file.write("кое-что еще") 
    print('Recording done')