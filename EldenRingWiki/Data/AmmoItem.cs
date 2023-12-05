using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EldenRingWiki.Data
{
    public class AmmoItem
    {
        public int id { get; set; }
        public string name { get; set; }
        public string image { get; set; }
        public string description { get; set; }
        public string type { get; set; }
        public string passive { get; set; }

        //public Dictionary<string, int> AttackPowers { get; set; }
    }
}
