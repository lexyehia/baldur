using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;
using Microsoft.IdentityModel.Tokens;
using System;
using System.Collections.Generic;
using System.IdentityModel.Tokens.Jwt;
using System.Linq;
using System.Security.Claims;
using System.Threading.Tasks;

namespace Baldur.Server.Helpers
{
    public partial class Authenticator
    {
        private const string Secret = "SZvaqbF2uQKL5CeZKvPBJJesOiDufsOlD1QxDa9AA9FgRE0JEL4x04Bi4qIF";

        public static string GenerateToken(string username, int expireMinutes = 20)
        {
            var symmetricKey = Convert.FromBase64String(Secret);
            var tokenHandler = new JwtSecurityTokenHandler();
            var now = DateTime.UtcNow;

            var tokenDescriptor = new SecurityTokenDescriptor
            {
                Subject = new ClaimsIdentity(new[]
                {
                    new Claim(ClaimTypes.Name, username)
                }),

                Expires = now.AddMinutes(Convert.ToInt32(expireMinutes)),

                SigningCredentials = new SigningCredentials(
                    new SymmetricSecurityKey(symmetricKey),
                    SecurityAlgorithms.HmacSha256Signature)
            };

            var stoken = tokenHandler.CreateToken(tokenDescriptor);
            var token = tokenHandler.WriteToken(stoken);
            return token;
        }

        private static bool ValidateToken(string token, out string username)
        {
            username = null;

            if (token.StartsWith("Bearer ")) {
                token = token.Substring(7);
            } else {
                return false;
            }

            var simplePrincipal = GetPrincipal(token);

            if (simplePrincipal == null) return false;
            if (!(simplePrincipal.Identity is ClaimsIdentity identity)) return false;
            if (!identity.IsAuthenticated) return false;

            var usernameClaim = identity.FindFirst(ClaimTypes.Name);
            username = usernameClaim?.Value;

            if (string.IsNullOrEmpty(username)) return false;

            // Db validation

            return true;
        }

        public static ClaimsPrincipal GetPrincipal(string token)
        {
            try {
                var tokenHandler = new JwtSecurityTokenHandler();

                if (!(tokenHandler.ReadToken(token) is JwtSecurityToken jwtToken)) return null;

                var symmetricKey = Convert.FromBase64String(Secret);

                var validationParameters = new TokenValidationParameters()
                {
                    RequireExpirationTime = true,
                    ValidateIssuer = false,
                    ValidateAudience = false,
                    IssuerSigningKey = new SymmetricSecurityKey(symmetricKey),
                };

                var principal = tokenHandler.ValidateToken(token, validationParameters, out SecurityToken securityToken);
                return principal;
            } catch (Exception e) {
                Console.WriteLine(e);
                return null;
            }
        }

        [AttributeUsage(AttributeTargets.Class | AttributeTargets.Method)]
        public class AuthenticatedAttribute : AuthorizeAttribute, IAuthorizationFilter
        {
            public void OnAuthorization(AuthorizationFilterContext context)
            {
                string token = context.HttpContext.Request.Headers["Authorization"];

                if (token == null || !ValidateToken(token, out string username)) {
                    context.Result = new UnauthorizedResult();
                }
            }
        }
    }
}
