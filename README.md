# git版本控制系統-學習筆記

## 1.什麼是Git
Git是分散式的版本控制軟體

在不同版本中會比較差異, 存取差異處

## 2.安裝Git
[git安裝連結](https://git-scm.com/downloads)

檢查git是否安裝成功
```bash
git --version
```

git基本操作指令
```bash
git config --global user.name "FIRST_NAME LAST_NAME" #設定名字
git config --global user.email "MY_NAME@example.com" #設定email
git init                        #初始化Git Repository
git status                       #觀察Repository檔案追蹤狀況
git log                         #查詢更改紀錄
git log --oneline --graph --all #將紀錄以圖呈現
git add .                       #將檔案加入追蹤清單
git commit -m 'message'               #此處填版本訊息
git branch                       #看分支名稱
git remote -v                     #查詢遠端的repository
git remote add 遠端空間名稱 遠端名稱網址     #將本機端和Github雲端上的專案相連
git push 遠端空間名稱 遠端空間的分支名稱     #將本機資料上傳到雲端
git clone 遠端空間網址 本機資料夾名稱       #下載/複製Github雲端專案到本機端
git rm file                    #剛除檔案
git rm file --cached               #取消追蹤, 檔案不會被刪除
git mv file1 file2                #修改檔名
git branch name                  #建立分支
git branch -d name               #刪除分支
git checkout name                #切換分支
git checkout -b name             #可以同時建立和切換分支
git merge name                   #先切換到master, 可以選擇合併其他分支
```

## 3.在本地端創建一個Git的Repository

先在本機端資料夾下建立git倉庫
```bash
git init
git status
git add .
git commit -m "message"
git status
```

* 在git init後會在資料夾中產生一個隱藏檔.git, 顯示隱藏檔打開即可看到

* 若要刪除追蹤, 直接將隱藏檔刪除即可

## 4.Github與 Git
Github是託管Git的雲端平台，讓你Git的程式碼可以放在網路上

登入Github後, 新建new repository
```
git remote -v
git remote add 遠端空間名稱 遠端空間網址
git push 遠端空間名稱 遠端空間的分支名稱
git status
```

## 5. 版本衝突處理
在發生衝突的地方插入git找到差異的部份, 做修改後再重新提交
```bash
git add 修改好的file
git commit -m "message"
```


