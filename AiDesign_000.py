import PySimpleGUI as sg 
sg.ChangeLookAndFeel('DarkAmber') 

DefaultWidth = 40

menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],      
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
            ['Bantuan', ['Tentang Kami', 'Bantuan1']], 
            ]   
layout = [      
    [sg.Menu(menu_def, tearoff=True)],      
    #[sg.Text('All graphic widgets in one window!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],   
    [sg.Text('Text Editor', justification='center', size=(DefaultWidth,1),font=("Helvetica",10), relief=sg.RELIEF_RIDGE), 
        sg.T(' '), sg.T(' '),
        sg.Text('Custom Logo', size=(DefaultWidth, 1), justification='center', font=("Helvetica", 10), relief=sg.RELIEF_RIDGE),
        sg.T(' '), sg.T(' '),
        sg.Text('Background Section', size=(DefaultWidth, 1), justification='center', font=("Helvetica", 10), relief=sg.RELIEF_RIDGE),
        ],
    
    [sg.InputText(('Masukkan Judul Besar'),size=(DefaultWidth,2)),
        sg.T(' '), sg.T(' '),
        sg.Text('Logo yang biasa digunakan', size=(DefaultWidth, 1)),
        sg.T(' '), sg.T(' '),
        sg.Text('Pilih Background sesuai kategori', size=(DefaultWidth, 1)),
        ],
    [sg.Checkbox('Shadow Teks Judul', size=(DefaultWidth,1)),
        sg.T(' '),
        sg.Checkbox('Logo AiDesign', size=(DefaultWidth,1), default=True, disabled=True),
        sg.T(' '),
        sg.InputOptionMenu(('-- Pilih Kategori --', 'Alam', 'Kota', 'Malam', 'Sunset', 'Sunrise')),
        ],
    [sg.InputOptionMenu(('-- Pilih Font --', 'Arial', 'Courier')),
        sg.T('   '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '),
        sg.Checkbox('Logo Muslim Designer Community', size=(DefaultWidth,1)),
        sg.T(' '),
        sg.Text('Pilih Background sendiri', size=(DefaultWidth, 1)),
        ],
    [sg.Checkbox('Font Judul Otomatis', size=(DefaultWidth,1), default=True),
        sg.T(' '),
        sg.Checkbox('Logo Yuk Share', size=(DefaultWidth,1)),
        sg.T(' '),
        sg.Text('Background :'), sg.Input(size=(15,1)), sg.FileBrowse()
        ],

    [sg.InputText(('Masukkan Sub Judul Kecil'),size=(DefaultWidth,2)),
        sg.T(' '), sg.T(' '),
        sg.Text('Upload logo sendiri', size=(DefaultWidth, 1))],
    [sg.Checkbox('Shadow Text Kecil', size=(DefaultWidth,1)),
        sg.T(' '),
        sg.Text('Logo 1 ', size=(6, 1)), sg.Input(size=(20,1)), sg.FileBrowse()],
    [sg.InputOptionMenu(('-- Pilih Font --', 'Arial', 'Courier')),
        sg.T('   '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '), sg.T(' '),
        sg.Text('Logo 2 ', size=(6, 1)), sg.Input(size=(20,1)), sg.FileBrowse()],
    [sg.Checkbox('Font Sub Judul Otomatis', size=(DefaultWidth,1), default=True),
        sg.T(' '),
        sg.Text('Logo #Hashtag '), sg.Input(default_text='AiDesign Generator',size=(24,1))],
    [sg.T(' ')],
    [sg.T(' ', size=(45,1)),
        sg.Submit(button_text='Generate Design'),
        sg.T(' ', size=(12,1)),
        sg.Exit(),
        ],
]

layout2 = [
    [sg.Text('Custom Logo', size=(30, 1), justification='center', font=("Helvetica", 15), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Logo yang biasa digunakan')],
    [sg.Checkbox('Logo AiDesign', size=(DefaultWidth,1))],
    [sg.Checkbox('Logo MDC', size=(DefaultWidth,1))],
    [sg.Checkbox('Logo Yuk Share', size=(DefaultWidth,1))],

]

# sg.PopupScrolled('Hallo Semuanya ^^', 
#     'Program ini adalah program gratis.',
#     'Mohon gunakan dengan bijak. Semoga bermanfaat ^^',
#     'Regards : Muhamamd Razif Rizqullah (IG : @Rzf.Gsh)',
#     'More at http://github.com/stacia')

window = sg.Window('AI Design : Your Instant Design Buddy', layout, default_element_size=(DefaultWidth, 1), grab_anywhere=False)      
# window2 = sg.Window('Template Section', layout2, default_element_size=(DefaultWidth, 1), grab_anywhere=False)      
while True:
    event, values = window.read()
    # event2, values2 = window2.read()
    print('-- // -- // -- // --')
    print(event)
    for key,val in values.items():
        print (key, val)
    if event in (None,'Exit'):
        break
    elif event == 'Tentang Kami...':
        sg.PopupScrolled('Tentang Pengembang.', 
            'Program ini adalah program gratis.',
            'Mohon gunakan dengan bijak. Semoga bermanfaat ^^',
            'Regards : Muhamamd Razif Rizqullah (IG : @Rzf.Gsh)',
            'More at http://github.com/stacia')
    elif event == 'Bantuan...':
        sg.Popup('Silahkan kunjungi http://github.com/stacia',
            'Regards : Muhamamd Razif Rizqullah (IG : @Rzf.Gsh)',)
    elif event == 'Generate Design':
        print(event)
        # print(values)
        # print('Judul Besar : ',values[0])
        # print('Sub Judul : ',values[4])