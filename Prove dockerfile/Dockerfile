FROM kathara/frr

RUN mkdir goBgp && \
    cd ./goBgp && \
    wget -q -O GOBGP.tar.gz https://github.com/osrg/gobgp/releases/download/v3.26.0/gobgp_3.26.0_linux_amd64.tar.gz && \
    tar xf GOBGP.tar.gz

ENV PATH=$PATH:/goBgp