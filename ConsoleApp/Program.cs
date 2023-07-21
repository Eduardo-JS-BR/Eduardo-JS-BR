using ScreenSoundAPI.Modelos;
using ScreenSoundAPI.Filtros;
using System.Text.Json;

using (HttpClient client = new HttpClient())
{
    try
    {
        string resposta = await client.GetStringAsync("https://guilhermeonrails.github.io/api-csharp-songs/songs.json");
        var musicas = JsonSerializer.Deserialize<List<Musica>>(resposta)!;

        //var musicasFavoritas = new MusicasPreferidas("Eduardo");
        //musicasFavoritas.AdicionarMusicasFavoritas(musicas[1]);
        //musicasFavoritas.AdicionarMusicasFavoritas(musicas[63]);
        //musicasFavoritas.AdicionarMusicasFavoritas(musicas[843]);
        //musicasFavoritas.AdicionarMusicasFavoritas(musicas[6]);
        //musicasFavoritas.AdicionarMusicasFavoritas(musicas[1790]);
        //musicasFavoritas.ExibirMusicasFavoritas();
        //musicasFavoritas.GerarArquivoJson();

        //musicas[0].ExibirDetalhesDaMusica();
        LinqFilter.FiltrarMusicasPorEscala(musicas, "C#");
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Erro: {ex.Message}");
    }
}