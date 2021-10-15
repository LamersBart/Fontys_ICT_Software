using System;

namespace De_Debugger
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] namen = { "naam1", "naam2", "naam3", "naam4", "naam5", "naam6" };

            foreach (string naam in namen)
            Console.WriteLine(naam);
            int temp = 4;
            for (int i = 0; i < 10; i++)
            {
                if (i > 5)
                    temp = 5;
                Console.WriteLine(temp);
            }
            Console.ReadLine();
        }
        
    }
}