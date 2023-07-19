using ConsoleApp.Modelos;

namespace ConsoleApp.Menus;

internal class MenuRegistrarMusica : Menu
{
    public override void Executar(Dictionary<string, Banda> bandasRegistradas)
    {
        base.Executar(bandasRegistradas);

        ExibirTituloDaOpcao("Registro de músicas");
        Console.Write("Digite a banda cujo música deseja registrar: ");
        string nomeDaBanda = Console.ReadLine()!;
        Banda banda = bandasRegistradas[nomeDaBanda];
        if (bandasRegistradas.ContainsKey(nomeDaBanda))
        {
            Console.Write("\nDigite o título do álbum da música deseja registrar: ");
            string nomeDoAlbum = Console.ReadLine()!;
            if (banda.Albuns.Any(a => a.NomeAlbum.Equals(nomeDoAlbum)))
            {
                Album album = banda.Albuns.First(a => a.NomeAlbum.Equals(nomeDoAlbum));
                Console.Write("\nDigite o nome da música a ser registrada: ");
                string nomeDaMusica = Console.ReadLine()!;
                album.AdicionarMusica(new Musica(new Banda(nomeDaBanda), nomeDaMusica));
                Console.WriteLine($"\nA musica {nomeDaMusica} foi registrada ao album {nomeDoAlbum} da banda {nomeDaBanda}");
                Thread.Sleep(4000);
                Console.Clear();
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
