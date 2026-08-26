## 7. Mayer-Vietoris

1. Use the Mayer-Vietoris sequence to calculate the homology of the spaces below.
   (If you need to identify any of the maps in the long exact sequence, it helps to first “coordinatise” the known spaces by choosing explicit generators for their homology groups.)

(a). $\mathbb { R } P ^ { 2 }$ , as the union of a M¨obius strip and a disc along their boundary.

(b). The torus, as the union of a torus minus a disc $( \simeq S ^ { 1 } \vee S ^ { 1 } )$ and a disc.

(c). The Klein bottle, as the ‘twisted’ union of two cylinders $S ^ { 1 } \times I$ (identify $( x , 0 ) \sim ( x , 1 )$ , and $( x , 1 ) \sim ( \bar { x } , 0 )$ , where the bar is complex conjugation.

(d). $S ^ { 1 } \cup B ^ { 2 }$ , where $B ^ { 2 }$ attaches along its boundary circle by the map $z \mapsto z ^ { n }$

2. The suspension ΣX of a topological space is obtained from $X \times I$ by “collapsing each end to a distinct point”: that is, identify all the points of $X \times \{ 0 \}$ together, and all the points of $X \times \{ 1 \}$ together.
   Show that

$$
{ \tilde { H } } _ { i } ( \Sigma X ) \cong { \tilde { H } } _ { i - 1 } ( X ) ,
$$

Show also that $\Sigma S ^ { n }$ is homeomorphic to $S ^ { n + 1 }$ , so this calculation subsumes the calculation of the homology of spheres.

3. Suspension is a functor: if $f : X \to Y$ then there is a suspended map $\Sigma f : \Sigma X \to \Sigma Y$ , defined as the map induced on the quotient space by $f \times \mathrm { i d } : X \times I \to X \times I$ . Show that for a self-map f of $S ^ { n } , \Sigma f$ has the same degree as f, and hence that for each $n \geq 1$ and integer d $\in \mathbb { Z } ,$ , there exists a self-map of $S ^ { n }$ with degree d.

4. Let $A _ { 1 } , A _ { 2 } , \ldots , A _ { n }$ be a sequence of finitely-generated abelian groups.
   Show that there exists a path-connected pace X with $H _ { i } ( X ) \cong A _ { i }$ for $1 \leq i \leq n$ and with vanishing homology above dimension n. (Hint: use the previous problem to first build spaces with only one non-zero reduced homology group, then think about suspension.)

5. Suppose X is a space which can be written as a union of non-empty open sets $A _ { 1 } , A _ { 2 } , \ldots , A _ { n }$ so that for each $1 \leq k \leq n$ , the intersection of any k of the sets is either empty or contractible.
   Show that the reduced homology ${ \tilde { H } } _ { i } ( X )$ is zero for $i \geq n - 1$ , and give an example showing that this inequality is sharp.

6. Use Mayer-Vietoris to compute (for any X) the homology $H _ { * } ( X \times S ^ { n } )$ in terms of $H _ { * } ( X )$ . Use this to compute the homology of the n-torus $T ^ { n } = S ^ { 1 } \times \cdot \cdot \cdot \times S ^ { 1 }$

7. Let M be the space obtained by gluing two solid tori $S ^ { 1 } \times B ^ { 2 }$ together via the identity map of their boundaries.
   Compute $H _ { * } ( M ; \mathbb { Z } )$

8. Suppose the two ends of $S ^ { n } \times I$ are glued together via a map $S ^ { n } \to S ^ { n }$ of degree d. Use Mayer-Vietoris to calculate the homology of the resulting space X.

9. Let N be a knotted solid torus in $S ^ { 3 }$ , let T be its boundary torus, and let X be its exterior, that is the closure of $S ^ { 3 } - N$ . Use Mayer-Vietoris to compute the homology $H _ { * } ( X ; \mathbb { Z } )$

10. Let $( X , A )$ be a pair of spaces and let CA be the cone on A. By considering the long exact sequence for the pair $( X \cup C A , C A )$ , show that ${ \tilde { H } } _ { * } ( X \cup C A ) \cong H _ { * } ( X , A )$ . This gives an alternative definition of relative homology.

11. Let $X = A \cup B , Y = C \cup D$ be decompositions of spaces into open sets and $f : X \to Y$ a map such that $f ( A ) \subseteq C , f ( B ) \subseteq D$ . Check that the Mayer-Vietoris sequence is natural in the sense that the diagram below commutes.
    (Hint: show it first when $H _ { * } ( A + B ) , H _ { * } ( C + D )$ replace $H _ { * } ( X ) , H _ { * } ( Y ) . ,$ )

$$
{ \begin{array} { r l } & { { \longrightarrow } H _ { n + 1 } ( X ) { \longrightarrow } H _ { n } ( A \cap B ) { \longrightarrow } H _ { n } ( A ) \oplus H _ { n } ( B ) { \longrightarrow } H _ { n } ( X ) { \longrightarrow } } \\ & { { \underbrace { { \Big \downarrow } f _ { * } } } { \longrightarrow } H _ { n } ( C \cap D ) { \longrightarrow } H _ { n } ( C ) \oplus H _ { n } ( D ) { \longrightarrow } H _ { n } ( Y ) { \longrightarrow } } \\ & { { \longrightarrow } H _ { n + 1 } ( Y ) { \longrightarrow } H _ { n } ( C \cap D ) { \longrightarrow } H _ { n } ( C ) \oplus H _ { n } ( D ) { \longrightarrow } H _ { n } ( Y ) { \longrightarrow } } \end{array} }
$$
