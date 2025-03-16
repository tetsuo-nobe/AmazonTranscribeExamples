# AmazonTranscribeExamples

[Amazon Transcribe 開発者ガイド](https://docs.aws.amazon.com/ja_jp/transcribe/latest/dg/what-is.html)

* Batch
  - S3 バケット内の mp3 ファイルからテキスト起こしを行い、結果の JSON ファイルを S3 バケットへ格納する

* CustomVocabulary
  - カスタムボキャブラリーを作成する
    - 日本語の場合、英字が混じった言葉よりも全角の固有名詞の方が適用されやすいようだ。
      - 例1: COツー → CO2 は、適用されにくい
      - 例2: 徳川義信 → 徳川慶喜 は適用されやすい
  - 作成したカスタムボキャブラリーを使用して、S3 バケット内の mp3 ファイルからテキスト起こしを行い、結果の JSON ファイルを S3 バケットへ格納する
