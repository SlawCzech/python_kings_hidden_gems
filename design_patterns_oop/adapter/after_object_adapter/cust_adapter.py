from design_patterns_oop.adapter.after_object_adapter.abs_adapter import AbsAdapter


class CustomerAdapter(AbsAdapter):
    @property
    def name(self):
        return self._adaptee.name

    @property
    def address(self):
        return self._adaptee.address

