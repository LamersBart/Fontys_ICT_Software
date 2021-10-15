using System;

namespace Ampere
{
    class Program
    {
        static decimal Weerstand(decimal volt, decimal ampere)
        {
            decimal ohm = volt / ampere;
            return ohm;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Spanning (Volt)");
            string voltage = Console.ReadLine();
            Console.WriteLine("Stroom (Ampere)");
            string ampereage = Console.ReadLine();

            decimal volt = Convert.ToDecimal(voltage);
            decimal ampere = Convert.ToDecimal(ampereage);

            Console.WriteLine("Weerstand is: " + Weerstand(volt, ampere));

        }
    }
}