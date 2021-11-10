using System;

namespace DB_WK2_Demo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            // Zo zet je commentaar in de code

            /* zo zet je meedere
             * zinnen commentaar
             * in je code 
             */

            int aantalStudenten;
            aantalStudenten = 25;
            int nieuweStudenten;
            nieuweStudenten = 5;
            aantalStudenten = aantalStudenten + nieuweStudenten;

            string tekstNL = "aantal studenden: ";
            string textEN = "Number of students: ";

            int chosenLanguage = 0;

            if (chosenLanguage == 0)
            {
                Console.WriteLine(textEN + aantalStudenten);
            }
            else
            {
                Console.WriteLine(tekstNL + aantalStudenten);
            }
        }
    }
}
