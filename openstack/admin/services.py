from openstack.api import base
from openstack.compute.api import API_OPTIONS


class Services(base.Resource):
    def __repr__(self):
        return "<Service: %s>" % self.name

    def update(self, disabled):
        self.manager.update(self.id, disabled)


class ServiceManager(base.ManagerWithFind):
    resource_class = Services

    def list(self):
        return self._list("/admin/services", "services")

    def get(self, id):
#        FIXME(dt): search services ourself until we get ServiceController.show added
#        return self._get("/admin/services/%s" % id, "services")
        services = self._list("/admin/services", "services")
        for service in services:
            if str(service.id) == str(id):
                return service
        return None

    def update(self, id, disabled):
        body = {"service": {'disabled': disabled}}
        self._update("/admin/services/%s" % id, body)
