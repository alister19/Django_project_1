class MyMixin(object):
    mixin_group = ''

    def get_grop(self):
        return self.mixin_group.upper()