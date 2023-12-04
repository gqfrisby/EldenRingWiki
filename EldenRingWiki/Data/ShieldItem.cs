using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EldenRingWiki.Data
{
    internal class ShieldItem : IClassModel
    {
        public string Id { get; set; }
        public string Name { get; set; }
        public string Image { get; set; }
        public string Description { get; set; }
        public string Category { get; set; }
        public double Weight { get; set; }
        //public Dictionary<string, int> Attack { get; set; }
        //public Dictionary<string, int> Defense { get; set; }
        //public Dictionary<string, int> RequiredAttributes { get; set; }
        //public Dictionary<string, string> ScalesWith { get; set; }
    }
}
