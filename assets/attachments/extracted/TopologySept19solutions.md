# UO TOPOLOGY QUALIFYING EXAM FALL 2019 SOLUTIONS

(1) Recall that the Klein bottle K can be described as the following identification space:

<!-- image-->

Show that the Klein bottle retracts onto one of the circles $\alpha , \beta$ but not the onto the other.

Solution 1. Identify the square above with $[ 0 , 1 ] ^ { 2 }$ in the obvious way. The map $f \colon [ 0 , 1 ] ^ { 2 }  [ 0 , 1 ] / ( 0 \sim 1 ) = \alpha$ given by $f ( x , y ) = x$ respects the equivalence relation, hence descends to a continuous map ${ \bar { f } } \colon K \to \alpha$ . By definition, ${ \bar { f } } | _ { \alpha }$ is the identity map, so $\bar { f }$ is a retraction.

Next, we show that there is no retraction $r \colon K \to \beta$ . If we let $H _ { 1 }$ denote the abelianization of $\pi _ { 1 }$ , van Kampen’s theorem gives $H _ { 1 } ( K ) \cong \mathbb { Z } \langle \alpha , \beta \rangle / ( 2 \beta )$ (where we are abusing notation to let $\alpha$ and $\beta$ denote the elements of $\pi _ { 1 } ( K )$ which go around α and $\beta$ once). Let i : $\beta \hookrightarrow K$ denote inclusion. If there were a retraction $r \colon K \to \beta .$ , so $r \circ i = \mathbb { I } _ { \beta } .$ , then we would have

$$
r _ { * } \circ i _ { * } = \mathbb { I } \colon H _ { 1 } ( \beta ) \to H _ { 1 } ( \beta ) .
$$

But $H _ { 1 } ( \beta ) = \mathbb { Z } \langle \beta \rangle$ , so $i _ { * } \colon H _ { 1 } ( \beta ) \to H _ { 1 } ( K )$ is not injective, a contradiction.

Solution 2 (sketch). The same as above, except use $H _ { 1 }$ computed by cellular homology or the Mayer-Vietoris theorem.

(2) Let $M ( 3 , 1 )$ be the result of attaching a 2-cell to $S ^ { 1 }$ by the map $z \mapsto z ^ { 3 }$ . Describe explicitly, with proof, all connected covering spaces of $M ( 3 , 1 ) \times \mathbb { R } P ^ { 2 }$

Solution. First, recall that the covering spaces of $X \times Y$ are exactly the products of covering spaces of X and covering spaces of $Y$ . (One can prove this directly, or from the classification of covering spaces and the fact that $\pi _ { 1 } ( X \times Y ) \cong \pi _ { 1 } ( X ) \times \pi _ { 1 } ( Y )$ . A proof is not required for full credit for this problem.) Now, the connected covering spaces of $M ( 3 , 1 )$ are in bijection with subgroups of $\pi _ { 1 } ( M ( 3 , 1 ) ) = \mathbb { Z } / 3 \mathbb { Z }$ , of which there are two: $\mathbb { Z } / 3 \mathbb { Z }$ and {0}. Similarly, covering spaces of R $P ^ { 2 }$ are in bijection with subgroups of $\mathbb { Z } / 2 \mathbb { Z }$ , of which the only two are $\mathbb { Z } / 2 \mathbb { Z }$ and {0}. Hence, there are four connected covering spaces of $M ( 3 , 1 ) \times \mathbb { R } \overset { \cdot } { P ^ { 2 } }$

The two connected covering spaces of R $P ^ { 2 }$ are $\mathbb { I } \colon \mathbb { R } P ^ { 2 }  \mathbb { R } P ^ { 2 }$ and the quotient map $S ^ { 2 }  S ^ { 2 } / \{ \pm 1 \} = \mathbb { R } P ^ { 2 }$

The two connected covering spaces of $M ( 3 , 1 )$ are I : ${ \cal M } ( 3 , 1 )  { \cal M } ( 3 , 1 )$ and another one, $f \colon X \to M ( 3 , 1 )$ defined as follows. Let

$$
X = D ^ { 2 } \times \{ 0 , 1 , 2 \} / \sim
$$

where $( x , i ) \sim ( x , j )$ for each $x \in \partial D ^ { 2 }$ . Let $q \colon D ^ { 2 } \to M ( 3 , 1 )$ be the quotient map. Then $f ( x , j ) = q ( e ^ { 2 \pi j { \sqrt { - 1 } } / 3 } x )$ . (A clear picture would also suffice here, though $M ( 3 , 1 )$ does not embed in $\mathbb { R } ^ { 3 } . )$

Now, the four connected covering spaces of $M ( 3 , 1 ) \times \mathbb { R } P ^ { 2 }$ are $M ( 3 , 1 ) \times \mathbb { R } P ^ { 2 } , M ( 3 , 1 ) \times$ $S ^ { 2 } , X \times \mathbb { R } P ^ { 2 }$ , and $X \times S ^ { 2 }$ , with the obvious maps.

(3) Let X be the union of the (hollow) cube $\partial ( [ - 1 , 1 ] ^ { 3 } )$ and the three coordinate axes in $\mathbb { R } ^ { 3 }$

<!-- image-->

(a) Compute $\pi _ { 1 } ( X )$

(b) Compute the homology groups of X.

Solution. We start by replacing X by a homotopy equivalent space where the computations are easier. First, X deformation retracts to the union of the hollow cube and the parts of the coordinate axes lying inside the cube. Call the image of this deformation retraction Y . The space Y can be given the structure of a CW complex with, say:

• 0-skeleton $\{ ( 0 , 0 , 0 ) , ( \pm 1 , 0 , 0 ) , ( 0 , \pm 1 , 0 ) , ( 0 , 0 , \pm 1 ) \}$ 2

• 1-skeleton $Y \cap \{ ( x , y , z ) \mid x y z = 0 \}$

• 8 2-cells, around the eight vertices of the cube.

(A good picture would be a fine substitute for words here.) Let $Z \subset Y$ be the union of: • 5 of the 6 faces of the cube, and

• the segment from one of those five faces to (0, 0, 0).

Then Z is a contractible subcomplex of Y , and the space $Y / Z$ is homeomorphic to the wedge sum of $S ^ { 2 }$ and 5 circles,

$$
S ^ { 2 } \vee S ^ { 1 } \vee S ^ { 1 } \vee S ^ { 1 } \vee S ^ { 1 } \vee S ^ { 1 } .
$$

Since both $\pi _ { 1 }$ and $H _ { * }$ are homotopy invariants,

$$
\begin{array} { r l } & { \pi _ { 1 } ( X ) \cong \pi _ { 1 } ( S ^ { 2 } \vee S ^ { 1 } \vee S ^ { 1 } \vee S ^ { 1 } \vee S ^ { 1 } \vee S ^ { 1 } ) } \\ & { H _ { i } ( X ) \cong H _ { i } ( S ^ { 2 } \vee S ^ { 1 } \vee S ^ { 1 } \vee S ^ { 1 } \vee S ^ { 1 } \vee S ^ { 1 } ) . } \end{array}
$$

So, it is immediate from van Kampen’s theorem and cellular homology that

$$
\begin{array} { l } { \displaystyle \pi _ { 1 } ( X ) \cong \ast _ { i = 1 } ^ { 5 } \pi _ { 1 } ( S ^ { 1 } ) \cong F _ { 5 } } \\ { \displaystyle H _ { 0 } ( X ) \cong \mathbb { Z } } \\ { \displaystyle H _ { 1 } ( X ) \cong \bigoplus _ { i = 0 } ^ { 5 } H _ { 1 } ( S ^ { 1 } ) \cong \mathbb { Z } ^ { 5 } } \\ { \displaystyle H _ { 2 } ( X ) \cong H _ { 2 } ( S ^ { 2 } ) \cong \mathbb { Z } } \\ { \displaystyle H _ { i } ( X ) = 0 \qquad i > 2 } \end{array}
$$

(Students do not need to spell out further details here for full credit.)

Solution 2 (sketch). Quotient by a different contractible subcomplex, or apply van Kampen’s theorem, and the Mayer-Vietoris sequence or cellular homology, directly to X.

(4) Let $\phi \colon S ^ { 2 } \times S ^ { 2 } \to S ^ { 2 } \times S ^ { 2 }$ be the map $\phi ( x , y ) ~ = ~ ( y , x )$ Let $T _ { \phi } ~ = ~ ( S ^ { 2 } \times S ^ { 2 } \times$ $[ 0 , 1 ] ) / ( ( x , y , 1 ) \sim ( y , x , 0 ) )$ be the mapping torus of $\phi .$

(a) Compute the homology groups of $T _ { \phi }$

Solution 1. Let

$$
\begin{array} { l } { { U = T _ { \phi } \setminus ( S ^ { 2 } \times S ^ { 2 } \times \{ 0 \} ) } } \\ { { V = T _ { \phi } \setminus ( S ^ { 2 } \times S ^ { 2 } \times \{ 1 / 2 \} ) . } } \end{array}
$$

There is an obvious homeomorphism $f \colon U \ { \stackrel { \cong } { \longrightarrow } } \ S ^ { 2 } \times S ^ { 2 } \times ( 0 , 1 )$ . There is also a homeomorphism $g \colon V \stackrel { \cong } { \longrightarrow } S ^ { 2 } \times S ^ { 2 } \times ( 1 / 2 , 3 / 2 )$ defined by

$$
g ( p , t ) = { \left\{ \begin{array} { l l } { ( \phi ^ { - 1 } ( p ) , t + 1 ) } & { 0 \leq t < 1 / 2 } \\ { ( p , t ) } & { 1 / 2 < t \leq 1 . } \end{array} \right. }
$$

For I = (0, 1), I = (1/2, 3/2), I = (0, 1/2), or $I = ( 1 / 2 , 1 )$ , let $p \colon S ^ { 2 } \times S ^ { 2 } \times I $ $S ^ { 2 } \times S ^ { 2 }$ denote projection. Then we have isomorphisms

$$
\begin{array} { c } { { ( p \circ f ) _ { * } \colon H _ { * } ( U ) { \stackrel { \cong } { \longrightarrow } } H _ { * } ( S ^ { 2 } \times S ^ { 2 } ) } } \\ { { ( p \circ g ) _ { * } \colon H _ { * } ( V ) { \stackrel { \cong } { \longrightarrow } } H _ { * } ( S ^ { 2 } \times S ^ { 2 } ) } } \\ { { ( ( p \amalg p ) \circ f ) _ { * } \colon H _ { * } ( U \cap V ) { \stackrel { \cong } { \longrightarrow } } H _ { * } ( S ^ { 2 } \times S ^ { 2 } ) \oplus H _ { * } ( S ^ { 2 } \times S ^ { 2 } ) . } } \end{array}
$$

Apply the Mayer-Vietoris theorem to the cover ${ \cal T } _ { \phi } = U \cup V$ and use the identifications above to obtain

$$
\begin{array} { r l } & { \quad \cdots \xrightarrow { \quad } H _ { i } ( U \cap V ) \xrightarrow { \quad \quad } H _ { i } ( U ) \oplus H _ { i } ( V ) \xrightarrow { \quad \quad } H _ { i } ( T _ { \phi } ) \quad \quad \cdots \xrightarrow { \quad } H _ { i } ( T _ { \phi } ) } \\ & { \quad \quad \quad \quad \quad ( ( p \mathbf { I } p ) \circ f ) _ { * } \bigg \downarrow } \\ & { \quad \quad \quad H _ { i } ( S ^ { 2 } \times S ^ { 2 } ) \oplus H _ { i } ( S ^ { 2 } \times S ^ { 2 } ) \xrightarrow [ \Psi _ { i } ] { \quad \quad } H _ { i } ( S ^ { 2 } \times S ^ { 2 } ) \oplus H _ { i } ( S ^ { 2 } \times S ^ { 2 } ) . } \end{array}
$$

The map Ψ is the unique map so that the diagram commutes. It follows from the definitions that

$$
\Psi _ { i } = \left( \begin{array} { c c } { { \mathbb I } } & { { \mathbb I } } \\ { { ( \phi ^ { - 1 } ) _ { * } } } & { { \mathbb I } } \end{array} \right) .
$$

(Depending on one’s sign convention for the Mayer-Vietoris sequence, there might be minus signs in the second row.) There is a short exact sequence

$$
0 \to \operatorname { c o k e r } ( \Phi _ { i } ) \to H _ { i } ( T _ { \phi } ) \to \ker ( \Phi _ { i - 1 } ) \to 0 .
$$

Note that $\phi ^ { 2 } = \mathbb { I }$ , so $( \phi ^ { - 1 } ) _ { * } = \phi _ { * }$ . Also, row-reducing,

$$
\begin{array} { c } { \mathrm { k e r } ( \Phi _ { i } ) = \mathrm { k e r } ( \phi _ { * } - \mathbb { I } ) } \\ { \mathrm { c o k e r } ( \Phi _ { i } ) = \mathrm { c o k e r } ( \phi _ { * } - \mathbb { I } ) . } \end{array}
$$

From cellular homology (or the K¨unneth theorem), we have

$$
\begin{array} { r } { H _ { i } ( S ^ { 2 } \times S ^ { 2 } ) = \left\{ \begin{array} { l l } { \mathbb { Z } } & { i = 0 } \\ { \mathbb { Z } ^ { 2 } } & { i = 2 } \\ { \mathbb { Z } } & { i = 4 } \\ { 0 } & { \mathrm { e l s e } . } \end{array} \right. } \end{array}
$$

Further, by considering degrees, $\phi _ { * }$ is the identity map on $H _ { 0 }$ , the matrix $\left( \begin{array} { l } { 0 \ 1 } \\ { 1 \ 0 } \end{array} \right)$ on $H _ { 2 } .$ and the identity map on $H _ { 4 }$

Hence, we have

$$
\begin{array} { r l } & { H _ { 0 } ( T _ { \phi } ) \cong \mathrm { c o k e r } \big ( ( \phi _ { * } - \mathbb { I } ) \colon H _ { 0 } ( S ^ { 2 } \times S ^ { 2 } )  H _ { 0 } ( S ^ { 2 } \times S ^ { 2 } ) \big ) \cong \mathbb { Z } } \\ & { H _ { 1 } ( T _ { \phi } ) \cong \mathrm { k e r } \big ( ( \phi _ { * } - \mathbb { I } ) \colon H _ { 0 } ( S ^ { 2 } \times S ^ { 2 } )  H _ { 0 } ( S ^ { 2 } \times S ^ { 2 } ) \big ) \cong \mathbb { Z } } \\ & { H _ { 2 } ( T _ { \phi } ) \cong \mathrm { c o k e r } \big ( ( \phi _ { * } - \mathbb { I } ) \colon H _ { 2 } ( S ^ { 2 } \times S ^ { 2 } )  H _ { 2 } ( S ^ { 2 } \times S ^ { 2 } ) \big ) \cong \mathrm { c o k e r } ( \begin{array} { l l } { - 1 } & { 1 } \\ { 1 } & { - 1 } \end{array} ) \cong \mathbb { Z } } \\ & { H _ { 3 } ( T _ { \phi } ) \cong \mathrm { k e r } \big ( ( \phi _ { * } - \mathbb { I } ) \colon H _ { 2 } ( S ^ { 2 } \times S ^ { 2 } )  H _ { 2 } ( S ^ { 2 } \times S ^ { 2 } ) \big ) \cong \mathrm { k e r } ( \begin{array} { l l } { - 1 } & { 1 } \\ { 1 } & { - 1 } \end{array} ) \cong \mathbb { Z } } \\ & { H _ { 4 } ( T _ { \phi } ) \cong \mathrm { c o k e r } \big ( ( \phi _ { * } - \mathbb { I } ) \colon H _ { 4 } ( S ^ { 2 } \times S ^ { 2 } )  H _ { 4 } ( S ^ { 2 } \times S ^ { 2 } ) \big ) \cong \mathbb { Z } } \\ & { H _ { 5 } ( T _ { \phi } ) \cong \mathrm { k e r } \big ( ( \phi _ { * } - \mathbb { I } ) \colon H _ { 4 } ( S ^ { 2 } \times S ^ { 2 } )  H _ { 4 } ( S ^ { 2 } \times S ^ { 2 } ) \big ) \cong \mathbb { Z } } \end \end{array}
$$

Solution 2. (sketch). Hatcher gives a long exact sequence for the homology of a mapping torus, which we did not cover in class but which some students might know.

Solution 3. (sketch). It is a bit tedious, but this computation can be done using cellular homology.

(5) (a) Define the compactly supported cohomology groups $H _ { c } ^ { i }$ of a space X.

Solution. If $K \subset L \subset X$ then $X \setminus K \supset X \setminus L$ . Hence, the inclusion map of pairs $( X , X \setminus L ) \hookrightarrow ( X , X \setminus K )$ induces a map of relative cohomology $H ^ { i } ( X , X \setminus K ) \to$ $H ^ { i } ( X , X \setminus L )$ . Further, if $K \subset L \subset M$ then, since the diagram of inclusions

<!-- image-->

commutes, the diagram of relative cohomologies

<!-- image-->

commutes.

Hence, the groups

$$
\{ H ^ { i } ( X , X \setminus K ) \} _ { K \subset X { \mathrm { ~ c o m p a c t } } }
$$

form a directed system. The compactly supported cohomology $H _ { c } ^ { i } ( X )$ is the direct limit of this directed system.

Solution 2 (sketch). Alternatively, one can define

$$
C _ { c } ^ { i } ( X ) = \operatorname * { l i m } _ { K \subset X { \mathrm { ~ c o m p a c t ~ } } } C ^ { i } ( X , X \setminus K ) ,
$$

see that d induces a map d : $C _ { c } ^ { i } ( X ) \to C _ { c } ^ { i + 1 } ( X )$ and these maps form a chain complex, and define $H _ { c } ^ { i } ( X )$ to be the homology of this chain complex.

(b) Show that $H _ { c } ^ { i }$ is not a cohomology theory. More precisely, show that there is no cohomology theory $h ^ { * }$ so that $h ^ { i } ( \breve { X } ) \cong H _ { c } ^ { i } ( X )$ for all spaces X and integers i. Solution. If $h ^ { * }$ is a cohomology theory then the homotopy axiom implies that if $X \simeq Y$ then $h ^ { i } ( X ) \cong h ^ { i } ( Y )$ for all i. For compactly supported cohomology, by definition $H _ { c } ^ { 0 } ( \mathbb { R } ^ { 0 } ) = H ^ { 0 } ( \mathbb { R } ^ { 0 } , \emptyset ) \cong \mathbb { Z }$ . On the other hand, $H _ { c } ^ { 0 } ( \mathbb { R } ^ { 1 } ) = 0 \mathrm { : }$ : it follows from Poincar´e duality that $H _ { c } ^ { 0 } ( \mathbb { R } ^ { 1 } ) \cong H _ { 1 } ( \mathbb { R } ^ { 1 } ) = 0$ (Alternatively, it is not hard to show directly that $H _ { c } ^ { 0 } ( \mathbb { R } ^ { 1 } ) = { \bar { 0 } } . )$

Remark. Compactly-supported cohomology is functorial under proper maps (though not all maps), and invariant under proper homotopies.

(6) Let $( \mathbb { R } P ^ { 2 } ) ^ { 2 0 1 9 }$ be the product of 2019 copies of R $P ^ { 2 }$ with itself. Suppose $f \colon ( \mathbb { R } P ^ { 2 } ) ^ { 2 0 1 9 } $ $( \mathbb { R } P ^ { 2 } ) ^ { 2 0 1 9 }$ is a continuous. Show f has a fixed point.

Solution. Recall that the homology of R $P ^ { 2 }$ is

$$
H _ { i } ( \mathbb { R } P ^ { 2 } ; \mathbb { Z } ) \cong { \left\{ \begin{array} { l l } { \mathbb { Z } } & { i = 0 } \\ { \mathbb { Z } / 2 \mathbb { Z } } & { i = 1 } \\ { 0 } & { { \mathrm { o t h e r w i s e . } } } \end{array} \right. }
$$

(This follows easily, for example, from cellular homology, or from the long exact sequence for a pair or the Mayer-Vietoris sequence.) Hence, by the universal coefficient theorem,

$$
H _ { i } ( \mathbb { R } P ^ { 2 } ; \mathbb { Q } ) \cong { \left\{ \begin{array} { l l } { \mathbb { Q } } & { i = 0 } \\ { 0 } & { { \mathrm { o t h e r w i s e . } } } \end{array} \right. }
$$

Now, by the K¨unneth theorem,

$$
H _ { i } ( ( \mathbb { R } P ^ { 2 } ) ^ { 2 0 1 9 } ; \mathbb { Q } ) \cong { \left\{ \begin{array} { l l } { \mathbb { Q } } & { i = 0 } \\ { 0 } & { { \mathrm { o t h e r w i s e . } } } \end{array} \right. }
$$

For any map $f \colon X \to X , f _ { * } \colon H _ { 0 } ( X ) \to H _ { 0 } ( X )$ is the identity map. Hence, for any map $f \colon ( \mathbb { R } \dot { P } ^ { 2 } ) ^ { 2 0 1 9 } \to ( \mathbb { R } P ^ { 2 } ) ^ { 2 0 1 9 }$ , the Lefschetz trace $\tau ( f ) = 1$ . Hence, f has a fixed point. (7) Consider the knot $5 _ { 2 }$

<!-- image-->

(a) I claim I have a normal covering space of $S ^ { 3 } \setminus 5 _ { 2 }$ with deck transformation group $\mathbb { Z } / 5 3 7 \mathbb { Z }$ . Do you believe me? Justify.

(b) Now I claim I have a normal covering space of $S ^ { 3 } \setminus 5 _ { 2 }$ with deck transformation group $\mathbb { Z } / 2 \mathbb { Z } \times \mathbb { Z } / 2 \mathbb { Z }$ . Do you believe me? Justify.

Solution 1. From the classification of covering spaces, a space X has a normal covering space $\widetilde { X }$ with deck group G if and only if $\pi _ { 1 } ( X )$ has a normal subgroup H with $\pi _ { 1 } ( X ) / H \cong G$ . Further, if G is abelian then H must contain the commutator subgroup of $\pi _ { 1 } ( X )$ , so

$$
H _ { 1 } ( X ) = \pi _ { 1 } ( X ) / [ \pi _ { 1 } ( X ) , \pi _ { 1 } ( X ) ] \twoheadrightarrow \pi _ { 1 } ( X ) / H \cong G .
$$

Conversely, if $H _ { 1 } ( X )$ surjects onto G then ker $( \pi _ { 1 } ( X )  H _ { 1 } ( X )  G )$ corresponds to a normal covering space with deck group G.

By Alexander duality, $H _ { 1 } ( S ^ { 3 } \setminus 5 _ { 2 } ) \cong H ^ { 1 } ( S ^ { 1 } ) \cong \mathbb { Z }$ Since Z surjects onto $\mathbb { Z } / 5 3 7 \mathbb { Z }$ $S ^ { 3 } \setminus 5 _ { 2 }$ does have a normal covering space with deck group $\mathbb { Z } / 5 3 7 \mathbb { Z }$ . Since Z does not surject onto $\mathbb { Z } / 2 \mathbb { Z } \times \mathbb { Z } / 2 \mathbb { Z } , S ^ { 3 } \backslash 5 _ { 2 }$ does not have a normal covering space with deck group $\mathbb { Z } / 2 \mathbb { Z } \times \mathbb { Z } / 2 \mathbb { Z }$

Solution 2 (sketch). Students in the class have seen the Wirtinger presentation for $\pi _ { 1 } ( S ^ { 3 } \backslash K )$ and could substitute that for Alexander duality (though it is slightly tedious).

(8) Let G be a finitely generated abelian group. Show that no closed 3-manifold is a $K ( G , 2 )$ (Hint: reduce to the orientable case and consider the homology of a $K ( G , 2 ) .$ )

Solution 1. Let M be a closed 3-manifold. If M is non-orientable then the orientation double cover of M is a nontrivial 2-fold cover, so $\pi _ { 1 } ( M ) \neq 0$ , so M is not a $K ( G , 2 )$

Next, if M is orientable then by Poincar´e duality, $H _ { 3 } ( M ) \cong \mathbb { Z }$ . So, it suffices to show that $H _ { 3 } ( K ( G , 2 ) ) = 0$ We can build a space $K ( G , 2 )$ as follows. Start with a Moore space built from 2-cells and 3-cells. By cellular approximation (or van Kampen’s theorem), $\pi _ { 1 } ( M ( G , 2 ) ) = 0$ , and by the Hurewicz theorem, $\pi _ { 2 } ( M ( G , 2 ) ) \cong H _ { 2 } ( M ( G , 2 ) ) \cong G$ . Now, attach 4-cells to $M ( G , 2 )$ to kill of $\pi _ { 3 } ( M ( G , 2 ) )$ , attach 5-cells to the result to kill of $\pi _ { 4 }$ and so on. Since the resulting $K ( G , 2 )$ has the same 3-skeleton as $M ( G , 2 ) , H _ { 3 } ( K ( G , 2 ) )$ is a quotient of $H _ { 3 } ( M ( G , 2 ) ) = 0$ , hence vanishes. In particular, $H _ { 3 } ( M ) \cong H _ { 3 } ( K ( G , 2 ) )$

Solution 2. Suppose that M is a $K ( G , 2 )$ . As in Solution 1, M is orientable. By the 1-dimensional Hurewicz theorem, $H _ { 1 } ( M ) = 0$ , so by Poincar´e duality $H ^ { 2 } ( M ) = 0$ so by the universal coefficient theorem $H _ { 2 } ( M ) = 0$ . So, by the Hurewicz theorem one more time, $G = \pi _ { 2 } ( M ) = 0$ . Now, if M is a $K ( \{ 0 \} , 2 )$ then $\pi _ { i } ( M ) = 0$ for all i so by the Hurewicz theorem $H _ { i } ( M ) = 0$ for all $i > 0$ . In particular, $H _ { 3 } ( M ) = 0$ , which contradicts the fact that M was closed and orientable.

(9) Recall that orientable k-dimensional vector bundles over X are in bijection with $[ X , \mathrm { G r _ { 3 } ^ { + } } ( \mathbb { R } ^ { \infty } ) ]$ where $\operatorname { G r } _ { 3 } ^ { + } ( { \mathbb { R } } ^ { \infty } ) = V _ { 3 } ( { \mathbb { R } } ^ { \infty } ) / S O ( 3 )$ is the Grassmanian of oriented 3-planes in $\mathbb { R } ^ { \infty }$ . Compute $\pi _ { i } ( \mathrm { G r _ { 3 } ^ { + } } ( \mathbb { R } ^ { \infty } ) )$ for $i \leq 4$ . (Hint: recall that $S O ( 3 ) \cong \mathbb { R } P ^ { 3 } . ,$ )

Solution. The space $V _ { 3 } ( \mathbb { R } ^ { \infty } )$ is contractible, so the long exact sequence for the fibration $S O ( 3 )  V _ { 3 } ( \mathbb { R } ^ { \infty } )  \mathrm { G r } _ { 3 } ^ { + } ( \mathbb { R } ^ { \infty } )$ decomposes as

$$
0 = \pi _ { n } ( V _ { 3 } ( \mathbb { R } ^ { \infty } ) \to \pi _ { n } ( { \mathrm { G r } } _ { 3 } ^ { + } ( \mathbb { R } ^ { \infty } ) ) \to \pi _ { n - 1 } ( S O ( 3 ) ) \to \pi _ { n - 1 } ( V _ { 3 } ( \mathbb { R } ^ { \infty } ) ) = 0 .
$$

Hence, $\pi _ { n } ( \operatorname { G r } _ { 3 } ^ { + } ( \mathbb { R } ^ { \infty } ) ) \cong \pi _ { n - 1 } ( S O ( 3 ) )$

As noted in the hint, $S O ( 3 ) \ \cong \ \mathbb { R } P ^ { 3 }$ Hence, $\pi _ { 1 } ( S O ( 3 ) ) ~ \cong ~ \mathbb { Z } / 2 \mathbb { Z }$ and for $i ~ > ~ 1$ , $\pi _ { i } ( S O ( 3 ) ) \cong \pi _ { i } ( S ^ { 3 } )$ (since $S ^ { 3 }$ is a covering space of R $P ^ { 3 } )$ . From the Hurewicz theorem, $\pi _ { 2 } ( S ^ { 3 } ) = 0$ and $\pi _ { 3 } ( S ^ { 3 } ) \cong H _ { 3 } ( S ^ { 3 } ) \cong \mathbb { Z }$ . Hence, the first few homotopy groups of $\mathrm { G r _ { 3 } ^ { + } } ( \mathbb { R } ^ { \infty } ) )$ are:

$$
\pi _ { i } ( \mathrm { G r } _ { 3 } ^ { + } ( \mathbb { R } ^ { \infty } ) ) = \left\{ \begin{array} { l l } { 0 } & { i = 0 } \\ { 0 } & { i = 1 } \\ { \mathbb { Z } / 2 \mathbb { Z } } & { i = 2 } \\ { 0 } & { i = 3 } \\ { \mathbb { Z } } & { i = 4 . } \end{array} \right.
$$

(10) Let Y be a 2-connected space and $p \colon Y \to \operatorname { G r } _ { 3 } ^ { + } ( \mathbb { R } ^ { \infty } )$ a fibration so that $p _ { * } \colon \pi _ { i } ( Y ) \to$ $\pi _ { i } ( \mathrm { G r _ { 3 } ^ { + } } ( \mathbb { R } ^ { \infty } ) )$ is an isomorphism for $i \ > \ 2$ (That is, Y is a 2-connected cover of $\mathrm { G r _ { 3 } ^ { + } ( \mathbb { R } ^ { \infty } ) . ) }$ Define the (primary) obstruction in cohomology to lifting a map $f \colon X \to$ $\mathrm { G r _ { 3 } ^ { + } } ( \mathbb { R } ^ { \infty } )$ to a map ${ \widetilde { f } } \colon X \to Y$ and give an example where the obstruction does not vanish.

Solution. From the long exact sequence in homotopy groups, the fibration $Y $ $\mathrm { G r _ { 3 } ^ { + } } ( \mathbb { R } ^ { \infty } )$ has fiber $K ( \mathbb { Z } / 2 \mathbb { Z } , 1 )$ Since $\pi _ { 1 } ( Y ) \cong \pi _ { 1 } ( \mathrm { G r } _ { 3 } ^ { + } ( \mathbb { R } ^ { \infty } ) ) = 0$ the map $Y $ $\mathrm { G r _ { 3 } ^ { + } } ( \mathbb { R } ^ { \infty } )$ is a principal fibration. (This is a special case of the statement about Moore-Postnikov fibrations on the “possibly useful theorems” page, and is also immediate from the construction above.) So, a map $f \colon X \to \operatorname { G r } _ { 3 } ^ { + } ( { \mathbb { R } } ^ { \infty } )$ has a lift if and only if the composite

$$
X \ { \overset { f } { \longrightarrow } } \ \operatorname { G r } _ { 3 } ^ { + } ( \mathbb { R } ^ { \infty } ) \ { \overset { g } { \longrightarrow } } \ K ( \mathbb { Z } / 2 \mathbb { Z } , 2 )
$$

is nullhomotopic. The homotopy class $[ g \circ f ] \in [ X , K ( \mathbb { Z } / 2 \mathbb { Z } , 2 ) ]$ is trivial if and only if

$$
( g \circ f ) ^ { * } ( \iota ) \in H ^ { 2 } ( X ; \mathbb { Z } / 2 \mathbb { Z } )
$$

vanishes. The element $( g \circ f ) ^ { * } ( \iota )$ is the primary obstruction to lifting $f .$

For an example where the primary obstruction does not vanish, take $X = \mathrm { G r _ { 3 } ^ { + } ( \mathbb { R } ^ { \infty } ) }$ and let $f$ be the identity map. Then from the construction in the previous solution $( g \circ \mathbb { I } ) ^ { * } ( \iota ) = g ^ { * } ( \iota )$ is a generator of $H ^ { 2 } ( \mathrm { G r _ { 3 } ^ { + } } ( \mathbb { R } ^ { \infty } ) ; \mathbb { Z } / 2 \mathbb { Z } )$