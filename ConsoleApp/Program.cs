Banda queen = new Banda("Queen");
Genero rock = new Genero("Rock");
Produtor roy = new Produtor("Roy Thomas Baker");
Estudio emi = new Estudio("EMI");

Album albumDoQueen = new Album("A Night at the Opera");

Musica musica1 = new Musica(queen, "Love of my Life")
{
    DuracaoMusica = 213,
    DisponibilidadeMusica = true,
    GeneroMusica = rock,
    ProdutorMusica = roy,
    EstudioMusica = emi,
};

Musica musica2 = new Musica(queen, "Bohemian Rhapsody")
{
    DuracaoMusica = 354,
    DisponibilidadeMusica = true,
    GeneroMusica = rock,
    ProdutorMusica = roy,
    EstudioMusica = emi,
};

albumDoQueen.AdicionarMusica(musica1);
albumDoQueen.AdicionarMusica(musica2);
queen.AdicionarAlbum(albumDoQueen);

musica1.ExibirFichaTecnica();
musica2.ExibirFichaTecnica();
albumDoQueen.ExibirMusicasDoAlbum();
queen.ExibirDiscografiaDaBanda();

//Episodio ep1 = new(1, "Thomas Aprende uma Lição", 11);
//ep1.AdicionarConvidados("Rev. W. Awdry");
//ep1.AdicionarConvidados("Britt Alcroft");
//ep1.AdicionarConvidados("David Mitton");
//
//Episodio ep2 = new(2, "A Ajuda de Edward", 11);
//ep2.AdicionarConvidados("Rev. W. Awdry");
//ep2.AdicionarConvidados("Britt Alcroft");
//ep2.AdicionarConvidados("David Mitton");
//
//Episodio ep3 = new(3, "Saia Daí, Henry", 11);
//ep3.AdicionarConvidados("Rev. W. Awdry");
//ep3.AdicionarConvidados("Britt Alcroft");
//ep3.AdicionarConvidados("David Mitton");
//
//Podcast ttte = new("HIT", "Thomas e Seus Amigos");
//ttte.AdicionarEpisodios(ep1);
//ttte.AdicionarEpisodios(ep2);
//ttte.AdicionarEpisodios(ep3);
//ttte.ExibirDetalhes();