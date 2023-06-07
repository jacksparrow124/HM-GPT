import json 
class Settings:
    recognizer = None

    def __init__(self) -> None:
        pass
        
        
    def Settings(self):   
        Settings = ({
        "python.analysis.typeCheckingMode": "basic",
        "python.languageServer": "Pylance",
        "python.linting.pylintEnabled": False,
        "python.analysis.diagnosticSeverityOverrides": {
            "reportMissingModuleSource": "none",
            "reportDuplicateImport": "information",
            "reportMissingImports": "error", 
        
        },
        "python.analysis.extraPaths": [
            "",
            "c:\\Users\\smith\\.vscode\\extensions\\joedevivo.vscode-circuitpython-0.1.20-win32-x64\\stubs",
            "c:\\Users\\smith\\AppData\\Roaming\\Code\\User\\globalStorage\\joedevivo.vscode-circuitpython\\bundle\\20230508\\adafruit-circuitpython-bundle-py-20230508\\lib"
        ],
        "circuitpython.board.version": None
    })

 
