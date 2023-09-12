# AWS SAM + Swagger

AWS SAM と Swagger での API 定義を使用した API Gateway を構築する検証用リポジトリです

## 構成情報

- Python: 3.11
- AWS SAM CLI: 1.95.0

## ローカル環境構築

### ライブラリをインストールする

```sh
pip install -r requirements.txt
```

### ビルドを行う

```sh
sam build
```

### 実行する

```sh
sam local invoke GetFunction
```

## デプロイ手順

### ビルドを行う

```sh
sam build
```

### デプロイ定義ファイルを作成する

初めての環境にデプロイする際は, 予めデプロイの定義を作成しデプロイする

```sh
sam deploy --guided --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM
```

### 再デプロイの方法

既にデプロイの定義がある際は, 下記のコマンドでデプロイする

```sh
sam deploy
```

### API Gateway のデプロイ

AWS SAM で API Gateway の設定は変更されても, API Gateway 自体をデプロイしないと反映されないため<br />
下記のコマンドで API Gateway をデプロイする

```sh
aws apigateway create-deployment --rest-api-id `<REST_API_ID>` --stage-name `<ステージ名>`
```

### API Gateway へリクエストする

```sh
curl -X GET https://<REST_API_ID>.execute-api.<リージョン名>.amazonaws.com/<ステージ名>/device
```

## 注意事項

- `sam local start-api` コマンドは, Integration の proxy タイプのみで, aws タイプには対応していない

## ドキュメント

- [AWS SAM - AWS::Serverless::Api](https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/sam-resource-api.html)
