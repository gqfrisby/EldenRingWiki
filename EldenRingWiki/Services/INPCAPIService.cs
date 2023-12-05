using EldenRingWiki.Data;

namespace EldenRingWiki.Services
{
    public interface INPCAPIService
    {
        Task<int> GetNPCCount();
        Task<NPCItem> GetNPC(int id);
    }
}
