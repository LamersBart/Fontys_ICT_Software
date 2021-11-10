using System;

namespace ArrayPresentatie
{
    class Program
    {
        public static object MessageBox { get; private set; }

        static void Main(string[] args)
        {
            int[] getallen = new int[10];
            for (int i = 0; i < getallen.Length; i++)
            {
                getallen[i] = (i + 1) * 5;
                string getal = Convert.ToString(i);
                Console.WriteLine("Getal nummer "+ getal +" = "+ getallen[i]);
            }
        }
    }
}
