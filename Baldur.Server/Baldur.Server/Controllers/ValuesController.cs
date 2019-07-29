﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Baldur.Server.Database;
using Baldur.Server.Entities;
using Baldur.Server.Helpers;
using Microsoft.AspNetCore.Mvc;
using static Baldur.Server.Helpers.Authenticator;

namespace Baldur.Server.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ValuesController : ControllerBase
    {
        // GET api/values
        [HttpGet]
        [Authenticated]
        public ActionResult<string> Get()
        {
            using (var db = new DataContext())
            {
                var newUser = new User
                {
                    Email = "bob@bob.com",
                    FirstName = "Bob",
                    LastName = "Doe"
                };

                var hash = HashPassword("bobrae");

                newUser.EncodedPassword = hash;

                var legit = VerifyPassword(hash, "bobrae");
                
                db.Users.Add(newUser);
                db.SaveChanges();
                var userCount = db.Users.Count();
                return "There are these many users: " + userCount.ToString();
            }
        }

        [HttpPost("token")]
        public ActionResult<string> GetToken()
        {
            return GenerateToken("bob@bob.com");
        }

        // GET api/values/5
        [HttpGet("{id}")]
        public ActionResult<string> Get(int id)
        {
            return "value";
        }

        // POST api/values
        [HttpPost]
        public void Post([FromBody] string value)
        {
        }

        // PUT api/values/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] string value)
        {
        }

        // DELETE api/values/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}
