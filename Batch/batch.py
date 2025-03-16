import time
import boto3
import datetime

input_file = 'example.mp3'
input_bucket = 'tnobe-transcribe/input'
output_bucket = 'tnobe-transcribe'
output_key = 'output/'

language = 'ja-JP'

file_uri = f's3://{input_bucket}/{input_file}'

def transcribe_file(job_name, file_uri, transcribe_client):
    transcribe_client.start_transcription_job(
        TranscriptionJobName = job_name,
        Media = {
            'MediaFileUri': file_uri
        },
        MediaFormat = 'mp3',
        LanguageCode = language,
        OutputBucketName=output_bucket,
        OutputKey=output_key
    )

    max_tries = 60
    while max_tries > 0:
        max_tries -= 1
        job = transcribe_client.get_transcription_job(TranscriptionJobName = job_name)
        job_status = job['TranscriptionJob']['TranscriptionJobStatus']
        if job_status in ['COMPLETED', 'FAILED']:
            print(f"Job {job_name} is {job_status}.")
            if job_status == 'COMPLETED':
                print(
                    f"Download the transcript from\n"
                    f"\t{job['TranscriptionJob']['Transcript']['TranscriptFileUri']}.")
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(10)


def main():
    transcribe_client = boto3.client('transcribe')
    now = datetime.datetime.now()
    now_formatted = now.strftime('%Y%m%d%H%M%S')
    job_name = f'Example-job-{now_formatted}'
    transcribe_file(job_name, file_uri, transcribe_client)


if __name__ == '__main__':
    main()