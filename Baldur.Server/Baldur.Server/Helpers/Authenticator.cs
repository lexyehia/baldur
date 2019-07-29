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
        private const int iterations = 8;
        private const int threads = 8;
        private const int memory = 512000;
        private const int hashLength = 24;
        private const int saltLength = 12;
        private static readonly string[] peppers = new string[]
        {
            "donde",
            "chacha",
            "quack"
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
            var pwdDict = DecodePassword(encodedPassword);
            if (pwdDict == null) return false;

            try {
                var hashBytes = Convert.FromBase64String(pwdDict["hash"]);

                foreach (var pepper in peppers) 
                {
                    var argon2 = new Argon2id(Encoding.UTF8.GetBytes(enteredPassword + pepper))
                    {
                        Iterations = int.Parse(pwdDict["iterations"]),
                        MemorySize = int.Parse(pwdDict["memory"]),
                        DegreeOfParallelism = int.Parse(pwdDict["threads"]),
                        Salt = Convert.FromBase64String(pwdDict["salt"])
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

        public static bool IsOldEncoding(string encodedPassword)
        {
            var pwdDict = DecodePassword(encodedPassword);
            if (pwdDict == null) return false;

            return int.Parse(pwdDict["threads"]) != threads ||
                int.Parse(pwdDict["iterations"]) != iterations ||
                int.Parse(pwdDict["memory"]) != memory;
        }

        private static string EncodePassword(byte[] hash, byte[] salt)
        {
            var saltString = Convert.ToBase64String(salt);
            var hashString = Convert.ToBase64String(hash);

            return $"{threads}${iterations}${memory}${saltString}${hashString}";
        }

        private static Dictionary<string, string> DecodePassword(string encodedPassword)
        {
            var dictionary = new Dictionary<string, string>();

            try {
                var splitStrings = encodedPassword.Split("$");
                dictionary["threads"] = splitStrings[0];
                dictionary["iterations"] = splitStrings[1];
                dictionary["memory"] = splitStrings[2];
                dictionary["salt"] = splitStrings[3];
                dictionary["hash"] = splitStrings[4];
            } catch (Exception e) {
                Console.WriteLine(e.StackTrace);
                return null;
            }

            return dictionary;
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
