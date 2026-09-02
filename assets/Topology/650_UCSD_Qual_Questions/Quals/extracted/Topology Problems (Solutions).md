# Topology Qual Problems

D. Zack Garza

November 15, 2019

## Contents

1 Problems 1   
1.1 Homotopy . . 1   
1.2 Fundamental Group 2   
1.3 Group Actions 2   
1.4 Applications . 2   
1.5 Van Kampen’s Theorem 3   
1.6 Mayer Vietoris (Sheet 7) . 3   
1.7 Cellular Homology (Sheet 8) . 4   
1.8 Degree . 5   
1.9 Universal Coefficient Theorem (Sheet 10) 5   
1.10 Homological Algebra (Sheet 11) . 6   
1.11 Cohomology Ring (Sheet 12) 6   
2 Topology Problems: Solutions 7   
2.1 Homotopy . . 7   
2.2 Fundamental Group 12   
2.3 Group Actions 16   
2.4 Covering Spaces . 16   
2.5 Simplicial Homology 22   
2.6 Mayer Vietoris Problems 25   
2.6.1 $\mathbb { R } \mathbb { P } ^ { 2 }$ 25   
2.7 Claim: $H _ { 0 } ( \mathbb { R P } ^ { 2 } ) = \mathbb { Z }$ 28   
2.8 Cellular Homology 29   
2.9 Degree . 29   
2.10 UCT . 29   
2.11 Homological Algebra . . 29

## 1 Problems

## 1.1 Homotopy

1. Show that any non-surjective map $f : X \to S ^ { n }$ is homotopic to the constant map.

2. Let $f , g \to S ^ { n }$ be such that $\forall x \in X , f ( x ) \neq - g ( x )$ . Show that $f \simeq g .$

3. Let $\alpha : S ^ { n }  S ^ { n } , \alpha ( p ) = - p$ be the antipodal map on $S ^ { n }$ . Show that $n \mathrm { o d d } \implies f \simeq \mathrm { i d } .$

4. Show that X is homotopy-equivalent to a point $\iff \operatorname { i d } _ { X } \simeq g$ for some constant map $g .$

5. Show that $S ^ { 1 } \times I \simeq M$ , the Mobius strip.

6. Show that $\mathbb { R } ^ { 3 } - S ^ { 1 } \simeq S ^ { 1 } \vee S ^ { 2 }$

7. Classify the letters of the alphabet up to homeomorphism, and up to homotopy.

8. REVISIT Let $f , g : S ^ { 1 }  X , P = X \cup _ { f } B ^ { 2 } \cong X \amalg B ^ { 2 } / \sim$ , where $x \sim f ( x ) , Q = X \cup _ { g } B ^ { 2 }$ Show that $f \simeq g \implies P \simeq Q$

## 1.2 Fundamental Group

1. Show that $x , y \in X$ path & simply-connected =⇒ all paths from x to y are homotopic rel {0, 1}.

2. Show that for X path connected, $\pi _ { 1 } ( X ) = \# \iff$ ∀cts. $f : S ^ { 1 } \to X ~ f$ , extends to a continuous map $F : B ^ { 2 } \to X$ .

3. Show $\pi _ { 1 } ( X \times Y , ( x _ { 0 } , y _ { 0 } ) ) \cong \pi _ { 1 } ( X , x _ { 0 } ) \times \pi _ { 1 } ( Y , y _ { 0 } )$

4. Show $\pi _ { 1 } ( S ^ { n } ) = 1 { \mathrm { ~ f o r ~ } } n \geq 2 .$

5. Show that $S ^ { 2 } - \{ p _ { 0 } , p _ { 1 } \} \simeq S ^ { 1 }$

6. Show that $S ^ { 3 } - \{ p _ { 0 } , p _ { 1 } \} \simeq S ^ { 2 }$

7. Show that $S ^ { 2 } \not \cong S ^ { 3 } .$

8. For each of the following $f : S ^ { 1 } \to S ^ { 1 }$ , identify the corresponding $f _ { * } : \mathbb { Z } \to \mathbb { Z } \colon$

1. $z \mapsto z ^ { n }$

2. ${ \bar { x } } \mapsto - { \bar { x } }$

3. $e ^ { i \theta } \mapsto e ^ { 2 \pi i \sin \theta }$

9. Determine the winding number of the following map: $f : S ^ { 1 } \to \mathbb { C } - \{ 0 \} , z \mapsto 8 z ^ { 4 } + 4 z ^ { 3 } + 2 z ^ { 2 } +$ $z ^ { - 1 }$

10. Identify $\pi _ { 1 } ( M , [ ( 1 , \frac { 1 } { 2 } ) ] )$ , and identify the class of $\partial M$

11. Let $X = S ^ { 1 } \times S ^ { 1 }$ and γ a loop based at x0. What is the induced map $\gamma _ { \sharp } ?$

## 1.3 Group Actions

1. Show that octagon pasting is homeomorphic to the $T = \mathbb { R } ^ { 2 } / \mathbb { Z } ^ { 2 }$

2. Let $x _ { 0 }$ be the image of 0, show that there is an order 6 homeomorphism $f : T  T$ fixing $x _ { 0 }$ Find a representation of $f _ { * }$ as a matrix, and find its determinant.

3. Show that $\pi _ { 1 } ( K )$ , the Klein bottle, is given by pairs $( m , n )$ where $( m , n ) \star ( p , q ) = ( m +$ $( - 1 ) ^ { n } p , n + q )$

1. Show this is torsion-free

2. Show that T is a double cover of $K$

4. For each of these actions of $\mathbb { Z } _ { 2 }$ on $S ^ { n }$ , compute $\pi _ { 1 } ( S ^ { n } / \mathbb { Z } _ { 2 } )$

1. $S ^ { 1 } , z \mapsto - z$

2. $S ^ { 2 } , ( x , y , z ) \mapsto ( - x , - y , z )$

3. $S ^ { 3 } , ( z , w ) \mapsto ( - z , - w )$

## 1.4 Applications

1. Let $i : \mathbb { R P } ^ { 2 }  \mathbb { R P } ^ { 3 }$ , induced by $S ^ { 2 } \hookrightarrow S ^ { 3 }$ as the equator. Show that $i \not \simeq$ const.

2. Show that there is no map $f : S ^ { 2 } \to S ^ { 1 }$ that commutes with the antipodal map.

3. Prove that for any $f : S ^ { 2 } \to \mathbb { R } ^ { 2 }$ , there exists $x \in S ^ { 2 }$ such that $f ( x ) = f ( - x )$

4. Prove the Ham Sandwich theorem.

5. Show that K can not be a topological group.

## 1.5 Van Kampen’s Theorem

1. Compute a presentation of $\pi _ { 1 } ( T )$ and prove it is isomorphic to $\mathbb { Z } _ { 2 }$

2. (Images)

3. Show that $T - D ^ { 1 } : = X \simeq S ^ { 1 } \vee S ^ { 1 }$

1. Show there does not exist a retraction $r : X \to \partial X$

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

12. $\mathbb { R } ^ { 2 } - I$

13. $\mathrm { T h e \ s y m b o l \oplus } \in \mathbb { R } ^ { 2 }$

14. $S ^ { 2 } - \{ p _ { i } \} _ { i = 1 } ^ { 4 }$

15. $T - \{ p _ { 0 } \}$

16. $S ^ { 2 } / \mathbb { Z } _ { 2 }$ via the antipodal map

17. $S ^ { 2 } / \mathbb { Z } _ { 3 } { \mathrm { ~ v i a ~ a ~ } } 2 \pi / 3$ rotation about the z-axis.

18. $S _ { 2 } \cup \{ ( 0 , 0 , z ) ~ | ~ - 1 \le z \le 1 \}$

19. $\mathbb { R } ^ { 3 } - \{ ( x , y , 0 ) \mid x ^ { 2 } + y ^ { 2 } = 1 \}$

20. $\mathbb { R } ^ { 2 } - H$ , the Hopf link

21. Prove that the homophony group is trivial.

## 1.6 Mayer Vietoris (Sheet 7)

1. Compute the homology of:

1. $\mathbb { R P } ^ { 2 } = M \cup _ { \partial } D ^ { 2 }$

2. $T ^ { 2 } = S ^ { 1 } \times \dot { S } ^ { 1 } = ( S ^ { 1 } \times I ) \bigcup _ { f } ( S ^ { 1 } \times I )$ where $( x , 0 ) \sim ( x , 1 ) \sim ( \bar { x } , 0 ) \in \mathbb { C }$

3. $S ^ { 1 } \bigcup _ { f } B ^ { 2 }$ attached along $\partial \dot { B } ^ { 2 }$ using $z \mapsto z ^ { n }$

2. Show ${ \tilde { H } } _ { i } ( \Sigma X ) \cong { \tilde { H } } _ { i - 1 } ( X )$

1. Show $\Sigma S ^ { n } \cong S ^ { n + 1 }$

3. For $f : S ^ { n } \odot$ , show deg $\boldsymbol { f } = \deg \boldsymbol { \Sigma } \boldsymbol { f }$

1. Conclude $\pi _ { n } ( S ^ { n } ) = \mathbb { Z }$

4. Let $\left\{ A _ { i } \right\} ^ { n } \in \mathbf { A b }$ be finitely generated, show $\exists X \mid H _ { i } ( X ) \cong A _ { i }$ for $i \leq n$ and 0 otherwise.

5. Suppose $\textstyle X = \bigcup _ { i } ^ { n } A _ { i }$ such that for any $1 \leq k \leq n , \ \cap _ { i } ^ { k } A _ { i }$ is either empty or contractible, show $i \geq n - 1 \implies \tilde { H } _ { i } ( X ) = 0$ and that this bound is sharp.

6. Compute $H _ { * } ( X \times S ^ { n } )$ in terms of $H _ { * } ( X )$

1. Compute $H _ { * } ( T ^ { n } )$

7. Let $M = ( S ^ { 1 } \times B ^ { 2 } ) \bigcup _ { \mathrm { i d } _ { \partial } } ( S ^ { 1 } \times B ^ { 2 } )$ and compute $H _ { * } ( M ; \mathbb { Z } )$

8. Let $X = S ^ { n } \times I$ with its ends glued together by a map $S ^ { n } \cup$ of degree d, calculate $H _ { * } ( X )$

9. Compute H∗(X) for $X = S ^ { 3 } - N$ , with N a knotted solid torus and $\partial N = T$ its boundary torus

10. Let CA be the cone on A, show that ${ \tilde { H } } _ { * } ( X \cup C A ) \cong { \tilde { H } } _ { * } ( X , A )$

11. Show that the Mayer-Vietoris sequence is natural, i.e. If $X ~ { \stackrel { f } { \to } } ~ Y$ where $f ( A ) \subset C$ and $f ( B ) \subset D$ , then this commutes:

$$
H _ { n } ( X ) \ \longrightarrow H _ { n } ( A \cap B ) \ \longrightarrow H _ { n } ( A ) \oplus H _ { n } ( B ) \ \longrightarrow \ H _ { n - 1 } ( X )
$$

$$
\Bigg \downarrow f _ { * } = \frac { 1 } { 2 } \Bigg \downarrow f _ { * } = \frac { 1 } { 2 } \Bigg \downarrow f _ { * } f _ { * } = \frac { 1 } { 2 } \Bigg \downarrow f _ { * }
$$

$$
H _ { n } ( Y ) \ \longrightarrow H _ { n } ( C \cap D ) \longrightarrow H _ { n } ( C ) \oplus H _ { n } ( D ) \longrightarrow H _ { n - 1 } ( Y )
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

10. Describe a CW complex structure for the lens space $L ( p , 1 )$ and compute $\pi _ { 1 } , H ,$ ∗ for it.

## 1.8 Degree

1. Let $\textstyle p ( x ) = \sum _ { i } ^ { n } a _ { i } x ^ { i }$ , view $p : \mathbb { C } \cup \infty \odot$ and determine its topological degree

2. Let $p ( z ) = { \frac { \prod _ { i } ^ { n } z - a _ { i } } { \prod _ { i } ^ { m } z - b _ { j } } }$ with all $a _ { i } , b _ { j }$ distinct. What is its topological degree?

3. Show that if ${ \bf \bar { \Psi } } f : S ^ { m } \to S ^ { n }$ and $\exists U \subset S ^ { m }$ such that $f | _ { U } \cong f ( U )$ , then $m = n$ and f is surjective.

## 1.9 Universal Coefficient Theorem (Sheet 10)

1. Identify the following groups up to isomorphism

1. $\mathbb { Z } _ { m } \otimes \mathbb { Z } _ { n }$

2. $\mathbb { Z } _ { 6 0 } ^ { 4 } \otimes \left( \mathbb { Z } _ { 2 4 } ^ { 3 } \oplus \mathbb { Z } _ { 8 } ^ { 4 } \oplus \mathbb { Z } _ { 1 2 0 } \right)$

3. $\mathbb { Z } _ { n } \otimes \mathbb { Q }$

4. $\left( \mathbb { Z } \oplus \mathbb { Z } _ { n } \right) \otimes \left( \mathbb { Q } / \mathbb { Z } \right)$

2. Compute:

1. $\mathrm { T o r } ( \mathbb { Z } \oplus \mathbb { Z } _ { 2 } \oplus \mathbb { Z } _ { 8 } , \mathbb { Z } \oplus \mathbb { Z } _ { 4 } \oplus \mathbb { Z } _ { 4 } )$

2. $\mathrm { E x t } ( \mathbb { Z } \oplus \mathbb { Z } _ { 2 } \oplus \mathbb { Z } _ { 3 } , \mathbb { Z } \oplus \mathbb { Z } _ { 4 } \oplus \mathbb { Z } _ { 5 } )$

3. Compute the following directly from chain complexes and check using UCT:

1. $H _ { * } ( \mathbb { R P } ^ { n } ; \mathbb { Z } _ { 2 } )$

2. $H _ { * } ( \mathbb { R P } ^ { n } , \mathbb { Z } _ { 3 } )$

3. $H ^ { * } ( \mathbb { R P } ^ { n } , \mathbb { Z } _ { 6 } )$

4. For any space X, show that $H ^ { 1 } ( X )$ is free abelian

5. Show that $H _ { * } ( X ; \mathbb { Q } ) = H _ { * } ( X ; \mathbb { Z } ) \otimes \mathbb { Q } \ H ^ { * } ( X ; \mathbb { Z } ) = \mathrm { h o m } ( H _ { * } ( X ; \mathbb { Z } ) , \mathbb { Q } )$

6. Construct a space X such that $H _ { * } ( X ; \mathbb { Z } ) = ( \mathbb { Z } , \mathbb { Z } _ { 6 } , \mathbb { Z } _ { 1 2 } , \mathbb { Z } \oplus \mathbb { Z } _ { 4 } , 0 \cdot \cdot \cdot )$ Compute $H ^ { * } ( X ; \mathbb { Z } )$

7. Compute $H _ { * } ( \mathbb { R P } ^ { 2 } \times \mathbb { R P } ^ { 2 } ; \mathbb { Z } _ { 2 } )$

8. Compute $H _ { * } ( \Sigma \mathbb { R P } ^ { 2 } \times \mathbb { R P } ^ { 2 } ; \mathbb { Z } )$

9. Compute $H _ { * } ( \mathbb { R P } ^ { 2 } \times \mathbb { R P } ^ { 3 } ; \mathbb { Z } )$

10. Let G be a topological group. Show that $H _ { * } ( G )$ is an algebra. Show that $G \cap H _ { * } ( G )$ , which factors through the homomorphism $G \to \pi _ { 0 } ( G )$ yielding a trivial action if G is path-connected.

## 1.10 Homological Algebra (Sheet 11)

1. Show that ker $A \to A \otimes \mathbb { Q }$ given by $a \mapsto a \otimes 1$ is the torsion subgroup of A.

2. Show that $A \hookrightarrow B \implies A \otimes \mathbb { Q } \hookrightarrow B \otimes \mathbb { Q }$

3. Find a free resolution of Q as a Z-module.

4. Compute Tor(Q, A)

1. Compute $\operatorname { T o r } ( \mathbb { Q } / \mathbb { Z } , A )$

5.

6. Let $R = \mathbb { Z } [ x , y ]$ , and $M = R / ( x - y ) , N = R / ( x , y )$ . Construct free resolutions of M, N to compute:

$\mathrm { E x t } _ { R } ^ { * } ( M , M )$

$\mathrm { E x t } _ { R } ^ { * } ( M , N )$

$\mathrm { E x t } _ { R } ^ { * } ( N , M )$

$\mathrm { E x t } _ { R } ^ { * } ( N , N )$

7. Let $\Lambda _ { * }$ be the exterior algebra generated by the symbols $\{ d x _ { i } \} ^ { n }$ over a field k. Show that letting $d = \cdot \vee d x _ { 1 }$ yields a chain complex $0 \to \Lambda ^ { 0 } \to \Lambda ^ { 1 } \to \dots \to \Lambda ^ { n } \to 0$ with trivial homology. Compute what happens when dx1 is replaced with an arbitrary non-zero element in $\Lambda ^ { 1 }$ .

8. Define M as the group ring $R = \mathbb { Z } [ \mathbb { Z } _ { 2 } ]$ with the action $( \cdot ) \times - 1$ . Construct a free resolution of M and compute $\operatorname { T o r } _ { R } ^ { * } ( M , M )$

9. Show $\operatorname { T o r } _ { R } ^ { * } ( \cdot , \cdot )$ is symmetric in the following way: Given M, N , take free resolutions, view $M _ { * } \to M$ as a chain map and tensor with $N _ { * }$ to get a chain mapψ $: M _ { * } \otimes _ { R } N _ { * } \to M \otimes _ { R } N _ { * }$ Show that ψ is a quasi-isomorphism using the exact sequence $0  ( Z _ { n } , 0 )  ( N _ { n } , 0 ) $ $( B _ { n - 1 } , 0 ) \to 0$ , then switch the roles of $M , N$

10. Prove that for a $\mathrm { S E S ~ 0 }  A  B  C .$ , the group $\operatorname { E x t } ( C , A )$ classifies extensions of C by A up to isomorphism.

## 1.11 Cohomology Ring (Sheet 12)

Todo

## 2 Topology Problems: Solutions

## 2.1 Homotopy

1. Main Idea: A linear homotopy projected onto the sphere works.

Let $f : X \to S ^ { n } \subset \mathbb { R } ^ { n + 1 }$ be an arbitrary map that fails to be surjective. Then, by definition, there is at least one point $s _ { 0 } \in S ^ { n } - f ( X )$ .

Then, $\forall x \in X$ , since $f ( x ) \neq s _ { 0 }$ , there is a unique geodesic C connecting $f ( x )$ and $s _ { 0 }$ . So a variant of the straight line homotopy will work, by interpolating between $f ( x )$ and $s _ { 0 }$ along C.

So let $H : X \times I \to S ^ { n }$ be defined by $H ( x , t ) = P ( t s _ { 0 } + ( 1 - t ) f ( x ) )$ , where $P : \mathbb { R } ^ { n + 1 }  S ^ { n }$ is given by $P ( x ) = x / \| x \|$ . This is well defined, since the denominator is zero iff $f ( x ) = s _ { 0 }$ , which by assumption is not the case. This is a homotopy, since $H ( x , 0 ) = P ( f ( x ) ) = f ( x )$ (since P fixes $S ^ { n } )$ and $H ( x , 1 ) = P ( s _ { 0 } ) = s _ { 0 }$ (since $s _ { 0 } \in S ^ { n } )$ .

2. Main Idea: Exact same idea as 1, just a more complicated check.

Take $H ( x , t ) = P ( t f ( x ) + ( 1 - t ) g ( x ) )$ This is well defined; the only case to check is when the denominator is zero. But kxk = 0 iff $x = 0$ , which would imply $t f ( x ) + ( 1 - t ) g ( x ) = 0$ and so $t f ( x ) = - ( 1 - t ) g ( x )$

Taking norms and observing that since $f , g \in S ^ { n } \implies \| f \| = \| g \| = 1$ , this forces $t = 1 - t$ and thus $t = 1 / 2$ . But this would force $( 1 / 2 ) f ( x ) = ( - 1 / 2 ) g ( x )$ and thus $f ( x ) = - g ( x )$ , which we assumed was not the case.

3. Main Idea: Linear homotopy fails continuity without the condition from (2), so use complex embedding to avoid the origin at $t = 1 / 2$

Suppose n is odd and define $f : S ^ { n } \to S ^ { n }$ to be the antipodal map. Since $n + 1$ is even, we have $n + 1 = 2 m$ for some $m \in \mathbb { N }$ , so identify $S ^ { n } = S ^ { 2 m - 1 } \subset \mathbb { R } ^ { 2 m } \cong \mathbb { C } ^ { m }$

Then $z \in S ^ { n }$ can be written as a vector $z \in \mathbb { C } ^ { m }$ such that $\| z \| = 1$

Then define $P : \mathbb { C } ^ { m }  \mathbb { C } ^ { m }$ by $P ( z ) = z / | z |$ , the projection onto the complex unit sphere, and define $\boldsymbol { H } : \mathbb { C } ^ { m } \times \boldsymbol { I }  \mathbb { C } ^ { m }$ by $H ( z , t ) = P ( e ^ { i \pi t } z )$

This is a homotopy, since $H ( z , 0 ) = P ( z ) = z { \mathrm { ~ } } ( { \mathrm { s i n c e ~ } } \| z \| = 1 )$ , so this is the identity map. We also have $H ( z , 1 ) = P ( - z ) = - z$ , the antipodal map.

This is well-defined, since $e ^ { i \pi t } > 0$ and $z \neq 0$ , so the linear homotopy in ambient $\mathbb { C } ^ { m }$ avoids the origin and thus the denominator when taking the projection is never zero.

4. ⇐: Main Idea: Projection and inclusion are homotopy inverses. One composition is equality, the other is just equality up to homotopy, but that’s all we need!

Suppose $\operatorname { i d } _ { X }$ is nullhomotopic.

Then there exists some constant map $g : X  \{ x _ { 0 } \}$ for some $x _ { 0 } \in X$ where $g ( x ) = x _ { 0 }$ and $g \simeq \operatorname { i d } _ { X }$ This means there is some homotopy $F : X \times I  X$ such that $F ( x , 0 ) = \mathrm { i d } _ { X } ( x ) = x$ and $F ( x , 1 ) =$ $g ( x ) = x _ { 0 }$ for all $x \in X$ .

So let $p : X  \{ x _ { 0 } \}$ be the projection map sending every point to $x _ { 0 }$ , and $\iota : \{ x _ { 0 } \} \to X$ be the inclusion. We will show that the two compositions are homotopy inverses, from which it follows that $X \ \simeq \ \{ x _ { 0 } \}$ This means that X is homotopy-equivalent to a point, and thus by definition contractible.

Then $( p \circ \iota ) : \{ x _ { 0 } \}  \{ x _ { 0 } \}$ is given by $p ( \iota ( x _ { 0 } ) ) = p ( x _ { 0 } ) = x _ { 0 }$ , so this is the identity on the target space {x0}.

Similarly, $( \iota \circ p ) : X \to X$ is given by $\iota ( p ( x ) ) = \iota ( x _ { 0 } ) = x _ { 0 }$ , so this is the constant map on X mapping every point from X to x0. But then this map is exactly g, and by assumption this is homotopic to the identity on X

But then we have $p \circ \iota \simeq \operatorname { i d } _ { \{ x _ { 0 } \} }$ and $\iota \circ p \simeq \operatorname { i d } _ { X }$ , so they are homotopy inverses.

⇒: Main Idea: One of the homotopy inverses is just a constant map.

Suppose $X \simeq \{ x _ { 0 } \}$ , then there exist a pair of homotopy inverses

$f : X  \{ x _ { 0 } \}$ and $g : \{ x _ { 0 } \} \to X$ such that $f \circ g \simeq \operatorname { i d } _ { \{ x _ { 0 } \} }$ and $g \circ f \simeq \operatorname { i d } _ { X }$

Since {x0} is a single point space, f is necessarily a constant map $( { \mathrm { i . e . ~ } } f ( x ) = x _ { 0 }$ for every $x \in X . )$ But then $( g \circ f ) ( x ) = g ( x _ { 0 } ) = y _ { 0 }$ for some constant $y _ { 0 } \in X$ , so $g \circ f$ is a constant map. By assumption, $g \circ f \simeq \operatorname { i d } _ { X }$ , so the identity is homotopic to a constant map.

5. Main Idea: Deformation retract M onto its center circle; two spaces that deformation retract onto a common space are themselves homotopy equivalent.

Claim: $S ^ { 1 } \times I \simeq S ^ { 1 } \times \{ * \}$ This is because I is contractible, so $I \simeq \{ * \}$ . (Maybe needs further proof)

Claim: $M \simeq S ^ { 1 } \times \{ * \}$

If both of these claims hold, then we will have $M \simeq S ^ { 1 } \times I$ as two spaces that deformation retract onto a common space. Identifying $M = I \times I / \sim$ where $( x , 0 ) \sim ( 1 - x , 1 )$ , fix $x = 1 / 2$

Then consider the subspace $U = \{ ( 1 / 2 , y ) \mid y \in [ 0 , 1 ] \} \subset M$ . Claim: $U \cong \{ * \} \times S ^ { 1 }$ for some point ∗.

U can be written $\{ 1 / 2 \} \times ( I / \sim )$ , and since $( 1 / 2 , 0 ) \sim ( 1 / 2 , 1 )$ , we have $I / \sim I / \partial I \cong S ^ { 1 }$ , so $U \cong \{ 1 / 2 \} \times S ^ { 1 }$ as desired $\begin{array} { r } { ( \mathrm { t a k i n g } * = \frac { 1 } { 2 } ) } \end{array}$

However, we can define a homotopy from M onto U, in the form of a deformation retract.

Let $F : M \times I \to M$ be defined by $F ( ( x , y ) , t ) = F _ { t } ( x , y ) = ( ( 1 - t ) x + { \textstyle \frac { 1 } { 2 } } t , y )$ . Then $F ( ( x , y ) , 0 ) =$ $( x , y ) = \operatorname { i d } _ { M }$ , and $F ( ( x , y ) , 1 ) = ( { \frac { 1 } { 2 } } , y ) \subseteq U$ . Moreover, if $( x , y ) \in U ,$ then $\left( x , y \right) = \left( { \textstyle { \frac { 1 } { 2 } } } , y \right)$ and $\begin{array} { r } { F ( ( x , y ) , t ) = ( ( 1 - t ) \frac { 1 } { 2 } + \frac { 1 } { 2 } t , y ) = ( \frac { 1 } { 2 } - t \frac { 1 } { 2 } + \frac { 1 } { 2 } t , y ) = ( \frac { 1 } { 2 } , y ) = ( x , y ) } \end{array}$ , so $F = \mathrm { i d } _ { U }$ . This makes $F { \mathrm { ~ a ~ } }$ deformation retract from M onto U , and so $M \simeq U$

But then, summarizing our results, we have $S ^ { 1 } \times I \simeq S ^ { 1 } \times \{ * \} \cong S ^ { 1 } \times \Big \{ \frac { 1 } { 2 } \Big \} = U \simeq M$ , and so $S ^ { 1 } \times I \simeq M$ as desired.

6. Main Idea: Using a funky deformation retract. See Hatcher, PDF page 55, Example 1.23. Add picture!!

Deformation retract

$R ^ { 3 } - S ^ { 1 }$ onto $S ^ { 2 } - U$ , where U is a diameter inside $S ^ { 2 }$ also passing through the middle of $S ^ { 1 }$ in the interior. This can be done by moving points outside of $S ^ { 2 }$ towards the surface, and points inside

$S ^ { 2 }$ just move away from the $S ^ { 1 }$ inside (either towards $U$ or towards the surface of $S ^ { 2 }$ , so they don’t hit $S ^ { 1 } )$

Then take a geodesic between the endpoints of the diameter on $S ^ { 2 }$ , pick any point p on the geodesic, and move both diameter points towards it. This yields $S ^ { 2 } \vee S ^ { 1 }$ at the point p.

7. Main Idea: Nothing to it. Homotopy:

8. $A \simeq \Delta \simeq S ^ { 1 }$

9. $a \simeq d \simeq o \simeq S ^ { 1 }$

10. $B \simeq 8 \simeq S ^ { 1 } \vee S ^ { 1 }$

11. $b \simeq o \simeq S ^ { 1 }$

12. $C \simeq *$

13. $c \simeq l \simeq *$

14. $D \simeq S ^ { 1 }$

15. $d \simeq o \simeq S ^ { 1 }$

16. $E \simeq *$

17. $e \simeq d \simeq S ^ { 1 }$

18. $F \simeq *$

19. $f \simeq *$

20. $G \simeq *$

21. $g \simeq 8 \simeq S ^ { 1 } \vee S ^ { 1 }$

22. $H \simeq *$

23. $h \simeq l \simeq *$

24. $I \simeq *$

25. $i \simeq \{ * _ { 1 } , * _ { 2 } \}$

26. $J \simeq *$

27. $j \simeq i \simeq \{ * _ { 1 } , * _ { 2 } \}$

28. $K \simeq *$

29. $L \simeq *$ $1 . \ l \simeq *$

30. $M \simeq *$ $1 , \ m \simeq *$

31. $N \simeq *$ 1. $n \simeq *$

32. $O \simeq S ^ { 1 }$

$$
1 . \ o \simeq S ^ { 1 }
$$

33. $P \simeq D \simeq S ^ { 1 }$

$$
1 . ~ p \simeq P \simeq S ^ { 1 }
$$

34. $Q \simeq O \simeq S ^ { 1 }$

$$
1 . \ q \simeq p \simeq o \simeq S ^ { 1 }
$$

35. $R \simeq D \simeq S ^ { 1 } .$

$$
1 . \ r \simeq l \simeq S ^ { 1 }
$$

36. $S \simeq *$

$$
1 . \ s \simeq S \simeq *
$$

37. T ' ∗

$$
1 . \ t \simeq l \simeq *
$$

38. $U \simeq *$

$$
1 . \ u \simeq U \simeq *
$$

39. $V \simeq *$

$$
1 . \ v \simeq V \simeq *
$$

40. $W \simeq *$

$$
1 . \ w \simeq W \simeq *
$$

41. $X \simeq *$

$$
1 . \ x \simeq X \simeq *
$$

42. $Y \simeq *$

$$
1 . ~ y \simeq v \simeq *
$$

43. $Z \simeq *$

$$
1 . ~ z \simeq Z \simeq *
$$

This results in a partition of the alphabet into the following homotopy types:

$$
\{ A , D , O , P , Q , R , S ^ { 1 } \} \cup \{ a , b , d , e , g , o , p , q \}
$$

$$
\{ C , E , F , G , H , I , J , \bar { K } , L , M , N , S , T , U , V , W , X , Y , Z , * \} \cup \{ c , f , h , k , l , m , n , r , s , t , u , v , w , x , y , z \}
$$

$\{ B , S ^ { 1 } \lor S ^ { 1 } \}$

$\{ i , j , \{ * , * \} \}$

Homeomorphisms: ignore ligatures!!

1. $\{ A , R \}$ Can remove a point to obtain two components homeomorphic to $\{ I , F \}$ respectively.

2. $\{ D , O , S ^ { 1 } \}$ These all have no single point that can be removed to disconnect the space.

3. $\{ B , S ^ { 1 } \lor S ^ { 1 } \}$ Remove point at junction

4. $\{ C , G , I , J , L , M , N , S , U , V , W , Z , [ 0 , 1 ] \}$ These all have a point that can be removed to yield two components, but no points that yield three. (Intuitively, all can be obtained by twisting a straight wire.)

5. $\left\{ E , F , T , Y , \bigvee _ { i = 1 } ^ { 3 } [ 0 , 1 ] \right\}$ These all have a point that can be removed to yield 3 connected components homeomorphic to I. This is the “pasting” point in the vee.

6. $\left\{ H , K , \bigvee _ { i = 1 } ^ { 5 } [ 0 , 1 ] \right\}$ Can remove two points to disconnect each into five components.

7. $\{ P , Q , S ^ { 1 } \lor [ 0 , 1 ] \}$ Both contain a nontrivial loop.

8. $\left\{ X , \mathsf { V } _ { i = 1 } ^ { 4 } [ 0 , 1 ] \right\}$ Can remove one point to separate into four components.

9. Main Idea: Show that both spaces are a deformation retract of the same space. (See Hatcher, Proposition 0.18, p. 25)

Suppose we have the following maps

$$
\begin{array} { r } { f : S ^ { 1 } \to X } \\ { g : S ^ { 1 } \to X } \end{array}
$$

where $f \simeq g$ . Then there exists a homotopy

$$
H : S ^ { 1 } \times I \to X
$$

such that $H ( z , 0 ) = f ( z )$ and $H ( z , 1 ) = g ( z )$

Then define

$$
\begin{array} { l } { P : = X \displaystyle \prod _ { f } B ^ { 2 } } \\ { Q : = X \displaystyle \prod _ { g } B ^ { 2 } } \end{array}
$$

We want to that P and $Q$ are homotopy-equivalent. In order to do so, we will construct a larger space which deformation retracts onto both P and $Q _ { i }$ , which is a homotopy equivalence.

With H in hand, we can define the space $R = X \amalg _ { H } B ^ { 2 } \times I ,$ where we recognize $S ^ { 1 } = \partial B ^ { 2 }$ . In particular, $S ^ { 1 }$ is a subspace of $B ^ { 2 }$

Claim: Both P and $Q$ are subspaces of R. Since $H ( z , 0 ) = f ( z )$ . So considering $\begin{array} { r } { X \left[ \right] _ { H } B ^ { 2 } \times \left\{ 0 \right\} \cong } \end{array}$ $\begin{array} { r } { X [ \bigl \mathrm { I } _ { f } B ^ { 2 } = P } \end{array}$ . A similar argument holds at the point $1 \in I .$ (Not a strong argument)

But note that $B ^ { 2 } \times I$ is a solid cylinder, and so can be deformation retracted onto the outer shell plus one of the “lids”. Formally, this would be given by $S ^ { 1 } \times I \cup B ^ { 2 } \times \{ p \}$ for some $p \in [ 0 , 1 ]$

Claim: choosing $p = 0$ induces a deformation retract of R onto $P ,$ and choosing $p = 1$ induces a deformation retract of R onto $Q$

Proof: ?

## 2.2 Fundamental Group

1. Main idea: just algebraic manipulations using the $\pi _ { 1 }$ functor and unravelling definitions.

Let X be path connected and simply connected, and let $x , y \in X$ be two arbitrary points. Then consider two paths, $\gamma : I  X , \gamma ( 0 ) = x , \gamma ( 1 ) = y \alpha : I  X , \alpha ( 0 ) = x , \alpha ( 1 ) = y .$

We would like to show $\gamma \simeq \alpha$ . Since X is simply connected, we know that $\pi _ { 1 } ( X ) = 0$ . This means that for any $a , b \in \pi _ { 1 } ( X ) , a = b = e ,$ the identity element in this group.

So we construct two loops: one as $\gamma \bar { \alpha }$ , the other as $\alpha \bar { \gamma }$ . Apply the $\pi _ { 1 }$ functor yields $[ \gamma \bar { \alpha } ] = e =$ $[ c _ { x } ] = [ \alpha \bar { \gamma } ]$ , where $[ c _ { x } ]$ is the equivalence class of the constant path at x, and equivalently the identity element in $\pi _ { 1 } ( X )$ . Lemma: If $f \simeq g$ , then $f \circ h \simeq g \circ h$ for any h.

But this says $\gamma \bar { \alpha } \simeq c _ { x }$ and $\alpha \bar { \gamma } \simeq c _ { x }$ . But $\gamma \simeq c _ { x } \circ \gamma \simeq ( \alpha \bar { \gamma } ) \circ \gamma \simeq \alpha \circ ( \bar { \gamma } \circ \gamma ) \simeq \alpha$ , which is what we desired.

2. Main Idea Homotopies on maps $S ^ { 1 } \to X$ are cylinders, find a way to continuously map a cylinder onto a disk given the existence of such a homotopy. Let X be path connected, $\pi _ { 1 } ( X ) = 0$ , and let $f : S ^ { 1 } \to X$ be arbitrary. Then $f ( S ^ { 1 } ) \subseteq X$ is a path in X, and since $\pi _ { 1 } ( X ) = 0$ , this path is homotopic to a point $x _ { 0 }$ . So f is homotopic to the constant map $c _ { x _ { 0 } } : S ^ { 1 } \to X , z \mapsto x _ { 0 }$

So let $H : S ^ { 1 } \times I \to X$ be this homotopy. We know that $H ( z , 0 ) = f ( z )$ and $H ( z , 1 ) = c _ { x _ { 0 } } ( z ) = x _ { 0 }$ Claim: Consider quotient $\frac { S ^ { 1 } \times I } { S ^ { 1 } \times \{ 1 \} }$ with the projection map $p : S ^ { 1 } \times I  S ^ { 1 } \times \{ 1 \}$ . Then H factors through the quotient uniquely $\mathrm { \left( w h y ? \right) }$ , and there exists a unique $\hat { H }$ making this diagram commute: This follow from the universal property of the quotient in Top, where it is sufficient that H is constant on $S ^ { 1 } \times \{ 1 \}$ - but this is exactly what was deduced above.

However, the quotient object constructed is homeomorphic to $D ^ { 2 }$ , as per the following diagram

Here, we just recognize that $S ^ { 1 } \times I$ is a cylinder, and quotienting at the $t = 1$ point in I simply collapses the top portion of the cylinder to a point, forming a cone. We then take the flattening map to just project every point on the cone directly downwards onto the base circle, yielding $D ^ { 2 }$

(Note: I guess this map can be constructed as $\Phi : S ^ { 1 } \times I  D ^ { 2 }$ where $\Phi ( z , t ) = z ( 1 - t )$ . Since $t = 1$ on $S ^ { 1 } \times \{ 1 \} , \Phi ( z , 1 ) = 0$ and this is exactly the kernel of Φ. Continuous as product of continuous functions, need to check injective/surjective and show inverse is continuous.)

Need to check injective/surjective, show that kernel is $S ^ { 1 } \times 1$ , then use first isomorphism theorem.) But then $\hat { H }$ is exactly a continuous map from $D ^ { 2 } \to X$ , as desired.

$3 . \Rightarrow$ Let $[ \alpha ] \ \in \ \pi _ { 1 } ( X \times Y , ( x _ { 0 } , y _ { 0 } ) )$ be an arbitrary loop in $X \times Y$ Then α is equivalently a map S1 → X × Y . Considering $S ^ { 1 }$ to be a subset of $\mathbb { R } ^ { 2 } .$ , we can parameterize α as $\alpha ( z ) = \alpha ( x + i y ) = ( \alpha _ { x } ( x ) , \alpha _ { y } ( y ) )$ in components. In particular, since α is continuous, so are $\alpha _ { x } , \alpha _ { y }$ Moreover, since $\alpha ( 0 ) = \alpha ( 0 + i 0 ) = ( x _ { 0 } , y _ { 0 } )$ , we have $\alpha _ { x } ( 0 ) = x _ { 0 } , \alpha _ { y } ( 0 ) = y _ { 0 }$ (Note: alternatively, given the product, we have projections $p _ { X } , p _ { y }$ , so we can define the map $\alpha \mapsto ( p _ { X } \circ \alpha , p _ { Y } \circ \alpha ) )$

But then $\alpha _ { x } : S ^ { 1 } \to X$ and $\alpha _ { y } : S ^ { 1 } \to Y$ are loops entirely in X, Y at the respective base points, and so we can define the map $F : \pi _ { 1 } ( X \times Y , ( x _ { 0 } , y _ { 0 } ) ) \to \pi _ { 1 } ( X , x _ { 0 } ) \times \pi _ { 1 } ( Y , y _ { 0 } ) { \mathrm { ~ b y ~ } } [ \alpha ] = [ ( \alpha _ { x } , \alpha _ { y } ) ] \mapsto \pi _ { 1 } ( X , y ) .$ $\left( \left[ \alpha _ { x } \right] , \left[ \alpha _ { y } \right] \right)$

<!-- image-->  
Figure 1: universal1

<!-- image-->  
Figure 2: 2017-11-24 14_59_29-Untitled page - OneNote

This is injective, since $( [ a ] , [ b ] ) = ( [ c ] , [ d ] )$ on the RHS means that $[ a ] = [ c ] , [ b ] = [ d ]$ in the fundamental groups, and thus $a \simeq c , b \simeq d$ in the spaces. We want to show that $[ ( a , b ) ] = [ ( c , d ) ]$ , which would follow if $\alpha ( x + i y ) = ( a ( x ) , b ( y ) ) \simeq \beta ( x + i y ) = ( c ( x ) , d ( y ) )$ in $X ~ \times Y , . . . ?$

This is surjective, because if $( [ a ] , [ b ] )$ are elements in the right-hand side, then $a ( 0 ) = a ( 1 ) = x _ { 0 }$ and $b ( 0 ) = b ( 1 ) = y _ { 0 }$ , so we can consider $( a , b ) : I \to X \times Y$ where $( a , b ) ( z ) = ( a , b ) ( x + i y ) =$ $( a ( x ) , b ( y ) )$ . This is then a loop in $X \times Y$ , since $( a , b ) ( 0 ) \ : = \ : ( a ( 0 ) , b ( 0 ) ) \ : = \ : ( 0 , 0 ) \ : = \ : ( x _ { 0 } , y _ { 0 } )$ and similarly $( a , b ) ( 1 ) = ( a ( 1 ) , b ( 1 ) ) = ( x _ { 0 } , y _ { 0 } )$ . So this is actually a map $( a , b ) : S ^ { 1 } \to X \times Y$ , or in other words, a loop in $X \times Y$ based at $( x _ { 0 } , y _ { 0 } )$ , which lifts to an element of the fundamental group on the LHS.

Maps in both directions are continuous, since a vector function is continuous iff its component functions are continuous.

This is well-defined, due to the fact that if $a \simeq b .$ , then $p _ { X } \circ a \simeq p _ { X } \circ b$ , and $\boldsymbol { F } = \left( f _ { x } , f _ { y } \right)$ is a homotopy iff its components functions are homotopies.

4. Let $A = S ^ { n } - \left\{ n _ { p } = { \mathrm { N o r t h ~ P o l e } } \right\} , B = S ^ { n } - \left\{ s _ { p } = { \mathrm { S o u t h ~ P o l e } } \right\}$ . Then $A \cup B \ : = \ : S ^ { n }$ and $A \bigcap B = S ^ { n } - \left\{ n _ { p } , s _ { p } \right\}$ . Since A, B are open and path connected, we can apply van Kampen’s theorem to obtain $\pi _ { 1 } ( X ) = \pi _ { 1 } ( A ) * \pi _ { 1 } ( B )$ amalgamated over $\pi _ { 1 } ( A \cap B )$ . But $A \cong \mathbb { R } ^ { n } \cong B$ via stereographic projection, and since $\mathbb { R } ^ { n }$ is contractible, $\pi _ { 1 } ( \mathbb { R } ^ { n } ) = 0 = \pi _ { 1 } ( A ) = \pi _ { 1 } ( B )$ . So $\pi _ { 1 } ( X ) = 0 * 0 = 0$ as desired.

This follow because we can compute $A \cap B \cong \mathbb { R } ^ { n } - \{ { \mathrm { p t } } \} \cong S ^ { n } - 1$ , and so $\pi _ { 1 } ( A \cap B ) = \pi _ { 1 } ( S ^ { n } ) \times$ $\pi _ { 1 } ( \mathbb { R } ^ { 1 } ) = 0 \times 0 = 0 .$ , and so has the presentation $\pi _ { 1 } ( A \cap B ) = \left. w \mid w ^ { 1 } = e \right.$ . We can then look at the inclusions $i : A \cap B \to A j : A \cap B \to B$ and the induced homomorphisms $I : \pi _ { 1 } ( A \cap B ) \to \pi _ { 1 } ( A ) \ J$ : $\pi _ { 1 } ( A \cap B ) \to \pi _ { 1 } ( B )$ . But since both sides in both maps are trivial, these are constant maps between identities. We can then present the group $0 = \pi _ { 1 } ( A ) = \langle a \mid a ^ { 1 } = e \rangle$ and since $I ( w ) J ( w ) ^ { - 1 } = e e ^ { - 1 } =$ $e ,$ we have $\pi _ { 1 } ( B ) = \langle b \mid b ^ { 1 } = e \rangle , \mathrm { s o } \pi _ { 1 } ( A ) * _ { \pi _ { 1 } ( A \cap B ) } \pi _ { 1 } ( B ) = \langle a , b \mid a ^ { 1 } = b ^ { 1 } = e \rangle$

(See https://en.wikipedia.org/wiki/Seifert%E2%80%93van_Kampen_theorem for presentation of amalgamated product)

5. WLOG, assume $p _ { 0 } , p _ { 1 }$ are the north and south poles of $S ^ { 2 }$ . We can then form a deformation retract of X onto the equator of $S ^ { 2 }$ , which is equal to $S ^ { 1 }$ . To do $\mathrm { s o } ,$ just move every point x along the unique great circle connecting $x , p _ { 0 } , p _ { 1 }$ , and proceed at linear speed towards the equator. This is well defined at every point on $S ^ { 2 }$ except the poles, which are not included in $X$ and the equator is fixed at every instant. So this forms a deformation retract. Alternatively, use the fact that $\mathbb { R } ^ { n } - \{ \mathrm { p t } \} \cong S ^ { n - 1 } \times$ R via polar coordinates, and $S ^ { n } - \{ \mathrm { p t } \} \cong \mathbb { R } ^ { n }$ by stereographic projection. So $S ^ { 2 } - \{ p _ { 0 } , p _ { 1 } \} \cong \mathbb { R } ^ { 2 } - \{ p _ { 1 } \} \cong S ^ { 1 } \times \mathbb { R }$ . But since R is contractible, the last one is homotopic to $S ^ { 1 } \times \{ 0 \} \cong S ^ { 1 }$ . Alternatively: use the lemma, then $k = 2$ and so $S ^ { 2 } - \{ p _ { 1 } , p _ { 2 } \} \simeq \bigvee _ { i = 1 } ^ { 1 } S ^ { 1 } = S ^ { 1 }$

6. Lemma: $S ^ { n } - \{ p _ { i } \} _ { i = 1 } ^ { k } = \bigvee _ { k - 1 } S ^ { n - 1 } , \mathrm { i . e . ~ } S ^ { n }$ minus k points is equal to $k - 1$ copies of of $S ^ { n - 1 }$ Proof: $S ^ { n } - \{ p _ { 1 } \} \cong \mathbb { R } ^ { n }$ by stereographic projection, so $S ^ { n } - \{ p _ { 1 } , p _ { 2 } \cdot \cdot \cdot p _ { k } \} \cong \mathbb { R } ^ { n } - \{ p _ { 2 } , \cdot \cdot \cdot p _ { k } \}$ WLOG, suppose none of these points are zero (otherwise, take a translation away from zero. This is affine and continuous.) Then $\mathrm { f i x } \ 0$ as the base point, and form $k - 1$ loops $\alpha _ { i } ,$ where the ith loop encircles $p _ { i }$ . Then $\mathbb { R } ^ { n }$ deformation retracts onto $\cup _ { i = 1 } ^ { k - 1 } \alpha _ { i }$ , which is homeomorphic to $\mathsf { V } _ { i = 1 } ^ { k - 1 } S ^ { 1 }$

7. Theorem: $\pi _ { 1 } ( \bigvee _ { i = 1 } ^ { k } S ^ { 1 } ) \cong * _ { i = 1 } ^ { n } \mathbb { Z }$ , the free product of n copies of Z. Proof: By induction, using Van-Kampen’s theorem. Base case: Take $i = 1$ , then $\pi _ { 1 } ( S ^ { 1 } ) = \mathbb { Z }$ as proved in Hatcher.

Inductive step: Suppose this holds for all $k < n$ , then we have $X = \bigvee ^ { n } S ^ { 1 } = \left( \bigvee ^ { n - 1 } S ^ { 1 } \right) \vee S ^ { 1 }$ Let p be the point of common intersection, then let $U = \bigvee ^ { n - 1 } S ^ { 1 } V = S ^ { 1 } \bigcup \{ p \}$

Then $U \bigcup V = X , U \bigcap V = \{ p \}$ , both $U , V$ are path-connected. Since we have $\pi _ { 1 } ( \{ \mathrm { p t } \} ) = 0$ , the amalgamated free product reduces to the usual free product. By the IH, we have $\pi _ { 1 } ( U ) = * ^ { n - 1 } \mathbb { Z }$ so

$$
\pi _ { 1 } ( X ) = \pi _ { 1 } ( U \cup V ) = \pi _ { 1 } ( U ) * \pi _ { 1 } ( V ) = _ { \mathrm { I H } } \left( * ^ { n - 1 } \mathbb { Z } \right) * \pi _ { 1 } ( V ) = ( * ^ { n - 1 } \mathbb { Z } ) * \mathbb { Z } = * ^ { n } \mathbb { Z } .
$$

Definition: Let $F _ { n } : = * ^ { n } \mathbb { Z }$ be the free abelian group on n generators. Lemma: If $n \not = m , F _ { n } \not \cong$ $F _ { m }$ . Proof: If ${ \cal F } ^ { n } \cong { \cal F } ^ { m }$ , then $\mathbb { Z } ^ { n } \cong \mathbb { Z } ^ { m }$ But then tensor both sides with $\mathbb { Z } _ { 2 }$ over $\mathbb { Z } ,$ yielding $\mathbb { Z } ^ { n } \otimes _ { \mathbb { Z } } \mathbb { Z } _ { 2 } \cong Z ^ { m } \otimes _ { \mathbb { Z } } \mathbb { Z } _ { 2 }$ . But the LHS is isomorphic to $( \mathbb { Z } / 2 \mathbb { Z } ) ^ { n }$ , while the RHS is isomorphic to $( \mathbb { Z } / 2 \mathbb { Z } ) ^ { m } . ( W h y . )$ These are both finite groups - there are 2 elements in $\mathbb { Z } / 2 \mathbb { Z }$ , so the first has $2 ^ { n }$ elements and the latter has $2 ^ { m }$ elements. But if $2 ^ { n } = 2 ^ { m }$ , then $n = m$ . The lemma follows from the contrapositive.

Now we have all we need - let $X = S ^ { 2 } - \{ p _ { 1 } , p _ { 2 } \}$ and $Y = S ^ { 3 } - \{ q _ { 1 } , q _ { 2 } \}$ . Then by the previous problems, $X \simeq S ^ { 1 }$ and $Y \simeq S ^ { 2 }$ 2, so if $S ^ { 2 } \cong S ^ { 3 }$ then $X \simeq Y$ and $S ^ { 1 } \simeq S ^ { 2 }$ . But $\pi _ { 1 } ( S ^ { 1 } ) = \mathbb { Z }$ and $\pi _ { 1 } ( S ^ { 2 } ) = 0$ , so $S ^ { 1 } \not \simeq S ^ { 2 }$ , a contradiction.

## 8. Here we go:

9. Let $\alpha ( t ) = e ^ { 2 \pi i t }$ where $t \in [ 0 , 1 ]$ , be a loop in $S ^ { 1 }$ parameterized by t, which goes around $S ^ { 1 }$ exactly once. Then under the map $f : z \mapsto z ^ { n }$ , we obtain $f ( \alpha ( t ) ) = e ^ { 2 \pi n i t }$ where $t \in [ 0 , 1 ]$ This resulting loop then goes around S1 n times, so the induced homomorphism on $\pi _ { 1 } ( S ^ { 1 } ) = \mathbb { Z }$ is the map $f ^ { * } : \mathbb { Z } \to \mathbb { Z }$ given by $f ^ { * } ( a ) = n a$ .

10. Define α as above, and define $f : S ^ { 1 } \to S ^ { 1 }$ to be the antipodal map, so $f ( z ) = - z$ for $z \in S ^ { 1 } \subset \mathbb { C }$ . We then left α to the fundamental group, and define $f _ { * } ( [ \alpha ] ) = [ f \circ \alpha ]$ . Computing, we have $( f \circ \alpha ) ( t ) = f ( \alpha ( t ) ) = - e ^ { 2 \pi i t }$ . Where $\alpha ( 0 ) = \alpha ( 1 ) = 1 + 0 i$ , we have $( f \circ \alpha ) ( 0 ) =$ $( f \circ \alpha ) ( 1 ) = - 1 + 0 i$ . But note that α was a counter-clockwise loop in $S ^ { 1 }$ , and the image of α is also a counter-clockwise loop. So this maps the generator $[ \alpha ] \in \pi _ { 1 } ( S ^ { 1 } , 1 )$ to the generator $[ \alpha ^ { \prime } ] \in \pi _ { 1 } ( S ^ { 1 } , - 1 )$ . But since $S ^ { 1 }$ is path-connected, the fundamental groups at these two base points are isomorphic. Alternatively: the antipodal map on $S ^ { 1 }$ is homotopic to the identity map (since $n = 1$ is odd), so $[ f \circ \alpha ] = [ f ] [ \alpha ] = [ \operatorname { i d } ] [ \alpha ] = [ \alpha ]$ , so the induced homomorphism on $\pi _ { 1 } ( S ^ { 1 } )$ is the identity map.

11. Let $\alpha ( t ) = e ^ { i t }$ where $t \in [ 0 , 2 \pi ]$ be a counter-clockwise loop in $S ^ { 1 }$ ; then [α] generates the fundamental group. Then $\mathbf { \bar { \begin{array} { r } { \bar { f } } { * } ( [ \bar { \alpha } ] ) } = [ ( f \circ \alpha ) ( t ) ] = [ e ^ { i t } \mapsto e ^ { 2 \pi i \sin t } ] } \end{array}$ . Then just consider how sin behaves in each quadrant. In quadrant 1, as t ranges from $0 , \pi / 2$ then sin t ranges from 0 to 1, so α is exactly traced out. In quadrant two, α¯ is traced out, since sin t decreases from 1 to 0. This happens again in the bottom quadrants, so we have $f ^ { * } ( [ \alpha ] ) = [ \alpha \bar { \alpha } \alpha \bar { \alpha } ] =$ $[ \alpha ] [ \alpha ] ^ { - 1 } [ \alpha ] [ \alpha ] ^ { - 1 } = [ \mathrm { i d } ]$ . But the identity element in Z is 0, so the induced homomorphism on Z is $f ^ { * } ( a ) = 0$ , the homomorphism sending everything to 0.

12. From complex analysis, $W ( f ( \alpha ( t ) ) ) = Z _ { f } - P _ { f } = 4 - 1 = 3$ . No idea how to approach with induced maps on the fundamental group of $S ^ { 1 } \mathrm { o r } \mathbb { C } - \{ 0 \}$

13. Let M be the mobius strip, identified as $I \times I / ( t , 0 ) \sim ( 1 - t , 1 )$ , and let $\begin{array} { r } { x _ { 0 } = [ ( 1 , \frac { 1 } { 2 } ) ] = [ ( 0 , \frac { 1 } { 2 } ) ] } \end{array}$ Let X be the line $( t , \textstyle { \frac { 1 } { 2 } } )$ for $t \in I ;$ ; by the identification of the endpoints this is actually a copy of $I / \partial I \cong S ^ { 1 }$ inside of M representing the middle circle of the strip. But then M deformation retracts onto $S ^ { 1 }$ by just moving every point in $I \times I$ horizontally towards this line, so $M \simeq S ^ { 1 }$ and $\pi _ { 1 } ( M ) \cong \mathbb { Z }$ , generated by the loop described which we’ll call α.

To see what the boundary curve is, label the corners $a , b$ with the suitable identification. Then take a path from a to b on the right-hand boundary of the square. By sliding this through $I \times I$ , this is homotopic α. But similarly, the path from b to a on the LHS of the square is also homotopic to $\alpha ,$ so the loop $a  b  a \simeq \alpha ^ { 2 }$ 2, so if $[ \alpha ] = 1 \in \pi _ { 1 } ( M )$ , then $[ a  b  a ] = 2$

11. First note that $\pi _ { 1 } ( S ^ { 1 } \times S ^ { 1 } ) \cong F ^ { 2 }$ , the free group on two generators, say $[ \alpha ] , [ \beta ]$ corresponding to the two nontrivial loops on the torus - say α is the longitudinal loop, and $\beta$ is the meridian. Then if $\gamma$ is a loop on a torus, then you can just count how many times it winds longitudinally and around the meridian, say m and n times respectively. Then $\gamma$ can be homotoped into m copies of α and n copies of β based at $x _ { 0 }$ . So the induced map is $f _ { \sharp } : F ^ { 2 } \to F ^ { 2 }$ given by $\alpha \mapsto \alpha ^ { m } , \beta \mapsto \beta ^ { n }$ . Since $F ^ { 2 } \cong Z \times Z$ , we equivalently have $[ \alpha ] = ( 1 , 0 ) , [ \beta ] = ( 0 , 1 )$ , and then $f _ { \sharp } : Z ^ { 2 } \to Z ^ { 2 }$ is given by $( 1 , 0 ) \mapsto ( m , 0 )$ and $( 0 , 1 ) \mapsto ( 0 , n )$

## 2.3 Group Actions

1.

## 2.4 Covering Spaces

1. Any covering map $p : S ^ { 1 } \times S ^ { 1 } \to \mathbb { R P } ^ { 2 }$ would induce an injection on fundamental groups, but $\pi _ { 1 } ( T ) = \mathbb { Z } ^ { 2 }$ and $\pi _ { 1 } ( \mathbb { Z } _ { 2 } )$ - but there are no homomorphisms between these groups. Why? One of them has an element of order 2, the other does not.

2. Theorem: if $M _ { g } \twoheadrightarrow M _ { h }$ is an n−sheeted covering space, then $g = n ( h - 1 ) + 1$

<!-- image-->

3. Draw CW square for T and cut down the center to see two copies of K.

4. Let $p : { \tilde { G } } \twoheadrightarrow G$ be such a covering, $a , b \in { \tilde { G } }$ , we then want to show that $p ( a ) p ( b ) = p ( a \star b )$ for some group operation ? which we need to construct.

Pick a basepoint $x \in G$ and any point $\tilde { x } \in p ^ { - 1 } ( x )$ . Since $\tilde { G }$ is path connected, pick two paths $\alpha , \beta$ from x˜ to a, b respectively.

Now define a path $f : I  G$ by $f ( t ) = ( p \circ \alpha ) ( t ) \cdot ( p \circ \beta ) ( t )$ , that is, evaluating $f , g$ at a given time in ${ \tilde { G } } ,$ projecting the results down into G, and multiplying them there. By uniqueness of path lifting, this yields a lift $\tilde { f } : I \to \tilde { G }$

Then define $a \star b = \tilde { f } ( 1 )$ , the endpoint of $\tilde { f }$ in ${ \tilde { G } } .$ Then by construction,

$p ( a \star b ) = p ( \tilde { f } ( 1 ) ) = f ( 1 ) = ( p \circ \alpha ) ( 1 ) \cdot ( p \circ \beta ) ( 1 ) = p ( a ) p ( b )$ . (Need to show this is continuous, and doesn’t depend on $\alpha , \beta ? )$

5. Since $\begin{array} { r } { T ^ { n } \ = \ \prod _ { n } S ^ { 1 } } \end{array}$ , we have $\begin{array} { r } { \pi _ { 1 } ( T ^ { n } ) \ : = \ : \prod _ { n } \pi _ { 1 } ( S ^ { 1 } ) \ : = \ : \mathbb { Z } ^ { n } } \end{array}$ We can also construct a cover $p : \mathbb { R } ^ { n }  T ^ { n }$ by just taking $\mathbb { R } \to S ^ { 1 }$ the usual cover in each coordinate, yielding the covering space $\tilde { X } = \mathbb { R } ^ { n }$ over $X = T ^ { n }$

By Hatcher (prop 4.1), the induced maps $p _ { * } ^ { i } : \pi _ { i } ( { \tilde { X } } ) \to \pi _ { i } ( X )$ is an isomorphism for $i \geq 2$ . But $\pi _ { i } ( \mathbb { R } ^ { n } ) = 0$ for $i \neq 0$ , so by this isomorphism $\pi _ { i } ( T ^ { n } ) = i \geq 2$

6. General construction: construct a tree T by picking a basepoint in G and adding a vertex for every non-backtracking walk in G.

In this case, it’s the infinite 3-valent graph (also called the infinite k−regular tree)

This is the universal cover, because T is connected and acyclic (i.e. a tree). This means that $\pi _ { 1 } ( T ) = 0$ , so T is simply connected. Since universal covers are simply connected and unique up to isomorphism, this is it.

7. Generators of the subgroups:

8. $\left. a b ^ { - 1 } , a b a ^ { - 2 } , a ^ { 3 } b ^ { - 1 } a ^ { - 2 } , a ^ { 3 } \right.$

9. $\langle b , a b a ^ { - 1 } , a ^ { 2 } b a ^ { - 2 } , a ^ { 3 } \rangle$

10. $\langle b ^ { 2 } , b a , a ^ { 3 } , a b a ^ { - 1 } \rangle$

11. hbi

12. $\langle b a , b ^ { - 1 } a \rangle$

Relevant covers:

<!-- image-->  
Figure 3: 1512964258737

<!-- image-->  
Figure 4: 1512964650272

<!-- image-->  
Figure 5: 1512965253808

<!-- image-->  
Figure 6: 1512965792844

<!-- image-->

5. Let T be a copy of the Cayley Tree on two on the two generators a, b, then:

6. This is just the Cayley graph over $\mathbb { Z } \times \mathbb { Z } .$ or essentially the integer lattice:

7. It’s helpful to note that $\langle ( 1 , 0 ) , ( 0 , p ) \rangle \subset \langle ( 1 , 0 ) , ( 0 , 1 ) \rangle \cong \mathbb { Z } \times \mathbb { Z } \subset \mathbb { R } \times \mathbb { R }$ is an index p subgroup.

## 2.5 Simplicial Homology

1. Todo

<!-- image-->

2. Figure 8

Here we have: $C _ { 3 } = \emptyset \ C _ { 1 } = [ 1 2 ] , [ 2 3 ] , [ 1 3 ] , [ 3 4 ] , [ 3 5 ] , [ 4 5 ] \cong \mathbb { Z } ^ { 6 } \ C _ { 0 } = [ 1 ] , [ 2 ] , [ 3 ] , [ 4 ] , [ 5 ] \cong \mathbb { Z } ^ { 5 }$

So we have $C _ { 2 } \to C _ { 1 } \to C _ { 0 } \cong 0 \xrightarrow [ ] { \partial _ { 2 } } \mathbb { Z } ^ { 6 } \xrightarrow { \partial _ { 1 } } \mathbb { Z } ^ { 5 } \xrightarrow [ ] { \partial _ { 0 } } ($ 0

Computing boundary operators, we have

$$
{ \begin{array} { r l } & { \partial _ { 1 } ( [ 1 2 ] ) = [ 2 ] - [ 1 ] ~ \partial _ { 1 } ( [ 2 3 ] ) = [ 3 ] - [ 2 ] ~ \partial _ { 1 } ( [ 1 3 ] ) = [ 3 ] - [ 1 ] ~ \partial _ { 1 } ( [ 3 4 ] ) = [ 4 ] - [ 3 ] ~ \partial _ { 1 } ( [ 3 5 ] ) = [ 5 ] - [ 3 ] } \\ & { \partial _ { 1 } ( [ 4 5 ] ) = [ 5 ] - [ 4 ] ~ } \end{array} }
$$

$$
\partial _ { 0 } = 0
$$

And so $\begin{array} { r } { H _ { 0 } = \ker \partial _ { 0 } / \mathrm { i m } \ \partial _ { 1 } = \frac { C _ { 0 } } { < \partial _ { 1 } ( [ i j ] ) > } } \end{array}$ , but from the above calculation we have $[ 5 ] = [ 4 ] = [ 3 ] =$ $[ 2 ] = [ 1 ]$ in the quotient, so there is just one generator and $H _ { 0 } \cong \mathbb { Z }$

generate two 1-cycles, so we have Note that $\partial _ { 2 }$ is an injection from $\begin{array} { r l } & { \mathrm { ~ 1 ~ 0 ~ i n t o ~ } C _ { 1 } , \mathrm { ~ s i n c e ~ t h e r e ~ a r e ~ n o ~ 2 - s i m p l i c e s . ~ } \mathrm { ~ N } } \\ & { H _ { 1 } = \frac { \ker \partial _ { 1 } } { \mathrm { i m } \partial _ { 2 } } = \frac { < [ 2 3 ] - [ 3 1 ] + [ 1 2 ] , [ 4 5 ] - [ 3 5 ] + [ 3 4 ] > } { 0 } \cong \mathbb { Z } ^ { 2 } } \end{array}$ Moreover, one can

One way to see that these are the generators is to pretend there are two 2-simplices, [123], [345]

and compute $\partial _ { 2 }$ of both of them. Since $\partial _ { 1 } \partial _ { 2 } = 0$ , anything in the image of $\partial _ { 2 }$ would have to go to zero anyways, and would thus be in the kernel of $\partial _ { 1 }$ . Since it’s not actually the boundary of any 2-chain, it doesn’t become trivial in homology.

So we have $H _ { 2 } \to H _ { 1 } \to H _ { 0 } = 0 \to \mathbb { Z } ^ { 2 } \to \mathbb { Z }$

<!-- image-->

$$
S ^ { 2 }
$$

$$
C _ { 3 } = \emptyset
$$

And $0 \xrightarrow [ ] { \partial _ { 3 } } C _ { 2 } \xrightarrow [ ] { \partial _ { 2 } } C _ { 1 } \xrightarrow [ ] { \partial _ { 1 } } C _ { 0 } \xrightarrow [ ] { \partial _ { 0 } } 0 \cong 0 \xrightarrow [ ] { \partial _ { 3 } } \mathbb { Z } ^ { 8 } \xrightarrow [ ] { \partial _ { 2 } } \mathbb { Z } ^ { 1 2 } \xrightarrow [ ] { \partial _ { 1 } } \mathbb { Z } ^ { 6 } \xrightarrow [ ] { \partial _ { 0 } } \mathbb { Z } ^ { 8 } $ 0 We have $\partial _ { 1 } ( [ i j ] ) = j - i$ and $\partial _ { 2 } ( [ i j k ] ) = j k - i k + i j$

We know in advance we should have $\prod H _ { n } = ( \cdot \cdot \cdot , 0 , \mathbb { Z } , 0 , \mathbb { Z } )$

For $\begin{array} { r } { H _ { 0 } = \frac { \ker \partial _ { 0 } } { \mathrm { i m } ~ \partial _ { 1 } } = \frac { C _ { 0 } } { \langle \{ j - i | i < j \} \rangle } } \end{array}$ . In the quotient, we see $1 = 6 = 3 = 2 = 5 = 4$ by just taking the indicated walk on the graph, so there is one generator in the quotient and $H _ { 0 } \cong \mathbb { Z }$

For $\begin{array} { r } { H _ { 1 } ~ = ~ \frac { \ker \partial _ { 1 } } { \operatorname { i m } \partial _ { 2 } } } \end{array}$ , we just note that there are 6 2-cycles, so each are in the kernel of $\partial _ { 1 }$ , but each of them comes from a 2-cell, so is in the image of $\partial _ { 2 }$ . So both groups in question are $\mathbb { Z } ^ { 8 }$ and the quotient is zero. For $\begin{array} { r } { H _ { 3 } = \frac { \ker \partial _ { 2 } } { \mathrm { i m } \ \partial _ { 3 } } } \end{array}$ , since im $\partial _ { 3 } = 0$ , we can just look at $\partial _ { 3 } ( [ 1 2 3 4 5 6 ] ) =$ $2 3 4 5 6 - 1 3 4 5 6 + 1 2 4 5 6 - 1 2 3 5 6 + 1 2 3 4 6 - 1 2 3 4 5$ . This is an element (and the only one) that goes to zero under $\partial _ { 2 }$ , it generates ker $\partial _ { 2 }$ . So there is one generator, and $H _ { 3 } = \mathbb { Z }$

3. $\mathbb { R } \mathbb { P } ^ { 2 }$

4. $S ^ { 2 } \cup _ { f } D ^ { 2 }$ , where f attaches to the equator

5. $T \cup _ { f } D ^ { 2 }$ , where f attaches inside the torus

## 2.6 Mayer Vietoris Problems

2.6.1 RP2

We start with a few known facts. Let $A = M$ , the Mobius strip, and $B = D ^ { 2 }$ , the solid disk.

$\mathbb { R P } ^ { 2 } = M \mathrm { L I } _ { \partial } D ^ { 2 }$

$H _ { * } ( M ) = H _ { * } ( S ^ { 1 } )$ , by a deformation retract of M onto its center circle.

$H _ { * } ( D ^ { 2 } ) = \mathbb { Z } \delta _ { 0 }$

$H _ { * } ( S ^ { 1 } ) = \mathbb { Z } ( \delta _ { 0 } + \delta _ { 1 } )$

$M \cap D ^ { 2 } = \partial M = S ^ { 1 }$

From Mayer-Vietoris, we have

<!-- image-->

and plugging in what is known yields

<!-- image-->

where $i : S ^ { 1 } \to M$ and $j : S ^ { 1 } \to D ^ { 2 }$

We can then identify all of the induced maps:

$$
\bullet i ^ { 2 } : H _ { 2 } \partial M \to H _ { 2 } M \implies i ^ { 2 } : 0 \to 0 \implies i ^ { 2 } = 0
$$

• i1 : H1∂M → H1M , i.e. i1 : Z → Z where 1 7→ 2

– Since M deformation retracts onto its center circle, $H _ { 1 } M \cong H _ { 1 } S _ { M }$ where $S _ { M }$ is the center circle (homotopies induce isomorphisms on homology). But $H _ { 1 } \partial M$ is generated by a cycle of edges with includes into ∂M, which retracts onto a cycle that double covers $S _ { M }$ , so this map acts by doubling the generator.

$i ^ { 0 } : H _ { 0 } \partial M \to H _ { 0 } M , { \mathrm { i . e . ~ } } i ^ { 0 } : \mathbb { Z } \to \mathbb { Z }$

$$
\bullet \ j ^ { 2 } : H _ { 2 } \partial M \to H _ { 2 } D ^ { 2 } \ \Longrightarrow \ j ^ { 2 } : 0 \to 0 \ \Longrightarrow \ j ^ { 2 } = 0
$$

$$
\bullet \ j ^ { 1 } : H _ { 1 } \partial M \to H _ { 1 } D ^ { 2 } \ \Longrightarrow \ j ^ { 1 } : \mathbb { Z } \to 0 \ \Longrightarrow \ j ^ { 1 } = 0
$$

$$
\bullet \ j ^ { 0 } : H _ { 0 } \partial M \to H _ { 0 } D ^ { 2 } \implies j _ { 0 } : \mathbb { Z } \to \mathbb { Z }
$$

So we can that the only nontrivial maps are $j ^ { 0 } , i ^ { 0 } , i ^ { 1 }$

Claim: $H _ { 2 } ( \mathbb { R } \mathbb { P } ^ { 2 } ) = 0 \colon$

We consider the portion of the sequence

$$
\begin{array} { r } { \cdot \cdot \cdot 0  H _ { 2 } \mathbb { R } \mathbb { P } ^ { 2 } \xrightarrow { \delta _ { 2 } } H _ { 1 } \partial M \xrightarrow { ( i ^ { 1 } , - j ^ { 1 } ) } H _ { 1 } M \oplus H _ { 1 } D ^ { 2 } \cdot \cdot \cdot } \\ { \cdot \cdot 0  H _ { 2 } \mathbb { R } \mathbb { P } ^ { 2 } \xrightarrow { \delta _ { 2 } } \mathbb { Z } \xrightarrow { ( i ^ { 1 } , - j ^ { 1 } ) } \mathbb { Z } \oplus 0 \cdot \cdot \cdot } \end{array}
$$

We will show that ker $\delta _ { 2 } =$ im $\delta _ { 2 } = 0$ . By the first isomorphism theorem, we would then have $\begin{array} { r } { \frac { H _ { 2 } \mathbb { R P } ^ { 2 } } { \ker \delta _ { 2 } } \cong \mathrm { i m } \ \delta _ { 2 } } \end{array}$ yielding $\textstyle \frac { \bar { H } _ { 2 } \mathbb { R } \mathbb { P } ^ { 2 } } { 0 } = \bar { H } _ { 2 } \mathbb { R } \mathbb { P } ^ { 2 } \cong \bar { 0 }$

• Claim: ker $\delta _ { 2 } = 0$

This follows because it is on the left tail of an exact sequence, where ker $\delta _ { 2 } = \mathrm { i m } 0 = 0$

• Claim: im $\delta _ { 2 } = 0$

$$
( i ^ { 1 } , - j ^ { 1 } ) : H _ { 1 } \partial M \to H _ { 1 } M \oplus H _ { 1 } D ^ { 2 }
$$

is injective; explicitly, it is the map

$$
\begin{array} { r } { M _ { 2 } : \mathbb { Z }  \mathbb { Z } \oplus 0 } \\ { 1 \mapsto ( 2 , 0 ) } \end{array}
$$

From above, know that $- j ^ { 1 }$ is a zero map, and that $i ^ { 1 }$ doubles each generator. By this explicit construction, it is injective since 0 maps to 0.

But then ker $( i ^ { 1 } , - j ^ { 1 } ) = \mathrm { i m } \ \delta _ { 2 } = 0$ by exactness.

So now we have:

<!-- image-->

Claim: $H _ { 1 } ( \mathbb { R P } ^ { 2 } ) = \mathbb { Z } _ { 2 }$

Here we are examining this portion of the sequence:

$$
\begin{array} { r } { \cdots \mathbb { Z } \xrightarrow { x \to ( 2 x , 0 ) } H _ { 1 } M \oplus H _ { 1 } D ^ { 2 } \xrightarrow { l ^ { 1 } - r ^ { 1 } } H _ { 1 } \mathbb { R } \mathbb { P } ^ { 1 } \xrightarrow { \delta _ { 1 } } H _ { 0 } \partial M \xrightarrow { ( \imath ^ { 0 } , - j ^ { 0 } ) } H _ { 0 } M \oplus H _ { 0 } D ^ { 2 } \cdots } \\ { \cdots \mathbb { Z } \xrightarrow { x \to ( 2 x , 0 ) } \mathbb { Z } \mathbb { Z } \oplus 0 \xrightarrow { l ^ { 1 } - r ^ { 1 } } H _ { 1 } \mathbb { R } \mathbb { P } ^ { 1 } \xrightarrow { \delta _ { 1 } } \mathbb { Z } \xrightarrow { ( \imath ^ { 0 } , - j ^ { 0 } ) } \mathbb { Z } \mathbb { G } \mathbb { Z } \cdots . } \end{array}
$$

In general, we have the first isomorphism theorem: given any map $f$ we have ${ \frac { \operatorname { d o m } f } { \ker f } } \cong$ im $f .$ . Here we will take $f = l ^ { 1 } - r ^ { 1 }$ and identify the necessary components to apply this theorem.

• Claim: im $l ^ { 1 } - r ^ { 1 } = H _ { 1 } \mathbb { R P } ^ { 2 }$

– We use the fact that the maps $( i ^ { * } , j ^ { * } )$ are all injections, so in particular $0 = \ker ( i ^ { 0 } , j ^ { 0 } ) =$ im $\delta _ { 1 }$ by exactness. Consequently ker $\delta _ { 1 } = H _ { 1 } \mathbb { R P } ^ { 1 } = \mathrm { i m } \ l ^ { 1 } - r ^ { 1 }$ by exactness.

• What is ker $( l ^ { 1 } - r ^ { 1 } ) \acute { : }$

– By exactness, ker $\begin{array} { r l } {  { \big ( l ^ { 1 } - r ^ { 1 } \big ) = } } \end{array}$ im $( x \mapsto ( 2 x , 0 ) ) = 2 \mathbb { Z } \oplus 0$

By the first isomorphism theorem, we have im $\begin{array} { r } { ( l ^ { 1 } - r ^ { 1 } ) \cong \frac { \operatorname { d o m } ( l ^ { 1 } - r ^ { 1 } ) } { \ker ( l ^ { 1 } - r ^ { 1 } ) } = \frac { \mathbb { Z } \oplus 0 } { 2 \mathbb { Z } \oplus 0 } \cong \mathbb { Z } _ { 2 } . } \end{array}$

Note that $l ^ { 1 } - r ^ { 1 }$ is a nontrivial homomorphism from $2 \mathbb { Z } \cong \mathbb { Z }$ to $\mathbb { Z } _ { 2 }$ , of which there is only one: the natural quotient map $x \mapsto x$ mod 2.

There is also no nontrivial homomorphism from $\mathbb { Z } _ { 2 } \to \mathbb { Z } .$ , so $\delta _ { 1 } = 0$

We now have:

<!-- image-->

## 2.7 Claim: $H _ { 0 } ( \mathbb { R P } ^ { 2 } ) = \mathbb { Z }$

Here we examine

$$
\begin{array} { r } { H _ { 1 } \mathbb { R } \mathbb { P } ^ { 2 } \xrightarrow { \delta _ { 1 } } H _ { 0 } \partial M \xrightarrow { ( i ^ { 0 } , j ^ { 0 } ) } H _ { 0 } M \oplus H _ { 0 } D ^ { 2 } \xrightarrow { l ^ { 0 } - r ^ { 0 } } H _ { 0 } \mathbb { R } \mathbb { P } ^ { 2 } \xrightarrow { \delta _ { 0 } } 0 } \\ { \mathbb { Z } _ { 2 } \xrightarrow { \delta _ { 1 } } \mathbb { Z } \xrightarrow { ( i ^ { 0 } , j ^ { 0 } ) } \mathbb { Z } \mathbb { \oplus Z } \xrightarrow { l ^ { 0 } + r ^ { 0 } } H _ { 0 } \mathbb { R } \mathbb { P } ^ { 2 } \xrightarrow { \delta _ { 0 } } 0 } \end{array}
$$

Since there is no nontrivial homomorphism from $\mathbb { Z } _ { 2 } \to \mathbb { Z } .$ we have $\delta _ { 1 } = 0$

We also have $\delta _ { 0 } = 0$ and ker $\delta _ { 0 } = H _ { 0 } \mathbb { R P } ^ { 2 } = \mathrm { i m } \ l ^ { 0 } + r ^ { 0 }$ making $l ^ { 0 } + r ^ { 0 }$ surjective, so by the first isomorphism theorem we have $\begin{array} { r } { H _ { 0 } \mathbb { R } \mathbb { P } ^ { 2 } \cong \frac { \mathbb { Z } \oplus \mathbb { Z } } { \mathrm { k e r } l ^ { 0 } + r ^ { 0 } } = \frac { \mathbb { Z } \oplus \mathbb { Z } } { \mathrm { i m } \ ( i ^ { 0 } , j ^ { 0 } ) } } \end{array}$

$\mathrm { B y }$ a similar argument used earlier, the double covering of the boundary circle ∂M over $S ^ { 1 }$ yields the map $( i ^ { 0 } , j ^ { 0 } ) : \mathbb { Z } \to \mathbb { Z } \oplus \mathbb { Z }$ given by $x \mapsto ( 2 x , 2 x )$ with

## Summary:

With all of this information, we finally have

<!-- image-->

And so we find $H _ { * } ( \mathbb { R P } ^ { 2 } ) = \mathbb { Z } \delta _ { 0 } + \mathbb { Z } _ { 2 } \delta _ { 1 }$

2.8 Cellular Homology

2.9 Degree

2.10 UCT

2.11 Homological Algebra
