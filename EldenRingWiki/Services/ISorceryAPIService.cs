using EldenRingWiki.Data;

namespace EldenRingWiki.Services
{
    public interface ISorceryAPIService
    {
        Task<int> GetSorceryCount();
        Task<SorceriesItem> GetSorcery(int id);
    }
}
