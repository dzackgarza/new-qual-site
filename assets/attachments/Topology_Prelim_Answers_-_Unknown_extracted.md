Topology Prelim Answers

William Malone and Matt Housley

Summer 2007

## Chapter 1

## 6520 Final Exam 2007

1. Let $X = \mathbb { R } P ^ { 2 } \vee \mathbb { R } P ^ { 2 }$ . Give an example of an irregular covering space ${ \tilde { X } }  X$

<!-- image-->

Let me rst describe the above picture. Everything that looks like a sphere is a sphere and the half-sphere is supposed to represent a copy of $\mathbb { R } P ^ { 2 }$ . And the identications as either A or B are supposed to represent which $\mathbb { R } P ^ { 2 }$ a given sphere or the $\mathbb { R } P ^ { 2 }$ is being mapped onto by the projection map. So we have an innite wedge of spheres and exactly one copy of $\mathbb { R } P ^ { 2 }$ The above picture is a covering space of $\mathbb { R } P ^ { 2 } \vee \mathbb { R } P ^ { 2 }$ and $\pi _ { 1 } ( \tilde { X } ) = \mathbb { Z } _ { 2 }$ with the generator being B and more importantly $H = p _ { * } ( \pi _ { 1 } ( { \tilde { X } } ) ) = < B | B ^ { 2 } >$ Now this is not a normal subgroup of $\pi _ { 1 } ( \mathbb { R } P ^ { 2 } \lor \mathbb { R } P ^ { 2 } ) = < A , B | A ^ { 2 } , B ^ { 2 } >$ since the element aba which is a conjugate of the element b is not contained in H. And since it is not a normal subgroup the covering space is an irregular covering space by Proposition 1.39 in Hatcher.

2. Compute the fundamental group of the space X obtained from the disjoint union of two 2-tori by identifying them along a pair of points.

<!-- image-->

It is obvious that the rst picture is homotopy equivalent to X where the homotopy could be thought of as collapsing the lines in the rst picture. Then after the pictured homotopy equivalence we see that X is homotopy equivalent to $T ^ { 2 } \vee T ^ { 2 } \vee S ^ { 1 }$ . Now using the corollary of Van Kampen's theorem that states $\pi _ { 1 } ( \vee _ { \alpha } X _ { \alpha } ) = * _ { \alpha } \pi _ { 1 } ( X _ { \alpha } )$ we see that $\pi _ { 1 } ( X ) = \mathbb { Z } ^ { 2 } * \mathbb { Z } ^ { 2 } * \mathbb { Z }$ since $\pi _ { 1 } ( T ^ { 2 } ) = \mathbb { Z } ^ { 2 }$ and $\pi _ { 1 } ( S ^ { 1 } ) = \mathbb { Z }$

3. Let S be an embedded circle in $\mathbb { R } P ^ { 2 }$ which is not nullhomotopic (up to isotopy there is only one) and let X be obtained by taking two copies of $\mathbb { R } P ^ { 2 }$ and identifying them along S. Construct an explicit $\Delta \cdot$ -complex structure on X and use it to compute homology and cohomology of X with coecients in Z and $\mathbb { Z } _ { 2 }$

<!-- image-->

<!-- image-->

The above $\Delta \cdot$ -complex is a $\Delta \cdot$ -complex structure on X since the not null-homotopic curve in any R $P ^ { 2 }$ is given by a simple path connecting antipotal points. In X we are connecting the antipotal points V . Now from this -complex structure we see that we have 3 vertices, 5 edges, and 4 faces. Thus the chain complex for X has the following form for an arbitrary group G.

$$
0 \to G ^ { 4 } { \overset { \partial _ { 1 } } { \to } } G ^ { 5 } { \overset { \partial _ { 2 } } { \to } } G ^ { 3 } \to 0
$$

Now computing the boundary of edges and faces we get

$$
\partial _ { 1 } ( L ) = A - B + C
$$

$$
\partial _ { 1 } ( U ) = - A + B + C
$$

$$
\partial _ { 1 } ( R ) = C - D + E
$$

$$
\partial _ { 1 } ( Z ) = C + D - E
$$

$$
\begin{array} { r l } & { \partial _ { 2 } ( A ) = W - V } \\ & { \partial _ { 2 } ( B ) = W - V } \\ & { \partial _ { 2 } ( C ) = V - V = 0 } \\ & { \partial _ { 2 } ( D ) = P - V } \\ & { \partial _ { 2 } ( E ) = P - V } \end{array}
$$

$$
\partial _ { 1 } = { \left[ \begin{array} { l l l l } { 1 } & { - 1 } & { 0 } & { 0 } \\ { - 1 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { 1 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { - 1 } & { 1 } \\ { 0 } & { 0 } & { 1 } & { - 1 } \end{array} \right] } \quad \partial _ { 2 } = { \left[ \begin{array} { l l l l } { 1 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { - 1 } & { - 1 } & { 0 } & { - 1 } & { - 1 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 1 } \end{array} \right] }
$$

Now by aecting a change of basis we see that

$$
\partial _ { 1 } = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] } \ a n d \ \partial _ { 2 } = { \left[ \begin{array} { l l l l l } { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] }
$$

Now we can compute the homology with both Z and $\mathbb { Z } _ { 2 }$ coecients.

$$
\begin{array} { r l r } { F o r \ \mathbb { Z } _ { 2 } } & { H _ { 0 } ( X ) = \mathbb { Z } _ { 2 } } & { F o r \ \mathbb { Z } } & { H _ { 0 } ( X ) = \mathbb { Z } } \\ & { H _ { 1 } ( X ) = \mathbb { Z } _ { 2 } } & { H _ { 1 } ( X ) = \mathbb { Z } _ { 2 } } \\ & { H _ { 2 } ( X ) = \mathbb { Z } _ { 2 } ^ { 2 } } & { H _ { 2 } ( X ) = \mathbb { Z } } \end{array}
$$

Now we can also form the cochain complex by letting $\delta _ { 1 } = \partial _ { 1 } ^ { T }$ and $\delta _ { 2 } = \partial _ { 2 } ^ { T }$ and we get:

$$
0 \to G ^ { 3 } { \overset { \delta _ { 2 } } { \to } } G ^ { 5 } { \overset { \delta _ { 1 } } { \to } } G ^ { 4 } \to 0
$$

Now we can compute the cohomology with Z and $\mathbb { Z } _ { 2 }$ coecients.

$$
\begin{array} { r l r l } { F o r \mathbb { Z } _ { 2 } } & { H ^ { 0 } ( X ) = \mathbb { Z } _ { 2 } } & { F o r \mathbb { Z } } & { H ^ { 0 } ( X ) = \mathbb { Z } } \\ & { H ^ { 1 } ( X ) = \mathbb { Z } _ { 2 } } & & { H ^ { 1 } ( X ) = 0 } \\ & { H ^ { 2 } ( X ) = \mathbb { Z } _ { 2 } ^ { 2 } } & & { H ^ { 2 } ( X ) = \mathbb { Z } \oplus \mathbb { Z } _ { 2 } } \end{array}
$$

## 4. Give a denition of the Hopf map and verify that it is a ber bundle.

Dene the Hopf map $\begin{array} { r } { H : S ^ { 3 }  S ^ { 2 } \mathrm { ~ b y ~ } ( Z , W ) \mapsto \frac { Z } { W } \in \mathbb { C } \cup \{ \infty \} } \end{array}$ . Now it is easy to see what the ber's are since we can consider $S ^ { 3 }$ to be the unit sphere in $\mathbb { C } ^ { 2 }$

$$
H ^ { - 1 } ( p ) = ( z , w ) \ s u c h \ t h a t \ \frac { z } { w } = p \Rightarrow z = p w \Rightarrow | p w | ^ { 2 } + | w | ^ { 2 } = 1 \Rightarrow | w | ^ { 2 } = \frac { 1 } { | p | ^ { 2 } + 1 }
$$

$$
\Rightarrow H ^ { - 1 } ( p ) = S ^ { 1 }
$$

Now we need to check the local trivialization condition. Let $U _ { 1 } = \mathbb { C }$ and $U _ { 2 } = $ $\{ \mathbb { C } - \{ 0 \} \} \cup \{ \infty \}$ . Dene $\begin{array} { r } { m _ { 1 } : H ^ { - 1 } ( U _ { 1 } ) \to U _ { 1 } \times S ^ { 1 } \mathrm { ~ b y ~ } ( z , w ) \mapsto ( \frac { z } { w } , \frac { w } { | w | } ) } \end{array}$ and $m _ { 2 } :$ $\begin{array} { r } { H ^ { - 1 } ( U _ { 2 } ) \to U _ { 1 } \times S ^ { 1 } \mathrm { ~ b y ~ } ( z , w ) \mapsto ( \frac { z } { w } , \frac { z } { | z | } ) } \end{array}$ . These maps take bers to bers and is a homeomorphism since the inverse of $m _ { 1 }$ is given by the map $\begin{array} { r } { \left( \frac { z } { w } , \lambda \right) \to \frac { \lambda | w | } { w } ( z , w ) } \end{array}$ and the inverse of $m _ { 2 }$ is given by the map $\begin{array} { r } { ( \frac { z } { w } , \lambda ) \to \frac { \lambda | z | } { z } ( z , w ) } \end{array}$ . Thus the Hopf map is a fiber bundle.

## 5. Let M be a closed connected 5-manifold and assume that $\pi _ { 1 } ( M ) = \mathbb { Z } _ { 3 }$ and $H _ { 2 } ( M , \mathbb { Z } ) = 0$ . Compute $H _ { i } ( M )$ for all i.

The rst thing that we notice is that since $\pi _ { 1 } ( M ) ~ = ~ \mathbb { Z } _ { 3 }$ (which has no index 2 subgroup) we know that M is orientable manifold by Propostion 3.25 in Hatcher. The second thing to notice is that $H _ { 1 } ( M , \mathbb { Z } ) = Z _ { 3 }$ since $H _ { 1 } ( M , \mathbb { Z } )$ is the abelianization of $\pi _ { 1 } ( M ) = \mathbb { Z } _ { 3 }$ which is already abelian. The third thing is for all $i > 5$ the homology groups $H _ { i } ( M , \mathbb { Z } ) = 0$ since i is bigger than the dimension of the manifold. Lastly we know that $H _ { 0 } ( M , \mathbb { Z } ) = \mathbb { Z }$ since M is connected.

Using the universal coecent theorem we get the following three split exact sequences.

$$
0 \to H ^ { 0 } ( M , \mathbb { Z } ) \to H o m ( H _ { 0 } ( M , \mathbb { Z } ) , \mathbb { Z } ) \to 0
$$

$$
0  E x t ( H _ { 0 } ( M , \mathbb { Z } ) , \mathbb { Z } )  H ^ { 1 } ( M , \mathbb { Z } )  H o m ( H _ { 1 } ( M , \mathbb { Z } ) , \mathbb { Z } )  0
$$

$$
0  E x t ( H _ { 1 } ( M , \mathbb { Z } ) , \mathbb { Z } )  H ^ { 2 } ( M , \mathbb { Z } )  H o m ( H _ { 2 } ( M , \mathbb { Z } ) , \mathbb { Z } )  0
$$

Now computing all these terms we get

$$
0 \to H ^ { 0 } ( M , \mathbb { Z } ) \to \mathbb { Z } \to 0
$$

$$
0  0  H ^ { 1 } ( M , \mathbb { Z } )  0  0
$$

$$
0 \to \mathbb { Z } _ { 3 } \to H ^ { 2 } ( M , \mathbb { Z } ) \to 0 \to 0 .
$$

This shows that $H ^ { 0 } ( M , \mathbb { Z } ) = \mathbb { Z } , H ^ { 1 } ( M , \mathbb { Z } ) = 0$ ,and $H ^ { 2 } ( M , \mathbb { Z } ) = \mathbb { Z } _ { 3 }$ . Now using Poincare duality $( H ^ { 5 - k } ( M , \mathbb { Z } ) = H _ { k } ( M , \mathbb { Z } ) )$ we see that $H _ { 5 } ( M , \mathbb { Z } ) = H ^ { 0 } ( M , \mathbb { Z } ) = \mathbb { Z }$ $H _ { 4 } ( M , \mathbb { Z } ) = H ^ { 1 } ( M , \mathbb { Z } ) = 0$ , and $H _ { 3 } ( M , \mathbb { Z } ) = H ^ { 2 } ( M , \mathbb { Z } ) = \mathbb { Z } _ { 3 }$

## 6. Let M be a connected orientable n-manifold which is not compact. Prove that $H _ { n } ( M , \mathbb { Z } ) = 0$

Let z represent a cycle in $H _ { n } ( M , \mathbb { Z } )$ which has a compact image in M. So let U be an open set containing the image of z which has compact closure such that $\overline { { U } } \subset M$ Let $V = M - { \overline { { U } } }$ . Now we are going to consider the long exact sequence of the triple $( M , U \cup V , V )$ in the following commutative diagram.

$$
\begin{array} { r l r } { H _ { n + 1 } ( M , U \cup V ; \mathbb { Z } ) \longrightarrow H _ { n } ( U \cup V , V ; \mathbb { Z } ) \longrightarrow H _ { n } ( M , V ; \mathbb { Z } ) } & { } & \\ { \overset { \mathrm { ~ } } { \cong } } & { \overset { \mathrm { ~ } } { \Big | } } & { } \\ { H _ { n } ( U ; \mathbb { Z } ) \longrightarrow } & { \ : H _ { n } ( M ; \mathbb { Z } ) \longrightarrow } & { \ : H _ { n } ( M ; \mathbb { Z } ) \ : } \end{array}
$$

Now the class $[ z ] \in H _ { n } ( M , \mathbb { Z } )$ defines a section $x \mapsto [ z ] _ { x }$ of the covering space $M _ { \mathbb { Z } }$ of M . Since M is connected, the section is determined by its value at a single point. Now since z has compact image and M is not compact the section must be zero on any point outside of $\bar { U }$ and thus $[ z ] _ { x } = 0$ . Now by lemma 3.27 we see that z represents 0 in $H _ { n } ( M , V ; \mathbb { Z } )$ and 0 in $H _ { n + 1 } ( M , U \cup V ; \mathbb { Z } )$ which follows since V and $U \cup V$ are complements of compact sets in M. Thus $H _ { n } ( U \cup V , V ; \mathbb { Z } ) = 0$ and $H _ { n } ( U ; \mathbb { Z } ) = 0$ by the isomorphism. Thus $z = 0$ in $H _ { n } ( M ; \mathbb { Z } )$ , and therefore $H _ { n } ( M , \mathbb { Z } ) = 0$ since z was an arbitrary element of the group.

(Alternate Proof ) Let $\sigma : { \mathcal { M } } \to \mathbb { Z }$ be a compactly supported 0-cocycle. Let $p \in C _ { 1 } ( M )$ be a path from a to b where a and b are points in M. Then,

$$
\delta \sigma ( p ) = \sigma ( \partial p ) = \sigma ( b ) - \sigma ( a ) = 0 .
$$

It follows that $\sigma$ is a constant function. But because $\sigma$ is compactly supported in a noncompact space, there exists $x \in M$ such that $\sigma ( x ) = 0$ . Hence, $\sigma = 0$ . It follows that $H _ { c } ^ { 0 } ( M ) \cong 0$ . Then, $H _ { n } ( M ) \cong 0$ by the general form of Poincare duality.

7. Show that $S L _ { n } ( \mathbb { R } )$ is connected and that $\pi _ { 1 } ( S L _ { n } ( \mathbb { R } ) )$ is cyclic for all $n \geq 2$ You don't have to provide a proof that ber bundles you use really are ber bundles.

The rst thing that we see is that $S L _ { n } ( \mathbb { R } )$ acts on $\mathbb { R } ^ { n } - \{ 0 \}$ by the map $h : S L _ { n } ( \mathbb { R } ) $ $\mathbb { R } ^ { n } - \{ 0 \}$ given by

$$
A  A [ \begin{array} { c } { 1 } \\ { 0 } \\ { \vdots } \\ { 0 } \end{array} ] f o r A \in S L _ { n } ( \mathbb { R } )
$$

Now to compute we need to compute the ber which is the stabilizer of the point

$$
\begin{array} { r } { \left[ \begin{array} { l } { 1 } \\ { 0 } \end{array} \right] } \\ { \vdots } \\ { 0 } \end{array}
$$

which is a matrix of the form

$$
[ \begin{array} { l l l } { \displaystyle \frac { 1 } { 0 } | a _ { 1 } } & { \cdots \cdot } & { a _ { n - 1 } } \\ { \vdots } & { \displaystyle S L _ { n - 1 } ( \mathbb { R } ) } \\ { 0 } \end{array} ] .
$$

We see that the above group of matrices is a product $S L _ { n - 1 } ( \mathbb { R } ) \times \mathbb { R } ^ { n - 1 }$ and thus we get a ber bundle of the form

$$
\mathbb { R } ^ { n - 1 } \hookrightarrow S L _ { n - 1 } ( \mathbb { R } ) \times \mathbb { R } ^ { n - 1 } \to S L _ { n - 1 } ( \mathbb { R } ) .
$$

Now since $\mathbb { R } ^ { n - 1 }$ has the same homotopy type as a point $\left( \mathrm { i e } \pi _ { m } ( \mathbb { R } ^ { n - 1 } ) \ = \ 0 \ \forall m \right)$ we see that in the long exact sequence of homotopy groups that $\pi _ { m } ( S L _ { n - 1 } ( \mathbb { R } ) ) \ \cong$ $\pi _ { m } ( S L _ { n - 1 } ( \mathbb { R } ) \times \mathbb { R } ^ { n - 1 } )$

Now returning to our original ber bundle

$$
S L _ { n - 1 } ( \mathbb { R } ) \times \mathbb { R } ^ { n - 1 } \hookrightarrow S L _ { n } ( \mathbb { R } ) \to \mathbb { R } ^ { n } - \{ 0 \}
$$

part of the long exact sequence of homotopy groups is

$$
\pi _ { 1 } ( \mathbb { R } ^ { n } - \{ 0 \} ) \to \pi _ { 0 } ( S L _ { n - 1 } ( \mathbb { R } ) \times \mathbb { R } ^ { n - 1 } ) \to \pi _ { 0 } ( S L _ { n } ( \mathbb { R } ) ) \to \pi _ { 0 } ( \mathbb { R } ^ { n } - \{ 0 \} ) .
$$

Which after using the isomorphism $\pi _ { n } ( S L _ { n - 1 } ( \mathbb { R } ) ) \cong \pi _ { n } ( S L _ { n - 1 } ( \mathbb { R } ) \times \mathbb { R } ^ { n - 1 } )$ and the facts that $\pi _ { 1 } ( \mathbb { R } ^ { n } - \{ 0 \} ) = 0$ since it deformation retracts onto $S ^ { 2 }$ and $\pi _ { 0 } ( \mathbb { R } ^ { n } - \{ 0 \} ) = 0$ since it is connected we get that

$$
0 \to \pi _ { 0 } ( S L _ { n - 1 } ( \mathbb { R } ) \to \pi _ { 0 } ( S L _ { n } ( \mathbb { R } ) \to 0
$$

and using induction we see that $\pi _ { 0 } ( { \cal S } L _ { n } ( \mathbb { R } ) \cong \pi _ { 0 } ( { \cal S } L _ { 1 } ( \mathbb { R } ) \cong \pi _ { 0 } [ 1 ] = 0$ . Hence $S L _ { n } ( \mathbb { R } )$ is connected.

Using another part of the long exact sequence namely

$$
\pi _ { 2 } ( \mathbb { R } ^ { n } - \{ 0 \} ) \to \pi _ { 1 } ( S L _ { n - 1 } ( \mathbb { R } ) \times \mathbb { R } ^ { n - 1 } ) \to \pi _ { 1 } ( S L _ { n } ( \mathbb { R } ) ) \to \pi _ { 1 } ( \mathbb { R } ^ { n } - \{ 0 \} )
$$

we see that when $n = 2$ we get

$$
\pi _ { 1 } ( S L _ { 1 } ( \mathbb { R } ) \times \mathbb { R } ^ { 1 } ) \to \pi _ { 1 } ( S L _ { 2 } ( \mathbb { R } ) ) \to \pi _ { 1 } ( \mathbb { R } ^ { 2 } - \{ 0 \} ) \to \pi _ { 0 } ( ( S L _ { 1 } ( \mathbb { R } ) \times \mathbb { R } ^ { 1 } ) ) .
$$

Now since $S L _ { 1 } ( \mathbb { R } ) = 1$ and $\pi _ { 1 } ( \mathbb { R } ^ { 2 } - \{ 0 \} ) = \mathbb { Z }$ since $\mathbb { R } ^ { 2 } - \{ 0 \}$ deformation retracts onto $S ^ { 1 }$ we get $0 \to \pi _ { 1 } ( S L _ { 2 } ( \mathbb { R } ) ) \to \mathbb { Z } \to 0$ which implies that $\pi _ { 1 } ( S L _ { 2 } ( \mathbb { R } ) ) = \mathbb { Z }$

When $n = 3$ we get

$$
\pi _ { 2 } ( \mathbb { R } ^ { 3 } - \{ 0 \} ) \to \pi _ { 1 } ( S L _ { 2 } ( \mathbb { R } ) \times \mathbb { R } ^ { 2 } ) \to \pi _ { 1 } ( S L _ { 3 } ( \mathbb { R } ) ) \to \pi _ { 1 } ( \mathbb { R } ^ { 3 } - \{ 0 \} ) .
$$

Since $\mathbb { R } ^ { 3 } - \{ 0 \}$ deformation retracts onto $S ^ { 2 }$ we see that $\pi _ { 1 } ( \mathbb { R } ^ { 3 } - \{ 0 \} ) = 0$ and $\pi _ { 2 } ( \mathbb { R } ^ { 3 } - \{ 0 \} ) = \mathbb { Z }$ . Now this tells us that the map $t : \pi _ { 1 } ( S L _ { 2 } ( \mathbb { R } ) \times \mathbb { R } ^ { 2 } ) \to \pi _ { 1 } ( S L _ { 3 } ( \mathbb { R } ) )$ is surjective. And since we know that $\pi _ { 1 } ( S L _ { 2 } ( \mathbb { R } ) \times \mathbb { R } ^ { 2 } ) \cong \pi _ { 1 } ( S L _ { 2 } ( \mathbb { R } ) = \mathbb { Z }$ we see that $\pi _ { 1 } ( S L _ { 3 } ( \mathbb { R } ) )$ is a quotient of Z and thus is cyclic.

Now for $n > 3$ we see that $\pi _ { 2 } ( \mathbb { R } ^ { n } - \{ 0 \} ) = 0 = \pi _ { 1 } ( \mathbb { R } ^ { n } - \{ 0 \} )$ and thus $\pi _ { 1 } ( S L _ { n } ( \mathbb { R } ) ) \cong$ $\pi _ { 1 } ( S L _ { n - 1 } ( \mathbb { R } ) ) \cong \pi _ { 1 } ( S L _ { 3 } ( \mathbb { R } ) )$ and thus $\pi _ { 1 } ( S L _ { n } ( \mathbb { R } ) )$ is cyclic for all $n \geq 2$

## 8. Prove that there is no map $f : \mathbb { C } P ^ { 2 } \to \mathbb { C } P ^ { 2 }$ of negative degree.

By definition the degree is defined to be the integer d such that $f _ { * } ( [ C P ^ { 2 } ] ) = d [ \mathbb { C } P ^ { 2 } ]$ where $\lbrack \mathbb { C } P ^ { 2 } ]$ is the fundamental class of $\mathbb { C } P ^ { 2 }$ . Now the cell structure on $\mathbb { C } P ^ { 2 }$ is given by $e _ { 0 } \cup e _ { 2 } \cup e _ { 4 }$ and thus the cup product structure on $\mathbb { C } P ^ { 2 }$ is given by $\mathbb { Z } [ \alpha ] / \alpha ^ { 3 }$ where α is two dimensional. Thus if such an f existed then $f ^ { * } ( \alpha ^ { 2 } ) = d \alpha ^ { 2 }$ since there is a natural isomorphism between $H ^ { 4 } ( \mathbb { C } P ^ { 2 } )$ and $H _ { 4 } ( \mathbb { C } P ^ { 2 } )$ given by the Universal Coefficient Theorem. But this map would send $\alpha  k \alpha$ and using the cup product structure $f ^ { * } ( \alpha ^ { 2 } ) = k ^ { 2 } \alpha ^ { 2 }$ and hence d would need to be a square in $\mathbb { Z } .$ . And if d is negative this cannot occur. Thus there are no maps of negative degree in this case.

## Chapter 2

## January 2007

1. Let $S ^ { n }$ be the unit sphere in $\mathbb { R } ^ { n + 1 }$ and $h : \mathbb { R } ^ { n + 1 }  \mathbb { R }$ the pro jection to the last coordinate. Prove that the restriction of h to $S ^ { n }$ is a Morse function and find all critical points and their indices.

First we need to chose charts and work in local coordinates. Let $U _ { i } ^ { + } = \{ ( x _ { 0 } , \ldots , x _ { n } ) | x _ { i } >$ 0g and $U _ { i } ^ { - } \ = \ \{ ( x _ { 0 } , \ldots , x _ { n } ) | x _ { i } \ < \ 0 \}$ let $\varphi _ { i } ^ { \pm } : \mathbb { R } ^ { n + 1 } \to \mathbb { R } ^ { n }$ given by $( x _ { 0 } , \ldots , x _ { n } ) $ $( x _ { 0 } , \ldots , { \hat { x } } _ { i } , \ldots , x _ { n } )$ be the chart map. Now if we look at the maps $P _ { i } ^ { \pm } = h \circ ( \varphi _ { i } ^ { \pm } ) ^ { - 1 }$ we get the map $( x _ { 0 } , . . . , x _ { n } )  x _ { n } { \mathrm { i f } } i \neq n$ in which case the partial derivatives $\begin{array} { r } { \frac { \partial { P _ { i } } } { \partial { x _ { j } } } = 0 } \end{array}$ $\mathrm { i f } \ j \neq n$ and $j \neq i$ , also $\begin{array} { r } { \frac { { \partial { P _ { i } ^ { \pm } } } } { { \partial { x _ { n } } } } = 1 } \end{array}$ . But this implies that we have no critical points in any chart except $U _ { n } ^ { \pm }$

In this case we see that $P _ { n } ^ { + } ( x _ { 0 } , \ldots , x _ { n - 1 } ) = { \sqrt { 1 - x _ { 0 } ^ { 2 } - x _ { 1 } ^ { 2 } - \cdots - x _ { n - 1 } ^ { 2 } } }$ . Now

$$
\frac { \partial P _ { n } ^ { + } } { \partial x _ { i } } = \frac { - x _ { i } } { \sqrt { 1 - x _ { 0 } ^ { 2 } - x _ { 1 } ^ { 2 } - \cdot \cdot \cdot - x _ { n - 1 } ^ { 2 } } }
$$

and thus the critical point is when all the $x _ { i } = 0$ ie at the point $( 0 , 0 , \ldots , 1 )$ . Also $P _ { n } ^ { - } ( x _ { 0 } , \ldots , x _ { n - 1 } ) = - { \sqrt { 1 - x _ { 0 } ^ { 2 } - x _ { 1 } ^ { 2 } - \cdots - x _ { n - 1 } ^ { 2 } } }$ thus

$$
{ \frac { \partial P _ { n } ^ { - } } { \partial x _ { i } } } = { \frac { x _ { i } } { \sqrt { 1 - x _ { 0 } ^ { 2 } - x _ { 1 } ^ { 2 } - \cdot \cdot \cdot - x _ { n - 1 } ^ { 2 } } } }
$$

and we see that another critical point is $( 0 , 0 , \ldots , - 1 )$ . Now we need to check that these critical points are nondegenerate.

$$
{ \frac { \partial ^ { 2 } P _ { n } ^ { + } } { \partial x _ { i } ^ { 2 } } } = { \frac { - { \sqrt { 1 - x _ { 0 } ^ { 2 } - x _ { 1 } ^ { 2 } - \cdot \cdot \cdot - x _ { n - 1 } ^ { 2 } } } - { \frac { x _ { i } ^ { 2 } } { \sqrt { 1 - x _ { 0 } ^ { 2 } - x _ { 1 } ^ { 2 } - \cdots - x _ { n - 1 } ^ { 2 } } } } } { 1 - x _ { 0 } ^ { 2 } - x _ { 1 } ^ { 2 } - \cdot \cdot \cdot - x _ { n - 1 } ^ { 2 } } }
$$

and

$$
{ \frac { \partial ^ { 2 } P _ { n } ^ { - } } { \partial x _ { i } ^ { 2 } } } = { \frac { \sqrt { 1 - x _ { 0 } ^ { 2 } - x _ { 1 } ^ { 2 } - \cdot \cdot \cdot - x _ { n - 1 } ^ { 2 } } + { \frac { x _ { i } ^ { 2 } } { \sqrt { 1 - x _ { 0 } ^ { 2 } - x _ { 1 } ^ { 2 } - \cdots - x _ { n - 1 } ^ { 2 } } } } } { 1 - x _ { 0 } ^ { 2 } - x _ { 1 } ^ { 2 } - \cdot \cdot \cdot - x _ { n - 1 } ^ { 2 } } }
$$

which equal  1 and 1 respectively when we evaluate each at its critical point. Also the mixed partials are

$$
\frac { \partial ^ { 2 } P _ { n } ^ { + } } { \partial x _ { i } \partial x _ { j } } = - \frac { x _ { i } x _ { j } } { 2 ( 1 - x _ { 0 } ^ { 2 } - x _ { 1 } ^ { 2 } - \cdot \cdot \cdot - x _ { n - 1 } ^ { 2 } ) ^ { \frac { 3 } { 2 } } }
$$

$$
{ \frac { \partial ^ { 2 } P _ { n } ^ { - } } { \partial x _ { i } \partial x _ { j } } } = { \frac { x _ { i } x _ { j } } { 2 ( 1 - x _ { 0 } ^ { 2 } - x _ { 1 } ^ { 2 } - \cdot \cdot \cdot - x _ { n - 1 } ^ { 2 } ) ^ { \frac { 3 } { 2 } } } }
$$

which take the value 0 when evaluated at the critical point. Thus the hessian matrix for the critical points in non-degenerate and hence our function h is a Morse function. Now in order to compute the index of the critical points we need to count the dimension of the negative eigenspace in the hessian matrix. For the critical point $( 0 , 0 , \ldots , - 1 )$ we see that all the numbers on the diagonal are 10s with zeros elsewhere so we get a Morse index of 0. For the critical point $( 0 , 0 , \ldots , 1 )$ we see that the only non-zero entries are on the diagonal and they are all 1 which gives us a Morse index of n.

## 2. Find a perturbation of the identity map $\mathbb { R } P ^ { 3 } \to \mathbb { R } P ^ { 3 }$ which is a Lefschetz map and compute its Lefschetz number.

For $\mathbb { R } \mathrm { { P } ^ { 3 } }$ , the identity map in projective coordinates is

$$
[ x : y : z : w ] \mapsto [ x : y : z : w ] .
$$

To make this a Lefschetz map, we will homotope it to the map

$$
[ x : y : z : w ] \mapsto [ x : 2 y : 3 z : 4 w ] .
$$

This map has four xed points: $[ 1 : 0 : 0 : 0 ] , [ 0 : 1 : 0 : 0 ] , [ 0 : 0 : 1 : 0 ]$ and $[ 0 : 0 : 0 : 1 ]$ We will show that these xed points have no +1 eigenvalues and compute the local Lefschetz index of each one.

Fix $x = 1$ . Then, our map becomes

$$
( y , z , w ) \mapsto ( 2 y , 3 z , 4 w ) .
$$

Clearly, this map has no +1 eigenvalues.

$$
d f - I = { \binom { 1 } { 0 } } \ 2 0 \atop 0  \ 3 \prime
$$

$$
L _ { [ 1 : 0 : 0 : 0 ] } ( f ) = 1 .
$$

Fix $y = 1$ . We have the local map

$$
( x , z , w ) \mapsto ( x / 2 , 3 z / 2 , 2 w ) .
$$

$$
d f - I = \left( \begin{array} { c c c } { { - \frac 1 2 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { \frac 1 2 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right) .
$$

$$
L _ { [ 0 : 1 : 0 : 0 ] } ( f ) = - 1 .
$$

Fix $z = 1$ . We have

$$
( x , y , w ) \mapsto ( x / 3 , 2 y / 3 , 4 w / 3 ) .
$$

$$
\begin{array} { c } { d f - I = \left( \begin{array} { c c c } { - \frac 2 3 } & { 0 } & { 0 } \\ { 0 } & { - \frac 1 3 } & { 0 } \\ { 0 } & { 0 } & { \frac 1 3 } \end{array} \right) . } \\ { L _ { [ 0 : 0 : 1 : 0 ] } = 1 . } \end{array}
$$

Fix $w = 1$

$$
( x , y , z ) \mapsto ( x / 4 , y / 2 , 3 z / 4 ) .
$$

$$
d f - I = \left( \begin{array} { c c c } { { - \frac { 3 } { 4 } } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { - \frac { 1 } { 2 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { - \frac { 1 } { 4 } } } \end{array} \right) .
$$

$$
L _ { [ 0 : 0 : 0 : 1 ] } ( f ) = - 1 .
$$

Hence, $L ( f ) = 0$

## 3. Give a proof that $\mathbb { R } P ^ { 2 }$ is non-orientable.

We can derive an orientation of $S ^ { 2 }$ from the standard orientation of $\mathbb { R } ^ { 3 }$ . When $S ^ { 2 }$ is embedded in $\mathbb { R } ^ { 3 }$ in the standard way, we have the inclusion map $i _ { * } : T _ { p } S ^ { 2 }  T _ { p } \mathbb { R } ^ { 3 }$ . Let $\mu$ be the standard (right hand) orientation of $\mathbb { R } ^ { 3 }$ . Formally, this is an equivalence class of ordered bases of $\mathbb { R } ^ { 3 }$ . Dene an orientation $\mu _ { T _ { p } S ^ { 2 } }$ of $S ^ { 2 }$ by saying that $( v _ { 0 } , v _ { 1 } ) \in \mu _ { T _ { p } S ^ { 2 } }$ if and only if $( i _ { * } ( v _ { 0 } ) , i _ { * } ( v _ { 1 } ) , p ) \in \mu$ . At each point $p \in S ^ { 2 }$ , we can pick a chart so that $\mu _ { T _ { p } S ^ { 2 } }$ lifts to an orientation of $\mathbb { R } ^ { 2 }$ , so this is a smooth orientation of $S ^ { 2 }$ . Now, observe that the antipodal map $p \mapsto - p$ reverses the orientation of $S ^ { 2 }$ : if $( v _ { 0 } , v _ { 1 } ) \in \mu _ { T _ { p } S ^ { 2 } }$ then $( - v _ { 0 } , - v _ { 1 } ) \ \in \ \mu _ { T _ { - p } S ^ { 2 } }$ Now, suppose that $\mathbb { R } \mathrm { P ^ { 2 } }$ is orientable. The projection map $P : S ^ { 2 }  \mathbb { R P } ^ { 2 }$ which identies point pairs $\{ p , - p \}$ is a local dieomorphism, so an orientation of $\mathbb { R } \mathrm { P ^ { 2 } }$ lifts by $P$ to an orientation of $S ^ { 2 }$ . Since the antipodal map $A : S ^ { 2 }  S ^ { 2 }$ is orientation reversing, lifting by $P \circ A$ would give the opposite orientation on $S ^ { 2 }$ . This is a contradiction since $P \circ A = P$

4. Compute de Rham cohomology of the 2   torus. You may use the Poincare lemma and the Mayer-Vietoris sequence. For example, you may want to compute $H ^ { * } ( S ^ { 1 } )$ rst.

5. Let $f : \mathbb { R } ^ { n }  \mathbb { R }$ be a smooth function. Show that for every $\epsilon > 0$ there is a $v \in \mathbb { R } ^ { n }$ with $| \boldsymbol { v } | < \epsilon$ such that the function $g _ { v } : \mathbb { R } ^ { n }  \mathbb { R }$ given by $g _ { v } ( x ) = f ( x ) + v \cdot x$ is Morse.

$\mathrm { S o }$ let $h : = \mathbb { R } ^ { n }  \mathbb { R } ^ { n }$ be given by $\begin{array} { r } { h ( x _ { 1 } , \ldots , x _ { n } ) = ( \frac { \partial f } { \partial x _ { 1 } } , \ldots , \frac { \partial f } { \partial x _ { n } } ) } \end{array}$ . Now the derivative of $g _ { v }$ at a point p is given by

$$
( d g _ { v } ) _ { p } = ( { \frac { \partial g _ { v } } { \partial x _ { 1 } } } , \ldots , { \frac { \partial g _ { v } } { \partial x _ { n } } } ) = h ( p ) + v .
$$

Now $p$ is a critical point of $g _ { v }$ if and only if $h ( p ) = - v$ . Also we see that $g _ { v }$ and $f$ have the same second partials and that the Hessian matrix of f at $p$ is exactly $( d h ) _ { p }$ If  v is a regular value for h then  v is a nondegenerate critical point of $g _ { v }$ since $( d h ) _ { p }$ is nonsingular. Thus if  v is a regular value of h then we have a Morse function since all critical points will be non-degenerate. Now by Sard we know that the set of regular values of h has full measure in $\mathbb { R } ^ { n }$ and hence in any  neighborhood of zero we can find $\mathrm { ~ a ~ } - v$ which is a regular value.

6. The set $S L _ { 2 } ( \mathbb { R } )$ of $2 \times 2$ matrices with determinant 1 can be viewed as a subset of $\mathbb { R } ^ { 4 }$ by choosing an ordering of entries. Show that this set is a submanifold of $\mathbb { R } ^ { 4 }$ and compute its tangent space at the identity matrix.

7. Consider the vector fields in $\mathbb { R } ^ { 3 }$ $\begin{array} { r } { X = x \frac { \partial } { \partial x } + \frac { \partial } { \partial y } } \end{array}$ and $\begin{array} { r } { Y = \frac { \partial } { \partial x } - \frac { \partial } { \partial z } } \end{array}$ Show that there is no non-empty surface $S \subset \mathbb { R } ^ { 3 }$ that is tangent to both vector elds at each of its points.

The rst thing that we need to do is compute $[ X , Y ] = X Y - Y X$

$$
= ( x { \frac { \partial } { \partial x } } + { \frac { \partial } { \partial y } } ) ( { \frac { \partial } { \partial x } } - { \frac { \partial } { \partial z } } ) - ( { \frac { \partial } { \partial x } } - { \frac { \partial } { \partial z } } ) ( x { \frac { \partial } { \partial x } } + { \frac { \partial } { \partial y } } )
$$

$$
= 0 - x { \frac { \partial ^ { 2 } } { \partial x \partial z } } + { \frac { \partial ^ { 2 } } { \partial x \partial y } } - { \frac { \partial ^ { 2 } } { \partial y \partial z } } - { \frac { \partial } { \partial x } } + 0 - { \frac { \partial ^ { 2 } } { \partial x \partial y } } + x { \frac { \partial ^ { 2 } } { \partial x \partial z } } + { \frac { \partial ^ { 2 } } { \partial y \partial z } } = - { \frac { \partial } { \partial x \partial z } }
$$

Now we notice that   $\textstyle { \frac { \partial } { \partial x } } \not \in S p a n \{ X , Y \}$ . Thus by the Frobenius Integrability Theorem there does not exist such a surface.

8. Show that for any two points $x , y \in \mathbb { R } ^ { n }$ that there is a compactly supported isotopy $\phi _ { t }$ (ie it is the identity outside a compact set) such that $\phi _ { 0 } = i d$ and $\phi _ { 1 } ( x ) = y$

9. Define a $\Delta { \bf - c o m p l e x }$ structure on the Klein bottle (K) and compute its homology with Z and $\mathbb { Z } _ { 2 }$ coefficients.

<!-- image-->

Now we see that the basis for the chain groups $\Delta _ { 2 } , \Delta _ { 1 } , \Delta _ { 0 }$ is given by the open simplices $\{ U , L \} , \{ a , b , c \}$ , and $\{ v \}$ respectively so we have the following chain complex

$$
0 \longrightarrow G ^ { 2 } \stackrel { \partial } { \longrightarrow } G ^ { 3 } \stackrel { 0 } { \longrightarrow } G \longrightarrow 0
$$

where the map $\partial = { \left[ \begin{array} { l l l } { 1 } & { 1 } & { - 1 } \\ { - 1 } & { 1 } & { 1 } \end{array} \right] } = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 0 } \end{array} \right] }$ . Now we see that $K e r \partial = 0$ if $G = \mathbb { Z }$ and $K e r { \partial } = \mathbb { Z } _ { 2 } ^ { \mathbf { \underline { { \omega } } } }$ if $G = \mathbb { Z } _ { 2 }$ . In addition $I m { \stackrel {  } { \partial \mathbf { \tau } } } = \mathbb { Z } \times 2 \mathbb { Z } { \mathrm { ~ i f ~ } } G = \mathbb { Z }$ and $I m \partial = \mathbb { Z } _ { 2 }$ if $G = \mathbb { Z } _ { 2 }$ . Thus we can compute the homology and we get

$$
{ \begin{array} { r l r } { F o r \mathbb { Z } } & { H _ { 0 } ( K ) = \mathbb { Z } / \{ 0 \} = \mathbb { Z } } & { F o r \mathbb { Z } _ { 2 } } & { H _ { 0 } ( K ) = \mathbb { Z } _ { 2 } / 0 = \mathbb { Z } _ { 2 } } \\ & { H _ { 1 } ( K ) = \mathbb { Z } ^ { 3 } / \mathbb { Z } \times 2 \mathbb { Z } = \mathbb { Z } \times \mathbb { Z } _ { 2 } } & { H _ { 1 } ( K ) = \mathbb { Z } _ { 2 } ^ { 3 } / \mathbb { Z } _ { 2 } = \mathbb { Z } _ { 2 } ^ { 2 } } \\ & { H _ { 2 } ( K ) = 0 / 0 = 0 } & { H _ { 2 } ( K ) = \mathbb { Z } _ { 2 } / 0 = \mathbb { Z } _ { 2 } } \end{array} }
$$

and all other homology groups are zero since there are no open simplices of dimension greater than 2.

10. Give an example of an irregular (i.e. not normal) covering space (with a proof ).

See Chapter 1 number 1 for an example.

11. Let $f ~ : ~ { \cal M } ~  ~ { \cal N }$ be a map of degree 1 between two smooth, closed, connected, oriented n-manifolds. Prove that $f _ { \# } : \pi _ { 1 } ( M ) \to \pi _ { 1 } ( N )$ is surjective.

12. Let M be a closed connected 5-manifold such that $\pi _ { 1 } ( M ) \equiv$ $\mathbb { Z } / 7$ . If $H _ { 2 } ( M , \mathbb { Z } ) \equiv \mathbb { Z }$ , compute all other homology and cohomology groups of M with integral coecients.

13. Let $F _ { n }$ be the free group of rank n and let $G \subset F _ { n }$ be a subgroup of index m. Prove that G is a free group and compute its rank.

14. Dene carefully a CW structure on R $P ^ { n }$ (you don't have to prove it here), and use it to compute $H ( \mathbb { R } p ^ { n } ; \mathbb { Q } )$ and $H ( \mathbb { R } P ^ { n } ; \mathbb { Z } / 2 )$

15. Prove that the map $h : S ^ { 3 } \to \mathbb { C } P ^ { 1 }$ given by $h ( x , y ) = [ x : y ]$ is a fiber bundle. Here $S ^ { 3 }$ is the unit sphere $| x | ^ { 2 } + | y | ^ { 2 } = 1$ in $\mathbb { C } ^ { 2 }$

16. Prove that $\mathbb { R } P ^ { 3 }$ is not homotopy equivalent to $\mathbb { R } P ^ { 2 } \vee S ^ { 3 }$

## Chapter 3

## 6510 Final Exam

1. Let M ; N be two manifolds. Show that $M \times N$ is orientable if and only if both M and N are orientable.

2. Using a Mayer-Vietoris argument compute deRham cohomology of spheres $S ^ { n }$ . Note allowed to use the fact that the cohomology of something that is contractible is the same as a point.

First note that $S ^ { n } - \{ p t \} \cong \mathbb { R } ^ { n }$ and since $\mathbb { R } ^ { n }$ is contractible we know that $H ^ { i } ( \mathbb { R } ^ { n } ) =$ $\left\{ \begin{array} { c l } { { \mathbb { R } } } & { \boldsymbol { i } = 0 } \\ { 0 } & { \boldsymbol { i } \neq 0 } \end{array} \right.$ . So let $U = S ^ { n } - N$ and $V = S ^ { n } - S$ . Notice that $U \cap V \cong \mathbb { R } ^ { n } - \{ p t \} \simeq$ $\dot { S } ^ { n - 1 }$ . Since $\mathbb { S } ^ { n }$ is connected we know that $H ^ { 0 } ( S ^ { n } ) = \mathbb { R }$ . Now in order to gure out $H ^ { i } ( S ^ { n } )$ notice that we can construct the following part of the Mayer-Vietoris long exact sequence

$$
H ^ { i - 1 } ( U ) \oplus H ^ { i - 1 } ( V ) \to H ^ { i - 1 } ( U \cap V ) \to H ^ { i } ( S ^ { n } ) \to H ^ { i } ( U ) \oplus H ^ { i } ( V )
$$

Now pluging in all of our equivalences and noting that the cohomology does not change under homotopy we have

$$
H ^ { i - 1 } ( \mathbb { R } ^ { n } ) \oplus H ^ { i - 1 } ( \mathbb { R } ^ { n } ) \to H ^ { i - 1 } ( S ^ { n - 1 } ) \to H ^ { i } ( S ^ { n } ) \to H ^ { i } ( \mathbb { R } ^ { n } ) \oplus H ^ { i } ( \mathbb { R } ^ { n } )
$$

Now in the case where $i \ = \ 1$ we get using facts about cohomology of contractible spaces if $n > 1$

$$
0 \to \mathbb { R } \to \mathbb { R } \oplus \mathbb { R } \to \mathbb { R } \to H ^ { i } ( S ^ { n } ) \to 0
$$

and thus using the alternating sum rule we get $H ^ { 1 } ( S ^ { n } ) = 0$ . If $n = 1$ then we get the short exact sequence

$$
0 \to \mathbb { R } \to \mathbb { R } \oplus \mathbb { R } \to \mathbb { R } \oplus \mathbb { R } \to H ^ { i } ( S ^ { n } ) \to 0
$$

which by the alternating sum rules gives us that $H ^ { 1 } ( S ^ { 1 } ) = \mathbb { R }$ . If $i ~ > ~ 1$ then we have the following sequence after plugging in what we know about the cohomology of contractible spaces.

$$
0 \to H ^ { i - 1 } ( S ^ { n - 1 } ) \to H ^ { i } ( S ^ { n } ) \to 0
$$

and thus we know that $H ^ { i - 1 } ( S ^ { n - 1 } ) \cong H ^ { i } ( S ^ { n } )$ . If $i > n$ then we get that $H ^ { i } ( S ^ { n } ) = 0$ by one of the properties of cohomology. $\operatorname { I f } i = n$ we get that $H ^ { i - \bar { 1 } } ( S ^ { n - 1 } ) \cong \dot { H } ^ { i } ( \dot { S } ^ { n } ) \cong$ $H ^ { 1 } ( S ^ { 1 } ) = \mathbb { R } . { \mathrm { ~ I f ~ } } i < n$ we get $H ^ { i } ( S ^ { n } ) { \stackrel {  } { \cong } } H ^ { i - 1 } ( S ^ { n - 1 } ) { \stackrel {  } { \cong } } H ^ { 1 } ( S ^ { n - i + 1 } ) = 0$

3. Suppose $M , N \subset \mathbb { R } ^ { 3 }$ are two 1-dimensional submanifolds of $\mathbb { R } ^ { 3 }$ . Show that for every $\epsilon > 0$ there is a $v \in \mathbb { R } ^ { 3 }$ with $| v | < \epsilon$ and so that $M + v = \{ x + v | x \in M \}$ is disjoint from N .

(Transversality Theorem): Let $F : X \times V  Y$ be smooth and $Z \subset Y$ a submanifold.   
Then if $F \pitchfork Z$ we have $\{ v \in V | F _ { v } ( x ) \cap Z \}$ has full measure in V .

Let $F : \mathcal { M } \times \mathbb { R } ^ { 3 } \to \mathbb { R } ^ { 3 }$ given by $F ( m , v ) = m + v$ Now this map is clearly surjective and hence f t N. Now by the Transversality Theorem we know that the set $\{ v \in \mathbb { R } ^ { 3 } | M + v \mathrm { ~ } \pitchfork N \}$ has full measure in $\mathbb { R } ^ { 3 }$ . Two submanifolds of $\mathbb { R } ^ { 3 }$ are transverse if for every $p \in M \cap N$ the condition $T _ { p } M + T _ { p } N = T _ { p } \mathbb { R } ^ { 3 }$ holds. But notice that since the tangent space at a point has the same dimension as the ambient manifold we would have to have $1 + 1 { = } 3$ for this to hold non-trivially in our case. So the only way that $M + v$ N is if $M \cap N = \emptyset$ . We just proved that this must happen for almost every $v \in \mathbb { R } ^ { 3 }$ so in particular we can nd a v such that for any $\epsilon > 0$ we have $| v | < \epsilon$ since the set of v has full measure.

4. Let $f : S ^ { 2 } \to S ^ { 2 }$ be a map whose degree is $\neq - 1$ . Show that $f$ has a xed point.

5. Give an example of a 2-plane eld in $\mathbb { R } ^ { 3 }$ that does not admit any (non-empty) integral manifolds.

(integrable k-plane) A k-plane eld $\Delta$ is said to be integrable if for any two vectorelds $X , Y \in \Delta$ we have that $[ X , Y ] \in \Delta$

(Frobenius Integrability Theorem) If we have an integrable k-plane eld $\Delta$ on a manifold M then around any point $p \in M$ there exists a local coordinate system so that $\begin{array} { r } { \Delta \ = \ S p a n \{ \frac { \partial } { \partial x _ { 1 } } , . . . , \frac { \partial } { \partial x _ { k } } \} } \end{array}$ More explititly there exists an integral manifold through any point $p \in { \dot { M } }$

Let $\begin{array} { r } { \Delta = S p a n \{ \frac { \partial } { \partial x } , \frac { \partial } { \partial y } + x \frac { \partial } { \partial z } \} } \end{array}$ . Then computing we nd that

$$
[ X , Y ] = { \frac { \partial } { \partial x } } ( { \frac { \partial } { \partial y } } + x { \frac { \partial } { \partial z } } ) - ( { \frac { \partial } { \partial y } } + x { \frac { \partial } { \partial z } } ) ( { \frac { \partial } { \partial x } } )
$$

$$
= { \frac { \partial ^ { 2 } } { \partial x \partial y } } + { \frac { \partial } { \partial z } } + x { \frac { \partial ^ { 2 } } { \partial z \partial x } } - x { \frac { \partial ^ { 2 } } { \partial z \partial x } } - { \frac { \partial ^ { 2 } } { \partial x \partial y } } = { \frac { \partial } { \partial z } } \not \in \Delta
$$

Thus $\Delta$ is not integrable and hence there does not eexist an integral manifold through any point in $\mathbb { R } ^ { 3 }$

6. Show that the map $h : S ^ { 3 } \to \mathbb { C } P ^ { 1 }$ given by $h ( x , y ) = [ x : y ]$ is a submersion. What are the point inverses of $h ?$ Here we view $S ^ { 3 }$ as the unit sphere in $\mathbb { C } ^ { 2 }$

7. Show that for any two points x; $\ b { y } \in \mathbb { R } ^ { n }$ there is a compactly supported isotopy $\phi _ { t }$ with $\phi _ { 0 } = i d$ and $\phi _ { 1 } ( x ) = y$

8. Show that $S L _ { n } ( \mathbb { R } ) \subset \mathbb { R } ^ { n ^ { 2 } }$ is a submanifold.

(Regular Value Theorem) Let $f : X ^ { n + m }  Y ^ { m }$ be a smooth map between manifolds and let $c \in Y$ be a regular value (for every $x \in f ^ { - 1 } ( c )$ the derivative $T _ { x } f : T _ { x } X  T _ { c } Y$ is surjective) then $Z = f ^ { - 1 } ( c )$ is a n-dimensional submanifold of X and for every $p \in Z$ we have $T _ { p } i ( T _ { p } Z ) = K e r [ T _ { p } f : T _ { p } X \to T _ { f } ( p ) Y ]$

Identify $M _ { n \times n }$ with $\mathbb { R } ^ { n ^ { 2 } }$ by choosing an ordering of entries. Then consider the determinant map det : $M _ { n \times n } \to \mathbb { R }$ Clearly $S L _ { n } ( \mathbb { R } ) = d e t ^ { - 1 } ( 1 )$ since $S L _ { n } ( \mathbb { R } )$ is the set of all matrices with determinant one. So if we can show that the derivative is surjective then we are done. So expanding along the rst row the formula for the determinant is $x _ { 1 1 } A _ { 1 1 } + . . . + x _ { 1 n } A _ { 1 n }$ and notice that only the first term has $x _ { 1 1 }$ in it. Now the Jacobian is $\begin{array} { r } { \left( \frac { \partial D e t } { \partial x _ { 1 1 } } , . . . , \frac { \partial D e t } { \partial x _ { n n } } \right) = \left( A _ { 1 1 } , . . . , A _ { n n } \right) } \end{array}$ and note that in order for this not to be surjective all the cofactors must be zero. But any matrix in $S L _ { n } ( \mathbb { R } )$ has determinant one and thus all of the cofactors can't be zero in any row let alone in all rows thus the derivative map is surjective and 1 is a regular value. Thus by the regular value theorem we are done.

## Chapter 4

## August 2006

1. Show that the set $M _ { 1 }$ of real $2 \times 2$ matrices of rank 1 is a 3 dimensional submanifold of the space $M ( 2 , 2 ) \cong \mathbb { R } ^ { 4 }$ of all real $2 \times 2$ matrices.

2. For which values of $a > 0$ does the hyperboloid $x ^ { 2 } + y ^ { 2 } - z ^ { 2 } = 1$ intersect the sphere $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = a$ transversally $( \mathbf { i n } \ \mathbb { R } ^ { 3 } ) ?$

3. Let $X , Y \subset \mathbb { R } ^ { 3 }$ be two 1-dimesional submanifolds. Show that there is $v \in \mathbb { R } ^ { 3 }$ such that X is disjoint from $Y + v : = \{ y + v | y \in Y \}$

4. Dene the Lefschetz index of an isolated xed point of a smooth map $f : M \to M$ . Compute the Lefschetz index at 0 of the map $f : \mathbb { C } \to \mathbb { C }$ given by $f ( z ) = z + z ^ { m }$

5. Compute the Gaussian curvature of the hyperboloid $x ^ { 2 } +$ $y ^ { 2 } - z ^ { 2 } = 1$ at the point $( \mathbf { 1 } , \mathbf { 0 } , \mathbf { 0 } )$

6. Regard the real pro jective plane $\mathbb { R } P ^ { 2 }$ as the space of triples $( x , y , z ) \in \mathbb { R } - \{ 0 \}$ modulo the relation $( x , y , z ) \sim ( t x , t y , t z )$ for $t \in \mathbb { R } - \lbrace 0 \rbrace$ . Dene $f : \mathbb { R } P ^ { 2 } \to \mathbb { R }$ by $\begin{array} { r } { f ( x , y , z ) = \frac { x ^ { 2 } + 2 y ^ { 2 } } { x ^ { 2 } + y ^ { 2 } + z ^ { 2 } } } \end{array}$ . Compute all critical points of f . Show that f is a Morse function and compute the Morse index of each critical point.

7. Give an example of a closed 1-form on $\mathbb { R } ^ { 2 } - \{ 0 \}$ which is not exact, and prove both properties.

8. Verify the formula $d \omega ( X , Y ) = X ( \omega ( Y ) ) - Y ( \omega ( X ) ) - \omega ( [ X , Y ] )$ for any 1-form $\omega$ on $\mathbb { R } ^ { n }$ and any two vectorelds $X , Y$ on $\mathbb { R } ^ { n }$ This is using Spivak's normalization conventions (dx ^ $\begin{array} { r } { d y ( \frac { \partial } { \partial x } , \frac { \partial } { \partial y } ) = 1 ) } \end{array}$ ; using Guillemin-Pollack's one should multiply the left-hand side by 2.

9. Let X be the quotient space of $S ^ { 2 }$ obtained by identifying the north and south noles to a single noint Carefully de-

10. For a connected CW complex X, call a connected covering space $\tilde { X } \  \ X$ abelian if it is normal and has abelian deck transformation group. Show that X has an abelian covering space that is a covering space of every other abelian covering space of X, and that such \`Universal' abelian covering space is unique up to isomorphism. Dexcribe this covering space explicitly for $X = S ^ { 1 } \vee S ^ { 1 }$ Carefully state theorems you are using.

11. Dene a -complex structure on the Klein bottle K and use it to compute H(K; Z), $H ( K , \mathbb { Z } _ { 2 } )$ , H(K; Q)

12. Let X be the quotient space of the 2-sphere $S ^ { 2 }$ under the identications $x \sim - x$ for x in the equator $S ^ { 1 }$ . Compute the homology groups $H _ { i } ( X )$ using any method that you like.

13. Apply the Lefschetz xed point theorem to show that every map $f : \mathbb { C } P ^ { n } \to \mathbb { C } P ^ { n }$ has a xed point when n is even (state the Lefschetz xed point theorem and any fact about the ring structure of H you are using). Construct a xed point free map $f : \mathbb { C } P ^ { n } \to \mathbb { C } P ^ { n }$ when n is odd.

14. Show that a p-sheeted covering map $M  N$ between two closed connected oriented smooth manifolds has degree $\pm P$

15. Show that if a closed orientable manifold M of dimension   
2k has $H _ { k - 1 } ( M ; \mathbb { Z } )$ torsionfree, then $H _ { k } ( M ; \mathbb { Z } )$ is also torsion free.

16. Show that if the closed orientable surface $M _ { g }$ of genus g retracts onto a graph $X \subset M _ { g } $ , then $H _ { 1 } ( X )$ has rank at most $g .$ You may use the following algebraic fact: a nonsingular skew-symmetric bilinear pairing over the rationals $\mathbb { Q } ,$ of the form $\mathbb { Q } ^ { n } \times \mathbb { Q } ^ { n } \to \mathbb { Q }$ , cannot be identically 0 when restricted to $V \times V$ for any Q-linear subspace $V \subset \mathbb { Q } ^ { n }$ of dimension $> n / 2$ .

## Chapter 5

## January 2006

1. Let X be a manifold and $f : X \to \mathbb { R } ^ { k }$ a continuous function. Show that for every $\epsilon > 0$ there is a smooth function $g : X \to \mathbb { R } ^ { k }$ such that $| g ( x ) - f ( x ) | | < \epsilon$ for every $x \in X$

2. Let $M _ { n \times n }$ be the set of all real $n \times n$ matrices. This set is naturally a manifold, since it can be identied with $\mathbb { R } ^ { n ^ { 2 } }$ by choosing an ordering of entries. Let $O ( n ) \subset M _ { n \times n }$ be the set of orthogonal matrices, ie matrices $A$ with $A A ^ { T } = I$ . Prove that $O ( n )$ is a submanifold of $M _ { n \times n }$ . What is the dimension of $O ( n ) ?$

3. Give a careful denition of the tangent bundle of a manifold X. Show that the total space of the tangent bundle of $S ^ { 2 }$ is not dieomorphic to $S ^ { 2 } \times \mathbb { R }$

4. State the Lefchetz xed point theorem (for Lefschetz maps). Compute the Lefschetz number of the identity map $i d : \mathbb { C } P ^ { 2 } \to$ $\mathbb { C } P ^ { 2 }$ by rst perturbing it to a Lefschetz map and then applying the Lefschetz xed point theorem.

5. State the Frobenius integrability theorem. Show that the plane eld in $\mathbb { R } ^ { 3 }$ spanned by the vector elds $\begin{array} { r } { X = \frac { \partial } { \partial x } + z \frac { \partial } { \partial y } } \end{array}$ and $\begin{array} { r } { Y = \frac { \partial } { \partial z } } \end{array}$ is not integrable on any nonempty open subset of $\mathbb { R } ^ { 3 }$ •

6. Let $\omega$ be a compactly supported smooth n-form on $\mathbb { R } ^ { n }$ Prove that the following two statements are equivalent. There exists a compactly supported smooth (n-1)-form $\eta$ such that $\begin{array} { r } { \omega = d \eta . \int _ { \mathbb { R } ^ { n } } \omega = 0 . } \end{array}$

7. Let $a : S ^ { n } \to S ^ { n }$ be the antipotal map. Suppose that $\omega$ is a smooth form on $S ^ { n }$ such that $a ^ { * } \omega = \omega$ . Prove that if ! is exact, then there is a smooth form  with $\omega = d \eta$ and $a ^ { * } \eta = \eta$ . Use the previous problem and the fact that $H ^ { k } ( S ^ { n } ) = 0$ for $0 < k < n$ to -1 1 11k(m Dn 1

1. Prove the following piece of the classication theorem for covering spaces: Let $x \in X$

## August 2005

1. In this problem we identify C with $\mathbb { R } ^ { 2 }$ in the usual manner via $z \mapsto ( \Re z , \Im z )$ Consider the following submanifolds of $\mathbb { C } ^ { 2 } -$ $\{ ( 0 , 0 ) , ( 0 , 0 . 5 ) \}$

$$
\begin{array} { r } { M _ { 1 } = \left\{ \left( z , w \right) \in \mathbb { C } ^ { 2 } | z ^ { 2 } + w ^ { 2 } = 1 \right\} , M _ { 2 } = \left\{ \left( z , w \right) \in \mathbb { C } ^ { 2 } | z ^ { 2 } - w ^ { 2 } + w = 1 \right\} , M _ { 3 } = \left\{ \left( x _ { 1 } , y _ { 1 } , x _ { 2 } , y _ { 2 } , x _ { 3 } \right) \in \mathbb { C } ^ { 2 } | z ^ { 2 } - w ^ { 2 } + w = 1 \right\} . } \end{array}
$$

Which of the pairs $M _ { i } , M _ { j }$ are transverse at $p = ( 1 , 0 ) \in \mathbb { C } ^ { 2 }$

2. Let $V , W : \mathbb { R } ^ { 4 } \to \mathbb { R } ^ { 4 }$ be vector elds on $\mathbb { R } ^ { 4 }$ dened by $V ( x , y , z , w ) = ( y , - x , w , - z )$ and $W ( x , y , z , w ) = ( w , z , - y , - x )$ . Is there a nonempty surface $\Sigma \subset \mathbb { R } ^ { 4 }$ such that for every $p \in \Sigma$ we have $V ( p ) , W ( p ) \in T _ { p } \Sigma ?$ Find such a surface or prove that it does not exist.

So we need to compute [V ; W ] where $\begin{array} { r } { V = y \frac { \partial } { \partial x } - x \frac { \partial } { \partial y } + w \frac { \partial } { \partial z } - z \frac { \partial } { \partial w } } \end{array}$ and $\begin{array} { r } { W = w \frac { \partial } { \partial x } + } \end{array}$ $\begin{array} { r } { z { \frac { \partial } { \partial y } } - y { \frac { \partial } { \partial z } } - x { \frac { \partial } { \partial w } } } \end{array}$

$$
\begin{array} { r l } { \left| V , W \right| } & { = \left| \mathcal { Y } , \partial _ { x } ^ { \bot \bot } , \emptyset , \mathcal { W } \right| = \left| \mathcal { Y } , \frac { \partial } { \partial x } , \mathcal { X } \right| = \left| \mathcal { Y } , \frac { \partial } { \partial y } , \mathcal { X } \right| = \left| \mathcal { Y } , \frac { \partial } { \partial x } , \mathcal { X } \right| = \left| \mathcal { Y } , \frac { \partial } { \partial y } , \mathcal { X } , - \mathcal { X } \right| ^ { \bot } , } \\ & { + \left| - \mathcal { X } , \frac { \partial } { \partial y } , \mathcal { B } , \frac { \partial } { \partial y } \right| + \left| - \mathcal { X } , \frac { \partial } { \partial x } , \frac { \partial } { \partial x } , + \ \mathcal { X } , - \mathcal { Y } , \frac { \partial } { \partial y } , \frac { \partial } { \partial z } \right| + \left| - \mathcal { X } , \frac { \partial } { \partial x } , - \mathcal { X } , \frac { \partial } { \partial z } \right| , } \\ & { + \left| \mathcal { X } , \frac { \partial } { \partial y } , \frac { \partial } { \partial z } , \mathcal { X } \right| = \left| \mathcal { Y } , \frac { \partial } { \partial z } , \frac { \partial } { \partial y } \right| + \left| \mathcal { X } , \frac { \partial } { \partial z } , \mathcal { Y } \right| ^ { \bot \partial } , } \\ & { + \left| - \mathcal { X } , \frac { \partial } { \partial z } , \mathcal { W } , \frac { \partial } { \partial z } \right| + \left| - 2 \frac { \partial } { \partial x } , \mathcal { Y } , \frac { \partial } { \partial y } \right| + \left| - \mathcal { X } , \frac { \partial } { \partial x } , - \mathcal { Y } , \frac { \partial } { \partial z } \right| + \left| \mathcal { X } , \frac { \partial } { \partial y } , - \mathcal { X } , \frac { \partial } { \partial z } \right| , } \\ &  + \left| - \mathcal { X } , \frac { \partial } { \partial y } , \frac { \partial } { \partial z } , \mathcal { X } \right| ^ { \partial } ,  \end{array}
$$

Thus by the Frobenius Integrability Theorem there does not exist such a surface.

3. Let M be a nonempty compact manifold with empty boundary. Prove that there is no compact manifold $W \subset M \times M$ whose boundary @W is the diagonal $\Delta = \{ ( x , x ) \in M \times M \}$

4. Is there a smooth embedding of $\mathbb { R } P ^ { 2 }$ into an orientable   
3-manifold? Provide a proof or an example.

5. Let $f : \mathbb { R } ^ { 2 } \to \mathbb { R } ^ { 3 }$ be the function given by $f ( x , y ) = ( x ^ { 2 } -$ $y , x + y ^ { 2 } , s i n ( x ) )$ . Let $\omega$ be the 2-form on $\mathbb { R } ^ { 3 }$ given by $\omega ( u , v , w ) =$ udv ^ dw. Compute the pull-back $f ^ { * } \omega$ •

6. Prove that for any two disjoint closed subsets A; $B \subset \mathbb { R } ^ { n }$ there is a smooth function $f : \mathbb { R } ^ { n }  \mathbb { R }$ such that $f = 0$ on A and $f = 1 \ \mathbf { o n } \ B$

7. Show that the total space of the tanget bundle $T ( S ^ { 2 } )$ of the   
2-sphere is not dieomorphic to $S ^ { 2 } \times \mathbb { R } ^ { 2 }$

8. Compute the Gaussian curvature of the hyperboloid $x ^ { 2 } +$ $y ^ { 2 } - z ^ { 2 } = 1$ at the point $( \mathbf { 1 } , \mathbf { 0 } , \mathbf { 0 } )$

## Chapter 6

## January 2005

1. Let $X = \{ ( x , y ) \in \mathbb { R } ^ { 3 } \times \mathbb { R } ^ { 3 } | x \cdot x = y \cdot y = 1 , x \cdot y = 0 \}$ . Show that X is a submanifold of $\mathbb { R } ^ { 3 } \times \mathbb { R } ^ { 3 }$

2. Prove that the tangent bundle T M of a smooth manifold M, viewed as a smooth manifold, is orientable.

3. Let $f : { \cal M }  N$ be a map between two closed connected oriented manifolds. If f has degree 1, show that $f _ { * }$

4. Let M be a manifold and $\Delta$ a smooth k-plane eld on M. Suppose that X and Y are smooth vector elds on M with values in $\Delta$ . Show that if for some $p \in M$ we have $X _ { p } = 0$ then $[ X , Y ] _ { p } \in \Delta$

5. Let $\begin{array} { r } { X = y \frac { \partial } { \partial x } - ( x + 1 ) \frac { \partial } { \partial y } } \end{array}$ and $\begin{array} { r } { Y = y \frac { \partial } { \partial x } - ( x - 1 ) \frac { \partial } { \partial y } } \end{array}$ be two vector elds in $\mathbb { R } ^ { 2 }$ . Compute [X; Y ].

6. Let X be the standard \middle thirds" Cantor set in R, viewed as a subset of the plane $\mathbb { R } ^ { 2 }$ . Assume that $f : X \to \mathbb { R }$ is a function with the property that for every $x \in X$ there is an open set $x \in U _ { x }$ in $\mathbb { R } ^ { 2 }$ and a smooth function $f _ { x } : U _ { x } \to \mathbb { R }$ such that $f _ { x } | _ { U _ { x } \cap X } = f | _ { U _ { x } \cap X }$ . Show that there is an open set U in $\mathbb { R } ^ { 2 }$ , $X \subset U$ , and a smooth function $g : U  \mathbb { R }$ such that $g | _ { X } = f$

7. Prove or give a counterexample (with proofs): If M is a closed submanifold of $\mathbb { R } ^ { n }$ then its tangent bundle is trivial if and only if its normal bundle is trivial.

8. Let $f : \mathbb { R } ^ { n }  \mathbb { R }$ be a smooth function. Show that for almost every $a \in \mathbb { R } ^ { n }$ the function

9.

10.