using EldenRingWiki.Data;
using System.Text.Json;

namespace EldenRingWiki.Services
{
    public class ClassAPIService
    {
        private HttpClient httpClient;

        public ClassAPIService()
        {
            httpClient = new HttpClient();
        }

        public async Task<ClassItem> GetClass(int id)
        {
            var apiResponse = await httpClient.GetFromJsonAsync<JsonElement>($"https://eldenring.fanapis.com/api/classes/{id}");

            return new ClassItem
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
