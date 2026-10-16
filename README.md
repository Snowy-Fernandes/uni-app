# University Enrolment System (CLIUniApp + GUIUniApp)

32555 Fundamentals of Software Development - Assessment 1, Group 10

## Folder layout

```
uni_app/
├── main_cli.py                  command line app
├── gui_app.py                   Streamlit GUI
├── requirements.txt
├── students.data                created automatically, JSON text, shared by CLI and GUI
├── .streamlit/config.toml       theme colours (hidden folder)
├── models/
│   ├── subject.py               Subject: id, mark, grade
│   ├── student.py               Student: details, subjects, average
│   └── database.py              reads and writes students.data
├── controllers/
│   ├── university_controller.py main menu
│   ├── student_controller.py    register, login, course menu
│   └── admin_controller.py      list, group, partition, remove, clear
├── utils/
│   ├── validation.py            email and password rules
│   └── console.py               coloured print and input
└── gui/
    ├── css/                     base.css, cards.css, menu.css
    ├── views/                   dashboard, subjects, results, grade_guide, password
    ├── actions.py               what the buttons do
    ├── cards.py                 overview and subject cards
    ├── charts.py                bar, line and donut charts
    ├── components.py            top bar, banner, clickable card
    ├── dialogs.py               popups
    ├── login_page.py            login page
    ├── sidebar.py               left menu
    ├── styles.py                loads the css files
    └── theme.py                 grade ranges and colours
```

## Rules

- Email: `firstname.lastname@university.com`, letters only, capital letters allowed anywhere.
- Password: starts with a capital letter, at least 5 letters in total, then 3 or more digits (for example `Snowy2004`).

## Run

1. Install Python 3.9 or newer.
2. Open a terminal inside the `uni_app` folder.
3. `pip install -r requirements.txt`
4. CLI: `python main_cli.py`
5. GUI: `streamlit run gui_app.py`

Register a student in the CLI first (Student, then `r`), then log in to the GUI.

## Notes

- `students.data` is plain JSON, so you can open it in VS Code and read it.
- The GUI keeps you logged in when you refresh the page: the login and the current page are kept in the page address.
- Logging out ends that login.
