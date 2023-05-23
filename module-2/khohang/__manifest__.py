{
    'name': "Kho Hang",

    'summary': """Quan ly kho""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Van Hien",


    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'data' : [
        'views/user.xml'
        'views/kho.xml'
        'views/loaihang.xml'
        'views/khachhang.xml'
        'views/nhanvien.xml'
        'views/banggia.xml'
        'views/vitrikho.xml'
        'views/hanghoa.xml'
        'views/hoadonnhap.xml'
        'views/hoadonxuat.xml'
    ],
    'depends': ['base'],
    'installable': True,
    'application': True,
    'auto_install': True,
}