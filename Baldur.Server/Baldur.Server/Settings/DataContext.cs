using Baldur.Server.Entities;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Baldur.Server.Database
{
    public class DataContext : DbContext
    {
        public DbSet<User> Users { get; set; }
        public DbSet<Firm> Firms { get; set; }
        public DbSet<Matter> Matters { get; set; }

        private readonly string schema;

        public DataContext(string schema = "public")
        {
            this.schema = schema;
        }

        public DataContext(DbContextOptions<DataContext> options): base(options) { }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {

            optionsBuilder.UseNpgsql("Host=localhost;Database=baldur;Username=postgres;Password=12345");
        }

        protected override void OnModelCreating(ModelBuilder builder)
        {
            builder.HasDefaultSchema(schema);
        }
    }

    public class DataContextFactory : IDesignTimeDbContextFactory<DataContext>
    {
        public DataContext CreateDbContext(string[] args) => new DataContext();
    }
}
