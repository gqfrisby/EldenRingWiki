using EldenRingWiki.Data;

namespace EldenRingWiki.Services
{
    public interface IArmorAPIService
    {
        Task<int> GetArmorCount();
        Task<ArmorItem> GetArmor(int id);
    }
}
