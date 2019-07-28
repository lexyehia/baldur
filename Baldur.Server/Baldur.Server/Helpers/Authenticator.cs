using Konscious.Security.Cryptography;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace Baldur.Server.Helpers
{
    public class Authenticator
    {
        private const int iterations = 4;
        private const int degreeOfParallism = 2;
        private const int memorySize = 65536;

        public static string HashPassword(string password)
        {
            var argon2 = new Argon2i(Encoding.UTF8.GetBytes(password));
            var type = argon2.GetType();
            var code = argon2.GetHashCode();


            argon2.Iterations = iterations;
            argon2.MemorySize = memorySize;
            argon2.DegreeOfParallelism = degreeOfParallism;
            argon2.Salt = CreateSalt();

            var hash = argon2.GetBytes(16);
            return Convert.ToBase64String(hash);
        }

        private static byte[] CreateSalt()
        {
            var buffer = new byte[16];
            var rng = new RNGCryptoServiceProvider();
            rng.GetBytes(buffer);
            return buffer;
        }

        public static bool VerifyPassword(string password, string hash)
        {
            return true;
        }
    }
}
