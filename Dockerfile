# Contains a set of instructions used to build a Docker image.

FROM python:3.11

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

# Set ownership and copy files/directories from the host machine to the container's filesystem during the build process.
COPY --chown=${USER} ./app.py app.py
COPY --chown=${USER} ./application application

USER ${USER}

ENTRYPOINT ["flask", "run"]
