using EldenRingWiki.Data;
using System.Text.Json;

namespace EldenRingWiki.Services
{
    public class AshOfWarAPIService
    {
        private HttpClient httpClient;

        public AshOfWarAPIService()
        {
            httpClient = new HttpClient();
        }
        public async Task<AshOfWarItem> GetAshOfWar(int id)
        {
            var apiResponse = await httpClient.GetFromJsonAsync<JsonElement>($"https://eldenring.fanapis.com/api/ashes/{id}");

            return new AshOfWarItem
            {
                Id = apiResponse.GetProperty("id").GetInt32(),
                Name = apiResponse.GetProperty("name").GetString(),
                Image = apiResponse.GetProperty("image").GetString(),
                Description = apiResponse.GetProperty("description").GetString(),
                Affinity = apiResponse.GetProperty("affinity").GetString(),
                Skill = apiResponse.GetProperty("skill").GetString()
            };
        }
    }
}
