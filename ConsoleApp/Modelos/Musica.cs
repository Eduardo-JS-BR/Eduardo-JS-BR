namespace ConsoleApp.Modelos;

internal class Musica : IAvaliavel
{
    List<Avaliacao> notas = new();
    public Musica(Banda nomeArtista, string? nomeMusica)
    {
        NomeArtista = nomeArtista;
        NomeMusica = nomeMusica;
    }

    public string? NomeMusica { get; }
    public Banda? NomeArtista { get; }
    public int DuracaoMusica { get; set; }
    public bool DisponibilidadeMusica { get; set; }
    public string? DescricaoResumida => $"A música {NomeMusica} pertence ao artista {NomeArtista}.";
    public Genero? GeneroMusica { get; set; }
    public Produtor? ProdutorMusica { get; set; }
    public Estudio? EstudioMusica { get; set; }

    public double Media
    {
        get
        {
            if (notas.Count == 0) return 0;
            else return notas.Average(a => a.Nota);
        }
    }

    public void ExibirFichaTecnica()
    {
        Console.WriteLine($"\nNome da Música: {NomeMusica}");
        Console.WriteLine($"Nome do Artista: {NomeArtista.NomeBanda}");
        Console.WriteLine($"Genêro da Música: {GeneroMusica.GeneroMusica}");
        Console.WriteLine($"Duração: {DuracaoMusica} minutos");
        Console.WriteLine($"Produtor: {ProdutorMusica.NomeProdutor}");
        Console.WriteLine($"Estudio: {EstudioMusica.Studio}");
        if (DisponibilidadeMusica)
        {
            Console.WriteLine("Disponível no Plano.");
        }
        else
        {
            Console.WriteLine("Assine o plano plus.");
        }
    }

    public void AdicionarNota(Avaliacao nota)
    {
        notas.Add(nota);
    }
}