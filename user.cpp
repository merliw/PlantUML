#pragma once

#include <string>
#include <iostream>

enum class Service {
    Direction,
    IT,
    Marketing
};

inline std::string toString(Service s) {
    switch (s) {
        case Service::Direction: return "Direction";
        case Service::IT:        return "IT";
        case Service::Marketing: return "Marketing";
    }
    return "Inconnu";
}

class PosteDeTravail {
private:
    std::string m_hostname;
    std::string m_ip;
    std::string m_mac;
    std::string m_os;

public:
    PosteDeTravail() = default;

    PosteDeTravail(std::string hostname, std::string ip, std::string mac, std::string os)
        : m_hostname(std::move(hostname)),
          m_ip(std::move(ip)),
          m_mac(std::move(mac)),
          m_os(std::move(os)) {}

    // Accesseurs
    const std::string& hostname() const { return m_hostname; }
    const std::string& ip() const { return m_ip; }
    const std::string& mac() const { return m_mac; }
    const std::string& os() const { return m_os; }

    // Mutateurs
    void hostname(const std::string& v) { m_hostname = v; }
    void ip(const std::string& v) { m_ip = v; }
    void mac(const std::string& v) { m_mac = v; }
    void os(const std::string& v) { m_os = v; }

    void demarrer() const {
        std::cout << "Le poste " << m_hostname << " (" << m_ip << ") demarre." << std::endl;
    }

    void arreter() const {
        std::cout << "Le poste " << m_hostname << " (" << m_ip << ") s'eteint." << std::endl;
    }

    friend std::ostream& operator<<(std::ostream& out, const PosteDeTravail& p) {
        return out << "PosteDeTravail(hostname=" << p.m_hostname
                   << ", IP=" << p.m_ip
                   << ", MAC=" << p.m_mac
                   << ", OS=" << p.m_os << ")";
    }
};

class User {
private:
    std::string m_nom;
    std::string m_prenom;
    std::string m_role;
    Service m_service{Service::IT};
    PosteDeTravail* m_poste{nullptr}; // même finalité que ton code (pointeur non-owning)

public:
    User(std::string nom, std::string prenom, std::string role, Service service,
         PosteDeTravail* poste = nullptr)
        : m_nom(std::move(nom)),
          m_prenom(std::move(prenom)),
          m_role(std::move(role)),
          m_service(service),
          m_poste(poste) {}

    // Accesseurs
    const std::string& nom() const { return m_nom; }
    const std::string& prenom() const { return m_prenom; }
    const std::string& role() const { return m_role; }
    Service service() const { return m_service; }
    PosteDeTravail* poste() const { return m_poste; }

    // Mutateurs
    void nom(const std::string& v) { m_nom = v; }
    void prenom(const std::string& v) { m_prenom = v; }
    void role(const std::string& v) { m_role = v; }
    void service(Service v) { m_service = v; }
    void poste(PosteDeTravail* p) { m_poste = p; }

    void connecter() const {
        std::cout << m_prenom << " " << m_nom << " se connecte au SI." << std::endl;
    }

    void deconnecter() const {
        std::cout << m_prenom << " " << m_nom << " se deconnecte du SI." << std::endl;
    }

    friend std::ostream& operator<<(std::ostream& out, const User& u) {
        out << "User(" << u.m_prenom << " " << u.m_nom
            << ", role=" << u.m_role
            << ", service=" << toString(u.m_service);
        if (u.m_poste) out << ", poste=" << *(u.m_poste);
        out << ")";
        return out;
    }
};