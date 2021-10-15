using System;
using System.Collections.Generic;
using System.Linq;

//bron: www.jeremyshanks.com/simple-address-book/

namespace WedstrijdContactenlijst V1
{

    class Program
    {

        public class Persoon
        {
            public string VoorNaam { get; set; }
            public string AchterNaam { get; set; }
            public string TelefoonNummer { get; set; }
            public string Mail { get; set; }
            public string[] Adres { get; set; }
        }

        public static List<Persoon> People = new List<Persoon>();

        public static void Main(string[] args)
        {
            string commando = "";
            while (commando != "Sluit")
            {
                Console.Clear();
                Console.WriteLine("Commando's:");
                Console.WriteLine("Toevoegen: Een contact toevoegen.");
                Console.WriteLine("Verwijderen: Een contact verwijderen.");
                Console.WriteLine("Lijst: Toon de lijst met contacten.");
                Console.WriteLine("Sluit: Sluit het programma.");
                Console.WriteLine("");
                Console.WriteLine("Voer een commando in: ");
                commando = Console.ReadLine().ToLower();
                switch (commando)
                {
                    case "toevoegen":
                        Console.Clear();
                        PersoonToevoegen();
                        break;

                    case "verwijderen":
                        Console.Clear();
                        VerwijderPersoon();
                        break;

                    case "lijst":
                        Console.Clear();
                        Lijst();
                        break;

                    case "sluit":
                        Console.Clear();
                        commando = "Sluit";
                        break;
                }
            }
        }

        private static void PersoonToevoegen()
        {
            Persoon persoon = new Persoon();

            Console.Write("Voornaam: ");
            persoon.VoorNaam = Console.ReadLine();
            Console.Write("Achternaam: ");
            persoon.AchterNaam = Console.ReadLine();
            Console.Write("Telefoonnummer: ");
            persoon.TelefoonNummer = Console.ReadLine();
            Console.Write("Email: ");
            persoon.Mail = Console.ReadLine();
            Console.Write("Adres 1: ");
            string[] adressen = new string[2];
            adressen[0] = Console.ReadLine();
            Console.Write("Adres 2 (optioneel): ");
            adressen[1] = Console.ReadLine();
            persoon.Adres = adressen;
            People.Add(persoon);
        }

        private static void PrintPersoon(Persoon persoon)
        {
            Console.WriteLine("Voornaam: " + persoon.VoorNaam);
            Console.WriteLine("Achternaam: " + persoon.AchterNaam);
            Console.WriteLine("Telefoonnummer: " + persoon.TelefoonNummer);
            Console.WriteLine("E-Mail: " + persoon.Mail);
            Console.WriteLine("Adres 1: " + persoon.Adres[0]);
            Console.WriteLine("Adres 2: " + persoon.Adres[1]);
            Console.WriteLine("-------------------------------------------------");
        }

        private static void Lijst()
        {
            if (People.Count == 0)
            {
                Console.WriteLine("Uw adresboek is leeg. Druk op een toets om verder te gaan.");
                Console.ReadKey();
                return;
            }
            Console.WriteLine("Hier zijn de contacten in uw adresboek:\n");
            foreach (var person in People)
            {
                PrintPersoon(person);
            }
            Console.WriteLine("\nDruk op een toets om verder te gaan.");
            Console.ReadKey();
        }

        public static void VerwijderPersoon()
        {
            Console.WriteLine("Voer de voornaam in van het contact dat u wilt verwijderen.");
            string voorNaam = Console.ReadLine();
            Persoon persoon = People.FirstOrDefault(x => x.VoorNaam.ToLower() == voorNaam.ToLower());
            if (persoon == null)
            {
                Console.WriteLine("Deze persoon is niet vonden. Druk op een toets om verder te gaan.");
                Console.ReadKey();
                return;
            }
            Console.WriteLine("Weet u zeker dat u deze persoon wilt verwijderen uit uw adresboek? (Ja/Nee)");
            PrintPersoon(persoon);
            if (Console.ReadLine().ToLower() == "ja")
            {
                People.Remove(persoon);
                Console.WriteLine("Persoon verwijderd. Druk op een toets om verder te gaan.");
                Console.ReadKey();
            }
        }
    }
}