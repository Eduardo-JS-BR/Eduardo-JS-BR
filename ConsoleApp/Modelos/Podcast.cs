namespace ConsoleApp.Modelos;

internal class Podcast
{
    private List<Episodio> episodios = new List<Episodio>();
    public Podcast(string? hostPodcast, string? nomePodcast)
    {
        HostPodcast = hostPodcast;
        NomePodcast = nomePodcast;
    }

    public string? HostPodcast { get; }
    public string? NomePodcast { get; }
    public int TotalEpisódios { get; set; }

    public void AdicionarEpisodios(Episodio episodio)
    {
        episodios.Add(episodio);
    }

    public void ExibirDetalhes()
    {
        Console.WriteLine($"\nLista de Episódios do Podcast {NomePodcast}:\n");
        Console.WriteLine($"Host: {HostPodcast}, Nome do Podcast: {NomePodcast}\n");
        foreach( var episode in episodios )
        {
            Console.WriteLine($"Episódio: {episode.ResumoEpisodio}");
        }
    }
}