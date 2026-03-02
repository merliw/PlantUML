class PosteDeTravail:
    def __init__(self, hostname: str, ip: str, mac: str):
        self.hostname = hostname
        self.ip = ip
        self.mac = mac

    def demarrer(self) -> None:
        print(f"{self.hostname} démarre.")

    def eteindre(self) -> None:
        print(f"{self.hostname} s'éteint.")


class User:
    def __init__(self, nom: str, role: str, service: str, poste: PosteDeTravail):
        self.nom = nom
        self.role = role
        self.service = service
        self.poste = poste  # association 1–1 : le user utilise ce poste

    def seConnecter(self) -> None:
        print(f"{self.nom} se connecte sur {self.poste.hostname}")

    def seDeconnecter(self) -> None:
        print(f"{self.nom} se déconnecte.")


# Exemple d’utilisation
if __name__ == "__main__":
    pc = PosteDeTravail("PC-Direction-01", "192.168.1.10", "AA:BB:CC:DD:EE:FF")
    u = User("Robert", "CEO", "Direction", pc)
    u.seConnecter()
    u.seDeconnecter()