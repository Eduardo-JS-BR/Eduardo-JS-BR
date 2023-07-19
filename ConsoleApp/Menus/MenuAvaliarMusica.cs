using ConsoleApp.Modelos;

namespace ConsoleApp.Menus;

internal class MenuAvaliarMusica : Menu
{
    public override void Executar(Dictionary<string, Banda> bandasRegistradas)
    {
        base.Executar(bandasRegistradas);

        ExibirTituloDaOpcao("Avaliar música");
        Console.Write("\nDigite o nome da banda que deseja avaliar: ");
        string nomeDaBanda = Console.ReadLine()!;
        Banda banda = bandasRegistradas[nomeDaBanda];
        if (bandasRegistradas.ContainsKey(nomeDaBanda))
        {
            Console.Write("\nDigite o nome do album que deseja avaliar: ");
            string nomeDoAlbum = Console.ReadLine()!;
            if (banda.Albuns.Any(a => a.NomeAlbum.Equals(nomeDoAlbum)))
            {
                Album album = banda.Albuns.First(a => a.NomeAlbum.Equals(nomeDoAlbum));
                Console.Write("\nDigite o nome da música que deseja avaliar: ");
                string nomeDaMusica = Console.ReadLine()!;
                if (album.Musicas.Any(a => a.NomeMusica.Equals(nomeDaMusica)))
                {
                    Console.Write($"\nQual a nota que o musica {nomeDaMusica} merece: ");
                    Musica musica = album.Musicas.First(a => a.NomeMusica.Equals(nomeDaMusica));
                    Avaliacao nota = Avaliacao.Parse(Console.ReadLine()!);
                    musica.AdicionarNota(nota);
                    Console.Write($"\nA nota {nota.Nota} foi registrada com sucesso para o música {nomeDaMusica}");
                    Thread.Sleep(2000);
                    Console.Clear();
                }
                else
                {
                    Console.WriteLine($"\nA musica {nomeDaMusica} não foi encontrada!");
                    Console.WriteLine("Digite uma tecla para voltar ao menu principal");
                    Console.ReadKey();
                    Console.Clear();
                }
            }
            else
            {
                Console.WriteLine($"\nO album {nomeDoAlbum} não foi encontrado!");
                Console.WriteLine("Digite uma tecla para voltar ao menu principal");
                Console.ReadKey();
                Console.Clear();
            }
        }
        else
        {
            Console.WriteLine($"\nA banda {nomeDaBanda} não foi encontrada!");
            Console.WriteLine("Digite uma tecla para voltar ao menu principal");
            Console.ReadKey();
            Console.Clear();
        }
    }
}