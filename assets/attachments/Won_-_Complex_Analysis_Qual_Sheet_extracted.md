# Complex Analysis Qual Sheet

Robert Won

“Tricks and traps. Basically all complex analysis qualifying exams are collections of tricks and traps.”

## 1 Useful facts

1. $e ^ { z } = \sum _ { n = 0 } ^ { \infty } \frac { z ^ { n } } { n ! }$

2. sin $z = \sum _ { n = 0 } ^ { \infty } ( - 1 ) ^ { n } { \frac { z ^ { 2 n + 1 } } { ( 2 n + 1 ) ! } } = { \frac { 1 } { 2 i } } ( e ^ { i z } - e ^ { - i z } )$

3. $\cos z = \sum _ { n = 0 } ^ { \infty } ( - 1 ) ^ { n } { \frac { z ^ { 2 n } } { 2 n ! } } = { \frac { 1 } { 2 } } ( e ^ { i z } + e ^ { - i z } )$

4. If g is a branch of $f ^ { - 1 }$ on G, then for $a \in G , g ^ { \prime } ( a ) = { \frac { 1 } { f ^ { \prime } ( g ( a ) ) } }$

5. $| z \pm a | ^ { 2 } = | z | ^ { 2 } \pm 2 \mathrm { R e } \overline { { { a } } } z + | a | ^ { 2 }$

6. If f has a pole of order m at $z = a$ and $g ( z ) = ( z - a ) ^ { m } f ( z )$ , then

$$
\operatorname { R e s } ( f ; a ) = { \frac { 1 } { ( m - 1 ) ! } } g ^ { ( m - 1 ) } ( a ) .
$$

7. The elementary factors are defined as

$$
E _ { p } ( z ) = ( 1 - z ) \exp { \Bigg ( } z + { \frac { z ^ { 2 } } { 2 } } + \cdots + { \frac { z ^ { p } } { p } } { \Bigg ) } .
$$

Note that elementary factors are entire and $E _ { p } ( z / a )$ has a simple zero at $z = a$

8. The factorization of sin is given by

$$
\sin \pi z = \pi z \prod _ { n = 1 } ^ { \infty } \left( 1 - { \frac { z ^ { 2 } } { n ^ { 2 } } } \right) .
$$

9. If $f ( z ) = ( z - a ) ^ { m } g ( z )$ where $g ( a ) \neq 0$ , then

$$
{ \frac { f ^ { \prime } ( z ) } { f ( z ) } } = { \frac { m } { z - a } } + { \frac { g ^ { \prime } ( z ) } { g ( z ) } } .
$$

## 2 Tricks

1. If f(z) nonzero, try dividing by $f ( z )$ . Otherwise, if the region is simply connected, try writing $f ( z ) = e ^ { g ( z ) }$ .

2. Remember that $| e ^ { z } | = e ^ { \mathrm { R e } z }$ and $\arg e ^ { z } =$ Imz. If you see a Rez anywhere, try manipulating to get $e ^ { z }$

3. On a similar note, for a branch of the log, log $r e ^ { i \theta } = \log | r | + i \theta$

4. Let $z = e ^ { i \theta }$

5. To show something is analytic use Morera or find a primitive.

6. If f and g agree on a set that contains a limit point, subtract them to show they’re equal.

7. Tait: “Expand by power series.”

8. If you want to count zeros, either Argument Principle or Rouch´e.

9. Know these M¨obius transformations:

(a) To map the right half-plane to the unit disk (or back), $\frac { 1 - z } { 1 + z }$

(b) To map from the unit disk to the unit disk, remember $\varphi _ { a } ( z ) = { \frac { z - a } { 1 - { \overline { { a } } } z } }$ . This is a bijective map with inverse $\varphi _ { - a } ( z )$ . Also, $\varphi _ { a } ( a ) = 0 , \varphi _ { a } ^ { \prime } ( z ) = \frac { 1 - | a | ^ { 2 } } { ( 1 - \overline { { { a } } } z ) ^ { 2 } } , \varphi _ { a } ^ { \prime } ( 0 ) = 1 - | a | ^ { 2 } \nonumber$ 2 , and $\varphi _ { a } ^ { \prime } ( a ) = { \frac { 1 } { 1 - | a | ^ { 2 } } } .$

10. If f (z) is analytic, then $\overline { { f ( \overline { { z } } ) } }$ is analytic (by Cauchy-Riemann). So if, for example, $f ( z )$ is real on the real axis, then $f ( z ) = { \overline { { f ( { \overline { { z } } } ) } } }$

11. To prove that a function defined by an integral is analytic, try Morera and reversing the integral. (e.g. $\int _ { \epsilon } ^ { \infty } e ^ { - t } t ^ { z - 1 } d t$ is analytic since $\begin{array} { r } { \bar { \int } _ { T } \int _ { \epsilon } ^ { \infty } e ^ { - t } t ^ { z - 1 } d t d z = \int _ { \epsilon } ^ { \infty } \int _ { T } e ^ { - t } t ^ { z - 1 } d z d t = \mathrm { 0 } . ) } \end{array}$

12. If given a point of $f ~ ( \operatorname { s a y } f ( 0 ) = a )$ and some condition on $f ^ { \prime }$ on a simply connected ${ \mathrm { s e t } } ,$ try $\begin{array} { r } { \int _ { [ 0 , z ] } f ^ { \prime } = f ( z ) - f ( 0 ) } \end{array}$

13. To create a non-vanishing function, consider exponentiating.

## 3 Theorems

1. Cauchy Integral Formula: Let G be region and $f : G \to \mathbb { C }$ be analytic. If $\gamma _ { 1 } , \ldots , \gamma _ { m }$ are closed rectifiable curves in G with $\begin{array} { r } { \sum _ { k = 0 } ^ { m } n ( \gamma _ { k } ; w ) = 0 } \end{array}$ for all $w \in \mathbb { C } \setminus G$ , then for $a \in$ $G \setminus ( \cup _ { k = 1 } ^ { m } \{ \gamma _ { k } \} )$ ,

$$
f ^ { ( n ) } ( a ) \cdot \sum _ { k = 0 } ^ { m } n ( \gamma _ { k } ; a ) = { \frac { n ! } { 2 \pi i } } \sum _ { k = 1 } ^ { m } \int _ { \gamma _ { k } } { \frac { f ( z ) } { ( z - a ) ^ { n + 1 } } } d z .
$$

2. Cauchy’s Theorem: Let G be a region and $f : G \to \mathbb { C }$ be analytic. If $\gamma _ { 1 } , \ldots , \gamma _ { m }$ are closed rectifiable curves in G with $\textstyle \sum _ { k = 0 } ^ { m } n ( \gamma _ { k } ; w ) = 0$ for all $w \in \mathbb { C } \setminus G$ , then

$$
\sum _ { k = 1 } ^ { m } \int _ { \gamma _ { k } } f ( z ) d z = 0
$$

3. Liouville’s Theorem: If f is a bounded entire function, then f is constant.

4. Maximum Modulus Theorem: Let G be a region and $f : G \to \mathbb { C }$ be analytic. If there exists an $a \in G$ such that $| f ( a ) | \geq | f ( z ) |$ for all $z \in G$ , then f is constant on G.

5. Morera’s Theorem: Let G be a region and $f : G \to \mathbb { C }$ be continuous. If $\textstyle \int _ { T } f = 0$ for every triangular path T in G, then f is analytic on G.

6. Goursat’s Lemma: Let G be a region and let $f : G \to \mathbb { C }$ . If f is differentiable, then f is analytic on G.

7. Cauchy-Riemann Equations: Let $f ( x , y ) = u ( x , y ) + i v ( x , y )$ for real-valued functions u and v. Then f is analytic if and only if

$$
{ \frac { \partial u } { \partial x } } = { \frac { \partial v } { \partial y } } \quad { \mathrm { a n d } } \quad { \frac { \partial u } { \partial y } } = - { \frac { \partial v } { \partial x } }
$$

8. Constant functions: Let $f : G \to \mathbb { C }$ be analytic. Then the following are equivalent

(i) $f ( z ) \equiv \alpha ;$

(ii) $\{ z \in G \mid f ( z ) = \alpha \}$ has a limit point in $G ;$

(iii) there exists $a \in G$ such that $f ^ { ( n ) } ( a ) = 0$ for all $n \geq 1$

9. Conformality: Let $f : G \to \mathbb { C }$ be analytic. Then if $z \in G$ and $f ^ { \prime } ( z ) \neq 0 ,$ f is conformal at z .

10. Roots of an analytic function: Let $f : G \to \mathbb { C }$ be analytic. If $f ( a ) = 0$ , then there exists a unique $m \geq 1$ and g analytic such that

$$
f ( z ) = ( z - a ) ^ { m } g ( z )
$$

with $g ( a ) \neq 0$

11. Power series: A function f is analytic on $B ( { a } ; R )$ if and only if there exists a power series $\begin{array} { r } { f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } ( z - a ) ^ { n } } \end{array}$ where we compute

$$
a _ { n } = \frac { f ^ { ( n ) } ( a ) } { n ! } = \frac { 1 } { 2 \pi i } \int _ { \gamma } \frac { f ( z ) } { ( z - a ) ^ { n + 1 } } d z .
$$

The series converges absolutely on $B ( { a } ; R )$ and uniformly on $B ( a ; r )$ for $0 \leq r < R$

12. Cauchy’s Estimate: If f analytic on $B ( { a } ; R )$ , and $| f ( z ) | \leq M$ for each $z \in B ( a ; R )$ , then

$$
\left| f ^ { ( n ) } ( a ) \right| \leq { \frac { n ! M } { R ^ { n } } } .
$$

13. Winding Number: To compute the index of a closed curve about a point $a ,$

$$
n ( \gamma ; a ) = \frac { 1 } { 2 \pi i } \int _ { \gamma } \frac { d z } { z - a } \in \mathbb { Z } .
$$

14. Open Mapping Theorem: Let G be a region, f a non-constant analytic function. If U is an open subset of G, then $f ( U )$ is open.

15. Zero-Counting Theorem: Let G be a region, $f : G \to \mathbb { C }$ analytic with roots $a _ { 1 } , \ldots a _ { m }$ . If $\{ \gamma \} \subseteq G$ and $a _ { k } \notin \{ \gamma \}$ for all k, and $\gamma \approx 0$ in $G ,$ then

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \gamma } { \frac { f ^ { \prime } ( z ) } { f ( z ) } } d z = \sum _ { k = 1 } ^ { m } n ( \gamma ; a _ { k } )
$$

Corollary: $\mathrm { I f } \ f ( a ) = \alpha$ , then $f ( z ) - \alpha$ has a root at a. So if $f ( a _ { k } ) = \alpha$ , then

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \gamma } { \frac { f ^ { \prime } ( z ) } { f ( z ) - \alpha } } d z = \sum _ { k = 1 } ^ { m } n ( \gamma ; a _ { k } )
$$

Corollary 2: If $\sigma = f \circ \gamma$ and α $\not \in \{ \sigma \}$ and $a _ { k }$ are the points where $f ( a _ { k } ) = \alpha$ , then

$$
n ( \sigma ; \alpha ) = \sum _ { k = 1 } ^ { m } n ( \gamma ; a _ { k } ) { \mathrm { ~ o r ~ } }
$$

$$
n ( f \circ \gamma ; f ( a ) ) = \sum _ { k = 1 } ^ { m } n ( \gamma ; a _ { k } )
$$

16. Roots of analytic functions: Suppose $f$ is analytic on $B ( { a } ; R )$ and let $f ( a ) = \alpha . { \mathrm { ~ I f ~ } } f ( z ) - \alpha$ has a zero of order m at $z = a$ , then there exist $\epsilon > 0$ and $\delta > 0$ such that if $0 < | \zeta - \alpha | < \delta .$ the equation $f ( z ) = \zeta$ has exactly m simple roots in $B ( a , \epsilon )$

17. Existence of Logarithm: Let $f ( z )$ be analytic and $f ( z ) \neq 0$ on $G ,$ , a simply connected region. Then there is analytic function $g ( z )$ on $G$ such that $f ( z ) = e ^ { g ( z ) }$ for all $z \in G$ .

18. Existence of Primitive: Let $f ( z )$ be analytic on $G ,$ a simply connected region. Then $f$ has a primitive.

19. Laurent Series: Let $f$ be analytic on $R _ { 1 } < | z - a | < R _ { 2 }$ , then there exists a sequence $\{ a _ { n } \} _ { n = - \infty } ^ { \infty }$ and

$$
f ( z ) = \sum _ { n = - \infty } ^ { \infty } a _ { n } ( z - a ) ^ { n }
$$

with absolute convergence in the open annulus and uniform convergence on every compact subset of the annulus. This series is called a Laurent series, and if $\gamma$ is a closed curve in the annulus, then

$$
a _ { n } = \frac { 1 } { 2 \pi i } \int _ { \gamma } \frac { f ( z ) } { ( z - a ) ^ { n + 1 } } d w .
$$

(Note that this is just the same as number 11).

20. Classification of Singularities: Suppose f analytic on $B ( a ; R ) \setminus \{ a \}$ and f has an isolated singularity at a. Then a is

(a) Removable singularity if there is a function g analytic on $B ( { a } ; R )$ such that $f ( z ) = g ( z )$ for all $z \in B ( a ; R ) \setminus \{ a \}$

The singularity is removable if and only ${ \mathrm { i f ~ } } \operatorname* { l i m } _ { z \to a } ( z - a ) f ( z ) = 0$

Also, the singularity is removable if and only if the Laurent series of f has no coefficients $a _ { n }$ for $n < 0$

(b) Pole if $\operatorname* { l i m } _ { z \to a } | f ( z ) | = \infty$

If a is a pole, then there is a unique $m \geq 1$ and an analytic function g such that $f ( z ) = { \frac { g ( z ) } { ( z - a ) ^ { m } } }$ for all $z \in B ( a ; R ) \setminus \{ a \}$ and $g ( a ) \neq 0$

The singularity is a pole if and only if the Laurent series of f has only finitely many coefficients $a _ { n }$ for $n < 0$ . The partial series for these coefficients is called the singular part of $f .$

(c) Essential singularity if a is not removable and not a pole.

The singularity is essential if and only if the Laurent series of f has infinitely many coefficients $a _ { n }$ for $n < 0$ •

21. Casorati-Weierstrass: If f has an essential singularity at a, then for all $\delta > 0 , f ( \{ z \mid 0 < | z - a | < \delta \} )$ is dense in C.

22. Residues: If f has an isolated singularity at a, then the residue of f at $a , \operatorname { R e s } ( f ; a ) = a _ { - 1 }$ We can calculate the residue using the formula for Laurent coefficients:

$$
\mathrm { R e s } ( f ; a ) = \frac { 1 } { 2 \pi i } \int _ { \gamma } f ( z ) d z .
$$

If a is a pole of order m, then if $g ( z ) = ( z - a ) ^ { m } f ( z )$

$$
\operatorname { R e s } ( f ; a ) = { \frac { g ^ { ( m - 1 ) } ( a ) } { ( m - 1 ) ! } } .
$$

23. Residue Theorem: Let f be analytic on a region G except for singularities at $a _ { 1 } , \ldots , a _ { m }$ Let $\gamma \approx 0$ be a closed curve in G with $a _ { 1 } , \dots , a _ { m } \notin \{ \gamma \}$ . Then

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \gamma } f ( z ) d z = \sum _ { k = 1 } ^ { m } n ( \gamma ; a _ { k } ) \cdot \operatorname { R e s } ( f ; a _ { k } ) .
$$

24. Argument Principle: Let f be meromorphic with roots $z _ { 1 } , \ldots , z _ { m }$ and poles $p _ { 1 } , \ldots , p _ { n }$ with $z _ { 1 } , \dots , z _ { m } , p _ { 1 } , \dots , p _ { n } \notin \{ \gamma \}$ . Then

$$
\frac { 1 } { 2 \pi i } \int _ { \gamma } \frac { f ^ { \prime } } { f } = \sum _ { k = 1 } ^ { m } n ( \gamma ; z _ { m } ) - \sum _ { j = 1 } ^ { n } n ( \gamma ; p _ { n } ) .
$$

25. Rouch´e’s Theorem: Let $f , g$ be meromorphic on G and let $\gamma$ be a closed curve in G. Then if, for all $z \in \{ \gamma \}$ ,

$$
| f ( z ) + g ( z ) | < | f ( z ) | + | g ( z ) |
$$

then $Z _ { f } - P _ { f } = Z _ { g } - P _ { g }$

26. Jordan’s Lemma: Suppose that:

(i) $f ( z )$ is analytic at all points z in the upper half plane $y \geq 0$ that are exterior to a circle $| z | = R _ { 0 }$ ;

(ii) $C _ { R }$ denotes a semicircle $z = R e ^ { i \theta }$ for $0 \leq \theta \leq 2 \pi$ with $R > R _ { 0 }$

(iii) for all points z on $C _ { R }$ there is a positive constant $M _ { R }$ such that $| f ( z ) | \leq M _ { R }$ , with lim $. \ d { \bf { R } } \to \infty { \ d { \bf { M } } } _ { R } = 0$

Then for every positive constant a:

$$
\operatorname* { l i m } _ { R \to \infty } \int _ { C _ { R } } f ( z ) e ^ { i a z } d z = 0 .
$$

27. Fractional Residue: If z0 is a simple pole of $f ( z )$ , and $C _ { R }$ is an arc of the circle $\{ | z - z _ { 0 } | = R \}$ of angle $\theta ,$ then

$$
\operatorname* { l i m } _ { R  0 } \int _ { C _ { R } } f ( z ) d z = \theta i R e s ( f ( z ) , z _ { 0 } ) .
$$

## 4 Theorems, part 2

## 1. Maximum Modulus Theorem:

(a) (First Version). If $f : G \to \mathbb { C }$ is analytic and there exists $a \in G$ with $| f ( a ) | \geq | f ( z ) |$ for all $z \in G$ , then f is constant.

(b) (Second Version). If G is open and bounded, and f analytic on G and continuous on ${ \overline { { G } } } ,$ then

$$
\operatorname* { m a x } \{ | f ( z ) | \mid z \in { \overline { { G } } } \} = \operatorname* { m a x } | f ( z ) | \mid z \in \partial G \} .
$$

(Or f attains its maximum on the boundary).

(c) (Third Version). If $f : G \to \mathbb { C }$ is analytic, and there is a constant M such that lim $\begin{array} { r } { \operatorname* { s u p } _ { z \to a } | f ( z ) | \leq M } \end{array}$ for all $a \in \partial _ { \infty } G$ , then $| f ( z ) | \leq M$ for all $z \in G$ .

$$
\begin{array} { r } { \operatorname* { s u p } _ { z \to a } f ( z ) = \operatorname* { l i m } _ { r \to 0 ^ { + } } \operatorname* { s u p } \{ f ( z ) ~ | ~ z \in G \cap B ( a ; r ) \} . ) } \end{array}
$$

2. Schwarz’s Lemma: Suppose $f : \mathbb { D } \to \mathbb { D }$ is analytic and $f ( 0 ) = 0$ . Then

(i) $| f ^ { \prime } ( 0 ) | \le 1$ 2

(ii) $| f ( z ) | \leq z ,$ , and

(iii) ${ \mathrm { i f ~ } } | f ^ { \prime } ( 0 ) | = 1 { \mathrm { ~ o r ~ } } | f ( z ) | = z$ for any $z \in \mathbb { D }$ , then $f ( z ) = c z$ for some $| c | = 1$

3. Generalized Schwarz’s Lemma: Suppose $f : \mathbb { D } \to \mathbb { D }$ is analytic. Then

(i) $| f ^ { \prime } ( a ) | \leq { \frac { 1 - | f ( a ) | ^ { 2 } } { 1 - | a | ^ { 2 } } } ,$

(ii) if equality, then $f ( z ) = \varphi _ { - a } ( c \varphi _ { a } ( z ) )$

4. Logarithmic Convexity: Let $a < b , G = \{ z \in \mathbb { C } \mid a < \mathrm { R e } \ z < b \}$ , and $f : \overline { { G } } \to \mathbb { C }$ . If f is continuous on ${ \overline { { G } } } ,$ analytic on G and bounded, then $M ( x ) = \operatorname* { s u p } _ { y \in \mathbb { R } } | f ( x + i y ) |$ is logarithmically convex.

5. Phragm\`en-Lindel¨of: Let G be simply connected, $f : G \to \mathbb { C }$ analytic, and suppose there exists $\varphi : G \to \mathbb { C }$ analytic, bounded, and nonzero on G. Suppose further that $\partial _ { \infty } G = A \cup B$ and

(i) for all $a \in A , \operatorname* { l i m } _ { z \to a } \operatorname* { s u p } | f ( z ) | \leq M$

(ii) for all $b \in B .$ , for all $\eta > 0 .$ , lim $\operatorname* { s u p } | f ( z ) | | \varphi _ { ( } a ) | ^ { \eta } \leq M$ 2 z→b

then $| f ( z ) | \leq M$ on G.

6. Logic of the ρ metric: For all $\epsilon > 0$ , there exist $\delta > 0$ and $K \subseteq G$ compact such that

$$
\rho _ { K } ( f , g ) < \delta \Longrightarrow \rho ( f , g ) < \epsilon
$$

and for all δ > 0, K compact, there exists an  such that

$$
\rho ( f , g ) < \epsilon \Longrightarrow \rho _ { K } ( f , g ) < \delta
$$

7. Spaces of Continuous Functions: If Ω is complete, then $C ( G , \Omega )$ is complete.

8. Normal Families: ${ \mathcal { F } } \subseteq C ( G , \Omega ) . \ { \mathcal { F } }$ is normal if all sequences have a convergent subsequence.

$\mathcal { F }$ is normal iff $\overline { \mathcal { F } }$ is compact iff $\mathcal { F }$ is totally bounded (i.e. for all $K , \delta > 0$ , there exist $f _ { 1 } , \ldots , f _ { n } \in { \mathcal { F } }$ such that $\begin{array} { r } { \mathcal { F } \subseteq \bigcup _ { i = 1 } ^ { n } \{ g \in C ( G , \Omega ) \mid \rho _ { K } ( f ; g ) < \delta \} } \end{array}$

## 9. Arzela-Ascoli: F is normal iff

(i) for all $z \in G , \{ f ( z ) \mid f \in { \mathcal { F } } \}$ has compact closure in Ω, and

(ii) for all $z \in G , { \mathcal { F } }$ is equicontinuous at z (for all $\epsilon > 0$ , there exists $\delta > 0$ such that $| z - w | < \delta \Rightarrow d ( f ( z ) , f ( w ) ) < \epsilon$ for all $f \in \mathcal F )$ •

10. The Space of Holomorphic Functions: Some useful facts:

(a) $f _ { n } \to f \Longleftrightarrow$ for all compact $K \subseteq G , f _ { n } \to f$ uniformly on K.

(b) $\{ f _ { n } \}$ in $H ( G ) , f \in C ( G , \mathbb { C } )$ , then $f _ { n } \to f \Longrightarrow f \in H ( G ) ( \operatorname { I f } f _ { n }$ converges, it will converge to an analytic function).

(c) $f _ { n } \to f \mathrm { ~ i n ~ } H ( G ) \Longrightarrow f _ { n } ^ { ( k ) } \to f ^ { ( k ) }$ (If f converges, its derivatives converge).

(d) H(G) is complete (Since H(G) is closed and $C ( G , \mathbb { C } )$ is complete).

11. Hurwitz’s Theorem: Let $\{ f _ { n } \} \in H ( G ) , f _ { n } \to f , f \not \equiv 0$ . Let ${ \overline { { B ( a ; r ) } } } \subseteq G$ such that $f \neq 0$ on $| z - a | = r$ . Then there exists an N such that $n \geq N \Longrightarrow f _ { n }$ and f have the same number of zeros in $B ( a ; r )$

Corollary: If $f _ { n }  f$ and $f _ { n } \neq 0 .$ , then either $f ( z ) \equiv 0 { \mathrm { ~ o r ~ } } f ( z ) \neq 0$

12. Local Boundedness: A set $\mathcal { F }$ in $H ( G )$ is locally bounded iff for each compact set $K \subset G$ there is a constant M such that $| f ( z ) | \leq M$ for all $f \in \mathcal F$ and $z \in K$ $( \mathrm { A l s o } , \mathcal { F }$ is locally bounded if for each point in G, there is a disk on which $\mathcal { F }$ is uniformly bounded.)

13. Montel’s Theorem: ${ \mathcal { F } } \subseteq H ( G )$ , then F is normal $\Longleftrightarrow \mathcal F$ is locally bounded (for all K compact, there exists M such that $f \in { \mathcal { F } } \Rightarrow | f ( z ) | \leq M$ for all $z \in K )$ .

Corollary: $\mathcal { F }$ is compact iff $\mathcal { F }$ is closed and locally bounded.

14. Meromorphic/Holomorphic Functions: If $\left\{ f _ { n } \right\}$ in $M ( G ) { \mathrm { ~ ( o r ~ } } H ( G ) )$ and $f _ { n }  f$ in $C ( G , \mathbb { C } _ { \infty } )$ , then either $f \in M ( G )$ (or H(G)) or $f \equiv \infty$

15. Riemann Mapping Theorem: G simply connected region which is not C. Let $a \in G$ , then there is a unique analytic function such that:

(a) f(a) = 0 and $f ^ { \prime } ( a ) > 0 ;$

(b) f is one-to-one;

(c) $f ( G ) = \mathbb { D } .$

16. Infinite Products: Some propositions for convergence of infinite products:

(a) Re $z _ { n } > 0$ . Then $\prod z _ { n }$ converges to a nonzero number iff $\sum \log z _ { n }$ converges.

(b) Re $z _ { n } > - 1$ . Then $\sum \log ( 1 + z _ { n } )$ converges absolutely iff $\sum z _ { n }$ converges absolutely.

(c) Re $z _ { n } > 0$ . Then $\prod z _ { n }$ converges absolutely iff $\textstyle \sum ( z _ { n } - 1 )$ converges absolutely.

17. Products Defining Analytic Functions: G a region and $\{ f _ { n } \}$ in $H ( G )$ such that $f _ { n } \not \equiv 0$ If $\sum [ f _ { n } ( z ) - 1 ]$ converges absolutely uniformly on compact subsets of G then $\prod f _ { n }$ converges in $H ( G )$ to an analytic function $f ( z )$ . The zeros of $f ( z )$ correspond to the zeros of the $f _ { n } \mathrm { \mathrm { : } } _ { \mathrm { s } }$

18. Entire Functions with Prescribed Zeros: Let $\left\{ a _ { n } \right\}$ be a sequence with lim $| a _ { n } | = \infty$ and $a _ { n } \neq 0 . { \mathrm { ~ I f ~ } } \{ p _ { n } \}$ is a sequence of integers such that for all $r > 0$

$$
\sum _ { n = 1 } ^ { \infty } \left( { \frac { r } { | a _ { n } | } } \right) ^ { p _ { n } + 1 } < \infty ,
$$

then $f ( z ) = \prod E _ { p _ { n } } ( z / a _ { n } )$ converges in $H ( \mathbb { C } )$ and $f$ is an entire function with the correct zeros. (Note that you can choose $p _ { n } = n - 1$ and it will always converge).

19. The (Boss) Weierstrass Factorization Theorem: Let $f$ be an entire function with nonzero zeros $\left\{ a _ { n } \right\}$ with a zero of order m at $z = 0$ . Then there is an entire function g and a sequence of integers $\{ p _ { n } \}$ such that

$$
f ( z ) = z ^ { m } e ^ { g ( z ) } \prod _ { n = 1 } ^ { \infty } E _ { p _ { n } } \left( { \frac { z } { a _ { n } } } \right) .
$$

20. Existence of Analytic Functions with Given Zeros: Let G be a region and $\{ a _ { j } \}$ a sequence of distinct points with no limit point in $G , \{ m _ { j } \}$ a sequence of integers. Then there is an analytic function $f$ defined on $G$ whose only zeros are the $\boldsymbol { a } _ { j } \mathrm { \dagger s }$ with multiplicity $m _ { j }$

21. Meromorphic Functions as a Quotient of Analytic: If f is a meromorphic function on the open set $G ,$ then there are analytic functions g and h on G such that $f = g / h$ .

22. Runge’s Theorem: Let K be compact and E meet each component of $\mathbb { C } _ { \infty } \backslash K$ . If f is analytic in an open set containing K, then for any $\epsilon > 0$ , there is a rational function $R ( z )$ with poles in $E$ such that $| f ( z ) - R ( z ) | < \epsilon$ for all $z \in K$

Corollary: Let G be an open subset of the plane and E a subset of $\mathbb { C } _ { \infty } \backslash G$ meeting each component. Let $R ( G , E )$ be the set of rational functions with poles in E. If $f \in H ( G )$ then there is a sequence $\{ R _ { n } \}$ in $R ( G , E )$ such that $f = \operatorname* { l i m } R _ { n }$ . (That is, $R ( G , E )$ is dense in $H ( G ) )$ .

Corollary: $\operatorname { I f } \mathbb { C } _ { \infty } \setminus G$ is connected, then polynomials are dense in $G .$ .

23. Polynomially Convex Hull: Let K be compact. The polynomially convex hull of $K ~ ( { \hat { K } } )$ is the set of all points w such that for every polynomial $p , | p ( w ) | \leq \operatorname* { m a x } \{ | p ( z ) | | z \in K \}$ If K is an annulus, then $\hat { K }$ is the disk obtained by filling in the interior hole.

24. A Few Words on Simple Connectedness (Ha): The following are equivalent for $G \subseteq \mathbb { C }$ open, connected:

(i) G is simply connected;

(ii) $n ( \gamma ; a ) = 0$ for every closed rectifiable curve γ in G and every point $a \in \mathbb { C } \setminus G ;$

(iii) $\mathbb { C } _ { \infty } \backslash G$ is connected;

(iv) For any $f \in H ( G )$ , there is a sequence of polynomials that converges to f in $H ( G )$

(v) For any $f \in H ( G )$ and any closed rectifiable curve $\gamma$ in $G , \int _ { \gamma } f = 0 ;$

(vi) Every function $f \in H ( G )$ has a primitive;

(vii) For any $f \in H ( G )$ such that $f ( z ) \neq 0$ , there is a function $g \in H ( G )$ such that $f ( z ) =$ exp $g ( z )$

(viii) For any $f \in H ( G )$ such that $f ( z ) \neq 0$ , there is a function $g \in H ( G )$ such that $f ( z ) =$ $[ g ( z ) ] ^ { 2 } ;$ ;

(ix) G is homeomorphic to D;

(x) If $u : G $ R is harmonic then there exists a harmonic conjugate.

25. Mittag-Leffler’s Theorem: Let G be open, $\{ a _ { k } \}$ distinct points in G without a limit point in $G ,$ and $\{ S _ { k } ( z ) \}$ be a sequence of singular parts at the $\boldsymbol { a } _ { k } { \mathrm { \tilde { s } } } .$ . Then there is a meromorphic function $f$ on G whose poles are exactly the $\{ a _ { k } \}$ such that the singular part of $f$ at $a _ { k }$ is $S _ { k } ( z )$ .

26. Mean Value Property: If $u : G \to \mathbb { R }$ is a harmonic function and $\overline { { B ( a ; r ) } }$ is a closed disk contained in $G$ , then

$$
u ( a ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } u ( a + r e ^ { i \theta } ) d \theta .
$$

In fact, for $z \in B ( 0 ; r )$

$$
u ( z ) = { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \operatorname { R e } \left( { \frac { r e ^ { i \theta } + z } { r e ^ { i \theta } - z } } \right) u ( r e ^ { i \theta } ) d \theta .
$$

27. Jensen’s Formula: Let $f$ be analytic on $\overline { { B ( 0 ; r ) } }$ and suppose $a _ { 1 } , \ldots , a _ { n }$ are the zeros of $f$ in $B ( 0 ; r )$ repeated according to multiplicity. If $f ( 0 ) \neq 0$ , then

$$
\log | f ( 0 ) | = - \sum _ { k = 1 } ^ { n } \log \left( \frac { r } { | a _ { k } | } \right) + \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \log | f ( r e ^ { i \theta } ) | d \theta .
$$

28. Poisson-Jensen Formula: Let f be analytic on $\overline { { B ( 0 ; r ) } }$ and suppose $a _ { 1 } , \ldots , a _ { n }$ are the zeros of $f$ in $B ( 0 ; r )$ repeated according to multiplicity. If $f ( z ) \neq 0$ , then

$$
\log | f ( z ) | = - \sum _ { k = 1 } ^ { n } \log \left( { \frac { r ^ { 2 } - { \overline { { a _ { k } } } } z } { r ( z - a _ { k } ) } } \right) + { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \operatorname { R e } \left( { \frac { r e ^ { i \theta } + z } { r e ^ { i \theta } - z } } \right) \log | f ( r e ^ { i \theta } ) | d \theta .
$$

29. Genus, Order, and Rank of Entire Functions:

• Rank: Let $f$ be an entire function with zeros $\{ a _ { k } \}$ repeated according to multiplicity such that $| a _ { 1 } | \leq | a _ { 2 } | \leq \cdot \cdot \cdot$ . Then $f$ is of finite rank if there is a $p \in \mathbb Z$ such that

$$
\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { | a _ { n } | ^ { p + 1 } } } < \infty .
$$

If $p$ is the smallest integer such that this occurs, then $f$ is of rank $p .$ A function with only a finite number of zeros has rank 0.

• Standard Form: Let $f$ be an entire function of rank p with zeros $\{ a _ { k } \}$ . Then the canonical product

$$
f ( z ) = z ^ { m } e ^ { g ( z ) } \prod _ { n = 1 } ^ { \infty } E _ { p } \left( { \frac { z } { a _ { n } } } \right)
$$

is the standard form for $f .$

• Genus: An entire function $f$ has finite genus if $f$ has finite rank and $g ( z )$ is a polynomial. If the rank is $p$ and the degree of $g$ is $q ,$ then the genus $\mu = \operatorname* { m a x } ( p , q )$ . If f has genus $\mu ,$ then for each $\alpha > 0$ , there exists an $r _ { 0 }$ such that $| z | > r _ { 0 }$ implies

$$
\begin{array} { r } { | f ( z ) | < e ^ { \alpha | z | ^ { \mu + 1 } } . } \end{array}
$$

• Order : An entire function f is of finite order if there exists $a > 0$ and $r _ { 0 } > 0$ such that $| f ( z ) | < \exp ( | z | ^ { a } )$ for $| z | > r _ { 0 }$ . The number

$$
\lambda = \operatorname* { i n f } \{ a \mid | f ( z ) | < \exp ( | z | ^ { a } ) { \mathrm { ~ f o r ~ } } | z | { \mathrm { ~ s u f f i c i e n t l y ~ l a r g e } } \}
$$

is called the order of $f .$

If $f$ has order λ and $\epsilon > 0$ , then $| f ( z ) | < \exp ( | z | ^ { \lambda + \epsilon } )$ for all $| z |$ sufficiently large, and a z can be found, with $| z |$ as large as desired, such that $| f ( z ) | \geq \exp ( | z | ^ { \lambda - \epsilon } )$

If $f$ is of genus $\mu ,$ then $f$ is of finite order $\lambda \leq \mu + 1$

30. Hadamard’s Factorization Theorem: If $f$ is entire with finite order λ, then f has finite $\mathrm { g e n u s } \le \lambda$ . Combined with above, we have that $f$ has finite order if and only if f has finite genus. Corollary: If $f$ is entire with finite order, then for all $c \in \mathbb { C }$ with one possible exception, we can always solve $f ( z ) = c$ •

Corollary: If $f$ is entire with finite order $\lambda \notin \mathbb { Z }$ , then $f$ has an infinite number of zeros.

## 5 Special Functions

1. The Riemann Zeta Function

$$
\zeta ( s ) = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { s } } } = \prod _ { p { \mathrm { ~ p r i m e } } } { \frac { 1 } { 1 - p ^ { - s } } } \quad { \mathrm { a n d } } \quad \zeta ( s ) = \zeta ( 1 - s )
$$

This function has a pole at $s = 1$ , zeros at the negative even integers, and its remaining zeros are in the critical strip $\{ z \ | \ 0 < \mathrm { R e } \ z < 1 \}$

Riemann’s functional equation is

$$
\zeta ( z ) = 2 ( 2 \pi ) ^ { z - 1 } \Gamma ( 1 - z ) \zeta ( 1 - z ) \sin \left( \frac { 1 } { 2 } \pi z \right) .
$$

2. The Gamma Function: The gamma function is the meromorphic function on $\mathbb { C }$ with simple poles at $z = 0 , - 1 , - 2 , . .$ . defined by:

$$
{ \begin{array} { r l } & { \Gamma ( z ) = \displaystyle \int _ { 0 } ^ { \infty } e ^ { - t } t ^ { z - 1 } d t } \\ & { \qquad = { \frac { e ^ { - \gamma z } } { z } } \displaystyle \prod _ { n = 1 } ^ { \infty } \left( 1 + { \frac { z } { n } } \right) ^ { - 1 } e ^ { z / n } } \\ & { \qquad = \displaystyle \operatorname* { l i m } _ { n \to \infty } { \frac { n ! n ^ { z } } { z ( z + 1 ) \cdots ( z + n ) } } = { \frac { \Gamma ( z + n ) } { z ( z + 1 ) \cdots ( z + n - 1 ) } } . } \end{array} }
$$

The residues at each of the poles is given by

$$
\operatorname { R e s } ( \Gamma , - n ) = { \frac { ( - 1 ) ^ { n } } { n ! } } .
$$

The functional equation holds for $z \neq 0 , 1 , . . .$

$$
\Gamma ( z + 1 ) = z \Gamma ( z ) .
$$

Note further that

$$
\Gamma ( 1 - z ) \Gamma ( z ) = { \frac { \pi } { \sin ( \pi z ) } } \quad { \mathrm { a n d } } \quad { \overline { { \Gamma ( z ) } } } = \Gamma ( { \overline { { z } } } ) \quad { \mathrm { a n d } } \quad \Gamma ( 1 / 2 ) = { \sqrt { \pi } } .
$$

## 6 Theorems, part 3

1. Schwarz Reflection Principle: Let G be a region such that $G = G ^ { * }$ (symmetric with respect to real axis). If $f : G _ { + } \cup G _ { 0 } \to \mathbb { C }$ is continuous and analytic on $G _ { + }$ , and $f ( G _ { 0 } ) \subseteq \mathbb { R }$ then there is an analytic function $g : G \to \mathbb { C }$ such that $f ( z ) = g ( z )$ for $z \in G _ { + } \cup G _ { 0 }$

2. Analytic Continuations: Let $\gamma : [ 0 , 1 ] \to \mathbb { C }$ be a curve and $[ f ] _ { a }$ be a germ at $a = \gamma ( 0 )$ . An analytic continuation of $[ f ] _ { a }$ along γ is a family $( f _ { t } , G _ { t } ) , t \in [ 0 , 1 ]$ such that

(i) $\gamma ( t ) \in G _ { t }$

(ii) $[ f _ { 0 } ] _ { a } = [ f ] _ { a }$

(iii) $\forall t \in [ 0 , 1 ] , \exists \delta > 0$ such that $| s - t | < \delta \Longrightarrow \gamma ( s ) \in G _ { t }$ and $[ f _ { s } ] _ { \gamma ( s ) } = [ f _ { t } ] _ { \gamma ( s ) }$

3. Uniqueness of Analytic Continuations: Let $\gamma : [ 0 , 1 ] \to \mathbb { C }$ be a path from a to b and let $\left( f _ { t } , G _ { t } \right)$ and $( g _ { t } , B _ { t } )$ be two analytic continuations along γ such that $[ f _ { 0 } ] _ { a } = [ g _ { 0 } ] _ { a }$ . Then $[ f _ { 1 } ] _ { b } = [ g _ { 1 } ] _ { b }$

4. Analytic Continuations along FEP Homotopic Curves: Let $a \in \mathbb { C }$ and $[ f ] _ { a }$ a germ at a. If $\gamma _ { 0 }$ and $\gamma _ { 1 }$ are FEP homotopic and $[ f ] _ { a }$ admits analytic continuation along every $\gamma _ { s } , s \in [ 0 , 1 ]$ , then the analytic continuations of $[ f ] _ { a }$ along γ0 and $\gamma _ { 1 }$ are equal.

5. Monodromy Theorem: Let G be a region, $a \in G , [ f ] _ { a }$ a germ at a. If G is simply connected and admits unrestricted continuation of $[ f ] _ { a }$ . then there exists $F \in H ( G )$ such that $[ F ] _ { a } = [ f ] _ { a }$

6. Neighborhood Systems: Let X be a set and for all $x \in X , { \mathcal { N } } _ { x }$ a collection of subsets of X such that

(i) for each $U \in { \mathcal { N } } _ { x } , x \in U ;$

(ii) if $U , V \in \mathcal { N } _ { x } , \exists W \in \mathcal { N } _ { x }$ such that $W \subseteq U \cap V ;$

(iii) if $U \in \mathcal { N } _ { x }$ and $V \in \mathcal { N } _ { y }$ then for $z \in U \cap V \exists W \in { \mathcal { N } } _ { z }$ such that $W \subseteq U \cap V$

Then $\{ { \mathcal { N } } _ { x } \mid x \in X \}$ is a neighborhood system on X.

7. Sheaf of Germs: For an open set G in C let

$$
\mathcal { S } ( G ) = \{ ( z , [ f ] _ { z } ) ~ | ~ z \in G , f \mathrm { ~ i s ~ a n a l y t i c ~ a t ~ } z \} ,
$$

and define a map $\rho : \mathcal { S } ( G )  \mathbb { C }$ by $\rho ( z , [ f ] _ { z } ) = z$ . Then $( { \mathcal { S } } ( G ) , \rho )$ is the sheaf of germs of analytic functions on G.

We put a topology on the sheaf of germs by defining a neighborhood system. For $D \subseteq G$ 2 and $f \in H ( D )$ , define

$$
N ( f , D ) = \{ ( z , [ f ] _ { z } ) \mid z \in D \} .
$$

For each point $( a , [ f ] _ { a } ) \in { \mathcal { S } } ( G )$ , let

$$
\mathcal { N } _ { ( a , [ f ] _ { a } ) } = \{ N ( g , B ) \mid a \in B \mathrm { ~ a n d ~ } [ g ] _ { a } = [ f ] _ { a } \} .
$$

This is a neighborhood system on ${ \mathcal { S } } ( G )$ and the induced topology is Hausdorff.

## 8. Components of the Sheaf of Germs:

• There is a path in ${ \mathcal { S } } ( G )$ from $( a , [ f ] _ { a } )$ to $( b , [ g ] _ { b } )$ iff there is a path γ in G from a to b such that $[ g ] _ { b }$ is the analytic continuation of $[ f ] _ { a }$ along γ.

• Let ${ \mathcal { C } } \subseteq { \mathcal { S } } ( G )$ and $( a , [ f ] _ { a } ) \in \mathcal { C }$ . Then C is a component of ${ \mathcal { S } } ( G )$ iff

$\mathcal { C } = \{ ( b , [ g ] _ { b } ) ~ \vert ~ [ g ] _ { b }$ is the continuation of $[ f ] _ { a }$ along some curve in $G \}$

9. Riemann Surfaces: Fix a function element $( f , D )$ . The complete analytic function $\mathcal { F }$ associated with $( f , D )$ is the collection

$\begin{array} { r } { \mathcal { F } = \{ { \sf { g } } \} _ { z } \mid [ g ] _ { \vdots } } \end{array}$ z is an analytic continuation of $[ f ] _ { a }$ for any $a \in D \}$

Then $\mathcal { R } = \{ ( z , [ g ] _ { z } ) ~ | ~ [ g ] _ { z } \in \mathcal { F } \}$ is a component of ${ \mathcal { S } } ( \mathbb { C } )$ , and $( { \mathcal { R } } , \rho )$ is the Riemann Surface of $\mathcal { F }$ .

## 10. Complex Manifolds: Let X be a topological space.

• A coordinate chart is a pair $( U , \varphi )$ such that $U \subseteq X$ is open and $\varphi : U \to V \subseteq \mathbb { C }$ is a homeomorphism.

• A complex manifold is a pair $( X , \Phi )$ where X is connected, Hausdorff and Φ is a collection of coordinate patches on X such that

(i) each point of X is contained in at least one member of Φ and

(ii) if $( U _ { a } , \varphi _ { a } ) , ( U _ { b } , \varphi _ { b } ) \in \Phi$ with $U _ { a } \cap U _ { b } \neq \emptyset$ , then $\varphi _ { a } \circ \varphi _ { b } ^ { - 1 }$ is analytic.

11. Analytic Functions: Let $( X , \Phi )$ and $( \Omega , \Psi )$ be analytic manifolds, $f : X \to \Omega$ continuous, $a \in X$ X, and $( a ) = \alpha$ . Then f is analytic at a if for any patch $( \Lambda , \psi ) \in \Psi$ which contains α, there is a patch $( U , \varphi ) \in \Phi$ which contains a such that

(i) $f ( U ) \subseteq \Lambda ;$

(ii) $\psi \circ f \circ \varphi ^ { - 1 }$ is analytic on $\varphi ( U ) \subseteq \mathbb { C }$

## 12. Some Results on Analytic Functions:

• Let $\mathcal { F }$ be a complete analytic function with Riemann surface $( { \mathcal { R } } , \rho )$ . If $\mathcal { F } : \mathcal { R }  \mathbb { C }$ is defined by $\mathcal { F } ( z , [ f ] _ { z } ) = f ( z )$ then $\mathcal { F }$ is an analytic function.

• Compositions of analytic function are analytic

• (Limit Points) If f and g are analytic functions $X  \Omega$ and if $\{ x \in X : f ( x ) = g ( x ) \}$ has a limit point in X, then $f = g$

• (Maximum Modulus) If $f : X \to \mathbb { C }$ is analytic and there is a point $a \ \in \ X$ and a neighborhood U of a such that $| f ( a ) | \geq | f ( x ) |$ for all $x \in U$ , then f is constant.

• (Liouville) If (X, Φ) is a compact analytic manifold, then there is no non-constant analytic function from X into C.

• (Open Mapping) Let $f : X \to \Omega$ be a non-constant analytic function. If U is an open subset of X, then $f ( U )$ is open in Ω.

13. Mean Value Property: If $u : G $ R is a harmonic function and $\overline { { B ( a ; r ) } } \subset G$ then

$$
u ( a ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } u ( a + r e ^ { i \theta } ) d \theta .
$$

## 14. Maximum Principles:

I. Suppose $u : G \to \mathbb { R }$ has the MVP. If there is a point $a \in G$ such that $u ( a ) \geq u ( z )$ for all z in G, then u is constant. (Analogously, there is a Minimum Principle).

II. Let $u , v : G \to \mathbb { R }$ be bounded and continuous functions with the MVP. If for each point $a \in \partial _ { \infty } G .$

$$
\operatorname* { l i m } _ { z \to a } \operatorname* { s u p } _ { } u ( z ) \leq \operatorname* { l i m } _ { z \to a } \operatorname* { i n f } _ { } v ( z )
$$

then $u ( z ) < v ( z )$ for all z in G or $u = v$

Corollary: If a continuous function satisfying the MVP is 0 on the boundary, then it is identically 0.

III. If $\varphi : G \to$ R is a subharmonic function and there is a point $a \in G$ with $\varphi ( a ) \geq \varphi ( z )$ for all z in $G ,$ then $\varphi$ is constant.

IV. If $\varphi , \psi : G \to \mathbb { R }$ are bounded functions such that $\varphi$ is subharmonic and $\psi$ is superharmonic and for each point $a \in \partial _ { \infty } G$

$$
\operatorname* { l i m } _ { z \to a } \operatorname* { s u p } \varphi ( z ) \leq \operatorname* { l i m } _ { z \to a } \operatorname* { i n f } \psi ( z )
$$

then $\varphi ( z ) < \psi ( z )$ for all z in G or $\varphi = \psi$ is harmonic.

15. The Poisson Kernel: For $\ 0 \leq r < 1 , - \infty < \theta < \infty$ , the Poisson kernel is the following:

$$
P _ { r } ( \theta ) = \sum _ { n = - \infty } ^ { \infty } r ^ { | n | } e ^ { i n \theta } = \operatorname { R e } \left( { \frac { 1 + r e ^ { i \theta } } { 1 - r e ^ { i \theta } } } \right) = { \frac { 1 - r ^ { 2 } } { 1 - 2 r \cos \theta + r ^ { 2 } } } .
$$

16. Dirichlet Problem in the Disk: If $f : \partial \mathbb { D } \to \mathbb { R }$ is a continuous function, then there is a continuous harmonic function $u : \overline { { \mathbb { D } } } \to$ R such that $u ( z ) = f ( z )$ for all $z \in \partial \mathbb { D }$ . Moreover, u is unique and defined by

$$
u ( r e ^ { i \theta } ) = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } P _ { r } ( \theta - t ) f ( e ^ { i t } ) d t .
$$

17. Harmonicity vs. MVP: If $u : G \to \mathbb { R }$ is a continuous function which has the MVP, then u is harmonic.

18. Harnack’s Inequality: If $u : \overline { { B ( a ; R ) } } \to \mathbb { R }$ is continuous, harmonic in $B ( { a } ; R )$ , and $u \geq 0$ then for $0 \leq r < R$ and all θ

$$
{ \frac { R - r } { R + r } } u ( a ) \leq u ( a + r e ^ { i \theta } ) \leq { \frac { R + r } { R - r } } u ( a ) .
$$

19. Harnack’s Theorem: Let G be a region. The metric space $\operatorname { H a r } ( G )$ is complete. If $\{ u _ { n } \}$ is a sequence in Har(G) such that $u _ { 1 } \leq u _ { 2 } \leq . .$ . then either $u _ { n } ( z ) \to \infty$ uniformly on compact subsets of G or $\{ u _ { n } \}$ converges in Har(G) to a harmonic function.

20. Subharmonic Functions: Let $\varphi : G \to \mathbb { R }$ be continuous. Then $\varphi$ is subharmonic iff for every $G _ { 1 } \subseteq G$ and every harmonic $u _ { 1 }$ on $G _ { 1 } , \varphi - u _ { 1 }$ satisfies the Maximum Principle on $G _ { 1 }$ Corollary: $\varphi$ is subharmonic iff for every bounded region $G _ { 1 }$ such that ${ \overline { { G _ { 1 } } } } \subset G$ and for every continuous function $u _ { 1 } : \overline { { G _ { 1 } } } \to \mathbb { R }$ that is harmonic on $G _ { 1 }$ and satisfies $\varphi ( z ) \leq u _ { 1 } ( z )$ on $\partial G _ { 1 }$ $\varphi ( z ) \leq u _ { 1 } ( z )$ for $z \in G _ { 1 }$

21. Maxima of Subharmonic Functions: If $\varphi _ { 1 }$ and $\varphi _ { 2 }$ are subharmonic functions on G then $\varphi ( z ) = \mathrm { m a x } \{ \varphi _ { 1 } ( z ) \varphi _ { 2 } ( z ) \}$ is a subharmonic function.

22. Bumping Let $\varphi : G \to \mathbb { R }$ be subharmonic and ${ \overline { { B ( a ; r ) } } } \subset G$ Define $\varphi ^ { \prime } ( z ) = \varphi ( z ) { \mathrm { ~ i f ~ } } z \in$ $G \setminus B ( a ; r )$ and $\varphi ^ { \prime } ( z )$ be the solution to the Dirichlet problem for $z \in B ( a ; r )$ . Then $\varphi ^ { \prime }$ is subharmonic.

23. The Perron Function: Let $f : \partial _ { \infty } G \to \mathbb { R }$ be continuous. Then $u ( z ) = \operatorname* { s u p } \{ \varphi ( z ) \mid \varphi \in$ $\mathcal { P } ( f , G ) \}$ defines a harmonic function on $G .$

$( { \mathcal { P } } ( f , G ) = \{ \varphi : G \to \mathbb { R } \mid \varphi$ subharmonic, lim $\begin{array} { r } { \operatorname* { s u p } _ { z \to a } \varphi ( z ) \le f ( a ) \forall a \in \partial _ { \infty } G \} ) } \end{array}$

24. General Dirichlet Problem: A region G is a Dirichlet Region iff there is a barrier for G at each point of $\partial _ { \infty } G$

(A barrier for G at a is a family $\{ \psi _ { r } \}$ such that $\psi _ { r }$ is superharmonic on $G ( a ; r )$ with $0 \leq$ $\psi _ { r } ( z ) \leq 1 , \operatorname* { l i m } _ { z  a } \psi _ { r } ( z ) = 0$ , and lim $\psi _ { r } ( z ) = 1$ for $w \in G \cap \{ w \mid | w - a | = r \} . )$ z→w

Corollary: Let G be a region such that no component of $\mathbb { C } _ { \infty } \backslash G$ reduces to a point, then G is a Dirichlet region.

Corollary: A simply connected region is a Dirichlet region.