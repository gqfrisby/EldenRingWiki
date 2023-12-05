using EldenRingWiki.Data;

namespace EldenRingWiki.Services
{
    public interface ITalismanAPIService
    {
        Task<int> GetTalismanCount();
        Task<TalismanItem> GetTalisman(int id);
    }
}
