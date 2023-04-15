void percursoLargura( int vInicio ){
	int nroNosMarcados = 0, n, m,
		nosMarcados = new int [nroVertices];
	Fila f = new Fila();
	visitarNo( vInicio);
	marcarNo( nosMarcados, nroNosMarcados, vInicio );
	f.enqueue ( vInicio );
	while (!f.qIsEsmpty()){
		n = f.dequeue();
	// Existe nó adjacente a n ainda não marcado
		while ((m = noAdjacente( n, nosMarcados ))!= -1){
			visitarNo( m );
			f.enqueue( m );
			marcarNo( nosMarcados, nroNosMarcados, m );
	} }
}
