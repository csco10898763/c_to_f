# echo "# c_to_f" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/csco10898763/c_to_f.git
# git push -u origin main

# git remote add origin https://github.com/csco10898763/c_to_f.git
# git branch -M main
# git push -u origin main

temp_C = input('請輸入攝氏溫度：')
temp_C = float(temp_C)
temp_F = temp_C * 9 / 5 + 32

print('\n攝氏溫度：', temp_C, '等於華氏溫度：', temp_F)