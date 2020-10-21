mkdir _converted
for %%a in (Mesh/*.mesh) do ConvertData_Rebellion mesh Mesh/%%a _converted/%%a txt
for %%a in (_converted/*.mesh) do python conv.py _converted/%%a _converted
