#Downloading python3 image from docker repo 
FROM python
#Running shell command
RUN pip3 install requests
COPY question3.py .
ENV site=http://www.stackoverflow.com
ENV times=5
#working directory
 
WORKDIR "/app"
#Add question3.py to dockerfile working directory
ADD question3.py .

#Executing script
CMD ["python3", "question3.py"]