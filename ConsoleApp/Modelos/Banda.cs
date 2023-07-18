namespace ConsoleApp.Modelos;

class Banda
{
    private List<Album> albuns = new List<Album>();
    private List<int> notas = new List<int>();

    public Banda(string? nomeBanda)
    {
        NomeBanda = nomeBanda;
    }

    public string? NomeBanda { get; }
    public double Media => notas.Average();
    public List<Album> Albuns => albuns;

    public void AdicionarAlbum(Album album)
    {
        albuns.Add(album);
    }

    public void AdicionarNota(int nota)
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