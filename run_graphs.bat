SET PYPHI_WELCOME_OFF='yes'
SET PYTHONIOENCODING='utf8'

for %%f in (graphs/*) do (
  echo %%f >> results.txt
  python graphs/%%f >> results.txt
)
