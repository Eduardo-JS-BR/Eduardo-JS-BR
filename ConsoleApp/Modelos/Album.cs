namespace ConsoleApp.Modelos;

internal class Album : IAvaliavel
{
    private List<Musica> musicas = new List<Musica>();
    private List<Avaliacao> notas = new();

    public Album(string? nomeAlbum)
    {
        NomeAlbum = nomeAlbum;
    }

    public string? NomeAlbum { get; }
    public double DuracaoAlbum => musicas.Sum(m => m.DuracaoMusica);
    public List<Musica> Musicas => musicas;

    public double Media
    {
        get
        {
            if (notas.Count == 0) return 0;
            else return notas.Average(a => a.Nota);
        }
    }

    public void AdicionarMusica(Musica musica)
    {
        musicas.Add(musica);
    }

    public void AdicionarNota(Avaliacao nota)
    {
        notas.Add(nota);
    }

    public void ExibirMusicasDoAlbum()
    {
        Console.WriteLine($"\nLista de músicas do album {NomeAlbum}:\n");
        foreach (var musica in musicas)
        {
            Console.WriteLine($"Música: {musica.NomeMusica}");
        }
        Console.WriteLine($"\nPara ouvir esse album inteiro você precisa de {DuracaoAlbum} segundos.");
    }
}