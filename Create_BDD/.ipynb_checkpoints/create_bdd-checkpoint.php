<?php

$serveur = "localhost"; 
$utilisateur = "votre_nom_utilisateur"; 
$motDePasse = "votre_mot_de_passe"; 


$connexion = new mysqli($serveur, $utilisateur, $motDePasse);

if ($connexion->connect_error) {
    die("Échec de la connexion : " . $connexion->connect_error);
}


$baseDeDonnees = "evenements_db";
$sql_create_database = "CREATE DATABASE IF NOT EXISTS $baseDeDonnees";
if ($connexion->query($sql_create_database) === TRUE) {
    echo "Base de données créée avec succès.<br>";
} else {
    echo "Erreur lors de la création de la base de données : " . $connexion->error . "<br>";
}


$connexion->select_db($baseDeDonnees);


$sql_create_event_table = "
CREATE TABLE IF NOT EXISTS Event (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Titre VARCHAR(255),
    DATE DATE,
    ADRESSE VARCHAR(255),
    PRIX DECIMAL(10, 2),
    VILLE INT,
    TYPE VARCHAR(255),
    FOREIGN KEY (VILLE) REFERENCES Ville(ID)
);";

$sql_create_restaurant_table = "
CREATE TABLE IF NOT EXISTS Restauration (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ADRESS VARCHAR(255),
    TYPE VARCHAR(255),
    VILLE INT,
    NOM VARCHAR(255),
    PRIX DECIMAL(10, 2),
    NOTE INT,
    FOREIGN KEY (VILLE) REFERENCES Ville(ID)
);";

$sql_create_hotel_table = "
CREATE TABLE IF NOT EXISTS Hotel (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ADRESSE VARCHAR(255),
    NOM VARCHAR(255),
    PRIX DECIMAL(10, 2),
    SERVICES TEXT,
    NOTE INT,
    VILLE INT,
    DATE DATE,
    FOREIGN KEY (VILLE) REFERENCES Ville(ID)
);";

$sql_create_voyage_table = "
CREATE TABLE IF NOT EXISTS Voyage (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Date_Départ  TIMESTAMP,
    Date_arrivée  TIMESTAMP,
    Horaire VARCHAR(255),
    trajet VARCHAR(255),
    type_trajet VARCHAR(255),
    temps_trajet VARCHAR(255),
    prix VARCHAR(30),
    type_voyage VARCHAR(255),
    Compagnie VARCHAR(255),
    VILLE_DEPART INT,
    VILLE_ARRIVEE INT,
    FOREIGN KEY (VILLE_DEPART) REFERENCES Ville(ID),
    FOREIGN KEY (VILLE_ARRIVEE) REFERENCES Ville(ID)
);";

$sql_create_ville_table = "
CREATE TABLE IF NOT EXISTS Ville (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NOM VARCHAR(255)
);";

if ($connexion->query($sql_create_event_table) === TRUE) {
    echo "Table 'Event' créée avec succès.<br>";
} else {
    echo "Erreur lors de la création de la table 'Event' : " . $connexion->error . "<br>";
}

if ($connexion->query($sql_create_restaurant_table) === TRUE) {
    echo "Table 'Restauration' créée avec succès.<br>";
} else {
    echo "Erreur lors de la création de la table 'Restauration' : " . $connexion->error . "<br>";
}

if ($connexion->query($sql_create_hotel_table) === TRUE) {
    echo "Table 'Hotel' créée avec succès.<br>";
} else {
    echo "Erreur lors de la création de la table 'Hotel' : " . $connexion->error . "<br>";
}

if ($connexion->query($sql_create_voyage_table) === TRUE) {
    echo "Table 'Voyage' créée avec succès.<br>";
} else {
    echo "Erreur lors de la création de la table 'Voyage' : " . $connexion->error . "<br>";
}

if ($connexion->query($sql_create_ville_table) === TRUE) {
    echo "Table 'Ville' créée avec succès.<br>";
} else {
    echo "Erreur lors de la création de la table 'Ville' : " . $connexion->error . "<br>";
}


$connexion->close();
?>
