r"""Wrapper for new_TleDll.h

Generated with:
/home/woodkn1/DND/bin/ctypesgen -I . ./new_TleDll.h -o ./TleDll.py

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

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 25
for _lib in _libs.values():
    if not _lib.has("TleInit", "cdecl"):
        continue
    TleInit = _lib.get("TleInit", "cdecl")
    TleInit.argtypes = [c_int64]
    TleInit.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 31
for _lib in _libs.values():
    if not _lib.has("TleGetInfo", "cdecl"):
        continue
    TleGetInfo = _lib.get("TleGetInfo", "cdecl")
    TleGetInfo.argtypes = [c_char * int(128)]
    TleGetInfo.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 42
for _lib in _libs.values():
    if not _lib.has("TleLoadFile", "cdecl"):
        continue
    TleLoadFile = _lib.get("TleLoadFile", "cdecl")
    TleLoadFile.argtypes = [c_char * int(512)]
    TleLoadFile.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 54
for _lib in _libs.values():
    if not _lib.has("TleSaveFile", "cdecl"):
        continue
    TleSaveFile = _lib.get("TleSaveFile", "cdecl")
    TleSaveFile.argtypes = [c_char * int(512), c_int, c_int]
    TleSaveFile.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 61
for _lib in _libs.values():
    if not _lib.has("TleRemoveSat", "cdecl"):
        continue
    TleRemoveSat = _lib.get("TleRemoveSat", "cdecl")
    TleRemoveSat.argtypes = [c_int64]
    TleRemoveSat.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 66
for _lib in _libs.values():
    if not _lib.has("TleRemoveAllSats", "cdecl"):
        continue
    TleRemoveAllSats = _lib.get("TleRemoveAllSats", "cdecl")
    TleRemoveAllSats.argtypes = []
    TleRemoveAllSats.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 73
for _lib in _libs.values():
    if not _lib.has("TleGetCount", "cdecl"):
        continue
    TleGetCount = _lib.get("TleGetCount", "cdecl")
    TleGetCount.argtypes = []
    TleGetCount.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 82
for _lib in _libs.values():
    if not _lib.has("TleGetLoaded", "cdecl"):
        continue
    TleGetLoaded = _lib.get("TleGetLoaded", "cdecl")
    TleGetLoaded.argtypes = [c_int, POINTER(c_int64)]
    TleGetLoaded.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 92
for _lib in _libs.values():
    if not _lib.has("TleAddSatFrLines", "cdecl"):
        continue
    TleAddSatFrLines = _lib.get("TleAddSatFrLines", "cdecl")
    TleAddSatFrLines.argtypes = [c_char * int(512), c_char * int(512)]
    TleAddSatFrLines.restype = c_int64
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 100
for _lib in _libs.values():
    if not _lib.has("TleAddSatFrLinesML", "cdecl"):
        continue
    TleAddSatFrLinesML = _lib.get("TleAddSatFrLinesML", "cdecl")
    TleAddSatFrLinesML.argtypes = [c_char * int(512), c_char * int(512), POINTER(c_int64)]
    TleAddSatFrLinesML.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 106
for _lib in _libs.values():
    if not _lib.has("TleAddSatFrCsv", "cdecl"):
        continue
    TleAddSatFrCsv = _lib.get("TleAddSatFrCsv", "cdecl")
    TleAddSatFrCsv.argtypes = [c_char * int(512)]
    TleAddSatFrCsv.restype = c_int64
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 112
for _lib in _libs.values():
    if not _lib.has("TleAddSatFrCsvML", "cdecl"):
        continue
    TleAddSatFrCsvML = _lib.get("TleAddSatFrCsvML", "cdecl")
    TleAddSatFrCsvML.argtypes = [c_char * int(512), POINTER(c_int64)]
    TleAddSatFrCsvML.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 137
for _lib in _libs.values():
    if not _lib.has("TleAddSatFrFieldsGP", "cdecl"):
        continue
    TleAddSatFrFieldsGP = _lib.get("TleAddSatFrFieldsGP", "cdecl")
    TleAddSatFrFieldsGP.argtypes = [c_int, c_char, c_char * int(8), c_int, c_double, c_double, c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int]
    TleAddSatFrFieldsGP.restype = c_int64
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 160
for _lib in _libs.values():
    if not _lib.has("TleAddSatFrFieldsGP2", "cdecl"):
        continue
    TleAddSatFrFieldsGP2 = _lib.get("TleAddSatFrFieldsGP2", "cdecl")
    TleAddSatFrFieldsGP2.argtypes = [c_int, c_char, c_char * int(8), c_int, c_double, c_double, c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_double, c_double]
    TleAddSatFrFieldsGP2.restype = c_int64
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 183
for _lib in _libs.values():
    if not _lib.has("TleAddSatFrFieldsGP2ML", "cdecl"):
        continue
    TleAddSatFrFieldsGP2ML = _lib.get("TleAddSatFrFieldsGP2ML", "cdecl")
    TleAddSatFrFieldsGP2ML.argtypes = [c_int, c_char, c_char * int(8), c_int, c_double, c_double, c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_double, c_double, POINTER(c_int64)]
    TleAddSatFrFieldsGP2ML.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 203
for _lib in _libs.values():
    if not _lib.has("TleUpdateSatFrFieldsGP", "cdecl"):
        continue
    TleUpdateSatFrFieldsGP = _lib.get("TleUpdateSatFrFieldsGP", "cdecl")
    TleUpdateSatFrFieldsGP.argtypes = [c_int64, c_char, c_char * int(8), c_double, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int]
    TleUpdateSatFrFieldsGP.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 223
for _lib in _libs.values():
    if not _lib.has("TleUpdateSatFrFieldsGP2", "cdecl"):
        continue
    TleUpdateSatFrFieldsGP2 = _lib.get("TleUpdateSatFrFieldsGP2", "cdecl")
    TleUpdateSatFrFieldsGP2.argtypes = [c_int64, c_char, c_char * int(8), c_double, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_double, c_double]
    TleUpdateSatFrFieldsGP2.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 245
for _lib in _libs.values():
    if not _lib.has("TleAddSatFrFieldsSP", "cdecl"):
        continue
    TleAddSatFrFieldsSP = _lib.get("TleAddSatFrFieldsSP", "cdecl")
    TleAddSatFrFieldsSP.argtypes = [c_int, c_char, c_char * int(8), c_int, c_double, c_double, c_double, c_double, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int]
    TleAddSatFrFieldsSP.restype = c_int64
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 268
for _lib in _libs.values():
    if not _lib.has("TleAddSatFrFieldsSPML", "cdecl"):
        continue
    TleAddSatFrFieldsSPML = _lib.get("TleAddSatFrFieldsSPML", "cdecl")
    TleAddSatFrFieldsSPML.argtypes = [c_int, c_char, c_char * int(8), c_int, c_double, c_double, c_double, c_double, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int, POINTER(c_int64)]
    TleAddSatFrFieldsSPML.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 289
for _lib in _libs.values():
    if not _lib.has("TleUpdateSatFrFieldsSP", "cdecl"):
        continue
    TleUpdateSatFrFieldsSP = _lib.get("TleUpdateSatFrFieldsSP", "cdecl")
    TleUpdateSatFrFieldsSP.argtypes = [c_int64, c_char, c_char * int(8), c_double, c_double, c_double, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int]
    TleUpdateSatFrFieldsSP.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 326
for _lib in _libs.values():
    if not _lib.has("TleSetField", "cdecl"):
        continue
    TleSetField = _lib.get("TleSetField", "cdecl")
    TleSetField.argtypes = [c_int64, c_int, c_char * int(512)]
    TleSetField.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 362
for _lib in _libs.values():
    if not _lib.has("TleGetField", "cdecl"):
        continue
    TleGetField = _lib.get("TleGetField", "cdecl")
    TleGetField.argtypes = [c_int64, c_int, c_char * int(512)]
    TleGetField.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 384
for _lib in _libs.values():
    if not _lib.has("TleGetAllFieldsGP", "cdecl"):
        continue
    TleGetAllFieldsGP = _lib.get("TleGetAllFieldsGP", "cdecl")
    TleGetAllFieldsGP.argtypes = [c_int64, POINTER(c_int), String, c_char * int(8), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int)]
    TleGetAllFieldsGP.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 409
for _lib in _libs.values():
    if not _lib.has("TleGetAllFieldsGP2", "cdecl"):
        continue
    TleGetAllFieldsGP2 = _lib.get("TleGetAllFieldsGP2", "cdecl")
    TleGetAllFieldsGP2.argtypes = [c_int64, POINTER(c_int), String, c_char * int(8), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_double), POINTER(c_double)]
    TleGetAllFieldsGP2.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 433
for _lib in _libs.values():
    if not _lib.has("TleGetAllFieldsSP", "cdecl"):
        continue
    TleGetAllFieldsSP = _lib.get("TleGetAllFieldsSP", "cdecl")
    TleGetAllFieldsSP.argtypes = [c_int64, POINTER(c_int), String, c_char * int(8), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int)]
    TleGetAllFieldsSP.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 458
for _lib in _libs.values():
    if not _lib.has("TleParseGP", "cdecl"):
        continue
    TleParseGP = _lib.get("TleParseGP", "cdecl")
    TleParseGP.argtypes = [c_char * int(512), c_char * int(512), POINTER(c_int), String, c_char * int(8), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int)]
    TleParseGP.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 468
for _lib in _libs.values():
    if not _lib.has("TleLinesToArray", "cdecl"):
        continue
    TleLinesToArray = _lib.get("TleLinesToArray", "cdecl")
    TleLinesToArray.argtypes = [c_char * int(512), c_char * int(512), c_double * int(64), c_char * int(512)]
    TleLinesToArray.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 493
for _lib in _libs.values():
    if not _lib.has("TleParseSP", "cdecl"):
        continue
    TleParseSP = _lib.get("TleParseSP", "cdecl")
    TleParseSP.argtypes = [c_char * int(512), c_char * int(512), POINTER(c_int), String, c_char * int(8), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int)]
    TleParseSP.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 501
for _lib in _libs.values():
    if not _lib.has("TleGetLines", "cdecl"):
        continue
    TleGetLines = _lib.get("TleGetLines", "cdecl")
    TleGetLines.argtypes = [c_int64, c_char * int(512), c_char * int(512)]
    TleGetLines.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 508
for _lib in _libs.values():
    if not _lib.has("TleGetCsv", "cdecl"):
        continue
    TleGetCsv = _lib.get("TleGetCsv", "cdecl")
    TleGetCsv.argtypes = [c_int64, c_char * int(512)]
    TleGetCsv.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 533
for _lib in _libs.values():
    if not _lib.has("TleGPFieldsToLines", "cdecl"):
        continue
    TleGPFieldsToLines = _lib.get("TleGPFieldsToLines", "cdecl")
    TleGPFieldsToLines.argtypes = [c_int, c_char, c_char * int(8), c_int, c_double, c_double, c_double, c_double, c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_char * int(512), c_char * int(512)]
    TleGPFieldsToLines.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 557
for _lib in _libs.values():
    if not _lib.has("TleGPFieldsToCsv", "cdecl"):
        continue
    TleGPFieldsToCsv = _lib.get("TleGPFieldsToCsv", "cdecl")
    TleGPFieldsToCsv.argtypes = [c_int, c_char, c_char * int(8), c_int, c_double, c_double, c_double, c_double, c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_char * int(512)]
    TleGPFieldsToCsv.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 568
for _lib in _libs.values():
    if not _lib.has("TleGPArrayToLines", "cdecl"):
        continue
    TleGPArrayToLines = _lib.get("TleGPArrayToLines", "cdecl")
    TleGPArrayToLines.argtypes = [c_double * int(64), c_char * int(512), c_char * int(512), c_char * int(512)]
    TleGPArrayToLines.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 577
for _lib in _libs.values():
    if not _lib.has("TleGPArrayToCsv", "cdecl"):
        continue
    TleGPArrayToCsv = _lib.get("TleGPArrayToCsv", "cdecl")
    TleGPArrayToCsv.argtypes = [c_double * int(64), c_char * int(512), c_char * int(512)]
    TleGPArrayToCsv.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 602
for _lib in _libs.values():
    if not _lib.has("TleSPFieldsToLines", "cdecl"):
        continue
    TleSPFieldsToLines = _lib.get("TleSPFieldsToLines", "cdecl")
    TleSPFieldsToLines.argtypes = [c_int, c_char, c_char * int(8), c_int, c_double, c_double, c_double, c_double, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_char * int(512), c_char * int(512)]
    TleSPFieldsToLines.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 610
for _lib in _libs.values():
    if not _lib.has("TleGetSatKey", "cdecl"):
        continue
    TleGetSatKey = _lib.get("TleGetSatKey", "cdecl")
    TleGetSatKey.argtypes = [c_int]
    TleGetSatKey.restype = c_int64
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 619
for _lib in _libs.values():
    if not _lib.has("TleGetSatKeyML", "cdecl"):
        continue
    TleGetSatKeyML = _lib.get("TleGetSatKeyML", "cdecl")
    TleGetSatKeyML.argtypes = [c_int, POINTER(c_int64)]
    TleGetSatKeyML.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 632
for _lib in _libs.values():
    if not _lib.has("TleFieldsToSatKey", "cdecl"):
        continue
    TleFieldsToSatKey = _lib.get("TleFieldsToSatKey", "cdecl")
    TleFieldsToSatKey.argtypes = [c_int, c_int, c_double, c_int]
    TleFieldsToSatKey.restype = c_int64
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 646
for _lib in _libs.values():
    if not _lib.has("TleFieldsToSatKeyML", "cdecl"):
        continue
    TleFieldsToSatKeyML = _lib.get("TleFieldsToSatKeyML", "cdecl")
    TleFieldsToSatKeyML.argtypes = [c_int, c_int, c_double, c_int, POINTER(c_int64)]
    TleFieldsToSatKeyML.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 653
for _lib in _libs.values():
    if not _lib.has("TleAddSatFrArray", "cdecl"):
        continue
    TleAddSatFrArray = _lib.get("TleAddSatFrArray", "cdecl")
    TleAddSatFrArray.argtypes = [c_double * int(64), c_char * int(512)]
    TleAddSatFrArray.restype = c_int64
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 660
for _lib in _libs.values():
    if not _lib.has("TleAddSatFrArrayML", "cdecl"):
        continue
    TleAddSatFrArrayML = _lib.get("TleAddSatFrArrayML", "cdecl")
    TleAddSatFrArrayML.argtypes = [c_double * int(64), c_char * int(512), POINTER(c_int64)]
    TleAddSatFrArrayML.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 669
for _lib in _libs.values():
    if not _lib.has("TleUpdateSatFrArray", "cdecl"):
        continue
    TleUpdateSatFrArray = _lib.get("TleUpdateSatFrArray", "cdecl")
    TleUpdateSatFrArray.argtypes = [c_int64, c_double * int(64), c_char * int(512)]
    TleUpdateSatFrArray.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 677
for _lib in _libs.values():
    if not _lib.has("TleDataToArray", "cdecl"):
        continue
    TleDataToArray = _lib.get("TleDataToArray", "cdecl")
    TleDataToArray.argtypes = [c_int64, c_double * int(64), c_char * int(512)]
    TleDataToArray.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 685
for _lib in _libs.values():
    if not _lib.has("TleLinesToCsv", "cdecl"):
        continue
    TleLinesToCsv = _lib.get("TleLinesToCsv", "cdecl")
    TleLinesToCsv.argtypes = [c_char * int(512), c_char * int(512), c_char * int(512)]
    TleLinesToCsv.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 694
for _lib in _libs.values():
    if not _lib.has("TleCsvToLines", "cdecl"):
        continue
    TleCsvToLines = _lib.get("TleCsvToLines", "cdecl")
    TleCsvToLines.argtypes = [c_char * int(512), c_int, c_char * int(512), c_char * int(512)]
    TleCsvToLines.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 700
for _lib in _libs.values():
    if not _lib.has("SetTleKeyMode", "cdecl"):
        continue
    SetTleKeyMode = _lib.get("SetTleKeyMode", "cdecl")
    SetTleKeyMode.argtypes = [c_int]
    SetTleKeyMode.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 705
for _lib in _libs.values():
    if not _lib.has("GetTleKeyMode", "cdecl"):
        continue
    GetTleKeyMode = _lib.get("GetTleKeyMode", "cdecl")
    GetTleKeyMode.argtypes = []
    GetTleKeyMode.restype = c_int
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 714
for _lib in _libs.values():
    if not _lib.has("GetCheckSums", "cdecl"):
        continue
    GetCheckSums = _lib.get("GetCheckSums", "cdecl")
    GetCheckSums.argtypes = [c_char * int(512), c_char * int(512), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    GetCheckSums.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 874
for _lib in _libs.values():
    if not _lib.has("LoadTleDll", "cdecl"):
        continue
    LoadTleDll = _lib.get("LoadTleDll", "cdecl")
    LoadTleDll.argtypes = []
    LoadTleDll.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 875
for _lib in _libs.values():
    if not _lib.has("FreeTleDll", "cdecl"):
        continue
    FreeTleDll = _lib.get("FreeTleDll", "cdecl")
    FreeTleDll.argtypes = []
    FreeTleDll.restype = None
    break

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 14
try:
    TleDll = 'libtle.so'
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 718
try:
    TLETYPE_SGP = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 719
try:
    TLETYPE_SGP4 = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 720
try:
    TLETYPE_PPT3 = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 721
try:
    TLETYPE_XP = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 722
try:
    TLETYPE_SP = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 726
try:
    XF_TLE_SATNUM = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 727
try:
    XF_TLE_CLASS = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 728
try:
    XF_TLE_SATNAME = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 729
try:
    XF_TLE_EPOCH = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 730
try:
    XF_TLE_BSTAR = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 731
try:
    XF_TLE_EPHTYPE = 6
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 732
try:
    XF_TLE_ELSETNUM = 7
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 733
try:
    XF_TLE_INCLI = 8
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 734
try:
    XF_TLE_NODE = 9
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 735
try:
    XF_TLE_ECCEN = 10
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 736
try:
    XF_TLE_OMEGA = 11
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 737
try:
    XF_TLE_MNANOM = 12
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 738
try:
    XF_TLE_MNMOTN = 13
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 739
try:
    XF_TLE_REVNUM = 14
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 741
try:
    XF_TLE_NDOT = 15
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 742
try:
    XF_TLE_NDOTDOT = 16
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 743
try:
    XF_TLE_AGOMGP = 16
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 745
try:
    XF_TLE_SP_AGOM = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 746
try:
    XF_TLE_SP_BTERM = 15
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 747
try:
    XF_TLE_SP_OGPARM = 16
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 749
try:
    XF_TLE_ORGSATNUM = 17
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 750
try:
    XF_TLE_BTERM = 18
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 751
try:
    XF_TLE_OBSTIME = 19
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 752
try:
    XF_TLE_EGR = 20
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 753
try:
    XF_TLE_EDR = 21
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 754
try:
    XF_TLE_VISMAG = 22
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 755
try:
    XF_TLE_RCS = 23
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 756
try:
    XF_TLE_OBJTYPE = 24
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 757
try:
    XF_TLE_SATNAME_12 = 25
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 763
try:
    XA_TLE_SATNUM = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 764
try:
    XA_TLE_EPOCH = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 765
try:
    XA_TLE_NDOT = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 766
try:
    XA_TLE_NDOTDOT = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 767
try:
    XA_TLE_BSTAR = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 768
try:
    XA_TLE_EPHTYPE = 5
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 771
try:
    XA_TLE_INCLI = 20
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 772
try:
    XA_TLE_NODE = 21
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 773
try:
    XA_TLE_ECCEN = 22
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 774
try:
    XA_TLE_OMEGA = 23
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 775
try:
    XA_TLE_MNANOM = 24
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 776
try:
    XA_TLE_MNMOTN = 25
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 777
try:
    XA_TLE_REVNUM = 26
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 778
try:
    XA_TLE_ELSETNUM = 30
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 781
try:
    XA_TLE_ORGSATNUM = 31
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 782
try:
    XA_TLE_BTERM = 32
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 783
try:
    XA_TLE_OBSTIME = 33
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 784
try:
    XA_TLE_EGR = 34
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 785
try:
    XA_TLE_EDR = 35
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 786
try:
    XA_TLE_VISMAG = 36
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 787
try:
    XA_TLE_RCS = 37
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 790
try:
    XA_TLE_AGOMGP = 38
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 794
try:
    XA_TLE_SP_BTERM = 2
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 795
try:
    XA_TLE_SP_OGPARM = 3
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 796
try:
    XA_TLE_SP_AGOM = 4
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 798
try:
    XA_TLE_SIZE = 64
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 802
try:
    XS_TLE_SECCLASS_1 = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 803
try:
    XS_TLE_SATNAME_12 = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 804
try:
    XS_TLE_OBJTYPE_11 = 13
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 806
try:
    XS_TLE_SIZE = 512
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 810
try:
    XS_TLE_SECCLASS_0_1 = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 811
try:
    XS_TLE_SATNAME_1_12 = 1
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 812
try:
    XS_TLE_OBJTYPE_13_1 = 13
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 814
try:
    XS_TLE_LENGTH = 512
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 818
try:
    XF_TLEFORM_ORG = 0
except:
    pass

# /tmp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_TleDll.h: 819
try:
    XF_TLEFORM_CSV = 1
except:
    pass

# No inserted files

# No prefix-stripping

