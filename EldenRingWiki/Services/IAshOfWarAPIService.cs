using EldenRingWiki.Data;

namespace EldenRingWiki.Services
{
    public interface IAshOfWarAPIService
    {
        Task<int> GetAshOfWarCount();
        Task<AshOfWarItem> GetAshOfWar(int id);
    }
}
