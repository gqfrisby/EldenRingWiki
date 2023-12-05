using EldenRingWiki.Data;

namespace EldenRingWiki.Services
{
    public interface ISpiritAPIService
    {
        Task<int> GetSpiritCount();
        Task<SpititItem> GetSpirit(int id);
    }
}
