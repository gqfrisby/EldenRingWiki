using EldenRingWiki.Data;

namespace EldenRingWiki.Services
{
    public interface IBossAPIService
    {
        Task<int> GetBossCount();
        Task<BossItem> GetBoss(int id);
    }
}
