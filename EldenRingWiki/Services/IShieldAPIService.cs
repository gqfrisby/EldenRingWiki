using EldenRingWiki.Data;

namespace EldenRingWiki.Services
{
    public interface IShieldAPIService
    {
        Task<int> GetShieldCount();
        Task<ShieldItem> GetShield(int id);
    }
}
