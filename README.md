# Open AstroStandard harnesses

Kerry N. Wood (kerry.wood@asterism.ai)

The AstroStandards come with some Python harnesses for the libraries, but I like to build my own.  This code uses Python
and `ctypesgen` to inspect the C headers and build the Python wrappers.  Why?  The C-headers are usually well
maintained, and allow for finer-grained control of the underlying FORTRAN.  

# I just want to use them!

- go get the DLL's and shared libraries from space-track.org and copy them to a directory
- copy the wrappers for the appropriate version and OS (e.g. V94/linux) to the same directory
- copy the utils/*.py code into the same directory
- try (on linux) : "LD_LIBRARY_PATH=<directory> PYTHONPATH=<directory> python <directory>/load_utils.py"
- try (on Windows) : set your PATH to include <directory>, your PYTHONPATH as well, and try python
  <directory>/load_utils.py"

# I want to try and build them

This process is a little wonky: headers are reformatted and then run through `ctypesgen`.  If `gcc` and the linker can
find the dependencies, you get auto-generated wrappers.  The easiest way is on linux.  Do the following:

- unzip the AstroStandards
- copy the appropriate linux libraries to the <astrostd>/SampleCode/c/DriverExamples/wrappers directory
- cd to that directory
- run `python <path>/build_ctypes_from_python.py --headers ./ --librariers ./`
- run the `runme.sh` script that it outputs
- this should generate the wrappers; if you open the python files up, you should see references to functions and
  parameters
- (optional) run `linux_to_win.py` on the wrappers to build the renamed Windows wrappers
