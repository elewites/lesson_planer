# lesson_planer

## Project Description

This project was developed in response to a friend's request and offers the following features:

- **Sentence Collection**: Users can create and manage a repository of sentences.

- **Categorization by Sections**: Sentences can be conveniently organized into sections or categories, making it easy to sort and retrieve specific content.

- **Random Sentence Retrieval**: Users have the ability to retrieve a specified number (N) of random sentences from each section during the app's lifecycle.

- **Structured Word Document**: The project provides users with the capability to generate a Word Document that organizes their selections by displaying sections and the sentences that were chosen randomly within each section.


### What this project cannot do YET:

1. **Deletion of Sentences**: At present, the user cannot delete sentences from the databank. This feature is in my roadmap for integration.

2. **Words Databank**: The user has expressed an interest in also having a databank for words. This will be integrated as well, so user has access to a databank of sentences and a databank of words.

3. **User-Friendly Design**: The current GUI interface might not be the most intuitive for now, and I'm actively working on enhancing its usability.   

## Distribution

If you want explore this project as I distributed it to my friend, particularly someone with no programming knowledge, I tried simplifying the process to the best of my abilities.

Everything related to distrubition can be found in this folder [dist](./dist).

In the [dist](./dist) directory, you'll find two folders: `main` and `main.zip`. They are essentially the same, with one being the compressed version. Grab the compressed `main.zip`. This folder contains everything necessary to run the app, including data storage and usage, output functionality.

```
├── dist
│ ├── main
│ └── main.zip
```

I've bundled the project in this compressed directory: [main.zip](./dist/main.zip). Please follow these steps to use the application:

1. **Download the .zip file**: Download and save the `main.zip` file to your computer.

2. **Extract the Contents**: Unzip the file to access its contents.

3. **Locate the Main Executable**: Inside the extracted folder, you'll find a file named `main.exe`. Double-clicking this executable will start the application.

4. **Finding Your Output**: If you're wondering where the Word Document generated by the app is located, don't worry. In the same main folder, I've included an `output` directory. This is where your Word Document titled `lesson.docx` will be generated every time you select the corresponding functionality within the app's interface.
   

## Starting the Project in "development mode"

If you want to explore this repo as a "programmer" and not a "user", do the following first: 

Clone first, then install dependencies.

### Option One: Run Bash Script
- Run this bash script [x_run_main.sh](./x_run_main.sh) located in the main directory. It will automatically install dependencies and start app. 

### Option Two: Install Dependencies Manually

The project's dependencies are listed in [requirements.txt](./requirements.txt).

To install the dependencies, I recommend first start the virtual environment I was working with [myenv](./myenv).

To activate the virtual environment, navigate to the root directory of the project and run the following command:

```bash
source myenv/Scripts/activate
```
Then proceed to install dependencies (still within root directory):
```bash
pip install requirements.txt
```

This should allow you to run the project in what I refer to as "development mode".

To run simply execute command (from root directory):
```bash
python main.py
```

### Bash Scripts
I have included two bash scripts in root directory. 
1. [x_run_main.sh](./x_run_main.sh): Installs dependencies in virtual environment and starts the application.
2. [x_distribution.sh](./x_distribution.sh): Updates the `dist` package. Script simplifies code updates and project bundling, generating an executable (.exe) file. It places everything in [main](./dist/main) folder inside `dist`. This `main` folder can then be compressed to be shared.

Notice: These scripts were primarily developed and tested for Windows, although I'm aware that cross-platform compatibility is ideal. However, the generated executable [main.exe](./dist/main/main.exe) does run on various platforms.

#### Important Directories

- [data](./data): This is where user data is stored.
- [dist](./dist): Distribution package.
- [myenv](./dist): virtual environment
- [output](./output): The Word Document generated by the app will be written to this directory as `lesson.docx`
- [src](./src): source code

```
├── data
│   ├── data.json
├── dist
├── myenv
├── output
│   ├── lesson.docx
├── src
```

## Source Code: Model-View-Controller design

In this project, I adopted the Model-View-Controller (MVC) design, which was a new approach for me. This decision offered several advantages, such as:
- improved code organization
- enhanced maintainability
- efficient separation of concerns

Where and how is this design structure happening in my code:
1. **View**: [window.py](./src/window.py): This class serves as the View, responsible for assembling interface elements. Event handling is not part of its role.
2. **Controllers**: Multiple controllers are employed to efficiently manage event handling and maintain well-organized code.
     - [main_controller](./src/main_controller.py): serves as base controller and is where branch components are instantiated. This          controller "depends-on" `window.py` as it needs to access the widgets that live in `window.py`. 
     - [upload_sentences_controller](./src/upload_sentences_controller.py)
     - [random_selection_controller](./src/random_selection_controller.py)
     - [view_user_selection_controller](./src/view_user_selection_controller.py)
     - [view_all_stored_data_controller](./src/view_all_stored_data_controller.py)
     - [print_to_word_document_controller](./src/print_to_word_document_controller.py)

This below is not the file/folder structure, it just to depict the compisition of these classes. `main_controller` has an instance of these other controllers. 
  ```
  ├── MainController (depends on window)
      ├── UploadSentencesController
      ├── RandomSelectionController
      ├── ViewUserSelectionController
      ├── ViewAllStoredDataController
      ├── PrintWordDocumentController
  ```

3. **Data Handlers**: In adherence to the MVC pattern, these components represent the Model. They encompass all the essential business logic for data manipulation, including data retrieval, storage, in-memory operations, and access interfaces for controllers.
      - [base_data_handler](./src/data_handlers/base_data_handler.py): Parent class for other data handlers.
      - [json_data_handler](./src/data_handlers/json_data_handler.py): Manages data retrieval and loading from files. Depends on [Serializer](./src/serializer.py) class
      - [user_selection_data_handler](./src/data_handlers/user_selection_data_handler.py): Records user-selected data for later            printing in a Word document.
```
BaseDataHandler
├── JsonDataHandler (depends on Serializer class)
└── UserSelectionDataHandler
```

## Observer Pattern
[controller_observer](./src/controller_observer.py): This abstract class defines a flexible observer interface for monitoring changes in application components, promoting efficient communication and adaptability across various modules.

In my application, I use this pattern to keep controllers informed about changes in data stored in JSON files. This is crucial when controllers like `UploadSentencesController` work with the `JsonDataHandler` to modify data. To achieve this, I've added two essential methods to `BaseDataHandler`: `add_observer` and `_notify_observers`. These methods allow me to set up observers within the `JsonDataHandler`. This way observers of `JsonDataHandler`, which are mostly other controllers, can respond to changes in stored data and update the GUI interface accordingly. 

## Unit Tests

Unit tests can be run with command (from root directory)
```
pytest
```

Unit tests included in project:
1. [test_serializer](./src/test_serializer.py)
2. [test_base_data_handler](./src/data_handlers/test_base_data_handler.py)
3. [test_json_data_handler](./src/data_handlers/test_json_data_handler.py)
4. [test_user_selection_data_handler](./src/data_handlers/test_user_selection_data_handler.py)

  
  
  
       
  





