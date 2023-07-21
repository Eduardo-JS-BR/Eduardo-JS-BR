using ScreenSoundAPI.Modelos;

namespace ScreenSoundAPI.Filtros;

internal class LinqOrder
{
    public static void ExibirListaDeArtistasOrdenados(List<Musica> musicas)
    {
        var artistasOrdenados = musicas.OrderBy(musica => musica.NomeArtista).Select(musica => musica.NomeArtista).Distinct().ToList();

        foreach (var artista in artistasOrdenados)
        {
            Console.WriteLine($"Artista: {artista}");
        }
    }
}
