#!/usr/bin/env python3
"""Generate icon-192.png and icon-512.png with the stdlib only (no PIL).
Full-bleed dark square (maskable-safe) with three list bars: two dim (last
order), one accent (this order)."""
import struct, zlib, math, sys, os

BG = (21, 23, 28)
DIM = (85, 92, 106)
ACC = (244, 185, 66)

def rounded_bar_alpha(px, py, x0, x1, cy, r):
    # signed distance to a horizontal capsule from (x0,cy) to (x1,cy), radius r
    cx = min(max(px, x0), x1)
    d = math.hypot(px - cx, py - cy) - r
    return max(0.0, min(1.0, 0.5 - d))  # 1px antialias

def make(size):
    s = size / 512.0
    bars = [  # x0, x1, cy, radius, color
        (128, 384, 176, 22, DIM),
        (128, 330, 256, 22, DIM),
        (128, 384, 336, 22, ACC),
    ]
    raw = bytearray()
    for y in range(size):
        raw.append(0)
        for x in range(size):
            px, py = (x + 0.5) / s, (y + 0.5) / s
            r, g, b = BG
            for x0, x1, cy, rad, col in bars:
                a = rounded_bar_alpha(px, py, x0, x1, cy, rad)
                if a > 0:
                    r = r + (col[0] - r) * a; g = g + (col[1] - g) * a; b = b + (col[2] - b) * a
            raw += bytes((int(r + 0.5), int(g + 0.5), int(b + 0.5), 255))
    def chunk(t, d):
        return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    return (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 6, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(bytes(raw), 9)) + chunk(b'IEND', b''))

if __name__ == '__main__':
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    for n in (192, 512):
        with open(os.path.join(out, f'icon-{n}.png'), 'wb') as f:
            f.write(make(n))
        print('wrote icon-%d.png' % n)
