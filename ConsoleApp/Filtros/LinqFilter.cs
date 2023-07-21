using ScreenSoundAPI.Modelos;
using System.Linq;

namespace ScreenSoundAPI.Filtros;

internal class LinqFilter
{
    public static void FiltrarGenerosMusicas(List<Musica> musicas)
    {
        var generosMusicais = musicas.Select(genero => genero.GeneroMusica).Distinct().ToList();

        foreach (var genero in generosMusicais)
        {
            Console.WriteLine($"Genero: {genero}");
        }
    }

    public static void FiltrarArtistasPorGenero(List<Musica> musicas, string genero)
    {
        var artistasPorGeneroMusical = musicas.Where(musica => musica.GeneroMusica!.Contains(genero)).Select(musica => musica.NomeArtista).Distinct().ToList();

        Console.WriteLine($"Artistas do gênero {genero}:\n");
        foreach (var artista in artistasPorGeneroMusical)
        {
            Console.WriteLine($"- {artista}");
        }
    }

    public static void FiltrarMusicasPorArtistas(List<Musica> musicas, string artista)
    {
        var musicasPorArtistas = musicas.Where(musica => musica.NomeArtista!.Equals(artista)).ToList();
        Console.WriteLine($"Musicas do artista {artista}");
        foreach (var musica in musicasPorArtistas)
        {
            Console.WriteLine($"- {musica.NomeMusica}");
        }
    }
    public static void FiltrarMusicasPeloAno(List<Musica> musicas, int ano)
    {
        var musicasPorAno = musicas.Where(musica => musica.AnoInt!.Equals(ano)).ToList();
        Console.WriteLine($"Musicas do ano de {ano}");
        foreach (var musica in musicasPorAno)
        {
            Console.WriteLine($"{musica.NomeMusica}");
        }
    }

    public static void FiltrarMusicasPorEscala(List<Musica> musicas, string escala)
    {
        Dictionary<string, int> escalaMusical = new Dictionary<string, int>()
        {
            {"C",0},
            {"C#",1},
            {"D",2},
            {"D#",3},
            {"E",4},
            {"F",5},
            {"F#",6},
            {"G",7},
            {"G#",8},
            {"A",9},
            {"A#",10},
            {"B",11}
        };

        var musicasPorEscala = musicas.Where(musica => musica.KeyInt!.Equals(escalaMusical[escala])).ToList();
        Console.WriteLine($"Musicas da escala {escala}");
        foreach (var musica in musicasPorEscala)
        {
            Console.WriteLine($"- {musica.NomeMusica}");
        }
    }
}
