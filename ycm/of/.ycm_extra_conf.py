import os
import ycm_core
from clang_helpers import PrepareClangFlags
 
# Set this to the absolute path to the folder (NOT the file!) containing the
# compile_commands.json file to use that instead of 'flags'. See here for
# more details: http://clang.llvm.org/docs/JSONCompilationDatabase.html
# Most projects will NOT need to set this to anything; you can just change the
# 'flags' list of compilation flags. Notice that YCM itself uses that approach.
compilation_database_folder = ''
 
# These are the compilation flags that will be used in case there's no
# compilation database set.
flags = [
    '-Wall',
    '-std=c++11',
    # '-stdlib=libstdc++',
    '-fexceptions',
    '-march=native',
    '-mtune=native',
    '-finline-functions',
    '-arch i386',
    '-fpascal-strings',
    '-mmacosx-version-min=10.9',
    '-fasm-blocks',
    '-funroll-loops',
    '-mssse3', 
    '-fmessage-length=0', 
    '-D__MACOSX_CORE__',
    # '-x',
    # 'c++',
    # '-c',
    '-0s',
    '-I',
    '.',
    '-isystem',
    '/usr/include',
    '-isystem',
    '/usr/local/include',
    '-isystem',
    #'/Library/Developer/CommandLineTools/usr/bin/../lib/c++/v1',
    '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../include/c++/v1',
    '-isystem',
    '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../lib/clang/6.0/include',
    '-isystem',
    '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include',
    '-I./src' 
    '-I../../../libs/FreeImage/include', 
    '-I../../../libs/cairo/include',
    '-I../../../libs/cairo/include/cairo',
    '-I../../../libs/cairo/include/libpng15',
    '-I../../../libs/cairo/include/pixman-1',
    '-I../../../libs/fmodex/include',
    '-I../../../libs/freetype/include',
    '-I../../../libs/freetype/include/freetype2',
    '-I../../../libs/freetype/include/freetype2/freetype',
    '-I../../../libs/freetype/include/freetype2/freetype/config',
    '-I../../../libs/freetype/include/freetype2/freetype/internal',
    '-I../../../libs/freetype/include/freetype2/freetype/internal/services',
    '-I../../../libs/glew/include', 
    '-I../../../libs/glew/include/GL',
    '-I../../../libs/glfw/include',
    '-I../../../libs/glfw/include/GLFW',
    '-I../../../libs/glu/include',
    '-I../../../libs/glut/include',
    '-I../../../libs/kiss/include',
    '-I../../../libs/openssl/include',
    '-I../../../libs/openssl/include/openssl',
    '-I../../../libs/poco/include',
    '-I../../../libs/rtAudio/include',
    '-I../../../libs/tess2/include',
    '-I../../../libs/openFrameworks',
    '-I../../../libs/openFrameworks/3d',
    '-I../../../libs/openFrameworks/app',
    '-I../../../libs/openFrameworks/communication',
    '-I../../../libs/openFrameworks/events',
    '-I../../../libs/openFrameworks/gl',
    '-I../../../libs/openFrameworks/graphics',
    '-I../../../libs/openFrameworks/math',
    '-I../../../libs/openFrameworks/sound',
    '-I../../../libs/openFrameworks/types',
    '-I../../../libs/openFrameworks/utils',
    '-I../../../libs/openFrameworks/video',
    # '-x objective-c++',
    '-MMD',
    '-MP' 
    '-MF',
    'obj/osx/Release/src/ofApp.d',
    ]


# flagsRec=['/Users/peacedove/Documents/Code/OF/of_v0.8.3_osx_release/libs/','/Users/peacedove/Documents/Code/OF/of_v0.8.3_osx_release/addons/']

# def AddDirsRecursively( flagsRec ):
#     global flags
#     new_flags = []
#     for flag in flagsRec:
#         for root, dirs, files in os.walk(flag, topdown=True):
#             for name in dirs:
#                 new_flags.append('-I')
#                 new_flags.append(os.path.join(root,name))
#     flags += new_flags
# AddDirsRecursively( flagsRec )

if compilation_database_folder:
    database = ycm_core.CompilationDatabase(compilation_database_folder)
else:
    database = None
 
 
def DirectoryOfThisScript():
    return os.path.dirname(os.path.abspath(__file__))
 
 
def MakeRelativePathsInFlagsAbsolute(flags, working_directory):
    if not working_directory:
        return flags
    new_flags = []
    make_next_absolute = False
    path_flags = ['-isystem', '-I', '-iquote', '--sysroot=']
    for flag in flags:
        new_flag = flag
 
        if make_next_absolute:
            make_next_absolute = False
            if not flag.startswith('/'):
                new_flag = os.path.join(working_directory, flag)
 
        for path_flag in path_flags:
            if flag == path_flag:
                make_next_absolute = True
                break
 
            if flag.startswith(path_flag):
                path = flag[len(path_flag):]
                new_flag = path_flag + os.path.join(working_directory, path)
                break
 
        if new_flag:
            new_flags.append(new_flag)
    return new_flags
 
 
def FlagsForFile(filename):
    if database:
        # Bear in mind that compilation_info.compiler_flags_ does NOT return a
        # python list, but a "list-like" StringVec object
        compilation_info = database.GetCompilationInfoForFile(filename)
        final_flags = PrepareClangFlags(
            MakeRelativePathsInFlagsAbsolute(
                compilation_info.compiler_flags_,
                compilation_info.compiler_working_dir_),
            filename)
    else:
        relative_to = DirectoryOfThisScript()
        final_flags = MakeRelativePathsInFlagsAbsolute(flags, relative_to)
 
    return {
        'flags': final_flags,
        'do_cache': True}

