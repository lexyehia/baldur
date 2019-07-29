using Microsoft.EntityFrameworkCore.Migrations;

namespace Baldur.Server.Migrations
{
    public partial class password : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "EncodedPassword",
                schema: "public",
                table: "Users",
                nullable: true);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "EncodedPassword",
                schema: "public",
                table: "Users");
        }
    }
}
