FROM python:3.7
WORKDIR /workspace
ADD requirements.txt /workspace/requirements.txt
RUN pip install -r requirements.txt
ADD app.py /workspace/
RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace
CMD [ "python3" , "/workspace/app.py" ]
docker build . -t gradio_app:latest
docker run --rm -it -p 8080:8080 --user=42420:42420 gradio_app:latest
