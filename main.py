from backend.fetch_candidate_emails import fetch_canditate_emails
from backend.send_email import send_email
from backend.interview_filter import interviews_page_filter_function
from check_assets import check_asset_path_and_fix_size


if __name__ == "__main__":
    # check_asset_path_and_fix_size()
    import sys
    from PyQt6 import QtWidgets, QtGui
    from login_ui import Ui_MainWindow as LoginUI
    from admin_menu_ui import Ui_MainWindow as AdminUI
    from application_menu_ui import Ui_MainWindow as ApplicationsUI
    from mentor_menu_ui import Ui_MainWindow as MentorUI
    from interviews_menu_ui import Ui_MainWindow as InterviewsUI
    from user_menu_ui import Ui_MainWindow as UserUI
    from admin_control_menu_ui import Ui_MainWindow as AdminControlUI
    from application_form_ui_ui import VITForm
    from backend.login import login
    from backend.set_table_data import set_table_data
    from send_email_form_ui import Ui_send_email_form
    from create_user_ui import Ui_create_user
    from backend.create_user import create_user
    from backend.mentor_interview_page_filter import mentor_interview_page_filter
    from backend.app_page_filter import app_page_filter

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginUI()
    admin_menu = AdminUI()
    applications_menu = ApplicationsUI()
    mentor_menu = MentorUI()
    interviews_menu = InterviewsUI()
    user_menu = UserUI()
    admin_control_menu = AdminControlUI()
    new_application_menu = VITForm()
    send_email_menu = Ui_send_email_form()
    create_user_menu = Ui_create_user()

    role = ""

    def get_role(user_role):
        global role
        role = user_role

    def login_menu_setup():
        ui.setupUi(MainWindow)
        ui.login_button.clicked.connect(
            lambda: login(
                ui.lineEdit.text(),
                ui.lineEdit_2.text(),
                ui,
                admin_setup,
                user_setup,
                get_role,
            )
        )
        ui.lineEdit_2.returnPressed.connect(
            lambda: login(
                ui.lineEdit.text(),
                ui.lineEdit_2.text(),
                ui,
                admin_setup,
                user_setup,
                get_role,
            )
        )
        ui.lineEdit.returnPressed.connect(
            lambda: login(
                ui.lineEdit.text(),
                ui.lineEdit_2.text(),
                ui,
                admin_setup,
                user_setup,
                get_role,
            )
        )
        ui.exit_button.clicked.connect(MainWindow.close)
        ui.apply_button.clicked.connect(new_application_setup)

    def admin_setup():
        admin_menu.setupUi(MainWindow)
        admin_menu.applications_Button.clicked.connect(applications_setup)
        admin_menu.Mentor_interview_Button.clicked.connect(mentor_setup)
        admin_menu.interviews_Button.clicked.connect(interviews_menu_setup)
        admin_menu.Admin_menu_Button.clicked.connect(setup_admin_control_menu)
        admin_menu.exit_Button.clicked.connect(MainWindow.close)
        admin_menu.main_menu.clicked.connect(login_menu_setup)

    def applications_setup():
        applications_menu.setupUi(MainWindow)
        set_table_data(applications_menu, "crm", "applications")
        applications_menu.main_menu.clicked.connect(
            (lambda: admin_setup if role == "admin" else user_setup)()
        )
        applications_menu.exit.clicked.connect(MainWindow.close)
        applications_menu.search.clicked.connect(
            lambda: app_page_filter(
                applications_menu.lineEdit.text(), applications_menu, None
            )
        )
        applications_menu.assigned_mentor_interviews.clicked.connect(  # Mentor atananlar
            lambda: app_page_filter(None, applications_menu, "OK")
        )
        applications_menu.unassigned_mentor_interviews.clicked.connect(  # Mentor atananmamis olanlar
            lambda: app_page_filter(None, applications_menu, "ATANMADI")
        )
        applications_menu.all_applications.clicked.connect(  # Butun basvurular
            lambda: app_page_filter(None, applications_menu, None)
        )

        applications_menu.prev_vit_check.clicked.connect(  # Onceki VIT versiyonlarini leri goruntule.
            lambda: app_page_filter(None, applications_menu, "VIT3")
        )
        applications_menu.filtered_applications.clicked.connect(  # her ismi birkez yaz.
            lambda: app_page_filter(None, applications_menu, "UNDUPLICATE")
        )
        applications_menu.duplicate_application.clicked.connect(  # Mekerrer OLANLAR.
            lambda: app_page_filter(None, applications_menu, "DUPLICATE")
        )

    def mentor_setup():
        mentor_menu.setupUi(MainWindow)
        set_table_data(mentor_menu, "crm", "mentors")
        mentor_menu.main_menu.clicked.connect(
            (lambda: admin_setup if role == "admin" else user_setup)()
        )
        mentor_menu.exit_button.clicked.connect(MainWindow.close)
        mentor_menu.filter_select_button.activated.connect(
            lambda: mentor_interview_page_filter(
                mentor_menu.filter_select_button,
                None,
                mentor_menu,
            )
        )
        mentor_menu.all_meetings.clicked.connect(
            lambda: set_table_data(mentor_menu, "crm", "mentors")
        )
        mentor_menu.search_button.clicked.connect(
            lambda: mentor_interview_page_filter(
                None,
                mentor_menu.lineEdit.text(),
                mentor_menu,
            )
        )

    def interviews_menu_setup():
        interviews_menu.setupUi(MainWindow)
        set_table_data(interviews_menu, "crm", "interviews")
        interviews_menu.mainmenu_Button.clicked.connect(
            (lambda: admin_setup if role == "admin" else user_setup)()
        )
        interviews_menu.exit_Button.clicked.connect(MainWindow.close)
        interviews_menu.project_send_Button.clicked.connect(
            lambda: interviews_page_filter_function(
                "Projenin gelis tarihi", None, interviews_menu
            )
        )
        interviews_menu.project_submitted_Button.clicked.connect(
            lambda: interviews_page_filter_function(
                "Proje gonderilis tarihi", None, interviews_menu
            )
        )
        interviews_menu.search_Button.clicked.connect(
            lambda: interviews_page_filter_function(
                None,
                interviews_menu.search_Line.text(),
                interviews_menu,
            )
        )
        interviews_menu.all_interviews.clicked.connect(
            lambda: set_table_data(interviews_menu, "crm", "interviews")
        )

    def user_setup():
        user_menu.setupUi(MainWindow)
        user_menu.app_Button.clicked.connect(applications_setup)
        user_menu.mentor_interview_Button.clicked.connect(mentor_setup)
        user_menu.interviews_Button.clicked.connect(interviews_menu_setup)
        user_menu.exit_Button.clicked.connect(MainWindow.close)

    def setup_admin_control_menu():
        admin_control_menu.setupUi(MainWindow)
        admin_control_menu.main_menu.clicked.connect(admin_setup)
        admin_control_menu.exit.clicked.connect(MainWindow.close)
        admin_control_menu.activity_check.clicked.connect(
            lambda: set_table_data(admin_control_menu, "crm", "activities")
        )
        set_table_data(admin_control_menu, "crm", "activities")
        admin_control_menu.send_email.clicked.connect(send_email_setup)
        admin_control_menu.create_user.clicked.connect(create_user_setup)

    def new_application_setup():
        new_application_menu.show()
        MainWindow.close()

    def send_email_setup():
        admin_control_menu.window = QtWidgets.QWidget()
        admin_control_menu.ui = send_email_menu
        admin_control_menu.ui.setupUi(admin_control_menu.window)
        admin_control_menu.window.show()
        fetch_canditate_emails(send_email_menu.candidate_names, send_email_menu.email)
        send_email_menu.send_button.clicked.connect(
            lambda: send_email(
                send_email_menu.email.text(),
                send_email_menu.textEdit.toPlainText(),
                send_email_menu.subject_input.text(),
            )
        )

    def create_user_setup():
        admin_control_menu.window = QtWidgets.QWidget()
        admin_control_menu.ui = create_user_menu
        admin_control_menu.ui.setupUi(admin_control_menu.window)
        admin_control_menu.window.show()
        create_user_menu.create_button.clicked.connect(
            lambda: create_user(
                create_user_menu.username.text(),
                create_user_menu.password.text(),
                create_user_menu.role.currentText(),
            )
        )

    login_menu_setup()
    MainWindow.show()
    sys.exit(app.exec())
