FROM python:3.12-slim

ARG USER=matthieu
ARG HOME=/home/$USER
ARG UID=1000

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV && \
    useradd -d $HOME -s /bin/bash -m $USER -u $UID -U && \
    apt-get update && apt-get install -y wget gnupg2 

# Install dependencies:
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | tee /etc/apt/keyrings/packages.mozilla.org.asc  > /dev/null
RUN gpg -n -q --import --import-options import-show /etc/apt/keyrings/packages.mozilla.org.asc | awk '/pub/{getline; gsub(/^ +| +$/,""); if($0 == "35BAA0B33E9EB396F59CA838C0BA5CE6DC6315A3") print "\nLʼempreinte de la clé correspond ("$0").\n"; else print "\nÉchec de la vérification : lʼempreinte ("$0") ne correspond pas à celle attendue.\n"}'
RUN echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
RUN apt-get update
RUN apt-get install -y firefox

WORKDIR $HOME
USER $USER
ENV HOME=$HOME

CMD ["jupyter", "lab"]
