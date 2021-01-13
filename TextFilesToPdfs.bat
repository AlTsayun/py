@echo off
SET batPath=%~dp0
python "%batPath%impl\TextFilesToPdfs.py" %*
pause