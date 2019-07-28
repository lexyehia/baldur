using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Baldur.Server.Config
{
    public class DataContext : DbContext
    {
        private readonly string schema;

        public DataContext(string schema)
        {
            this.schema = schema;
        }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {

            optionsBuilder.UseNpgsql("postgres://postgres:12345@localhost:5432");
        }

        protected override void OnModelCreating(ModelBuilder builder)
        {
            builder.HasDefaultSchema(schema);
        }
    }
}
