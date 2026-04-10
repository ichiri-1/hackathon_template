# デプロイ手順メモ
## 前提
- Renderにデプロイ済み
- リモートリポジトリのmainブランチへのプッシュ（develop->mainへのマージ）でデプロイ

## 手順

### 1. developの最新を取り込む

```bash
git switch develop
git pull origin develop
```

### 2. ローカルで動作確認

```bash
# developブランチでビルド
docker build -f docker/prod/Dockerfile -t app-prod:latest .

# コンテナ起動
docker run --name app_prod -e PORT=8080 -p 8080:8080 myapp-prod:latest
```
localhost:8080 にアクセスし動作確認

### 3. 変更があればコミット・プッシュ

```bash
git add path/to/file
git commit -m "comment"
git push origin develop
```
-> 動作確認

### 4. PRを作成してマージ
リモートのdevelop -> main へのPRマージ

### 5. Renderのデプロイを確認