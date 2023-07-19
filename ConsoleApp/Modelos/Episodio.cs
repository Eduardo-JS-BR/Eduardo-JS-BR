namespace ConsoleApp.Modelos;

internal class Episodio
{
    List<string> convidados = new List<string>();
    public Episodio(int numeroEpisodio, string? tituloEpisodio, int duracaoEpisodio)
    {
        NumeroEpisodio = numeroEpisodio;
        TituloEpisodio = tituloEpisodio;
        DuracaoEpisodio = duracaoEpisodio;
    }

    //resumo = concatena o número, titulo, duração e convidados

    public int NumeroEpisodio { get; }
    public string? TituloEpisodio { get; }
    public int DuracaoEpisodio { get; }
    public string? ResumoEpisodio => $"{NumeroEpisodio}. {TituloEpisodio}. ({DuracaoEpisodio} Minutos). - {string.Join(", ", convidados)}";

    //metodo adicionar convidados

    public void AdicionarConvidados(string? convidado)
    {
        convidados.Add(convidado);
    }
}