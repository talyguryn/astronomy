#!/usr/bin/env python3
import sys
import re

_iaudata = (
    (( 0.0,  0.0,  0.0,  0.0,  1.0), (-172064161.0,    -174666.0,      33386.0,   92052331.0,       9086.0,      15377.0)),
    (( 0.0,  0.0,  2.0, -2.0,  2.0), ( -13170906.0,      -1675.0,     -13696.0,    5730336.0,      -3015.0,      -4587.0)),
    (( 0.0,  0.0,  2.0,  0.0,  2.0), (  -2276413.0,       -234.0,       2796.0,     978459.0,       -485.0,       1374.0)),
    (( 0.0,  0.0,  0.0,  0.0,  2.0), (   2074554.0,        207.0,       -698.0,    -897492.0,        470.0,       -291.0)),
    (( 0.0,  1.0,  0.0,  0.0,  0.0), (   1475877.0,      -3633.0,      11817.0,      73871.0,       -184.0,      -1924.0)),
    (( 0.0,  1.0,  2.0, -2.0,  2.0), (   -516821.0,       1226.0,       -524.0,     224386.0,       -677.0,       -174.0)),
    (( 1.0,  0.0,  0.0,  0.0,  0.0), (    711159.0,         73.0,       -872.0,      -6750.0,          0.0,        358.0)),
    (( 0.0,  0.0,  2.0,  0.0,  1.0), (   -387298.0,       -367.0,        380.0,     200728.0,         18.0,        318.0)),
    (( 1.0,  0.0,  2.0,  0.0,  2.0), (   -301461.0,        -36.0,        816.0,     129025.0,        -63.0,        367.0)),
    (( 0.0, -1.0,  2.0, -2.0,  2.0), (    215829.0,       -494.0,        111.0,     -95929.0,        299.0,        132.0)),
    (( 0.0,  0.0,  2.0, -2.0,  1.0), (    128227.0,        137.0,        181.0,     -68982.0,         -9.0,         39.0)),
    ((-1.0,  0.0,  2.0,  0.0,  2.0), (    123457.0,         11.0,         19.0,     -53311.0,         32.0,         -4.0)),
    ((-1.0,  0.0,  0.0,  2.0,  0.0), (    156994.0,         10.0,       -168.0,      -1235.0,          0.0,         82.0)),
    (( 1.0,  0.0,  0.0,  0.0,  1.0), (     63110.0,         63.0,         27.0,     -33228.0,          0.0,         -9.0)),
    ((-1.0,  0.0,  0.0,  0.0,  1.0), (    -57976.0,        -63.0,       -189.0,      31429.0,          0.0,        -75.0)),
    ((-1.0,  0.0,  2.0,  2.0,  2.0), (    -59641.0,        -11.0,        149.0,      25543.0,        -11.0,         66.0)),
    (( 1.0,  0.0,  2.0,  0.0,  1.0), (    -51613.0,        -42.0,        129.0,      26366.0,          0.0,         78.0)),
    ((-2.0,  0.0,  2.0,  0.0,  1.0), (     45893.0,         50.0,         31.0,     -24236.0,        -10.0,         20.0)),
    (( 0.0,  0.0,  0.0,  2.0,  0.0), (     63384.0,         11.0,       -150.0,      -1220.0,          0.0,         29.0)),
    (( 0.0,  0.0,  2.0,  2.0,  2.0), (    -38571.0,         -1.0,        158.0,      16452.0,        -11.0,         68.0)),
    (( 0.0, -2.0,  2.0, -2.0,  2.0), (     32481.0,          0.0,          0.0,     -13870.0,          0.0,          0.0)),
    ((-2.0,  0.0,  0.0,  2.0,  0.0), (    -47722.0,          0.0,        -18.0,        477.0,          0.0,        -25.0)),
    (( 2.0,  0.0,  2.0,  0.0,  2.0), (    -31046.0,         -1.0,        131.0,      13238.0,        -11.0,         59.0)),
    (( 1.0,  0.0,  2.0, -2.0,  2.0), (     28593.0,          0.0,         -1.0,     -12338.0,         10.0,         -3.0)),
    ((-1.0,  0.0,  2.0,  0.0,  1.0), (     20441.0,         21.0,         10.0,     -10758.0,          0.0,         -3.0)),
    (( 2.0,  0.0,  0.0,  0.0,  0.0), (     29243.0,          0.0,        -74.0,       -609.0,          0.0,         13.0)),
    (( 0.0,  0.0,  2.0,  0.0,  0.0), (     25887.0,          0.0,        -66.0,       -550.0,          0.0,         11.0)),
    (( 0.0,  1.0,  0.0,  0.0,  1.0), (    -14053.0,        -25.0,         79.0,       8551.0,         -2.0,        -45.0)),
    ((-1.0,  0.0,  0.0,  2.0,  1.0), (     15164.0,         10.0,         11.0,      -8001.0,          0.0,         -1.0)),
    (( 0.0,  2.0,  2.0, -2.0,  2.0), (    -15794.0,         72.0,        -16.0,       6850.0,        -42.0,         -5.0)),
    (( 0.0,  0.0, -2.0,  2.0,  0.0), (     21783.0,          0.0,         13.0,       -167.0,          0.0,         13.0)),
    (( 1.0,  0.0,  0.0, -2.0,  1.0), (    -12873.0,        -10.0,        -37.0,       6953.0,          0.0,        -14.0)),
    (( 0.0, -1.0,  0.0,  0.0,  1.0), (    -12654.0,         11.0,         63.0,       6415.0,          0.0,         26.0)),
    ((-1.0,  0.0,  2.0,  2.0,  1.0), (    -10204.0,          0.0,         25.0,       5222.0,          0.0,         15.0)),
    (( 0.0,  2.0,  0.0,  0.0,  0.0), (     16707.0,        -85.0,        -10.0,        168.0,         -1.0,         10.0)),
    (( 1.0,  0.0,  2.0,  2.0,  2.0), (     -7691.0,          0.0,         44.0,       3268.0,          0.0,         19.0)),
    ((-2.0,  0.0,  2.0,  0.0,  0.0), (    -11024.0,          0.0,        -14.0,        104.0,          0.0,          2.0)),
    (( 0.0,  1.0,  2.0,  0.0,  2.0), (      7566.0,        -21.0,        -11.0,      -3250.0,          0.0,         -5.0)),
    (( 0.0,  0.0,  2.0,  2.0,  1.0), (     -6637.0,        -11.0,         25.0,       3353.0,          0.0,         14.0)),
    (( 0.0, -1.0,  2.0,  0.0,  2.0), (     -7141.0,         21.0,          8.0,       3070.0,          0.0,          4.0)),
    (( 0.0,  0.0,  0.0,  2.0,  1.0), (     -6302.0,        -11.0,          2.0,       3272.0,          0.0,          4.0)),
    (( 1.0,  0.0,  2.0, -2.0,  1.0), (      5800.0,         10.0,          2.0,      -3045.0,          0.0,         -1.0)),
    (( 2.0,  0.0,  2.0, -2.0,  2.0), (      6443.0,          0.0,         -7.0,      -2768.0,          0.0,         -4.0)),
    ((-2.0,  0.0,  0.0,  2.0,  1.0), (     -5774.0,        -11.0,        -15.0,       3041.0,          0.0,         -5.0)),
    (( 2.0,  0.0,  2.0,  0.0,  1.0), (     -5350.0,          0.0,         21.0,       2695.0,          0.0,         12.0)),
    (( 0.0, -1.0,  2.0, -2.0,  1.0), (     -4752.0,        -11.0,         -3.0,       2719.0,          0.0,         -3.0)),
    (( 0.0,  0.0,  0.0, -2.0,  1.0), (     -4940.0,        -11.0,        -21.0,       2720.0,          0.0,         -9.0)),
    ((-1.0, -1.0,  0.0,  2.0,  0.0), (      7350.0,          0.0,         -8.0,        -51.0,          0.0,          4.0)),
    (( 2.0,  0.0,  0.0, -2.0,  1.0), (      4065.0,          0.0,          6.0,      -2206.0,          0.0,          1.0)),
    (( 1.0,  0.0,  0.0,  2.0,  0.0), (      6579.0,          0.0,        -24.0,       -199.0,          0.0,          2.0)),
    (( 0.0,  1.0,  2.0, -2.0,  1.0), (      3579.0,          0.0,          5.0,      -1900.0,          0.0,          1.0)),
    (( 1.0, -1.0,  0.0,  0.0,  0.0), (      4725.0,          0.0,         -6.0,        -41.0,          0.0,          3.0)),
    ((-2.0,  0.0,  2.0,  0.0,  2.0), (     -3075.0,          0.0,         -2.0,       1313.0,          0.0,         -1.0)),
    (( 3.0,  0.0,  2.0,  0.0,  2.0), (     -2904.0,          0.0,         15.0,       1233.0,          0.0,          7.0)),
    (( 0.0, -1.0,  0.0,  2.0,  0.0), (      4348.0,          0.0,        -10.0,        -81.0,          0.0,          2.0)),
    (( 1.0, -1.0,  2.0,  0.0,  2.0), (     -2878.0,          0.0,          8.0,       1232.0,          0.0,          4.0)),
    (( 0.0,  0.0,  0.0,  1.0,  0.0), (     -4230.0,          0.0,          5.0,        -20.0,          0.0,         -2.0)),
    ((-1.0, -1.0,  2.0,  2.0,  2.0), (     -2819.0,          0.0,          7.0,       1207.0,          0.0,          3.0)),
    ((-1.0,  0.0,  2.0,  0.0,  0.0), (     -4056.0,          0.0,          5.0,         40.0,          0.0,         -2.0)),
    (( 0.0, -1.0,  2.0,  2.0,  2.0), (     -2647.0,          0.0,         11.0,       1129.0,          0.0,          5.0)),
    ((-2.0,  0.0,  0.0,  0.0,  1.0), (     -2294.0,          0.0,        -10.0,       1266.0,          0.0,         -4.0)),
    (( 1.0,  1.0,  2.0,  0.0,  2.0), (      2481.0,          0.0,         -7.0,      -1062.0,          0.0,         -3.0)),
    (( 2.0,  0.0,  0.0,  0.0,  1.0), (      2179.0,          0.0,         -2.0,      -1129.0,          0.0,         -2.0)),
    ((-1.0,  1.0,  0.0,  1.0,  0.0), (      3276.0,          0.0,          1.0,         -9.0,          0.0,          0.0)),
    (( 1.0,  1.0,  0.0,  0.0,  0.0), (     -3389.0,          0.0,          5.0,         35.0,          0.0,         -2.0)),
    (( 1.0,  0.0,  2.0,  0.0,  0.0), (      3339.0,          0.0,        -13.0,       -107.0,          0.0,          1.0)),
    ((-1.0,  0.0,  2.0, -2.0,  1.0), (     -1987.0,          0.0,         -6.0,       1073.0,          0.0,         -2.0)),
    (( 1.0,  0.0,  0.0,  0.0,  2.0), (     -1981.0,          0.0,          0.0,        854.0,          0.0,          0.0)),
    ((-1.0,  0.0,  0.0,  1.0,  0.0), (      4026.0,          0.0,       -353.0,       -553.0,          0.0,       -139.0)),
    (( 0.0,  0.0,  2.0,  1.0,  2.0), (      1660.0,          0.0,         -5.0,       -710.0,          0.0,         -2.0)),
    ((-1.0,  0.0,  2.0,  4.0,  2.0), (     -1521.0,          0.0,          9.0,        647.0,          0.0,          4.0)),
    ((-1.0,  1.0,  0.0,  1.0,  1.0), (      1314.0,          0.0,          0.0,       -700.0,          0.0,          0.0)),
    (( 0.0, -2.0,  2.0, -2.0,  1.0), (     -1283.0,          0.0,          0.0,        672.0,          0.0,          0.0)),
    (( 1.0,  0.0,  2.0,  2.0,  1.0), (     -1331.0,          0.0,          8.0,        663.0,          0.0,          4.0)),
    ((-2.0,  0.0,  2.0,  2.0,  2.0), (      1383.0,          0.0,         -2.0,       -594.0,          0.0,         -2.0)),
    ((-1.0,  0.0,  0.0,  0.0,  2.0), (      1405.0,          0.0,          4.0,       -610.0,          0.0,          2.0)),
    (( 1.0,  1.0,  2.0, -2.0,  2.0), (      1290.0,          0.0,          0.0,       -556.0,          0.0,          0.0)),
)

def OptimizeDotProduct(nlist, vlist):
    text = ''
    first = True
    for n, v in zip(nlist, vlist):
        if n != 0.0:
            if n < 0.0:
                n *= -1.0
                op = ' - '
            else:
                op = ' + '

            if n == 1.0:                
                prod = v
            else:
                prod = '({:0.1f}*{})'.format(n, v)

            if first:
                if op == ' - ':
                    text += '-'
                text += prod
            else:
                text += op + prod
            first = False
    return text

def UnrollIauLoop():
    text = ''
    nv = ['el', 'elp', 'f', 'd', 'om']
    for n, (c0, c1, c2, c3, c4, c5) in _iaudata:
        #      arg = math.fmod((n0*el + n1*elp + n2*f + n3*d + n4*om), _PI2)
        #      sarg = math.sin(arg)
        #      carg = math.cos(arg)
        #      dp += (c0 + c1*t)*sarg + c2*carg
        #      de += (c3 + c4*t)*carg + c5*sarg

        # Form optmized dot product of n*nv.
        dotprod = OptimizeDotProduct(n, nv)
        text += '        arg = math.fmod({}, _PI2)\n'.format(dotprod)
        text += '        sarg = math.sin(arg)\n'
        text += '        carg = math.cos(arg)\n'
        text += '        dp += ({:0.1f} + {:0.1f}*t)*sarg + {:0.1f}*carg\n'.format(c0, c1, c2)
        text += '        de += ({:0.1f} + {:0.1f}*t)*carg + {:0.1f}*sarg\n'.format(c3, c4, c5)

    return text


def Translate(line):
    if line.strip() == '__IAULOOP__':
        return UnrollIauLoop()

    m = re.match(r'^    AddSol\(\s*([0-9\+\-\.]+)\s*,\s*([0-9\+\-\.]+)\s*,\s*([0-9\+\-\.]+)\s*,\s*([0-9\+\-\.]+)\s*,\s*([\+\-]?\d+)\s*,\s*([\+\-]?\d+)\s*,\s*([\+\-]?\d+)\s*,\s*([\+\-]?\d+)\s*\)\s*$', line)
    if m:
        cl = float(m.group(1))
        cs = float(m.group(2))
        cg = float(m.group(3))
        cp = float(m.group(4))
        p = int(m.group(5))
        q = int(m.group(6))
        r = int(m.group(7))
        s = int(m.group(8))

        text = '\n'
        text += '    # AddSol({}, {}, {}, {}, {}, {}, {}, {})\n'.format(cl, cs, cg, cp, p, q, r, s)

        op = ''
        text += '    z = '
        if p != 0:
            text += op + 'ex[{}][1]'.format(p)
            op = ' * '
        if q != 0:
            text += op + 'ex[{}][2]'.format(q)
            op = ' * '
        if r != 0:
            text += op + 'ex[{}][3]'.format(r)
            op = ' * '
        if s != 0:
            text += op + 'ex[{}][4]'.format(s)
        text += '\n'

        if cl != 0:
            text += '    DLAM  += {} * z.imag\n'.format(cl)
        if cs != 0:
            text += '    DS    += {} * z.imag\n'.format(cs)
        if cg != 0:
            text += '    GAM1C += {} * z.real\n'.format(cg)
        if cp != 0:
            text += '    SINPI += {} * z.real\n'.format(cp)
        
        return text
    return line

def FixAddSol(inFileName, outFileName):
    with open(inFileName, 'rt') as infile:
        with open(outFileName, 'wt') as outfile:
            lnum = 0
            for line in infile:
                lnum += 1
                xlat = Translate(line)
                outfile.write(xlat)

if __name__ == '__main__':
    FixAddSol('template/old.py', 'template/astronomy.py')
    sys.exit(0)
