import pandas as pd
# from dataprep.eda import create_report
import json
import argparse
import boto3
from pandas_profiling import ProfileReport
from boto3.s3.transfer import S3Transfer

# import common parameters
CONFIG_FILE = 'config.json'
C = json.load(open(CONFIG_FILE))



# ----------------------------------------------
# #on eda button click these all scripts are to be executed in sequence

# #list all files in particular user directory of s3 to check if report.html is already present or not
# allfiles = []
# resp = s3.list_objects_v2(Bucket='testbucketai', Prefix='dinesh/heart/')
# for obj in resp['Contents']:
#   allfiles.append(obj['Key'].split("/")[-1])



# #check if report is already present in s3 or not and then follow if-else according to it
# if 'report.html' in allfiles:
#     print("report already present")
#     # download report.html from s3 to local and render it
#     with open('report.html', 'wb') as f:
#         s3.download_fileobj('testbucketai', 'dinesh/heart/report.html', f)
#     #render the downloaded report.html from local
# else:
#     print("report is not present in s3")
#     #create the report, render it then upload to s3
    
#     #0. Download csv from s3
#     result = self.s3client.get_object(Bucket='testbucketai', Key= 'dinesh/heart/report.html')
#     file = result['Body'].read().decode('utf-8')
#     initial_df = pd.read_csv(file) 
#     print("This is downloded csvDf from s3",initial_df.head(5))
    
#     #1. create report using dataprep by the df created from csv
#    profile = ProfileReport(initial_df, title="Pandas Profiling Report")
#     #2. save it on local
#     tosavethis.save()
    
#     #3. directly upload it from local to s3 for future reference
#     s3.upload_file('report.html', 'testbucketai', 'dinesh/heart/report.html')
    
#     #4. render report.html directly from local
# -----------------------------------------------

class GetReportDetails():
    def __init__(self, user: str, project: str, dfile: str):
        print('inside init')
        self.user = user
        self.proj = project
        self.dfile = dfile
        # initialize s3 client
        self.s3client = boto3.client('s3', aws_access_key_id=C['AWS_ACCESS_KEY'],aws_secret_access_key=C['AWS_ACCESS_SECRET_KEY'])

    #

    def generateReport(self):

        # on eda button click these all scripts are to be executed in sequence

        # list all files in particular user directory of s3 to check if report.html is already present or not
        allfiles = []
        prefix=self.user+"/"+self.proj+"/"
        resp = self.s3client.list_objects_v2(Bucket=C['PROJECT_BUCKET'], Prefix=prefix)
        for obj in resp['Contents']:
            allfiles.append(obj['Key'].split("/")[-1])

        # check if report is already present in s3 or not and then follow if-else according to it
        if 'report.html' in allfiles:
            print("report already present")
        # download report.html from s3 to local and render it
            with open('D:/ML_pipeline/appFlask/templates/report.html', 'wb') as f:
                self.s3client.download_fileobj(C['PROJECT_BUCKET'], 'dinesh/heart/report.html', f)
        # render the downloaded report.html from local
        else:
            print("report is not present in s3")
            # create the report, render it then upload to s3
            #0. Download csv from s3
            key=self.user+"/"+self.proj+"/"+self.dfile
            result = self.s3client.get_object(Bucket=C['PROJECT_BUCKET'], Key=key)
            # print("csv downloaded")
            # file = result['Body'].read().decode('utf-8')
            # print("complete reading of csv",file)
            initial_df = pd.read_csv(result['Body']) 
            print("This is downloded csvDf from s3",initial_df.head(5))
        
            #1. create report using dataprep by the df created from csv
            profile = ProfileReport(initial_df, title="Pandas Profiling Report")
            #2. save it on local
            print("saving eda report")
            profile.to_file("D:/ML_pipeline/appFlask/templates/report.html")

            # 3. directly upload it from local to s3 for future reference
            self.s3client.upload_file('D:/ML_pipeline/appFlask/templates/report.html', 'testbucketai', 'dinesh/heart/report.html')

        # 4. render report.html directly from local

    # make a function for downloading a file from s3
#     def getCsvFromS3(self):
#         print('inside getProjectDataFile')
#          # 0. Download csv from s3
#         result = self.s3client.get_object(
#         Bucket='testbucketai', Key='dinesh/heart/report.html')
#         file = result['Body'].read().decode('utf-8')
#         initial_df = pd.read_csv(file)
#         print("This is downloded csvDf from s3", initial_df.head(5)


#         # result = self.s3client.get_object(
#         #     Bucket=C['PROJECT_BUCKET'], Key=f'{self.user}/{self.proj}/{self.dfile}')


#         # print("result",result)
#         # result = self.s3client.get_object(Bucket=C['PROJECT_BUCKET'], Key="manish/heart/US_Heart_Patients.csv"){self.dfile}
#         #0. Download csv from s3
#      result = self.s3client.get_object(Bucket='testbucketai', Key= 'dinesh/heart/report.html')

#         file = result['Body'].read().decode('utf-8')

#         initial_df = pd.read_csv(file)  # 'Body' is a key word
#         print("This is downloded csvDf from s3", initial_df.head(5))
#         return initial_df

#         # make a condition to check wheather there is early report or not

#     # def edaReportGeneration(self):
#     #     print('inside eda report generate')
#     #     # df1 = pd.read_csv("read from s3")
#     #     reportCsvDf=self.getCsvFromS3()
#     #     report = create_report(reportCsvDf)
#     #     report.save()
#     # list all files in particular user directory of s3 to check if report.html is already present or not
#     allfiles = []
#     resp = s3.list_objects_v2(Bucket='testbucketai', Prefix='dinesh/heart/')
#     for obj in resp['Contents']:
#         allfiles.append(obj['Key'].split("/")[-1])

#     # create the report, render it then upload to s3


#     # 3. directly upload it from local to s3 for future reference
#     s3.upload_file('report.html', 'testbucketai', 'dinesh/heart/report.html')

#     # 4. render report.html directly from local

#         # check if report is already present in s3 or not and then follow if-else according to it
#     if 'report.html' in allfiles:
#         print("report already present")
#         # download report.html from s3 to local and render it
#         with open('report.html', 'wb') as f:
#             s3.download_fileobj('testbucketai', 'dinesh/heart/report.html', f)
#         # render the downloaded report.html from local
#     else:
#         print("report is not present in s3")
#         # 1. create report using dataprep by the df created from csv
#     tosavethis = create_report(df)
#     # 2. save it on local
#     tosavethis.save()


#         # upload repost to s3 (html report to csv folder in s3 )
#         # report download from s3
#         # render to web page on button click

#         # make a function for uoloading report


if __name__ == "__main__":
    # Disabled in notebook.
    # contruct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument('-u', '--user', type=str, required=True, help='username')
    ap.add_argument('-p', '--proj', type=str, required=True, help='project')
    ap.add_argument('-d', '--dfile', type=str, required=True, help='datafile')
    args = vars(ap.parse_args())
    print(f'input arguments: {args}')
    args_user = args['user']
    args_proj = args['proj']
    args_dfile = args['dfile']
    print(f'input user: {args_user}')
    print(f'input proj: {args_proj}')
    print(f'input datafile: {args_dfile}')

    # invoke class
    reportDetails = GetReportDetails(args_user, args_proj, args_dfile)
    reportDetails.edaReportGeneration()
    print("DONE")
