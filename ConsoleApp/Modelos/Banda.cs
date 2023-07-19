namespace ConsoleApp.Modelos;

internal class Banda : IAvaliavel
{
    private List<Album> albuns = new List<Album>();
    private List<Avaliacao> notas = new List<Avaliacao>();

    public Banda(string? nomeBanda)
    {
        NomeBanda = nomeBanda;
    }

    public string? NomeBanda { get; }
    public double Media
    {
        get
        {
            if (notas.Count == 0) return 0;
            else return notas.Average(a => a.Nota);
        }
    }
    public IEnumerable<Album> Albuns => albuns;

    public void AdicionarAlbum(Album album)
    {
        albuns.Add(album);
    }

    public void AdicionarNota(Avaliacao nota)
    {
        notas.Add(nota);
    }

    public void ExibirDiscografiaDaBanda()
    {
        Console.WriteLine($"\nDiscografia da banda {NomeBanda}");
        foreach(Album album in albuns)
        {
            Console.WriteLine($"Algum: {album.NomeAlbum} ({album.DuracaoAlbum} segundos)");
        }
    }
}