import streamlit as st

quiz_data_1 = [
    {
        "question_number": 1,
        "question": "C in CPU denotes",
        "options": ["Central", "Common", "Convenient", "Computer", "None of these"],
        "answer": "Central"
    },
    {
        "question_number": 2,
        "question": "Which of the following uses a handheld operating system?",
        "options": ["supercomputer", "personal computer", "Laptop", "PDA", "None of these"],
        "answer": "PDA"
    },
    {
        "question_number": 3,
        "question": "To display the contents of a folder in Windows Explorer you should",
        "options": ["click on it", "collapse it", "name it", "give it a password", "None of these"],
        "answer": "click on it"
    },
    {
        "question_number": 4,
        "question": "The CPU comprises of Control, Memory and ________ units",
        "options": ["Microprocessor", "Arithmetic/Logic", "Output", "ROM", "None of these"],
        "answer": "Arithmetic/Logic"
    },
    {
        "question_number": 5,
        "question": "_________ is the most important/powerful computer in a typical network",
        "options": ["Desktop", "Network client", "Network server", "Network station", "None of these"],
        "answer": "Network server"
    },
    {
        "question_number": 6,
        "question": "A(n) ________ appearing on a web page opens another document when clicked",
        "options": ["anchor", "URL", "hyperlink", "reference", "None of these"],
        "answer": "hyperlink"
    },
    {
        "question_number": 7,
        "question": "Which of the following refers to the rectangular area for displaying information and running programs?",
        "options": ["Desktop", "Dialog box", "Menu", "Window", "None of these"],
        "answer": "Window"
    },
    {
        "question_number": 8,
        "question": "_________ is a windows utility program that locates and eliminates unncessary fragments and rearranges filed and unused disk space to optimize operations",
        "options": ["Backup", "Disk cleanup", "Disk defragmenter", "Restore", "None of these"],
        "answer": "Disk defragmenter"
    },
    {
        "question_number": 9,
        "question": "Which of the following refers to too much electricity and may cause a voltage surge?",
        "options": ["Anomaly", "Shock", "Spike", "Virus", "None of these"],
        "answer": "Spike"
    },
    {
        "question_number": 10,
        "question": "The software that is used to create text-based documents are referred to as",
        "options": ["word processors", "DBMS", "spreadsheets", "presentation software", "None of these"],
        "answer": "word processors"
    },
    {
        "question_number": 11,
        "question": "A directory within a directory is called",
        "options": ["Mini Directory", "Junior Directory", "Sub Directory", "Part Directory", "None of these"],
        "answer": "Sub Directory"
    },
    {
        "question_number": 12,
        "question": "Which of the following is not an Operating System?",
        "options": ["DOS", "Linux", "Windows", "Oracle", "None of these"],
        "answer": "Oracle"
    },
    {
        "question_number": 13,
        "question": "Which of the following is not a storage medium?",
        "options": ["Hard Disk", "Flash Drive", "DVD", "Scanner", "None of these"],
        "answer": "Scanner"
    },
    {
        "question_number": 14,
        "question": "Which application is commonly used to prepare a presentation/slide show?",
        "options": ["MS-Word", "MS-Excel", "MS-Access", "MS-PowerPoint", "None of these"],
        "answer": "MS-PowerPoint"
    },
    {
        "question_number": 15,
        "question": "Which of the following is not a hardware?",
        "options": ["Processor", "Printer", "Keyboard", "Assembler", "None of these"],
        "answer": "Assembler"
    },
    {
        "question_number": 16,
        "question": "The main circuit board of the system unit is the",
        "options": ["keyboard", "motherboard", "mouse", "monitor", "None of these"],
        "answer": "motherboard"
    },
    {
        "question_number": 17,
        "question": "Where are programs and data kept while the processor is using them?",
        "options": ["Main memory", "Secondary memory", "Disk memory", "Program memory", "None of these"],
        "answer": "Main memory"
    },
    {
        "question_number": 18,
        "question": "________ is a collection of data that is stored electronically as a series of records in a table",
        "options": ["Spreadsheet", "Presentation", "Database", "Word processing", "None of these"],
        "answer": "Database"
    },
    {
        "question_number": 19,
        "question": "Which of the following is application software?",
        "options": ["MS Word", "Windows 7", "Linux", "MAC OS X", "None of these"],
        "answer": "MS Word"
    },
    {
        "question_number": 20,
        "question": "What is the permanent memory built into your computer called?",
        "options": ["RAM", "ROM", "CPU", "CD-ROM", "None of these"],
        "answer": "ROM"
    },
    {
        "question_number": 21,
        "question": "The ability to recover and read deleted or damaged files from a criminal's computer is an example of a law enforcement specialty called",
        "options": ["robotics", "simulation", "animation", "computer forensics", "None of these"],
        "answer": "computer forensics"
    },
    {
        "question_number": 22,
        "question": "Which device is required for the Internet access?",
        "options": ["CD-Drive", "Modem", "NIC", "DVD-Drive", "None of these"],
        "answer": "Modem"
    },
    {
        "question_number": 23,
        "question": "Which of the following is used as a primary storage device?",
        "options": ["Magnetic tape", "Floppy Disk", "Optical Disks", "Magnetic drum", "None of these"],
        "answer": "Magnetic drum"
    },
    {
        "question_number": 24,
        "question": "Full form of URL is",
        "options": ["Uniform Resource Locator", "Uniform Resource Link", "Uniform Registered Link", "Unified Resource Link", "None of these"],
        "answer": "Uniform Resource Locator"
    },
    {
        "question_number": 25,
        "question": "Which of the following has the smallest storage capacity?",
        "options": ["Floppy disk", "CD ROM", "Hard Disk", "Data cartridge", "None of these"],
        "answer": "Floppy disk"
    }
]

quiz_data_2 = [
    {
        "question_number": 1,
        "question": "The software application that is used the most often is .......................",
        "options": ["Word Processing", "Spreadsheet", "Publishing", "Databases", "Presentations"],
        "answer": "Word Processing"
    },
    {
        "question_number": 2,
        "question": "Input, processing, output and storage are the steps in the .......................",
        "options": ["Information Cycle", "Information Processing Cycle", "Data Cycle", "Data Processing Cycle"],
        "answer": "Information Processing Cycle"
    },
    {
        "question_number": 3,
        "question": "The most commonly used input device is the .......................",
        "options": ["Mouse", "Keyboard", "Joystick", "Scanner"],
        "answer": "Keyboard"
    },
    {
        "question_number": 4,
        "question": "CPU stands for .......................",
        "options": ["Central Packet Unit", "Core Processing Unit", "Central Processing Unit", "Central Product Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question_number": 5,
        "question": "Which of the following is NOT a type of printer? .......................",
        "options": ["Dot-Matrix", "Inkjet", "Portrait", "Laser"],
        "answer": "Portrait"
    },
    {
        "question_number": 6,
        "question": "The equipment that makes up the computer .......................",
        "options": ["Software", "System Unit", "Hardware", "CPU", "RAM"],
        "answer": "Hardware"
    },
    {
        "question_number": 7,
        "question": "A set of instructions that tells the computer how to perform a task. ..............",
        "options": ["BIOS", "Mouse", "Hard Drive", "Software", "Input"],
        "answer": "Software"
    },
    {
        "question_number": 8,
        "question": "Software designed to do a specific task like word processing or spreadsheets.",
        "options": ["Application Software", "System Software", "Operating System", "Monitor", "Keyboard"],
        "answer": "Application Software"
    },
    {
        "question_number": 9,
        "question": "Software that manages the hardware & the other software on your computer",
        "options": ["BIOS", "Operating System", "RAM", "CPU", "CD-ROM"],
        "answer": "Operating System"
    },
    {
        "question_number": 10,
        "question": "The process of communicating with the computer.",
        "options": ["Software", "Output", "DVD", "Storage", "Input"],
        "answer": "Input"
    },
    {
        "question_number": 11,
        "question": "The result of the work done by your computer.",
        "options": ["Storage", "Output", "Processing", "Input", "Software"],
        "answer": "Output"
    },
    {
        "question_number": 12,
        "question": "The actions performed by a computer to manipulate data.",
        "options": ["Input", "Output", "Power Supply", "Processing", "Saving"],
        "answer": "Processing"
    },
    {
        "question_number": 13,
        "question": "Printers that have nozzles that spray ink on the paper.",
        "options": ["Inkjet", "Portrait", "Laser", "Dot-Matrix", "Multi-functional"],
        "answer": "Inkjet"
    },
    {
        "question_number": 14,
        "question": "Printers that are similar to copiers.",
        "options": ["Multifunctional", "Inkjet", "Laser", "Dot-Matrix", "Landscape"],
        "answer": "Laser"
    },
    {
        "question_number": 15,
        "question": "The brain of the computer.",
        "options": ["Brainette", "CD-ROM", "Hard Drive", "CPU", "FSU"],
        "answer": "CPU"
    },
    {
        "question_number": 16,
        "question": "Other hardware, like the keyboard or monitor, plugs into this.",
        "options": ["Motherboard", "DVD", "System Unit", "CPU", "Port"],
        "answer": "Port"
    },
    {
        "question_number": 17,
        "question": "Memory that can read and write, but is lost when the computer is turned off.",
        "options": ["ROM", "RAM", "EPROM", "PROM"],
        "answer": "RAM"
    },
    {
        "question_number": 18,
        "question": "Contains the disk drives and stores the processor.",
        "options": ["CPU", "System Unit", "Keyboard", "Motherboard", "Bag"],
        "answer": "System Unit"
    },
    {
        "question_number": 19,
        "question": "Hand-held device that controls the pointer on the screen.",
        "options": ["Keyboard", "Mouse", "Scanner", "Printer", "Speakers"],
        "answer": "Mouse"
    },
    {
        "question_number": 20,
        "question": "Magnetic cylinders on which information in the computer is store.",
        "options": ["DVD", "Thumb Drive", "Hard Drive", "CD", "Zip Disk"],
        "answer": "Hard Drive"
    },
    {
        "question_number": 21,
        "question": "The desktop contains small graphics called",
        "options": ["windows", "logos", "icons", "pictures", "None of these"],
        "answer": "icons"
    },
    {
        "question_number": 22,
        "question": "Which key is used in combination with another key to perform a specific task?",
        "options": ["Function", "Control", "Arrow", "Space Bar", "None of these"],
        "answer": "Control"
    },
    {
        "question_number": 23,
        "question": "Extension of a word file in MS-Office-2007 is",
        "options": [".doc", ".docx", ".docxs", "All the above", "None of these"],
        "answer": ".docx"
    },
    {
        "question_number": 24,
        "question": "What is Outlook Express?",
        "options": ["Scheduler", "E-mail client", "Address Book", "All the above", "None of these"],
        "answer": "E-mail client"
    },
    {
        "question_number": 25,
        "question": "In which of the following topologies, there are n devices in a network and each device has (n ⎯ 1) parts for cables?",
        "options": ["Mesh", "Star", "Ring", "Bus", "None of these"],
        "answer": "Mesh"
    },
    {
        "question_number": 26,
        "question": "Which of the following items is not used in local area network (LAN)?",
        "options": ["Computer", "Modem", "Printer", "Cable", "Connector"],
        "answer": "Modem"
    },
    {
        "question_number": 27,
        "question": "When sending an e-mail, the _________ line describes the content of the message?",
        "options": ["To", "CC", "Contents", "BCC", "Subject"],
        "answer": "Subject"
    },
    {
        "question_number": 28,
        "question": "What is the keyboard shortcut for creating chart from the selected cell range?",
        "options": ["F2", "F4", "F8", "F10", "F11"],
        "answer": "F11"
    },
    {
        "question_number": 29,
        "question": "The power of a spreadsheet lies in its",
        "options": ["Cells", "Formulas", "Labels", "Worksheets", "Rows and Coloumns"],
        "answer": "Formulas"
    },
    {
        "question_number": 30,
        "question": "IP address consists of how many bits?",
        "options": ["16 bits", "8 bits", "30 bits", "36 bits", "None of these"],
        "answer": "None of these"
    }]


quiz_data_3 =[
    {
        "question_number": 1,
        "question": "This person develops software that the computer uses to process data into information.",
        "options": ["Director", "Program manager", "Programmer", "User"],
        "answer": "Programmer"
    },
    {
        "question_number": 2,
        "question": "This system contains billions of documents called Web pages.",
        "options": ["World Wide Web", "Telnet", "Newsnet", "Web server"],
        "answer": "World Wide Web"
    },
    {
        "question_number": 3,
        "question": "What is it called when a computer connects to a network?",
        "options": ["Linked", "Inline", "Resourced", "Online"],
        "answer": "Online"
    },
    {
        "question_number": 4,
        "question": "Which one of these is a light, portable, storage device that can hold billions of characters?",
        "options": ["CD Drive", "USB Flash Drive", "DVD Drive", "Hard Drive"],
        "answer": "USB Flash Drive"
    },
    {
        "question_number": 5,
        "question": "Which of these give the computer instructions on what to do and how to do it?",
        "options": ["Website", "Software", "Server", "Hardware"],
        "answer": "Software"
    },
    {
        "question_number": 6,
        "question": "This term mean using communication technologies for the purpose of harming another person.",
        "options": ["Netiquette", "Emoticon", "Cyberbullying", "Podcasting"],
        "answer": "Cyberbullying"
    },
    {
        "question_number": 7,
        "question": "This behavior is socially acceptable in an online or digital situation.",
        "options": ["Netiquette", "Emoticon", "Cyberbullying", "Podcasting"],
        "answer": "Netiquette"
    },
    {
        "question_number": 8,
        "question": "It is legal to download copyrighted music only if the song's copyright holder has granted permission for users to download and play the song.",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "question_number": 9,
        "question": "A portable media player allows users to exchange messages with other connected users.",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question_number": 10,
        "question": "An entertainment Web site contains factual information.",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question_number": 11,
        "question": "A game console is a mobile computing device designed for single-player or multiplayer video games.",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "question_number": 12,
        "question": "Computers do not come with system software already installed",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question_number": 13,
        "question": "Which of the following is an Electronic Medical Gadget?",
        "options": ["Frenzel Goggles", "Electronic Wheel Chair", "Computer Tomography Scanner", "All of the above", "None of the above"],
        "answer": "All of the above"
    },
    {
        "question_number": 14,
        "question": "This is an electronic device that can accept and manipulate data to produce a meaningful information.",
        "options": ["Input device", "Processing device", "Output device", "Storage media"],
        "answer": "Processing device"
    },
    {
        "question_number": 15,
        "question": "ASDF JKL; of the keyboard are called _____.",
        "options": ["Finger keys", "Home keys", "Middle keys", "All of the above", "None of the above"],
        "answer": "Home keys"
    },
    {
        "question_number": 16,
        "question": "Which menu will allow me to undo a mistake I made?",
        "options": ["Edit menu", "Window menu", "Format menu", "Help menu"],
        "answer": "Edit menu"
    },
    {
        "question_number": 17,
        "question": "What is the first step when you want to change the format of text?",
        "options": ["Rename it", "Highlight it", "Erase it", "Type your answer again"],
        "answer": "Highlight it"
    },
    {
        "question_number": 18,
        "question": "Which application would I use to type a letter to my teacher?",
        "options": ["Spreadsheet", "Word processing", "Internet"],
        "answer": "Word processing"
    },
    {
        "question_number": 19,
        "question": "How do you know a word is a link on a website?",
        "options": ["It tuns green", "It turns into a hand", "It smiles"],
        "answer": "It turns into a hand"
    },
    {
        "question_number": 20,
        "question": "What is the name of the bar which contains the name of your document?",
        "options": ["Menu bar", "Toolbar", "Dock", "Title bar"],
        "answer": "Title bar"
    },
    {
        "question_number": 21,
        "question": "Organizing and saving files to the correct place on a computer is called ..",
        "options": ["Drag and drop", "Copy and paste", "File management"],
        "answer": "File management"
    },
    {
        "question_number": 22,
        "question": "What is the name of the toolbar which contains the line tool?",
        "options": ["Menu bar", "Drawing toolbar", "Standard toolbar", "Title bar"],
        "answer": "Drawing toolbar"
    },
    {
        "question_number": 23,
        "question": "Which menu could you use to search for directions on how to complete a task on the computer?",
        "options": ["Help menu", "Edit menu", "File menu", "Window menu"],
        "answer": "Help menu"
    },
    {
        "question_number": 24,
        "question": "What is the name of the gray bar which runs across the top of every application?",
        "options": ["Title bar", "Menu bar", "Toolbar", "Drawing bar"],
        "answer": "Title bar"
    },
    {
        "question_number": 25,
        "question": "If you cannot \"see\" a toolbar, which menu will help you see what is missing?",
        "options": ["View menu", "Menu bar", "Title bar", "Edit menu"],
        "answer": "View menu"
    },
    {
        "question_number": 26,
        "question": "Which menu will help you change the way something looks?",
        "options": ["Edit menu", "Window menu", "Format menu", "Tools menu"],
        "answer": "Format menu"
    },
    {
        "question_number": 27,
        "question": "Which extension would give you a graphic that is on a transparent background?",
        "options": [".jpg", ".png", ".gif", ".xls"],
        "answer": ".png"
    },
    {
        "question_number": 28,
        "question": "Which application would I use to create a graph of my data?",
        "options": ["Spreadsheet", "Word processing", "Internet"],
        "answer": "Spreadsheet"
    },
    {
        "question_number": 29,
        "question": "In which window can you display the available hard drive space most quickly?",
        "options": ["System Properties", "My Computer", "My Documents"],
        "answer": "My Computer"
    },
    {
        "question_number": 30,
        "question": "What are documents, drawings, and programs stored on the hard drive called?",
        "options": ["Folders", "Files", "Folder properties", "DVD"],
        "answer": "Files"
    }
]

quiz_data_4 = [
    {
        "question_number": 1,
        "question": "Are spaces allowed in web addresses?",
        "options": ["Yes, but only between two letters", "Yes", "No"],
        "answer": "No"
    },
    {
        "question_number": 2,
        "question": "What is jumping from one website to another called?",
        "options": ["Leaping", "Hyperlinking", "Surfing"],
        "answer": "Surfing"
    },
    {
        "question_number": 3,
        "question": "What kinds of printers are there?",
        "options": ["Laser printers and modem printers", "Laser printers and inkjet printers", "Laser printers and typex printers"],
        "answer": "Laser printers and inkjet printers"
    },
    {
        "question_number": 4,
        "question": "Is www.visualsteps@com a proper web address?",
        "options": ["Yes, this address is correct. As a result of the @ symbol, the first web page is immediately opened", "No, because the dot should be replaced by an @ symbol", "No, because the @ should be replaced by a dot"],
        "answer": "No, because the @ should be replaced by a dot"
    },
    {
        "question_number": 5,
        "question": "What does downloading from the Internet mean?",
        "options": ["Retrieving files from the Internet", "Lowering your game level on the Internet", "Viewing web pages on the Internet"],
        "answer": "Retrieving files from the Internet"
    },
    {
        "question_number": 6,
        "question": "What does a green wavy line under a word or phrase in the document mean in Microsoft Word?",
        "options": ["The word or phrase might be misspelled", "The word or phrase might contain a grammatical error", "The word or phrase has been copied to the clipboard"],
        "answer": "The word or phrase might contain a grammatical error"
    },
    {
        "question_number": 7,
        "question": "What is a search engine?",
        "options": ["A program that monitors your surfing behavior on the Internet", "A website where you can type in key words and search for them in millions of web pages", "A website where you can click on hundreds of categorized web addresses"],
        "answer": "A website where you can type in key words and search for them in millions of web pages"
    },
    {
        "question_number": 8,
        "question": "Which device connects your computer to the Internet?",
        "options": ["Telephone table", "Modem", "Hard drive", "CD rom"],
        "answer": "Modem"
    },
    {
        "question_number": 9,
        "question": "What ribbon do you use to change margins?",
        "options": ["Page Layout", "View", "Home", "Insert"],
        "answer": "Page Layout"
    },
    {
        "question_number": 10,
        "question": "What does WWW mean?",
        "options": ["Web World Works", "World Wide Web", "World Wide Watch", "World Wrestling Federation"],
        "answer": "World Wide Web"
    },
    {
        "question_number": 11,
        "question": "If you’re connected to the Internet, you are:",
        "options": ["Outline", "Offline", "Online"],
        "answer": "Online"
    },
    {
        "question_number": 12,
        "question": "In Microsoft Word 2007, a squiggly red line under a word means",
        "options": ["Check your grammer", "Word does not have a synonym match", "The word is misspelled", "The dictionary is full"],
        "answer": "The word is misspelled"
    },
    {
        "question_number": 13,
        "question": "What is the 1 shortcut key in Microsoft Word that will start the spellcheck feature automatically?",
        "options": ["F5", "F4", "F7", "F2"],
        "answer": "F7"
    },
    {
        "question_number": 14,
        "question": "On what tool bar do you need to be on to select the ruler?",
        "options": ["Home", "Developer", "Page Layout", "View"],
        "answer": "View"
    },
    {
        "question_number": 15,
        "question": "What page view can you use to see what it will look like when printed?",
        "options": ["Draft View", "Outline View", "Print View", "Reading View"],
        "answer": "Print View"
    },
    {
        "question_number": 16,
        "question": "The ribbon consists of a series of ___________ which contains groups of tools related to specific tasks.",
        "options": ["Files", "Tabs", "Dialog Boxes", "Task Panes"],
        "answer": "Tabs"
    },
    {
        "question_number": 17,
        "question": "The prefix kilo, as in kilobyte, stands for what number?",
        "options": ["10,000", "100", "1,000,000", "1,000"],
        "answer": "1,000"
    },
    {
        "question_number": 18,
        "question": "To get help using Word, click the Help icon on the ribbon or press the F1 key.",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "question_number": 19,
        "question": "A ___________ is a document that provides a preformatted layout for text and graphics, as well as some content.",
        "options": ["Wizard", "Template", "Letter", "Thumbnail"],
        "answer": "Template"
    },
    {
        "question_number": 20,
        "question": "The first time you save a document in word you must name the file.",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "question_number": 21,
        "question": "After selecting text, use the ___________ and ___________ commands to move the text to a different location.",
        "options": ["Copy; Paste", "Cut; Repeat", "Copy; Paste Special", "Cut; Paste"],
        "answer": "Cut; Paste"
    },
    {
        "question_number": 22,
        "question": "With regards to storing information, can you create a folder within a folder?",
        "options": ["Yes", "No", "It depends on the folder size"],
        "answer": "Yes"
    },
    {
        "question_number": 23,
        "question": "In Word 07, you can only undo the last change made to the document.",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question_number": 24,
        "question": "In Word, a quick way to change all the instances of the word beautiful with the word picturesque is to use the ___________ feature.",
        "options": ["Find and Replace", "Thesaurus", "Document Information", "Properties"],
        "answer": "Find and Replace"
    },
    {
        "question_number": 25,
        "question": "In Microsoft Word, to insert a word into the middle of a sentence....",
        "options": ["Move the cursor to the desired location in the sentence and type the new word", "Move the cursor to the desired location in the sentence, press Enter key, and type the new word", "Move the cursor to the beginning of the sentence and start typing", "Retype the whole sentence"],
        "answer": "Move the cursor to the desired location in the sentence and type the new word"
    },
    {
        "question_number": 26,
        "question": "In Microsoft word, the arrow keys can be used to",
        "options": ["Move the cursor in the text that has already been entered", "Delete text", "Save the document", "Move the cursor while deleting text"],
        "answer": "Move the cursor in the text that has already been entered"
    },
    {
        "question_number": 27,
        "question": "The Standard Toolbar",
        "options": ["Provides a list of pull-down menu names", "Displays information about commands being selected", "Is used to execute commonly performed actions.", "Is used to bring hidden parts of a document into view."],
        "answer": "Is used to execute commonly performed actions."
    }
]

quiz_data_5 = [
    {
        "question_number": 1,
        "question": "IF THERE ARE TOO MANY NUMBERS AFTER A DECIMAL IN A CELL WHAT CAN YOU DO TO VIEW THE MISSING NUMBERS",
        "options": ["SCROLL IN THE CELL", "DECREASE THE COLUMN WIDTH", "REENTER THE NUMBERS", "NONE OF THE ABOVE"],
        "answer": "NONE OF THE ABOVE"
    },
    {
        "question_number": 2,
        "question": "ONCE YOU HIDE A ROW IT REMAINS HIDDEN AS LONG AS THE WORKBOOK IS ACTIVE",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "question_number": 3,
        "question": "THE NAME BOX SHOWS YOU THE CONTENT OF THE CELL",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question_number": 4,
        "question": "AN EXCEL WORKSHEET IS",
        "options": ["A PAGE WITH RECTANGLES", "A TABLE OF DATA ORGANIZED IN ROWS AND COLUMNS", "A GRAPH", "NONE OF THE ABOVE"],
        "answer": "A TABLE OF DATA ORGANIZED IN ROWS AND COLUMNS"
    },
    {
        "question_number": 5,
        "question": "HOW DO YOU KNOW WHICH CELL IN EXCEL IS THE ACTIVE ONE (THE ONE YOU ARE WORKING IN)",
        "options": ["A DOTTED BORDER", "BOLD TEXT", "A BLINKING BORDER", "A SOLID DARK, WIDE BORDER"],
        "answer": "A SOLID DARK, WIDE BORDER"
    },
    {
        "question_number": 6,
        "question": "WHEN YOU PRESS 'ENTER' IN EXCEL IT WILL MOVE ONE COLUMN TO THE LEFT",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question_number": 7,
        "question": "WHAT DO YOU TYPE IN EXCEL TO START A FORMULA",
        "options": ["/", "*", "START FORMULA", "="],
        "answer": "="
    },
    {
        "question_number": 8,
        "question": "'CTRL B' IS A SHORTCUT FOR",
        "options": ["ADDING A BORDER", "GOING BACKWARDS", "BOLDING TEXT", "NONE OF THE ABOVE"],
        "answer": "BOLDING TEXT"
    },
    {
        "question_number": 9,
        "question": "YOU CANNOT EDIT DATA ONCE YOU HAVE EXITED THE CELL YOU ENTERED IT IN",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question_number": 10,
        "question": "MAIL MERGE ALLOWS YOU TO SEND THE SAME LETTER TO THE SAME PERSON",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question_number": 11,
        "question": "A MAIL MERGE LIST CAN CONTAIN MULTIPLE ADDRESSES BUT NOT MULTIPLE RECORDS (PEOPLE)",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question_number": 12,
        "question": "TO ACCESS THE MAIL MERGE TASK PANE YOU MUST CLICK TOOLS, AND ON THE TOOLS MENU YOU MUST CLICK 'MAIL MERGE'",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question_number": 13,
        "question": "WHICH OF THE FOLLOWING ALLOWS YOU TO POSITION THE DATA CORRECTLY IN A MAIL MERGE?",
        "options": ["INSERT", "ENTER KEY", "PLACEHOLDERS", "NONE OF THE ABOVE"],
        "answer": "PLACEHOLDERS"
    },
    {
        "question_number": 14,
        "question": "WHAT ITEMS ARE MERGED DURING A MAIL MERGE?",
        "options": ["A WEB PAGE AND A MAILING LIST", "AN EMAIL AND A MAILING LIST", "AN EMAIL AND A WORD DOCUMENT", "NONE OF THE ABOVE"],
        "answer": "NONE OF THE ABOVE"
    },
    {
        "question_number": 15,
        "question": "MAIL MERGE MERGES A DOCUMENT WITH A MAILING LIST",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "question_number": 16,
        "question": "UNLIKE EXCEL, OTHER SPREADSHEET SOFTWARE HAVE LIMITATIONS BECAUSE THEY",
        "options": ["USE THIN DATA", "ARE A FLAT FILE", "JUST DON'T WORK", "KEEP MISSPELLING DRINKWATER"],
        "answer": "ARE A FLAT FILE"
    },
    {
        "question_number": 17,
        "question": "A POWERPOINT PRESENTATION IS MADE UP OF A SERIES OF",
        "options": ["COOPER'S EYE GLASS LENS", "SLIDES", "LAYOUTS", "PICTURES"],
        "answer": "SLIDES"
    },
    {
        "question_number": 18,
        "question": "IN EXCEL 'EURO' IS A",
        "options": ["FORMULA", "CELL NAME", "DATA TYPE", "NONE OF THE ABOVE"],
        "answer": "DATA TYPE"
    },
    {
        "question_number": 19,
        "question": "WHICH MICROSOFT OFFICE PROGRAMS/SOFTWARES HAVE THE RIBBON",
        "options": ["WORD", "EXCEL", "ACCESS", "POWERPOINT", "ALL OF THE ABOVE"],
        "answer": "ALL OF THE ABOVE"
    },
    {
        "question_number": 20,
        "question": "IN MSWORD WHICH TOOLBAR DO I USE TO INSERT A HEADER?",
        "options": ["MAILINGS", "VIEW", "HOME", "NONE OF THE ABOVE"],
        "answer": "NONE OF THE ABOVE"
    },
    {
        "question_number": 21,
        "question": "YOU CAN INSERT A HEADER IN MSWORD BUY USING THE 'HEADER' BUTTON ON THE _______________ TAB (one word)",
        "options": ["insert","format","view"],
        "answer": "insert"
    },
    {
        "question_number": 22,
        "question": "IN EXCEL A QUICK WAY TO ADD UP NUMBERS IN A COLUMN WOULD BE TO CLICK ON / IN THE CELL BELOW THE COLUMN OF NUMBERS AND THEN",
        "options": ["WAIT FOR THE TOTAL TO SHOW", "ASK MOSES TO ADD IT UP FOR YOU", "CLICK THE EQUAL SIGN", "CLICK THE AUTOSUM BUTTON ON THE STANDARD TOOLBAR"],
        "answer": "CLICK THE AUTOSUM BUTTON ON THE STANDARD TOOLBAR"
    },
    {
        "question_number": 23,
        "question": "EXCEL HAS A LIMITED AMOUNT OF DATA THAT CAN BE ORGANIZED IN A SPREADSHEET (think carefully)",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question_number": 24,
        "question": "WHEN A CELL SHOWS '#######' IN IT, IT USUALLY MEANS",
        "options": ["JOHN AND CHRIS ARE PLAYING TICK-TAC-TOE", "THERE IS NO DATA IN THE CELL", "THE CELL WIDTH NEEDS TO BE ADJUSTED TO SHOW THE DATA", "THE DATA IN THE CELL IS MISSPELLED"],
        "answer": "THE CELL WIDTH NEEDS TO BE ADJUSTED TO SHOW THE DATA"
    }
]

quiz_data_6 = [
    {
        "question_number": 1,
        "question": "The Internet is just made up of many other networks all interacting together.",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "question_number": 2,
        "question": "The purpose of a web browser is what?",
        "options": ["To do internet searches.", "Search for cob webs in your house", "Is to display web page from websites"],
        "answer": "Is to display web page from websites"
    },
    {
        "question_number": 3,
        "question": "What does ISP stand for?",
        "options": ["Internet Service Provider", "Internet Service Protection", "Internet Signal Piping"],
        "answer": "Internet Service Provider"
    },
    {
        "question_number": 4,
        "question": "A group of related web pages form",
        "options": ["Www", "Html", "Website", "Home page"],
        "answer": "Website"
    },
    {
        "question_number": 5,
        "question": "The Internet and World Wide Web is really the same thing",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "question_number": 6,
        "question": "What is the language used to build web pages?",
        "options": ["Http", "Www", "Html", "Url"],
        "answer": "Html"
    },
    {
        "question_number": 7,
        "question": "Which of the following is considered a Directory/Index Internet search engine?",
        "options": ["Google", "Yahoo", "Ask Jeeves", "Dogpile"],
        "answer": "Yahoo"
    },
    {
        "question_number": 8,
        "question": "Which of the following Top Level Domain is considered the MOST credible?",
        "options": [".org", ".biz", ".com", ".edu"],
        "answer": ".edu"
    },
    {
        "question_number": 9,
        "question": "A firewall is the name used for software that restricts the access to certain Internet content.",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "question_number": 10,
        "question": "Online fights using electronic messages with angry and vulgar language is called what?",
        "options": ["Impersonation", "Cyberbullying", "Flaming"],
        "answer": "Flaming"
    },
    {
        "question_number": 11,
        "question": "Which one should you never do in a cyberbullying situation?",
        "options": ["Tell a responsable adult", "Block harmful messages", "Respond to the messages in an angry way"],
        "answer": "Respond to the messages in an angry way"
    },
    {
        "question_number": 12,
        "question": "Which screenname is the most dangerous for a child to have?",
        "options": ["Basketballstar19", "Carlvr1232", "Dave93_CA"],
        "answer": "Dave93_CA"
    },
    {
        "question_number": 13,
        "question": "What is the use of information and communication technologies to support deliberate, repeated, and hostile behavior by an individual or group, that is intended to harm others?",
        "options": ["Hacking", "Cyberbullying", "Predator"],
        "answer": "Cyberbullying"
    },
    {
        "question_number": 14,
        "question": "All of the following are forms of technology used to cyberbully except:",
        "options": ["E-Mails", "Instant Messaging", "Web Pages", "Television"],
        "answer": "Television"
    },
    {
        "question_number": 15,
        "question": "What technology do teens use the most for cyberbullying?",
        "options": ["Email", "Cell Phones", "Instant Messages", "Mail"],
        "answer": "Cell Phones"
    },
    {
        "question_number": 16,
        "question": "To be safer, what should you do if you post pictures online?",
        "options": ["Have a picture of only yourself", "Blur the pictures", "Have everyone in the picture tagged with their full name"],
        "answer": "Blur the pictures"
    },
    {
        "question_number": 17,
        "question": "What is the safest things to do in public chatrooms?",
        "options": ["Don't invite anyone to them", "Make a screen name that has nothing to do with yourself", "Block any unknown people that talk to you", "Don't say a word"],
        "answer": "Block any unknown people that talk to you"
    },
    {
        "question_number": 18,
        "question": "What is one of the problems that makes cyberbullying easy?",
        "options": ["Computers are in a teen's private room which keeps their parents from seeing the problem", "The bully doesn't think that it makes more of an impact since it is over the internet", "The bully doesn't have to see the victim's reaction to being bullie", "Online predators are very good at grooming them into talking to the"],
        "answer": "Computers are in a teen's private room which keeps their parents from seeing the problem"
    },
    {
        "question_number": 19,
        "question": "Schools and businesses most often connect to the Internet through a __________.",
        "options": ["Firewall", "LAN (Local Area Network)", "Internet Service Provider", "World Wide Web"],
        "answer": "LAN (Local Area Network)"
    },
    {
        "question_number": 20,
        "question": "All computers are identified with a 4 digit number separated by periods. This is called",
        "options": ["Domain name", "Host name", "Ip address"],
        "answer": "Ip address"
    },
    {
        "question_number": 21,
        "question": "Which of the following domains is LEAST reliable?",
        "options": [".edu", ".net", ".gov"],
        "answer": ".net"
    },
    {
        "question_number": 22,
        "question": "The .com domain web sites are",
        "options": ["Government Institutions", "Business or other mixed sites.", "Non-profit Institutions", "Education Institutions"],
        "answer": "Business or other mixed sites."
    },
    {
        "question_number": 23,
        "question": "The .org domains",
        "options": ["Contain reputable non-profit organizations with reliable information always.", "Are always non-profit organizations that are reputable.", "Contain only advocacy group web sites with political agendas", "Must be evaluated well because this domain contains both very reputable non-profit organization web sites and advocacy groups with hidden agendas"],
        "answer": "Must be evaluated well because this domain contains both very reputable non-profit organization web sites and advocacy groups with hidden agendas"
    },
    {
        "question_number": 24,
        "question": "If the web site has an author and looks professional",
        "options": ["You should look at the domain", "You should expect good research", "You should research the author, look at the domain, check the links, check for errors, look for bias, etc."],
        "answer": "You should research the author, look at the domain, check the links, check for errors, look for bias, etc."
    },
    {
        "question_number": 25,
        "question": "Which of the following are considered a meta search engine?",
        "options": ["Dogpile", "Yahoo", "Google"],
        "answer": "Dogpile"
    },
    {
        "question_number": 26,
        "question": "All of the following are BOOLEAN operators used in Google EXCEPT",
        "options": ["But", "And", "Or", "And Not"],
        "answer": "But"
    },
    {
        "question_number": 27,
        "question": "The language of the Internet, allowing cross-network communication",
        "options": ["TCP/IP", "Internetworking", "ISP", "Router"],
        "answer": "TCP/IP"
    },
    {
        "question_number": 28,
        "question": "Web entry station that offer quick and easy access to a variety of general- interest links",
        "options": ["Portals", "Consumer portals", "Corporate portals", "Vertical portals"],
        "answer": "Portals"
    }]

quiz_data_7 = [
    {
        "question_number": 1,
        "question": "Unsolicited emails are called",
        "options": ["Spams", "Viruses", "Trojans", "Spyware"],
        "answer": "Spams"
    },
    {
        "question_number": 2,
        "question": "Doing a Search on the Internet using the Boolean Operator of \"OR\" will find all websites that",
        "options": ["Contain all keywords used", "Contain one or the other keywords", "Contain all BUT the keywords"],
        "answer": "Contain one or the other keywords"
    },
    {
        "question_number": 3,
        "question": "On an excel sheet the active cell in indicated by ?",
        "options": ["A dotted border", "A dark wide border", "A blinking border", "By italic text"],
        "answer": "A dark wide border"
    },
    {
        "question_number": 4,
        "question": "What term describes explanatory text attached to a cell ?",
        "options": ["Context", "Callout", "Comment", "Dialog"],
        "answer": "Comment"
    },
    {
        "question_number": 5,
        "question": "How we can view a cell comment ?",
        "options": ["position the mouse pointer over the cell", "click the comment command on the view menu", "click the edit comment commands on the Insert menu", "click the Display comment command on the window menu"],
        "answer": "position the mouse pointer over the cell"
    },
    {
        "question_number": 6,
        "question": "Which of these will not select all the cells in a document ?",
        "options": ["Using the Edit – Select All menu", "Pressing Ctrl + A on the keyboard", "Clicking three times with the right mouse button in the spreadsheet"],
        "answer": "Clicking three times with the right mouse button in the spreadsheet"
    },
    {
        "question_number": 7,
        "question": "The default style for new data keyed in a new workbook is ?",
        "options": ["Comma", "Normal", "Currency", "Percent"],
        "answer": "Normal"
    },
    {
        "question_number": 8,
        "question": "If you press ___, the cell accepts your typing as its contents ?",
        "options": ["Tab", "Ctrl+Enter", "Enter", "Alt+Enter"],
        "answer": "Enter"
    },
    {
        "question_number": 9,
        "question": "Which of the following keyboard shortcut can be used for creating a chart from the selected cells ?",
        "options": ["F11", "F10", "F4", "F2"],
        "answer": "F11"
    },
    {
        "question_number": 10,
        "question": "Formula palette is used to ?",
        "options": ["format cells containing numbers", "create and edit formulas containing functions", "entered assumptions data", "copy all cells"],
        "answer": "create and edit formulas containing functions"
    },
    {
        "question_number": 11,
        "question": "A value used in a formula that does not change is called a ?",
        "options": ["Constant", "Cell address", "Varaible", "Static"],
        "answer": "Constant"
    },
    {
        "question_number": 12,
        "question": "A Spreadsheet contains ?",
        "options": ["Columns", "Rows", "rows and columns", "None of above"],
        "answer": "rows and columns"
    },
    {
        "question_number": 13,
        "question": "To open an existing workbook, click the Open button on the ___ toolbar ?",
        "options": ["Form", "Standard", "Drawing", "Formatting"],
        "answer": "Standard"
    },
    {
        "question_number": 14,
        "question": "Which among following is not associated with spelling dialogue box ?",
        "options": ["Edit", "Ignore", "Ignore All", "Change"],
        "answer": "Edit"
    },
    {
        "question_number": 15,
        "question": "what term describes a background that appears as a grainy, non smooth surface ?",
        "options": ["Pattern", "Gradient", "Texture", "Velvet"],
        "answer": "Texture"
    },
    {
        "question_number": 16,
        "question": "Which among following is associated with excel ?",
        "options": ["Graphic program", "Word Processor", "Presentation", "Spreadsheet"],
        "answer": "Spreadsheet"
    },
    {
        "question_number": 17,
        "question": "The cell reference for a range of cells that starts in cell C1 and goes over to column H and down to row 10 is ?",
        "options": ["C1:10H", "C1:H10", "C1:H-10", "C1:H:10"],
        "answer": "C1:H10"
    },
    {
        "question_number": 18,
        "question": "You can convert existing Excel worksheet data and charts to HTML document by using the ?",
        "options": ["Internet Assistant Wizard", "Intranet Wizard", "Import Wizard", "Export Wizard"],
        "answer": "Internet Assistant Wizard"
    },
    {
        "question_number": 19,
        "question": "To create an interactive Pivot Table for the web, you use a Microsoft Office Web component called ?",
        "options": ["HTML", "Pivot Table Field List", "Pivot Table Report", "Pivot Table List"],
        "answer": "Pivot Table Report"
    },
    {
        "question_number": 20,
        "question": "What function displays row data in a column or column data in a row ?",
        "options": ["Transpose", "Index", "Rows", "Hyperlinks"],
        "answer": "Transpose"
    },
    {
        "question_number": 21,
        "question": "Except which of the following function, a formula with a logical function shows the word \"TRUE\" or \"FALSE\" as a result ?",
        "options": ["NOT", "OR", "IF", "AND"],
        "answer": "IF"
    },
    {
        "question_number": 22,
        "question": "Macros can be executed from the which of the following menu ?",
        "options": ["Format", "Home", "Insert", "Tools"],
        "answer": "Tools"
    },
    {
        "question_number": 23,
        "question": "Protection and the Protect Sheet options can be selected from ?",
        "options": ["Data", "Tools", "Edit", "Format"],
        "answer": "Tools"
    },
    {
        "question_number": 24,
        "question": "Which of the following is not a valid Zoom percentage in Excel ?",
        "options": ["10", "100", "300", "500"],
        "answer": "500"
    },
    {
        "question_number": 25,
        "question": "You can check the conditions against ____ when applying conditional formatting ?",
        "options": ["Cell Value", "Formula", "Both of above", "None of above"],
        "answer": "Both of above"
    },
    {
        "question_number": 26,
        "question": "How can we set Page Border in Excel ?",
        "options": ["From Edit menu", "From Home", "You can not set page border in Excel", "From Tools menu"],
        "answer": "You can not set page border in Excel"
    },
    {
        "question_number": 27,
        "question": "Which function calculates your monthly mortage payment ?",
        "options": ["PV", "NPER", "PMT", "All of above"],
        "answer": "PMT"
    },
    {
        "question_number": 28,
        "question": "Which types of charts can excel produce ?",
        "options": ["Line graphs and pie charts only", "Bar charts, line graphs and pie charts", "Bar charts and line graphs only", "Only line graphs"],
        "answer": "Bar charts, line graphs and pie charts"
    },
    {
        "question_number": 29,
        "question": "How is data organized in a spreadsheet ?",
        "options": ["Rows and columns", "Layers and planes", "Lines and spaces", "Height and width"],
        "answer": "Rows and columns"
    }]

quiz_data_8 = [
  {
    "question_number": 1,
    "question": "Which is not a font style?",
    "options": ["Bold", "Superscript", "Italic", "Regular"],
    "answer": "Superscript"
  },
  {
    "question_number": 2,
    "question": "What is gutter margin?",
    "options": [
      "Margin that is added to right margin when printing",
      "Margin that is added to the left margin when printing",
      "Margin that is added to the outside of the page when printing",
      "Margin that is added to the binding side of page when printing"
    ],
    "answer": "Margin that is added to the binding side of page when printing"
  },
  {
    "question_number": 3,
    "question": "Landscape is?",
    "options": ["A font style", "Paper Size", "Page Layout", "Page Orientation"],
    "answer": "Page Orientation"
  },
  {
    "question_number": 4,
    "question": "Typeface option will come under which menu?",
    "options": ["Edit", "View", "Format", "Tools"],
    "answer": "Format"
  },
  {
    "question_number": 5,
    "question": "Background color on a document is not visible in?",
    "options": ["Web layout view", "Print Preview", "Reading View", "Print Layout view"],
    "answer": "Print Preview"
  },
  {
    "question_number": 6,
    "question": "What is a portion of a document in which you set certain page formatting options?",
    "options": ["Page Setup", "Section", "Page", "Document"],
    "answer": "Section"
  },
  {
    "question_number": 7,
    "question": "Which of the following is not available on the Ruler of MS Word screen?",
    "options": ["Tab stop box", "Left Indent", "Right Indent", "Center Indent"],
    "answer": "Center Indent"
  },
  {
    "question_number": 8,
    "question": "Gutter position can be set in following positions",
    "options": ["Left & Right", "Left & Top", "Left & Bottom", "Left Only"],
    "answer": "Left & Top"
  },
  {
    "question_number": 9,
    "question": "What is the Short cut key for line break?",
    "options": ["CTRL + Enter", "Alt + Enter", "Shift + Enter", "Space + Enter"],
    "answer": "Shift + Enter"
  },
  {
    "question_number": 10,
    "question": "By pressing F12, which of following will happen?",
    "options": [
      "Save As dialog box will open",
      "Save dialog box will open",
      "Open dialog box will open",
      "Close dialog box will open"
    ],
    "answer": "Save As dialog box will open"
  },
  {
    "question_number": 11,
    "question": "Which key will open an Open dialogue box?",
    "options": ["F12", "Alt + F12", "Ctrl + F12", "Shift + F12"],
    "answer": "Ctrl + F12"
  },
  {
    "question_number": 12,
    "question": "How will MS Word will respond in repeated word?",
    "options": [
      "A Green wavy line under the repeated word",
      "A Red wavy line under the repeated word",
      "A Blue wavy line under the repeated word",
      "None of above"
    ],
    "answer": "A Red wavy line under the repeated word"
  },
  {
    "question_number": 13,
    "question": "What is the use of \"All Caps\" feature in MS-Word?",
    "options": [
      "It changes all selected text into Capital Letter",
      "It adds captions for selected Image",
      "It shows all the image captions",
      "None of above"
    ],
    "answer": "It changes all selected text into Capital Letter"
  },
  {
    "question_number": 14,
    "question": "Which file is responsible to start MS Word?",
    "options": ["Winword.exe", "Win.exe", "Word.exe", "Wordwin.exe"],
    "answer": "Winword.exe"
  },
  {
    "question_number": 15,
    "question": "To keep track of different editions of a document which feature we will use?",
    "options": ["Editions", "Versions", "Tracks", "traces"],
    "answer": "Versions"
  },
  {
    "question_number": 16,
    "question": "Which is not a type of margin?",
    "options": ["Top", "Left", "Right", "Center"],
    "answer": "Center"
  },
  {
    "question_number": 17,
    "question": "what will be the use of Ctrl + J?",
    "options": ["Insert Image", "Insert Hyperlink", "Align Justify", "Search file"],
    "answer": "Align Justify"
  },
  {
    "question_number": 18,
    "question": "What shortcut will we use to align centre?",
    "options": ["Ctrl + A", "Ctrl + E", "Ctrl + D", "Ctrl + B"],
    "answer": "Ctrl + E"
  },
  {
    "question_number": 19,
    "question": "Which shortcut will we use to make text Italic?",
    "options": ["Ctrl + U", "Ctrl + T", "Ctrl + I", "Ctrl + P"],
    "answer": "Ctrl + I"
  },
  {
    "question_number": 20,
    "question": "How to use Format Painter multiple times?",
    "options": [
      "By Click on Lock Format Painter Icon",
      "Format Painter cannot be use multiple times",
      "By Double Click on the Format Painter Icon"
    ],
    "answer": "By Double Click on the Format Painter Icon"
  },
  {
    "question_number": 21,
    "question": "What is place to the left of horizontal scroll bar?",
    "options": ["Indicators", "Split buttons", "Tab stop buttons", "View buttons"],
    "answer": "View buttons"
  },
  {
    "question_number": 22,
    "question": "Where can you find the horizontal split bar on MS Word screen?",
    "options": [
      "On the top of vertical scroll bar",
      "On the bottom of vertical scroll bar",
      "On the left of horizontal scroll bar",
      "On the right of horizontal scroll bar"
    ],
    "answer": "On the top of vertical scroll bar"
  },
  {
    "question_number": 23,
    "question": "Tabs stop position cannot be the following alignment?",
    "options": ["Decimal Alignment", "Center Alignment", "Bar Alignment", "Justify Alignment"],
    "answer": "Justify Alignment"
  },
  {
    "question_number": 24,
    "question": "What is the use of bookmarks?",
    "options": [
      "To correct the spellings.",
      "To jump to a specific location in the document",
      "To ignore spelling mistakes",
      "To save alignments as it is."
    ],
    "answer": "To jump to a specific location in the document"
  },
  {
    "question_number": 25,
    "question": "Which feature is used to replace straight quotes with smart quotes as you type?",
    "options": [
      "Auto Correct as you type",
      "Auto Change as you type",
      "Auto Ignore as you type",
      "Auto Format as you type"
    ],
    "answer": "Auto Format as you type"
  },
  {
    "question_number": 26,
    "question": "Ctrl + D is short cut used for?",
    "options": ["Open Dialogue Box", "Font Dialogue Box", "Save as Dialogue Box", "Save Dialogue Box"],
    "answer": "Font Dialogue Box"
  },
  {
    "question_number": 27,
    "question": "Ctrl + G is shortcut for?",
    "options": [
      "Open Find and Replace Dialog box with activating Goto Tab",
      "Open Find and Replace Dialog box with activating Find Tab",
      "Open Find and Replace Dialog box with activating Replace Tab",
      "Open Goto Dialog box"
    ],
    "answer": "Open Find and Replace Dialog box with activating Goto Tab"
  },
  {
    "question_number": 28,
    "question": "Ctrl + H is short cut for?",
    "options": [
      "Open Insert Dialog box activating Insert Hyper Link Tab",
      "Open Find and Replace Dialog box with activating Go to Tab",
      "Open Find and Replace Dialog box with activating Find Tab",
      "Open Find and Replace Dialog box with activating Replace Tab"
    ],
    "answer": "Open Find and Replace Dialog box with activating Replace Tab"
  },
  {
    "question_number": 29,
    "question": "What can be searched by find?",
    "options": ["Format", "Characters", "Symbol", "All of above"],
    "answer": "All of above"
  },
  {
    "question_number": 30,
    "question": "on which page the header or the footer is printed by default?",
    "options": ["on first page", "on last page", "on alternate page", "every page"],
    "answer": "every page"
  }
]

quiz_data_9 = [
  {
    "question_number": 31,
    "question": "Which of these toolbars allows changing of Fonts and their sizes?",
    "options": ["Standard", "Formatting", "Options", "None of above"],
    "answer": "Formatting"
  },
  {
    "question_number": 32,
    "question": "To spell check which function key you will press?",
    "options": ["F5", "F6", "F7", "F8"],
    "answer": "F7"
  },
  {
    "question_number": 33,
    "question": "How to insert a sound file in word document?",
    "options": [
      "From insert -> sound menu option",
      "From insert -> object menu option",
      "From insert -> subject menu option",
      "From insert -> file menu option"
    ],
    "answer": "From insert -> object menu option"
  },
  {
    "question_number": 34,
    "question": "How many maximum number of columns can be inserted in the word document?",
    "options": ["45", "50", "55", "65"],
    "answer": "45"
  },
  {
    "question_number": 35,
    "question": "What is smallest and largest available font on formatting toolbar?",
    "options": [
      "Smallest 8 and Largest 70",
      "Smallest 5 and Largest 72",
      "Smallest 8 and Largest 72",
      "Smallest 5 and Largest 70"
    ],
    "answer": "Smallest 8 and Largest 72"
  },
  {
    "question_number": 36,
    "question": "Why drop cap is used in document?",
    "options": [
      "To get all first character capital",
      "To get all first character small",
      "To begin a paragraph with a large dropped initial capital letter",
      "To begin a paragraph with a large dropped initial small letter"
    ],
    "answer": "To begin a paragraph with a large dropped initial capital letter"
  },
  {
    "question_number": 37,
    "question": "What is Macro?",
    "options": [
      "Small add-on programs that are installed afterwards if you need them",
      "Type of high level programming language",
      "Type of low level programming language",
      "Small programs created in MS-Word to automate repetitive tasks by using VBA"
    ],
    "answer": "Small programs created in MS-Word to automate repetitive tasks by using VBA"
  },
  {
    "question_number": 38,
    "question": "Which among following can be a vertical separation between columns?",
    "options": ["Margin", "Header", "Orientation", "Gutter"],
    "answer": "Gutter"
  },
  {
    "question_number": 39,
    "question": "MS Office is not an application software?",
    "options": ["True", "False"],
    "answer": "False"
  },
  {
    "question_number": 40,
    "question": "To change the typeface of a document, we will choose following menu option",
    "options": ["Edit", "View", "Tools", "Format"],
    "answer": "Format"
  },
  {
    "question_number": 41,
    "question": "To autofit the width of column",
    "options": [
      "Double click the left border of column",
      "Double click the right border of column",
      "Double click the column header",
      "None of above"
    ],
    "answer": "Double click the right border of column"
  },
  {
    "question_number": 42,
    "question": "A keyboard shortcut can be assigned to a Macro.",
    "options": ["True", "False"],
    "answer": "True"
  },
  {
    "question_number": 43,
    "question": "A keyboard shortcut can be assigned to a Macro.",
    "options": ["True", "False"],
    "answer": "True"
  },
  {
    "question_number": 44,
    "question": "What is the default font size of a new Word document based on Normal template?",
    "options": ["8 pt", "10 pt", "12 pt", "14 pt"],
    "answer": "12 pt"
  },
  {
    "question_number": 45,
    "question": "Which of following line spacing is invalid?",
    "options": ["Single", "Double", "Triple", "Multiple"],
    "answer": "Triple"
  },
  {
    "question_number": 46,
    "question": "Format painter tool can be found in",
    "options": ["Options toolbar", "Standard toolbar", "Formatting toolbar", "Drawing toolbar"],
    "answer": "Standard toolbar"
  },
  {
    "question_number": 47,
    "question": "Which among following is correct extension of word files?",
    "options": ["Xls", "Doc", "Ppt", "dcw"],
    "answer": "Doc"
  },
  {
    "question_number": 48,
    "question": "You can jump to the next column by",
    "options": ["Press Alt + Down-arrow", "Clicking with your mouse on the next column", "Both of above", "None of above"],
    "answer": "Clicking with your mouse on the next column"
  },
  {
    "question_number": 49,
    "question": "Which of the following is not the part of standard office suite?",
    "options": ["Database", "File Manager", "Image Editor", "File Presentation"],
    "answer": "File Manager"
  },
  {
    "question_number": 50,
    "question": "Superscript, subscript, outline, emboss, engrave are known as?",
    "options": ["Text effects", "Font effects", "Word art", "Clip art"],
    "answer": "Font effects"
  },
  {
    "question_number": 51,
    "question": "A screen element of MS Word that is usually located below the title bar that provides categorized options is known as?",
    "options": ["Menu Bar", "Tool Bar", "Status Bar", "Address Bar"],
    "answer": "Menu Bar"
  },
  {
    "question_number": 52,
    "question": "Minimum number of rows and columns in MS Word document is",
    "options": ["1 and 1", "2 and 1", "1 and 2", "2 and 2"],
    "answer": "1 and 1"
  },
  {
    "question_number": 53,
    "question": "How many maximum columns can be inserted in MS word document?",
    "options": ["40", "45", "50", "55", "Unlimited"],
    "answer": "45"
  },
  {
    "question_number": 54,
    "question": "What we call to that character which is raised and smaller above the base line?",
    "options": ["Raised", "Smaller", "Quotient", "Superscript"],
    "answer": "Superscript"
  },
  {
    "question_number": 55,
    "question": "Ruler in MS Word can help us in",
    "options": ["to set tabs", "to set indents", "to change page margins", "all of above"],
    "answer": "all of above"
  },
  {
    "question_number": 56,
    "question": "What we call to a combination of row and column",
    "options": ["Line", "Column", "Row", "Cell"],
    "answer": "Cell"
  },
  {
    "question_number": 57,
    "question": "What is Gutter Margin?",
    "options": [
      "Margin that is added to the outside of the page when printing",
      "Margin that is added to the binding side of page when printing",
      "Margin that is added to right margin when printing",
      "Margin that is added to the left margin when printing"
    ],
    "answer": "Margin that is added to the binding side of page when printing"
  },
  {
    "question_number": 58,
    "question": "typeface option is under which menu?",
    "options": ["Format", "Insert", "Edit", "View"],
    "answer": "Format"
  },
  {
    "question_number": 59,
    "question": "In which view background color will not be visible?",
    "options": ["Print Layout View", "Web Layout View", "Print Preview", "Reading View"],
    "answer": "Print Preview"
  },
  {
    "question_number": 60,
    "question": "Spreadsheets are created in?",
    "options": ["MS Word", "MS Powerpoint", "MS Excel", "MS Access"],
    "answer": "MS Excel"
  }
]

quiz_data_10 = [
  {
    "question_number": 1,
    "question": "You can search a word document for",
    "options": ["Formatting", "Special Characters", "Phrases", "All of the above"],
    "answer": "All of the above"
  },
  {
    "question_number": 2,
    "question": "When you display your document in full screen view ...",
    "options": [
      "You cannot use the menu or shortcut menu commands",
      "You see the previous page and next page buttons",
      "You add selection break to your document.",
      "The title bar, status bar, menu bar, scroll bars, taskbar and toolbars are not display."
    ],
    "answer": "The title bar, status bar, menu bar, scroll bars, taskbar and toolbars are not display."
  },
  {
    "question_number": 3,
    "question": "What keystroke combination selects the entire document?",
    "options": ["Ctrl+A", "Alt+F8", "Shift+Ctrl+A", "Alt+A"],
    "answer": "Ctrl+A"
  },
  {
    "question_number": 4,
    "question": "To save an existing document in a new file with a different location you",
    "options": ["Save As", "Save", "Close", "All of the above"],
    "answer": "Save As"
  },
  {
    "question_number": 5,
    "question": "Which of the following is not an editing view?",
    "options": ["Online layout view", "Full screen view", "Format view", "Page layout view"],
    "answer": "Format view"
  },
  {
    "question_number": 6,
    "question": "Which key deletes text before, or to the left of the insert point?",
    "options": ["Delete", "Backspace", "Page Down", "Page Up"],
    "answer": "Backspace"
  },
  {
    "question_number": 7,
    "question": "The use of smart cut and past option....",
    "options": [
      "Inserts a special symbols at the end of each document",
      "Copy text in a document without using clipboard",
      "Adds or deletes space as needed when pasting text",
      "All of the above"
    ],
    "answer": "Adds or deletes space as needed when pasting text"
  },
  {
    "question_number": 8,
    "question": "Right-clicking something in Word...",
    "options": [
      "Deletes the object",
      "Nothing - the right mouse button is there for left handed people",
      "Opens a shortcut menu listing everything you can do to the object",
      "Selects the object"
    ],
    "answer": "Opens a shortcut menu listing everything you can do to the object"
  },
  {
    "question_number": 9,
    "question": "How can you apply format of one text into other text?",
    "options": ["Using copy and paste", "Using style", "Using format painter", "All of the above"],
    "answer": "All of the above"
  },
  {
    "question_number": 10,
    "question": "You can moved and copy text ..",
    "options": [
      "Within a word document",
      "Between office application",
      "Between word document",
      "All of the above"
    ],
    "answer": "All of the above"
  },
  {
    "question_number": 11,
    "question": "Which of the following options is not an option in the print dialog box?",
    "options": [
      "Print selected pages",
      "Print selected text",
      "Set the paper orientation",
      "Collate copies"
    ],
    "answer": "Print selected text"
  },
  {
    "question_number": 12,
    "question": "What is the fastest way to select a single word?",
    "options": [
      "Move the insertion point to the beginning of the word and hold down the shift key",
      "Double click the word",
      "Click the select word wizard button on the tool-bar",
      "None of the above"
    ],
    "answer": "Double click the word"
  },
  {
    "question_number": 13,
    "question": "Auto text entries",
    "options": ["Can be deleted", "Can be edited", "Are saved with the normal template", "All of the above"],
    "answer": "All of the above"
  },
  {
    "question_number": 14,
    "question": "What key can you press to get help in any windows-based program?",
    "options": ["Scroll lock", "F1", "Esc", "F1"],
    "answer": "F1"
  },
  {
    "question_number": 15,
    "question": "To insert page break press ..",
    "options": ["Shift + Ctrl + Enter", "Alt + Enter", "Shift + Enter", "Ctrl + Enter"],
    "answer": "Ctrl + Enter"
  },
  {
    "question_number": 16,
    "question": "The spike ....",
    "options": [
      "Allow you to combine text from several documents and then inserts all the text into one documents at one time",
      "Allows you to edit auto text entries",
      "Allows you to format auto text entries",
      "All of the above"
    ],
    "answer": "Allow you to combine text from several documents and then inserts all the text into one documents at one time"
  },
  {
    "question_number": 17,
    "question": "You can decrease your document by one page by using the ...",
    "options": [
      "Shrink to fit button",
      "Fit to one page button",
      "Magnifier button",
      "Reduce by one page button"
    ],
    "answer": "Shrink to fit button"
  },
  {
    "question_number": 18,
    "question": "What color are grammar errors?",
    "options": ["Yellow", "Red", "Green", "Blue"],
    "answer": "Green"
  },
  {
    "question_number": 19,
    "question": "When you create an auto text entry",
    "options": [
      "You can save it with the current template",
      "You should keep the name short",
      "You must assign it a unique name",
      "All of the above"
    ],
    "answer": "All of the above"
  },
  {
    "question_number": 20,
    "question": "The auto complete feature",
    "options": [
      "Presents a tip box with contents you can insert by presenting the enter key",
      "Checks the style of the documents",
      "Checks the readability of the document",
      "Checks the spelling in the document"
    ],
    "answer": "Presents a tip box with contents you can insert by presenting the enter key"
  },
  {
    "question_number": 21,
    "question": "End Key",
    "options": [
      "Moves the cursor end of the line",
      "Moves the cursor end of the document",
      "Moves the cursor end of the paragraph",
      "Moves the cursor end of the screen"
    ],
    "answer": "Moves the cursor end of the line"
  },
  {
    "question_number": 22,
    "question": "“Ctrl + PageDown” is used to",
    "options": [
      "Moves the cursor one Paragraph Down",
      "Moves the cursor one Page Down",
      "Moves the cursor one Line Down",
      "Moves the cursor one Screen Down"
    ],
    "answer": "Moves the cursor one Page Down"
  },
  {
    "question_number": 23,
    "question": "“Ctrl + Down Arrow” is used to",
    "options": [
      "Moves the cursor one paragraph down",
      "Moves the cursor one line down",
      "Moves the cursor one page down",
      "Moves the cursor one screen down"
    ],
    "answer": "Moves the cursor one paragraph down"
  },
  {
    "question_number": 24,
    "question": "Page Up Key",
    "options": [
      "Moves the cursor one line up",
      "Moves the cursor one screen up",
      "Moves the cursor one page up",
      "Moves the cursor one paragraph up"
    ],
    "answer": "Moves the cursor one screen up"
  }
]

quiz_data_11 = [
  {
    "question_number": 25,
    "question": "“Ctrl + Left Arrow” is used to",
    "options": [
      "Moves the cursor beginning of the Line",
      "Moves the cursor one word left",
      "Moves the cursor one paragraph up",
      "Moves the cursor one paragraph down"
    ],
    "answer": "Moves the cursor one word left"
  },
  {
    "question_number": 26,
    "question": "Page Down Key",
    "options": [
      "Moves the cursor one line down",
      "Moves the cursor one page down",
      "Moves the cursor one screen down",
      "Moves the cursor one paragraph down"
    ],
    "answer": "Moves the cursor one screen down"
  },
  {
    "question_number": 27,
    "question": "“Ctrl + PageUp” is used to",
    "options": [
      "Moves the cursor one Page Up",
      "Moves the cursor one Paragraph Up",
      "Moves the cursor one Screen Up",
      "Moves the cursor one Line Up"
    ],
    "answer": "Moves the cursor one Page Up"
  },
  {
    "question_number": 28,
    "question": "“Ctrl + Up Arrow” is used to",
    "options": [
      "Moves the cursor one page up",
      "Moves the cursor one line up",
      "Moves the cursor one screen up",
      "Moves the cursor one paragraph up"
    ],
    "answer": "Moves the cursor one paragraph up"
  },
  {
    "question_number": 29,
    "question": "“Ctrl + Home”is used to",
    "options": [
      "Moves the cursor to the beginning of Document",
      "Moves the cursor to the beginning of Line",
      "Moves the cursor to the beginning of Paragraph",
      "All of the above"
    ],
    "answer": "Moves the cursor to the beginning of Document"
  },
  {
    "question_number": 30,
    "question": "“Ctrl + End”is used to",
    "options": [
      "Moves the cursor to the end of Line",
      "Moves the cursor to the end of Document",
      "Moves the cursor to the end of Paragraph",
      "None of the Above"
    ],
    "answer": "Moves the cursor to the end of Document"
  },
  {
    "question_number": 31,
    "question": "Which of the following are word processing software?",
    "options": ["WordPerfect", "Easy Word", "MS Word", "All of above"],
    "answer": "All of above"
  },
  {
    "question_number": 32,
    "question": "Which file starts MS Word?",
    "options": ["winword.exe", "word.exe", "msword.exe", "word2003.exe"],
    "answer": "winword.exe"
  },
  {
    "question_number": 33,
    "question": "Ctrl + N",
    "options": ["Save Document", "Open Document", "New Document", "Close Document"],
    "answer": "New Document"
  },
  {
    "question_number": 34,
    "question": "To exit from the Resume Wizard and return to the document window without creating a resume, click the _____ button in any panel in the Resume Wizard dialog box.",
    "options": ["Cancel", "Back", "Next", "Finish"],
    "answer": "Finish"
  },
  {
    "question_number": 35,
    "question": "A _____ is a collection of predefined design elements and color schemes.",
    "options": ["feature", "hyperlink", "palette", "theme"],
    "answer": "theme"
  },
  {
    "question_number": 36,
    "question": "Change the _____ to create a document in wide format",
    "options": ["Page Orientation", "Page margins", "Paper Style", "Paper Source"],
    "answer": "Page Orientation"
  },
  {
    "question_number": 37,
    "question": "In MS Word, Ctrl+Sis for …..",
    "options": ["Scenarios", "Size", "Save", "Spelling Check"],
    "answer": "Save"
  },
  {
    "question_number": 38,
    "question": "Ctrl + W",
    "options": [
      "Save and Print the Document",
      "Save and Close Word Application",
      "Save and Close document",
      "Without Save, Close Document"
    ],
    "answer": "Save and Close document"
  },
  {
    "question_number": 39,
    "question": "The key F12 opens a",
    "options": ["Save As dialog box", "Open dialog box", "Save dialog box", "Close dialog box"],
    "answer": "Save As dialog box"
  },
  {
    "question_number": 40,
    "question": "Ctrl + I",
    "options": ["Italic", "Left Indent", "Save Document", "Close Document"],
    "answer": "Italic"
  },
  {
    "question_number": 41,
    "question": "Ctrl + S",
    "options": [
      "Save Document with different name",
      "Save Document with same name",
      "Save Document and Close Word Application",
      "Save Document and Print whole Pages"
    ],
    "answer": "Save Document with same name"
  },
  {
    "question_number": 42,
    "question": "If you will be displaying or printing your document on another computer, you‟ll want to make sure and select the _____________ option under the „Save‟ tab.",
    "options": [
      "Embed Fonts",
      "Embed True Type Fonts",
      "Save True Type Fonts",
      "Save Fonts"
    ],
    "answer": "Embed True Type Fonts"
  },
  {
    "question_number": 43,
    "question": "Ctrl + J",
    "options": ["Align Justify", "Insert Hyperlink", "Search", "Print"],
    "answer": "Align Justify"
  },
  {
    "question_number": 44,
    "question": "What is a portion of a document in which you set certain page formatting options?",
    "options": ["Page", "Document", "Section", "Page Setup"],
    "answer": "Section"
  },
  {
    "question_number": 45,
    "question": "If you need to double underline a word, how will you do that?",
    "options": [
      "Go to Format menu and then Font option. Open Underline Style and choose Double Underline",
      "From Format menu choose Font option and then from Font tab open Underline Style and select Double Underline",
      "Select the text then choose Format >> Font and on Font tab, open Underline Style and choose Double Underline",
      "Click double underline tool on formatting toolbar"
    ],
    "answer": "Select the text then choose Format >> Font and on Font tab, open Underline Style and choose Double Underline"
  }
]

quiz_data_12 = [
  {
    "question_number": 1,
    "question": "Which file format can be added to a PowerPoint show ?",
    "options": [".gif", ".jpg", ".wav", "All of above"],
    "answer": "All of above"
  },
  {
    "question_number": 2,
    "question": "How to select one hyperlink after another during a slide presentation ?",
    "options": ["Ctrl + K", "Ctrl + D", "Tab", "Ctrl + H"],
    "answer": "Tab"
  },
  {
    "question_number": 3,
    "question": "Special effects used to introduce slides in a presentation are known as ?",
    "options": ["Transitions", "Effects", "custom animations", "annotations"],
    "answer": "Transitions"
  },
  {
    "question_number": 4,
    "question": "You can edit an embedded organization chart object by ?",
    "options": [
      "Double clicking the organization chart object",
      "Clicking edit object",
      "Right clicking the chart object, then clicking edit MS-Organizaiton Chart object",
      "A and C both"
    ],
    "answer": "A and C both"
  },
  {
    "question_number": 5,
    "question": "Which of the following is not one of PowerPoint view ?",
    "options": ["Slide show view", "Slide view", "Presentation view", "Outline view"],
    "answer": "Presentation view"
  },
  {
    "question_number": 6,
    "question": "Which PowerPoint view works best for adding slide transitions ?",
    "options": ["Slide show view", "Slide sorter view", "Slide view", "Notes view"],
    "answer": "Slide sorter view"
  },
  {
    "question_number": 7,
    "question": "Which PowerPoint feature allows the user to create a simple presentation quickly ?",
    "options": ["AutoContent Wizard", "Transition Wizard", "Chart Wizard", "Animations"],
    "answer": "AutoContent Wizard"
  },
  {
    "question_number": 8,
    "question": "Slide sorter can be accessed from which menu ?",
    "options": ["Insert", "File", "Edit", "View"],
    "answer": "View"
  },
  {
    "question_number": 9,
    "question": "To print powerpoint presentation, press :",
    "options": ["Ctrl + A", "Ctrl + Shift + P", "Ctrl + P", "CTRL + S"],
    "answer": "Ctrl + P"
  },
  {
    "question_number": 10,
    "question": "What would I choose to create a pre-formatted style ?",
    "options": ["Slide sorter view", "Slide layout", "Format", "None of above"],
    "answer": "Slide layout"
  },
  {
    "question_number": 11,
    "question": "To edit a chart, we can",
    "options": [
      "Double click the chart object",
      "Click and drag the chart object",
      "Triple click the chart object",
      "Click the chart object"
    ],
    "answer": "Double click the chart object"
  },
  {
    "question_number": 12,
    "question": "To preview a motion path effect using the custom animation task pane, we should :",
    "options": ["double click the motion path", "click the show effect button", "click the play button", "none of above"],
    "answer": "click the play button"
  },
  {
    "question_number": 13,
    "question": "You can create a new presentation by completing all of the following except",
    "options": [
      "Clicking the new button on the standard toolbar",
      "Clicking file, new",
      "Pressing ctrl + N",
      "Clicking file open"
    ],
    "answer": "Clicking file open"
  },
  {
    "question_number": 14,
    "question": "What is the term used when you press and hold the left mouse key and more the mouse around the slide ?",
    "options": ["Moving", "Monitoring", "Dragging", "Highlighting"],
    "answer": "Dragging"
  },
  {
    "question_number": 15,
    "question": "Which of the following views is the best view to use when setting transition effects for all slides in a presentation ?",
    "options": ["Slide view", "Notes page view", "Slide sorter view", "Outline view"],
    "answer": "Slide sorter view"
  },
  {
    "question_number": 16,
    "question": "Which of the following will not advance the slides in a slide show view ?",
    "options": ["The mouse button", "The enter key", "The space bar", "The esc key"],
    "answer": "The esc key"
  },
  {
    "question_number": 17,
    "question": "Which option can be used to set custom timings for slides in a presentation ?",
    "options": ["Slider Timings", "Rehearsal", "Slider Timer", "Slide Show Setup"],
    "answer": "Rehearsal"
  },
  {
    "question_number": 18,
    "question": "Which of the following can you use to add times to the slides in a presentation ?",
    "options": ["Rehearse timing button", "Slice Show menu", "Slide transition button", "All of above"],
    "answer": "Rehearse timing button"
  },
  {
    "question_number": 19,
    "question": "Which key can be used to view Slide show ?",
    "options": ["F5", "F2", "F7", "F9"],
    "answer": "F5"
  },
  {
    "question_number": 20,
    "question": "Which type of fonts are best suite for titles and headlines ?",
    "options": ["Sans Serif Fonts", "Picture Fonts", "Text Fonts", "Serif Fonts"],
    "answer": "Sans Serif Fonts"
  },
  {
    "question_number": 21,
    "question": "How can we view slide show repeated continuously ?",
    "options": ["repeat continuously", "loop continuously until ‘Esc’", "loop more", "none"],
    "answer": "loop continuously until ‘Esc’"
  },
  {
    "question_number": 22,
    "question": "Ellipse Motion is a predefined ___ .",
    "options": ["Design Template", "Animation Scheme", "Color Scheme", "None of above"],
    "answer": "Animation Scheme"
  },
  {
    "question_number": 23,
    "question": "To open the existing presentation, press",
    "options": ["CTRL + A", "CTRL + O", "CTRL + N", "CTRL + L"],
    "answer": "CTRL + O"
  },
  {
    "question_number": 24,
    "question": "PowerPoint slides can have ?",
    "options": ["title, text, graphs", "drawn objects, shapes", "clipart, drawn art, visual", "any of the above"],
    "answer": "any of the above"
  },
  {
    "question_number": 25,
    "question": "Which key do you press to check spelling ?",
    "options": ["F3", "F5", "F7", "F9"],
    "answer": "F7"
  },
  {
    "question_number": 26,
    "question": "The spelling dialog box can be involved by choosing spelling from ____ menu.",
    "options": ["Insert", "File", "View", "Tools"],
    "answer": "Tools"
  },
  {
    "question_number": 27,
    "question": "The spelling dialog box can be involved by choosing spelling from ____ menu.",
    "options": ["Insert", "File", "View", "Tools"],
    "answer": "Tools"
  },
  {
    "question_number": 28,
    "question": "Power Point can display data from which of the following add-in software of MS Office ?",
    "options": ["Equation Editor", "Photo Album", "Organization Chart", "All of above"],
    "answer": "All of above"
  },
  {
    "question_number": 29,
    "question": "How can we stop a slide show ?",
    "options": ["Press the right arrow", "Press Escape", "Press Ctrl + A", "Press Ctrl + S"],
    "answer": "Press Escape"
  }]

quiz_data_13 = [
  {
    "question_number": 30,
    "question": "A File which contains readymade styles that can be used for a presentation is called __ ?",
    "options": ["AutoStyle", "Wizard", "Template", "Pre formatting"],
    "answer": "Template"
  },
  {
    "question_number": 31,
    "question": "What is maximum Zoom percentage in Microsoft PowerPoint ?",
    "options": ["100%", "200%", "300%", "400%"],
    "answer": "400%"
  },
  {
    "question_number": 32,
    "question": "How we can put a Chart in the presentation using PowerPoint ?",
    "options": ["Edit -> Chart", "Insert -> Pictures -> Chart", "Insert -> Chart", "View -> Chart"],
    "answer": "Insert -> Chart"
  },
  {
    "question_number": 33,
    "question": "How we can replace a font on all slides with another font in Powerpoint ?",
    "options": ["Tools -> Fonts", "Edit -> Fonts", "Format -> Replace Fonts", "Tools -> Replace Fonts"],
    "answer": "Format -> Replace Fonts"
  },
  {
    "question_number": 34,
    "question": "Shortcut to insert new slide in the current Presentation is ?",
    "options": ["CTRL+O", "CTRL+M", "CTRL+F", "CTRL+N"],
    "answer": "CTRL+M"
  },
  {
    "question_number": 35,
    "question": "The boxes that are displayed to indicate that the text, pictures or objects are placed in it is called ?",
    "options": ["Word Art", "Placeholder", "AutoText", "Text box"],
    "answer": "Placeholder"
  },
  {
    "question_number": 36,
    "question": "How can you see all your slides at once ?",
    "options": ["Through slide sorter view", "Through slide view", "Through normal view", "Through slide show"],
    "answer": "Through slide sorter view"
  },
  {
    "question_number": 37,
    "question": "Which view in Power Point can be used to enter Speaker Comments ?",
    "options": ["Slide Show", "Notes Page view", "Slide Sorter", "Normal"],
    "answer": "Notes Page view"
  },
  {
    "question_number": 38,
    "question": "Which of the following tool bars provide different options in various master views ?",
    "options": ["Standard toolbar", "Formatting toolbar", "Common tasks toolbar", "Drawing toolbar"],
    "answer": "Common tasks toolbar"
  },
  {
    "question_number": 39,
    "question": "In Microsoft PowerPoint two kind of sound effects files that can be added to the presentation are ?",
    "options": [".wav files and .gif files", ".jpg files and .gif files", ".wav files and .jpg files", ".wav files and .mid files"],
    "answer": ".wav files and .mid files"
  },
  {
    "question_number": 40,
    "question": "Which pane would be used to enter a speaker's information about what can be said about each slide ?",
    "options": ["Notes pane", "Outline pane", "Slide pane"],
    "answer": "Notes pane"
  },
  {
    "question_number": 41,
    "question": "In Powerpoint the arrangement of elements such as Title and subtitle text, pictures, tables etc. is known as ?",
    "options": ["Layout", "Design", "Presentation", "Scheme"],
    "answer": "Layout"
  },
  {
    "question_number": 42,
    "question": "What is a motion path in Powerpoint ?",
    "options": ["A type of animation entrance effect", "A method of moving items on a slide", "A method of advancing slides", "All of above"],
    "answer": "A method of moving items on a slide"
  },
  {
    "question_number": 43,
    "question": "What is a slide-title master pair ?",
    "options": ["A slide master and title master for a specific design template", "The title area and text area of a specific slide", "A slide master and title master merged into a single slide", "None of above"],
    "answer": "A slide master and title master for a specific design template"
  },
  {
    "question_number": 44,
    "question": "What is a trigger, in context of animations ?",
    "options": ["An object to be inserted in the presentation", "An action button that advances to the next slide", "The name of a motion path", "An item on the slide that performs an action when clicked"],
    "answer": "An item on the slide that performs an action when clicked"
  },
  {
    "question_number": 45,
    "question": "From where can we set the timing for each object ?",
    "options": ["slide show, custom animation", "view, slide sorter", "slide show, custom transition", "Slide show, Slide transition"],
    "answer": "slide show, custom animation"
  },
  {
    "question_number": 46,
    "question": "How we can create a uniform appearance by adding a background image to all slides ?",
    "options": ["By editing last slide", "Use the autocorrect wizard", "Create a template", "Edit the slide master"],
    "answer": "Edit the slide master"
  },
  {
    "question_number": 47,
    "question": "When you open a presentation which tab is not available on left panel?",
    "options": ["Slides", "Outline", "Notes", "All of above are available"],
    "answer": "Notes"
  },
  {
    "question_number": 48,
    "question": "Which of the following statements is false ?",
    "options": [
      "You can type text directly into a PowerPoint slide but typing in text box is more convenient",
      "You can show or hide task pane from View -> Toolbars",
      "You can view a PowerPoint presentation in Normal, Slide Sorter or Slide Show view",
      "From Insert menu choose Picture and then File to insert your images into slides"
    ],
    "answer": "You can type text directly into a PowerPoint slide but typing in text box is more convenient"
  },
  {
    "question_number": 49,
    "question": "You can start power point application with",
    "options": [
      "Goint to Start -> Programs -> All Programs -> Microsoft PowerPoint",
      "Going to Start -> Run -> type \"powerpnt\" and press enter",
      "type ppoint.exe in run and press enter",
      "All of above"
    ],
    "answer": "Going to Start -> Run -> type \"powerpnt\" and press enter"
  },
  {
    "question_number": 50,
    "question": "In a slide layout, which of the following section does not exist ?",
    "options": ["Animation Section", "Lists Section", "Titles Section", "Chart Section"],
    "answer": "Animation Section"
  },
  {
    "question_number": 51,
    "question": "One can change color of different objects without changing content using",
    "options": ["Font Color", "Object Color", "Layout Section", "Color Scheme"],
    "answer": "Color Scheme"
  },
  {
    "question_number": 52,
    "question": "All of above are false statements",
    "options": [
      "You can change positioning by selecting fomr one of pre made slide layouts",
      "You can't delete objects within layout if you choose to select from pre made slide layouts",
      "In the slide layout panel we can find blank slide at the top of Content Layouts",
      "All of above are false statements"
    ],
    "answer": "You can change positioning by selecting fomr one of pre made slide layouts"
  },
  {
    "question_number": 53,
    "question": "You can apply motion effects to different objects of a slide using",
    "options": ["Animation Scheme", "Slide Transition", "Color Scheme", "Font scheme"],
    "answer": "Animation Scheme"
  },
  {
    "question_number": 54,
    "question": "What is the difference between Slide Design and Auto Content Wizard ?",
    "options": [
      "There is no difference",
      "AutoContent Wizard is just the wizard version of Slide Design",
      "Slide Design asks your choice in steps but Auto Content Wizard does not let you make choices",
      "Slide Design does not provide sample content but Auto Content Wizard provides sample content too"
    ],
    "answer": "Slide Design does not provide sample content but Auto Content Wizard provides sample content too"
  },
  {
    "question_number": 55,
    "question": "Animation Scheme, custom Animation, Slide Transition…which menu provides these options",
    "options": ["Slide Show Menu", "Tools Menu", "Format Menu", "Insert Menu"],
    "answer": "Slide Show Menu"
  },
  {
    "question_number": 56,
    "question": "If you select first and second slide and then click on New Slide button on toolbar, what will happen then ?",
    "options": [
      "A new slide is inserted as second slide in presentation",
      "A new slide is inserted as third slide in presentation",
      "A new slide is inserted as first slide in presentation",
      "None of above"
    ],
    "answer": "A new slide is inserted as third slide in presentation"
  },
  {
    "question_number": 57,
    "question": "To create another copy of a slide, what is the best way…?",
    "options": [
      "Click the slide then press Ctrl+A and paste in new slide",
      "Redo everything on a new slide that you had done on previous slide",
      "From Insert Menu choose Duplicate Slide",
      "None of above"
    ],
    "answer": "From Insert Menu choose Duplicate Slide"
  },
  {
    "question_number": 58,
    "question": "To access Picture, Test Box, Chart etc. which menu you have to select ?",
    "options": ["Insert", "View", "File", "Edit"],
    "answer": "Insert"
  },
  {
    "question_number": 59,
    "question": "Name the three options that are available in Insert >> Picture menu?",
    "options": ["Clipart, Pictures, AutoShapes", "Clipart, From Files, AutoShapes", "Clipart, Pictures, Shapes", "Clipart, From File, Shapes"],
    "answer": "Clipart, From Files, AutoShapes"
  },
  {
    "question_number": 60,
    "question": "What are the steps to insert slide numbers?",
    "options": [
      "Insert a text box and select Insert >> Page Number",
      "Choose Insert >> Slide Number",
      "Insert a new text box and select Insert >> slide Number",
      "Insert a textbox and select Insert >> Number >> PageNumber"
    ],
    "answer": "Insert a new text box and select Insert >> slide Number"
  },
  {
    "question_number": 61,
    "question": "In a slide, what are the steps to insert a hyperlink ?",
    "options": ["Press Ctrl + K", "Choose Insert >> Hyperlink", "Hyperlinks can’t be inserted in slides", "both a & b"],
    "answer": "both a & b"
  }
]

quiz_data_14= [
  {
    "question_number": 1,
    "question": "Which of the following is used to perform calculations in Excel?",
    "options": ["Tables", "Charts", "Formulas", "Macros"],
    "answer": "Formulas"
  },
  {
    "question_number": 2,
    "question": "What is the intersection of a row and a column called in Excel?",
    "options": ["Sheet", "Cell", "Range", "Formula"],
    "answer": "Cell"
  },
  {
    "question_number": 3,
    "question": "Which function is used to add up a range of cells?",
    "options": ["AVERAGE", "COUNT", "SUM", "MAX"],
    "answer": "SUM"
  },
  {
    "question_number": 4,
    "question": "What is the shortcut key to save an Excel workbook?",
    "options": ["Ctrl+S", "Ctrl+O", "Ctrl+N", "Ctrl+P"],
    "answer": "Ctrl+S"
  },
  {
    "question_number": 5,
    "question": "How do you select an entire column in Excel?",
    "options": ["Click on the row number", "Click on the column letter", "Ctrl+A", "Shift+Space"],
    "answer": "Click on the column letter"
  },
  {
    "question_number": 6,
    "question": "Which symbol is used to start a formula in Excel?",
    "options": ["#", "$", "=", "@"],
    "answer": "="
  },
  {
    "question_number": 7,
    "question": "What is the default file extension for an Excel workbook?",
    "options": [".txt", ".docx", ".xlsx", ".pdf"],
    "answer": ".xlsx"
  },
  {
    "question_number": 8,
    "question": "Which function is used to find the largest value in a range of cells?",
    "options": ["MIN", "MAX", "AVERAGE", "COUNT"],
    "answer": "MAX"
  },
  {
    "question_number": 9,
    "question": "What is the purpose of the fill handle in Excel?",
    "options": ["To delete cells", "To format cells", "To copy or extend data", "To create charts"],
    "answer": "To copy or extend data"
  },
  {
    "question_number": 10,
    "question": "Which feature is used to automatically fill a series of data?",
    "options": ["AutoSum", "AutoFill", "AutoCorrect", "AutoFormat"],
    "answer": "AutoFill"
  },
  {
    "question_number": 11,
    "question": "What does the 'AVERAGE' function calculate?",
    "options": ["Sum of values", "Highest value", "Lowest value", "Arithmetic mean"],
    "answer": "Arithmetic mean"
  },
  {
    "question_number": 12,
    "question": "How do you insert a new row in Excel?",
    "options": ["Click Insert > Column", "Click Insert > Row", "Ctrl+I", "Alt+R"],
    "answer": "Click Insert > Row"
  },
  {
    "question_number": 13,
    "question": "Which chart type is used to represent data as slices of a circle?",
    "options": ["Bar chart", "Line chart", "Pie chart", "Scatter plot"],
    "answer": "Pie chart"
  },
  {
    "question_number": 14,
    "question": "What is the purpose of conditional formatting in Excel?",
    "options": ["To create formulas", "To format cells based on conditions", "To insert charts", "To create macros"],
    "answer": "To format cells based on conditions"
  },
  {
    "question_number": 15,
    "question": "Which function is used to count the number of cells that contain numbers?",
    "options": ["COUNT", "COUNTA", "COUNTBLANK", "COUNTIF"],
    "answer": "COUNT"
  },
  {
    "question_number": 16,
    "question": "How do you freeze panes in Excel?",
    "options": ["View > Freeze Panes", "Insert > Freeze Panes", "Format > Freeze Panes", "Data > Freeze Panes"],
    "answer": "View > Freeze Panes"
  },
  {
    "question_number": 17,
    "question": "What does the 'VLOOKUP' function do?",
    "options": ["Calculates variance", "Looks up a value in a vertical range", "Creates visual effects", "Validates input data"],
    "answer": "Looks up a value in a vertical range"
  },
  {
    "question_number": 18,
    "question": "Which feature is used to filter data in Excel?",
    "options": ["Sort", "Filter", "PivotTable", "Conditional Formatting"],
    "answer": "Filter"
  },
  {
    "question_number": 19,
    "question": "What is a 'range' in Excel?",
    "options": ["A single cell", "A group of adjacent cells", "A formula", "A chart"],
    "answer": "A group of adjacent cells"
  },
  {
    "question_number": 20,
    "question": "Which function is used to concatenate text strings?",
    "options": ["ADD", "JOIN", "CONCATENATE", "MERGE"],
    "answer": "CONCATENATE"
  },
  {
    "question_number": 21,
    "question": "How do you hide a column in Excel?",
    "options": ["Format > Hide Column", "View > Hide Column", "Right-click > Hide", "Data > Hide Column"],
    "answer": "Right-click > Hide"
  },
  {
    "question_number": 22,
    "question": "What is a PivotTable used for?",
    "options": ["To create charts", "To summarize and analyze data", "To insert images", "To create formulas"],
    "answer": "To summarize and analyze data"
  },
  {
    "question_number": 23,
    "question": "Which symbol is used for absolute cell referencing?",
    "options": ["#", "$", "@", "%"],
    "answer": "$"
  },
  {
    "question_number": 24,
    "question": "What is the purpose of the 'IF' function?",
    "options": ["To calculate averages", "To perform conditional tests", "To count cells", "To create charts"],
    "answer": "To perform conditional tests"
  },
  {
    "question_number": 25,
    "question": "How do you merge cells in Excel?",
    "options": ["Format > Merge Cells", "View > Merge Cells", "Home > Merge & Center", "Data > Merge Cells"],
    "answer": "Home > Merge & Center"
  },
  {
    "question_number": 26,
    "question": "Which function is used to count the number of non-empty cells?",
    "options": ["COUNT", "COUNTA", "COUNTBLANK", "COUNTIF"],
    "answer": "COUNTA"
  },
  {
    "question_number": 27,
    "question": "What is the purpose of data validation in Excel?",
    "options": ["To create formulas", "To restrict data input", "To insert charts", "To format cells"],
    "answer": "To restrict data input"
  },
  {
    "question_number": 28,
    "question": "How do you rename a worksheet?",
    "options": ["File > Rename", "View > Rename", "Right-click on sheet tab > Rename", "Data > Rename"],
    "answer": "Right-click on sheet tab > Rename"
  },
  {
    "question_number": 29,
    "question": "Which chart type displays trends over time?",
    "options": ["Bar chart", "Line chart", "Pie chart", "Scatter plot"],
    "answer": "Line chart"
  },
  {
    "question_number": 30,
    "question": "What is a 'macro' in Excel?",
    "options": ["A formula", "A chart", "An automated task", "A data filter"],
    "answer": "An automated task"
  }
]

quiz_data_15 = [
  {
    "question_number": 1,
    "question": "What is the shortcut for saving a document?",
    "options": ["Ctrl + S", "Ctrl + N", "Ctrl + O", "Ctrl + P"],
    "answer": "Ctrl + S"
  },
  {
    "question_number": 2,
    "question": "What is the shortcut for creating a new document?",
    "options": ["Ctrl + S", "Ctrl + N", "Ctrl + O", "Ctrl + P"],
    "answer": "Ctrl + N"
  },
  {
    "question_number": 3,
    "question": "What is the shortcut for opening an existing document?",
    "options": ["Ctrl + S", "Ctrl + N", "Ctrl + O", "Ctrl + P"],
    "answer": "Ctrl + O"
  },
  {
    "question_number": 4,
    "question": "What is the shortcut for printing a document?",
    "options": ["Ctrl + S", "Ctrl + N", "Ctrl + O", "Ctrl + P"],
    "answer": "Ctrl + P"
  },
  {
    "question_number": 5,
    "question": "What is the shortcut for undoing the last action?",
    "options": ["Ctrl + Z", "Ctrl + Y", "Ctrl + X", "Ctrl + C"],
    "answer": "Ctrl + Z"
  },
  {
    "question_number": 6,
    "question": "What is the shortcut for redoing the last undone action?",
    "options": ["Ctrl + Z", "Ctrl + Y", "Ctrl + X", "Ctrl + C"],
    "answer": "Ctrl + Y"
  },
  {
    "question_number": 7,
    "question": "What is the shortcut for cutting selected text?",
    "options": ["Ctrl + Z", "Ctrl + Y", "Ctrl + X", "Ctrl + C"],
    "answer": "Ctrl + X"
  },
  {
    "question_number": 8,
    "question": "What is the shortcut for copying selected text?",
    "options": ["Ctrl + Z", "Ctrl + Y", "Ctrl + X", "Ctrl + C"],
    "answer": "Ctrl + C"
  },
  {
    "question_number": 9,
    "question": "What is the shortcut for pasting copied or cut text?",
    "options": ["Ctrl + V", "Ctrl + A", "Ctrl + S", "Ctrl + P"],
    "answer": "Ctrl + V"
  },
  {
    "question_number": 10,
    "question": "What is the shortcut for selecting all text?",
    "options": ["Ctrl + V", "Ctrl + A", "Ctrl + S", "Ctrl + P"],
    "answer": "Ctrl + A"
  },
  {
    "question_number": 11,
    "question": "What is the shortcut for creating a new workbook?",
    "options": ["Ctrl + N", "Ctrl + S", "Ctrl + O", "Alt + ="],
    "answer": "Ctrl + N"
  },
  {
    "question_number": 12,
    "question": "What is the shortcut for saving a workbook?",
    "options": ["Ctrl + N", "Ctrl + S", "Ctrl + O", "Alt + ="],
    "answer": "Ctrl + S"
  },
  {
    "question_number": 13,
    "question": "What is the shortcut for opening an existing workbook?",
    "options": ["Ctrl + N", "Ctrl + S", "Ctrl + O", "Alt + ="],
    "answer": "Ctrl + O"
  },
  {
    "question_number": 14,
    "question": "What is the shortcut to select an entire column?",
    "options": ["Ctrl + Space", "Shift + Space", "Alt + =", "Ctrl + 1"],
    "answer": "Ctrl + Space"
  },
  {
    "question_number": 15,
    "question": "What is the shortcut to select an entire row?",
    "options": ["Ctrl + Space", "Shift + Space", "Alt + =", "Ctrl + 1"],
    "answer": "Shift + Space"
  },
  {
    "question_number": 16,
    "question": "What is the shortcut to apply the AutoSum function?",
    "options": ["Ctrl + Space", "Shift + Space", "Alt + =", "Ctrl + 1"],
    "answer": "Alt + ="
  },
  {
    "question_number": 17,
    "question": "What is the shortcut to open the Format Cells dialog box?",
    "options": ["Ctrl + Space", "Shift + Space", "Alt + =", "Ctrl + 1"],
    "answer": "Ctrl + 1"
  },
  {
    "question_number": 18,
    "question": "What is the shortcut for creating a new presentation?",
    "options": ["Ctrl + N", "Ctrl + S", "Ctrl + O", "F5"],
    "answer": "Ctrl + N"
  },
  {
    "question_number": 19,
    "question": "What is the shortcut for saving a presentation?",
    "options": ["Ctrl + N", "Ctrl + S", "Ctrl + O", "F5"],
    "answer": "Ctrl + S"
  },
  {
    "question_number": 20,
    "question": "What is the shortcut for opening an existing presentation?",
    "options": ["Ctrl + N", "Ctrl + S", "Ctrl + O", "F5"],
    "answer": "Ctrl + O"
  },
  {
    "question_number": 21,
    "question": "What is the shortcut to start a slide show from the beginning?",
    "options": ["Ctrl + M", "F5", "F7", "F12"],
    "answer": "F5"
  },
  {
    "question_number": 22,
    "question": "What is the shortcut to insert a new slide?",
    "options": ["Ctrl + M", "F5", "F7", "F12"],
    "answer": "Ctrl + M"
  },
  {
    "question_number": 23,
    "question": "What does the F1 key typically do in most Windows applications?",
    "options": ["Opens Help", "Edit cell", "Find next", "Repeat action"],
    "answer": "Opens Help"
  },
  {
    "question_number": 24,
    "question": "What does the F2 key typically do in Excel?",
    "options": ["Opens Help", "Edit cell", "Find next", "Repeat action"],
    "answer": "Edit cell"
  },
  {
    "question_number": 25,
    "question": "What does the F3 key typically do in some applications' find dialog boxes?",
    "options": ["Opens Help", "Edit cell", "Find next", "Repeat action"],
    "answer": "Find next"
  },
  {
    "question_number": 26,
    "question": "What does the F4 key typically do in Word?",
    "options": ["Opens Help", "Edit cell", "Find next", "Repeat action"],
    "answer": "Repeat action"
  },
  {
    "question_number": 27,
    "question": "What does the F5 key typically do in a web browser or PowerPoint?",
    "options": ["Refresh page/Start slideshow", "Spelling check", "Save As", "Open Dialog"],
    "answer": "Refresh page/Start slideshow"
  },
  {
    "question_number": 28,
    "question": "What does the F7 key typically do in MS Office applications?",
    "options": ["Refresh page/Start slideshow", "Spelling check", "Save As", "Open Dialog"],
    "answer": "Spelling check"
  },
  {
    "question_number": 29,
    "question": "What does the F12 key typically do in MS Office applications?",
    "options": ["Refresh page/Start slideshow", "Spelling check", "Save As", "Open Dialog"],
    "answer": "Save As"
  },
  {
    "question_number": 30,
    "question": "what does Ctrl + F12 do in MS word?",
    "options": ["Refresh page/Start slideshow", "Spelling check", "Save As", "Opens the open dialog box."],
    "answer": "Opens the open dialog box."
  }
]
quiz_sets = {
    "Quiz 1": quiz_data_1,
    "Quiz 2": quiz_data_2,
    "Quiz 3": quiz_data_3,
    "Quiz 4": quiz_data_4,
    "Quiz 5": quiz_data_5,
    "Quiz 6": quiz_data_6,
    "Quiz 7": quiz_data_7,
    "MS Word 1": quiz_data_8,
    "MS Word 2": quiz_data_9,
    "MS Word 3": quiz_data_10,
    "MS Word 4": quiz_data_11,
    "MS Powerpoint 1": quiz_data_12, 
    "MS Powerpoint 2": quiz_data_13,     
    "MS Excel":  quiz_data_14,
    "Shortcuts": quiz_data_15

}

# Initialize session state
if 'selected_quiz' not in st.session_state:
    st.session_state.selected_quiz = None
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.show_result = False
    st.session_state.responses = []  # Store user responses

# Quiz selection
if st.session_state.selected_quiz is None:
    st.subheader("Select a Quiz to Begin")
    quiz_choice = st.selectbox("Choose a quiz topic:", list(quiz_sets.keys()))
    if st.button("Start Quiz"):
        st.session_state.selected_quiz = quiz_choice
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.show_result = False
        st.session_state.responses = []
        st.rerun()

# Proceed with the selected quiz
if st.session_state.selected_quiz:
    quiz_data = quiz_sets[st.session_state.selected_quiz]
    
    # Function to check answer
    def check_answer(selected_option):
        question_data = quiz_data[st.session_state.current_question]
        correct_answer = question_data["answer"]
        st.session_state.show_result = True
        
        # Store response
        st.session_state.responses.append({
            "question_number": question_data["question_number"],
            "question": question_data["question"],
            "selected_option": selected_option,
            "correct_answer": correct_answer,
            "is_correct": selected_option == correct_answer
        })
        
        if selected_option == correct_answer:
            st.session_state.score += 1

    # Display question if within bounds
    if st.session_state.current_question < len(quiz_data):
        question_data = quiz_data[st.session_state.current_question]
        st.subheader(f"Question {question_data['question_number']}")
        st.write(question_data["question"])
        
        selected_option = st.radio("Select an answer:", question_data["options"], index=None)
        
        if st.button("Submit"):
            if selected_option:
                check_answer(selected_option)
                st.rerun()

        if st.session_state.show_result:
            correct_answer = question_data["answer"]
            if selected_option == correct_answer:
                st.success("Correct!")
            else:
                st.error(f"Wrong! The correct answer is: {correct_answer}")
            
            if st.button("Next Question"):
                st.session_state.current_question += 1
                st.session_state.show_result = False
                st.rerun()
    
    else:
        st.success(f"Quiz Completed! Your final score is {st.session_state.score}/{len(quiz_data)}")
        
        # Format responses into a text report
        responses_text = "Quiz Results:\n\n"
        for resp in st.session_state.responses:
            responses_text += f"Q{resp['question_number']}: {resp['question']}\n"
            responses_text += f"Your Answer: {resp['selected_option']}\n"
            responses_text += f"Correct Answer: {resp['correct_answer']}\n"
            responses_text += f"Result: {'✅ Correct' if resp['is_correct'] else '❌ Incorrect'}\n"
            responses_text += "-" * 50 + "\n"

        # Provide a download button for the quiz report
        st.download_button(
            label="Download Quiz Report",
            data=responses_text,
            file_name="quiz_results.txt",
            mime="text/plain"
        )
        
        if st.button("Restart Quiz"):
            st.session_state.selected_quiz = None
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.show_result = False
            st.session_state.responses = []
            st.rerun()
