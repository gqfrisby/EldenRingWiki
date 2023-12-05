using EldenRingWiki.Data;
using System.Text.Json;

namespace EldenRingWiki.Services
{
    public class BossAPIService
    {
        private HttpClient httpClient;

        public BossAPIService()
        {
            httpClient = new HttpClient();
        }
        public async Task<BossItem> GetBoss(int id)
        {
            var apiResponse = await httpClient.GetFromJsonAsync<JsonElement>($"https://eldenring.fanapis.com/api/bosses/{id}");

            return new BossItem
            {
                Id = apiResponse.GetProperty("id").GetInt32(),
                Name = apiResponse.GetProperty("name").GetString(),
                Image = apiResponse.GetProperty("image").GetString(),
                Description = apiResponse.GetProperty("description").GetString(),
                //Type = apiResponse.GetProperty("type").GetString(),
                //Passive = apiResponse.GetProperty("passive").GetString()
            };
        }
    }
}
