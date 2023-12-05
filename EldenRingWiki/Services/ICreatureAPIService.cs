using EldenRingWiki.Data;

namespace EldenRingWiki.Services
{
    public interface ICreatureAPIService
    {
        Task<int> GetCreatureCount();
        Task<CreatureItem> GetCreature(int id);
    }
}
