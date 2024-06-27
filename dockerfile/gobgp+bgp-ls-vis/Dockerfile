FROM kathara/frr:debian10

RUN mkdir goBgp && \
    cd ./goBgp && \
    wget -q -O GOBGP.tar.gz https://github.com/osrg/gobgp/releases/download/v3.26.0/gobgp_3.26.0_linux_amd64.tar.gz && \
    tar xf GOBGP.tar.gz
  
RUN git clone https://github.com/YungTimAllen/bgp-ls-vis.git && \
    mv /bgp-ls-vis/bgp_ls_vis/examples.py /bgp-ls-vis

COPY requirements.txt /bgp-ls-vis/requirements.txt
COPY upgrades.txt /bgp-ls-vis/upgrades.txt

RUN python3 -m pip install --break-system-packages -r /bgp-ls-vis/requirements.txt

RUN python3 -m pip install --upgrade --break-system-packages -r /bgp-ls-vis/upgrades.txt

RUN git clone https://github.com/osrg/gobgp.git 

ENV PATH=$PATH:/goBgp

# per provare se funziona ricordarsi di modificare con nano il file examples.py in questo modo:
# commentare esempio1 e scommentare esempio3
# togliere ../ dentro alla variabile che indica il percorso della cartella dumps