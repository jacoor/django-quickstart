FROM python:3.9 
ENV DEBIAN_FRONTEND noninteractive
ENV GECKODRIVER_VER v0.31.0
ENV FIREFOX_VER 100.0
ENV TERM=xterm
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/www/:/www/.venv/:/www/.venv/bin
ENV PIPENV_VENV_IN_PROJECT=1
RUN git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \
    && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \
    && chsh -s /bin/zshrc.zsh-template \ 
    && echo '[[ "$TERM" == "xterm" ]] && export TERM=xterm-256color' >> ~/.zshrc \
    && echo 'source /www/venv/bin/activate' >> ~/.zshrc \
    && echo 'source /www/venv/bin/activate' >> ~/.bashrc
WORKDIR /www
RUN pip install pipenv
RUN pipenv --python 3.9
RUN pipenv install --dev
RUN set -x \
    && apt update \
    && apt upgrade -y \
    && apt install -y \
    firefox-esr 

# Add latest FireFox
RUN set -x \
    && apt install -y \
    libx11-xcb1 \
    libdbus-glib-1-2 \
    && curl -sSLO https://download-installer.cdn.mozilla.net/pub/firefox/releases/${FIREFOX_VER}/linux-x86_64/en-US/firefox-${FIREFOX_VER}.tar.bz2 \
    && tar -jxf firefox-* \
    && mv firefox /opt/ \
    && chmod 755 /opt/firefox \
    && chmod 755 /opt/firefox/firefox

# Add geckodriver
RUN set -x \
    && curl -sSLO https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VER}/geckodriver-${GECKODRIVER_VER}-linux64.tar.gz \
    && tar zxf geckodriver-*.tar.gz \
    && mv geckodriver /usr/bin/