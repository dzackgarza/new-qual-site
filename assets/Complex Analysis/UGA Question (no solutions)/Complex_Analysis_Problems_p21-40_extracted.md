is analytic in $\mathbb { C } \setminus \gamma .$

<!-- image-->

## 7.8 9

<!-- image-->

Suppose that $f : \mathbb { C } \to \mathbb { C }$ is continuous everywhere and analytic on C \ R and prove that f is entire.

Something missing?

Solution omitted.

<!-- image-->

## 7.9 10

Prove Liouville’s theorem: suppose $f : \mathbb { C } \to \mathbb { C }$ is entire and bounded.
Use Cauchy’s formula to prove that $f ^ { \prime } \equiv 0$ and hence f is constant.

Solution omitted.

## 8 Extra

## 8.1 ?

Assume f is continuous in the region: $0 < | z - a | \leq R , 0 \leq \arg ( z - a )$ ≤ β0 $( 0 < \beta _ { 0 } \le 2 \pi )$ and the limit $\operatorname* { l i m } _ { z \to a } ( z - a ) f ( z ) = A $ exists.
Show that

$$
\operatorname * { l i m } _ { r  0 } \int _ { \gamma _ { r } } f ( z ) d z = i A \beta _ { 0 } \ ,
$$

where $\gamma _ { r } : = \lbrace z \mid z = a + r e ^ { i t } , 0 \leq t \leq \beta _ { 0 } \rbrace$

## 8.1.1 Tie’s Extra Questions: Fall 2009

Let f be a continuous function in the region

$$
D = \{ z \mid | z | > R , 0 \leq \arg z \leq \theta \} \quad \mathrm { w h e r e } \quad 1 \leq \theta \leq 2 \pi .
$$

If there exists k such that $\operatorname* { l i m } _ { z \to \infty } z f ( z ) = k$ for z in the region D. Show that

$$
\operatorname* { l i m } _ { R ^ { \prime } \to \infty } \int _ { L } f ( z ) d z = i \theta k ,
$$

where L is the part of the circle $| z | = R ^ { \prime }$ which lies in the region D.

## 8.1.2 Spring 2020 HW 2 # 2.6.5

Suppose $f \in C _ { \mathbb { C } } ^ { 1 } ( \Omega )$ and $T \subset \Omega$ is a triangle with $T ^ { \circ } \subset \Omega .$ . 1. Apply Green’s theorem to show that $\int _ { T } f ( z ) \ d z = 0 .$

2. Assume that f 0 is continuous and prove Goursat’s theorem.

Hint: Green’s theorem states

$$
\int _ { T } F d x + G d y = \int _ { T ^ { \circ } } \left( { \frac { \partial G } { \partial x } } - { \frac { \partial F } { \partial y } } \right) d x d y .
$$

## 8.1.3 Spring 2020 HW 2 # 2.6.6

Suppose that f is holomorphic on a punctured open set $\Omega \setminus \{ w _ { 0 } \}$ and let $T \subset \Omega$ be a triangle containing w0. Prove that if f is bounded near w0, then $\int _ { T } f ( z ) \ d z = 0$

## 8.1.4 Spring 2020 HW 2 # 2.6.7

Suppose $f : \mathbb { D } \to \mathbb { C }$ is holomorphic and let $d : = \operatorname* { s u p } _ { z , w \in \mathbb { D } } | f ( z ) - f ( w ) |$ be the diameter of the image of f. Show that $2 | f ^ { \prime } ( 0 ) | \leq d ,$ and that equality holds iff f is linear, so $f ( z ) = a _ { 1 } z + a _ { 2 }$

Hint:

$$
2 f ^ { \prime } ( 0 ) = { \frac { 1 } { 2 \pi i } } \int _ { | \xi | = r } { \frac { f ( \xi ) - f ( - \xi ) } { \xi ^ { 2 } } } \ d \xi
$$

whenever $0 < r < 1$

## 8.1.5 Spring 2020 HW 2 # 2.6.8

Suppose that f is holomorphic on the strip $S \ = \ \left\{ x + i y \ \big \vert \ x \in \mathbb { R } , \ - 1 < y < 1 \right\}$ with $| f ( z ) | \leq$ $A \left( 1 + | z | \right) ^ { \nu }$ for ν some fixed real number.
Show that for all $z \in S ,$ , for each integer $n \geq 0$ there exists an $A _ { n } \geq 0$ such that $\left| f ^ { ( n ) } ( x ) \right| \le A _ { n } ( 1 + | x | ) ^ { \nu }$ for all $x \in \mathbb { R }$

Hint: Use the Cauchy inequalities.

## 8.1.6 Spring 2020 HW 2 # 2.6.9

Let $\Omega \subset \mathbb { C }$ be open and bounded and $\varphi : \Omega \to \Omega$ holomorphic.
Prove that if there exists a point $z _ { 0 } \in \Omega$ such that $\varphi ( z _ { 0 } ) = z _ { 0 }$ and $\varphi ^ { \prime } ( z _ { 0 } ) = 1$ , then $\varphi$ is linear.

Hint: assume $z _ { 0 } = 0$ (explain why this can be done) and write $\varphi ( z ) = z + a _ { n } z ^ { n } + O ( z ^ { n + 1 } )$ near 0. Let $\varphi _ { k } = \varphi \circ \varphi \circ \cdots \circ \varphi$ and prove that $\varphi _ { k } ( z ) = z +$ $k a _ { n } z ^ { n } + O ( z ^ { n + 1 } )$ . Apply Cauchy’s inequalities and $l e t \ k  \infty$ to conclude.

## 8.1.7 Spring 2020 HW 2 # 6

Show by example that there exists a function $f ( z )$ that is holomorphic on $\left\{ z \in \mathbb { C } \Big \vert 0 < | z | < 1 \right\}$ and for all $r < 1$ 1,

$$
\int _ { | z | = r } f ( z ) d z = 0 ,
$$

but $f$ is not holomorphic at $z = 0$

## 8.1.8 Spring 2020 HW 2 # 7

Let $f$ be analytic on a region R and suppose $f ^ { \prime } ( z _ { 0 } ) \neq 0$ for some $z _ { 0 } \in R$ . Show that if C is a circle of sufficiently small radius centered at $z _ { \mathrm { 0 } }$ , then

$$
\frac { 2 \pi i } { f ^ { \prime } \left( z _ { 0 } \right) } = \int _ { C } \frac { d z } { f ( z ) - f \left( z _ { 0 } \right) } .
$$

Hint: use the inverse function theorem.

## 8.1.9 Spring 2020 HW 2 # 8

Assume two functions $u , b : \mathbb { R } ^ { 2 } $ R have continuous partial derivatives at $( x _ { 0 } , y _ { 0 } )$ . Show that $f : = u +$ iv has derivative $f ^ { \prime } ( z _ { 0 } )$ at $z _ { 0 } = x _ { 0 } + i y _ { 0 }$ if and only if

$$
\operatorname * { l i m } _ { r  0 } \frac { 1 } { \pi r ^ { 2 } } \int _ { | z - z _ { 0 } | = r } f ( z ) d z = 0 .
$$

## 8.1.10 Spring 2020 HW 2 # 9 (Cauchy’s Formula for Exterior Regions)

Let $\gamma$ be a piecewise smooth simple closed curve with interior $\Omega _ { 1 }$ and exterior $\Omega _ { 2 }$ . Assume $f ^ { \prime }$ exists\
in an open set containing $\gamma$ and $\Omega _ { 2 }$ with lim $f ( z ) = A$ . Show that z→∞

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \gamma } { \frac { f ( \xi ) } { \xi - z } } d \xi = { \left\{ \begin{array} { l l } { A , } & { { \mathrm { ~ i f ~ } } z \in \Omega _ { 1 } } \\ { - f ( z ) + A , } & { { \mathrm { ~ i f ~ } } z \in \Omega _ { 2 } } \end{array} \right. } .
$$

## 8.1.11 Spring 2020 HW 2 # 10

Let $f ( z )$ be bounded and analytic in C. Let $a \neq b$ be any fixed complex numbers.
Show that the following limit exists:

$$
\operatorname* { l i m } _ { R \to \infty } \int _ { | z | = R } { \frac { f ( z ) } { ( z - a ) ( z - b ) } } d z .
$$

Use this to show that $f ( z )$ must be constant.

## 8.1.12 Spring 2020 HW 2 # 11

Suppose $f ( z )$ is entire and

$$
\operatorname* { l i m } _ { z \to \infty } \frac { f ( z ) } { z } = 0 .
$$

Show that f (z) is a constant.

## 8.1.13 Spring 2020 HW 2 # 12

Let $f$ be analytic in a domain D and $\gamma$ be a closed curve in $D$ . For any $z _ { 0 } \in D$ not on γ, show that

$$
\int _ { \gamma } \frac { f ^ { \prime } ( z ) } { \left( z - z _ { 0 } \right) } d z = \int _ { \gamma } \frac { f ( z ) } { \left( z - z _ { 0 } \right) ^ { 2 } } d z .
$$

Give a generalization of this result.

## 8.1.14 Spring 2020 HW 2 # 13

Compute

$$
\int _ { | z | = 1 } \left( z + { \frac { 1 } { z } } \right) ^ { 2 n } { \frac { d z } { z } }
$$

and use it to show that

$$
\int _ { 0 } ^ { 2 \pi } \cos ^ { 2 n } ( \theta ) d \theta = 2 \pi \left( { \frac { 1 \cdot 3 \cdot 5 \cdot \cdot \cdot ( 2 n - 1 ) } { 2 \cdot 4 \cdot 6 \cdot \cdot \cdot ( 2 n ) } } \right) .
$$

## 8.1.15 Entire and O of polynomial implies polynomial $^ { + } _ { \nsucc }$

Problem 8.1.1 (?)\
Let $f ( z )$ be entire and assume that $| f ( z ) | \leq M | z | ^ { 2 }$ outside of some disk for some constant M . Show that f(z) is a polynomial in z of degree $\leq 2 .$

Solution omitted.

## 8.2 Uniform sequence implies uniform derivatives

Problem 8.2.1 (?)\
Let $a _ { n } ( z )$ be an analytic sequence in a domain D such that $\sum _ { n = 0 } ^ { \infty } \left| a _ { n } ( z ) \right|$ converges uniformly on bounded and closed sub-regions of D. Show that $\sum _ { n = 0 } ^ { \infty } \left| a _ { n } ^ { \prime } ( z ) \right|$ converges uniformly on bounded and closed sub-regions of D.

Solution omitted.

<!-- image-->

## 9 Liouville’s Theorem, Power Series (8155e)

## 9.1 1

Suppose f is analytic on a region Ω such that $\mathbb { D } \subseteq \Omega \subseteq \mathbb { C }$ and $f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ is a power series with radius of convergence exactly 1.

a. $\downarrow$ Give an example of such an f that converges at every point of $S ^ { 1 }$

b. Give an example of such an f which is analytic at 1 but $\sum _ { n = 0 } ^ { \infty } a _ { n }$ diverges.

c. Prove that f can not be analytic at every point of $S ^ { 1 }$

## Missing part (c)

Solution omitted.

## 9.2 2

Suppose f is entire and has Taylor series $\sum a _ { n } z ^ { n }$ about 0.

a. 7 Express $a _ { n }$ as a contour integral along the circle $| z | = R$

b. Apply (a) to show that the above Taylor series converges uniformly on every bounded subset of C.

c. Determine those functions f for which the above Taylor series converges uniformly on all of C.

## 9.3 3

Suppose D is a domain and $f , g$ are analytic on D.

Prove that if $f g = 0$ on D, then either f ≡ 0 or g ≡ 0 on D.

## 9.4 4

Suppose f is analytic on $\mathbb { D } ^ { \circ }$ . Determine with proof which of the following are possible:

a. $f \left( { \frac { 1 } { n } } \right) = ( - 1 ) ^ { n }$ for each $n > 1$

b. $f \left( { \frac { 1 } { n } } \right) = e ^ { - n }$ for each even integer $n > 1$ while $f \left( { \frac { 1 } { n } } \right) = 0$ for each odd integer $n > 1$

c. $f \left( { \frac { 1 } { n ^ { 2 } } } \right) = { \frac { 1 } { n } }$ for each integer $n > 1$

d. $f \left( { \frac { 1 } { n } } \right) = { \frac { n - 2 } { n - 1 } }$ for each integer $n > 1$

## 9.5 5

Prove the Fundamental Theorem of Algebra (using complex analysis).

Solution omitted.

## 9.6 6

Find all entire functions that satisfy

$$
| f ( z ) | \geq | z | \quad \forall z \in \mathbb { C } .
$$

Prove this list is complete.

Solution omitted.

## 9.7 7

Suppose $\sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ converges for some $z _ { 0 } \neq 0 .$

a. Prove that the series converges absolutely for each z with $| z | < | z | _ { 0 }$

b. Suppose $0 < r < | z _ { 0 } |$ and show that the series converges uniformly on $| z | \leq r$

## 9.8 8

Suppose f is entire and suppose that for some integer $n \geq 1$

$$
\operatorname* { l i m } _ { z \to \infty } \frac { f ( z ) } { z ^ { n } } = 0 .
$$

Prove that f is a polynomial of degree at most $n - 1$

## 9.9 9

Find all entire functions satisfying

$$
| f ( z ) | \leq | z | ^ { \frac { 1 } { 2 } } \quad { \mathrm { ~ f o r ~ } } | z | > 1 0 .
$$

## 9.10 10

Prove that the following series converges uniformly on the set $\left\{ z \ | \ \Im ( z ) < \ln 2 \right\}$

$$
\sum _ { n = 1 } ^ { \infty } { \frac { \sin ( n z ) } { 2 ^ { n } } } .
$$

## 10 Extra

## 10.1 Tie’s Questions

Let f(z) be entire and assume values of $f ( z )$ lie outside a bounded open set Ω. Show without using Picard’s theorems that f (z) is a constant.

Let $f ( z )$ be entire and assume values of $f ( z )$ lie outside a bounded open set Ω.

Show without using Picard’s theorems that f (z) is a constant.

## 10.2 Tie’s Questions

<!-- image-->

1. Assume $f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } z ^ { n }$ converges in $| z | < R .$

Show that for $r < R$

$$
{ \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } | f ( r e ^ { i \theta } ) | ^ { 2 } d \theta = \sum _ { n = 0 } ^ { \infty } | c _ { n } | ^ { 2 } r ^ { 2 n } .
$$

2. Deduce Liouville’s theorem from (1).

## 10.2.1 Tie’s Extra Questions: Fall 2009

Suppose f is entire and there exist A, $R > 0$ and natural number N such that

$$
| f ( z ) | \geq A | z | ^ { N } { \mathrm { ~ f o r ~ } } | z | \geq R .
$$

Show that

1. f is a polynomial and

2. the degree of f is at least $N$

## 10.2.2 Tie’s Extra Questions: Fall 2009

Let $f ( z )$ be entire and assume values of $f ( z )$ lie outside a bounded open set $\Omega .$ Show without using Picard’s theorems that $f ( z )$ is a constant.

## 10.2.3 Tie’s Extra Questions: Fall 2009

Let $f ( z )$ be entire and assume that $f ( z ) \leq M | z | ^ { 2 }$ outside some disk for some constant M. Show that f (z) is a polynomial in z of degree $\leq 2 .$

## 10.2.4 Spring 20202 HW 2 # 4

Without using Cauchy’s integral formula, show that ${ \mathrm { i f ~ } } | a | < r < | b |$ , then

$$
\int _ { \gamma } { \frac { d z } { ( z - \alpha ) ( z - \beta ) } } = { \frac { 2 \pi i } { \alpha - \beta } }
$$

where $\gamma$ denotes the circle centered at the origin of radius r with positive orientation.

Hint: take a Laurent expansion.

## 10.2.5 Spring 20202 HW 3 # 1

Prove that if f has two Laurent series expansions,

$$
f ( z ) = \sum c _ { n } ( z - a ) ^ { n } \quad { \mathrm { a n d } } \quad f ( z ) = \sum c _ { n } ^ { \prime } ( z - a ) ^ { n }
$$

then $c _ { n } = c _ { n } ^ { \prime }$

## 10.2.6 Spring 20202 HW 3 # 2

Find Laurent series expansions of

$$
\frac { 1 } { 1 - z ^ { 2 } } + \frac { 1 } { 3 - z }
$$

How many such expansions are there?
In what domains are each valid?

## 10.2.7 Spring 20202 HW 3 # 3

Let $P , Q$ be polynomials with no common zeros.
Assume a is a root of $Q .$ Find the principal part of $P / Q$ at $z = a$ in terms of $P$ and $Q$ if a is (1) a simple root, and (2) a double root.

## 10.2.8 Spring 20202 HW 3 # 5

Show that if f is entire and $\operatorname* { l i m } _ { z \to \infty } f ( z ) = \infty$ , then $f$ is a polynomial.

# 11 Laurent Expansions and Singularities(8155f)

$$
\mathbf { 1 1 . 1 \textbf { 1 } } \mathrm { \Omega }
$$

Find the Laurent expansion of

$$
f ( z ) = { \frac { z + 1 } { z ( z - 1 ) } }
$$

about $z = 0$ and $z = 1$ respectively.

Solution omitted.

<!-- image-->

$$
1 1 . 2 \ 2 \ \mathrm { ~ }
$$

<!-- image-->

Find the Laurent expansions about $z = 0$ of the following functions:

$$
e ^ { \frac { 1 } { z } }
$$

$$
\cos \left( { \frac { 1 } { z } } \right) .
$$

Solution omitted.

## 11.3 3

<!-- image-->

Find the Laurent expansion of

$$
f ( z ) = { \frac { z + 1 } { z ( z - 1 ) ^ { 2 } } }
$$

about z = 0 and z = 1 respectively.

Hint: recall that power series can be differentiated.

<!-- image-->

## 11.4 4

<!-- image-->

For the following functions, find the Laurent series about 0 and classify their singularities there:

$$
\sin ^ { 2 } ( z )
$$

$$
z \exp { \frac { z } { z ^ { 2 } } }
$$

$$
{ \frac { 1 } { z ( 4 - z ) } } .
$$

<!-- image-->

## 11.5 5

<!-- image-->

Find all entire functions with have poles at ∞.

<!-- image-->

## 11.6 6

<!-- image-->

Find all functions on the Riemann sphere that have a simple pole at z = 2 and a double pole at $z = \infty$ , but are analytic elsewhere.

<!-- image-->

## 11.7 7

<!-- image-->

Let f be entire, and discuss (with proofs and examples) the types of singularities f might have (removable, pole, or essential) at $z = \infty$ in the following cases:

1. f has at most finitely many zeros in $\mathbb { C } .$

2. f has infinitely many zeros in C.

## 11.8 8

Define

$$
f ( z ) = { \frac { \pi ^ { 2 } } { \sin ^ { 2 } \left( \pi z \right) } }
$$

$$
g ( z ) = \sum _ { n \in \mathbb { Z } } { \frac { 1 } { ( z - n ) ^ { 2 } } } .
$$

a. Show that f and g have the same singularities in C.

b. Show that f and g have the same singular parts at each of their singularities.

c. Show that $f , g$ each have period one and approach zero uniformly on $0 \leq x \leq 1$ as $| y |  \infty$

d. Conclude that $f = g .$

Not finished.

Solution omitted.

## 12 Residues

12.1

Problem 12.1.1 (?)

Calculate

$$
\int _ { 0 } ^ { \infty } { \frac { 1 } { ( 1 + z ) ^ { 2 } ( z + 9 x ^ { 2 } ) } } d x .
$$

12.2

Problem 12.2.1 (?)

Let a > 0 and calculate

$$
\int _ { 0 } ^ { \infty } { \frac { x \sin ( x ) } { x ^ { 2 } + a ^ { 2 } } } d x .
$$

12.3

Problem 12.3.1 (?) Calculate

$$
\int _ { 0 } ^ { \infty } { \frac { \sqrt { x } } { ( x + 1 ) ^ { 2 } } } d x .
$$

12.4

Problem 12.4.1 (?) Calculate

$$
\int _ { 0 } ^ { \infty } { \frac { \cos ( x ) - \cos ( 4 x ) } { x ^ { 2 } } } d x .
$$

12.5

Problem 12.5.1 (?)

Let $a > 0$ and calculate

$$
\int _ { 0 } ^ { \infty } { \frac { x ^ { 2 } } { ( x ^ { 2 } + a ^ { 2 } ) ^ { 2 } } } d x .
$$

12.6

Problem 12.6.1 (?) Calculate

Problem 12.8.1 (?) Calculate

Problem 12.7.1 (?) Calculate

Problem 12.9.1 (?) Calculate

$$
\int _ { 0 } ^ { \infty } { \frac { \sin ( x ) } { x } } d x .
$$

12.7

$$
\int _ { 0 } ^ { \infty } { \frac { \sin ( x ) } { x ( x ^ { 2 } + 1 ) } } d x .
$$

12.8

$$
\int _ { 0 } ^ { \infty } { \frac { \sqrt { x } } { 1 + x ^ { 2 } } } d x .
$$

12.9

$$
\int _ { - \infty } ^ { \infty } { \frac { 1 + x ^ { 2 } } { 1 + x ^ { 4 } } } d x .
$$

12.10

Problem 12.10.1 (?)

Let $a > 0$ and calculate

$$
\int _ { 0 } ^ { \infty } { \frac { \cos ( x ) } { ( x ^ { 2 } + a ^ { 2 } ) ^ { 2 } } } d x .
$$

## 12.11

Problem 12.11.1 (?)

Calculate

$$
\int _ { 0 } ^ { \infty } { \frac { \sin ^ { 3 } ( x ) } { x ^ { 3 } } } d x .
$$

## 12.12

Problem 12.12.1 (?)

Let $n \in \mathbb { Z } ^ { \geq 1 }$ and $0 < \theta < \pi$ and show that

$$
{ \frac { 1 } { 2 \pi i } } \int _ { | z | = 2 } { \frac { z ^ { n } } { 1 - 3 z \cos ( \theta ) + z ^ { 2 } } } d z = { \frac { \sin ( n \theta ) } { \sin ( \theta ) } } .
$$

## 12.13

Problem 12.13.1 (?)

Suppose $a > b > 0$ and calculate

$$
\int _ { 0 } ^ { 2 \pi } { \frac { 1 } { ( a + b \cos ( \theta ) ) ^ { 2 } } } d \theta .
$$

## 13 Extra Questions

## 13.1

Problem 13.1.1 (?)

Suppose that f is an analytic function in the region D which contains the point a. Let

$F ( z ) = z - a - q f ( z ) .$ , where q is a complex parameter.

1. Let $K \subset D$ be a circle with the center at point a and also we assume that $f ( z ) \neq 0$ for $z \in K$ . Prove that the function $F$ has one and only one zero $z = w$ on the closed disc $\overline { { K } }$ whose boundary is the circle K if

$$
| q | < \operatorname* { m i n } _ { z \in K } { \frac { | z - a | } { | f ( z ) | } } . .
$$

2. Let $G ( z )$ be an analytic function on the disk $\overline { { K } }$ . Apply the residue theorem to prove that

$$
\frac { G ( w ) } { F ^ { \prime } ( w ) } = \frac { 1 } { 2 \pi i } \int _ { K } \frac { G ( z ) } { F ( z ) } d z ,
$$

where w is the zero from (1).

## 13.2

Problem 13.2.1 (?)

Evaluate

$$
\int _ { 0 } ^ { \infty } { \frac { x \sin x } { x ^ { 2 } + a ^ { 2 } } } d x .
$$

13.3

Problem 13.3.1 (?)

Show that

$$
\int _ { 0 } ^ { \infty } { \frac { x ^ { a - 1 } } { 1 + x ^ { n } } } d x = { \frac { \pi } { n \sin { \frac { a \pi } { n } } } }
$$

using complex analysis, $0 < a < n$ . Here n is a positive integer.

## 13.4

Problem 13.4.1 (?)

Show that

$$
\int _ { 0 } ^ { \infty } { \frac { \cos ( x ) } { x ^ { 2 } + b ^ { 2 } } } d x = { \frac { \pi e ^ { - b } } { 2 b } } .
$$

Solution omitted.

## 13.4.1 Tie’s Extra Questions: Fall 2009

Suppose that $f$ is an analytic function in the region D which contains the point a. Let

$F ( z ) = z - a - q f ( z )$ where q is a complex parameter.

(1) Let $K \subset D$ be a circle with the center at point a and also we assume that $f ( z ) \neq 0$ for $z \in K$ Prove that the function F has one and only one zero $z = w$ on the closed disc K whose boundary is the circle K ${ \mathrm { i f ~ } } | q | < \operatorname* { m i n } _ { z \in K } { \frac { | z - a | } { | f ( z ) | } }$

(2) Let $G ( z )$ be an analytic function on the disk $\overline { { K } }$ . Apply the residue theorem to prove that $\frac { G ( w ) } { F ^ { \prime } ( w ) } = \frac { 1 } { 2 \pi i } \int _ { K } \frac { G ( z ) } { F ( z ) } d z$ , where w is the zero from (1).

(3) $\mathrm { I f } ~ z \in K$ , prove that the function $\frac { 1 } { F ( z ) }$ can be represented as a convergent series with respect to q: ${ \frac { 1 } { F ( z ) } } = \sum _ { n = 0 } ^ { \infty } { \frac { ( q f ( z ) ) ^ { n } } { ( z - a ) ^ { n + 1 } } }$

## 13.4.2 Tie’s Extra Questions: Fall 2009

Evaluate

$$
\int _ { 0 } ^ { \infty } { \frac { x \sin x } { x ^ { 2 } + a ^ { 2 } } } d x .
$$

## 13.4.3 Tie’s Extra Questions: Fall 2009

Show that

$$
\int _ { 0 } ^ { \infty } { \frac { x ^ { a - 1 } } { 1 + x ^ { n } } } d x = { \frac { \pi } { n \sin { \frac { a \pi } { n } } } }
$$

using complex analysis, $0 < a \le n$ . Here n is a positive integer.

## 13.4.4 Spring 20202 HW 2 # 2.6.1

Show that

$$
\int _ { 0 } ^ { \infty } \sin \left( x ^ { 2 } \right) d x = \int _ { 0 } ^ { \infty } \cos \left( x ^ { 2 } \right) d x = { \frac { \sqrt { 2 \pi } } { 4 } } .
$$

Hint: integrate $e ^ { - x ^ { 2 } }$ over the following contour, using the fact that $\int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } } d x = { \sqrt { \pi } } .$

<!-- image-->

## 13.4.5 Spring 20202 HW 2 # 2.6.2

Show that

$$
\int _ { 0 } ^ { \infty } { \frac { \sin { x } } { x } } d x = { \frac { \pi } { 2 } } .
$$

fact that this integral equals $\frac { 1 } { 2 i } \int _ { - \infty } ^ { \infty } \frac { e ^ { i x } - 1 } { x } d x$ and integrate around an indented

## 13.4.6 Spring 20202 HW 3 # 3.8.1

Use the following formula to show that the complex zeros of sin(πz) are exactly the integers, and they are each of order 1:

$$
\sin \pi z = { \frac { e ^ { i \pi z } - e ^ { - i \pi z } } { 2 i } } .
$$

Calculate the residue of $\frac { 1 } { \sin ( \pi z ) }$ at $z = n \in \mathbb { Z }$

## 13.4.7 Spring 20202 HW 3 # 3.8.2

Evaluate the integral

$$
\int _ { \mathbb { R } } { \frac { d x } { 1 + x ^ { 4 } } } .
$$

What are the poles of $\frac { 1 } { 1 + z ^ { 4 } } ?$

## 13.4.8 Spring 20202 HW 3 # 3.8.4

Show that

$$
\int _ { - \infty } ^ { \infty } { \frac { x \sin x } { x ^ { 2 } + a ^ { 2 } } } d x = \pi e ^ { - a } , \quad { \mathrm { ~ f o r ~ a l l ~ } } a > 0 .
$$

## 13.4.9 Spring 20202 HW 3 # 3.8.5

Show that if $\xi \in \mathbb { R }$ , then

$$
\int _ { - \infty } ^ { \infty } \frac { e ^ { - 2 \pi i x \xi } } { \left( 1 + x ^ { 2 } \right) ^ { 2 } } d x = \frac { \pi } { 2 } ( 1 + 2 \pi | \xi | ) e ^ { - 2 \pi | \xi | } .
$$

## 13.4.10 Spring 20202 HW 3 # 3.8.6

Show that

$$
\int _ { - \infty } ^ { \infty } { \frac { d x } { ( 1 + x ^ { 2 } ) ^ { n + 1 } } } = { \frac { 1 \cdot 3 \cdot 5 \cdot \cdot \cdot ( 2 n - 1 ) } { 2 \cdot 4 \cdot 6 \cdot \cdot \cdot ( 2 n ) } } \cdot \pi .
$$

## 13.4.11 Spring 20202 HW 3 # 3.8.7

Show that

$$
\int _ { 0 } ^ { 2 \pi } \frac { d \theta } { ( a + \cos \theta ) ^ { 2 } } = \frac { 2 \pi a } { ( a ^ { 2 } - 1 ) ^ { 3 / 2 } } , ~ \mathrm { w h e n e v e r } ~ a > 1 .
$$

## 13.4.12 Spring 20202 HW 3 # 3.8.8

Show that if $a , b \in \mathbb { R }$ with $a > | b |$ , then

$$
\int _ { 0 } ^ { 2 \pi } { \frac { d \theta } { a + b \cos \theta } } = { \frac { 2 \pi } { \sqrt { a ^ { 2 } - b ^ { 2 } } } } .
$$
