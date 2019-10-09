# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import casbin_pb2 as casbin__pb2


class CasbinStub(object):
  """The Casbin service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.NewEnforcer = channel.unary_unary(
        '/proto.Casbin/NewEnforcer',
        request_serializer=casbin__pb2.NewEnforcerRequest.SerializeToString,
        response_deserializer=casbin__pb2.NewEnforcerReply.FromString,
        )
    self.NewAdapter = channel.unary_unary(
        '/proto.Casbin/NewAdapter',
        request_serializer=casbin__pb2.NewAdapterRequest.SerializeToString,
        response_deserializer=casbin__pb2.NewAdapterReply.FromString,
        )
    self.Enforce = channel.unary_unary(
        '/proto.Casbin/Enforce',
        request_serializer=casbin__pb2.EnforceRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.LoadPolicy = channel.unary_unary(
        '/proto.Casbin/LoadPolicy',
        request_serializer=casbin__pb2.EmptyRequest.SerializeToString,
        response_deserializer=casbin__pb2.EmptyReply.FromString,
        )
    self.SavePolicy = channel.unary_unary(
        '/proto.Casbin/SavePolicy',
        request_serializer=casbin__pb2.EmptyRequest.SerializeToString,
        response_deserializer=casbin__pb2.EmptyReply.FromString,
        )
    self.AddPolicy = channel.unary_unary(
        '/proto.Casbin/AddPolicy',
        request_serializer=casbin__pb2.PolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.AddNamedPolicy = channel.unary_unary(
        '/proto.Casbin/AddNamedPolicy',
        request_serializer=casbin__pb2.PolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.RemovePolicy = channel.unary_unary(
        '/proto.Casbin/RemovePolicy',
        request_serializer=casbin__pb2.PolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.RemoveNamedPolicy = channel.unary_unary(
        '/proto.Casbin/RemoveNamedPolicy',
        request_serializer=casbin__pb2.PolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.RemoveFilteredPolicy = channel.unary_unary(
        '/proto.Casbin/RemoveFilteredPolicy',
        request_serializer=casbin__pb2.FilteredPolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.RemoveFilteredNamedPolicy = channel.unary_unary(
        '/proto.Casbin/RemoveFilteredNamedPolicy',
        request_serializer=casbin__pb2.FilteredPolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.GetPolicy = channel.unary_unary(
        '/proto.Casbin/GetPolicy',
        request_serializer=casbin__pb2.EmptyRequest.SerializeToString,
        response_deserializer=casbin__pb2.Array2DReply.FromString,
        )
    self.GetNamedPolicy = channel.unary_unary(
        '/proto.Casbin/GetNamedPolicy',
        request_serializer=casbin__pb2.PolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.Array2DReply.FromString,
        )
    self.GetFilteredPolicy = channel.unary_unary(
        '/proto.Casbin/GetFilteredPolicy',
        request_serializer=casbin__pb2.FilteredPolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.Array2DReply.FromString,
        )
    self.GetFilteredNamedPolicy = channel.unary_unary(
        '/proto.Casbin/GetFilteredNamedPolicy',
        request_serializer=casbin__pb2.FilteredPolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.Array2DReply.FromString,
        )
    self.AddGroupingPolicy = channel.unary_unary(
        '/proto.Casbin/AddGroupingPolicy',
        request_serializer=casbin__pb2.PolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.AddNamedGroupingPolicy = channel.unary_unary(
        '/proto.Casbin/AddNamedGroupingPolicy',
        request_serializer=casbin__pb2.PolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.RemoveGroupingPolicy = channel.unary_unary(
        '/proto.Casbin/RemoveGroupingPolicy',
        request_serializer=casbin__pb2.PolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.RemoveNamedGroupingPolicy = channel.unary_unary(
        '/proto.Casbin/RemoveNamedGroupingPolicy',
        request_serializer=casbin__pb2.PolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.RemoveFilteredGroupingPolicy = channel.unary_unary(
        '/proto.Casbin/RemoveFilteredGroupingPolicy',
        request_serializer=casbin__pb2.FilteredPolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.RemoveFilteredNamedGroupingPolicy = channel.unary_unary(
        '/proto.Casbin/RemoveFilteredNamedGroupingPolicy',
        request_serializer=casbin__pb2.FilteredPolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.GetGroupingPolicy = channel.unary_unary(
        '/proto.Casbin/GetGroupingPolicy',
        request_serializer=casbin__pb2.EmptyRequest.SerializeToString,
        response_deserializer=casbin__pb2.Array2DReply.FromString,
        )
    self.GetNamedGroupingPolicy = channel.unary_unary(
        '/proto.Casbin/GetNamedGroupingPolicy',
        request_serializer=casbin__pb2.PolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.Array2DReply.FromString,
        )
    self.GetFilteredGroupingPolicy = channel.unary_unary(
        '/proto.Casbin/GetFilteredGroupingPolicy',
        request_serializer=casbin__pb2.FilteredPolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.Array2DReply.FromString,
        )
    self.GetFilteredNamedGroupingPolicy = channel.unary_unary(
        '/proto.Casbin/GetFilteredNamedGroupingPolicy',
        request_serializer=casbin__pb2.FilteredPolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.Array2DReply.FromString,
        )
    self.GetAllSubjects = channel.unary_unary(
        '/proto.Casbin/GetAllSubjects',
        request_serializer=casbin__pb2.EmptyRequest.SerializeToString,
        response_deserializer=casbin__pb2.ArrayReply.FromString,
        )
    self.GetAllNamedSubjects = channel.unary_unary(
        '/proto.Casbin/GetAllNamedSubjects',
        request_serializer=casbin__pb2.SimpleGetRequest.SerializeToString,
        response_deserializer=casbin__pb2.ArrayReply.FromString,
        )
    self.GetAllObjects = channel.unary_unary(
        '/proto.Casbin/GetAllObjects',
        request_serializer=casbin__pb2.EmptyRequest.SerializeToString,
        response_deserializer=casbin__pb2.ArrayReply.FromString,
        )
    self.GetAllNamedObjects = channel.unary_unary(
        '/proto.Casbin/GetAllNamedObjects',
        request_serializer=casbin__pb2.SimpleGetRequest.SerializeToString,
        response_deserializer=casbin__pb2.ArrayReply.FromString,
        )
    self.GetAllActions = channel.unary_unary(
        '/proto.Casbin/GetAllActions',
        request_serializer=casbin__pb2.EmptyRequest.SerializeToString,
        response_deserializer=casbin__pb2.ArrayReply.FromString,
        )
    self.GetAllNamedActions = channel.unary_unary(
        '/proto.Casbin/GetAllNamedActions',
        request_serializer=casbin__pb2.SimpleGetRequest.SerializeToString,
        response_deserializer=casbin__pb2.ArrayReply.FromString,
        )
    self.GetAllRoles = channel.unary_unary(
        '/proto.Casbin/GetAllRoles',
        request_serializer=casbin__pb2.EmptyRequest.SerializeToString,
        response_deserializer=casbin__pb2.ArrayReply.FromString,
        )
    self.GetAllNamedRoles = channel.unary_unary(
        '/proto.Casbin/GetAllNamedRoles',
        request_serializer=casbin__pb2.SimpleGetRequest.SerializeToString,
        response_deserializer=casbin__pb2.ArrayReply.FromString,
        )
    self.HasPolicy = channel.unary_unary(
        '/proto.Casbin/HasPolicy',
        request_serializer=casbin__pb2.PolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.HasNamedPolicy = channel.unary_unary(
        '/proto.Casbin/HasNamedPolicy',
        request_serializer=casbin__pb2.PolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.HasGroupingPolicy = channel.unary_unary(
        '/proto.Casbin/HasGroupingPolicy',
        request_serializer=casbin__pb2.PolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.HasNamedGroupingPolicy = channel.unary_unary(
        '/proto.Casbin/HasNamedGroupingPolicy',
        request_serializer=casbin__pb2.PolicyRequest.SerializeToString,
        response_deserializer=casbin__pb2.BoolReply.FromString,
        )
    self.GetRolesForUser = channel.unary_unary(
        '/proto.Casbin/GetRolesForUser',
        request_serializer=casbin__pb2.UserRoleRequest.SerializeToString,
        response_deserializer=casbin__pb2.ArrayReply.FromString,
        )
    self.GetImplicitRolesForUser = channel.unary_unary(
        '/proto.Casbin/GetImplicitRolesForUser',
        request_serializer=casbin__pb2.UserRoleRequest.SerializeToString,
        response_deserializer=casbin__pb2.ArrayReply.FromString,
        )
    self.GetUsersForRole = channel.unary_unary(
        '/proto.Casbin/GetUsersForRole',
        request_serializer=casbin__pb2.UserRoleRequest.SerializeToString,
        response_deserializer=casbin__pb2.ArrayReply.FromString,
        )
    self.GetPermissionsForUser = channel.unary_unary(
        '/proto.Casbin/GetPermissionsForUser',
        request_serializer=casbin__pb2.PermissionRequest.SerializeToString,
        response_deserializer=casbin__pb2.Array2DReply.FromString,
        )
    self.GetImplicitPermissionsForUser = channel.unary_unary(
        '/proto.Casbin/GetImplicitPermissionsForUser',
        request_serializer=casbin__pb2.PermissionRequest.SerializeToString,
        response_deserializer=casbin__pb2.Array2DReply.FromString,
        )


class CasbinServicer(object):
  """The Casbin service definition.
  """

  def NewEnforcer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NewAdapter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Enforce(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LoadPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SavePolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddNamedPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemovePolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveNamedPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveFilteredPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveFilteredNamedPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNamedPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFilteredPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFilteredNamedPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddGroupingPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddNamedGroupingPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveGroupingPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveNamedGroupingPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveFilteredGroupingPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveFilteredNamedGroupingPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetGroupingPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNamedGroupingPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFilteredGroupingPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFilteredNamedGroupingPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllSubjects(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllNamedSubjects(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllObjects(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllNamedObjects(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllActions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllNamedActions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllRoles(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllNamedRoles(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HasPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HasNamedPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HasGroupingPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HasNamedGroupingPolicy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRolesForUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetImplicitRolesForUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUsersForRole(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPermissionsForUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetImplicitPermissionsForUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CasbinServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'NewEnforcer': grpc.unary_unary_rpc_method_handler(
          servicer.NewEnforcer,
          request_deserializer=casbin__pb2.NewEnforcerRequest.FromString,
          response_serializer=casbin__pb2.NewEnforcerReply.SerializeToString,
      ),
      'NewAdapter': grpc.unary_unary_rpc_method_handler(
          servicer.NewAdapter,
          request_deserializer=casbin__pb2.NewAdapterRequest.FromString,
          response_serializer=casbin__pb2.NewAdapterReply.SerializeToString,
      ),
      'Enforce': grpc.unary_unary_rpc_method_handler(
          servicer.Enforce,
          request_deserializer=casbin__pb2.EnforceRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'LoadPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.LoadPolicy,
          request_deserializer=casbin__pb2.EmptyRequest.FromString,
          response_serializer=casbin__pb2.EmptyReply.SerializeToString,
      ),
      'SavePolicy': grpc.unary_unary_rpc_method_handler(
          servicer.SavePolicy,
          request_deserializer=casbin__pb2.EmptyRequest.FromString,
          response_serializer=casbin__pb2.EmptyReply.SerializeToString,
      ),
      'AddPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.AddPolicy,
          request_deserializer=casbin__pb2.PolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'AddNamedPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.AddNamedPolicy,
          request_deserializer=casbin__pb2.PolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'RemovePolicy': grpc.unary_unary_rpc_method_handler(
          servicer.RemovePolicy,
          request_deserializer=casbin__pb2.PolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'RemoveNamedPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveNamedPolicy,
          request_deserializer=casbin__pb2.PolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'RemoveFilteredPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveFilteredPolicy,
          request_deserializer=casbin__pb2.FilteredPolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'RemoveFilteredNamedPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveFilteredNamedPolicy,
          request_deserializer=casbin__pb2.FilteredPolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'GetPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.GetPolicy,
          request_deserializer=casbin__pb2.EmptyRequest.FromString,
          response_serializer=casbin__pb2.Array2DReply.SerializeToString,
      ),
      'GetNamedPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.GetNamedPolicy,
          request_deserializer=casbin__pb2.PolicyRequest.FromString,
          response_serializer=casbin__pb2.Array2DReply.SerializeToString,
      ),
      'GetFilteredPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.GetFilteredPolicy,
          request_deserializer=casbin__pb2.FilteredPolicyRequest.FromString,
          response_serializer=casbin__pb2.Array2DReply.SerializeToString,
      ),
      'GetFilteredNamedPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.GetFilteredNamedPolicy,
          request_deserializer=casbin__pb2.FilteredPolicyRequest.FromString,
          response_serializer=casbin__pb2.Array2DReply.SerializeToString,
      ),
      'AddGroupingPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.AddGroupingPolicy,
          request_deserializer=casbin__pb2.PolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'AddNamedGroupingPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.AddNamedGroupingPolicy,
          request_deserializer=casbin__pb2.PolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'RemoveGroupingPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveGroupingPolicy,
          request_deserializer=casbin__pb2.PolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'RemoveNamedGroupingPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveNamedGroupingPolicy,
          request_deserializer=casbin__pb2.PolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'RemoveFilteredGroupingPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveFilteredGroupingPolicy,
          request_deserializer=casbin__pb2.FilteredPolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'RemoveFilteredNamedGroupingPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveFilteredNamedGroupingPolicy,
          request_deserializer=casbin__pb2.FilteredPolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'GetGroupingPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.GetGroupingPolicy,
          request_deserializer=casbin__pb2.EmptyRequest.FromString,
          response_serializer=casbin__pb2.Array2DReply.SerializeToString,
      ),
      'GetNamedGroupingPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.GetNamedGroupingPolicy,
          request_deserializer=casbin__pb2.PolicyRequest.FromString,
          response_serializer=casbin__pb2.Array2DReply.SerializeToString,
      ),
      'GetFilteredGroupingPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.GetFilteredGroupingPolicy,
          request_deserializer=casbin__pb2.FilteredPolicyRequest.FromString,
          response_serializer=casbin__pb2.Array2DReply.SerializeToString,
      ),
      'GetFilteredNamedGroupingPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.GetFilteredNamedGroupingPolicy,
          request_deserializer=casbin__pb2.FilteredPolicyRequest.FromString,
          response_serializer=casbin__pb2.Array2DReply.SerializeToString,
      ),
      'GetAllSubjects': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllSubjects,
          request_deserializer=casbin__pb2.EmptyRequest.FromString,
          response_serializer=casbin__pb2.ArrayReply.SerializeToString,
      ),
      'GetAllNamedSubjects': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllNamedSubjects,
          request_deserializer=casbin__pb2.SimpleGetRequest.FromString,
          response_serializer=casbin__pb2.ArrayReply.SerializeToString,
      ),
      'GetAllObjects': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllObjects,
          request_deserializer=casbin__pb2.EmptyRequest.FromString,
          response_serializer=casbin__pb2.ArrayReply.SerializeToString,
      ),
      'GetAllNamedObjects': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllNamedObjects,
          request_deserializer=casbin__pb2.SimpleGetRequest.FromString,
          response_serializer=casbin__pb2.ArrayReply.SerializeToString,
      ),
      'GetAllActions': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllActions,
          request_deserializer=casbin__pb2.EmptyRequest.FromString,
          response_serializer=casbin__pb2.ArrayReply.SerializeToString,
      ),
      'GetAllNamedActions': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllNamedActions,
          request_deserializer=casbin__pb2.SimpleGetRequest.FromString,
          response_serializer=casbin__pb2.ArrayReply.SerializeToString,
      ),
      'GetAllRoles': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllRoles,
          request_deserializer=casbin__pb2.EmptyRequest.FromString,
          response_serializer=casbin__pb2.ArrayReply.SerializeToString,
      ),
      'GetAllNamedRoles': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllNamedRoles,
          request_deserializer=casbin__pb2.SimpleGetRequest.FromString,
          response_serializer=casbin__pb2.ArrayReply.SerializeToString,
      ),
      'HasPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.HasPolicy,
          request_deserializer=casbin__pb2.PolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'HasNamedPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.HasNamedPolicy,
          request_deserializer=casbin__pb2.PolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'HasGroupingPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.HasGroupingPolicy,
          request_deserializer=casbin__pb2.PolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'HasNamedGroupingPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.HasNamedGroupingPolicy,
          request_deserializer=casbin__pb2.PolicyRequest.FromString,
          response_serializer=casbin__pb2.BoolReply.SerializeToString,
      ),
      'GetRolesForUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetRolesForUser,
          request_deserializer=casbin__pb2.UserRoleRequest.FromString,
          response_serializer=casbin__pb2.ArrayReply.SerializeToString,
      ),
      'GetImplicitRolesForUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetImplicitRolesForUser,
          request_deserializer=casbin__pb2.UserRoleRequest.FromString,
          response_serializer=casbin__pb2.ArrayReply.SerializeToString,
      ),
      'GetUsersForRole': grpc.unary_unary_rpc_method_handler(
          servicer.GetUsersForRole,
          request_deserializer=casbin__pb2.UserRoleRequest.FromString,
          response_serializer=casbin__pb2.ArrayReply.SerializeToString,
      ),
      'GetPermissionsForUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetPermissionsForUser,
          request_deserializer=casbin__pb2.PermissionRequest.FromString,
          response_serializer=casbin__pb2.Array2DReply.SerializeToString,
      ),
      'GetImplicitPermissionsForUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetImplicitPermissionsForUser,
          request_deserializer=casbin__pb2.PermissionRequest.FromString,
          response_serializer=casbin__pb2.Array2DReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.Casbin', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
