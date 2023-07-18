namespace ConsoleApp.Modelos;

class Estudio
{
    public Estudio(string? studio)
    {
        Studio = studio;
    }

    public string? Studio { get; }

    public void ExibirEstudio()
    {
        if (Studio == null)
            Console.WriteLine($"Estúdio: {Studio}.");
    }
}