from segtypes.common.asm import CommonSegAsm

from util import options


class PsxSegAsm(CommonSegAsm):
    @staticmethod
    def get_file_header():
        ret = []

        ret.append('.include "macro.inc"')
        ret.append("")
        ret.append(".set noat")
        ret.append(".set noreorder")
        ret.append("")
        preamble = options.opts.generated_s_preamble
        if preamble:
            ret.append(preamble)
            ret.append("")
        ret.append('.section .text, "ax"')
        ret.append("")

        return ret
