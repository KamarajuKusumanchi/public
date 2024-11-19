-------------------------------------------------------------------------------
today | 2024-11-18

==== background ====
The ibkr cp gateway is available from
https://www.interactivebrokers.com/campus/ibkr-api-page/cpapi-v1/#gw-step-one
-> Download the Standard Release .

After installing it, I tried to run it from git bash. It failed with the
following error

<code>
raju@DESKTOP-CRLPVE5 MINGW64 ~/software/unzipped/ibkr_cp_gateway
$ ./bin/run.sh ./root/conf.yaml
running
 runtime path : ./root:dist/ibgroup.web.core.iblink.router.clientportal.gw.jar:build/lib/runtime/*
 config file  : ./root/conf.yaml
Error: Could not find or load main class ibgroup.web.core.clientportal.gw.GatewayStart
</code>

==== solution ====
The bin/run.sh script is doing something like
  java -cp "${RUNTIME_PATH}"

But it is using ':' as the path separator while initializing it. On windows, it should use ";" instead. So changing

  export RUNTIME_PATH="$config_path:dist/ibgroup.web.core.iblink.router.clientportal.gw.jar:build/lib/runtime/*"

to

  export RUNTIME_PATH="$config_path;dist/ibgroup.web.core.iblink.router.clientportal.gw.jar;build/lib/runtime/*"

will fix it. I made the fix a bit generic and added it in this directory (under ./bin/run.sh)
-------------------------------------------------------------------------------
