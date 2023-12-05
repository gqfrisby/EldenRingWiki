using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EldenRingWiki.Data
{
    public class ArmorItem
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Image { get; set; }
        public string Description { get; set; }
        public string Category { get; set; }
        public double Weight { get; set; }
        //public Dictionary<string, int> DmgNegation { get; set; }
        //public Dictionary<string, int> Resistance { get; set; }
    }
}
