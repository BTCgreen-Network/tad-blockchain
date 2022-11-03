!include "nsDialogs.nsh"

; Add our customizations to the finish page
!macro customFinishPage
XPStyle on

Var DetectDlg
Var FinishDlg
Var TadSquirrelInstallLocation
Var TadSquirrelInstallVersion
Var TadSquirrelUninstaller
Var CheckboxUninstall
Var UninstallTadSquirrelInstall
Var BackButton
Var NextButton

Page custom detectOldTadVersion detectOldTadVersionPageLeave
Page custom finish finishLeave

; Add a page offering to uninstall an older build installed into the tad-blockchain dir
Function detectOldTadVersion
  ; Check the registry for old tad-blockchain installer keys
  ReadRegStr $TadSquirrelInstallLocation HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\tad-blockchain" "InstallLocation"
  ReadRegStr $TadSquirrelInstallVersion HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\tad-blockchain" "DisplayVersion"
  ReadRegStr $TadSquirrelUninstaller HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\tad-blockchain" "QuietUninstallString"

  StrCpy $UninstallTadSquirrelInstall ${BST_UNCHECKED} ; Initialize to unchecked so that a silent install skips uninstalling

  ; If registry keys aren't found, skip (Abort) this page and move forward
  ${If} TadSquirrelInstallVersion == error
  ${OrIf} TadSquirrelInstallLocation == error
  ${OrIf} $TadSquirrelUninstaller == error
  ${OrIf} $TadSquirrelInstallVersion == ""
  ${OrIf} $TadSquirrelInstallLocation == ""
  ${OrIf} $TadSquirrelUninstaller == ""
  ${OrIf} ${Silent}
    Abort
  ${EndIf}

  ; Check the uninstall checkbox by default
  StrCpy $UninstallTadSquirrelInstall ${BST_CHECKED}

  ; Magic create dialog incantation
  nsDialogs::Create 1018
  Pop $DetectDlg

  ${If} $DetectDlg == error
    Abort
  ${EndIf}

  !insertmacro MUI_HEADER_TEXT "Uninstall Old Version" "Would you like to uninstall the old version of Tad Blockchain?"

  ${NSD_CreateLabel} 0 35 100% 12u "Found Tad Blockchain $TadSquirrelInstallVersion installed in an old location:"
  ${NSD_CreateLabel} 12 57 100% 12u "$TadSquirrelInstallLocation"

  ${NSD_CreateCheckBox} 12 81 100% 12u "Uninstall Tad Blockchain $TadSquirrelInstallVersion"
  Pop $CheckboxUninstall
  ${NSD_SetState} $CheckboxUninstall $UninstallTadSquirrelInstall
  ${NSD_OnClick} $CheckboxUninstall SetUninstall

  nsDialogs::Show

FunctionEnd

Function SetUninstall
  ; Set UninstallTadSquirrelInstall accordingly
  ${NSD_GetState} $CheckboxUninstall $UninstallTadSquirrelInstall
FunctionEnd

Function detectOldTadVersionPageLeave
  ${If} $UninstallTadSquirrelInstall == 1
    ; This could be improved... Experiments with adding an indeterminate progress bar (PBM_SETMARQUEE)
    ; were unsatisfactory.
    ExecWait $TadSquirrelUninstaller ; Blocks until complete (doesn't take long though)
  ${EndIf}
FunctionEnd

Function finish

  ; Magic create dialog incantation
  nsDialogs::Create 1018
  Pop $FinishDlg

  ${If} $FinishDlg == error
    Abort
  ${EndIf}

  GetDlgItem $NextButton $HWNDPARENT 1 ; 1 = Next button
  GetDlgItem $BackButton $HWNDPARENT 3 ; 3 = Back button

  ${NSD_CreateLabel} 0 35 100% 12u "Tad has been installed successfully!"
  EnableWindow $BackButton 0 ; Disable the Back button
  SendMessage $NextButton ${WM_SETTEXT} 0 "STR:Let's Farm!" ; Button title is "Close" by default. Update it here.

  nsDialogs::Show

FunctionEnd

; Copied from electron-builder NSIS templates
Function StartApp
  ${if} ${isUpdated}
    StrCpy $1 "--updated"
  ${else}
    StrCpy $1 ""
  ${endif}
  ${StdUtils.ExecShellAsUser} $0 "$launchLink" "open" "$1"
FunctionEnd

Function finishLeave
  ; Launch the app at exit
  Call StartApp
FunctionEnd

; Section
; SectionEnd
!macroend
