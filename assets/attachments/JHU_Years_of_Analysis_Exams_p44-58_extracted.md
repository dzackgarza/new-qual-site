# ANALYSIS QUALIFYING EXAM SPRING 2005

## Notation:

${ \mathcal { C } } ^ { \infty } ( \mathbb { R } )$ : complex-valued ${ \mathcal { C } } ^ { \infty }$ functions on $\mathbb { R } .$

$\mathcal { C } _ { c } ^ { \infty } ( \mathbb { R } )$ : compactly supported functions in ${ \mathcal { C } } ^ { \infty } ( \mathbb { R } )$

$L ^ { p } ( \mathbb { R } ) , \ L ^ { p } ( [ 0 , 1 ] ) : \ L ^ { p }$ functions with respect to Lebesgue measure on R, [0, 1], respectively ${ \widehat { f } } :$ Fourier transform of $f$

$$
D = \{ z \in \mathbb { C } : | z | < 1 \}
$$

$$
\mathbb { R } ^ { + } = \{ x \in \mathbb { R } : x > 0 \}
$$

Do all 8 problems. Show all work. In each solution, state which theorems from 110.605 and 110.607 you are applying and verify that the hypotheses are satisfied.

() Let $f ( x ) = e ^ { - \lvert x \rvert } \mathrm { ~ f o r ~ } x \in \mathbb { R } .$

(a) Is ${ \widehat { f } } \in { \mathcal { C } } ^ { \infty } ( \mathbb { R } ) ?$ Prove that your answer is correct.

(b) Show that $| { \widehat { f } } ( \xi ) | \to 0 { \mathrm { ~ a s ~ } } | \xi | \to \infty$

(2) Suppose that $f \in L ^ { 1 } [ 0 , 1 ]$ and let $g ( x ) = \int _ { x } ^ { 1 } \frac { f ( t ) } { t } d t$ Show that $g \in L ^ { 1 } [ 0 , 1 ]$ and that

$$
\int _ { 0 } ^ { 1 } g ( x ) d x = \int _ { 0 } ^ { 1 } f ( x ) d x .
$$

(3) Prove or find a counterexample to each of the following statements:

(a) $L ^ { 2 } ( \mathbb { R } ) \subset L ^ { 1 } ( \mathbb { R } )$

(b) $L ^ { 1 } ( \mathbb { R } ) \subset L ^ { 2 } ( \mathbb { R } )$

(c) $L ^ { 2 } ( [ 0 , 1 ] ) \subset L ^ { 1 } ( [ 0 , 1 ] ) ;$

(d) $L ^ { 1 } ( [ 0 , 1 ] ) \subset L ^ { 2 } ( [ 0 , 1 ] ) ;$

(4) Let $\{ e _ { n } \}$ be an orthonormal basis for a Hilbert space $H$

(a) Show that $e _ { n } \to 0$ weakly. (Explain what weak convergence means.)

(b) Show that $e _ { n }$ does not tend to zero strongly. (Explain what strong convergence means.)

(c) Let $\begin{array} { r } { v _ { n } = \frac { 1 } { n } \sum _ { j = 1 } ^ { n } e _ { j } } \end{array}$ . Show that $v _ { n } \to 0$ strongly.

(5) Do there exist functions $f \in { \mathcal { C } } _ { c } ^ { \infty } ( \mathbb { R } )$ such that f is not identically zero and ${ \widehat { f } } \in { \mathcal { C } } _ { c } ^ { \infty } ( \mathbb { R } ) ?$ If $\mathrm { s o } ,$ find one. If not, prove that none exist.

$$
{ \widehat { f } } ( \xi )
$$

$$
\xi \in \mathbb { C }
$$

(6) Use residues to evaluate the integral

$$
\int _ { - \infty } ^ { \infty } { \frac { x \sin x d x } { ( x ^ { 2 } + 1 ) ( x ^ { 2 } + 4 ) } } \ .
$$

(7) Find a bijective holomorphic map f from the quadrant

$$
Q = \{ x + i y \in \mathbb { C } : x > 0 , \ y > 0 \}
$$

onto the unit disk D in C with $f ( 1 + i ) = 0 .$

(8) Let U be an open set in C containing the closed unit disk ${ \overline { { D } } } .$ Suppose f is a meromorphic function on U such that $f ( \partial D ) \subset \mathbb { R } ^ { + }$ . (In particular, f has no zeros or poles on ∂D.) Show that f has the same number of zeros as poles in $D$ (counting multiplicities).

Directions: This is a closed book exam. You have two and a half hours to do all seven problems. $\# 7$ is worth 10 points; the others are worth 20 points each.

.a)Let $C ( [ 0 , 1 ] )$ denote the space of continuous functions on $[ 0 , 1 ]$ , endowed with the $^ { 6 6 } \mathrm { { s u p } ^ { , \dag } }$ norm. Show that $C ( [ 0 , 1 ] )$ is a Banach space.

Let $B _ { p } = L ^ { p } ( [ 0 , 1 ] )$ , with $1 < p < \infty$ . Define weak and strong convergence in $B _ { p }$ . Then, show that the sequence $f _ { n } ( x ) =$ sin nπx converges weakly to 0, but not strongly to 0, in $B _ { 2 }$

2. a) Let f be integrable over a set A and suppose $A = \cup _ { n = 1 } ^ { \infty } A _ { n }$ , where the $A _ { n }$ are pairwise disjoint. Show that

$$
\int _ { A } f \ = \ \sum _ { n = 1 } ^ { \infty } \int _ { A _ { n } } f
$$

and that the sum on the right-hand side is absolutely convergent.

Let $\mu$ be Lebesgue measure on $\mathbb { R } ^ { 2 }$ and let $f \in L ^ { 1 } ( \mathbb { R } ^ { 2 } )$ . Show there is a Borel measure λ for which $d \lambda = f d \mu$ (verify that it is a measure).

For $f = x ^ { 2 } + y ^ { 2 }$ and D the unit disc, compute $\lambda ( D )$

3. Let $f \in L ^ { 1 } ( \mathbb { R } )$ Show directly (i.e., do not cite properties of the Fourier transform) that the function

$$
{ \widehat { f } } ( \xi ) = \int _ { \mathbb { R } } e ^ { - i x \xi } f ( x ) d x
$$

is uniformly continuous and ${ \widehat { f } } ( \xi ) \to 0 { \mathrm { ~ a s ~ } } | \xi | \to \infty$

4. Show that $f ( x ) = { \frac { \cos x } { 1 + x ^ { 2 } } }$ is an $L ^ { 1 }$ function on the real line (with respect to Lebesgue measure). Then evaluate

$$
\int _ { 0 } ^ { \infty } { \frac { \cos x \ d x } { 1 + x ^ { 2 } } } .
$$

5. Determine whether the equation $z ^ { 3 } + z ^ { 4 } = 2$ in the complex variable z has any non-real solutions with $| z | < 2$

6. Let $f$ be an entire function with $| f ( z ) | \leq 3 \log | z |$ when $| z | > 2$ Either verify that f must be constant, or give a counterexample.

7. Let $\gamma$ denote the curve $| z - 1 | = 2$ , oriented counterclockwise. Evaluate

$$
\int _ { \gamma } { \frac { e ^ { z } d z } { z ^ { 3 } } } .
$$

Instructions: Do all problems. Show all details in your solutions. Unless statcd otherwise, you mnay cite any of the theorems mentioncd in the syllabus.

1. Consider the sequence of functions $g _ { n } ( x ) = [ \sin ( n x ) ] ^ { 2 }$ on $[ 0 , 2 \pi ]$ . Define each of the following notions of convergence and determine whether the sequcnce converges in that sense; if so, determinc the limit:

a) Converges pointwise

b) Converges strongly in $L ^ { 1 }$

c) Converges weakly in $L ^ { 1 }$

2. Consider the set of positive continuous periodic functions $f$ on $[ 0 , 2 \pi ]$ satisfying $\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } f d \theta = 1$ . What is the largest possible value of $\exp \left( { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \log f d \theta \right)$ for such functions? Prove that your answer is correct.

3. Let $\alpha > 1 / 2$ and consider $f _ { \alpha } ( x ) = \int _ { \mathbb { R } } ( 1 + \xi ^ { 2 } ) ^ { - \alpha } e ^ { 2 \pi i x \xi } d \xi .$

Without doing the integration, determinc, for each α, which of the following properties holds for $f _ { \alpha }$ , and prove that your answcr is correct:

a) i) lim|x|→∞ |fα(x)| = 0, ii) $f _ { \alpha } \in L ^ { 2 } ( \mathbb { R } )$

b) Without appealing to thc properties of the Fourier transform, show that i) fα  C(R), ii) $f _ { \alpha }$ is bounded on R.

4. In problem $\# 3$ , take $\alpha = 1$ . Calculate $f _ { 1 } ( x )$ , as defined in $\# 3$ , by the method of residues.

5.a)Let $f ( z )$ be complex analytic in the disc $| z | < \pi$ . Assume that the only zero of $f$ in the closed unit disc $\overline { { D } } = \{ z : | z | \leq 1 \}$ is a simple zero at the origin. Lct C be the unit circle, oriented counterclockwise. Evaluate

$$
\int _ { C } { \frac { d z } { f ( z ) } } ,
$$

in the sense that no integration symbols should appear in the answer.

$| \ u _ { ) } \}$ Lct $f$ be as in part $\mathrm { \Pi ^ { \ a } } )$ , except assume that $f$ has a 2nd-order (i.e., double) zero at the origin. Verify or givc a counterexample:

$$
\mathrm { A s s c r t i o n : } \quad \int _ { C } { \frac { d z } { f ( z ) } } = 0 .
$$

6. Let $f ( z )$ bc holomorphic in an open sct containing the closed unit disc $\overrightharpoon { D }$ Suppose that $| f ( z ) | < 1$ for all z on the unit circle. Show that there is exactly one point $z \in D$ (the intcrior of $\overline { { D } } )$ for which $f ( z ) = z$

7. Determinc a one-to-one complex analytic mapping $f .$ other than $f ( z ) = z$ that takes $D$ (notation as above) onto itself and satisfics $\begin{array} { r } { f ( \frac { 1 } { 3 } ) = \frac { 1 } { 3 } } \end{array}$ •

Directions: This is a closed book exam. You have two hours to do all six of the (equally weighted) problems.

Question 1. Suppose that $f \in L ^ { 1 } ( \mathbf { R } )$ . Prove that given $\epsilon > 0$ , there exists $\delta > 0$ so that $\int _ { A } | f | < \epsilon$ for every measurable set A with $| A | < \delta$ ,

where A denotes the measure of A.

Question 2. Suppose that $f \in C ^ { 1 } ( [ 0 , \pi ] ) )$ and $f ( 0 ) = f ( \pi ) = 0$ . Prove that

$$
\int _ { 0 } ^ { \pi } f ^ { 2 } \leq \int _ { 0 } ^ { \pi } ( f ^ { \prime } ) ^ { 2 } .
$$

Question 3. Suppose that $1 < p <$ ∞ and the linear mapping $T$ is defined by

$$
T f ( x ) = x ^ { - 1 / p } \int _ { 0 } ^ { x } f ( t ) d t .
$$

Show that $T$ is a bounded map from $L ^ { q } ( ( 0 , \infty ) )$ to $C ^ { 0 } ( ( 0 , \infty ) )$ , where q satisfies $1 / p + 1 / q = 1$

Question 4. Determine the number of zeros the function $f ( z ) = 2 z ^ { 5 } + 8 z - 1$ has in the annulus $1 < | z | < 2$

Question 5. Suppose that f is holomorphic on the punctured disk $0 < | z | < 2$

(A) Prove that if there is a real constant C such that $| f ( z ) | \le C$ ,then

$$
\int _ { | z | < 1 } | f ^ { \prime } ( z ) | ^ { 2 } d z < \infty .
$$

(B) What happens when $| f |$ is unbounded?

Question 6. Suppose that $u > 0$ is a positive harmonic function on the punctured plane $0 < | z |$ . Prove that u is constant.

## SPRING 2003 COMPLEX ANALYSIS QUALIFYING EXAM

Please attempt all the problems and show all your work. In the following, "holomorphic" is synonymous with "analytic." Also, $\Delta$ will denote the open unit disk in $\mathbb { C }$

(1) (a) Let $f : \mathbb { C } \to \mathbb { C }$ be meromorphic with a pole at infinity. Show that $f$ must be a rational function.

(b) Use the above to prove the following: if $f : \Delta  \mathbb { C }$ is holomorphic with a continuous extension to the boundary of $\Delta$ such that $| f ( z ) | = 1$ for all $| z | = 1$ , then $f ( z )$ is the restriction of a rational function.

) Let $f : \Delta  \Delta$ be a holomorphic function with $f ( 0 ) = 0$ and $\left| f ^ { \prime } ( 0 ) \right| = M$ .If $0 \neq w \in \Delta$ is any other zero of $f ( z )$ , show that:

$$
\frac { M } { 1 + M } \leq | w | ~ .
$$

(3) Let C be the closed curve defined by two pieces: the first piece is given by the set of all $z$ satisfying $| z - 1 | = 3$ and $\operatorname { R e } ( z - 1 ) \geq 0$ . The second piece is the straight line segment from $1 + 3 i$ to $1 - 3 i$ . Orient C in the counterclockwise direction, and let Ω be the region enclosed by C. Suppose f is holomorphic in a neighborhood of $\overline { { \Omega } }$ with no zeros on $C .$ Suppose also that:

$$
{ \frac { 1 } { 2 \pi i } } \int _ { C } { \frac { z f ^ { \prime } ( z ) } { f ( z ) } } d z = 3 \qquad \mathrm { a n d } \qquad { \frac { 1 } { 2 \pi i } } \int _ { C } { \frac { z ^ { 2 } f ^ { \prime } ( z ) } { f ( z ) } } d z = { \frac { 5 } { 2 } } \ .
$$

Determine all the zeros of $f$ in Ω explicitly.

(4) (a) State Rouché's Theorem.

(b) Let $\varphi : \Omega \to \mathbb { C }$ be holomorphic on an open convex set Ω. Show that for z, $w \in \Omega$

$$
| \varphi ( z ) - \varphi ( w ) | \leq \operatorname* { m a x } _ { \xi \in L } | \varphi ^ { \prime } ( \xi ) | | z - w | ~ ,
$$

where L is the straight line segment from z to w.

(c) Use the above to prove the following: suppose

$$
f ( z ) = z + \sum _ { n = 2 } ^ { \infty } a _ { n } z ^ { n }
$$

where

$$
\sum _ { n = 2 } ^ { \infty } n | a _ { n } | \leq 1 ~ .
$$

Show that $f ( z )$ is a 1-1 holomorphic function on $\Delta$

# Real Analysis Qualifying Exam, Fall 2002

Instructions: You have 2 hours to do all problems as completely as possible.

1. Let $\psi ( x ) = x$ on $[ 0 , \frac { 1 } { 2 } ] \ , \ \psi ( x ) = 1 - x$ on $[ \textstyle { \frac { 1 } { 2 } } , 1 ]$ and extended periodically of period 1. Define $\begin{array} { r } { f ( x ) = \sum _ { n = 0 } ^ { \infty } 2 ^ { - n } \psi ( 8 ^ { n } x ) } \end{array}$

i. Show that $f ( x )$ is continuous everywhere.

ii. Show that $f ( x )$ is differentiable nowhere.

Hint: Consider the difference quotients

$$
\Delta _ { h } f ( x ) \equiv { \frac { f ( x + h ) - f ( x ) } { h } }
$$

where $h = \pm 8 ^ { - k }$ and the sign is chosen so that x and $x + h$ lie on the same linear segment of the graph of $\psi ( 8 ^ { k - 1 } x )$ . Then

a. $\begin{array} { r } { \Delta _ { h } f ( x ) = \sum _ { n = 0 } ^ { k - 1 } 2 ^ { - n } \Delta _ { h } \psi ( 8 ^ { n } x ) } \end{array}$

b. $\begin{array} { r } { | \Delta _ { h } f ( x ) | \geq 4 ^ { k - 1 } - \sum _ { n = 0 } ^ { k - 2 } 4 ^ { n } } \end{array}$

2. Let $f _ { 1 } ( x ) \leq f _ { 2 } ( x ) \leq . . . \leq f _ { n } ( x ) \leq . . .$ on a set A, where the functions $f _ { n }$ are integrable and $\textstyle \int _ { A } f _ { n } ( x ) \ d x \leq M$ for some constant M. Show that the limit

$$
f ( x ) = \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x )
$$

exists and is finite almost everywhere on A and that

$$
\operatorname* { l i m } _ { n  \infty } \int _ { A } f _ { n } ( x ) \ d x = \int _ { A } f ( x ) \ d x \ .
$$

3. i. Define equicontinuity and state the Arzela-Ascoli theorem.

ii. Let $\mathcal { F }$ be the family of real valued functions on [0,1] satising $f ( 0 ) = 0$ and $\begin{array} { r } { \int _ { 0 } ^ { 1 } f ^ { \prime } ( x ) ^ { 2 } \ d x \leq 1 } \end{array}$ Show that any sequence in $\mathcal { F }$ has a subsequence that converges uniformly.

4. Let K be a closed convex subset of a Hilbert space H. Show that for each $x \in H$ , there is a unique $y \in K$ such that

$$
| | x - y | | = i n f _ { z \in K } | | x - z | |
$$

5. i. Find the sum of the series $\begin{array} { r } { \sum _ { n = 1 } ^ { \infty } \frac { \sin { ( 2 n - 1 ) x } } { 2 n - 1 } \mathrm { o n } \left( 0 , 2 \pi \right) } \end{array}$

ii. Show that $\begin{array} { r } { \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { ( 2 n - 1 ) ^ { 2 } } } = { \frac { \pi ^ { 2 } } { 8 } } } \end{array}$

## Complex Analysis Core Qualifying Exam, Fall 2002

Do 5 of the 6 problems. Indicate clearly which 5 you want graded; if it is not clear, we will grade $\# 1 \mathrm { - } 5$ . Each problem counts for 20 points. In the case where there are two parts, the score is subdivided as indicated. Note: for the purposes of the exam, holomorphic is the same as complex analytic.

1. (a) (5 points) Give a counterexample to the assertion: If f is holomorphic on the annulus $\{ z : 1 < | z | < 3 \}$ , then f extends holomorphically to the disc $\{ z : | z | < 3 \}$

(b) (15 points) Determine whether the following is true: If f is holomorphic on the annulus $\{ z : 1 < | z | < 3 \}$ , then f extends meromorphically to the disc $\{ z : | z | < 3 \}$

2. (a) (15 points) Show that there is no one-to-one holomorphic mapping of the open annulus $\{ z : 1 < | z | < 2 \}$ onto the punctured unit disc $\{ z : 0 < | z | < 1 \}$ . (HINT: consider the inverse mapping)

(b) (5 points) Give an example of a one-to-one $C ^ { \infty }$ mapping of the open annulus $\{ z : 1 < | z | < 2 \}$ onto the punctured unit disc $\{ z : 0 < | z | < 1 \}$

3. (20 points) Determine all entire functions f for which $| f ( z ) | \leq | z | ^ { 2 }$ for all $z \in \mathbb { C }$

4. (20 points) Let D denote the unit disc $\{ z : | z | < 1 \}$ . Determine a holomorphic mapping f of D onto itself for which $\begin{array} { r } { f ( \frac { 1 } { 2 } ) = - \frac { 1 } { \pi } } \end{array}$

5. Let $\begin{array} { r } { P ( z ) = z ^ { 7 } + z ^ { 3 } + \frac { 1 } { 1 6 } } \end{array}$

(a) (5 points) Show that P has no multiple zeros.

(b) (15 points) Determine the number of zeros of P that lie in the closed disc $| z | \leq { \frac { 1 } { 2 } }$ .

6. (20 points) Evaluate the integral:

$$
\int _ { 0 } ^ { \infty } { \frac { u ^ { 2 } d u } { u ^ { 6 } + 1 } }
$$

## Real Analysis Qualifying Exam

Time: 2 hours

Instructions: Do five of the following 6 problems. (If you attempt all 6 problems, clearly indicate which problems you want graded.) Each problem is worth 20 points.

1. Let $f : [ 0 , 2 ] $ R be $\mathrm { ~ a ~ } \mathcal { C } ^ { 1 }$ function such that $f ( x )$ and $f ^ { \prime } ( x )$ vanish at $x = 0$ and at $x = 2 .$ Prove that for all $\varepsilon > 0$ there exists $t _ { \varepsilon } \in \mathbb { R } ^ { + }$ such that

$$
\left| \int _ { 0 } ^ { 2 } f ( x ) e ^ { i t x } d x \right| \leq { \frac { \varepsilon } { t } } \qquad { \mathrm { f o r } } t \geq t _ { \varepsilon } .
$$

2. Let $\left\{ c _ { n } \right\}$ be a sequence of positive real numbers, and let $f _ { n } : \mathbb { R } \to \mathbb { R }$ be given by

$$
f _ { n } ( x ) = \sin ( x + c _ { n } ^ { 2 } ) + { \frac { 1 } { c _ { n } } } \sin ( c _ { n } x ) .
$$

Prove that the sequence $\{ f _ { n } \}$ has a subsequence converging pointwise to a continuous function.

3. Let X denote the set of functions $f : [ 0 , 1 ] \to \mathbb { R }$ such that $\| f \| < \infty$ , where

$$
\| f \| : = | f ( 0 ) | + \operatorname* { s u p } \left\{ { \frac { | f ( x ) - f ( y ) | } { | x - y | ^ { 1 / 5 } } } : x \neq y \right\} ~ .
$$

Prove that $( X , \parallel \cdot \parallel )$ is a Banach space; i.e., show that X is a vector space, $\| \cdot \|$ is a norm, and X is complete.

4. Suppose that $f \in L ^ { 1 } ( \mathbb { R } ^ { n } , m )$ satisfies

$$
\left| \int _ { E } f d m \right| \leq m ( E )
$$

for all Lebesgue measurable sets E (where m denotes Lebesgue measure on $\mathbb { R } ^ { n } )$ . Prove that $| f | \le 1$ almost everywhere.

5. Let $( X , { \mathcal { M } } , \mu )$ be a measure space, and let $f \in L ^ { 1 } ( \mu ) \cap L ^ { \infty } ( \mu )$ . Prove that

$$
\operatorname* { l i m } _ { p \to \infty } \| f \| _ { p } = \| f \| _ { \infty } .
$$

6. Let $u \in \mathcal { D } ^ { \prime } ( \mathbb { R } )$ be given by

$$
( u , \varphi ) = \operatorname* { l i m } _ { \varepsilon \to 0 ^ { + } } \left[ \int _ { - \infty } ^ { - \varepsilon } \frac { \varphi ( x ) } { x } d x + \int _ { \varepsilon } ^ { + \infty } \frac { \varphi ( x ) } { x } d x \right] \ , \qquad \forall \ \varphi \in \mathcal { D } ( \mathbb { R } ) = \mathcal { C } _ { c } ^ { \infty } ( \mathbb { R } ) \ .
$$

Show that the above limit exists and that u is the distribution derivative of the function $f \in L _ { \mathrm { l o c } } ^ { 1 } ( \mathbb { R } )$ given by $f ( x ) = \log | x |$ •

# Complex Analysis Core Qualifying Exam Spring 2002 Instruction: Answer any FOUR questions

1. Let f be an entire function such that the image of f does not intersect $\{ z \in \mathbb { R } : z \geq 5 \}$ . Prove that $f$ is a constant.

2. Evaluate the integral

$$
\int _ { 0 } ^ { 2 \pi } { \frac { d x } { a ^ { 2 } + \cos ^ { 2 } x } } .
$$

Where $a > 1$

3. Classify all simply connected regions in the extended complex plane up to biholomorphic equivalence. i.e, give a list of simply connected region, prove that every simply connected region in the extended complex plane is biholomorphic equivalent to a member in your list. Prove also that no two members in your list are biholomorphic equivalent.

4. Let f be a holomorphic function which maps the unit disk into the unit disc. Show that

$$
| f ( z ) + f ( - z ) | \leq 2 | z | ^ { 2 }
$$

for all z in the unit disc, and if the equality holds for some z, then,

$$
f \left( z \right) = e ^ { i \theta } z ^ { 2 }
$$

for some real θ.

5. Let $\scriptstyle \sum _ { n = - \infty } ^ { \infty } a _ { n } z ^ { n }$ be the Laurent series expansion of $\scriptstyle { \frac { 1 } { \sin z } }$ on the annulus $\left\{ z \in \mathbb { C } : \pi < | z | < 2 \pi \right\}$ . Evaluate the coefficients $a _ { n }$ for $n < 0$

6. Show that a Möbius transformation maps a straight line or circle onto a straight line or circle.

## Real Analysis Qualifying Exam, Fall 2001

Instructions: Attempt to do all problems. Each is worth 20 points. All the measures involved are Lebesgue measure.

1.) Let f be a continuous function on $[ 0 , \infty )$ such that lim $_ { 1 _ { X \to \infty } } f ( x )$ exists (finitely). Prove that f is uniformly continuous.

2.) Let f and g be continuous real valued functions on

R such that lim $\scriptstyle { \mathrm { 1 } } | x | \to \infty , f ( x ) = 0$ and

$\textstyle \int _ { - \infty } ^ { \infty } | g ( x ) | d x < \infty$ . Define the function h

on R by

$$
h ( x ) = \int _ { - \infty } ^ { \infty } f ( x - y ) g ( y ) d y .
$$

Prove that $\scriptstyle \operatorname* { l i m } _ { | x | \to \infty } h ( x ) = 0$

Let $\left\{ f _ { n } \right\}$ be a sequence of real valued functions in

$L ^ { 4 / 3 } ( 0 , 1 )$ such that $f _ { n } \to 0$ in measure as $n \to \infty$

and $\begin{array} { r } { \int _ { 0 } ^ { 1 } | f _ { n } ( x ) | ^ { 4 / 3 } d x \leq 1 } \end{array}$ . Show that $\begin{array} { r } { \int _ { 0 } ^ { 1 } | f _ { n } ( x ) | d x \to 0 { \mathrm { ~ a s ~ } } n \to \infty } \end{array}$

Let $f \in L ^ { 1 } ( [ 0 , 1 ] )$ . For $k \in \mathbb N$ ,let $f _ { k }$ be

the step function defined on $[ 0 , 1 ]$ by

$$
f _ { k } ( x ) = k \int _ { j / k } ^ { ( j + 1 ) / k } f ( t ) d t , \quad { \mathrm { f o r ~ } } { \frac { j } { k } } \leq x < { \frac { j + 1 } { k } } .
$$

Show that $f _ { k }$ tends to $f$ in

$L ^ { 1 }$ norm as k tends to +∞.

Hint: Treat first the case where f is

continuous, and use approximation.

.) Let $1 \leq p < q < \infty$ . Which of the following statements

(i)-(vi) are true, and which are false? Justify all the negative

answers by a counterexample, but you do not have to justify the

positive answers.

(i) $L ^ { { \boldsymbol { p } } } ( \mathbb { R } ) \subset L ^ { q } ( \mathbb { R } )$

(ii) $L ^ { q } ( \mathbb { R } ) \subset L ^ { p } ( \mathbb { R } )$

(iii) $L ^ { p } ( [ 0 , 1 ] ) \subset L ^ { q } ( [ 0 , 1 ] )$

(iv) $L ^ { q } ( [ 0 , 1 ] ) \subset L ^ { p } ( [ 0 , 1 ] )$

(v) $\ell ^ { p } ( \mathbb { Z } ) \subset \ell ^ { q } ( \mathbb { Z } )$

(vi) $\ell ^ { q } ( \mathbb { Z } ) \subset \ell ^ { p } ( \mathbb { Z } )$

Justify your answer to the following question:

(vii) For which $s \geq 1$ is $L ^ { p } ( \mathbb { R } ) \cap L ^ { q } ( \mathbb { R } ) \subset L ^ { s } ( \mathbb { R } ) ?$

## COMPLEX ANALYSIS CORE QUALIFYING EXAM, FALL 2001

Instructions: Attempt FOUR of the following problems. Each is worth 25 points. Please label clearly which four of the five problems you want graded. Show all your work.

Notation: C denotes the complex numbers. For $z \in \mathbb { C } , \operatorname { R e } ( z )$ denotes the real part of $z .$ For each $r \geq 0 , D _ { r } ( 0 ) = \{ z \in \mathbb { C } : | z | < r \}$ •

Problem 1. A meromorphic function on $\mathbb { C } \cup \{ \infty \}$ is a meromorphic function $f ( z )$ on C such that $g ( z ) = f ( 1 / z )$ is also meromorphic. Show that a meromorphic function on $\mathbb { C } \cup \{ \infty \}$ must be rational, i.e. one can express it as the quotient of two polynomials.

Problem 2. Fix a real number $\alpha > 1$ . Show that the equation $z - \alpha = e ^ { - z }$ has precisely one solution in the half plane $\mathrm { R e } ( z ) > 0$ and that this solution must be real.

Problem 3. Compute: $\int _ { 0 } ^ { \infty } { \frac { d x } { 1 + x ^ { 3 } } } .$

Problem 4. Suppose that $f : D _ { 1 } ( 0 ) \to \mathbb { C }$ is a one-to-one holomorphic function with $\Omega = f \left( D _ { 1 } ( 0 ) \right)$ Let $g : D _ { 1 } ( 0 ) \to \Omega$ be another holomorphic function with $g ( 0 ) = f ( 0 )$ . Show that for each $0 \leq r < 1$ $g \left( D _ { r } ( 0 ) \right) \subset f \left( D _ { r } ( 0 ) \right)$ ∞

Problem 5. Use the result in Problem 4 to prove the following: If $g$ is a holomorphic function on $D _ { 1 } ( 0 )$ with $g ( 0 ) = 0$ and $| \mathrm { R e } ( g ( z ) ) | < 1$ for all $z \in D _ { 1 } ( 0 )$ , then

$$
| g ( z ) | \leq { \frac { 2 } { \pi } } \log \left\{ { \frac { 1 + | z | } { 1 - | z | } } \right\}
$$

for all $z \in D _ { 1 } ( 0 )$

# REAL ANALYSIS QUALIFYING EXAM, SPRING 2001

Instructions: Attempt to do all of the problems. Each is worth 20 points. All the measures involved are Lebesgue measure.

1.) Suppose that $\phi \in C _ { 0 } ^ { \infty } ( \mathbb { R } ^ { n } )$ has ∫ φdx = 1. If $\phi _ { \varepsilon } ( x ) = \varepsilon ^ { - n } \phi ( x / \varepsilon )$ , prove that if $1 \leq p <$ ∞ and $f \in L ^ { p } ( \mathbb { R } ^ { n } )$ then $f * \phi _ { \varepsilon } \to f$ in $L ^ { p } ( \mathbb { R } ^ { n } )$ . Prove that this is not true for $p = \infty$

2.) Suppose that $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ . Prove that for every $\varepsilon > 0$ there is a $\delta > 0$ such that if A is measurable with measure $< \delta$ then

$$
| \int _ { A } f d x | < \varepsilon .
$$

3.) Recall that $f : [ 0 , 1 ] \to \mathbb { R }$ is lower semicontinuous if lim in $\operatorname { f } _ { x \to x _ { 0 } } f ( x ) \geq f ( x _ { 0 } )$ for every $x _ { 0 } \in [ 0 , 1 ]$ Prove that if $f$ is a nonnegative lower semicontinuous function then one always has $\begin{array} { r } { S _ { + } ( f , P ) \to \int _ { 0 } ^ { 1 } } \end{array}$ f(x)dx as $| P | \to 0$ if $S _ { + } ( f , P )$ is the lower Riemann sum associated with a partition $\dot { P }$ of $[ 0 , 1 ]$ and $| P |$ is the smallest interval of the partition. Here $\textstyle \int _ { 0 } ^ { 1 } f ( x ) d x$ is the Lebesgue integral of $f .$

Here, if $0 = t _ { 0 } < t _ { 1 } < \cdots < t _ { n } = 1$ , is the partition $P ,$ then

$$
S _ { + } ( f , P ) = \sum _ { j = 1 } ^ { n } \operatorname* { i n f } _ { x \in [ t _ { j - 1 } , t _ { j } ) } f ( x ) ( t _ { j } - t _ { j - 1 } ) .
$$

Hint: To prove $\begin{array} { r } { S _ { + } ( f , P )  \int _ { 0 } ^ { 1 } f ( x ) d x } \end{array}$ as $| P | \to 0 ,$ ,it suffices to show that $S _ { + } ( f , P _ { n } ) $ $\textstyle \int _ { 0 } ^ { 1 } f ( x ) d x { \mathrm { ~ i f ~ } } P _ { n }$ is a nested sequence of partitions whose lengths goes to zero.

4.) For which values of α and $\beta$ does the following inequality hold?

$$
\| f \| _ { 2 } \leq \| f \| _ { 4 / 3 } ^ { \alpha } \| f \| _ { 4 } ^ { \beta } .
$$

Prove your assertion.

5.) Let $K \in C ( [ 0 , 1 ] \times [ 0 , 1 ] )$ . For $f \in C ( [ 0 , 1 ] )$ define

$$
T f ( x ) = \int _ { 0 } ^ { 1 } K ( x , y ) f ( y ) d y .
$$

Prove that $T f \in C ( [ 0 , 1 ] )$ . Moreover, prove that $\Omega = \{ T f : \| f \| _ { s u p } \leq 1 \}$ is precompact in $C ( [ 0 , 1 ] )$ . Here, we are using the sup-norm $\| \cdot \| _ { s u p }$ on $C ( [ 0 , 1 ] )$ and Ω being precompact means that every sequence in Ω must have a subsequence that converges with respect to this norm to an element of $C ( [ 0 , 1 ] )$

# COMPLEX ANALYSIS CORE QUALIFYING EXAM, SPRING 2001

Directions: Do FIVE of the following six questions; they are weighted equally. Label clearly which five that you want graded (otherwise only first five will be). Show your work.

Question 1. Suppose that $f , g$ are entire holomorphic functions with $| f ( z ) | \leq | g ( z ) |$ for all $z \in \mathbf { C }$ . Prove that there is a constant $c \in \mathbf { C }$ so that $f = c g$ .

Question 2. Find the number of zeros of the function $f ( z ) = 2 z ^ { 5 } + 8 z - 1$ in the annulus $1 < | z | < 2$

Question 3. Assume that $f _ { n }$ is holomorphic in $| z | < 1$ and $| f _ { n } | \leq 1 0$ Assume also that $\scriptstyle \operatorname* { l i m } _ { n \to \infty } f _ { n } \left( 2 ^ { - j } \right)$ exists for each $j = 1 , 2 , \dots$ Prove that $\scriptstyle \operatorname* { l i m } _ { n \to \infty } f _ { n } ( z )$ exists for all z with $| z | < 1$

Question 4. Let $u ( z ) > 0$ be a positive harmonic function in the punctured plane $0 < | z |$ Show that u must be constant.

Question 5. Let f be a non-constant holomorphic function in the annulus $1 < | z | < 2$ with $| f | \equiv 5$ on the boundary. Show that f has at least two zeros.

Question 6. Let $P ( z )$ be a polynomial. Show that all zeros of $P ^ { \prime } ( z )$ lie in the convex hull of the zeros of $P ( z )$