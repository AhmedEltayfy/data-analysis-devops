FROM python:3.10-slim

WORKDIR /app

COPY . /app
RUN ls -l /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -c "import arabic_reshaper"
EXPOSE 8501
RUN flake8 streamlit_app.py test_data_validation.py
CMD streamlit run streamlit_app.py --server.port=$PORT --server.enableCORS=false
