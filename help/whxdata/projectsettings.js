// Publish project specific data
(function() {
rh = window.rh;
model = rh.model;
var defaultTopic = "First_Topic.htm";
rh._.exports(defaultTopic);
rh.consts('DEFAULT_TOPIC', encodeURI("First_Topic.htm"));
rh.consts('HOME_FILEPATH', encodeURI('index.htm'));
rh.consts('START_FILEPATH', encodeURI('index.htm'));
rh.consts('HELP_ID', '09cce50e-a30f-487b-bac2-cfd67e68c077' || 'preview');
rh.consts('LNG_SUBSTR_SEARCH', 0);

model.publish(rh.consts('KEY_LNG_NAME'), "pt");
model.publish(rh.consts('KEY_DIR'), "ltr");
model.publish(rh.consts('KEY_LNG'), {"BreadcrumbStart":"Início:","BrsNextButton":"Próximo","BrsPrevButton":"Anterior","CloseFavorites":"Fechar Favoritos","ContentsTab":"Conteúdo","CookiesAcceptText":"Pedimos-lhe que aceite os cookies com a finalidade de melhorar o desempenho, a legibilidade e a experiência. Os cookies são usados ​​para marcar os tópicos favoritos e para restaurar o índice e o glossário quando algum tópico for alterado. Essa configuração é solicitada apenas uma vez e pode ser revertida limpando os cookies do navegador.","CookiesAcceptButton":"Aceitar","CookiesDenyButton":"Mais tarde","EditFavorites":"Editar Favoritos","FavoriteArticle":"artigo salvo","FavoriteArticles":"artigos salvos","FullScreenButton":"Tela inteira","GlossaryTab":"Glossário","GlossResultHeaderLabel":"Dicionário do Glossário","HideLeftPanelTip":"Ocultar Painel Esquerdo","HideResults":"Ocultar resultados","HomeButton":"Início","HomePageLogoTitle":"Logotipo","HomePageSubtitle":"Como podemos ajudá-lo","IndexTab":"Índice","MCSearchResultShowFullTopic":"Leia mais...","MiniTOCCaption":"Neste tópico","NoResultsFoundText":"Nenhum resultado encontrado","PrintButtonTip":"Imprimir","RemoveFavItem":"Remover ","RemoveHighlight":"Remover destaque","ResultsFoundText":"%1 resultado(s) encontrado(s) para %2","SearchPlaceHolder":"Pesquisar...","IndexFilterKewords":"Filtrar palavras-chave","GlossaryFilterTerms":"Filtrar termos","SetAsFavorite":"Definir como Favorito","ShowLeftPanelTip":"Mostrar Painel Esquerdo","TOCTileArticlesCount":"artigo(s)","ToTopButtonTip":"Ir para o início","UnsetAsFavorite":"Remover de Favoritos","TopicHiddenText":"Este tópico tem os filtros selecionados aplicados.","ResetFilters":"Limpar filtros","SkipToMainContent":"Ir para o conteúdo principal","ClearSearchBox":"Limpar Caixa de Pesquisa","RemoveFilter":"Remover Filtro","SelectedFilters":"Limpar filtros","CloseSidebar":"Fechar Barra Lateral","OpenMenu":"Abrir Menu","CloseMenu":"Fechar Menu","ViewMore":"Ver mais","SearchPaginationLabel":"%1 a %2 de %3 resultados","NextSearchResults":"Próxima página de pesquisa","PrevSearchResults":"Página de pesquisa anterior"});

model.publish(rh.consts('KEY_HEADER_TITLE'), "Adição de Frações");
model.publish(rh.consts('PDF_FILE_NAME'), "");
model.publish(rh.consts('MAX_SEARCH_RESULTS'), "20");
model.publish(rh.consts('KEY_SKIN_FOLDER_NAME'), "Orange");
model.publish(rh.consts('CHAT_API_SESSION_TOKEN'), "");
model.publish(rh.consts('CHAT_API_PROJ_ID'), "");

model.publish(rh.consts('KEY_SUBSTR_SEARCH'), "");
model.publish(rh.consts('KEY_LOGO_URL'), "");
model.publish(rh.consts('KEY_SPECIAL_CHARS'), "0;1;2;3;4;5;6;7;8;9");
})();
