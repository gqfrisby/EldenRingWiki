using EldenRingWiki.Data;

namespace EldenRingWiki.Services
{
    public interface IWeaponAPIService
    {
        Task<int> GetWeaponCount();
        Task<WeaponItem> GetWeapon(int id);
    }
}
