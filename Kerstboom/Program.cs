using System;

namespace Kerstboom_wk1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Prompt();
            Console.ReadKey();
    }
            
        static void Prompt() {
            Console.WriteLine("Hoeveel kerstbomen?");
            if (int.TryParse(Console.ReadLine(), out int aantalKerstbomen)) {
                Console.WriteLine("Welk karakter?");
                string karakter = Console.ReadLine();
                Console.Clear();
                RandomKerstbomen(aantalKerstbomen, karakter);
            }
            else
            {
                Console.Clear();
                Console.WriteLine("Vul een getal in.");
                Prompt();
            }
        }

        static void Kerstboom(string karakter, int x, int y, int hoogte)
        { 
            int offset = 0;
            for (int i = y; i < (y + hoogte); i++)
            {
                Console.SetCursorPosition(x, i);
                Console.Write(karakter);
                for (int j = 0; j < (offset + 1); j++)
                {
                    Console.SetCursorPosition(x + j, i);
                    Console.Write(karakter);
                }
                x--;
                offset = offset + 2;
            }
        }
        static void RandomKerstbomen(int aantalKerstbomen, string karakter)
        {
            for (int i = 0; i < aantalKerstbomen; i++)
            {
                Random rnd = new Random();
                int x = rnd.Next(10, 100);
                int hoogte = rnd.Next(3, 10);
                int y = i * 10;
                Kerstboom(karakter, x, y, hoogte);
            }
        }
    }
}