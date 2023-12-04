﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EldenRingWiki.Data    
{
    internal class ClassItem : IClassModel
    {
        public string Id { get; set; }
        public string Name { get; set; }
        public string Image { get; set; }
        public string Description { get; set; }
        public string[] Stats { get; set; }
    }
}
