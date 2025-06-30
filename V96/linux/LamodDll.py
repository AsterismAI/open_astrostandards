r"""Wrapper for new_LamodDll.h

Generated with:
/home/woodkn1/DND/bin/ctypesgen -I . ./new_LamodDll.h -o ./LamodDll.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# No libraries

# No modules

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 23
for _lib in _libs.values():
    if not _lib.has("LamodInit", "cdecl"):
        continue
    LamodInit = _lib.get("LamodInit", "cdecl")
    LamodInit.argtypes = [c_int64]
    LamodInit.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 29
for _lib in _libs.values():
    if not _lib.has("LamodGetInfo", "cdecl"):
        continue
    LamodGetInfo = _lib.get("LamodGetInfo", "cdecl")
    LamodGetInfo.argtypes = [c_char * int(128)]
    LamodGetInfo.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 36
for _lib in _libs.values():
    if not _lib.has("LamodLoadFile", "cdecl"):
        continue
    LamodLoadFile = _lib.get("LamodLoadFile", "cdecl")
    LamodLoadFile.argtypes = [c_char * int(512)]
    LamodLoadFile.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 42
for _lib in _libs.values():
    if not _lib.has("LamodLoadFileAll", "cdecl"):
        continue
    LamodLoadFileAll = _lib.get("LamodLoadFileAll", "cdecl")
    LamodLoadFileAll.argtypes = [c_char * int(512)]
    LamodLoadFileAll.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 48
for _lib in _libs.values():
    if not _lib.has("LamodLoadCard", "cdecl"):
        continue
    LamodLoadCard = _lib.get("LamodLoadCard", "cdecl")
    LamodLoadCard.argtypes = [c_char * int(512)]
    LamodLoadCard.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 57
for _lib in _libs.values():
    if not _lib.has("LamodSaveFile", "cdecl"):
        continue
    LamodSaveFile = _lib.get("LamodSaveFile", "cdecl")
    LamodSaveFile.argtypes = [c_char * int(512), c_int, c_int]
    LamodSaveFile.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 64
for _lib in _libs.values():
    if not _lib.has("LamodGetNumOfSensSats", "cdecl"):
        continue
    LamodGetNumOfSensSats = _lib.get("LamodGetNumOfSensSats", "cdecl")
    LamodGetNumOfSensSats.argtypes = [POINTER(c_int), POINTER(c_int)]
    LamodGetNumOfSensSats.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 69
for _lib in _libs.values():
    if not _lib.has("LamodGetSenNums", "cdecl"):
        continue
    LamodGetSenNums = _lib.get("LamodGetSenNums", "cdecl")
    LamodGetSenNums.argtypes = [POINTER(c_int)]
    LamodGetSenNums.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 75
for _lib in _libs.values():
    if not _lib.has("LamodGetSatNums", "cdecl"):
        continue
    LamodGetSatNums = _lib.get("LamodGetSatNums", "cdecl")
    LamodGetSatNums.argtypes = [POINTER(c_int)]
    LamodGetSatNums.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 80
for _lib in _libs.values():
    if not _lib.has("LamodGet1pCard", "cdecl"):
        continue
    LamodGet1pCard = _lib.get("LamodGet1pCard", "cdecl")
    LamodGet1pCard.argtypes = [c_char * int(512)]
    LamodGet1pCard.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 95
for _lib in _libs.values():
    if not _lib.has("LamodGet1pAll", "cdecl"):
        continue
    LamodGet1pAll = _lib.get("LamodGet1pAll", "cdecl")
    LamodGet1pAll.argtypes = [POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), String, POINTER(c_int), POINTER(c_double)]
    LamodGet1pAll.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 119
for _lib in _libs.values():
    if not _lib.has("LamodSet1pAll", "cdecl"):
        continue
    LamodSet1pAll = _lib.get("LamodSet1pAll", "cdecl")
    LamodSet1pAll.argtypes = [c_int, c_double, c_double, c_double, c_int, c_int, c_int, c_int, c_char, c_int, c_double]
    LamodSet1pAll.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 149
for _lib in _libs.values():
    if not _lib.has("LamodGet1pField", "cdecl"):
        continue
    LamodGet1pField = _lib.get("LamodGet1pField", "cdecl")
    LamodGet1pField.argtypes = [c_int, c_char * int(512)]
    LamodGet1pField.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 156
for _lib in _libs.values():
    if not _lib.has("LamodSet1pField", "cdecl"):
        continue
    LamodSet1pField = _lib.get("LamodSet1pField", "cdecl")
    LamodSet1pField.argtypes = [c_int, c_char * int(512)]
    LamodSet1pField.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 163
for _lib in _libs.values():
    if not _lib.has("LamodGet3pAll", "cdecl"):
        continue
    LamodGet3pAll = _lib.get("LamodGet3pAll", "cdecl")
    LamodGet3pAll.argtypes = [POINTER(c_int), c_int * int(3)]
    LamodGet3pAll.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 170
for _lib in _libs.values():
    if not _lib.has("LamodSet3pAll", "cdecl"):
        continue
    LamodSet3pAll = _lib.get("LamodSet3pAll", "cdecl")
    LamodSet3pAll.argtypes = [c_int, c_int * int(3)]
    LamodSet3pAll.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 176
for _lib in _libs.values():
    if not _lib.has("LamodGetObsFileName", "cdecl"):
        continue
    LamodGetObsFileName = _lib.get("LamodGetObsFileName", "cdecl")
    LamodGetObsFileName.argtypes = [c_char * int(512)]
    LamodGetObsFileName.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 184
for _lib in _libs.values():
    if not _lib.has("LamodSetObsFileName", "cdecl"):
        continue
    LamodSetObsFileName = _lib.get("LamodSetObsFileName", "cdecl")
    LamodSetObsFileName.argtypes = [c_char * int(512)]
    LamodSetObsFileName.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 194
for _lib in _libs.values():
    if not _lib.has("LamodSenSatVisible", "cdecl"):
        continue
    LamodSenSatVisible = _lib.get("LamodSenSatVisible", "cdecl")
    LamodSenSatVisible.argtypes = [c_int64, c_int64]
    LamodSenSatVisible.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 206
for _lib in _libs.values():
    if not _lib.has("LamodInitSenSat", "cdecl"):
        continue
    LamodInitSenSat = _lib.get("LamodInitSenSat", "cdecl")
    LamodInitSenSat.argtypes = [c_int64, c_int64]
    LamodInitSenSat.restype = c_int64
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 220
for _lib in _libs.values():
    if not _lib.has("LamodInitSenSat_MT", "cdecl"):
        continue
    LamodInitSenSat_MT = _lib.get("LamodInitSenSat_MT", "cdecl")
    LamodInitSenSat_MT.argtypes = [c_double * int(16), c_int64, c_int64]
    LamodInitSenSat_MT.restype = c_int64
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 232
for _lib in _libs.values():
    if not _lib.has("LamodGetSenSatDataAll", "cdecl"):
        continue
    LamodGetSenSatDataAll = _lib.get("LamodGetSenSatDataAll", "cdecl")
    LamodGetSenSatDataAll.argtypes = [c_int64, POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    LamodGetSenSatDataAll.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 257
for _lib in _libs.values():
    if not _lib.has("LamodGetSenSatDataField", "cdecl"):
        continue
    LamodGetSenSatDataField = _lib.get("LamodGetSenSatDataField", "cdecl")
    LamodGetSenSatDataField.argtypes = [c_int64, c_int, c_char * int(512)]
    LamodGetSenSatDataField.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 264
for _lib in _libs.values():
    if not _lib.has("LamodSenSatDataToArray", "cdecl"):
        continue
    LamodSenSatDataToArray = _lib.get("LamodSenSatDataToArray", "cdecl")
    LamodSenSatDataToArray.argtypes = [c_int64, c_double * int(32)]
    LamodSenSatDataToArray.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 272
for _lib in _libs.values():
    if not _lib.has("LamodGetNumPasses", "cdecl"):
        continue
    LamodGetNumPasses = _lib.get("LamodGetNumPasses", "cdecl")
    LamodGetNumPasses.argtypes = [c_int64]
    LamodGetNumPasses.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 284
for _lib in _libs.values():
    if not _lib.has("LamodGetRiseCulmSetTimes", "cdecl"):
        continue
    LamodGetRiseCulmSetTimes = _lib.get("LamodGetRiseCulmSetTimes", "cdecl")
    LamodGetRiseCulmSetTimes.argtypes = [c_int64, POINTER(c_double * int(3))]
    LamodGetRiseCulmSetTimes.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 295
for _lib in _libs.values():
    if not _lib.has("LamodComputeLookAngle", "cdecl"):
        continue
    LamodComputeLookAngle = _lib.get("LamodComputeLookAngle", "cdecl")
    LamodComputeLookAngle.argtypes = [c_int64, c_double, POINTER(c_int), c_double * int(6), c_double * int(9), c_double * int(9)]
    LamodComputeLookAngle.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 305
for _lib in _libs.values():
    if not _lib.has("LamodComputeLookView", "cdecl"):
        continue
    LamodComputeLookView = _lib.get("LamodComputeLookView", "cdecl")
    LamodComputeLookView.argtypes = [c_int64, c_double, c_double * int(128)]
    LamodComputeLookView.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 315
for _lib in _libs.values():
    if not _lib.has("LamodFindExactIOTime", "cdecl"):
        continue
    LamodFindExactIOTime = _lib.get("LamodFindExactIOTime", "cdecl")
    LamodFindExactIOTime.argtypes = [c_int64, c_double, c_double]
    LamodFindExactIOTime.restype = c_double
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 329
for _lib in _libs.values():
    if not _lib.has("LamodGetOrbSenViewdata", "cdecl"):
        continue
    LamodGetOrbSenViewdata = _lib.get("LamodGetOrbSenViewdata", "cdecl")
    LamodGetOrbSenViewdata.argtypes = [c_int64, c_double * int(3), c_double * int(3), c_double * int(5), POINTER(c_int), POINTER(c_int), c_double * int(4)]
    LamodGetOrbSenViewdata.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 391
for _lib in _libs.values():
    if not _lib.has("LamodGetViewDataField", "cdecl"):
        continue
    LamodGetViewDataField = _lib.get("LamodGetViewDataField", "cdecl")
    LamodGetViewDataField.argtypes = [c_int64, c_int, POINTER(c_double)]
    LamodGetViewDataField.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 405
for _lib in _libs.values():
    if not _lib.has("LamodCompRaDec", "cdecl"):
        continue
    LamodCompRaDec = _lib.get("LamodCompRaDec", "cdecl")
    LamodCompRaDec.argtypes = [c_double * int(3), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_double)]
    LamodCompRaDec.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 418
for _lib in _libs.values():
    if not _lib.has("LamodGenObs", "cdecl"):
        continue
    LamodGenObs = _lib.get("LamodGenObs", "cdecl")
    LamodGenObs.argtypes = [c_int64, c_int, c_char, c_char * int(512), c_char * int(512), POINTER(c_int)]
    LamodGenObs.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 431
for _lib in _libs.values():
    if not _lib.has("LamodGenObsAtTime", "cdecl"):
        continue
    LamodGenObsAtTime = _lib.get("LamodGenObsAtTime", "cdecl")
    LamodGenObsAtTime.argtypes = [c_int64, c_double, c_int, c_char, c_char * int(512), c_char * int(512), POINTER(c_int)]
    LamodGenObsAtTime.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 437
for _lib in _libs.values():
    if not _lib.has("LamodRemoveSenSat", "cdecl"):
        continue
    LamodRemoveSenSat = _lib.get("LamodRemoveSenSat", "cdecl")
    LamodRemoveSenSat.argtypes = [c_int64]
    LamodRemoveSenSat.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 442
for _lib in _libs.values():
    if not _lib.has("LamodRemoveAllSenSats", "cdecl"):
        continue
    LamodRemoveAllSenSats = _lib.get("LamodRemoveAllSenSats", "cdecl")
    LamodRemoveAllSenSats.argtypes = []
    LamodRemoveAllSenSats.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 447
for _lib in _libs.values():
    if not _lib.has("LamodReset", "cdecl"):
        continue
    LamodReset = _lib.get("LamodReset", "cdecl")
    LamodReset.argtypes = []
    LamodReset.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 458
for _lib in _libs.values():
    if not _lib.has("LamodSenSatDirect_OS", "cdecl"):
        continue
    LamodSenSatDirect_OS = _lib.get("LamodSenSatDirect_OS", "cdecl")
    LamodSenSatDirect_OS.argtypes = [c_double, c_double * int(16), c_double * int(6), c_double * int(128)]
    LamodSenSatDirect_OS.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 786
for _lib in _libs.values():
    if not _lib.has("LoadLamodDll", "cdecl"):
        continue
    LoadLamodDll = _lib.get("LoadLamodDll", "cdecl")
    LoadLamodDll.argtypes = []
    LoadLamodDll.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 787
for _lib in _libs.values():
    if not _lib.has("FreeLamodDll", "cdecl"):
        continue
    FreeLamodDll = _lib.get("FreeLamodDll", "cdecl")
    FreeLamodDll.argtypes = []
    FreeLamodDll.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 14
try:
    LamodDll = 'liblamod.so'
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 462
try:
    XF_SENSAT_STEPMODE = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 463
try:
    XF_SENSAT_OPTVISFLAG = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 464
try:
    XF_SENSAT_VISPASSONLY = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 465
try:
    XF_SENSAT_BEGDS50TAI = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 466
try:
    XF_SENSAT_ENDDS50TAI = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 467
try:
    XF_SENSAT_INTERVAL = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 468
try:
    XF_SENSAT_PERIOD = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 474
try:
    LOOK_VALID = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 475
try:
    LOOK_HTEST = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 476
try:
    LOOK_SENLIMS = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 482
try:
    XA_LOOK_DS50UTC = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 483
try:
    XA_LOOK_MSE = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 484
try:
    XA_LOOK_ELEV = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 485
try:
    XA_LOOK_AZIM = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 486
try:
    XA_LOOK_RNG = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 487
try:
    XA_LOOK_RNGRT = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 488
try:
    XA_LOOK_SIZE = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 494
try:
    XF_VIEW_UVEC = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 495
try:
    XF_VIEW_RUVEC = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 496
try:
    XF_VIEW_LVEC = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 497
try:
    XF_VIEW_ZVEC = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 498
try:
    XF_VIEW_RNGVEC = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 499
try:
    XF_VIEW_RRTVEC = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 500
try:
    XF_VIEW_SUNVEC = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 501
try:
    XF_VIEW_MOONVEC = 8
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 502
try:
    XF_VIEW_ANGARR = 9
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 503
try:
    XF_VIEW_CVIS = 10
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 504
try:
    XF_VIEW_RELVEL = 11
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 505
try:
    XF_VIEW_SENEFG = 12
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 506
try:
    XF_VIEW_LIMFLGS = 13
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 507
try:
    XF_VIEW_AZELRATES = 14
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 508
try:
    XF_VIEW_MOONANGLES = 15
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 515
try:
    XA_ANGLE_MOONSENSAT = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 516
try:
    XA_ANGLE_SUNEARTHSAT = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 517
try:
    XA_ANGLE_SUNEARTHSEN = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 518
try:
    XA_ANGLE_SUNSENSAT = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 519
try:
    XA_ANGLE_SOLARASPECT = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 520
try:
    XA_ANGLE_SIZE = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 525
try:
    XA_ANGLE_MOONEARTHSAT = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 526
try:
    XA_ANGLE_MOONEARTHSEN = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 533
try:
    XA_OFFBORE_EL1 = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 534
try:
    XA_OFFBORE_AZ1 = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 535
try:
    XA_OFFBORE_EL2 = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 536
try:
    XA_OFFBORE_AZ2 = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 537
try:
    XA_OFFBORE_SIZE = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 543
try:
    XF_1P_TIMEFRM = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 544
try:
    XF_1P_BEGTIME = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 545
try:
    XF_1P_ENDTIME = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 546
try:
    XF_1P_INTERVAL = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 547
try:
    XF_1P_PRTOPT = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 548
try:
    XF_1P_GENOBS = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 549
try:
    XF_1P_VISFLG = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 550
try:
    XF_1P_STEPMODE = 8
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 551
try:
    XF_1P_PROCMODE = 9
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 552
try:
    XF_1P_DIAGNOST = 10
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 553
try:
    XF_1P_MAXSAA = 11
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 559
try:
    XA_LIMFLG_AZLIM = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 560
try:
    XA_LIMFLG_ELLIM = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 561
try:
    XA_LIMFLG_EARTHBK = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 562
try:
    XA_LIMFLG_EARTHOB = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 563
try:
    XA_LIMFLG_LUNEXCL = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 564
try:
    XA_LIMFLG_MAXRANGE = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 565
try:
    XA_LIMFLG_MINRANGE = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 566
try:
    XA_LIMFLG_PENECLIP = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 567
try:
    XA_LIMFLG_RVELLIM = 8
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 568
try:
    XA_LIMFLG_SAALIM = 9
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 569
try:
    XA_LIMFLG_SOLEXCL = 10
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 570
try:
    XA_LIMFLG_UMBECLIP = 11
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 571
try:
    XA_LIMFLG_SIZE = 12
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 576
try:
    GENOBS_NONE = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 577
try:
    GENOBS_B3 = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 578
try:
    GENOBS_TTY = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 579
try:
    GENOBS_SPTASKER = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 580
try:
    GENOBS_CSV = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 585
try:
    XA_LV_LOOKCODE = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 586
try:
    XA_LV_DS50UTC = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 587
try:
    XA_LV_MSE = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 588
try:
    XA_LV_ELEV = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 589
try:
    XA_LV_AZIM = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 590
try:
    XA_LV_RNG = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 591
try:
    XA_LV_RNGRT = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 592
try:
    XA_LV_RA = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 593
try:
    XA_LV_DEC = 8
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 594
try:
    XA_LV_AZRATE = 9
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 595
try:
    XA_LV_ELRATE = 10
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 597
try:
    XA_LV_SENPOSX = 11
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 598
try:
    XA_LV_SENPOSY = 12
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 599
try:
    XA_LV_SENPOSZ = 13
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 600
try:
    XA_LV_SENVELX = 14
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 601
try:
    XA_LV_SENVELY = 15
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 602
try:
    XA_LV_SENVELZ = 16
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 603
try:
    XA_LV_SENLAT = 17
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 604
try:
    XA_LV_SENLON = 18
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 605
try:
    XA_LV_SENHEIGHT = 19
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 607
try:
    XA_LV_SATPOSX = 20
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 608
try:
    XA_LV_SATPOSY = 21
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 609
try:
    XA_LV_SATPOSZ = 22
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 610
try:
    XA_LV_SATVELX = 23
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 611
try:
    XA_LV_SATVELY = 24
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 612
try:
    XA_LV_SATVELZ = 25
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 613
try:
    XA_LV_SATLAT = 26
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 614
try:
    XA_LV_SATLON = 27
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 615
try:
    XA_LV_SATHEIGHT = 28
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 617
try:
    XA_LV_UVECX = 31
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 618
try:
    XA_LV_UVECY = 32
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 619
try:
    XA_LV_UVECZ = 33
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 620
try:
    XA_LV_RUVECX = 34
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 621
try:
    XA_LV_RUVECY = 35
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 622
try:
    XA_LV_RUVECZ = 36
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 623
try:
    XA_LV_LVECX = 37
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 624
try:
    XA_LV_LVECY = 38
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 625
try:
    XA_LV_LVECZ = 39
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 626
try:
    XA_LV_ZVECX = 40
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 627
try:
    XA_LV_ZVECY = 41
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 628
try:
    XA_LV_ZVECZ = 42
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 629
try:
    XA_LV_RNGVECX = 43
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 630
try:
    XA_LV_RNGVECY = 44
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 631
try:
    XA_LV_RNGVECZ = 45
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 632
try:
    XA_LV_RRTVECX = 46
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 633
try:
    XA_LV_RRTVECY = 47
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 634
try:
    XA_LV_RRTVECZ = 48
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 635
try:
    XA_LV_USUNX = 49
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 636
try:
    XA_LV_USUNY = 50
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 637
try:
    XA_LV_USUNZ = 51
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 638
try:
    XA_LV_UMOONX = 52
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 639
try:
    XA_LV_UMOONY = 53
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 640
try:
    XA_LV_UMOONZ = 54
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 641
try:
    XA_LV_MOSESA = 55
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 642
try:
    XA_LV_MOEASA = 56
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 643
try:
    XA_LV_MOEASE = 57
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 644
try:
    XA_LV_SUSESA = 58
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 645
try:
    XA_LV_SUEASA = 59
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 646
try:
    XA_LV_SUEASE = 60
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 647
try:
    XA_LV_SOLAA = 61
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 648
try:
    XA_LV_VIS = 62
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 649
try:
    XA_LV_RELVEL = 63
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 650
try:
    XA_LV_OBSANGLE = 64
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 651
try:
    XA_LV_ANG2FAN = 65
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 653
try:
    XA_LV_AZLIM = 70
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 654
try:
    XA_LV_ELLIM = 71
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 655
try:
    XA_LV_EARTHBK = 72
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 656
try:
    XA_LV_EARTHOB = 73
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 657
try:
    XA_LV_LUNEXCL = 74
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 658
try:
    XA_LV_MAXRANGE = 75
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 659
try:
    XA_LV_MINRANGE = 76
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 660
try:
    XA_LV_PENECLIP = 77
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 661
try:
    XA_LV_RVELLIM = 78
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 662
try:
    XA_LV_SAALIM = 79
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 663
try:
    XA_LV_SOLEXCL = 80
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 664
try:
    XA_LV_UMBECLIP = 81
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 665
try:
    XA_LV_OPTVIS = 82
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 667
try:
    XA_LV_SENPOSE = 90
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 668
try:
    XA_LV_SENPOSF = 91
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 669
try:
    XA_LV_SENPOSG = 92
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 670
try:
    XA_LV_NBORE1 = 93
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 671
try:
    XA_LV_NBORE2 = 94
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 672
try:
    XA_LV_OBEL1 = 95
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 673
try:
    XA_LV_OBAZ1 = 96
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 674
try:
    XA_LV_OBAZ2 = 97
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 675
try:
    XA_LV_OBEL2 = 98
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 677
try:
    XA_LV_SIZE = 128
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 682
try:
    XA_SENSAT_SENNUM = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 683
try:
    XA_SENSAT_SATNUM = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 684
try:
    XA_SENSAT_VIEWTYPE = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 685
try:
    XA_SENSAT_OBSTYPE = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 686
try:
    XA_SENSAT_PTSPERPAS = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 687
try:
    XA_SENSAT_STEPMODE = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 688
try:
    XA_SENSAT_OPTVISFLAG = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 689
try:
    XA_SENSAT_VISPASSONLY = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 690
try:
    XA_SENSAT_STARTAI = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 691
try:
    XA_SENSAT_STOPTAI = 8
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 692
try:
    XA_SENSAT_INTERVAL = 9
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 693
try:
    XA_SENSAT_PERIOD = 10
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 694
try:
    XA_SENSAT_SENKEY = 11
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 696
try:
    XA_SENSAT_SIZE = 32
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 701
try:
    XA_LA_PARMS_TIMEFLG = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 702
try:
    XA_LA_PARMS_STARTTIME = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 703
try:
    XA_LA_PARMS_STOPTIME = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 704
try:
    XA_LA_PARMS_STEPMODE = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 705
try:
    XA_LA_PARMS_VISFLG = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 706
try:
    XA_LA_PARMS_XMSAA = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 708
try:
    XA_LA_PARMS_SIZE = 16
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 712
try:
    SENLOC_TYPE_ECI = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 716
try:
    XA_LOCSEN_LOCTYPE = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 717
try:
    XA_LOCSEN_POS1 = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 718
try:
    XA_LOCSEN_POS2 = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 719
try:
    XA_LOCSEN_POS3 = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 722
try:
    XA_LOCSEN_ASTROLAT = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 723
try:
    XA_LOCSEN_ASTROLON = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 726
try:
    XA_LOCSEN_VEL1 = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 727
try:
    XA_LOCSEN_VEL2 = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 728
try:
    XA_LOCSEN_VEL3 = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 730
try:
    XA_LOCSEN_SIZE = 16
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 735
try:
    XA_PVSAT_POSX = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 736
try:
    XA_PVSAT_POSY = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 737
try:
    XA_PVSAT_POSZ = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 738
try:
    XA_PVSAT_VELX = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 739
try:
    XA_PVSAT_VELY = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 740
try:
    XA_PVSAT_VELZ = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_LamodDll.h: 742
try:
    XA_PVSAT_SIZE = 6
except:
    pass

# No inserted files

# No prefix-stripping

