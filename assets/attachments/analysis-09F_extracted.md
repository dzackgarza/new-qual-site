## ANALYSIS QUALIFYING EXAM, FALL 2009

Instructions: Work any 10 problems and therefore at least 4 from Problcms 1-6 and at least 4 from Problems 7-12. All problems are worth ten points. Full credit on one problem will be better than part credit on two problcms. If you attempt more than 10 problems, indicate which 10 arc to bc graded.

1: Find a non-empty closed sct in the Hilbert space $L ^ { 2 } ( [ 0 , 1 ] )$ that does not contain an clement of smallest norm. Prove your assertion.

2: Let v be a trigonometric polynomial in two variables, that is,

$$
\boldsymbol { v } ( \boldsymbol { x } , \boldsymbol { y } ) = \sum _ { n , m \in \mathbb { Z } } \boldsymbol { a } _ { n , m } e ^ { 2 \pi i ( n , \boldsymbol { x } + m \boldsymbol { y } ) } \ ,
$$

with only finitely many non-zero cocfficicnts $a _ { n , m }$ . If

$$
{ \mathfrak { u } } = { \mathfrak { v } } - \Delta { \mathfrak { v } }
$$

where $\Delta = \partial _ { x } ^ { 2 } + \partial _ { y } ^ { 2 }$ is the Laplacian, prove that

$$
\| v \| _ { L ^ { \infty } ( [ 0 , 1 ] \times [ 0 , 1 ] ) } \leq C \| u \| _ { L ^ { 2 } ( [ 0 , 1 ] \times [ 0 , 1 ] ) }
$$

for some constant C independent of v.

3: Let $f : [ 0 , 1 ]  \mathbb { R }$ be continuous with

$$
\operatorname* { m i n } _ { 0 \leq x \leq 1 } f ( x ) = 0 ~ .
$$

Assume that for all $0 \leq a < b \leq 1$ we have

$$
\int _ { a } ^ { b } { \bigl [ } f ( x ) - \operatorname* { m i n } _ { a \leq x \leq b } f ( y ) { \bigr ] } d x \leq { \frac { 1 } { 2 } } | b - a |
$$

aProve that for all $\lambda \geq 0$

$$
| \{ x : f ( x ) > \lambda + 1 \} | \leq { \frac { 1 } { 2 } } | \{ x : f ( x ) > \lambda \} |
$$

Here |S] dcnotcs the Lebesgue measure the sct S.

) Prove that for all $1 \leq c < 2 .$

$$
\int _ { 0 } ^ { 1 } c ^ { f ( x ) } d x \leq { \frac { 1 0 0 } { 2 - c } }
$$

[The constant 100 is not optimal, but is certainly largc cnough.]

4: Provc the following variant of the Lebesgue Differentiation thcorem: Let $\mu$ bc a finite Borel measure on R, singular with respect to Lebesgue measurc. Then for Lebcsguealmost every $x \in \mathbb { R } .$

$$
\operatorname* { l i m } _ { \epsilon \to 0 } { \frac { \mu ( [ x - \epsilon , x + \epsilon ] ) } { 2 \epsilon } } = 0
$$

5: Construct a Borel subset E of the real line R such that for all intervals $[ a , b ]$ we have

$$
0 < m ( E \cap [ a , b ] ) < | b - a |
$$

whcre m denotes Lcbesgue measure.

6: The Poisson kcrnel for $0 \leq \rho < 1$ is the 2π periodic function on R defined by

$$
P _ { \rho } ( \theta ) = \mathrm { R e } \left( { \frac { 1 + \rho e ^ { i \theta } } { 1 - \rho e ^ { i \theta } } } \right)
$$

For functions $h$ continuous on and harmonic inside the closed disc of radius R about the origin one has (you need not prove this)

$$
h ( r e ^ { i \eta } ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } P _ { r / R } ( \eta - \theta ) h ( R e ^ { i \theta } ) . d \theta
$$

Assume that h is harmonic and positive on the open unit disc $D = \{ z \in \mathbb { C } : | z | < 1 \}$ Prove that there cxists a positive Borel measure $\mu$ on [0, 2π] such that for all $r e ^ { i \theta } \in D$ one has

$$
h ( r e ^ { i \eta } ) = \int _ { 0 } ^ { 2 \pi } P _ { r } ( \eta - \theta ) d \mu ( \theta )
$$

7: a) Define unitary operator on a complex Hilbert spacc.

b) Let S be a unitary operator on a complex Hilbert space. Using your definition, prove that for every complex number $| \lambda | < 1$ the opcrator $S - \lambda I$ is invertible. Here I denotes the identity operator.

c) For a fixed vector v in the Hilbert space and all $\{ \lambda \in \mathbb { C } : | \lambda | < 1 \}$ , we define

$$
h ( \lambda ) = \left. ( S + \lambda I ) ( S - \lambda I ) ^ { - 1 } \upsilon , \upsilon \right. .
$$

Show that Re h is a positive harmonic function. [You may not invoke the spectral theorem — this is part of a proof of that theorem.]

8: Let Ω be an open convex region in the complex plane. Assume f is a holomorphic function on Ω2 and the real part of its derivative is positive: $\mathrm { R e } ( f ^ { \prime } ( z ) ) > 0$ for all $z \in \Omega$ a) Provc that f is one-to-one.

b) Show by example that the word "convex" cannot be replaced by "connected and simply connected".

9: Let f be a non-constant meromorphic function on thc complex plane C that obeys

$$
f ( z ) = f ( z + \sqrt { 2 } ) = f ( z + i \sqrt { 2 } ) .
$$

(In particular, the poles of these three functions coincide.) Assumc $f$ has at most one pole in the closed unit disc

$$
\overline { { D } } = \{ z : | z | \leq 1 \}
$$

Prove that $f$ has exactly one pole in $\overline { 1 }$

b) Prove that this is not a simple pole.

10: Consider thc unit sphere in $\mathbb { R } ^ { 3 }$ with poles removed:

$$
S : = { \big \{ } { \big ( } \cos ( \theta ) \sin ( \phi ) , \sin ( \theta ) \sin ( \phi ) , \cos ( \phi ) { \big ) } : 0 < \phi < \pi \ \mathrm { a n d } \ \theta \in \mathbb { R } { \big \} } \ .
$$

Give an explicit formula for a conformal map from the complex plane onto S so that horizontal lines are mapped to circles of constant $\phi$ and vertical lines are mapped to arcs of constant $\theta .$

11: Let $f$ be an analytic function in thc open unit disc $D = \{ z : | z | < 1 \}$ that obeys $| f ( z ) | \leq 1$ for all $z \in D$ . Let $g$ be the restriction of $f$ to the real interval $( 0 , 1 )$ and assume

$$
\operatorname* { l i m } _ { r \to 1 } g ( r ) = 1
$$

and

Prove that $f$ is constant.

$$
\operatorname * { l i m } _ { r \to 1 } { g ^ { \prime } ( r ) } = 0 .
$$

12: Let $f$ be a non-constant meromorphic function in the complex plane. Assume that if $f$ has a pole at the point $z \in \mathbb { C }$ , then z is of the form nπ with an integer $\pi \in \mathbb { Z }$ Assume that for all non-real z we have the estimate

$$
| f ( z ) | \leq ( 1 + | \mathrm { I m } ( z ) | ^ { - 1 } ) e ^ { - | \mathrm { I m } ( z ) | }
$$

Prove that for every integer $n \in \mathbb { Z } , f$ has a polc at the point πn.