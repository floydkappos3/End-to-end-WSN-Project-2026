# TinyOS Setup Guide: Ubuntu 16.04 on VirtualBox

This guide explains how to set up Ubuntu 16.04 in VirtualBox, configure
USB access for TelosB and Iris motes, and install TinyOS.

------------------------------------------------------------------------

## 1. Download and Install Required Software

Download and install the following:

-   VirtualBox
-   VirtualBox Extension Pack
-   Ubuntu 16.04 ISO

**Make sure you check the "Install Guest Additions" option in the "Set up unattended guest OS installation" when installing Ubuntu 16.04 LTS in the Virtual Box.** 

------------------------------------------------------------------------

## 2. Enable `sudo` and Terminal Access

Boot Ubuntu 16.04 into recovery mode:

1.  While Ubuntu 16.04 LTS is booting, hold the **SHIFT** key.

2.  Choose:

    ``` text
    Advanced Options for Ubuntu -> <kernel_version> (recovery mode)
    ```

3.  Choose **root** and press **ENTER**.

Remount the filesystem as writable:

``` bash
mount -o remount,rw /
```

Add your user to the `sudo` group:

``` bash
adduser <your_username> sudo
```

Edit the locale file:

``` bash
nano /etc/default/locale
```

Update the entries so that all values are:

``` text
en_US.UTF-8
```

Save and exit, then run:

``` bash
locale-gen
reboot
```

Verify terminal access after reboot:

1.  Log in to Ubuntu 16.04.
2.  Press:

``` text
Ctrl + Alt + T
```

------------------------------------------------------------------------

## 3. Add User to `vboxusers` in the host machine (only if the host machine is Linux based)

``` bash
sudo adduser $USER vboxusers
```

Then log out and back in, or reboot.

------------------------------------------------------------------------

## 4. Install VirtualBox Recommendations

Add the VirtualBox Extension Pack:

Extensions > Install > \<the downloaded extension pack\>

------------------------------------------------------------------------

## 5. Configure USB Devices in VirtualBox

1.  Close the VM.

2.  Plug in the TelosB and Iris motes.

3.  In VirtualBox, right-click the VM.

4.  Go to:

    ``` text
    Settings -> USB
    ```

5.  Click **Add Filter**.

6.  Choose the Iris and TelosB motes.

------------------------------------------------------------------------

## 6. Update and Upgrade Packages

Run:

``` bash
sudo apt update && sudo apt upgrade
```

------------------------------------------------------------------------

## 7. Install Necessary Packages

Run:

``` bash
sudo apt install -y python2.7 python-minimal openjdk-8-jdk gcc-avr avr-libc nescc minicom wget unzip automake autoconf libtool avrdude curl gcc-msp430 git python-serial tinyos-tools
```

------------------------------------------------------------------------

## 8. Install TinyOS

Clone the TinyOS repository:

``` bash
git clone https://github.com/tinyos/tinyos-main.git
```

Go into the TinyOS tools directory:

``` bash
cd ~/tinyos-main/tools
```

Build and install TinyOS tools:

``` bash
./Bootstrap
./configure
make
sudo make install
```

------------------------------------------------------------------------

## 9. Configure USB Permissions

Add your user to the `dialout` group:

``` bash
sudo usermod -aG dialout $USER
```

Reboot:

``` bash
reboot
```

## 10. Create Shared Folder

1. Close the VM
2. Go to Settings > Shared Folders > Add new shared folder
3. Pick a folder (or better, create a new one to the Host machine and choose this one)
4. Check the auto-mount option
5. apply changes and open the VM
6. In the terminal, run:
``` bash
sudo usermod -aG vboxsf $USER
```
7. Log-out and login back or reboot

------------------------------------------------------------------------

## Done

Ubuntu 16.04, TinyOS, and mote USB access should now be configured.

# Περαιτέρω οδηγίες

## Σχετικά με τις μετρήσεις

1. Όσες ομάδες έχουν TelosB mote, να χρησιμοποιήσουν τους πραγματικούς sensors του TelosB
2. Όσες ομάδες δεν έχουν TelosB mote, να χρησιμοποιήσουν 'fake' μετρήσεις.

Συγκεκριμένα, μελετήστε το παράδειγμα Sensing. Όσοι έχουν TelosB, να χρησιμοποιήσουν το tmote_onboard_sensors module, ενώ όσοι δεν έχουν να χρησιμοποιήσουν το universal_sensors module. Περισσότερες λεπτομέρειες στο README του παραδείγματος.

## Εύρεση των θυρών USB

Για να βρείτε σε ποιά θύρα USB είναι συνδεδεμένο το mote, χρησιμοποιήστε την παρακάτω εντολή:

``` bash
ls /dev | grep ttyUSB* 
```

## Compile and Flash programs

### TelosB

Για να φορτώσετε κώδικα στα TelosB εκτελείτε τις παρακάτω εντολές:

``` bash
sudo make clean  // Optional, but useful sometimes
sudo make telosb install.<TOS_NODE_ID>  bsl,/dev/ttyUSBx  // Βρείτε τη θύρα USB στην οποία είναι συνδεδεμένη η συσκευή σας
```

Παράδειγμα εκτέλεσης:

``` bash
sudo make clean
sudo make telosb install.0 bsl,/dev/ttyUSB0 // Εδώ περνάμε TOS_NODE_ID=0 και το mote είναι συνδεδεμένο στη θύρα USB0
```

### IRIS

Αντίστοιχα, για τα IRIS χρησιμοποιήστε τις παρακάτω εντολές:
``` bash
sudo make clean
sudo make iris install.<TOS_NODE_ID> mib520,/dev/ttyUSBx  // Βρείτε τη θύρα USB στην οποία είναι συνδεδεμένη η συσκευή σας
```

Παράδειγμα εκτέλεσης:

``` bash
sudo make clean
sudo make telosb install.0 bsl,/dev/ttyUSB0 // Εδώ περνάμε TOS_NODE_ID=0 και το mote είναι συνδεδεμένο στη θύρα USB0
```

**Προσοχη: Όταν συνδέσετε ένα TelosB mote, θα δείτε ότι εμφανίζει μία μόνο θύρα USB στον φάκελο /dev. Ωστόσο, για το IRIS mote, εμφανίζει 2 θύρες. Θα χρησιμοποιήσετε την 1η θύρα μόνο κατα τη διαδικασία flash την εφαρμογής σας και τη δεύτερη θύρα μόνο όταν θέλετε να διαβάσετε output της συσκευής (π.χ. τα αποτελέσματα των printf εντολών σας).**

## PrintfClient

Αν γράψετε printf εντολές, τότε πρέπει να ξεκινήσετε έναν PrintfClient για να μπορέσετε να δείτε τα αποτελέσματα των printf εντολών. Για να το κάνετε, εκτελέστε μία από τις παρακάτω εντολές, ανάλογα με το mote που θέλετε να ελέγξετε:

### TelosB

``` bash
sudo java net.tinyos.tools.PrintfClient -comm serial@/dev/ttyUSBx:telosb   // Βρείτε τη θύρα USB στην οποία είναι συνδεδεμένο το mote
```

### IRIS
```bash
sudo java net.tinyos.tools.PrintfClient -comm serial@/dev/ttyUSBx:iris   // Βρείτε τη θύρα USB στην οποία είναι συνδεδεμένο το mote
```

## SerialForwarder

Προτείνουμε, αντί να ξεκινήσετε έναν Client ο οποίος θα "μιλάει" κατευθείαν με τη θύρα USB, μπορείτε να ξεκινήσετε ένα Network Socket, το οποίο θα "μιλάει" με τη συσκευή μέσω UART και o Client θα "μιλάει" με το Network Socket. Γενικά, είναι πιο stable σαν μέθοδος. Επίσης, optionally μπορείτε να χρησιμοποιήσετε και το δικό σας port number. Το default είναι 9002.

### TelosB (Παράδειγμα για PrintfClient)
``` bash
sudo java net.tinyos.sf.SerialForwarder -comm serial@/dev/ttyUSB*:telosb <-port 9002> // Βρείτε τη θύρα USB στην οποία είναι συνδεδεμένο το mote
sudo java net.tinyos.tools.PrintfClient -comm sf@localhost:<port>
```

### IRIS (Παράδειγμα για PrintfClient)
``` bash
sudo java net.tinyos.sf.SerialForwarder -comm serial@/dev/ttyUSB*:iris <-port 9002> // Βρείτε τη θύρα USB στην οποία είναι συνδεδεμένο το mote
sudo java net.tinyos.tools.PrintfClient -comm sf@localhost:<port>
```


# Προτάσεις

Δείτε αναλυτικά τα παρακάτω παραδείγματα που περιέχονται στη βιβλιοθήκη, καθώς και τα παραδείγματα (examples) που δίνονται στο παρόν Repository:

1. examples/Blink
2. examples/BlinkToRadio
3. examples/Sensing

Τα παραδείγματα αυτά είναι παραλλαγές των αρχικών παραδειγμάτων του TinyOS:

1. apps/Blink
2. apps/tutorials/BlinkToRadio
3. examples/LowPowerSensing

# Αναφορά

Σε αυτό το section γράψτε μία σύντομη αναφορά σχετικά με την υλοποίηση και τα βήματα της άσκησης.

## 1ο μέρος
## 1ο μέρος

Στο πρώτο μέρος ασχολήθηκα με την εγκατάσταση και τη ρύθμιση του περιβάλλοντος TinyOS ώστε να μπορέσω να χρησιμοποιήσω τα motes TelosB και IRIS.

Αρχικά εγκατέστησα τα απαραίτητα εργαλεία και βιβλιοθήκες και έλεγξα ότι οι συσκευές αναγνωρίζονται σωστά από το σύστημα χρησιμοποιώντας:

```bash
motelist
```

ή

```bash
ls /dev | grep ttyUSB*
```

Για τη ρύθμιση του TinyOS χρησιμοποιήθηκαν οι παρακάτω εντολές:

```bash
git clone https://github.com/tinyos/tinyos-main.git

cd ~/tinyos-main/tools

./Bootstrap
./configure
make
sudo make install
```

Στη συνέχεια πρόσθεσα τα κατάλληλα δικαιώματα πρόσβασης στις USB συσκευές:

```bash
sudo usermod -aG dialout $USER

reboot
```

Για την επιβεβαίωση της σωστής λειτουργίας του περιβάλλοντος εκτελέστηκε αρχικά η εφαρμογή Blink στα motes.

Παράδειγμα μεταγλώττισης και φόρτωσης:

```bash
make telosb install.5 bsl,/dev/ttyUSB2
```

Έπειτα χρησιμοποιήθηκε το παράδειγμα `examples/Sensing` για τη δημιουργία δικτύου τοπολογίας αστέρα, όπου ένας κεντρικός κόμβος λειτουργούσε ως κόμβος πατέρας και συγκέντρωνε δεδομένα από τους υπόλοιπους κόμβους αισθητήρων.

Πραγματοποιήθηκε επίσης τροποποίηση στον κώδικα ώστε οι μετρήσεις να αποστέλλονται περιοδικά κάθε 20 δευτερόλεπτα:

```c
enum {
    TIMER_PERIOD_MILLI = 20000
};
```

Επιπλέον έγινε αλλαγή στη μορφή εμφάνισης των μετρήσεων ώστε όλα τα δεδομένα να εμφανίζονται στην ίδια γραμμή:

```c
printf("ID=%d Count=%d Temp=%d Humidity=%d Photo=%d Solar=%d\n",
id,
count,
temperature,
humidity,
photo,
solar);
```

Παράδειγμα εξόδου:

```text
ID=5 Count=18 Temp=7176 Humidity=1224 Photo=1 Solar=0
```

Η συγκεκριμένη μορφή επιλέχθηκε ώστε να είναι πιο εύκολη η παρακολούθηση των δεδομένων και η επεξεργασία τους στα επόμενα στάδια της άσκησης.

## 2ο μέρος
## 2ο μέρος

Στο δεύτερο μέρος ασχολήθηκα με την εγκατάσταση της MongoDB και την αποθήκευση των δεδομένων που λαμβάνονταν από τους αισθητήρες σε πραγματικό χρόνο.

Αρχικά εγκατέστησα και εκκίνησα τη MongoDB ώστε να είναι διαθέσιμη για αποθήκευση των μετρήσεων:

```bash
sudo systemctl start mongod

sudo systemctl status mongod
```

Στη συνέχεια χρησιμοποιήθηκε το `SensingApp.java`, το οποίο τροποποιήθηκε ώστε να πραγματοποιείται επεξεργασία των δεδομένων που λαμβάνονταν από τον κόμβο πατέρα και να γίνεται εξαγωγή των απαραίτητων πεδίων.

Οι μετρήσεις είχαν μορφή:

```text
ID=5 Count=18 Temp=7176 Humidity=1224 Photo=1 Solar=0
```

Από κάθε γραμμή δεδομένων αποθηκεύονταν τα εξής στοιχεία:

- Timestamp
- ID
- Count
- Temperature
- Humidity
- Photo
- Solar

Για τη σύνδεση με τη MongoDB χρησιμοποιήθηκαν οι κατάλληλες βιβλιοθήκες Java:

```java
MongoClient mongoClient = MongoClients.create("mongodb://localhost:27017");

MongoDatabase database = mongoClient.getDatabase("wsn_database");

MongoCollection<Document> collection =
database.getCollection("sensor_data");
```

Στη συνέχεια δημιουργούνταν ένα document και αποθηκευόταν αυτόματα στη βάση:

```java
Document sensorData = new Document()
.append("timestamp", timestamp)
.append("id", id)
.append("count", count)
.append("temp", temperature)
.append("humidity", humidity)
.append("photo", photo)
.append("solar", solar);

collection.insertOne(sensorData);
```

Με αυτόν τον τρόπο κάθε νέα μέτρηση που λάμβανα από τους αισθητήρες αποθηκευόταν αυτόματα στη MongoDB σε πραγματικό χρόνο και μπορούσε να χρησιμοποιηθεί στα επόμενα στάδια της άσκησης.

## 3ο μέρος
## 3ο μέρος

Στο τρίτο μέρος ασχολήθηκα με την οπτικοποίηση των δεδομένων που συλλέγονταν από τους αισθητήρες μέσω web εφαρμογής. Για την υλοποίηση χρησιμοποιήθηκε Flask σε συνδυασμό με MongoDB, ώστε να εμφανίζονται τόσο οι νέες μετρήσεις σε πραγματικό χρόνο όσο και ιστορικά δεδομένα.

Αρχικά ξεκίνησα την εφαρμογή dashboard:

```bash
cd ~/wsn_dashboard

python3 app.py
```

Η εφαρμογή συνδεόταν με τη MongoDB και ανακτούσε τις αποθηκευμένες μετρήσεις αισθητήρων.

Στον κώδικα της εφαρμογής χρησιμοποιήθηκε λογική αντίστοιχη με:

```python
client = MongoClient("mongodb://localhost:27017/")

db = client["wsn_database"]

collection = db["sensor_data"]

data = list(collection.find())
```

Το dashboard εμφάνιζε δυναμικά πληροφορίες όπως:

- ID κόμβου
- Count
- Θερμοκρασία
- Υγρασία
- Φωτεινότητα
- Ηλιακή ακτινοβολία

Επιπλέον υλοποιήθηκαν δύο τρόποι εμφάνισης δεδομένων:

- Live προβολή των πιο πρόσφατων μετρήσεων
- Full History προβολή όλων των καταγεγραμμένων δεδομένων

Με τον τρόπο αυτό μπορούσα να παρακολουθώ σε πραγματικό χρόνο τη συμπεριφορά των αισθητήρων αλλά και να έχω πρόσβαση στο ιστορικό των μετρήσεων μέσω browser.

## 4ο μέρος

Στο τέταρτο μέρος ασχολήθηκα με την ανάλυση των δεδομένων που συλλέχθηκαν από τους αισθητήρες και με την εκπαίδευση μοντέλου Machine Learning για πρόβλεψη μελλοντικών τιμών θερμοκρασίας. Για την υλοποίηση χρησιμοποιήθηκε Jupyter Notebook μαζί με τις βιβλιοθήκες Pandas και Scikit-learn.

Αρχικά πραγματοποιήθηκε σύνδεση με τη MongoDB και ανάκτηση των δεδομένων ώστε να μετατραπούν σε DataFrame:

```python
from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["wsn_database"]
collection = db["sensor_data"]

data = list(collection.find())

df = pd.DataFrame(data)

df.head()
```

Στη συνέχεια πραγματοποιήθηκε στατιστική ανάλυση των δεδομένων:

```python
df.describe()
```

Για την εκπαίδευση του μοντέλου χρησιμοποιήθηκαν ως χαρακτηριστικά οι μετρήσεις `humidity`, `photo`, `solar` και `count`, ενώ ως στόχος χρησιμοποιήθηκε η θερμοκρασία (`temp`):

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = df[['count','humidity','photo','solar']]
y=df['temp']

X_train,X_test,y_train,y_test=train_test_split(
        X,y,test_size=0.2,random_state=42
)

model=LinearRegression()

model.fit(X_train,y_train)

prediction=model.predict(X_test)

print("Predicted temperatures:")
print(prediction[:10])
```

Στη συνέχεια δημιουργήθηκε γράφημα σύγκρισης πραγματικών και προβλεπόμενων τιμών:

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))

plt.plot(y_test.values[:20],label='Actual Temperature')
plt.plot(prediction[:20],label='Predicted Temperature')

plt.legend()
plt.xlabel("Samples")
plt.ylabel("Temperature")

plt.show()
```

Επίσης υπολογίστηκε το πλήθος των δεδομένων που συλλέχθηκαν:

```python
len(df)
```

Συλλέχθηκαν συνολικά:

```text
1955 samples
```

Τέλος υπολογίστηκαν οι μετρικές αξιολόγησης του μοντέλου:

```python
from sklearn.metrics import mean_squared_error, r2_score

print("R²:", r2_score(y_test, prediction))
print("MSE:", mean_squared_error(y_test, prediction))
```

Τα αποτελέσματα που προέκυψαν ήταν:

```text
R²: 0.8317512678794513

MSE: 1721.1996375438061
```

Παρατηρήθηκε ότι οι προβλέψεις ακολουθούν σε αρκετά καλό βαθμό τις πραγματικές μετρήσεις θερμοκρασίας, γεγονός που δείχνει ότι το μοντέλο παρουσίασε ικανοποιητική απόδοση.
