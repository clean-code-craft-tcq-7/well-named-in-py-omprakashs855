from colorCode import ColorCode
import colorCodingManual as ccm
import test_colorCode as tcc

if __name__ == '__main__':
    cc_Obj = ColorCode()
    tcc.test_main(cc_Obj)
    ccm.color_coding_manual(cc_Obj)
    print('Done :)')