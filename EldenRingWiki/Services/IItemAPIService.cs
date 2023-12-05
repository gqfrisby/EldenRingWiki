using EldenRingWiki.Data;

namespace EldenRingWiki.Services
{
    public interface IItemAPIService
    {
        Task<int> GetItemCount();
        Task<BasicItem> GetItem(int id);
    }
}
