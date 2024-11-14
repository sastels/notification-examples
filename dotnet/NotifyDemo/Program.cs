using Microsoft.Extensions.Configuration;
using Newtonsoft.Json.Linq;
using System.Text;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        Console.WriteLine("\n\nNotify Demo\n\n");

        // Read environment variables
        var config =
            new ConfigurationBuilder()
                .SetBasePath(Directory.GetCurrentDirectory())
                .AddEnvironmentVariables()
                .Build();


        var notifyUrl = "https://api.notification.canada.ca/v2/notifications/email";

        var jsonObject = new JObject
        {
            ["email_address"] = "stephen.astels@cds-snc.ca",
            ["template_id"] = config["TEMPLATE_ID"],
            ["personalisation"] = new JObject
            {
                ["var"] = "api demo!"
            }
        };
        var content = new StringContent(jsonObject.ToString(), Encoding.UTF8, "application/json");

        client.DefaultRequestHeaders.Add("Authorization", "ApiKey-v1 " + config["API_KEY"]);

        Console.WriteLine("Sending Email");

        var response = await client.PostAsync(notifyUrl, content);

        Console.WriteLine("Sent!");

        // Always check the response - we should have a 201
        var responseCode = response.StatusCode;
        var responseString = await response.Content.ReadAsStringAsync();
        Console.WriteLine("Response Code: " + responseCode);
        Console.WriteLine("Response: " + responseString);
    }
}



