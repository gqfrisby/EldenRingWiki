using EldenRingWiki.Data;

namespace EldenRingWiki.Services
{
    public interface IIncantationAPIService
    {
        Task<int> GetIncantationCount();
        Task<IncantationItem> GetIncantation(int id);
    }
}
