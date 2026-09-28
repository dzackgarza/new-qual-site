## Warm-up Problems

• $T _ { 4 } \Rightarrow T _ { 3 } \Rightarrow T _ { 2 } \Rightarrow T _ { 1 } \Rightarrow T _ { 0 }$

• (June 2004, A3) Show that if X is a Hausdorff space, and A, $B \subseteq X$ are disjoint, finite subsets of X, then there are disjoint open sets U, V in X with $A \subseteq U$ and $B \subseteq V$

• (June 2009, A4) Let (X, T ) and $( X , \mathcal { T } ^ { \prime } )$ be topological spaces with $\mathcal { T } \subseteq \mathcal { T } ^ { \prime } )$ . (a) If $( X , T ^ { \prime } )$ is normal, must (X, T ) also be normal?

## Separation Axioms:

1. (Jan 2004, A2) Show that if the metric space $( X , d )$ is separable (ie, it contains a countable dense subset), then the metric topology on X is second countable.

2. (Jan 2004, A4) Two subsets A, $B \subseteq X$ of the space (X, T ) are called separated if there are $U , V \in { \mathcal { T } }$ with $A \subseteq U \subseteq X \backslash B$ and $B \subseteq V \subseteq X \backslash A$ . X is called completely normal if X is $T _ { 1 }$ and for every pair of separated subsets A, B there are $U , V \in { \mathcal { T } }$ such that $A \subseteq U , B \subseteq V$ , and $U \cap V = \emptyset$

Show that a space $( X , \tau )$ is completely normal if and only if every subset of X is normal.

3. (June 2004, A4) Show that for a topological space X, if every $x \in X$ has an open neighborhood whose closure is a regular space, then X is regular.

4. (June 2009, A1) Show that every compact metrizable space has a countable basis.

## Counterexamples:

1. (Jan 2004, A3) Let $( X , \tau )$ be a Hausdorff space and let ${ \mathcal { T } } ^ { \prime } = \{ U \subseteq X : X \backslash U$ is compact}∪ {∅}. Show that $\tau ^ { \prime }$ is a topology on X, and is coarser than T . Show that, in general, they need not be equal.

2. (June 2008, A1) Let A be a subset of a topological space X and let B be a subset of a topological space Y . Let $X \times Y$ be the product space, and let intZ(C) denote the interior of the set C in the space Z. Prove or give a counterexample to int $x \times Y ( A \times B ) =$ in ${ \mathrm { ; } } _ { X } ( A ) \times \operatorname { i n t } _ { Y } ( B )$

3. (June 2009, A2) For a topological space X and $y \in X$ , the path component $P _ { y }$ of X containing y is the largest path-connected subset with $y \in P _ { y } \subseteq X$

(a) Show that this concept is well-defined (that is, show that every point y is contained in a largest path-connected subset).

(b) Give an example of a space and a point $y \in X$ so that $P _ { y }$ is neither an open nor a closed subset of X.

## Definition Problems:

1. (Jan 2002, A2) Let X be a topological space. A set $A \subseteq X$ is called nowhere dense if the closure A of A has empty interior, ie, int $( { \overline { { A } } } ) = \varnothing$ . Show that if $U \subseteq X$ is open, then $A = { \overline { { U } } } \backslash U$ is nowhere dense.

2. (June 2005, A4) A topological space X is called metacompact if for every open cover C of X, there is a subcover $C ^ { \prime }$ satisfying the property that for every point $p \in X$ , there are only finitely many open sets in $C ^ { \prime }$ containing p.

(a) Show that metacompactness is a homeomorphism invariant.

(b) Let X be the integers with the topology ${ \mathcal { T } } : = \{ U \subseteq X | 0 \in U \} \cup \{ \emptyset \}$ . Show that this space is not metacompact.

3. (Jan 2006, A2) A topological space (X, T ) is called limit-point compact if every infinite subset A of X has a limit point. Show that every closed subset of a limit-point compact space is limit-point compact.

4. (June 2014, A4) A space X is locally connected if for each $x \in X$ and each open set U containing x, there is a connected open set V in X satisfying $x \in V \subseteq U$ . Let X and Y be locally connected spaces. Determine whether or not the product space $X \times Y$ must also be locally connected.

Separation Axioms Definitions

• If a space X has a countable basis for its topology, then X is said to be second countable.

• A subset A of a space X is dense in X if ${ \overline { { A } } } = X$

• A space having a countable dense subset is separable.

$X$ is $T _ { 0 }$ if for any two distinct points $a , b \in X$ there is an open set U containing one of a or b but not both.

• X is $T _ { 1 }$ if for any two distinct points $a , b \in X$ there are open sets $U , V$ in X with $a \in U , b \notin U .$ , and $b \in V , a \not \in V$

• X is $T _ { 2 }$ (Hausdorff) if for any two distinct points $a , b \in X$ there are disjoint open sets $U , V$ in X with $a \in U$ and $b \in V$

• X is $T _ { 3 }$ (Regular) if X is $T _ { 1 }$ and for any point $a \in X$ and closed set B in X with a $\notin B$ , there are disjoint open sets $U , V$ in X with $a \in U$ and $B \subseteq V$

• X is $T _ { 4 }$ (Normal) if X is T1 and for any two disjoint closed sets A, B in X there are disjoint open sets $U , V$ in X with $A \subseteq U$ and $B \subseteq V$

Useful examples:

• R with the finite complement topology is $T _ { 1 }$ but not $T _ { 2 }$

$X = \{ a , b \}$ with $\mathcal { T } = \{ \emptyset , \{ a \} , X \}$ is $T _ { 0 }$ but not $T _ { 1 }$

• Any space X with the power set (discrete) topology is $T _ { 4 }$

Common places to look for counterexamples

• Flea and Comb (differentiates connected and path connected)

• Comb (sans the flea) (differentiates path connected and locally path connected)

• Topologist’s sine curve (differentiates connected and path connected)

• 2 or 3 point sets (especially useful if you assume your space must be compact)

• Any space with the discrete topology

• Any space with the indiscrete topology