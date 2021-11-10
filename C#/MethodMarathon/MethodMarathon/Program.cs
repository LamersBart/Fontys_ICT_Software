using System;

namespace MethodMarathon
{
    class Program
    {
        //Dit is opdacht 1
        public static string FullName(string voorNaam, string achterNaam)
        {
            return voorNaam + " " + achterNaam;
        }

        //Dit is opdracht 2
        public static int Times(string voorNaam, string achterNaam)
        {
            return voorNaam.Length * achterNaam.Length;
        }

        //Dit is opdracht 3
        public static bool IsIn(string character, string word)
        {
            return word.Contains(character); 
        }

        //Dit is opdracht 4, is te lastig.

        //Dit is opdracht 5
        public static int HowMuchLonger()
        {

        }


        static void Main(string[] args)
        {
            Console.WriteLine(FullName("Ada","Lovelace"));      //Ada Lovelace
            Console.WriteLine(Times("Ada", "Lovelace"));        //24
            Console.WriteLine(Isln("Ada", "Lovelace"));         //false
            Console.WriteLine(Isln("Ada", "Ada"));              //true
        }
    }
}