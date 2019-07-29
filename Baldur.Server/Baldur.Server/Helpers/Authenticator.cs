using Konscious.Security.Cryptography;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace Baldur.Server.Helpers
{
    public partial class Authenticator
    {
        private const int iterations = 8;
        private const int threads = 8;
        private const int memory = 512000;
        private const int hashLength = 24;
        private const int saltLength = 12;
        private static readonly string[] peppers = new string[]
        {
            "donde",
            "chacha",
            "quack",
        };

        public static string HashPassword(string password)
        {
            var argon2 = new Argon2id(Encoding.UTF8.GetBytes(password + GetRandomPepper()))
            {
                Iterations = iterations,
                MemorySize = memory,
                DegreeOfParallelism = threads,
                Salt = CreateSalt(saltLength)
            };

            return EncodePassword(argon2.GetBytes(hashLength), argon2.Salt);
        }

        public static bool VerifyPassword(string encodedPassword, string enteredPassword)
        {
            var (salt, hash) = DecodePassword(encodedPassword);
            if (salt == null || hash == null) return false;

            try {
                var saltBytes = Convert.FromBase64String(salt);
                var hashBytes = Convert.FromBase64String(hash);

                foreach (var pepper in peppers) 
                {
                    var argon2 = new Argon2id(Encoding.UTF8.GetBytes(enteredPassword + pepper))
                    {
                        Iterations = iterations,
                        MemorySize = memory,
                        DegreeOfParallelism = threads,
                        Salt = saltBytes
                    };

                    if (hashBytes.SequenceEqual(argon2.GetBytes(hashLength))) {
                        return true;
                    }
                }
                
            } catch (Exception e) {
                Console.WriteLine(e.StackTrace);
            }

            return false;
        }

        private static string EncodePassword(byte[] hash, byte[] salt)
        {
            var saltString = Convert.ToBase64String(salt);
            var hashString = Convert.ToBase64String(hash);

            return saltString + hashString;
        }

        private static Tuple<string, string> DecodePassword(string encodedPassword)
        {
            var saltString = encodedPassword.Substring(0, saltLength);
            var hashString = encodedPassword.Substring(saltLength + 1, hashLength);

            return new Tuple<string, string>(saltString, hashString);
        }

        private static byte[] CreateSalt(int saltLength)
        {
            var buffer = new byte[saltLength];
            var rng = new RNGCryptoServiceProvider();
            rng.GetBytes(buffer);
            return buffer;
        }

        private static string GetRandomPepper()
        {
            var random = new Random();
            return peppers[random.Next(peppers.Count())];
        }
    }
}
