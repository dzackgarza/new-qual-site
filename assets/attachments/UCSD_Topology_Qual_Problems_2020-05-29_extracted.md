# Topology Qual Problems

D. Zack Garza

Friday 29th May, 2020

## Contents

1 Problems 1   
1.1 Homotopy . . 1   
1.2 Fundamental Group 1   
1.3 Group Actions 2   
1.4 Applications . 2   
1.5 Van Kampen’s Theorem 2   
1.6 Mayer Vietoris (Sheet 7) 3   
1.7 Cellular Homology (Sheet 8) . 4   
1.8 Degree . . . 5   
1.9 Universal Coefficient Theorem (Sheet 10) 5   
1.10 Homological Algebra (Sheet 11) 6   
1.11 Cohomology Ring (Sheet 12) 6

## 1 Problems

## 1.1 Homotopy

1. Show that any non-surjective map $f : X \to S ^ { n }$ is homotopic to the constant map.

2. Let $f , g \to S ^ { n }$ be such that $\forall x \in X , f ( x ) \neq - g ( x )$ . Show that $f \simeq g .$

3. Let $\alpha : S ^ { n } \longrightarrow S ^ { n } , \ \alpha ( p ) = - p$ be the antipodal map on $S ^ { n }$ . Show that n odd $\implies f \simeq \operatorname { i d }$

4. Show that X is homotopy-equivalent to a point $\iff \operatorname { i d } _ { X } \simeq g$ for some constant map g.

5. Show that $S ^ { 1 } \times I \simeq M$ , the Mobius strip.

6. Show that $\mathbb { R } ^ { 3 } - S ^ { 1 } \simeq S ^ { 1 } \vee S ^ { 2 }$

7. Classify the letters of the alphabet up to homeomorphism, and up to homotopy.

8. REVISIT Let $f , g : S ^ { 1 }  X , P = X \cup _ { f } B ^ { 2 } \cong X \lceil \lceil B ^ { 2 } / \sim$ , where $x \sim f ( x ) , Q = X \cup _ { g } B ^ { 2 }$ Show that $f \simeq g \implies P \simeq Q$

## 1.2 Fundamental Group

1. Show that $x , y \in X$ path & simply-connected =⇒ all paths from x to y are homotopic rel $\{ 0 , 1 \}$

2. Show that for X path connected, $\pi _ { 1 } ( X ) = \# \iff$ ∀cts. $f : S ^ { 1 } \to X \ f .$ , extends to a continuous map $F : B ^ { 2 } \to X$ ·

3. Show $\pi _ { 1 } ( X \times Y , ( x _ { 0 } , y _ { 0 } ) ) \cong \pi _ { 1 } ( X , x _ { 0 } ) \times \pi _ { 1 } ( Y , y _ { 0 } )$

4. Show $\pi _ { 1 } ( S ^ { n } ) = 1$ for $n \geq 2 .$

5. Show that $S ^ { 2 } - \{ p _ { 0 } , p _ { 1 } \} \simeq S ^ { 1 }$

6. Show that $S ^ { 3 } - \{ p _ { 0 } , p _ { 1 } \} \simeq S ^ { 2 }$

7. Show that $S ^ { 2 } \not \cong S ^ { 3 }$

8. For each of the following $f : S ^ { 1 } \to S ^ { 1 }$ , identify the corresponding $f _ { * } : \mathbb { Z } \longrightarrow \mathbb { Z } :$

1. $z \mapsto z ^ { n }$

2. $\textstyle { \overline { { x } } } \mapsto - { \overline { { x } } }$

3. $e ^ { i \theta } \mapsto e ^ { 2 \pi i \sin \theta }$

9. Determine the winding number of the following map: $f : S ^ { 1 } \longrightarrow \mathbb { C } - \{ 0 \} , z \mapsto 8 z ^ { 4 } + 4 z ^ { 3 } +$ $2 z ^ { 2 } + z ^ { - 1 }$

10. Identify $\pi _ { 1 } ( M , [ ( 1 , \frac { 1 } { 2 } ) ] )$ , and identify the class of $\partial M$

11. Let $\ b X = \ b S ^ { 1 } \times \ b S ^ { 1 }$ and γ a loop based at $x _ { 0 }$ . What is the induced map $\gamma _ { \sharp } ?$

## 1.3 Group Actions

1. Show that octagon pasting is homeomorphic to the $T = \mathbb { R } ^ { 2 } / \mathbb { Z } ^ { 2 }$

2. Let $x _ { 0 }$ be the image of 0, show that there is an order 6 homeomorphism $f : T \longrightarrow T$ fixing $x _ { 0 }$ Find a representation of $f _ { * }$ as a matrix, and find its determinant.

3. Show that $\pi _ { 1 } ( K )$ , the Klein bottle, is given by pairs $( m , n )$ where $( m , n ) \star ( p , q ) = ( m +$ $( - 1 ) ^ { n } p , n + q )$

1. Show this is torsion-free

2. Show that T is a double cover of $K$

4. For each of these actions of $\mathbb { Z } _ { 2 }$ on $S ^ { n }$ , compute $\pi _ { 1 } ( S ^ { n } / \mathbb { Z } _ { 2 } )$

1. $S ^ { 1 } , z \mapsto - z$

2. $S ^ { 2 } , ( x , y , z ) \mapsto ( - x , - y , z )$

3. $S ^ { 3 } , ( z , w ) \mapsto ( - z , - w )$

## 1.4 Applications

1. Let $i : \mathbb { R P } ^ { 2 } \longrightarrow \mathbb { R P } ^ { 3 }$ , induced by $S ^ { 2 } \hookrightarrow S ^ { 3 }$ as the equator. Show that $i \not \simeq$ const.

2. Show that there is no map $f : S ^ { 2 } \longrightarrow S ^ { 1 }$ that commutes with the antipodal map.

3. Prove that for any $f : S ^ { 2 } \longrightarrow \mathbb { R } ^ { 2 }$ , there exists $x \in S ^ { 2 }$ such that $f ( x ) = f ( - x )$

4. Prove the Ham Sandwich theorem.

5. Show that K can not be a topological group.

## 1.5 Van Kampen’s Theorem

1. Compute a presentation of $\pi _ { 1 } ( T )$ and prove it is isomorphic to $\mathbb { Z } _ { 2 }$

2. (Images)

3. Show that $T - D ^ { 1 } : = X \simeq S ^ { 1 } \vee S ^ { 1 }$

1. Show there does not exist a retraction $r : X \longrightarrow \partial X$

4. Images

5. IMages

6. Images

7. Calculate a presentation of $\pi _ { 1 } ( S ^ { 3 } - K )$

8. Show that all 3 presentations of $\pi _ { 1 } ( K )$ are isomorphic

1. Square with sides glued

2. Two mobius strips glues along boundary

3. Multiplication rule

9. Given a group $G = < A : R >$ , show how to construct a CW-complex X such that $\pi _ { 1 } ( X ) = G$

10. Write down the fundamental group of the following spaces:

11. $\mathbb { R } ^ { 2 } - \{ 0 , 1 \}$

12. $\mathbb { R } ^ { 2 } - \dot { I }$

13. The symbol $\Phi \in \mathbb { R } ^ { 2 }$

14. $S ^ { 2 } - \{ p _ { i } \} _ { i = 1 } ^ { 4 }$

15. $T - \{ p _ { 0 } \}$

16. $S ^ { 2 } / \mathbb { Z } _ { 2 }$ via the antipodal map

17. $S ^ { 2 } / \mathbb { Z } _ { 3 }$ via a $2 \pi / 3$ rotation about the z-axis.

18. $S _ { 2 } \cup \{ ( 0 , 0 , z ) \mid - 1 \leq z \leq 1 \}$

19. $\mathbb { R } ^ { 3 } - \{ ( x , y , 0 ) \ \big | \ x ^ { 2 } + y ^ { 2 } = 1 \}$

20. $\mathbb { R } ^ { 2 } - H$ , the Hopf link

21. Prove that the homophony group is trivial.

## 1.6 Mayer Vietoris (Sheet 7)

1. Compute the homology of:

1. $\mathbb { R P } ^ { 2 } = M \bigcup D ^ { 2 }$

2. $T ^ { 2 } = S ^ { 1 } \times S ^ { 1 } = ( S ^ { 1 } \times I ) \bigcup ( S ^ { 1 } \times I )$ where $( x , 0 ) \sim ( x , 1 ) \sim ( \bar { x } , 0 ) \in \mathbb { C }$ f

3. $S ^ { 1 } \bigcup _ { f } B ^ { 2 }$ attached along $\partial B ^ { 2 }$ using $z \mapsto z ^ { n }$

2. Show ${ \tilde { H } } _ { i } ( \Sigma X ) \cong { \tilde { H } } _ { i - 1 } ( X )$

1. Show $\Sigma S ^ { n } \cong S ^ { n + 1 }$

3. For $f : S ^ { n } \odot ,$ , show deg $\boldsymbol { f } = \deg \boldsymbol { \Sigma } \boldsymbol { f }$

1. Conclude $\pi _ { n } ( S ^ { n } ) = \mathbb { Z }$

4. Let $\left\{ A _ { i } \right\} ^ { n } \in \mathbf { A b }$ be finitely generated, show $\exists X \ { \Big | } \ H _ { i } ( X ) \cong A _ { i }$ for $i \leq n$ and 0 otherwise.

5. Suppose $X = \bigcup _ { i } ^ { n } A _ { i }$ such that for any $1 \leq k \leq n , \bigcap _ { i } ^ { k } A _ { i }$ is either empty or contractible, show $i \geq n - 1 \implies \tilde { H } _ { i } ( X ) = 0$ and that this bound is sharp.

6. Compute $H _ { * } ( X \times S ^ { n } )$ in terms of $H _ { * } ( X )$

1. Compute $H _ { * } ( T ^ { n } )$

7. Let $\boldsymbol { M } = ( \boldsymbol { S } ^ { 1 } \times \boldsymbol { B } ^ { 2 } ) \bigcup _ { \mathrm { i d } _ { \partial } } ( \boldsymbol { S } ^ { 1 } \times \boldsymbol { B } ^ { 2 } )$ and compute $H _ { * } ( M ; \mathbb { Z } )$

8. Let $X = S ^ { n } \times I$ with its ends glued together by a map $S ^ { n } \cup$ of degree d, calculate $H _ { * } ( X )$

9. Compute $H _ { * } ( X )$ for $X = S ^ { 3 } - N$ , with N a knotted solid torus and $\partial N = T$ its boundary torus

10. Let CA be the cone on A, show that $\tilde { H } _ { * } ( X \lfloor \rfloor C A ) \cong \tilde { H } _ { * } ( X , A )$

11. Show that the Mayer-Vietoris sequence is natural, i.e. If $X ~ { \stackrel { f } { \to } } ~ Y$ where $f ( A ) \subset C$ and $f ( B ) \subset D$ , then this commutes:

$$
H _ { n } ( X ) \ { \longrightarrow } \ H _ { n } ( A { \bigcap } B ) \ { \longrightarrow } \ H _ { n } ( A ) \oplus H _ { n } ( B ) \ { \longrightarrow } \ H _ { n - 1 } ( X )
$$

$$
\Bigg \downarrow f _ { * } = \frac { 1 } { 2 } \Bigg \downarrow f _ { * } = \frac { 1 } { 2 } \Bigg \downarrow f _ { * } f _ { * } . 
$$

$$
H _ { n } ( Y ) \ \longrightarrow \ H _ { n } ( C \bigcap D ) \ \longrightarrow \ H _ { n } ( C ) \oplus H _ { n } ( D ) \ \longrightarrow \ H _ { n - 1 } ( Y )
$$

## 1.7 Cellular Homology (Sheet 8)

Compute the homology of these spaces

1. $S _ { m } \lor S _ { n }$

2. $S ^ { m } \times S ^ { n }$

3. A hexagon with the identifications $a + b + c - a - b - c$

4. Orientable surface of genus g

1. $g = 2$ is given by $a + b - a - b + c + d - c - d$

5. Nonorientable surface of genus g Obtain by removing g discs from $S ^ { 2 }$ and attaching g mobius strips

6. $S _ { 1 } \lor S _ { 1 }$ with two discs attached via $( a b ) ^ { 3 }$ and $( a b ) ^ { 6 }$

<!-- image-->

7. This identification space:

<!-- image-->

8. This identification space:

262

<!-- image-->

9. This identification space:

10. Describe a CW complex structure for the lens space $L ( p , 1 )$ and compute $\pi _ { 1 } , H _ { * }$ for it.

## 1.8 Degree

1. Let $p ( x ) = \sum _ { i } ^ { n } a _ { i } x ^ { i }$ , view $p : \mathbb { C } \bigcup \infty \cup$ and determine its topological degree

2. Let $p ( z ) = { \frac { \prod _ { i } ^ { n } z - a _ { i } } { \prod _ { i } ^ { m } z - b _ { j } } }$ with all $a _ { i } , b _ { j }$ distinct. What is its topological degree?

3. Show that if ${ } ^ { \prime } : S ^ { m } \longrightarrow S ^ { n }$ and $\exists U \subset S ^ { m }$ such that $f | _ { U } \cong f ( U )$ , then $m = n$ and f is surjective.

## 1.9 Universal Coefficient Theorem (Sheet 10)

1. Identify the following groups up to isomorphism

1. $\mathbb { Z } _ { m } \otimes \mathbb { Z } _ { n }$

2. $\mathbb { Z } _ { 6 0 } ^ { 4 } \otimes ( \mathbb { Z } _ { 2 4 } ^ { 3 } \oplus \mathbb { Z } _ { 8 } ^ { 4 } \oplus \mathbb { Z } _ { 1 2 0 } )$

3. $\mathbb { Z } _ { n } \otimes \mathbb { Q }$

4. $\left( \mathbb { Z } \oplus \mathbb { Z } _ { n } \right) \otimes \left( \mathbb { Q } / \mathbb { Z } \right)$

2. Compute:

1. $\mathrm { T o r } ( \mathbb { Z } \oplus \mathbb { Z } _ { 2 } \oplus \mathbb { Z } _ { 8 } , \mathbb { Z } \oplus \mathbb { Z } _ { 4 } \oplus \mathbb { Z } _ { 4 } )$

$$
\mathrm { E x t } ( \mathbb { Z } \oplus \mathbb { Z } _ { 2 } \oplus \mathbb { Z } _ { 3 } , \mathbb { Z } \oplus \mathbb { Z } _ { 4 } \oplus \mathbb { Z } _ { 5 } )
$$

3. Compute the following directly from chain complexes and check using UCT:

1. $H _ { * } ( \mathbb { R P } ^ { n } ; \mathbb { Z } _ { 2 } )$

2. $H _ { * } ( \mathbb { R P } ^ { n } , \mathbb { Z } _ { 3 } )$

3. $H ^ { \ast } ( \mathbb { R P } ^ { n } , \mathbb { Z } _ { 6 } )$

4. For any space X, show that $H ^ { 1 } ( X )$ is free abelian

5. Show that $H _ { * } ( X ; \mathbb { Q } ) = H _ { * } ( X ; \mathbb { Z } ) \otimes \mathbb { Q } \ H ^ { * } ( X ; \mathbb { Z } ) = \mathrm { h o m } ( H _ { * } ( X ; \mathbb { Z } ) , \mathbb { Q } )$

6. Construct a space X such that $H _ { * } ( X ; \mathbb { Z } ) = ( \mathbb { Z } , \mathbb { Z } _ { 6 } , \mathbb { Z } _ { 1 2 } , \mathbb { Z } \oplus \mathbb { Z } _ { 4 } , 0 \cdot \cdot \cdot )$ Compute $H ^ { * } ( X ; \mathbb { Z } )$

7. Compute $H _ { * } ( \mathbb { R P } ^ { 2 } \times \mathbb { R P } ^ { 2 } ; \mathbb { Z } _ { 2 } )$

8. Compute $H _ { * } ( \Sigma \mathbb { R P } ^ { 2 } \times \mathbb { R P } ^ { 2 } ; \mathbb { Z } )$

9. Compute $H _ { * } ( \mathbb { R P } ^ { 2 } \times \mathbb { R P } ^ { 3 } ; \mathbb { Z } )$

10. Let G be a topological group. Show that $H _ { * } ( G )$ is an algebra. Show that $G \cap H _ { * } ( G )$ which factors through the homomorphism $G \longrightarrow \pi _ { 0 } ( G )$ yielding a trivial action if G is path-connected.

## 1.10 Homological Algebra (Sheet 11)

1. Show that ker $A \longrightarrow A \otimes \mathbb { Q }$ given by $a \mapsto a \otimes 1$ is the torsion subgroup of A.

2. Show that $A \hookrightarrow B \implies A \otimes \mathbb { Q } \hookrightarrow B \otimes \mathbb { Q }$

3. Find a free resolution of Q as a Z-module.

4. Compute Tor(Q, A)

1. Compute Tor $( \mathbb { Q } / \mathbb { Z } , A )$

6. Let $R = \mathbb { Z } [ x , y ]$ , and $M = R / ( x - y ) , N = R / ( x , y )$ . Construct free resolutions of $M , N$ to compute:

$\mathrm { E x t } _ { R } ^ { * } ( M , M )$

$\mathrm { E x t } _ { R } ^ { * } ( M , N )$

$\mathrm { E x t } _ { R } ^ { * } ( N , M )$

$\mathrm { E x t } _ { R } ^ { * } ( N , N )$

7. Let Λ∗ be the exterior algebra generated by the symbols $\left\{ d x _ { i } \right\} ^ { n }$ over a field k. Show that letting $d = \cdot \vee$ dx1 yields a chain complex $0 \longrightarrow \Lambda ^ { 0 } \longrightarrow \Lambda ^ { 1 } \longrightarrow \cdots \longrightarrow \Lambda ^ { n } \longrightarrow 0$ with trivial homology. Compute what happens when $d { x } _ { 1 }$ is replaced with an arbitrary non-zero element in $\Lambda ^ { 1 }$ .

8. Define M as the group ring $R = \mathbb { Z } [ \mathbb { Z } _ { 2 } ]$ with the action $( \cdot ) \times - 1$ . Construct a free resolution of M and compute $\operatorname { T o r } _ { R } ^ { * } ( M , M )$

9. Show $\operatorname { T o r } _ { R } ^ { * } ( \cdot , \cdot )$ is symmetric in the following way: Given M, N , take free resolutions, view $M _ { * } \longrightarrow M$ as a chain map and tensor with N∗ to get a chain map $\psi : { \cal M } _ { * } \otimes _ { R } { \cal N } _ { * } \longrightarrow { \cal M } \otimes _ { R } { \cal N } _ { * }$ Show that ψ is a quasi-isomorphism using the exact sequence $0 \longrightarrow ( Z _ { n } , 0 ) \longrightarrow ( N _ { n } , 0 ) \longrightarrow$ $( B _ { n - 1 } , 0 ) \longrightarrow 0$ , then switch the roles of $M , N$

10. Prove that for a SES $0 \longrightarrow A \longrightarrow B \longrightarrow C$ , the group $\operatorname { E x t } ( C , A )$ classifies extensions of C by A up to isomorphism.

## 1.11 Cohomology Ring (Sheet 12)

Todo