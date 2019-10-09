
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import logging

import grpc

import casbin_pb2, casbin_pb2_grpc

ADDRESS = "localhost:50051"

if __name__ == '__main__':
    logging.info("Trying to connect to casbin server.")
    channel = grpc.insecure_channel(ADDRESS)
    stub = casbin_pb2_grpc.CasbinStub(channel)

    # Adapter can be made using an adapter request, with custom csv file or db
    # Server defaults will be used, if the request is empty
    adapter = stub.NewAdapter(casbin_pb2.NewAdapterRequest())

    # Enforcer can be made using an enforcer request, with custom conf file based on the policy
    # Server defaults will be used, if the request is empty
    enforcer = stub.NewEnforcer(casbin_pb2.NewEnforcerRequest(modelText="", adapterHandle= adapter.handler))
    logging.info("Enforcer: %s", enforcer)

    resp = stub.GetAllActions(casbin_pb2.EmptyRequest())
    print(resp)

