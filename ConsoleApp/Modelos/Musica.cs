using System.Text.Json.Serialization;

namespace ScreenSoundAPI.Modelos;

internal class Musica
{
    [JsonPropertyName("song")]
    public string? NomeMusica { get; set; }
    [JsonPropertyName("artist")]
    public string? NomeArtista { get; set; }
    [JsonPropertyName("duration_ms")]
    public int DuracaoMusica { get; set; }
    [JsonPropertyName("genre")]
    public string? GeneroMusica { get; set; }
    [JsonPropertyName("year")]
    public string? AnoString { get; set; }
    public int AnoInt
    {
        get
        {
            return int.Parse(AnoString!);
        }
    }
    [JsonPropertyName("key")]
    public int? KeyInt { get; set; }

    Dictionary<int, string> escalaMusical = new Dictionary<int, string>()
    {
        {0,"C"},
        {1,"C#"},
        {2,"D"},
        {3,"D#"},
        {4,"E"},
        {5,"F"},
        {6,"F#"},
        {7,"G"},
        {8,"G#"},
        {9,"A"},
        {10,"A#"},
        {11,"B"}
    };

    public void ExibirDetalhesDaMusica()
    {
        Console.WriteLine($"\nMúsica: {NomeMusica}");
        Console.WriteLine($"Artista: {NomeArtista}");
        Console.WriteLine($"Ano: {AnoInt}");
        Console.WriteLine($"Duração: {DuracaoMusica / 1000} segundos");
        Console.WriteLine($"Gênero: {GeneroMusica}");
        Console.WriteLine($"Key: {escalaMusical[KeyInt.Value]}");
    }
}
