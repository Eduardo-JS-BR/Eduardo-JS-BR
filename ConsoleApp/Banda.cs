class Banda
{
    private List<Album> albuns = new List<Album>();

    public Banda(string? nomeBanda)
    {
        NomeBanda = nomeBanda;
    }

    public string? NomeBanda { get; }

    public void AdicionarAlbum(Album album)
    {
        albuns.Add(album);
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