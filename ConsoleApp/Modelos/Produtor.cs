namespace ConsoleApp.Modelos;

internal class Produtor
{
    public Produtor(string? nomeProdutor)
    {
        NomeProdutor = nomeProdutor;
    }

    public string? NomeProdutor { get; }

    public void ExibirNomeProdutor()
    {
        if (NomeProdutor != null)
            Console.WriteLine($"Produtor: {NomeProdutor}.");
    }
}