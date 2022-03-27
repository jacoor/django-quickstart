FROM python:3.9 
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
RUN pipenv install
