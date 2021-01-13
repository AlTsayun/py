@echo off
SET batPath=%~dp0
python "%batPath%impl\MergePdfs.py" %*
pause