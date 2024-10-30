<h1>Rapport de Projet de Programmation</h1>

<p><strong>Auteurs</strong> : Enzo Moran et Alexis Dahlen<br>
<strong>Cours</strong> : Algorithmique et Programmation | ENSAE Paris | Institut Polytechnique de Paris<br>
<strong>Superviseur</strong> : Xavier DUPRE<br>
<strong>Année</strong> : 2024</p>

<h2>Introduction</h2>
<p>Ce projet aborde le problème de réorganisation d'une grille de dimensions <code>m x n</code> dans laquelle il est demandé d'aligner les carreaux numérotés dans un ordre spécifique. L'objectif est de trouver la séquence de mouvements la plus courte pour ordonner les carreaux de telle sorte que chaque ligne contienne une séquence croissante de chiffres. Le projet se focalise sur l’implémentation et l’évaluation de plusieurs algorithmes de parcours de graphe pour résoudre ce puzzle efficacement, tout en proposant une interface utilisateur interactive pour expérimenter la solution.</p>

<h2>Analyse des Algorithmes</h2>

<h3>1. Algorithme BFS (Breadth-First Search)</h3>
<p>L'algorithme BFS permet de parcourir un graphe en largeur, idéal pour explorer des solutions par niveaux. Chaque état de la grille est modélisé comme un nœud du graphe, et un déplacement valide constitue une arête reliant deux nœuds.</p>
<ul>
  <li><strong>Description</strong> : L’algorithme utilise une file d'attente pour examiner chaque voisin d’un nœud avant de progresser vers des nœuds plus éloignés. Pour chaque état de la grille, BFS vérifie si l’état est déjà visité ou non.</li>
  <li><strong>Optimisation</strong> : La mémoire des nœuds visités est gérée via un dictionnaire (<code>father</code>), où chaque nœud est mappé avec son état précédent.</li>
  <li><strong>Complexité</strong> : Dans le pire des cas, la complexité de BFS est de <code>O(m * n * (m * n)!)</code>, ce qui inclut la visite de tous les états possibles de la grille.</li>
</ul>

<h3>2. Algorithme BFS Amélioré</h3>
<p>Le BFS amélioré optimise la recherche en intégrant la génération dynamique des nœuds explorés. Cela signifie que seuls les nœuds accessibles sont générés en temps réel, réduisant la charge mémoire par rapport au BFS classique.</p>
<ul>
  <li><strong>Description</strong> : Cet algorithme utilise une fonction <code>neighbors</code> pour générer uniquement les états accessibles depuis l’état courant. Cela permet de conserver en mémoire uniquement les états pertinents pour chaque étape de la recherche.</li>
  <li><strong>Complexité</strong> : Bien que dans le pire des cas la complexité reste théoriquement équivalente à celle du BFS classique, en pratique, cet algorithme est plus rapide car il réduit le nombre de nœuds explorés.</li>
</ul>

<h3>3. Algorithme A*</h3>
<p>L'algorithme A* (A-Star) combine des techniques de recherche informée pour prioriser les nœuds plus prometteurs et optimiser le parcours.</p>
<ul>
  <li><strong>Heuristique</strong> : La distance de Manhattan est utilisée comme heuristique, permettant d’évaluer rapidement la distance entre deux états.</li>
  <li><strong>Optimisation</strong> : Contrairement à BFS, chaque nœud est traité en fonction de son coût total, soit la somme du coût pour atteindre le nœud et du coût estimé pour atteindre la destination.</li>
  <li><strong>Complexité</strong> : La complexité est dominée par les opérations de tri et d’accès dans la liste ouverte, ce qui donne une complexité asymptotique de <code>O(m * n * log((m * n)!))</code>.</li>
</ul>

<h2>Interface Utilisateur avec Pygame</h2>
<p>Pour faciliter l’interaction et l’expérimentation, une interface graphique a été développée avec Pygame. Cette interface permet à l’utilisateur de jouer directement en effectuant des échanges de carreaux pour essayer de résoudre le puzzle manuellement. Une variable d'état (<code>running</code>) détermine si le jeu est en cours ou si le joueur a terminé.</p>

<ul>
  <li><strong>Fonctionnalités</strong> : 
    <ul>
      <li>L’utilisateur peut effectuer des échanges en cliquant sur les cases adjacentes.</li>
      <li>Le jeu affiche un écran de victoire lorsque le puzzle est résolu.</li>
    </ul>
  </li>
  <li><strong>Niveaux de Difficulté</strong> : La difficulté est modulée par la taille de la grille, augmentant le nombre de carreaux et la complexité du jeu.</li>
</ul>

<h2>Conclusion et Perspectives</h2>
<p>Ce projet a permis d’analyser différents algorithmes de parcours de graphe pour résoudre un problème de réarrangement de grille, avec un focus particulier sur l'optimisation mémoire et le temps d’exécution. Bien que BFS et BFS amélioré soient efficaces, A* se révèle être le meilleur compromis en termes de rapidité grâce à son approche informée.</p>

<p><strong>Perspectives</strong> : Plusieurs axes d’amélioration sont envisageables, notamment l’exploration de nouvelles heuristiques pour A*, la mise en place de fonctionnalités de suivi des scores ou l’ajout de grilles personnalisées pour varier les niveaux de difficulté.</p>
