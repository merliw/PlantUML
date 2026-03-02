#include "User.hpp"
#include <vector>

int main() {

    // --- Création des machines ---
    PosteDeTravail pcDir1("PC-DIR-01", "192.168.1.10", "AA:BB:CC:DD:EE:01", "Windows 11");
    PosteDeTravail pcDir2("PC-DIR-02", "192.168.1.11", "AA:BB:CC:DD:EE:02", "Windows 11");
    PosteDeTravail pcIT1("PC-IT-01",  "192.168.1.20", "AA:BB:CC:DD:EE:03", "Ubuntu 22.04");
    PosteDeTravail pcMkt1("PC-MKT-01","192.168.1.30", "AA:BB:CC:DD:EE:04", "Windows 11");
    PosteDeTravail pcMkt2("PC-MKT-02","192.168.1.31", "AA:BB:CC:DD:EE:05", "Windows 11");
    PosteDeTravail pcMkt3("PC-MKT-03","192.168.1.32", "AA:BB:CC:DD:EE:06", "Windows 11");

    // --- Création des collaborateurs ---
    std::vector<User> equipe = {
        User("Le CEO", "Robert", "CEO", Service::DIRECTION, &pcDir1),
        User("L'Insider Threat", "Rachel", "Secretaire du CEO", Service::DIRECTION, &pcDir2),
        User("IT Guy", "Guillaume", "Technicien IT", Service::IT, &pcIT1),
        User("Le Dev", "Nathan", "Dev Full Stack", Service::MARKETING, &pcMkt1),
        User("Le Marketeur", "Mickael", "Marketeur", Service::MARKETING, &pcMkt2),
        User("La Marketeuse", "Celia", "Marketeuse", Service::MARKETING, &pcMkt3)
    };

    // --- Simulation des connexions ---
    for (const User& utilisateur : equipe) {
        std::cout << utilisateur << std::endl;
        utilisateur.seConnecter();
        std::cout << "-----------------------------" << std::endl;
    }

    return 0;
}