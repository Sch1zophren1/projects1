Dateks info scraper - Automatizēta cenu apkopotāja sistēma

Projekta uzdevums

Projekts "Dateks info scraper" ir izstrādāts, lai automatizētu cenu apkopojumu no interneta veikala **Dateks.lv** un sagatavotu statistikas pārskatus par datoru produktiem. Programma izmanto tīmekļa skrāpēšanu, lai iegūtu datus no majaslapas, un pēc tam tos klasificē pēc cenu diapazoniem. Rezultāti tiek saglabāti Excel failā, kur tiek norādīta katra produkta informācija, kā arī tās kategorija atbilstoši cenai.

Projekta mērķis ir palīdzēt lietotājiem iegūt datus par portatīvajiem datoriem un automātiski veikt to analīzi, lai varētu ērti salīdzināt dažādos cenu diapazonos pieejamos produktus.
(Projects var izmantots jebkuram kategorijam dateks internet veikala, jo visa informacija ir html koda nevis dinamiska no js, vajag tikai samainit kategorijas cenas)

📊 Rezultāta pārskatā iekļautā informācija:
- Produktu skaits pēc cenu kategorijām
- Nosaukums, cena un saite uz produktu
- Kategorijas noteikšana atbilstoši cenai (piemēram, "Līdz 500 €", "No 500 € līdz 1500 €", utt.)

Programma automatizē šo datu apstrādi, lai lietotājs varētu koncentrēties uz analīzes un interpretācijas uzdevumiem.

 Izmantotās Python bibliotēkas

📦 Trešo pušu bibliotēkas:

1. requests — tīmekļa datu ieguvei.
   - Kāpēc tiek izmantota? Tā tiek izmantota, lai veiktu HTTP pieprasījumus un iegūtu datus no tīmekļa lapām.

2. BeautifulSoup (no `bs4`) — HTML datu parsēšanai un produktu informācijas iegūšanai.
   Kāpēc tiek izmantota? Tā ļauj efektīvi apstrādāt HTML struktūras un izvilkt nepieciešamos datus, piemēram, produkta nosaukumu, cenu un saiti.

3. openpyxl — darbam ar Excel failiem.
   Kāpēc tiek izmantota? Tā nodrošina iespēju saglabāt produktus un to informāciju Excel failā.

📚 Standarta Python moduļi:

1. re — regulāro izteiksmju izmantošanai.
   Kāpēc tiek izmantota? Regulārie izteiksmji tiek izmantoti, lai apstrādātu cenas un noņemtu liekos simbolus.


Datu struktūras

Projekta izstrādē tika izmantotas šādas pašdefinētas datu struktūras:

1. Product: Klase, kas attēlo katru produktu, saglabājot tā nosaukumu, cenu, saiti un kategoriju.
   - Kategorija tiek noteikta atbilstoši cenu diapazonam (piemēram, "Līdz 500 €", "No 500 € līdz 1500 €", utt.).

2. CategoryNode: Klase, kas pārstāv katru kategoriju un satur sarakstu ar produktiem, kas atbilst šai kategorijai.
   - Katras kategorijas produkti tiek saglabāti atsevišķi, lai būtu viegli piekļūt un analizēt katru kategoriju atsevišķi.

3. Catalog: Klase, kas pārvalda visu katalogu un nodrošina iespēju pievienot produktus attiecīgajām kategorijām, kā arī saglabāt datus Excel failā.
   - Šī klase arī palīdz nodrošināt strukturētu piekļuvi katrai kategorijai.

 Programmatūras izmantošanas metodes

1. Lapas ielāde un datu iegūšana: Lietotājs ievada, cik daudz lapu no Dateks.lv vēlas apstrādāt. Programmatūra izmanto `requests` un `BeautifulSoup`, lai iegūtu datus no tīmekļa lapām.

2. Produktu kategorizēšana: Katram produktam tiek aprēķināta cena un piešķirta atbilstošā kategorija (piemēram, "Līdz 500 €", "No 500 € līdz 1500 €", utt.).

3. Datu saglabāšana Excel failā: Kad visi dati ir iegūti, tie tiek saglabāti Excel failā. Katras kategorijas produkti tiek saglabāti atsevišķās lapās Excel dokumentā.

4. Programmas darbība: Lietotājs var izvēlēties, cik lapu vēlas apskatīt. Programmatūra apstrādā šīs lapas un pēc tam saglabā rezultātus Excel failā.

Kā uzsākt darbu

1. Instalējiet nepieciešamās Python bibliotēkas terminala:

   pip install requests beautifulsoup4 openpyxl


2. Lejupielādējiet vai kopējiet projekta failus un palaidiet skriptu

3. Sekojiet norādījumiem ekrānā, lai norādītu, cik daudz lapu vēlaties apskatīt un izvēlētos failu saglabāšanas vietu.

4. Rezultāts: Kad process ir pabeigts, iegūstiet saglabāto Excel failu ar visiem produktiem un to kategorijām.

Projects tika taisits pedeja bridi , tapec ka no sakuma bija planots taisit ar biedru, bet viņš pardomaja un tapec viss bija izplidits 5 stundu laika pycharm iekša bez komitiem.



