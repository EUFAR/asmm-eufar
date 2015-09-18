# module based on EGADS/netcdf_io.py created by Matt Freer in the EUFAR framework

import netCDF4

class FileCore(object):
 
    def __init__(self, filename=None, perms='r', **kwargs):
        self.f = None
        self.filename = filename
        self.perms = perms

        for key, val in kwargs.iteritems():
            setattr(self, key, val)
        if filename is not None:
            self._open_file(filename, perms)

    def open(self, filename, perms=None):
        if perms is not None:
            self.perms = perms
        else:
            perms = self.perms
        self._open_file(filename, perms)

    def close(self):
        if self.f is not None:
            self.f.close()
            self.f = None
            self.filename = None

    def get_perms(self):
        if self.f is not None:
            return self.perms
        else:
            return

    def get_filename(self):
        return self.filename


class NetCdf(FileCore):
    
    TYPE_DICT = {'char':'c',
        'byte':'b',
        'short':'i2',
        'int':'i4',
        'float':'f4',
        'double':'f8'}

    def __del__(self):
        if self.f is not None:
            self.f.close()

    def open(self, filename, perms=None):
        FileCore.open(self, filename, perms)

    def get_attribute_list(self, varname=None):
        return self._get_attribute_list(varname)

    def get_attribute_value(self, attrname, varname=None):
        attrs = self._get_attribute_list(varname)
        return attrs[attrname]

    def get_dimension_list(self, varname=None):
        return self._get_dimension_list(varname)

    def get_variable_list(self):
        return self._get_variable_list()

    def get_perms(self):
        if self.f is not None:
            return self.perms
        else:
            return

    def read_variable(self, varname, input_range=None):
        try:
            varin = self.f.variables[varname]
        except KeyError:
            raise KeyError("ERROR: Variable %s does not exist in %s" % (varname, self.filename))
        except Exception:
            print "Error: Unexpected error"
            raise
        if input_range is None:
            value = varin[:]
        else:
            obj = 'slice(input_range[0], input_range[1])'
            for i in xrange(2, len(input_range), 2):
                obj = obj + ', slice(input_range[%i], input_range[%i])' % (i, i + 1)
            value = varin[eval(obj)]
        return value

    def _open_file(self, filename, perms):
        self.close()
        try:
            self.f = netCDF4.Dataset(filename, perms)  # @UndefinedVariable
            self.filename = filename
            self.perms = perms
        except RuntimeError:
            raise RuntimeError("ERROR: File %s doesn't exist" % (filename))
        except Exception:
            print "ERROR: Unexpected error"
            raise

    def _get_attribute_list(self, var=None):
        if self.f is not None:
            if var is not None:
                varin = self.f.variables[var]
                return varin.__dict__
            else:
                return self.f.__dict__
        else:
            raise

    def _get_dimension_list(self, var=None):
        dimdict = {}
        if self.f is not None:
            file_dims = self.f.dimensions
            if var is not None:
                varin = self.f.variables[var]
                dims = varin.dimensions
                for dimname in dims:
                    dimobj = file_dims[dimname]
                    dimdict[dimname] = len(dimobj)
            else:
                dims = file_dims
                for dimname, dimobj in dims.iteritems():
                    dimdict[dimname] = len(dimobj)
            return dimdict
        else:
            raise
        return None

    def _get_variable_list(self):

        if self.f is not None:
            return self.f.variables.keys()
        else:
            raise