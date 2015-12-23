import cffi

ffi = cffi.FFI()
ffi.set_source(
    "kociemba",
    """
    #include <stdio.h>
    #include <stdlib.h>
    #include <search.h>

    char* solve(char *cubestring)
    {
        char *sol = solution(
            cubestring,
            24,
            1000,
            0
        );
        return sol;
    }
    """,
    include_dirs=['include'],
    sources=['coordcube.c', 'cubiecube.c', 'facecube.c', 'search.c'],
    extra_compile_args=['-std=c99'])

ffi.cdef("char* solve(char *cubestring);")

if __name__ == "__main__":
    ffi.compile(verbose=True)
