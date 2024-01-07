FROM ubuntu@sha256:2b7412e6465c3c7fc5bb21d3e6f1917c167358449fecac8176c6e496e5c1f05f
MAINTAINER Lys

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq xinetd

RUN useradd -m lab
RUN chown -R root:root /home/lab
RUN chmod -R 755 /home/lab

USER lab
CMD ["/usr/sbin/xinetd", "-dontfork"]
