```sh
python -m synapse.app.homeserver --server-name matrix.lab-lama.com --generate-config --config-path /opt/matrix/homeserver.yaml --report-stats=no

register_new_matrix_user -c /opt/matrix/homeserver.yaml http://localhost:8008
```
