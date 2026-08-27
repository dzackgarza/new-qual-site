1. Let $f \colon X \to Y$ be a continuous surjection, and suppose f is a closed map. Let $g \colon Y \to Z$ be a function so that $g \circ f \colon X \to Z$ is continuous. Show that g is continuous.

Proof. It is enough to show: For every closed subset $F \subset Z$ , the subset $g ^ { - 1 } ( F ) \subset$ Y is closed.

Now, by continuity of $g \circ f$ , we know that $( g \circ f ) ^ { - 1 } ( F ) = f ^ { - 1 } ( g ^ { - 1 } ( F ) )$ is a closed subset of X. Since f is a closed map, it takes this closed subset of X to a closed subset of Y . But

$$
f ( ( g \circ f ) ^ { - 1 } ( F ) ) = f ( f ^ { - 1 } ( g ^ { - 1 } ( F ) ) ) = g ^ { - 1 } ( F ) ,
$$

since f is surjective. Hence, $g ^ { - 1 } ( F )$ is closed.

2. Let X be a space. Show that X is Hausdorff if, and only if, the diagonal $\Delta : =$ $\{ ( x , x ) \mid x \in X \}$ is a closed subspace of $X \times X$

Proof. Suppose X is a Hausdorff space. We need to show that the complement of the diagonal, $\Delta ^ { \mathrm { { c } } } : = X \times X \setminus \Delta$ , is open. So let $( x , y ) \in \Delta ^ { \mathrm { c } }$ . Then $x \neq y ,$ and so there are disjoint open sets U and $V$ , containing x and y, respectively. By definition of the product topology, $U \times V$ is an open subset of $X \times X$ , and clearly $U \times V \subset \Delta ^ { \mathrm { { c } } }$ (for otherwise $U \cap V \neq \emptyset )$ . This shows that $\Delta ^ { \mathrm { c } }$ is open.

Conversely, suppose $\Delta$ is closed, that is to say, $\Delta ^ { \mathrm { c } }$ is open. Let x and y be two distinct elements of X. Then $( x , y ) \in \Delta ^ { \mathrm { c } }$ , and so there is a basis open set $U \times V \subset \Delta ^ { \mathrm { { c } } }$ containing $( x , y )$ . Now note that U and V are open, disjoint subsets of X, containing x and y, respectively. This shows that X is Hausdorff. 

3. Let $X = [ 0 , 1 ] / ( \frac { 1 } { 4 } , \frac { 3 } { 4 } )$ be the quotient space of the unit interval, where the open interval $\left( \textstyle { \frac { 1 } { 4 } } , \frac { 3 } { 4 } \right)$ is identified to a single point. Show that X is not a Hausdorff space.

Proof. Recall that in a quotient space $X / A = ( X \setminus A ) \coprod [ \{ * \}$ , the open sets are of one of two types:

(1) either an open set in $X \setminus A ;$ ; or

(2) of the form $\{ * \} \cup ( W \cap ( X \setminus A ) )$ , where W is an open set in X, containing A. In our situation, $X = \left\lceil 0 , 1 \right\rceil$ and $\begin{array} { r } { A = \left( \frac { 1 } { 4 } , \frac { 3 } { 4 } \right) } \end{array}$ . Take $\textstyle x = { \frac { 1 } { 4 } }$ and $\begin{array} { r } { y = \frac { 3 } { 4 } } \end{array}$ , viewed as elements of $X / A$ Suppose U and and V are open, disjoint subsets of $X / A _ { ; }$ containing x and y, respectively. Then, necessarily, both U and V must be of type (2), since an open subset of [0, 1] containing one of the endpoints of the interval $\textstyle { \left( { \frac { 1 } { 4 } } , { \frac { 3 } { 4 } } \right) }$ must intersect that interval. But then both U and V must contain the element $\{ * \}$ , and thus cannot be disjoint—a contradiction. 

4. Let X be a Hausdorff space. Suppose A is a compact subspace, and $x \in X \setminus A$ Show that there exist disjoint open sets U and V containing A and x, respectively.

Proof. Let $y \in A$ . Since $x \in X \setminus A$ , we see that $y \neq x .$ . Since X is Hausdorff, there are open, disjoint sets $U _ { y }$ and $V _ { y }$ containing y and x, respectively.

Now note that $\{ U _ { y } \} _ { y \in A }$ is an open cover of A. Since A is compact, this cover admits a finite subcover, say, $U _ { y _ { 1 } } , \ldots , U _ { y _ { n } }$ . Define:

$$
U : = \bigcup _ { i = 1 } ^ { n } U _ { y _ { i } } \quad { \mathrm { a n d } } \quad V : = \bigcap _ { i = 1 } ^ { n } V _ { y _ { i } } .
$$

It is readily seen that U and V are the desired open sets.

5. Let $p \colon X \to Y$ be a quotient map. Suppose Y is connected, and, for each $y \in Y$ the subspace $p ^ { - 1 } ( \{ y \} )$ is connected. Show that X is connected.

Proof. Suppose X is disconnected, that is, there are disjoint, open, non-empty sets U and V such that $X = U \cup V$

Consider the subsets $p ( U )$ and $p ( V )$ of Y : they are both open (since U and V are open, and p is a quotient map), and non-empty (since U and V are non-empty). Thus, by the connectivity of $Y .$ , the sets $p ( U )$ and $p ( V )$ cannot be disjoint.

So let $y \in p ( U ) \cap p ( V )$ . We then have

$$
p ^ { - 1 } ( \{ y \} ) = \left( U \cap p ^ { - 1 } ( \{ y \} ) \right) \cup \left( V \cap p ^ { - 1 } ( \{ y \} ) \right) .
$$

Both sets on the right side are open subsets of $p ^ { - 1 } ( \{ y \} )$ (by definition of the subspace topology), and both are non-empty (since $y \in p ( U )$ means $y = p ( x )$ , for some $x \in U$ , and so $x \in U \cap p ^ { - 1 } ( \{ y \} )$ , and similarly for the other subset). Thus, by the connectivity of $p ^ { - 1 } ( \{ y \} )$ , these sets $U \cap p ^ { - 1 } ( \{ y \} )$ ) and $V \cap p ^ { - 1 } ( \{ y \} )$ cannot be disjoint. This means there is a $z \in U \cap V \cap p ^ { - 1 } ( \{ y \} )$ . Consequently, $U \cap V \neq \emptyset .$ a contradiction. 

6. Let X be a discrete topological space, and let ∼ be an equivalence relation on X. Prove that $X / \sim _ { ; }$ endowed with the quotient topology, is also a discrete space.

Proof. Let p : $X  X / \sim$ be the quotient map. By definition of quotient topology, a subset U of $X / \sim$ is open if and only if $p ^ { - 1 } ( U )$ is an open subset of X. But every subset of X is open (since X has the discrete topology). Hence, every subset of $X / \sim$ is open; that is to say, $X / \sim$ is discrete. 