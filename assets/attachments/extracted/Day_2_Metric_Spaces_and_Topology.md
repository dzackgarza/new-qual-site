## Day 2: Metric spaces and topology

Definition. A set E is countable if a bijective function f : E → N exists.

## Proposition 1.1.

i) If a surjective function $g : E \to F$ exists and E is countable, then F is countable.

ii) If an injective function $h : E \to F$ exists and F is countable, then E is countable.

iii) If each $E _ { j }$ is countable for $j = 1 , 2 , . . . ,$ then $\textstyle \bigcup _ { j = 1 } ^ { \infty } E _ { j }$ is countable.

Definition. A metric space is a pair $( X , d )$ consisting of a set X along with a function d : $X \times X \to$ R such that for any $p , q \in X$

i) $d ( p , q ) > 0 { \mathrm { ~ i f ~ } } p \neq q ; d ( p , p ) = 0$

ii) $d ( p , q ) = d ( q , p )$

iii) $d ( p , q ) \leq d ( p , r ) + d ( r , q )$ for any $r \in X$

The metric d gives rise to a topology on X with basis given by the neighborhoods

$$
N _ { r } ( p ) = \{ x \in X : d ( x , p ) < r \} .
$$

A set $G \subset X$ is open this topology if every point in G is an interior point. A metric space is called separable if it contains a countable dense subset.

Definition. A normed space $( X , | | \cdot | | )$ is a vector space X over a field F (nearly always R or C) along with a norm $\vert \vert \cdot \vert \vert : X \to \mathbb { R }$ such that for all $x , y \in X$ ,

i) $\| x \| > 0 { \mathrm { ~ i f ~ } } x \neq 0 , \| 0 \| = 0 .$

ii) $\| \alpha x \| = | \alpha | \| x \| { \mathrm { ~ f o r ~ } } \alpha \in \mathbb { F } .$

iii) $| | x + y | | \leq | | x | | + | | y | | .$

Every normed space $( X , | | \cdot | | )$ is a metric space by taking $d ( x , y ) = | | x - y | |$ . The converse is not true in general—even if X is a vector space.

Definition. An inner product space is a vector space X over a field $\mathbb { F } = \mathbb { R } { \mathrm { ~ o r ~ } } \mathbb { C }$ along with an inner product $\langle \cdot , \cdot \rangle : X \times X \to \mathbb { F }$ such that for all $x , y , z \in X$

i) $\langle x , y \rangle = { \overline { { \langle y , x \rangle } } } .$

ii) $\langle \alpha x + y , z \rangle = \alpha \langle x , z \rangle + \langle y , z \rangle .$

iii) $\langle x , x \rangle \geq 0 .$ and if $\langle x , x \rangle = 0$ then x = 0.

Every inner product space is a normed space via the induced norm $\vert \vert x \vert \vert : = { \sqrt { \langle x , x \rangle } }$

Theorem 1.2 (Heine-Borel / Rud76, Thm. 2.41). If $E \subset \mathbb { R } ^ { n }$ has any one of these properties, then it has the other two:

i) E is closed and bounded.

ii) E is compact.

iii) Every infinite subset of E has a limit point in E.

Note that the assumption that E is a subset of Rn (with the usual topology) is essential.

Theorem 1.3 (Weierstrass / Rud76, Thm. 2.42). Every bounded infinite subset of Rn has a limit point $i n \mathbb { R } ^ { n }$

Proposition 1.4. Every open set $G \subset \mathbb { R }$ can be written as a finite or countable union of disjoint open intervals $( a _ { j } , b _ { j } )$ with at most one $a _ { j } = - \infty$ and at most one $b _ { j } = \infty$

Definition. A metric space $( X , d )$ is connected if whenever $U , V \subseteq X$ are open and satisfy $U \cap V = \emptyset$ and $U \cup V = X$ , then either $U = \emptyset$ or $V = \emptyset$

Warm-up problems. Throughout, X is a metric space.

1) State the definition of what it means for a set $K \subset X$ to be compact, including the definition of open cover.

2) (June 2010 #2b) Prove that $\{ 1 / n : n \in \mathbb { Z } \backslash \{ 0 \} \} \cup \{ 0 \}$ is compact using the above definition.

3) Is the set of all sequences $x _ { 1 } , x _ { 2 } , \ldots$ . with $x _ { i } \in \{ 0 , 1 \}$ for $i = 1 , 2 , . . .$ . countable?

4) Show that an inner product space satisfies the parallelogram law with its induced norm:

$$
| | x + y | | ^ { 2 } + | | x - y | | ^ { 2 } = 2 | | x | | ^ { 2 } + 2 | | y | | ^ { 2 } .
$$

(For simplicity, you may assume that this is an inner product space over R.)

5) (January 2010 #1a partial) Determine whether or not the sets $\{ ( x , y ) \in \mathbb { R } ^ { 2 } : x + y < 3 \}$ and $\{ f \in C ( [ - 1 , 1 ] ) : f ( 0 ) = 0 \}$ are open, closed, or compact, where $C ( [ - 1 , 1 ] )$ is considered with $\| \cdot \| _ { \infty }$

## Problems.

6) (May 2019, #1) Let $( M , d _ { M } ) , ( N , d _ { N } )$ be metric spaces. Define $d _ { M \times N } \colon ( M \times N ) \times ( M \times N ) \to$ R by

$$
d _ { M \times N } \big ( ( x _ { 1 } , y _ { 1 } ) , ( x _ { 2 } , y _ { 2 } ) \big ) : = d _ { M } ( x _ { 1 } , x _ { 2 } ) + d _ { N } ( y _ { 1 } , y _ { 2 } ) .
$$

1) Prove that $( M \times N , d _ { M \times N } )$ is a metric space.

2) Let $S \subseteq M$ and $T \subseteq N$ be compact sets in $( M , d _ { M } )$ and $( N , d _ { N } )$ , respectively. Prove that $S \times T$ is a compact set in $( M \times N , d _ { M \times n } )$

7) (June 2003, #1b,c) (b) Show by example that the union of infinitely many compact subsets of a metric space need not be compact. (c) If $( X , d )$ is a metric space and $K \subset X$ is compact, define $d ( x _ { 0 } , K ) = \operatorname* { i n f } _ { y \in K } d ( x _ { 0 } , y )$ . Prove that there exists a point $y _ { 0 } \in K$ such that $d ( x _ { 0 } , K ) = d ( x _ { 0 } , y _ { 0 } )$

8) (January 2009, #4a) Consider the metric space $( \mathbb { Q } , d )$ where Q denotes the rational numbers and $d ( x , y ) = | x - y |$ |. Let $E = \left\{ x \in \mathbb { Q } : x > 0 , 2 < x ^ { 2 } < 3 \right\}$ . Is E closed and bounded in $\mathbb { Q } ?$ Is E compact in Q?

9) (January 2011 $\# 3 \mathrm { a } )$ Let $( X , d )$ be a metric space, $K \subset X$ be compact, and $F \subset X$ be closed. If $K \cap F = \emptyset$ , prove that there exists an $\epsilon > 0$ so that $d ( k , f ) \geq \epsilon$ for all $k \in K$ and $f \in F .$

10) Let $( X , d )$ be an unbounded and connected metric space. Prove that for each $x _ { 0 } \in X$ , the set $\{ x \in X : d ( x , x _ { 0 } ) = r \}$ is nonempty.

## Additional Problems.

11) Show that if $f : \mathbb { R } \to \mathbb { R }$ is monotone increasing, then f has at most a countable set of jump discontinuities.

12) Prove Proposition 1.4.

13) Verify the remark following the definition of normed space.