using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EldenRingWiki.Data
{
    public class IncantationItem 
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Image { get; set; }
        public string Description { get; set; }
        public string Type { get; set; }
        public int Cost { get; set; }
        public int Slots { get; set; }
        public string Effects { get; set; }
        //public Dictionary<string, int> Requires { get; set; }
    }
}
