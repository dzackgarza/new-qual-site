## Topology Qual Workshop Day 4: Counterexamples

## Warm-up Problems:

For a set $A \subset X , { \overline { { A } } }$ is defined to be the intersection of all closed sets containing A. Using this definition, show: $x \in { \overline { { A } } }$ if and only if every open set U containing x intersects A.

Let $f : X \to Y$ be a continuous, bijective, open map.
Show that f is a homeomorphism.
[Open map can be replaced with closed map and the same result holds.]

• Provide an example of a topological space where open sets are compact.
Then find an infinite set with a Hausdorff topology where open sets are compact.

(1) (June $\mathrm { \ ' 0 9 \# 2 A ) }$ For a topological space X and $y \in X$ , the path component $P _ { y }$ of X containing y is the largest path-connected subset with $y \in P _ { y } \subseteq X$

(a) Show that this concept is well defined (that is, show that every point y is contained in a largest path-connected subset).

(b) Give an example of a space and a point $y \in X$ so that $P _ { y }$ is neither an open nor a closed subset of X.

(2) (June ’08 # A1) Let A be a subset of a topological space X, and let B be a subset of a topological space Y . Let $X \times Y$ be the product space, and let intZ (C) denote the interior of the set C in the space Z. Prove or give a counterexample to int $x \times Y ( A \times B ) = \operatorname* { i n t } _ { X } ( A ) \times \operatorname* { i n t } _ { Y } ( B )$

(3) (Jan ’04 # A3) Let $( X , \tau )$ be a Hausdorff space and let $\tau ^ { \prime } = \{ U \subseteq X : X \backslash U \subseteq X$ is $\mathrm { c o m p a c t } \} \cup \{ \emptyset \}$ Show that $\tau ^ { \prime }$ is a topology on X and is coarser than τ . Show that, in general, they need not be equal.

(4) Let X be a compact space.
If $X = A \cup B$ with both A and B Hausdorff, must X be Hausdorff?

Tips: The following are common places to look for counterexamples:

• Flea and Comb (Differentiates Connected and Path Connected)

• Comb (Sans the flea) (Differentiates Path Connected and Locally Path Connected)

• Topologists Sine Curve (Differentiates Connected and Path Connected)

• 2 or 3 point sets (Especially useful if you assume your space must be compact)

• Any space with the Discrete Topology

• Any space with the Indiscrete Topology

(1) (June ’10 # A1) Let X be a topological space and let $f , g : X \to$ R be continuous functions.

(a) Show that the set $L = \{ p \in X : f ( p ) \leq g ( p ) \}$ is a closed subset of X.

(b) Show that the function $h : X \to \mathbb { R }$ given by $h = \operatorname* { m i n } \{ f ( p ) , g ( p ) \}$ is continuous.

(2) (June ${ } ^ { \ ' } 0 8 \notin \mathrm { A 3 } )$

(a) Prove that a map $f : X \to Y$ between topological spaces is continuous if and only if $f ( { \overline { { A } } } ) \subseteq$ $\overline { { f ( A ) } }$ for all $A \subseteq X$

(b) Prove that if f is continuous and $f ( { \overline { { A } } } )$ closed for some $A \subseteq X$ , then $f ( { \overline { { A } } } ) = { \overline { { f ( A ) } } }$

(3) (Jan $^ { \prime } 0 8 \ \# \ \mathrm { \bf ~ B 8 } )$ Suppose that X is an arbitrary topological space and Y is a compact space.
Consider the projection map $\pi : X \times Y \to X$ defined by $\pi ( x , y ) = x .$ . Prove that if $X \times Y$ has the product topology, then π is a closed map.

(4) $( \mathrm { J u n e } ~ ^ { \prime } 0 4 \# \mathrm { A } 2 )$ Let X be the unit sphere in $\mathbb { R } ^ { 3 }$ and define an equivalence relation on X by

$$
( x , y , z ) \sim ( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } ) \Leftrightarrow z = z ^ { \prime }
$$

Let $Z = X / \sim$ be the quotient space under this equivalence relation, with the quotient topology.\
Show that Z is homeomorphic to the interval [−1, 1].
