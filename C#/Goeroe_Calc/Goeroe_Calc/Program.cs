using System;

namespace Goeroe_Calc
{
    class Program
    {
        static void Main(string[] args)
        {
            //Hier vraag ik om invoer van de getallen en operator
            Console.WriteLine("voer getal in:");
            string invoer1 = Console.ReadLine();
            Console.WriteLine("voer getal in:");
            string invoer2 = Console.ReadLine();
            Console.WriteLine("voer operator in:");
            string invoer3 = Console.ReadLine();

            //Hier wordt de invoer van string naar int geconverteerd
            int getalEen = Convert.ToInt32(invoer1);
            int getalTwee = Convert.ToInt32(invoer2);
            int resultaat = 0;

            // Hier wordt het resultaat berekend op basis van ingevoerde operator
            if (invoer3 == "+")
            {
                resultaat = getalEen + getalTwee;
            }

            else if (invoer3 == "-")
            {
                resultaat = getalEen - getalTwee;
            }

            else if (invoer3 == "*")
            {
                resultaat = getalEen * getalTwee;
            }

            //Hier wordt het resultaat geprint
            Console.WriteLine("het resultaat is: " + resultaat);
        }
    }
}