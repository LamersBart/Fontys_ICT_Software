using System;

namespace WorpenGenerator
{
    class Program
    {
        static void Main(string[] args)
        {
            bool worpInvoer = false;
            int worpUitkomst = 0;

            while (worpInvoer == false)
            {
                Console.WriteLine("Aantal worpen:");
                string invoer1 = Console.ReadLine();
                int instellingAantalWorpen = Convert.ToInt32(invoer1);

                if (instellingAantalWorpen >= 1001 && instellingAantalWorpen >= 1)
                {
                    Console.WriteLine("Houd het getal lager dan 1001, probeer opnieuw");
                    instellingAantalWorpen = 0;
                }
                if (instellingAantalWorpen <= 1001 && instellingAantalWorpen >= 1)
                {
                    worpInvoer = true;
                    worpUitkomst = instellingAantalWorpen;
                }
            }

            bool ogenInvoer = false;
            int ogenUitkomst = 0;

            while (ogenInvoer == false)
            {
                Console.WriteLine("Aantal ogen:");
                string invoer1 = Console.ReadLine();
                int instellingAantalOgen = Convert.ToInt32(invoer1);

                if (instellingAantalOgen >= 7 && instellingAantalOgen >= 1)
                {
                    Console.WriteLine("Houd het getal lager dan 7, probeer opnieuw");
                    instellingAantalOgen = 0;
                }
                if (instellingAantalOgen <= 7 && instellingAantalOgen >= 1)
                {
                    ogenInvoer = true;
                    ogenUitkomst = instellingAantalOgen;
                }
            }

            int tellen = 0;
            int numTotaal = 0;
            while (tellen != worpUitkomst)
            {
                Random rnd = new Random();
                int num = rnd.Next(1,ogenUitkomst);
                tellen = tellen + 1;
                Console.WriteLine("Worp:" + tellen + "  " + num);
                numTotaal = numTotaal + num;
            }

            Console.WriteLine("totaal: " + numTotaal);
        }
    }
}