r"""Wrapper for new_BatchDCDll.h

Generated with:
/home/woodkn1/DND/bin/ctypesgen -I . ./new_BatchDCDll.h -o ./BatchDCDll.py

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

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 22
for _lib in _libs.values():
    if not _lib.has("BatchDCInit", "cdecl"):
        continue
    BatchDCInit = _lib.get("BatchDCInit", "cdecl")
    BatchDCInit.argtypes = [c_int64]
    BatchDCInit.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 28
for _lib in _libs.values():
    if not _lib.has("BatchDCGetInfo", "cdecl"):
        continue
    BatchDCGetInfo = _lib.get("BatchDCGetInfo", "cdecl")
    BatchDCGetInfo.argtypes = [c_char * int(128)]
    BatchDCGetInfo.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 34
for _lib in _libs.values():
    if not _lib.has("BatchDCLoadFile", "cdecl"):
        continue
    BatchDCLoadFile = _lib.get("BatchDCLoadFile", "cdecl")
    BatchDCLoadFile.argtypes = [c_char * int(512)]
    BatchDCLoadFile.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 40
for _lib in _libs.values():
    if not _lib.has("BatchDCLoadFileAll", "cdecl"):
        continue
    BatchDCLoadFileAll = _lib.get("BatchDCLoadFileAll", "cdecl")
    BatchDCLoadFileAll.argtypes = [c_char * int(512)]
    BatchDCLoadFileAll.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 46
for _lib in _libs.values():
    if not _lib.has("BatchDCLoadCard", "cdecl"):
        continue
    BatchDCLoadCard = _lib.get("BatchDCLoadCard", "cdecl")
    BatchDCLoadCard.argtypes = [c_char * int(512)]
    BatchDCLoadCard.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 51
for _lib in _libs.values():
    if not _lib.has("BatchDCGetPCard", "cdecl"):
        continue
    BatchDCGetPCard = _lib.get("BatchDCGetPCard", "cdecl")
    BatchDCGetPCard.argtypes = [c_char * int(512)]
    BatchDCGetPCard.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 59
for _lib in _libs.values():
    if not _lib.has("BatchDCSaveFile", "cdecl"):
        continue
    BatchDCSaveFile = _lib.get("BatchDCSaveFile", "cdecl")
    BatchDCSaveFile.argtypes = [c_char * int(512), c_int, c_int]
    BatchDCSaveFile.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 115
for _lib in _libs.values():
    if not _lib.has("BatchDCGetParams", "cdecl"):
        continue
    BatchDCGetParams = _lib.get("BatchDCGetParams", "cdecl")
    BatchDCGetParams.argtypes = [c_int * int(256), c_double * int(256), c_char * int(512)]
    BatchDCGetParams.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 123
for _lib in _libs.values():
    if not _lib.has("BatchDCSetParams", "cdecl"):
        continue
    BatchDCSetParams = _lib.get("BatchDCSetParams", "cdecl")
    BatchDCSetParams.argtypes = [c_int * int(256), c_double * int(256), c_char * int(512)]
    BatchDCSetParams.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 128
for _lib in _libs.values():
    if not _lib.has("BatchDCGetCtrlArr", "cdecl"):
        continue
    BatchDCGetCtrlArr = _lib.get("BatchDCGetCtrlArr", "cdecl")
    BatchDCGetCtrlArr.argtypes = [c_double * int(64)]
    BatchDCGetCtrlArr.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 134
for _lib in _libs.values():
    if not _lib.has("BatchDCSetCtrlArr", "cdecl"):
        continue
    BatchDCSetCtrlArr = _lib.get("BatchDCSetCtrlArr", "cdecl")
    BatchDCSetCtrlArr.argtypes = [c_double * int(64)]
    BatchDCSetCtrlArr.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 146
for _lib in _libs.values():
    if not _lib.has("BatchDCInitSat", "cdecl"):
        continue
    BatchDCInitSat = _lib.get("BatchDCInitSat", "cdecl")
    BatchDCInitSat.argtypes = [c_int64, POINTER(c_int), POINTER(c_int64), c_int * int(256), c_double * int(256), c_char * int(512)]
    BatchDCInitSat.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 159
for _lib in _libs.values():
    if not _lib.has("BatchDCInitSatObsKeys", "cdecl"):
        continue
    BatchDCInitSatObsKeys = _lib.get("BatchDCInitSatObsKeys", "cdecl")
    BatchDCInitSatObsKeys.argtypes = [c_int64, c_double * int(64), c_int, POINTER(c_int64), c_int * int(256), c_double * int(256), c_char * int(512)]
    BatchDCInitSatObsKeys.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 174
for _lib in _libs.values():
    if not _lib.has("BatchDCInitSatObsSel", "cdecl"):
        continue
    BatchDCInitSatObsSel = _lib.get("BatchDCInitSatObsSel", "cdecl")
    BatchDCInitSatObsSel.argtypes = [c_int64, c_double * int(64), c_double * int(128), POINTER(c_int), POINTER(c_int64), c_int * int(256), c_double * int(256), c_char * int(512)]
    BatchDCInitSatObsSel.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 241
for _lib in _libs.values():
    if not _lib.has("BatchDCSolve", "cdecl"):
        continue
    BatchDCSolve = _lib.get("BatchDCSolve", "cdecl")
    BatchDCSolve.argtypes = [c_int64, c_int * int(256), c_double * int(256), c_char * int(512)]
    BatchDCSolve.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 256
for _lib in _libs.values():
    if not _lib.has("BatchDCSolveSelObs", "cdecl"):
        continue
    BatchDCSolveSelObs = _lib.get("BatchDCSolveSelObs", "cdecl")
    BatchDCSolveSelObs.argtypes = [c_int64, POINTER(c_int64), c_int, c_int * int(256), c_double * int(256), c_char * int(512)]
    BatchDCSolveSelObs.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 262
for _lib in _libs.values():
    if not _lib.has("BatchDCRemoveSat", "cdecl"):
        continue
    BatchDCRemoveSat = _lib.get("BatchDCRemoveSat", "cdecl")
    BatchDCRemoveSat.argtypes = [c_int64]
    BatchDCRemoveSat.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 320
for _lib in _libs.values():
    if not _lib.has("BatchDCIterate", "cdecl"):
        continue
    BatchDCIterate = _lib.get("BatchDCIterate", "cdecl")
    BatchDCIterate.argtypes = [c_int64, POINTER(c_double * int(100)), POINTER(c_int * int(32)), c_int * int(256), c_double * int(256), c_char * int(512)]
    BatchDCIterate.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 327
for _lib in _libs.values():
    if not _lib.has("BatchDCGetVcm", "cdecl"):
        continue
    BatchDCGetVcm = _lib.get("BatchDCGetVcm", "cdecl")
    BatchDCGetVcm.argtypes = [c_int64, c_char * int(4000)]
    BatchDCGetVcm.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 333
for _lib in _libs.values():
    if not _lib.has("BatchDCGetSpVOut", "cdecl"):
        continue
    BatchDCGetSpVOut = _lib.get("BatchDCGetSpVOut", "cdecl")
    BatchDCGetSpVOut.argtypes = [c_char * int(512)]
    BatchDCGetSpVOut.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 338
for _lib in _libs.values():
    if not _lib.has("BatchDCSetSpVOut", "cdecl"):
        continue
    BatchDCSetSpVOut = _lib.get("BatchDCSetSpVOut", "cdecl")
    BatchDCSetSpVOut.argtypes = [c_char * int(512)]
    BatchDCSetSpVOut.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 342
for _lib in _libs.values():
    if not _lib.has("BatchDCResetAll", "cdecl"):
        continue
    BatchDCResetAll = _lib.get("BatchDCResetAll", "cdecl")
    BatchDCResetAll.argtypes = []
    BatchDCResetAll.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 349
for _lib in _libs.values():
    if not _lib.has("BatchDCGetAccptCrit", "cdecl"):
        continue
    BatchDCGetAccptCrit = _lib.get("BatchDCGetAccptCrit", "cdecl")
    BatchDCGetAccptCrit.argtypes = [c_int64, c_double * int(64)]
    BatchDCGetAccptCrit.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 361
for _lib in _libs.values():
    if not _lib.has("SpToEGP", "cdecl"):
        continue
    SpToEGP = _lib.get("SpToEGP", "cdecl")
    SpToEGP.argtypes = [c_int64, c_double * int(64), c_int * int(256), c_double * int(256), c_char * int(512)]
    SpToEGP.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 372
for _lib in _libs.values():
    if not _lib.has("SpToTle", "cdecl"):
        continue
    SpToTle = _lib.get("SpToTle", "cdecl")
    SpToTle.argtypes = [c_int64, c_double * int(64), c_char * int(512), c_char * int(512)]
    SpToTle.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 385
for _lib in _libs.values():
    if not _lib.has("SpToTleComb", "cdecl"):
        continue
    SpToTleComb = _lib.get("SpToTleComb", "cdecl")
    SpToTleComb.argtypes = [c_int64, c_double * int(64), c_char * int(512), c_char * int(512), c_int * int(256), c_double * int(256), c_char * int(512)]
    SpToTleComb.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 395
for _lib in _libs.values():
    if not _lib.has("SpToCsv", "cdecl"):
        continue
    SpToCsv = _lib.get("SpToCsv", "cdecl")
    SpToCsv.argtypes = [c_int64, c_double * int(64), c_char * int(512)]
    SpToCsv.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 407
for _lib in _libs.values():
    if not _lib.has("SpToCsvComb", "cdecl"):
        continue
    SpToCsvComb = _lib.get("SpToCsvComb", "cdecl")
    SpToCsvComb.argtypes = [c_int64, c_double * int(64), c_char * int(512), c_int * int(256), c_double * int(256), c_char * int(512)]
    SpToCsvComb.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 418
for _lib in _libs.values():
    if not _lib.has("ExtEphemToEGP", "cdecl"):
        continue
    ExtEphemToEGP = _lib.get("ExtEphemToEGP", "cdecl")
    ExtEphemToEGP.argtypes = [c_char * int(512), c_double * int(64), c_int * int(256), c_double * int(256), c_char * int(512)]
    ExtEphemToEGP.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 429
for _lib in _libs.values():
    if not _lib.has("IomodDC", "cdecl"):
        continue
    IomodDC = _lib.get("IomodDC", "cdecl")
    IomodDC.argtypes = [c_int, POINTER(c_int64), c_double * int(64), c_int * int(256), c_double * int(256), c_char * int(512)]
    IomodDC.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 820
for _lib in _libs.values():
    if not _lib.has("LoadBatchDCDll", "cdecl"):
        continue
    LoadBatchDCDll = _lib.get("LoadBatchDCDll", "cdecl")
    LoadBatchDCDll.argtypes = []
    LoadBatchDCDll.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 821
for _lib in _libs.values():
    if not _lib.has("FreeBatchDCDll", "cdecl"):
        continue
    FreeBatchDCDll = _lib.get("FreeBatchDCDll", "cdecl")
    FreeBatchDCDll.argtypes = []
    FreeBatchDCDll.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 14
try:
    BatchDCDll = 'libbatchdc.so'
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 432
try:
    DCPROPTYPE_GP = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 433
try:
    DCPROPTYPE_PPT3 = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 434
try:
    DCPROPTYPE_XP = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 435
try:
    DCPROPTYPE_SP = 99
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 439
try:
    ITERCODE_DONE = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 440
try:
    ITERCODE_ERROR = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 441
try:
    ITERCODE_ITERATING = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 442
try:
    ITERCODE_DIVERGED = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 446
try:
    EPFLG_NODALXINGLATESTOB = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 447
try:
    EPFLG_LATESTOB = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 448
try:
    EPFLG_NODALXINGATTIME = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 449
try:
    EPFLG_ATEPOCH = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 450
try:
    EPFLG_ATSPECIFIEDTIME = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 451
try:
    EPFLG_MIDDLEOBSSPAN = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 452
try:
    EPFLG_EARLIESTOB = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 453
try:
    EPFLG_BEGINDAYEPOCH = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 454
try:
    EPFLG_BEGINDAYLATESTOB = 8
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 455
try:
    EPFLG_NODALXINGEPOCH = 9
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 459
try:
    CORT_TIME = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 460
try:
    CORT_PLANE = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 461
try:
    CORT_7ELT = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 462
try:
    CORT_INTRK = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 463
try:
    CORT_8ELT = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 464
try:
    CORT_SUBELT = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 468
try:
    CORORD_7ELT = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 469
try:
    CORORD_TIM7ELT = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 470
try:
    CORORD_TIMPLN7ELT = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 471
try:
    CORORD_PLNTIM7ELT = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 472
try:
    CORORD_PLN7ELT = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 473
try:
    CORORD_N7ELT = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 474
try:
    CORORD_L7ELT = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 475
try:
    CORORD_LN7ELT = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 476
try:
    CORORD_AFAGLN7ELT = 8
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 477
try:
    CORORD_6ELT7ELT = 9
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 482
try:
    XA_EGPCTRL_OPTION = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 483
try:
    XA_EGPCTRL_DCELTTYPE = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 484
try:
    XA_EGPCTRL_STARTMSE = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 485
try:
    XA_EGPCTRL_STOPMSE = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 486
try:
    XA_EGPCTRL_STEPMIN = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 487
try:
    XA_EGPCTRL_DRAGCOR = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 488
try:
    XA_EGPCTRL_NDOTCOR = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 489
try:
    XA_EGPCTRL_AGOMCOR = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 490
try:
    XA_EGPCTRL_EPFLG = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 491
try:
    XA_EGPCTRL_NEWEPOCH = 8
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 493
try:
    XA_EGPCTRL_BVAL = 9
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 494
try:
    XA_EGPCTRL_AGOMVAL = 10
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 496
try:
    XA_EGPCTRL_ORDERCOR = 11
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 497
try:
    XA_EGPCTRL_MAXOFITERS = 12
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 501
try:
    XA_EGPCTRL_SATNUM = 63
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 503
try:
    XA_EGPCTRL_SIZE = 64
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 509
try:
    MAX_PARAMS = 256
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 514
try:
    DC_PRINT_FIRSTBEST = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 515
try:
    DC_PRINT_ALLPASS = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 516
try:
    DC_PRINT_SUMONLY = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 517
try:
    DC_PRINT_ELTONLY = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 518
try:
    DC_PRINT_NONE = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 522
try:
    ITER_SUM_KEP = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 523
try:
    ITER_SUM_EQNX = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 527
try:
    XAI_CTRL_PRINTOPTION = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 528
try:
    XAI_CTRL_DEBIASOBS = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 529
try:
    XAI_CTRL_WEIGHTEDDC = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 530
try:
    XAI_CTRL_EPOCHOPTION = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 531
try:
    XAI_CTRL_CORRECT_AG = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 532
try:
    XAI_CTRL_CORRECT_AF = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 533
try:
    XAI_CTRL_CORRECT_PSI = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 534
try:
    XAI_CTRL_CORRECT_CHI = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 535
try:
    XAI_CTRL_CORRECT_L = 8
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 536
try:
    XAI_CTRL_CORRECT_N = 9
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 537
try:
    XAI_CTRL_CORRECT_B = 10
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 538
try:
    XAI_CTRL_CORRECT_AGOM = 11
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 539
try:
    XAI_CTRL_CORRECTORDER = 12
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 540
try:
    XAI_CTRL_FOR1ITERONLY = 13
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 541
try:
    XAI_CTRL_RESIDSELECT = 14
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 542
try:
    XAI_CTRL_SENPERFORM = 15
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 543
try:
    XAI_CTRL_DWOBSPERTRCK = 16
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 544
try:
    XAI_CTRL_ITERSUMOPT = 17
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 545
try:
    XAI_CTRL_PARTIALMETH = 18
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 546
try:
    XAI_CTRL_LTC = 19
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 547
try:
    XAI_CTRL_BRUCE = 20
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 548
try:
    XAI_CTRL_PROPMETHOD = 21
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 549
try:
    XAI_CTRL_CORRECTBVSX = 22
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 550
try:
    XAI_CTRL_MAXOFITERS = 23
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 551
try:
    XAI_CTRL_USEPREDRMS = 24
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 552
try:
    XAI_CTRL_RESCOMPMETH = 25
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 553
try:
    XAI_CTRL_USEANGRATES = 26
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 555
try:
    XAI_CTRL_SIZE = 256
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 561
try:
    XAR_CTRL_RMSMULT = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 562
try:
    XAR_CTRL_USEREPOCH = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 563
try:
    XAR_CTRL_CNVCRITONT = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 564
try:
    XAR_CTRL_1STPASDELTAT = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 565
try:
    XAR_CTRL_CNVCRITON7ELT = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 566
try:
    XAR_CTRL_BRESET = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 567
try:
    XAR_CTRL_SIZE = 256
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 572
try:
    XAI_DCELTS_SATNUM = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 573
try:
    XAI_DCELTS_ELSETNUM = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 574
try:
    XAI_DCELTS_ORBTYPE = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 575
try:
    XAI_DCELTS_PROPTYPE = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 576
try:
    XAI_DCELTS_SPECTR = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 577
try:
    XAI_DCELTS_REVNUM = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 578
try:
    XAI_DCELTS_CORRTYPE = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 580
try:
    XAI_DCELTS_ITERCOUNT = 10
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 581
try:
    XAI_DCELTS_SUBITER = 11
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 582
try:
    XAI_DCELTS_RESACC = 12
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 583
try:
    XAI_DCELTS_RESREJ = 13
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 585
try:
    XAI_DCELTS_CORRFLGS = 20
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 587
try:
    XAI_DCELTS_SIZE = 256
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 591
try:
    XAR_DCELTS_EPOCHDS50UTC = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 592
try:
    XAR_DCELTS_NDOT = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 593
try:
    XAR_DCELTS_N2DOT = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 594
try:
    XAR_DCELTS_BFIELD = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 595
try:
    XAR_DCELTS_AGOM = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 596
try:
    XAR_DCELTS_OGPARM = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 597
try:
    XAR_DCELTS_KEP_A = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 598
try:
    XAR_DCELTS_KEP_E = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 599
try:
    XAR_DCELTS_KEP_INCLI = 8
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 600
try:
    XAR_DCELTS_KEP_MA = 9
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 601
try:
    XAR_DCELTS_KEP_NODE = 10
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 602
try:
    XAR_DCELTS_KEP_OMEGA = 11
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 603
try:
    XAR_DCELTS_EQNX_AF = 12
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 604
try:
    XAR_DCELTS_EQNX_AG = 13
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 605
try:
    XAR_DCELTS_EQNX_CHI = 14
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 606
try:
    XAR_DCELTS_EQNX_PSI = 15
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 607
try:
    XAR_DCELTS_EQNX_L = 16
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 608
try:
    XAR_DCELTS_EQNX_N = 17
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 609
try:
    XAR_DCELTS_POSX = 18
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 610
try:
    XAR_DCELTS_POSY = 19
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 611
try:
    XAR_DCELTS_POSZ = 20
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 612
try:
    XAR_DCELTS_VELX = 21
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 613
try:
    XAR_DCELTS_VELY = 22
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 614
try:
    XAR_DCELTS_VELZ = 23
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 616
try:
    XAR_DCELTS_RMS = 40
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 617
try:
    XAR_DCELTS_RMSUNWTD = 41
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 618
try:
    XAR_DCELTS_DELTATRMS = 42
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 619
try:
    XAR_DCELTS_BETARMS = 43
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 620
try:
    XAR_DCELTS_DELTAHTRMS = 44
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 621
try:
    XAR_DCELTS_CONVQLTY = 45
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 622
try:
    XAR_DCELTS_RMSPD = 46
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 624
try:
    XAR_DCELTS_COVL = 60
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 625
try:
    XAR_DCELTS_COVN = 61
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 626
try:
    XAR_DCELTS_COVCHI = 62
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 627
try:
    XAR_DCELTS_COVPSI = 63
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 628
try:
    XAR_DCELTS_COVAF = 64
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 629
try:
    XAR_DCELTS_COVAG = 65
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 630
try:
    XAR_DCELTS_COVBTERM = 66
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 631
try:
    XAR_DCELTS_COVNA = 67
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 632
try:
    XAR_DCELTS_COVAGOM = 68
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 634
try:
    XAR_DCELTS_XMAX = 70
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 635
try:
    XAR_DCELTS_XMAX2 = 71
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 636
try:
    XAR_DCELTS_XMAX3 = 72
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 637
try:
    XAR_DCELTS_XMAX4 = 73
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 638
try:
    XAR_DCELTS_PATCL = 74
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 639
try:
    XAR_DCELTS_PATCH = 75
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 641
try:
    XAR_DCELTS_EQNXCOVMTX = 200
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 643
try:
    XAR_DCELTS_SIZE = 256
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 647
try:
    XA_REJFLG_DECAYED = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 648
try:
    XA_REJFLG_ERROR = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 649
try:
    XA_REJFLG_RA = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 650
try:
    XA_REJFLG_BETA = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 651
try:
    XA_REJFLG_DEC = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 652
try:
    XA_REJFLG_HEIGHT = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 653
try:
    XA_REJFLG_RANGE = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 654
try:
    XA_REJFLG_RR = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 655
try:
    XA_REJFLG_TIME = 8
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 657
try:
    XA_REJFLG_SIZE = 32
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 661
try:
    XA_AC_STD_EPOCH = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 662
try:
    XA_AC_STD_NORES = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 663
try:
    XA_AC_STD_PRCNTRES = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 664
try:
    XA_AC_STD_RMS = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 665
try:
    XA_AC_STD_OBSSPAN = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 666
try:
    XA_AC_STD_DELTAW = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 667
try:
    XA_AC_STD_DELTAABAR = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 668
try:
    XA_AC_STD_DELTAN = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 669
try:
    XA_AC_STD_DELTAB = 8
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 671
try:
    XA_AC_ACT_EPOCH = 20
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 672
try:
    XA_AC_ACT_NORES = 21
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 673
try:
    XA_AC_ACT_PRCNTRES = 22
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 674
try:
    XA_AC_ACT_RMS = 23
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 675
try:
    XA_AC_ACT_OBSSPAN = 24
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 676
try:
    XA_AC_ACT_DELTAW = 25
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 677
try:
    XA_AC_ACT_DELTAABAR = 26
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 678
try:
    XA_AC_ACT_DELTAN = 27
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 679
try:
    XA_AC_ACT_DELTAB = 28
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 681
try:
    XA_AC_SIZE = 64
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 686
try:
    XAS_DCELTS_SATNAME_0TO7 = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 688
try:
    XAS_DCELTS_SIZE = 512
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 692
try:
    DCCTRL_MODE_GLOBAL = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 693
try:
    DCCTRL_MODE_LOCAL = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 698
try:
    XA_DCCTRL_MODE = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 699
try:
    XA_DCCTRL_PROPMETHOD = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 700
try:
    XA_DCCTRL_DEBIASOBS = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 701
try:
    XA_DCCTRL_CORRECTORDER = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 702
try:
    XA_DCCTRL_EPOCHOPTION = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 703
try:
    XA_DCCTRL_USEPREDRMS = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 704
try:
    XA_DCCTRL_RESIDSELECT = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 705
try:
    XA_DCCTRL_FOR1ITERONLY = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 706
try:
    XA_DCCTRL_MAXOFITERS = 8
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 707
try:
    XA_DCCTRL_WEIGHTEDDC = 9
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 708
try:
    XA_DCCTRL_LTC = 10
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 709
try:
    XA_DCCTRL_BRUCE = 11
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 710
try:
    XA_DCCTRL_DWOBSPERTRCK = 12
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 711
try:
    XA_DCCTRL_PARTIALMETH = 13
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 712
try:
    XA_DCCTRL_CORRECT_AG = 20
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 713
try:
    XA_DCCTRL_CORRECT_AF = 21
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 714
try:
    XA_DCCTRL_CORRECT_PSI = 22
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 715
try:
    XA_DCCTRL_CORRECT_CHI = 23
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 716
try:
    XA_DCCTRL_CORRECT_L = 24
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 717
try:
    XA_DCCTRL_CORRECT_N = 25
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 718
try:
    XA_DCCTRL_CORRECT_B = 26
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 719
try:
    XA_DCCTRL_CORRECT_AGOM = 27
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 720
try:
    XA_DCCTRL_CNVCRITONT = 30
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 721
try:
    XA_DCCTRL_1STPASDELTAT = 31
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 722
try:
    XA_DCCTRL_CNVCRITON7ELT = 32
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 723
try:
    XA_DCCTRL_RMSMULT = 33
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 724
try:
    XA_DCCTRL_BRESET = 34
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 725
try:
    XA_DCCTRL_USEREPOCH = 35
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 726
try:
    XA_DCCTRL_CONSIDER = 40
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 727
try:
    XA_DCCTRL_GPRCM = 40
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 728
try:
    XA_DCCTRL_CORRECTBVSX = 41
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 730
try:
    XA_DCCTRL_SIZE = 64
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 734
try:
    XA_IOMDC_MODE = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 735
try:
    XA_IOMDC_DCELTTYPE = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 736
try:
    XA_IOMDC_EPFLG = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 737
try:
    XA_IOMDC_NEWEPOCH = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 738
try:
    XA_IOMDC_ORDERCOR = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 739
try:
    XA_IOMDC_OBSSELMODE = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 740
try:
    XA_IOMDC_RESIDSELECT = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 741
try:
    XA_IOMDC_FOR1ITERONLY = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 742
try:
    XA_IOMDC_MAXOFITERS = 8
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 743
try:
    XA_IOMDC_WEIGHTEDDC = 9
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 744
try:
    XA_IOMDC_LTC = 10
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 745
try:
    XA_IOMDC_BRUCE = 11
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 746
try:
    XA_IOMDC_DWOBSPERTRCK = 12
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 747
try:
    XA_IOMDC_PARTIALMETH = 13
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 748
try:
    XA_IOMDC_DEBIASOBS = 14
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 749
try:
    XA_IOMDC_USEPREDRMS = 15
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 751
try:
    XA_IOMDC_CORRECT_AG = 20
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 752
try:
    XA_IOMDC_CORRECT_AF = 21
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 753
try:
    XA_IOMDC_CORRECT_PSI = 22
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 754
try:
    XA_IOMDC_CORRECT_CHI = 23
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 755
try:
    XA_IOMDC_CORRECT_L = 24
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 756
try:
    XA_IOMDC_CORRECT_N = 25
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 757
try:
    XA_IOMDC_CORRECT_B = 26
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 758
try:
    XA_IOMDC_CORRECT_AGOM = 27
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 759
try:
    XA_IOMDC_CNVCRITONT = 30
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 760
try:
    XA_IOMDC_1STPASDELTAT = 31
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 761
try:
    XA_IOMDC_CNVCRITON7ELT = 32
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 762
try:
    XA_IOMDC_RMSMULT = 33
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 763
try:
    XA_IOMDC_BRESET = 34
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 764
try:
    XA_IOMDC_CONSIDER = 40
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 765
try:
    XA_IOMDC_GPRCM = 40
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 766
try:
    XA_IOMDC_CORRECTBVSX = 41
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 768
try:
    XA_IOMDC_METHOD = 50
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 770
try:
    XA_IOMDC_NHREV = 51
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 771
try:
    XA_IOMDC_IND = 52
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 772
try:
    XA_IOMDC_MAXIT = 53
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 773
try:
    XA_IOMDC_RNG1 = 54
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 774
try:
    XA_IOMDC_RNG3 = 55
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 775
try:
    XA_IOMDC_PDINC = 56
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 776
try:
    XA_IOMDC_CONVCR = 57
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 778
try:
    XA_IOMDC_SIZE = 64
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 782
try:
    IOMDC_METHOD_HB = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 783
try:
    IOMDC_METHOD_GDDEFLT = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_BatchDCDll.h: 784
try:
    IOMDC_METHOD_GDSPEC = 2
except:
    pass

# No inserted files

# No prefix-stripping

