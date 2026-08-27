## Homework 3

1. (Page 37 of B&T) Let $S ^ { n } ( r )$ be the sphere of radius r in $\mathbb { R } ^ { n + 1 }$ . Let

$$
\omega = { \frac { 1 } { r } } \sum _ { i = 1 } ^ { n + 1 } ( - 1 ) ^ { i - 1 } x _ { i } d x _ { 1 } \cdot \cdot \cdot \widehat { d x _ { i } } \cdot \cdot \cdot d x _ { n + 1 }
$$

be an n-form. (The hat denotes omission, i.e. $d x _ { 1 } \widehat { d x _ { 2 } } d x _ { 3 } = d x _ { 1 } d x _ { 3 } . )$

(a) Compute $\int _ { S ^ { n } ( 1 ) } \omega .$ . (There might be a clever way to do this but at some point you have to really compute an integral.) Use your computation to conclude that ω is not an exact form.

(b) Think of r the radius function on $\mathbb { R } ^ { n + 1 } \backslash \{ 0 \}$ . Show that dr $\wedge \omega = d x _ { 1 } \ldots d x _ { n } .$

(c) B&T claim that your answer to the first part gives you a generator of $H ^ { 2 } ( S ^ { 2 } )$ Explain why and give a formula for the generator of $H ^ { n } ( S ^ { n } )$

2. (Page 38 of B&T) Show that the map $\pi _ { * }$ in the proof of the Poincarelemma is a \` chain map.

3. Compute the cohomology groups (regular and compactly supported) of the cylinder $S ^ { 1 } \times \mathbb { R }$ and the open Mobius strip, i.e. the twisted $S ^ { 1 } \times \mathbb { R }$ . Do not use a Kunneth formula. ¨

4. Let $f \colon  { \mathbb { R } } ^ { m } \to  { \mathbb { R } } ^ { m }$ be a proper map. In class showed that $\begin{array} { r } { \deg ( f ) = \sum _ { p \in f ^ { - 1 } ( q ) } \pm 1 } \end{array}$ where the signs depend on $p .$ .

(a) Show that if $f \simeq g$ then $\deg ( f ) = \deg ( g )$ using differential forms.

(b) The degree of f mod two is $\deg ( f )$ mod 2. Give another proof that the degree mod two is homotopy invariant as follows. Let $F$ be a homotopy between $f$ and g. Consider the restriction of $F$ to $\mathbb { R } ^ { m } \times [ 0 , 1 ]$ . Study $F ^ { - 1 } ( q )$ . (To get started: what sort of space is $F ^ { - 1 } ( q ) \cap \mathbb { R } ^ { m } \times \{ t \}$ for $t \in [ 0 , 1 ] \colon )$

## 5. Degree examples:

(a) The unit circle in C is the set $\| z \| = 1$ . The map $z \mapsto z ^ { k }$ for $k \in \mathbb N$ induces a smooth map $S ^ { 1 } \to S ^ { 1 }$ . Compute the degree of this map.

(b) A complex polynomial $p ( z )$ induces a smooth map $\mathbb { C } \to \mathbb { C }$ . Show that the degree of this map is the degree of the polynomial.

(c) (The linking number) Let M and N be disjoint manifolds in $\mathbb { R } ^ { r + 1 }$ . (We haven’t talked much about embedded manifolds. You can take M to be a subspace of $\mathbb { R } ^ { r + 1 }$ so that each $p \in M$ has a neighborhood U so that $U \cap M$ is diffeomorphic to $\mathbb { R } ^ { m } . )$ Define

$$
\lambda \colon M \times N  \mathbb { R } ^ { r + 1 }
$$

by

$$
\lambda ( x , y ) = { \frac { x - y } { \| x - y \| } } .
$$

Verify that $\lambda ( x , y )$ lands in the unit sphere in $\mathbb { R } ^ { r + 1 }$ for any x and $y .$ . Show that $\lambda ( x , y ) = - \lambda ( y , x )$

6. Let M be a connected manifold of dimension n. A smooth curve in M is a smooth map $[ 0 , 1 ]  M$ A smooth loop in M is a smooth map $\gamma \colon [ 0 , 1 ] \ \to \ M$ so that $\gamma ( 0 ) = \gamma ( 1 )$ . (Of course this is equivalent to a smooth map $S ^ { 1 } \to M . )$

Show that if M is simply-connected then $H ^ { 1 } ( M ) = 0$