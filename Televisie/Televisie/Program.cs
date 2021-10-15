using System;
using System.Collections.Generic; //toevoegen om List's te kunnen gebruiken

namespace Televisie
{
    class Program
    {
        static void Main(string[] args)
        {

            bool tvStatus = false;
            bool auth = true;

            while (auth == true)
            {
                Console.WriteLine("Maak uw keuze u kunt 'Aan' of 'Uit' kiezen");
                Console.WriteLine("Aan of Uit:");
                string tvStand = Console.ReadLine();
                Console.WriteLine();
                Console.Clear();
                if (tvStand == "Aan")
                {
                    Console.WriteLine("Welkom");
                    tvStatus = true;
                    auth = false;
                }
                else if (tvStand == "Uit")
                {
                    Console.WriteLine("Tot ziens!");
                    tvStatus = false;
                    auth = false;
                }
                else
                {
                    Console.WriteLine("Onjuiste invoer, probeer opnieuw");
                    tvStand = "";
                }
            }

            List<string> zenders = new List<string>();
            zenders.Add("NPO 1");
            zenders.Add("NPO 2");
            zenders.Add("NPO 3");
            zenders.Add("RTL 4");
            zenders.Add("RTL 5");
            zenders.Add("SBS 6");
            zenders.Add("RTL 7");
            zenders.Add("NET 8");
            zenders.Add("Veronica");

            int num = 0;
            string huidigeZender = zenders[0];

            while (tvStatus == true)
            {
                Console.WriteLine("");
                Console.WriteLine("U kijkt nu naar " + zenders[num]);
                Console.WriteLine("");
                Console.WriteLine("Kies nummer?");
                Console.WriteLine("1. Zenderlijst");
                Console.WriteLine("2. Zendertoevoegen");
                Console.WriteLine("3. Volgende zender");
                Console.WriteLine("4. Vorige zender");
                Console.WriteLine("5. Standby");
                Console.WriteLine("6. Zet TV uit");
                string invoer = Console.ReadLine();
                Console.Clear();
                int MaxZenders = zenders.Count;
                if (invoer == "1")
                {
                    zenders.ForEach(Console.WriteLine);
                    Console.WriteLine("");
                    Console.WriteLine("Druk op enter om verder te gaan.");
                    string enter = Console.ReadLine();
                    if (enter == "")
                    {
                        Console.Clear();
                    }
                }

                if (invoer == "2")
                {
                    Console.WriteLine("Voer uw nieuwe zender in:");
                    string nieuweZender = Console.ReadLine();
                    if (nieuweZender != string.Empty)
                    {
                        zenders.Add(nieuweZender);
                        Console.WriteLine("zender " + nieuweZender + " is opgeslagen!");
                        Console.WriteLine("");
                    }
                    else Console.WriteLine("zender is niet opgeslagen!");
                    Console.WriteLine("");
                    Console.WriteLine("Druk op enter om verder te gaan.");
                    string enter = Console.ReadLine();
                    if (enter == "")
                    {
                        Console.Clear();
                    }
                }

                if (invoer == "3")
                {
                    num = num + 1;
                }

                if (invoer == "4")
                {
                    if (num <= 0)
                    {
                        num = MaxZenders;
                    }
                    num = num - 1;
                }

                if (invoer == "5")
                {
                    Console.WriteLine("Druk op enter om TV uit standby te halen.");
                    string enter = Console.ReadLine();
                    if (enter == "")
                    {
                        Console.Clear();
                    }
                }
                if (invoer == "6")
                {
                    tvStatus = false;
                    Console.WriteLine("Tot Ziens!");
                }
                if (num == MaxZenders)
                {
                    num = 0;
                }
            }
        }
    }
}