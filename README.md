Python client for Casbin Server
====

``casbin-python-client`` is Python's client for [Casbin-Server](https://github.com/casbin/casbin-server). ``Casbin-Server`` is the ``Access Control as a Service (ACaaS)`` solution based on [Casbin](https://github.com/casbin/casbin).

## Installation
    pip install -r requirements.txt

## Generating Proto Files

Run the following command inside the casbin-server folder to generate new proto files.

    python -m grpc_tools.protoc -I proto/ --python_out=$PATH_TO_CASBIN_PYTHON_CLIENT --grpc_python_out=$PATH_TO_CASBIN_PYTHON_CLIENT proto/casbin.proto  

## Run
    python main.py

## License

This project is under Apache 2.0 License. See the [LICENSE](LICENSE) file for the full license text.