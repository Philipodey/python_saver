class Native:
    def __init__(self, _name, _scv_id):
        self._name = _name
        self._scv_id = _scv_id

    def set_name(self, _name):
        self._name = _name

    def get_name(self):
        return self._name

    def set_scv_id(self, _scv_id):
        self._scv_id = _scv_id

    def get_scv_id(self):
        return self._scv_id
