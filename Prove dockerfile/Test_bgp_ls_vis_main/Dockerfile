FROM kathara/frr

RUN mkdir goBgp && \
    cd ./goBgp && \
    wget -q -O GOBGP.tar.gz https://github.com/osrg/gobgp/releases/download/v3.26.0/gobgp_3.26.0_linux_amd64.tar.gz && \
    tar xf GOBGP.tar.gz

RUN wget https://www.python.org/ftp/python/3.9.19/Python-3.9.19.tar.xz && \
    tar xfv Python-3.9.19.tar.xz && \
    cd Python-3.9.19 && \
    ./configure --enable-optimizations --enable-shared && \
    make -j8 build_all && \
    make -j8 altinstall && \
    ldconfig && \
    cd .. && rm -rf Python-3.9.19*

RUN git clone https://github.com/YungTimAllen/bgp-ls-vis.git && \
    mv /bgp-ls-vis/bgp_ls_vis/examples.py /bgp-ls-vis && \
    cd bgp-ls-vis && \
    python3 -m pip install --break-system-packages networkx==2.5 matplotlib==3.3.2 PyYAML==5.3.1 dash==1.18.1 plotly==4.14.1 google-api-python-client==2.130.0

RUN python3 -m pip install --break-system-packages grpcio==1.64.0 grpcio-tools==1.64.0

RUN python3 -m pip install --upgrade --break-system-packages protobuf==3.20.3 && \
    python3 -m pip install --upgrade --break-system-packages numpy==1.26.4 && \
    python3 -m pip install --upgrade --break-system-packages Werkzeug==2.0.1 && \
    python3 -m pip install --upgrade --break-system-packages flask==2.1.3
   
RUN python3 -m pip install --break-system-packages dash-cytoscape==0.2.0 && \
    python3 -m pip install --break-system-packages pandas==2.2.1

ENV PATH=$PATH:/goBgp

# per provare se funziona ricordarsi di modificare con nano il file examples.py in questo modo:
# commentare esempio1 e scommentare esempio3
# togliere ../ dentro alla variabile che indica il percorso della cartella dumps