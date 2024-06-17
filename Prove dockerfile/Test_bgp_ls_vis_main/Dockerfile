FROM kathara/frr

RUN mkdir goBgp && \
    cd ./goBgp && \
    wget -q -O GOBGP.tar.gz https://github.com/osrg/gobgp/releases/download/v3.26.0/gobgp_3.26.0_linux_amd64.tar.gz && \
    tar xf GOBGP.tar.gz

RUN wget https://www.python.org/ftp/python/3.9.17/Python-3.9.17.tar.xz && \
    tar xfv Python-3.9.17.tar.xz && \
    cd Python-3.9.17 && \
    ./configure --enable-optimizations --enable-shared && \
    make -j8 build_all && \
    make -j8 altinstall && \
    ldconfig && \
    cd .. && rm -rf Python-3.9.17*
    

RUN git clone https://github.com/YungTimAllen/bgp-ls-vis.git && \
    cd bgp-ls-vis && \
    python3.9 -m pip install --break-system-packages -r requirements.txt


ENV PATH=$PATH:/goBgp