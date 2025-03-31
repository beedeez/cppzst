{
  "targets": [
    {
      "target_name": "compress",
      "type": "static_library",
      "standlone_static_library": 1,
      "defines": [
      ],

      "include_dirs": [
        "zstd/lib",
        "zstd/lib/common",
        "zstd/lib/compress"
      ],

      "sources" : [
'zstd/lib/common/debug.c',
    'zstd/lib/common/entropy_common.c',
    'zstd/lib/common/error_private.c',
    'zstd/lib/common/fse_decompress.c',
    'zstd/lib/common/pool.c',
    'zstd/lib/common/threading.c',
    'zstd/lib/common/xxhash.c',
    'zstd/lib/common/zstd_common.c',

    'zstd/lib/compress/fse_compress.c',
    'zstd/lib/compress/hist.c',
    'zstd/lib/compress/huf_compress.c',
    'zstd/lib/compress/zstd_compress.c',
    'zstd/lib/compress/zstd_compress_literals.c',
    'zstd/lib/compress/zstd_compress_sequences.c',
    'zstd/lib/compress/zstd_compress_superblock.c',
    'zstd/lib/compress/zstd_double_fast.c',
    'zstd/lib/compress/zstd_fast.c',
    'zstd/lib/compress/zstd_lazy.c',
    'zstd/lib/compress/zstd_ldm.c',
    'zstd/lib/compress/zstd_opt.c',
    'zstd/lib/compress/zstdmt_compress.c',

    'zstd/lib/decompress/huf_decompress.c',
    'zstd/lib/decompress/zstd_ddict.c',
    'zstd/lib/decompress/zstd_decompress.c',
    'zstd/lib/decompress/zstd_decompress_block.c',

    'zstd/lib/dictBuilder/cover.c',
    'zstd/lib/dictBuilder/divsufsort.c',
    'zstd/lib/dictBuilder/fastcover.c',
    'zstd/lib/dictBuilder/zdict.c',

    'zstd/lib/legacy/zstd_v07.c',
    'zstd/lib/legacy/zstd_v01.c',
      ],

      "conditions": [
        [
          "OS == 'mac'", {
            "xcode_settings": {
              "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
              "MACOSX_DEPLOYMENT_TARGET": "10.11"
            }
          }
        ],
        [
          'OS=="win"', {
            "sources=" : [
              '<!@(FOR %i IN (zstd/lib/common/*.c)      DO @echo zstd/lib/common/%i)',
              '<!@(FOR %i IN (zstd/lib/compress/*.c)    DO @echo zstd/lib/compress/%i)'
            ]
          }
        ]
      ]
    },
    {
      "target_name": "decompress",
      "type": "static_library",
      "standlone_static_library": 1,
      "defines": [
      ],

      "include_dirs": [
        "zstd/lib",
        "zstd/lib/common",
        "zstd/lib/decompress"
      ],

      "sources" : [
'zstd/lib/common/debug.c',
    'zstd/lib/common/entropy_common.c',
    'zstd/lib/common/error_private.c',
    'zstd/lib/common/fse_decompress.c',
    'zstd/lib/common/pool.c',
    'zstd/lib/common/threading.c',
    'zstd/lib/common/xxhash.c',
    'zstd/lib/common/zstd_common.c',

    'zstd/lib/compress/fse_compress.c',
    'zstd/lib/compress/hist.c',
    'zstd/lib/compress/huf_compress.c',
    'zstd/lib/compress/zstd_compress.c',
    'zstd/lib/compress/zstd_compress_literals.c',
    'zstd/lib/compress/zstd_compress_sequences.c',
    'zstd/lib/compress/zstd_compress_superblock.c',
    'zstd/lib/compress/zstd_double_fast.c',
    'zstd/lib/compress/zstd_fast.c',
    'zstd/lib/compress/zstd_lazy.c',
    'zstd/lib/compress/zstd_ldm.c',
    'zstd/lib/compress/zstd_opt.c',
    'zstd/lib/compress/zstdmt_compress.c',

    'zstd/lib/decompress/huf_decompress.c',
    'zstd/lib/decompress/zstd_ddict.c',
    'zstd/lib/decompress/zstd_decompress.c',
    'zstd/lib/decompress/zstd_decompress_block.c',

    'zstd/lib/dictBuilder/cover.c',
    'zstd/lib/dictBuilder/divsufsort.c',
    'zstd/lib/dictBuilder/fastcover.c',
    'zstd/lib/dictBuilder/zdict.c',

    'zstd/lib/legacy/zstd_v07.c',
    'zstd/lib/legacy/zstd_v01.c',
      ],

      "conditions": [
        [
          "OS == 'mac'", {
            "xcode_settings": {
              "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
              "MACOSX_DEPLOYMENT_TARGET": "10.11"
            }
          }
        ],
        [
          'OS=="win"', {
            "sources=" : [
              '<!@(FOR %i IN (zstd/lib/common/*.c)      DO @echo zstd/lib/common/%i)',
              '<!@(FOR %i IN (zstd/lib/decompress/*.c)  DO @echo zstd/lib/decompress/%i)'
            ]
          }
        ]
      ]
    }
  ]
}
