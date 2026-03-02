from enum import Enum


class Service(Enum):
    Direction = "Direction"
    IT = "IT"
    Marketing = "Marketing"


class Machine:
    def __init__(self, hostname: str, ip: str, mac: str, systeme: str):
        self._hostname = hostname
        self._ip = ip
        self._mac = mac
        self._systeme = systeme

    # --- Propriétés ---
    @property
    def hostname(self) -> str:
        return self._hostname

    @hostname.setter
    def hostname(self, value: str):
        self._hostname = value

    @property
    def ip(self) -> str:
        return self._ip

    @ip.setter
    def ip(self, value: str):
        self._ip = value

    @property
    def mac(self) -> str:
        return self._mac

    @mac.setter
    def mac(self, value: str):
        self._mac = value

    @property
    def systeme(self) -> str:
        return self._systeme

    @systeme.setter
    def systeme(self, value: str):
        self._systeme = value

    # --- Méthodes ---
    def demarrer(self):
        print(f"Le poste {self._hostname} ({self._ip}) démarre.")

    def arreter(self):
        print(f"Le poste {self._hostname} ({self._ip}) s'éteint.")

    def __str__(self) -> str:
        return (f"Machine(hostname={self._hostname}, "
                f"IP={self._ip}, "
                f"MAC={self._mac}, "
                f"OS={self._systeme})")


class Collaborateur:
    def __init__(self, nom: str, prenom: str, fonction: str,
                 departement: Service, machine: Machine | None = None):
        self._nom = nom
        self._prenom = prenom
        self._fonction = fonction
        self._departement = departement
        self._machine = machine

    # --- Propriétés ---
    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, value: str):
        self._nom = value

    @property
    def prenom(self) -> str:
        return self._prenom

    @prenom.setter
    def prenom(self, value: str):
        self._prenom = value

    @property
    def fonction(self) -> str:
        return self._fonction

    @fonction.setter
    def fonction(self, value: str):
        self._fonction = value

    @property
    def departement(self) -> Service:
        return self._departement

    @departement.setter
    def departement(self, value: Service):
        self._departement = value

    @property
    def machine(self) -> Machine | None:
        return self._machine

    @machine.setter
    def machine(self, value: Machine | None):
        self._machine = value

    # --- Méthodes ---
    def connecter(self):
        print(f"{self._prenom} {self._nom} se connecte au SI.")

    def deconnecter(self):
        print(f"{self._prenom} {self._nom} se déconnecte du SI.")

    def __str__(self) -> str:
        return (f"Collaborateur({self._prenom} {self._nom}, "
                f"fonction={self._fonction}, "
                f"service={self._departement.value}, "
                f"machine={self._machine})")


if __name__ == "__main__":

    # --- Création des machines ---
    machines = [
        Machine("PC-DIR-01", "192.168.1.10", "AA:BB:CC:DD:EE:01", "Windows 11"),
        Machine("PC-DIR-02", "192.168.1.11", "AA:BB:CC:DD:EE:02", "Windows 11"),
        Machine("PC-IT-01",  "192.168.1.20", "AA:BB:CC:DD:EE:03", "Ubuntu 22.04"),
        Machine("PC-MKT-01", "192.168.1.30", "AA:BB:CC:DD:EE:04", "Windows 11"),
        Machine("PC-MKT-02", "192.168.1.31", "AA:BB:CC:DD:EE:05", "Windows 11"),
        Machine("PC-MKT-03", "192.168.1.32", "AA:BB:CC:DD:EE:06", "Windows 11"),
    ]

    # --- Création des collaborateurs ---
    equipe = [
        Collaborateur("Le CEO", "Robert", "CEO", Service.Direction, machines[0]),
        Collaborateur("L'Insider Threat", "Rachel", "Secrétaire du CEO", Service.Direction, machines[1]),
        Collaborateur("IT Guy", "Guillaume", "Technicien IT", Service.IT, machines[2]),
        Collaborateur("Le Dev", "Nathan", "Dev Full Stack", Service.Marketing, machines[3]),
        Collaborateur("Le Marketeur", "Mickael", "Marketeur", Service.Marketing, machines[4]),
        Collaborateur("La Marketeuse", "Celia", "Marketeuse", Service.Marketing, machines[5]),
    ]

    # --- Simulation ---
    for membre in equipe:
        print(membre)
        membre.connecter()
        print("-" * 40)