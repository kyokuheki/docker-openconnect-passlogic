FROM alpine:edge
LABEL maintainer Kenzo Okuda <kyokuheki@gmail.com>

ENV VPNC=/etc/vpnc/vpnc-script

RUN set -x \
 && apk add --no-cache -X https://dl-cdn.alpinelinux.org/alpine/edge/testing \
    openconnect \
 && apk add --no-cache \
    iproute2 \
    py3-lxml \
    py3-pandas

COPY ./assets/* /
RUN chmod +x /wrapper-script /passlogic.py

ENTRYPOINT []
CMD set -x \
 && python3 /passlogic.py | /usr/bin/openconnect \
      --passwd-on-stdin \
      --no-dtls \
      --verbose \
      --script=/wrapper-script \
      --user=$USERID \
      $VPN_HOST \
