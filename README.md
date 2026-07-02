# Tray-FM
Ελληνόφωνα ραδιόφωνα στο system tray

## Το Sheldio με system tray

Ελληνόφωνοι ραδιοφωνικοί σταθμοί στο system tray του συστήματός σας.
Βασίζεται στο Sheldio, αλλά αντί να τρέχει στο bash δημιουργεί ένα indicator στο πάνελ του συστήματός σας.

Αρχικό πρότζεκτ: https://github.com/CerebruxCode/shelldio

### Οδηγίες εγκατάστασης

Το Tray-FM είναι συμβατό με Linux.
Το κατεβάζετε, το αποσυμπιέζετε, το κάνετε εκτελέσιμο και το τρέχετε.

### Προαπαιτούμενα  
- python3  
- mpv  
- PyGObject  
- Ayatana AppIndicator

Θα τα βρείτε όλα στους Διαχειριστές Λογισμικού της διανομής σας.

### Στα to-do για τις αμέσως επόμενες εκδόσεις:

- Πλήρες GTK tray app
- Metadata από το mpv socket (`media-title`)
- Notifications
- MPRIS
- .desktop` + autostart
- Binary μέσω PyInstaller
- deb πακέτο
- AppImage πακέτο
- Υπομενού Favorites
- Υπομενού All Stations
- Αναζήτηση σταθμού
- Εμφάνιση τρέχοντος σταθμού στο tooltip
- Αποθήκευση τελευταίου σταθμού
- Ανάγνωση metadata από το IPC socket του mpv στο tooltip του indicator
- Desktop notifications όταν αλλάζει τραγούδι
- MPRIS integration
- Να φαίνεται στα media controls του Cinnamon
- Play / Stop από multimedia keys

Οι εκδόσεις  με τις ανωτέρω προσθήκες θα κυκλοφορούν διαδοχικά. 
