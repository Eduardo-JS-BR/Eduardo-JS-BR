namespace ConsoleApp.Modelos;

class Album
{
    private List<Musica> musicas = new List<Musica>();

    public Album(string? nomeAlbum)
    {
        NomeAlbum = nomeAlbum;
    }

    public string? NomeAlbum { get; }
    public double DuracaoAlbum => musicas.Sum(m => m.DuracaoMusica);
    public List<Musica> Musicas => musicas;

    public void AdicionarMusica(Musica musica)
    {
        musicas.Add(musica);
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