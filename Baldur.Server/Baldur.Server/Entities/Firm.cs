using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Baldur.Server.Entities
{
    public class Firm
    {
        [Key]
        public int Id { get; set; }
    }
}
