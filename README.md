# TM
## Installation pour l'importation de données Excel dans MySQL
1. Télécharger les fichiers ImportExcelToMySQL.py, PlotlyDashFromMySQLdata.py et divorces (copy).xls.
2. Installer Visual Studio Code comme IDE (ma préférence) https://code.visualstudio.com/
3. Installer Python v.3.8.5 64bit https://www.python.org/downloads/release/python-385/
4. Installer mysql.connector https://dev.mysql.com/downloads/connector/odbc/
5. Installer xlrd ```pip install xlrd```
6. Installer MySQL https://dev.mysql.com/downloads/installer/ Ce tutoriel peut aider à mettre en place la base donnée https://ladvien.com/data-analytics-mysql-localhost-setup/ Attention à créér votre serveur avec ces informations sinon il faudra adapter le code à vos informations:   
```host="localhost", user="python", password="Travail_Maturite2021", database="statistiques"```
7. Installer MySQL Workbench pour créer le contenu de la base donnée https://www.mysql.com/fr/products/workbench/
8. Dans MySQL Workbench créer un tableau divorce et les colonnes comme sur ces images :

![image](https://user-images.githubusercontent.com/73735756/135769535-5a2babb0-e9a0-4ee2-880f-04790517fa61.png)
![Capture d’écran 2021-10-03 220030](https://user-images.githubusercontent.com/73735756/135769622-f05e4b89-7636-4428-bad4-fb909568fffe.png)

9. Lancer le programme ImportExcelToMySQL.py

## Installation pour créer un graphique dans une page web à l'aide de données MySQL
1. Installer Plotly ```pip install plotly==4.12.0```
2. Installer Dash ```pip install dash```
3. Installer les composants DAQ pour Dash ```pip install dash-daq```
4. Installer pandas ```pip install pandas```
5. Installer la version d'essai de cdata.mysql à l'aide du fichier readme.txt obtenu après téléchargement https://www.cdata.com/drivers/mysql/download/python/
Il requiert l'installation du paquet ".whl" et l'activation de la licence en mode version d'essai.
Sur Windows :
```pip install cdata_mysql_connector-21.0.7930-cp37-cp37-win_amd64.whl```
Pour la licence (cité du fichier readme.txt) :
"After the installation, a separate step must be done to activate a license for the connector. Among
the CData assets in the distribution's site packages, there should be an install-license tool that
will activate this license. From the python distribution's site-packages folder, after navigating
to the "cdata/installlic_mysql" folder, simply use a command like the below to
activate the license. Omitting the <key> argument will activate a trial license:
Windows:
```./install-license.exe <key>```
6. Lancer le programme PlotlyDashFromMySQLdata.py

### Remarques:
- Si la commande pip ne marche pas essayer de remplacer ```pip``` par ```pip3```
