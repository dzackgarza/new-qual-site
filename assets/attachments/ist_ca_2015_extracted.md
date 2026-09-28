# PROBLEMS IN COMPLEX ANALYSIS

## SAMEER CHAVAN

## 1. A Maximum Modulus Principle for Analytic Polynomials

In the following problems, we outline two proofs of a version of Maximum Modulus Principle. The first one is based on linear algebra (not the simplest one).

Problem 1.1 (Orr Morshe Shalit, Amer. Math. Monthly). Let $p ( z ) = a _ { 0 } + a _ { 1 } z +$ $\cdots + a _ { n } z ^ { n }$ be an analytic polynomial and let $s : = \sqrt { 1 - | z | ^ { 2 } } \ f o r \ z \in \mathbb { C }$ with $| z | \leq 1$ Let $e _ { i }$ denote the column $n \times 1$ matrix with 1 at the ith place and 0 else. Verify:

(1) Consider the $( n + 1 ) \times ( n + 1 )$ matrix U with columns $z e _ { 1 } + s e _ { 2 } , e _ { 3 } , e _ { 4 } , \cdot \cdot \cdot , e _ { n + 1 } $ and $s e _ { 1 } - \bar { z } e _ { 2 }$ (in order). Then U is unitary with eigenvalues $\lambda _ { 1 } , \cdots , \lambda _ { n + 1 }$ of modulus 1 (Hint. Check that columns of U are mutually orthonormal).

(2) $z ^ { k } = ( e _ { 1 } ) ^ { t } U ^ { k } e _ { 1 }$ (Check: Apply induction on k), and hence

$$
p ( z ) = ( e _ { 1 } ) ^ { t } p ( U ) e _ { 1 } .
$$

(3) ma $\tau _ { | z | \leq 1 } | p ( z ) | \leq \| p ( U ) \|$ (Hint. Recall that $\| A B \| \leq \| A \| \| B \| )$

(4) If D is the diagonal matrix with diagonal entries $\lambda _ { 1 } , \cdots , \lambda _ { n + 1 }$ then

$$
\| p ( U ) \| = \| p ( D ) \| = \operatorname* { m a x } _ { i = 1 , \cdots , n + 1 } | p ( \lambda _ { i } ) | .
$$

Conclude that ma $\mathbf { x } _ { | z | \leq 1 } | p ( z ) | = \operatorname* { m a x } _ { | z | = 1 } | p ( z ) |$

Problem 1.2 (Walter Rudin, Real and Complex Analysis). Let $p ( z ) = a _ { 0 } + a _ { 1 } z +$ $\cdots + a _ { n } z ^ { n }$ be an analytic polynomial. Let z0 $\in \ \mathbb { C }$ be such that $| f ( z ) | \leq | f ( z _ { 0 } ) |$ Assume $| z _ { 0 } | < 1$ , and write $p ( z ) = b _ { 0 } + b _ { 1 } ( z - z _ { 0 } ) + \cdot \cdot \cdot + b _ { n } ( z - z _ { 0 } ) ^ { n } . ~ { f f } 0 < r < 1 - | z _ { 0 } |$ then verify the following:

$$
\begin{array} { r } { \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } | p ( z + r e ^ { i \theta } ) | ^ { 2 } d \theta = | b _ { 0 } | ^ { 2 } + | b _ { 1 } | ^ { 2 } r ^ { 2 } + \cdot \cdot \cdot + | b _ { n } | ^ { 2 } r ^ { 2 n } . } \end{array}
$$

(2) $\begin{array} { r } { \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } | p ( z + r e ^ { i \theta } ) | ^ { 2 } d \theta \leq | b _ { 0 } | ^ { 2 } . } \end{array}$

Conclude that $i f p$ is non-constant then max $\ L _ { | z | \leq 1 } | p ( z ) | = \operatorname* { m a x } _ { | z | = 1 } | p ( z ) |$

Problem 1.3. Let $\textstyle f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ converges uniformly on the closed unit disc. Show that max $_ { | z | \leq 1 } | f ( z ) | = \operatorname* { m a x } _ { | z | = 1 } | f ( z ) |$

## 2. Zeros of Analytic Polynomials

Problem 2.1 (Anton R. Schep, Amer. Math. Monthly). Let $f : \mathbb { C } \to \mathbb { C }$ be an entire function such that $f ( z ) \neq 0$ for any $z \in \mathbb { C }$ . For a positive number r, verify the following:

(1) $\begin{array} { r } { \int _ { | z | = r } { \frac { d z } { z f ( z ) } } = { \frac { 2 \pi i } { f ( 0 ) } } , w h e r e | z | = r } \end{array}$ is traversed in counter clockwise direction.

(2) $\begin{array} { r } { \left| \int _ { | z | = r } \frac { d z } { z f ( z ) } \right| \le \frac { 2 \pi } { \operatorname* { m i n } _ { | z | = r } | f ( z ) | } } \end{array}$ , and hence min $\left| \boldsymbol { \mathbf { \mathit { 1 } } } \right| z | = r \left| f ( z ) \right| \leq \left| f ( 0 ) \right|$

Deduce the fact that an analytic polynomial admits a zero in the complex plane (known as Fundamental Theorem of Algebra) by verifying

$$
| a _ { 0 } + a _ { 1 } z + \cdot \cdot \cdot + a _ { n - 1 } z ^ { n - 1 } + z ^ { n } | \geq | z | ^ { n } ( 1 - | a _ { n - 1 } | / | z | - \cdot \cdot \cdot - | a _ { 0 } | / | z ^ { n } | ) .
$$

Remark 2.2 : The conclusion in (2) is applicable to the exponential function. What does it say ?

Theorem 2.3 (Rouch´e’s Theorem). Suppose that f and g are holomorphic in an open set containing a circle C and its interior. $I f \left| f ( z ) \right| > \left| g ( z ) \right|$ | for $a l l z \in C$ , then f and $f + g$ have the same number of zeros inside the circle C.

We will prove Rouch´e’s Theorem in the next section. Let us use it to prove an interesting statement about zeros of analytic polynomials.

Problem 2.4 (Jim Agler, Online Notes). Consider the analytic polynomial $p ( z ) =$ $a _ { 0 } + a _ { 1 } z + \cdots + a _ { n - 1 } z ^ { n - 1 } + z ^ { n }$ and let $R : = \sqrt { | a _ { 0 } | ^ { 2 } + \cdots + | a _ { n - 1 } | ^ { 2 } + 1 }$ . Verify:

(1) If R = 1 then the set of zeros of $p ( z )$ is singleton {0}, and hence contained in any open disc with center 0.

(2) Assume $R > 1 . \ I f \left| z \right| = R$ then

$$
| z ^ { n } - p ( z ) | < | z ^ { n } |
$$

(Hint. Use Cauchy-Schwarz inequality).

The set of zeros of $p ( z )$ is contained in the open disc with center 0 and radius R.

## 3. Argument Principle and its Consequences

For any non-zero complex number $z = | z | e ^ { i \theta }$ , where θ is unique up to a multiple of 2π, one may define argument of z as θ (θ is the $\mathrm { \ddot { \mathrm { \Omega } } a n g l e \mathrm { \uparrow } }$ between the X-axis and the half-line starting at the origin and passing through z with positive counter clockwise orientation). But then argument is not a function in the sense that it is multi-valued $( \mathrm { e . g . ~ \ a r g ( 1 ) }$ is 0 as well as any integer multiple of 2π). However, $\arg ( z ) : = \theta$ mod 2π (to be referred to as the principle branch of argument) defines a well-defined function on the punctured plane $\mathbb { C } ^ { * } : = \mathbb { C } \setminus \{ 0 \}$

Problem 3.1. Show that arg $: \mathbb { C } ^ { * } \to [ 0 , 2 \pi )$ is not a continuous function. What is the set of discontinuities of arg ?

Remark 3.2 : The restriction arg $| \mathbb { C } ^ { * } \backslash [ 0 , \infty )$ is continuous. Thus we have a continuous “branch” log $: \mathbb { C } ^ { * } \setminus [ 0 , \infty )  \mathbb { C }$ of logarithm given by log $z = \log | z | + \arg ( z )$

Later we will see that a branch of logarithm always exists on any simply connected domain not containing origin. On domains which are not simply connected, it may be impossible to define a branch f logarithm. It is interesting to know in this context that there exist analytic functions with an analytic branch of square-root but without an analytic branch of logarithm.

Problem 3.3 (Jim Agler, Online Notes). Consider $f ( z ) = z ^ { 2 } - 1$ on $\Omega : = \mathbb { C } \backslash [ - 1 , 1 ]$ Let $g : \Omega \to \mathbb { C }$ be defined by

$$
g ( z ) : = | f ( z ) | ^ { 1 / 2 } e ^ { i ( \arg ( z - 1 ) + \arg ( z + 1 ) ) / 2 } .
$$

Verify the following:

(1) g is a well-defined continuous function on Ω satisfying $g ^ { 2 } = f$

(2) g is analytic (Hint. $s \circ g = f _ { \cdot }$ , where $s ( z ) = z ^ { 2 }$ which is locally one-to-one on the punctured plane $\mathbb { C } ^ { * } )$

Show further that f does not have an analytic logarithm on $\Omega$

In an effort to understand (when one can define) logarithm of a holomorphic function $f : \Omega \to \mathbb { C } ^ { * }$ , we must understand the change in the argument

$$
\log f : = \int _ { \gamma } { \frac { f ^ { \prime } ( z ) } { f ( z ) } } d z { \mathrm { ~ ( m i n u s ~ t h e ~ m o d u l u s ~ } } \log | f ( z ) | )
$$

of $f$ as z traverses the curve $\gamma .$ . The argument principle says that for a closed curve $\gamma$ (that is a curve with same values at end-points), log f is completely determined by the zeros and poles of $f$ inside $\gamma .$ .

A function f on an open set Ω is meromorphic if there exists a sequence of points $A : = \{ z _ { 0 } , z _ { 1 } , z _ { 2 } , \cdot \cdot \cdot \}$ that has no limit points in Ω, and such that

(1) the function $f$ is holomorphic in $\Omega \setminus A .$ and

(2) f has poles at the points in $A .$

Recall that a function f defined in a deleted neighborhood of $z _ { \mathrm { 0 } }$ has a pole at $z _ { \mathrm { 0 } }$ , if the function $1 / f ,$ defined to be zero at $z _ { 0 } .$ , is holomorphic in a full neighborhood of $z _ { \mathrm { 0 } } .$ . Equivalently, f has a pole at $z _ { 0 }$ if there exist a unique positive integer n (to be referred to as the order of the pole) and a holomorphic function non-vanishing in a neighborhood of $z _ { 0 }$ such that $f ( z ) = ( z - z _ { 0 } ) ^ { - n } h ( z )$ holds in that neighborhood.

Theorem 3.4 (Argument Principle). Suppose $f$ is meromorphic in an open set containing a circle C and its interior. $I f f$ has no poles and zeros on $C _ { i }$ , then

$$
\frac { 1 } { 2 \pi i } \int _ { C } \frac { f ^ { \prime } ( z ) } { f ( z ) } d z = n _ { z } ( f ) - n _ { p } ( f ) ,
$$

where $n _ { z } ( f )$ is the number of zeros of f inside $C , n _ { p } ( f )$ is the number of poles of f inside $C ,$ and the zeros and poles are counted with their multiplicities.

Outline of Proof. We need the formula

$$
{ \frac { { \bigl ( } \prod _ { k = 1 } ^ { N } f _ { k } { \bigr ) } ^ { \prime } } { \prod _ { k = 1 } ^ { N } f _ { k } } } = \sum _ { k = 1 } ^ { N } { \frac { f _ { k } ^ { \prime } } { f _ { k } } } ,
$$

which may be proved by induction on N. For $N = 1$ , it is trivial. Assuming the formula for $k = N - 1$ , by the product rule,

$$
{ \frac { \left( \prod _ { k = 1 } ^ { N } f _ { k } \right) ^ { \prime } } { \prod _ { k = 1 } ^ { N } f _ { k } } } = { \frac { \left( \prod _ { k = 1 } ^ { N - 1 } f _ { k } \right) ^ { \prime } } { \prod _ { k = 1 } ^ { N - 1 } f _ { k } } } + { \frac { f _ { N } ^ { \prime } } { f _ { N } } } = \sum _ { k = 1 } ^ { N } { \frac { f _ { k } ^ { \prime } } { f _ { k } } } .
$$

If f has a zero at $z _ { \mathrm { 0 } }$ of order n then $f ( z ) = ( z - z _ { 0 } ) ^ { n } g ( z )$ in the interior of $C$ for a non-vanishing function $g .$ It is easy to see that $\textstyle \int _ { C } f ^ { \prime } / f = n$ . Similarly, If f has a zero at $z _ { 0 }$ of order n then $\textstyle \int _ { C } f ^ { \prime } / f = - n$ 

Outline of Proof of Rouch´e’s Theorem. $\mathrm { A p p l y }$ the Argument Principle to $f + t g$ for $t \in [ 0 , 1 ]$ to conclude that $\begin{array} { r } { n _ { z } ( f _ { t } ) = \int _ { C } \frac { f _ { t } ^ { \prime } ( z ) } { f _ { t } ( z ) } d z } \end{array}$ is an integer-valued, continuous function of t, and hence by Intermediate Value Theorem, $n _ { z } ( f _ { 0 } ) = n _ { z } ( f _ { 1 } )$ , that is, $n _ { z } ( f ) = n _ { z } ( f + g )$ 

Problem 3.5. Let f be non-constant and holomorphic in an open set containing the closed unit disc. $I f | f ( z ) | = 1$ whenever $| z | = 1$ then the following hold true:

(1) $f ( z ) = 0 ~ f o r ~ z$ in the open unit disc (Hint. Maximum Modulus Principle).

(2) $f ( z ) = w _ { 0 }$ has a root for every $| w _ { 0 } | < 1$ , that $i s ,$ the image of f contains the unit disc (Hint. Rouch´e’s Theorem).

Problem 3.6. Show that the functional equation $\lambda = z + e ^ { - z } \left( \lambda > 1 \right)$ has exactly one (real) solution in the right half plane.

Problem 3.7. Find the number of zeros of $3 e ^ { z } - z$ in the closed unit disc centered at the origin.

## 4. Hurwitz’s Theorem

Theorem 4.1 (Hurwitz’s Theorem). Let $\{ f _ { n } \}$ be a sequence of nowhere-vanishing holomorphic functions converging compactly to holomorphic f. Then either $f = 0$ or $f$ is nowhere-vanishing.

Proof. Suppose $f \neq 0$ . Let C be a circle enclosing a zero of f such that f does not vanish on it. Note that $f _ { n } ( \mathrm { r e s p . } \ f _ { n } ^ { \prime } )$ converges uniformly to $f \ ( \mathrm { r e s p . } \ f ^ { \prime } )$ on C (Justify). Apply now Argument Principle to $f _ { n } ^ { \prime } / f _ { n }$ to get a contradiction. 

Problem 4.2. Show that at least one partial sum of the cosine series has a zero in the disc with center and radius $\pi / 2$

Problem 4.3. Let $\left\{ f _ { n } \right\}$ be a sequence of injective holomorphic functions converging compactly to holomorphic f. Show that either f constant or f is injective.

## 5. Open Mapping Theorem

Theorem 5.1 (Open Mapping Theorem). A non-constant holomorphic function f on a open connected set Ω maps open sets to open sets.

Proof. Let $w _ { 0 }$ be such that $w _ { 0 } = f ( z _ { 0 } )$ for some $z _ { \mathrm { 0 } }$ . Define $g ( z ) : = f ( z ) - w$ and write $g ( z ) = F ( z ) + G ( z )$ , where $F ( z ) : = ( f ( z ) - w _ { 0 } ) , G ( z ) : = ( w _ { 0 } - w )$ . Now choose $\delta > 0$ such that the closed disc centered at z0 and of radius δ is contained in $\Omega ,$ Ω, and f does not vanish on the circle $| z | = \delta$ . We then select $\epsilon > 0$ so that we have $| f ( z ) - w _ { 0 } | \ge \epsilon$ on C. Now $\mathrm { i f ~ } | w - w _ { 0 } | < \epsilon$ then $| F ( z ) | > | G ( z ) |$ on $| z | = \delta$ , and by Rouch´e’s Theorem, $g ( z ) = F ( z ) + G ( z ) = 0$ for some $| z | < \delta$ since $F ( z _ { 0 } ) = 0$ 

Problem 5.2. Let $\Omega \subseteq \mathbb { C }$ be an open set. Show that $| \Omega | : = \{ | z | : z \in \Omega \}$ is relatively open in non-negative real numbers R+ (Hint. Let $U \subseteq \Omega$ be open. Pick up $b \in | U |$ and fix $a \in U$ such that $| a | = b$ . Choose $0 < r < | a |$ such that $\mathbb { D } _ { r } ( a ) \subseteq U .$ Check that $| \mathbb { D } _ { r } ( a ) | = ( | a | - r , | a | + r ) . ,$ )

Problem 5.3 (Maximum Modulus Principle for Open Mappings). Let $f : \Omega \to \mathbb { C }$ be an open mapping defined on open set $\Omega \subset \mathbb { C }$ . Define $\vert f \vert : \Omega  \mathbb { R } _ { + } \ b y \vert f \vert ( z ) = \vert f ( z ) \vert$ Verify the following statements:

(1) |f| can not have a (local) maximum at $a \in \Omega$

(2) If Ω is compact and f is continuous on Ω then $| f |$ attains a maximum on the boundary of Ω.

Remark 5.4 : By the Open Mapping Theorem, we obtain Maximum Modulus Principle for holomorphic functions.

Problem 5.5. Let $D \subseteq \mathbb { C }$ be a domain, $B \subseteq D$ an open and bounded subset such that ${ \overline { { B } } } \subseteq D$ . If f is holomorphic in D then show that the boundary $\partial ( f ( B ) )$ of $f ( B )$ is contained in $f ( \partial B )$

Conclude that this is not true if B is unbounded.

Problem 5.6 (Minimum Modulus Principle). Let f be a non-constant holomorphic function on a bounded open set Ω such that f is continuous on Ω. Show that either f has a zero in Ω or |f | assumes its minimum on the boundary of Ω.

## 6. Schwarz’s Lemma

Let $f : \mathbb { D }  \mathbb { D }$ be a holomorphic function such that $f ( 0 ) = 0$ . Then $f ( z ) =$ $\textstyle \sum _ { n = 1 } ^ { \infty } a _ { n } z ^ { n } = z g ( z )$ , where $\begin{array} { r } { g ( z ) = \sum _ { n = 1 } ^ { \infty } a _ { n } z ^ { n - 1 } } \end{array}$ is holomorphic on D. Note that $| f ( z ) | < 1$ , and hence $| g ( z ) | < 1 / | z |$ for every $z \in \mathbb { D }$ . Thus for $| z | = r , | g ( z ) | \leq 1 / r$ Hence, by Maximum Modulus Principle, $| g ( z ) | \leq 1 / r$ for every $| z | \leq r .$ Fixing z and letting $r \uparrow 1$ , we obtain $| g ( z ) | \leq 1$

Theorem 6.1 (Schwarz’s Lemma). Let $f : \mathbb { D } \to \mathbb { \Lambda }$ D be a holomorphic function such that $f ( 0 ) = 0$ . Then $| f ( z ) | \leq | z |$ and $| f ^ { \prime } ( 0 ) | \le 1$ . Moreover, $f ( z ) = e ^ { i \theta } z$ for some $\theta \in [ 0 , 2 \pi )$ if either $| f ( z _ { 0 } ) | = | z _ { 0 } |$ for some non-zero $z _ { 0 } \in \mathbb { D }$ or $\left| f ^ { \prime } ( 0 ) \right| = 1$

Proof. To see the remaining half, apply Maximum Modulus Principle to $f ( z ) / z . \quad \bigsqcup$

Let us see some applications of Schwarz’s Lemma.

Corollary 6.2 (Automorphisms of Unit Disc). Every biholomorphism of the open unit disc is one of the following: a rotation $r _ { \theta } ( z ) : = e ^ { i \theta } z$ for some $\theta \in [ 0 , 2 \pi )$ , $\textstyle \psi _ { a } ( z ) : = { \frac { a - z } { 1 - z \bar { a } } }$ for some $| a | < 1$ , or compositions of rθ and $\psi _ { a }$

Proof. Let $f : \mathbb { D } \to \mathbb { D }$ be a biholomorphism, that is, a holomorphic mapping such that f is one-to-one, onto, and $f ^ { - 1 }$ is holomorphic. Suppose $f ( a ) = 0$ for some $| a | < 1$ . Note that $\psi _ { a }$ maps D bijectively onto D with $\psi _ { a } ^ { - 1 } = \psi _ { a }$ . Set $g : = f \circ \psi _ { a } ,$ and note that $g ( 0 ) = 0$ . By Schwarz’s Lemma, $| g ( z ) | \leq | z |$ for every $| z | < 1$ Applying same argument to $g ^ { - 1 }$ , we obtain $| g ^ { - 1 } ( z ) | \leq | z |$ for every $| z | < 1$ . Hence, by Schwarz’s Lemma, g is a rotation. 

Problem 6.3 (Transitivity of the Automorphism Group). Show that the group $A u t ( \mathbb { D } ) : = \{ f : \mathbb { D } \to \mathbb { D } : f$ is a biholomorphism} of automorphisms of the open unit disc is transitive, that is, for every $a , b$ in the open unit disc, there exists $f \in A u t ( \mathbb { D } )$ such that $f ( a ) = b$

Corollary 6.4 (A Fixed Point Theorem). Let $f : \mathbb { D } \to \mathbb { D }$ be a holomorphic function. Then either $f ( z ) = z o r f$ can have at most one fixed point.

Proof. Let $a , b \in \mathbb { D }$ such that $f ( a ) = a$ and $f ( b ) = b .$ . Let $g : = \psi _ { a } \circ f \circ \psi _ { a } .$ and note that g maps D into D such that $g ( 0 ) = 0$ . Also, if $c : = \psi _ { a } ( b )$ then $g ( c ) = c .$ Since $a \neq b , c \neq 0$ . Hence, by Schwarz’s Lemma, $g ( z ) = e ^ { i \theta } z$ for some $\theta \in [ 0 , 2 \pi )$ , and hence $f = \psi _ { a } \circ ( e ^ { i \theta } \psi _ { a } ( z ) )$ . But then $b = \psi _ { a } ( e ^ { i \theta } c )$ , and hence $c = e ^ { i \theta } c$ . It follows that $\theta = 0 ,$ and $f ( z ) = z .$ 

## 7. Simple Connectivity and Cauchy’s Theorem

Let $\gamma _ { 0 }$ and $\gamma _ { 1 }$ be two curves in an open set Ω with common end-points, that is, $\gamma _ { 0 } ( a ) = \alpha = \gamma _ { 1 } ( a )$ and $\gamma _ { 0 } ( b ) = \beta = \gamma _ { 1 } ( b )$ . These two curves are said to be homotopic in Ω if for each $0 \leq s \leq 1$ , there exists a curve $\gamma _ { s }$ in Ω defined on $[ a , b ]$ such that for every $s \in [ 0 , 1 ] , \ : , \ : \gamma _ { s } ( a ) = \alpha , \gamma _ { s } ( b ) = \beta$ , and for all $t \in [ a , b ]$

$$
\gamma _ { s } ( t ) _ { \mid } s = 0 = \gamma _ { 0 } ( t ) , \gamma _ { s } ( t ) \vert _ { s = 1 } = \gamma _ { 1 } ( t ) .
$$

Moreover, $\gamma _ { s } ( t )$ should be jointly continuous in $s \in [ 0 , 1 ]$ and $t \in [ a , b ]$

Remark 7.1 : Any two curves in a convex region are homotopic. One may take $\gamma _ { s } ( t ) : = ( 1 - s ) \gamma _ { 0 } ( t ) + s \gamma _ { 1 } ( t )$

Problem 7.2. Show that the complex plane minus a half-line is simply connected (Hint. Use polar co-ordinates).

In this section, we discuss the following notions of simply connectedness:

(1) A region Ω is simply connected if any two curves in Ω with the same endpoints are homotopic.

(2) A region Ω is topologically simply connected if its complement in the Riemann sphere is connected.

(3) A region Ω is holomorphically simply connected if whenever $\gamma \subseteq \Omega$ is closed and f is holomorphic in Ω then $\begin{array} { r } { \int _ { \gamma } f ( z ) d z = 0 } \end{array}$

It turns out that all these notions are equivalent [2, Appendix $\mathrm { A l }$ . Let us see an argument that ensures the implication (3) implies (1). Suppose that Ω is holomorphically simply connected. If $\Omega = \mathbb { C } .$ , then it is clearly simply connected. If Ω is not all of C, in view of the proof Riemann Mapping Theorem as presented in $[ 2 ,$ Chapter 8]), Ω is biholomorphically equivalent to the unit disc. Since the unit disc is simply connected, the same must be true of Ω. The implication (1) implies (3) follows from homotopic version of Cauchy’s Theorem.

Theorem 7.3 (Homotopy Version of Cauchy’s Theorem). If f is holomorphic in Ω, then $\begin{array} { r } { \int _ { \gamma _ { 0 } } f ( z ) d z = \int _ { \gamma _ { 1 } } f ( z ) d z } \end{array}$ whenever the two curves γ0 and $\gamma _ { 1 }$ are homotopic in Ω.

Proof. Note that $F ( s , t ) = \gamma _ { s } ( t )$ is jointly continuous on $[ 0 , 1 ] \times [ a , b ]$ . In particular, $K : = F ( [ 0 , 1 ] \times [ a , b ] )$ is compact. We divide the proof into following steps:

(1) There exists $\epsilon > 0$ such that every disc of radius 3 centered at a point in K is completely contained in Ω (Justify).

(2) One can find $\delta > 0$ so that

$$
\operatorname* { s u p } _ { t \in [ a , b ] } | \gamma _ { s _ { 1 } } ( t ) - \gamma _ { s _ { 2 } } ( t ) | < \epsilon { \mathrm { ~ w h e n e v e r ~ } } | s _ { 1 } - s _ { 2 } | < \delta .
$$

This is possible in view of the uniform continuity of $F .$

(3) Let $s _ { 1 } , s _ { 2 }$ be such that $| s _ { 1 } - s _ { 2 } | < \delta .$ Choose discs $\{ D _ { 0 } , \cdots , D _ { n } \}$ of radius $2 \epsilon ,$ and consecutive points $\{ z _ { 0 } , \cdot \cdot \cdot , z _ { n + 1 } \}$ on $\gamma _ { s _ { 1 } }$ and $\{ w _ { 0 } , \cdot \cdot \cdot , w _ { n + 1 } \}$ on $\gamma _ { s _ { 2 } }$ such that the union of these discs covers both curves, $z _ { 0 } = w _ { 0 } , z _ { n + 1 } = w _ { n + 1 } ,$ and $z _ { i } , z _ { i + 1 } , w _ { i } , w _ { i + 1 } \in D _ { i }$

On each disc $D _ { i }$ , let $F _ { i }$ denote a primitive of $f .$ On the intersection of $D _ { i }$ and $D _ { i + 1 } , F _ { i }$ and $F _ { i + 1 }$ 1 are two primitives of the same function, so they must differ by a constant, say $c _ { i }$ . Therefore, $F _ { i + 1 } ( z _ { i + 1 } ) - F _ { i } ( z _ { i + 1 } ) = F _ { i + 1 } ( w _ { i + 1 } ) - F _ { i } ( w _ { i + 1 } )$ , hence

$$
F _ { i + 1 } ( z _ { i + 1 } ) - F _ { i + 1 } ( w _ { i + 1 } ) = F _ { i } ( z _ { i + 1 } ) - F _ { i } ( w _ { i + 1 } ) .
$$

$$
\begin{array} { r } { \int _ { \gamma _ { s _ { 1 } } } f - \int _ { \gamma _ { s _ { 2 } } } f = F _ { n } ( z _ { n + 1 } ) - F _ { n } ( w _ { n + 1 } ) - ( F _ { 0 } ( z _ { 0 } ) - F _ { 0 } ( w _ { 0 } ) ) = 0 . } \end{array}
$$

We can now complete the proof. By subdividing $[ 0 , 1 ]$ into subintervals $[ s _ { i } , s _ { i + 1 } ]$ of length less than $\delta ,$ we may go from γ0 to $\gamma _ { 1 }$ by finitely many applications of the above argument. 

Remark $\begin{array} { r } { 7 . 4 : \int _ { \gamma } f ( z ) d z = 0 } \end{array}$ for any closed curve γ that is homotopic to a constant curve in Ω.

Problem 7.5. Show that the complex plane minus a finite non-empty set is not simply connected.

Let us derive a variant of the Cauchy integral formula as an application. Let $f$ be a function holomorphic on an open set containing a circle and its interior. Let $C _ { z }$ be a circle centered at z such that $C _ { z }$ is contained in the interior of $C .$ . Since $\frac { f ( w ) } { w - z }$ is holomorphic except at z, by the preceding theorem,

$$
\begin{array} { r c l } { \displaystyle \frac { 1 } { 2 \pi i } \int _ { C } \frac { f ( w ) } { w - z } d w } & { = } & { \displaystyle \frac { 1 } { 2 \pi i } \int _ { C ^ { \prime } } \frac { f ( w ) } { w - z } d w } \\ & { = } & { \displaystyle \frac { 1 } { 2 \pi i } \int _ { C ^ { \prime } } \frac { f ( w ) - f ( z ) } { w - z } d w + \frac { 1 } { 2 \pi i } \int _ { C ^ { \prime } } \frac { f ( z ) } { w - z } d w , } \end{array}
$$

which equals $f ( z )$ by Cauchy’s Theorem since $\frac { f ( w ) - f ( z ) } { w - z }$ is holomorphic inside $C ^ { \prime }$ with removable singularity at z.

Theorem 7.6 (Existence of a Primitive). Any holomorphic function $f$ in a simply connected domain Ω has a primitive.

Proof. Fix a point $z _ { 0 }$ in $\Omega .$ . Define $\begin{array} { r } { F ( z ) = \int _ { { \gamma } } f ( w ) d w } \end{array}$ , where $\gamma$ is any curve in Ω joining z0 to z. By the preceding theorem, the definition of $F$ is independent of the choice of $\gamma$ . To see that $F ^ { \prime } = f ,$ note that by another application of the preceding

theorem, one can write $\begin{array} { r } { F ( z + h ) - F ( z ) = \int _ { [ z , z + h ] } f ( w ) d w } \end{array}$ , where $[ z , z + h ]$ denotes the line segment joining z to $z + h$ . It follows that

$$
\left| \frac { F ( z + h ) - F ( z ) } { h } - f ( z ) \right| \leq \int _ { 0 } ^ { 1 } | f ( ( 1 - t ) z + t ( z + h ) ) - f ( z ) | d t ,
$$

which converges to 0 as $h  0$

Theorem 7.7 (Existence of a Logarithm). If f is a nowhere vanishing holomorphic function in a simply connected region Ω, then there exists a holomorphic function $F$ on Ω such that $f ( z ) = e ^ { F ( z ) }$

Proof. Fix a point $z _ { \mathrm { 0 } }$ in Ω. Define $\begin{array} { r } { F ( z ) = \int _ { \gamma } \frac { f ^ { \prime } ( w ) } { f ( w ) } d w + c _ { 0 } } \end{array}$ , where γ is any curve in Ω joining $z _ { \mathrm { 0 } }$ to z, and $c _ { 0 }$ satisfies $e ^ { c _ { 0 } } = f ( z _ { 0 } )$ . By the homotopy version of Cauchy’s Theorem, the definition of $F$ is independent of the choice of $\gamma$ . It is easy to see that $F ^ { \prime } ( z ) = f ^ { \prime } ( z ) / f ( z )$ . But then $( f e ^ { - F } ) ^ { \prime } = 0 \nonumber$ , so that $f ( z ) = c e ^ { F ( z ) }$ for some constant c. By the choice of $c _ { 0 }$ , we obtain $c = e ^ { c _ { 0 } - g ( z _ { 0 } ) } = 1$ , and hence $f ( z ) = e ^ { F ( z ) }$ 

Corollary 7.8 (Irving Glicksberg, Amer. Math. Monthly). Suppose f and g are meromorphic in a neighborhood of the closed disc $| z - a | \leq R$ with no zeros or poles on $\left| z - a \right| = R . \ I f \left| f ( z ) + g ( z ) \right| < \left| f ( z ) \right| + \left| g ( z ) \right| \ o n \ \left| z - a \right| = R _ { 1 }$ then

$$
n _ { z } ( f ) - n _ { p } ( f ) = n _ { z } ( g ) - n _ { p } ( g ) .
$$

Proof. Since $| f ( z ) / g ( z ) + 1 | < | f ( z ) / g ( z ) | + 1$ holds on $| z - a | = R$ , f /g maps $| z - a | = R$ into the simply connected region $\Omega : = \mathbb { C } \backslash ( - \infty , 0 ]$ . By the last theorem, log has a valid branch on Ω. Consider $h ( z ) : = \log ( f ( z ) / g ( z ) )$ defined on some neighborhood of $\gamma .$ Consider the closed curve $\gamma ( t ) : = f ( e ^ { i t } ) / g ( e ^ { i t } )$ for $t \in [ 0 , 2 \pi )$ in Ω. By the previous theorem, $\textstyle \int _ { \gamma } { \frac { 1 } { z } } d z = 0$ , that is,

$$
\int _ { \gamma } { \frac { ( f / g ) ^ { \prime } } { f / g } } d z = \int _ { \gamma } \left( { \frac { f ^ { \prime } } { f } } - { \frac { g ^ { \prime } } { g } } \right) d z .
$$

Now apply the Argument Principle.

Remark 7.9 : Note that ${ \mathrm { i f ~ } } | h ( z ) | < | h ( z ) + g ( z ) | + | g ( z ) | { \mathrm { ~ o n ~ } } | z - a | = R$ , then

$$
n _ { z } ( h + g ) - n _ { p } ( h + g ) = n _ { z } ( g ) - n _ { p } ( g ) .
$$

Thus we obtain a generalization of Rouch´e’s Theorem.

## 8. Range of a Holomorphic Function

Problem 8.1. Show that the range of a non-constant entire function is dense in C (Hint. Negation plus Liouville Theorem).

Problem 8.2. Show that there exists no non-constant, entire function with range contained in the complement of any half-line.

Theorem 8.3 (Casorati-Weierstrass Theorem). Suppose f is holomorphic in the punctured disc centered at $z _ { \mathrm { 0 } }$ and has an essential singularity at $z _ { \mathrm { 0 } }$ . Then, the image of the punctured disc under f is dense in the complex plane.

Proof. If possible then the image of the punctured disc under $f$ misses an open disc of radius R centered at some point w. Note that $\begin{array} { r } { \frac { | f ( z ) - w | } { | z - z _ { 0 } | } \leq \frac { R } { | z - z _ { 0 } | }  } \end{array}$ ∞ as $z  z _ { 0 }$ This shows that $\frac { f ( z ) - w } { z - z _ { 0 } }$ has pole at $z _ { \mathrm { 0 } }$ . Let $m \geq 1$ be the order of the pole. Then $| f ( z ) - w | | z - z _ { 0 } | ^ { m } \to 0$ as $z  z _ { 0 }$ . But then by triangle inequality,

$$
| f ( z ) | | z - z _ { 0 } | ^ { m } \to 0 { \mathrm { ~ a s ~ } } z \to z _ { 0 } .
$$

Thus $f ( z ) ( z - z _ { 0 } ) ^ { m - 1 }$ has removable singularity at $z _ { \mathrm { 0 } }$ , which contradicts the hypothesis that $f$ has essential singularity at $z _ { 0 }$ 

Recall that a continuous $f : U \to V$ is proper if pre-image under $f$ of any compact subset of $V$ is compact, where U and $V$ are subsets of C. Any homeomorphism is proper.

Lemma 8.4. Let $f : \mathbb { C } \to \mathbb { C }$ be a continuous mapping. Then f is a proper mapping $i f$ and only $i f \operatorname* { l i m } _ { | z | \to \infty } | f ( z ) | = \infty$

Proof. Suppose $\{ f ( z _ { n } ) \}$ is bounded for some unbounded sequence $\left\{ z _ { n } \right\}$ . Let $K \equiv$ $\textstyle { \overline { { \{ f ( z _ { n } ) \} } } }$ . Then $K$ is compact while the inverse image of $K$ under $f$ consists unbounded $\left\{ z _ { n } \right\}$ . Hence, $f$ can not be proper. Conversely, if the inverse image K of a compact set under $f$ is not compact then K being closed must be unbounded, which is impossible if lim $\operatorname { 1 } _ { | z | \to \infty } | f ( z ) | = \infty$ 

Remark 8.5 : Note that any non-constant analytic polynomial p in one variable is proper.

Corollary 8.6. An entire function f is proper if and only if it is an analytic polynomial.

Proof. For a entire, proper function $f ,$ suppose the function $g$ holomorphic in $\mathbb { C } ^ { * }$ given by

$$
g ( z ) \equiv f \left( { \frac { 1 } { z } } \right) { \big ( } z \in \mathbb { C } ^ { * } { \big ) }
$$

has essential singularity at $z = 0$ . Then, the Casorati-Weierstrass Theorem implies that for any $\delta > 0 , g ( A ^ { 1 } ( 0 , 0 , \delta ) )$ ) is dense in $\mathbb { C } .$ , where $A ^ { 1 } ( 0 , 0 , \delta )$ is the punctured disc in $\mathbb { C }$ of radius $\delta$ centered at 0. However, $g \left( A ^ { 1 } ( 0 , 0 , \delta ) \right) = f \left( A ^ { 1 } \left( 0 , { \frac { 1 } { \delta } } , \infty \right) \right)$ , so that for any $w \in \mathbb { C }$ , one can choose $z _ { n } \in A ^ { 1 } \left( 0 , n , \infty \right)$ such that $f ( z _ { n } )$ lies in the disc centered at w of radius $\textstyle { \frac { 1 } { n } }$ . It follows that $\operatorname* { l i m } _ { n \to \infty } | f ( z _ { n } ) | = | w |$ with lim $_ { { n  \infty } } | z _ { n } | = \infty$ , which clearly contradicts the assumption that $f$ is proper in view of Lemma $8 . 4$ Hence, $g$ has either a removable singularity or a pole at 0. Accordingly, either $g$ is a constant or a non-constant analytic polynomial. 

Problem 8.7 (Automorphisms of C). The group

$$
\{ f : \mathbb { C } \to \mathbb { C } : f \ i s \ e n t i r e \ w i t h \ e n t i r e \ i n v e r s e \}
$$

of automorphisms $o f \mathbb { C }$ equals $\{ a z + b : a \in \mathbb { C } ^ { * } , b \in \mathbb { C } \}$

## 9. Zeros of Analytic Polynomials in Several Variables

Let $p$ be an analytic polynomial in n complex variables $z _ { 1 } , \cdots , z _ { n }$ . The zero set $Z ( p )$ of $p$ is given by

$$
Z ( p ) : = \{ ( z _ { 1 } , \cdot \cdot \cdot , z _ { n } ) \in \mathbb { C } ^ { n } : p ( z _ { 1 } , \cdot \cdot \cdot , z _ { n } ) = 0 \} .
$$

The Fundamental Theorem of Algebra states that the zero set $Z ( p )$ of any analytic polynomial $p$ in one variable is non-empty. This simple looking fact has several notable consequences. Firstly, the zero set $Z ( p )$ of a non-zero analytic polynomial $p$ in more than one variable has empty interior. For simplicity, assume that the number of variables is two. Suppose contrary to this, $Z ( p )$ contains some polydisc $\mathbb { D } ( a , R ) \times \mathbb { D } ( b , R )$ for some $( a , b ) \in Z ( p )$ , so that for every $z \in \mathbb { D } ( a , R )$ , the one-variable analytic polynomial $p ( z , \cdot )$ admits infinitely many solution. By Fundamental Theorem of Algebra, $p ( z , \cdot )$ must be identically zero forcing $p = 0$

Problem 9.1. The set of $n \times n$ matrices with determinant equal to is dense in the space $o f n \times n$ complex matrices.

Secondly, unlike the one-variable situation, the zero set of a non-constant analytic polynomial in several variables is never compact.

Theorem 9.2. The zero set of any non-constant analytic polynomial in at least two variables is unbounded. In particular, it contains infinitely many points.

Proof. Let a positive number M be given. Without loss of generality, assume that $p$ is dependent of $z _ { n }$ , and set $\begin{array} { r } { p _ { z ^ { \prime } } ( z _ { n } ) = p ( z ^ { \prime } , z _ { n } ) = \sum _ { i = 1 } ^ { m } c _ { j } ( z ^ { \prime } ) z _ { n } ^ { j } } \end{array}$ . Let $c _ { j }$ denote the non-zero coefficient of $z _ { n } ^ { j } ~ ( j \neq 0 )$ in $p _ { z ^ { \prime } }$ . Since $c _ { j }$ are polynomials in $z ^ { \prime } .$ , by the discussion prior to Theorem $9 . 2 .$ the intersection $Z$ of the zero sets of $c _ { j } \ ( j \neq 0 )$ has empty interior. Thus one may choose w0 $\in \mathbb { C } ^ { n - 1 } \setminus Z$ with $\| w ^ { \prime } \| _ { 2 } > M _ { \operatorname* { m } }$ , so that $p _ { w ^ { \prime } }$ is a non-constant analytic polynomial in $z _ { n }$ . By Fundamental Theorem of Algebra, there exists $w _ { n } \in \mathbb { C }$ such that $p _ { w ^ { \prime } } ( w _ { n } ) = 0$ . Thus $p ( w ^ { \prime } , w _ { n } ) = 0$ with

$$
\| ( w ^ { \prime } , w _ { n } ) \| _ { 2 } \geq \| w ^ { \prime } \| _ { 2 } > M ,
$$

which completes the proof of the theorem.

On the other hand, the zero set of a non-constant real polynomial in more than one real variable need not be unbounded: $p ( x , y ) = x ^ { 2 } + y ^ { 2 } - 1$

Corollary 9.3. A non-constant analytic polynomial in n variables is proper $i f$ and only $i f n = 1$

Another striking difference between one and several variable theories is that the zeroes of non-constant analytic polynomials in more than one complex variable are never isolated.

Problem 9.4. Let p be a non-constant analytic polynomial in more than one variable. Show that any open neighborhood of a zero of p contains infinitely many zeros of $\dot { p }$ (Hint. Argue as in the proof of Theorem 9.2).

Theorem 9.5. Let p denote an analytic polynomial in n variables. Then $\mathbb { C } ^ { n } \backslash Z ( p )$ is path-connected.

Proof. The idea of the following proof is well-known (see, for instance, [3]). Let $z , w \in \mathbb { C } ^ { n } \setminus Z ( p )$ . Consider the straight-line path

$$
\gamma ( t ) = ( 1 - t ) z + t w \ ( t \in \mathbb { C } ) .
$$

Note that $\{ t \in \mathbb { C } : \gamma ( t ) \in Z ( p ) \}$ is precisely the zero set $Z ( p \circ \gamma ) : = Z$ . However, Z is a finite subset of C. Thus γ maps the path-connected set $\mathbb { C } \backslash Z$ continuously into $\mathbb { C } ^ { n } \setminus Z ( p )$ . In particular, z and w belong to the path-connected subset $\gamma ( \mathbb { C } \backslash Z )$ of $\mathbb { C } ^ { n } \setminus Z ( p )$ 

Problem 9.6. Show that the general linear group $G L _ { n } ( \mathbb { C } )$ is path-connected.

## References

[1] J. B. Conway, Functions of One Complex Variables, Springer-Verlag New York, 1995.

[2] E. Stein and R. Shakarchi, Complex Analysis, Princeton University Press, Priceton and Oxford, 2002.

[3] S. Kumar, An elementary proof of the connectedness of the general linear group $G L _ { n } ( \mathbb { C } )$ , The Mathematics Student, 84 (2015), 111-112.