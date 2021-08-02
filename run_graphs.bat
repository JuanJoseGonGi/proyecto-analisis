SET PYPHI_WELCOME_OFF='yes'
SET PYTHONIOENCODING='utf8'

for %%f in (graphs/*) do (
  echo "----------" >> results_bat.txt
  echo %%f >> results_bat.txt
  python graphs/%%f >> results_bat.txt
)
