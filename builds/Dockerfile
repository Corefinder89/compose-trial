FROM ubuntu:latest

# Install updates to base image
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install tzdata
ENV TZ=Australia/Melbourne
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata
RUN apt-get update -y \
 && apt-get install -y software-properties-common \
                       apt-utils \
                       curl \
                       wget \
                       unzip \
                       libxss1 \
                       libappindicator1 \
                       libindicator7 \
                       libasound2 \
                       libgconf-2-4 \
                       libnspr4 \
                       libnss3 \
                       libpango1.0-0 \
                       fonts-liberation \
                       xdg-utils \
                       git
RUN add-apt-repository ppa:deadsnakes/ppa

# Install chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update \
 && apt-get install -y google-chrome-stable

# Install python
# Install python version 3.0+
RUN apt install -y python3.8 \
                  python3-pip
