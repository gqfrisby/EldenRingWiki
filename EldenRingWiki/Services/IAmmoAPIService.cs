using EldenRingWiki.Data;

namespace EldenRingWiki.Services
{
    public interface IAmmoAPIService
    {
        Task<int> GetAmmoCount();
        Task<AmmoItem> GetAmmo(string id);
    }
}
