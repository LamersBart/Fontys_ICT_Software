using System;

namespace CalorieënTracker
{
    class Program
    {
        static void Main(string[] args)
        {

            string zwanger = "";
            double caloriën = 0;

            //Hier vraag ik de 3 vragen die nodig zijn voor de berekening
            Console.WriteLine("Bent u een man of een vrouw? ");
            string geslacht = Console.ReadLine();
            if (geslacht == "vrouw")
            {
                Console.WriteLine("Bent u zwanger? ");
                zwanger = Console.ReadLine();
            }
            Console.WriteLine("Heeft u een actieve levenstijl? ");
            string levenstijl = Console.ReadLine();
            Console.WriteLine("Wat is uw leeftijd? ");
            string leeftijd = Console.ReadLine();

            int leeftijdGetal = Convert.ToInt32(leeftijd);

            if (geslacht == "man")
            {
                caloriën = caloriën + 2500;
            }
            if (geslacht == "vrouw")
            {
                caloriën = caloriën + 2000;
            }
            if (zwanger == "ja")
            {
                if (leeftijdGetal <= 30)
                {
                    caloriën = 2600;
                }
                if (leeftijdGetal >= 30)
                {
                    caloriën = 2500;
                }
            }
            if (levenstijl == "nee")
            {
                caloriën = caloriën * 0.9;
            }
            if (leeftijdGetal >= 50)
            {
                caloriën = caloriën - 200;
            }
            if (leeftijdGetal <= 12)
            {
                caloriën = caloriën - 180;
            }

            //Hier wordt het resultaat geprint
            Console.WriteLine("Caloriën die u mag hebben: " + caloriën);
        }
    }
}