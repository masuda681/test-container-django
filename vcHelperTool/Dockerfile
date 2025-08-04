FROM python:3.11-slim

# 必要なライブラリ・ツールをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    unzip \
    libx11-6 \
    libxt6 \
    libxrender1 \
    libnsl2 \
    libgtk2.0-0 \
    libpng16-16 \
    libc6 \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# ovftoolのZIPファイルをコンテナへコピー
COPY VMware-ovftool-5.0.0-24781994-lin.x86_64.zip /tmp/ovftool.zip

# 解凍してパスを通す
RUN unzip /tmp/ovftool.zip -d /opt && \
    rm -f /tmp/ovftool.zip

ENV PATH="/opt/vmware-ovftool:$PATH"

# 作業ディレクトリ
WORKDIR /work

CMD ["/bin/bash"]

# -------------------------------------------
# # Python 3.11 ベースの公式イメージを使用
# FROM python:3.11-slim

# # 必要なパッケージと作業ディレクトリの設定
# WORKDIR /app

# # アプリケーションコードのコピー（ビルド対象がローカルにある場合）
# # COPY . .

# # アプリケーションコードのコピー
# COPY . /app

# # Pythonライブラリのインストール（Django, pyVmomiなど）
# RUN pip install --no-cache-dir -r requirements.txt

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
