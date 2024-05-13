# HTTP-FLOOD

## Web API -

### Developer Setup for Linux

- Recommended: Create a new Python environment (using Venv):

  - `python3 -m venv {env_name}`

- Recommended (contd.): Activate the new Python environment

  - `source {env_name}/bin/activate`

- Install dependencies

  - `pip3 install fastapi uvicorn`

- Run web application:

  - `uvicorn web:app --host 0.0.0.0 --port {port_number}`

- Navigate over to the static url: `http://127.0.0.1:{port_number}/static`

## DDOS Script

- Navigate over to the "DDOS Script" directory and run the python script:
  - `python3 web.py {url path} {desired number of threads}`
