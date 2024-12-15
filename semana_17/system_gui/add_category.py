import PySimpleGUI as sg

def add_category_window(existing_categories):
    layout = [
        [sg.Text("Enter the Category name")],
        [sg.Input(key="CATEGORY_NAME")],
        [sg.Button("Confirm"), sg.Button("Cancel")]
    ]

    category_window = sg.Window("Add Category", layout)

    while True:  #Infinite loop until exit or X is pressed
        event, values = category_window.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            category_window.close()
            return None  #If cancel or if window close
        elif event == "Confirm":
            category_name = values["CATEGORY_NAME"].strip()  #strip method to delete white spaces

            if not category_name:
                sg.popup_error("Category name cannot be empty, please enter a valid name")
                continue

            if category_name in existing_categories:
                sg.popup_error("Category name cannot be repeated, please enter a valid name")
                continue

            category_window.close()
            return category_name  # Returns it if everything is ok
