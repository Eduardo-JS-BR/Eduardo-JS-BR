namespace ConsoleApp.Modelos;

internal class Genero
{
    public Genero(string? generoMusica)
    {
        GeneroMusica = generoMusica;
    }

    public string? GeneroMusica { get; }

    public void ExibirGeneroDaMusica()
    {
        if (GeneroMusica == null)
            Console.WriteLine($"Genero: {GeneroMusica}");
    }
}