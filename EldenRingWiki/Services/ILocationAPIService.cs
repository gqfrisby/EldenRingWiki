using EldenRingWiki.Data;

namespace EldenRingWiki.Services
{
    public interface ILocationAPIService
    {
        Task<int> GetLocationCount();
        Task<LocationItem> GetLocation(int id);
    }
}
