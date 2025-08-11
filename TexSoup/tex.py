from TexSoup.reader import read_expr, read_tex
from TexSoup.data import *
from TexSoup.utils import *
from TexSoup.tokens import tokenize
from TexSoup.category import categorize
import itertools


def read(tex, skip_envs=(), tolerance=0, progress_callback=None):
    """Read and parse all LaTeX source.

    :param Union[str,iterable] tex: LaTeX source
    :param Union[str] skip_envs: names of environments to skip parsing
    :param int tolerance: error tolerance level (only supports 0 or 1)
    :param progress_callback: a function to call with current position 
        when new expression is parsed (maximum value is length of source)
    :return TexEnv: the global environment
    """
    if not isinstance(tex, str):
        tex = ''.join(itertools.chain(*tex))
    buf = categorize(tex)
    buf = tokenize(buf)
    buf = read_tex(buf, skip_envs=skip_envs, tolerance=tolerance, progress_callback=progress_callback)
    env = TexEnv('[tex]', begin='', end='', contents=buf) # This is where the generators are expanded
    if progress_callback:
        progress_callback(len(tex))
    return env, tex
