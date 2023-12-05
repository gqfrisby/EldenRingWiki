using EldenRingWiki.Data;
using System.Text.Json;

namespace EldenRingWiki.Services
{
    public class ArmorAPIService
    {
        private HttpClient httpClient;

        public ArmorAPIService()
        {
            httpClient = new HttpClient();
        }

        public async Task<int> GetArmorCount()
        {
        }
        public async Task<ArmorItem> GetArmor(int id)
        {
            var apiResponse = await httpClient.GetFromJsonAsync<JsonElement>($"https://eldenring.fanapis.com/api/armors/{id}");

            return new ArmorItem
            {
                Id = apiResponse.GetProperty("id").GetInt32(),
                Name = apiResponse.GetProperty("name").GetString(),
                Image = apiResponse.GetProperty("image").GetString(),
                Description = apiResponse.GetProperty("description").GetString(),
                Category = apiResponse.GetProperty("category").GetString(),
                Weight = apiResponse.GetProperty("weight").GetDouble()
            };
        }
    }
}
