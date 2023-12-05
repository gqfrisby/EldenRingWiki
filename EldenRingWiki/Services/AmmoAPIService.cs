using EldenRingWiki.Data;
using System.Text.Json;
using System.Transactions;
using Newtonsoft;

namespace EldenRingWiki.Services
{
    public class AmmoAPIService : IAmmoAPIService
    {
        private HttpClient httpClient;

        public AmmoAPIService()
        {
            httpClient = new HttpClient();
        }

        public async Task<int> GetAmmoCount()
        {
        }

        public async Task<AmmoItem> GetAmmo(string id)
        {
            var apiResponse = await httpClient.GetFromJsonAsync<JsonElement>($"https://eldenring.fanapis.com/api/ammos?name={id}");
            var response2 = apiResponse.GetProperty("data");
            //string preparse = apiResponse.GetProperty("id").GetString();
            //int postparse = Int32.Parse(preparse);
            Console.WriteLine(response2);

            return new AmmoItem
            {
                id = 1,
                name = response2[1],
                image = response2[2].GetString(),
				description = response2[3].GetString(),
                type = response2[4].GetString(),
                passive = "Blank"
            };
        }
    }
}
