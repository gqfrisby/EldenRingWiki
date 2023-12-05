using EldenRingWiki.Data;

namespace EldenRingWiki.Services
{
    public interface IClassAPIService
    {
        Task<int> GetClassCount();
        Task<ClassItem> GetClass(int id);
    }
}
