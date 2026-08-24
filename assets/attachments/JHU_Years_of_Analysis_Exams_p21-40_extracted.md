All problems are equally weighted. Show all your work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

## Time: 3 hours

## Part I. Complex Analysis

1. Use residues to calculate the integral $\textstyle \int _ { 0 } ^ { \infty } { \frac { 1 } { ( 1 + x ^ { 2 } ) ^ { 2 } } } d x$

2. Suppose f is holomorphic on the open unit disc $D ( 0 , 1 )$ and continuous on $\overline { { D ( 0 , 1 ) } }$ . Assume $| f ( \xi ) | < 1$ for $\xi \in \partial D ( 0 , 1 )$ . Show that there exists an unique point $a \in D ( 0 , 1 )$ such that $f ( a ) = a$

3. Suppose f is holomorphic on $U : = D ( 0 , 1 ) \setminus \{ 0 \}$ . Assume that the real part $\operatorname { R e } ( f )$ is bounded from below on U. Prove that $z = 0$ is a removable singularity.

4. Let $\begin{array} { r } { U = \left\{ z \in \mathbb { C } \mid \operatorname { I m } ( z ) \leq { \frac { \pi } { 2 } } \right\} } \end{array}$ and f be an entire function satisfying $f ( U ) \subset U , f ( - 1 ) = 0 , f ( 0 ) = \mathbf { \bar { 1 } }$ . Prove that $f ( z ) = z + 1$

## Part II. Real Analysis

5. Justify or give a counterexample to the following assertions:   
a. If $\{ f _ { i } \}$ is a sequence in $L ^ { 2 } ( [ 0 , 1 ] )$ converging weakly to f in $L ^ { 2 } ( [ 0 , 1 ] )$ then $f _ { i } ^ { 2 }$ converges weakly to $f ^ { 2 }$ in $L ^ { 1 } ( [ 0 , 1 ] )$ .   
b. If $\{ f _ { i } \}$ is a sequence in $L ^ { 2 } ( [ 0 , 1 ] )$ converging strongly to f in $L ^ { 2 } ( [ 0 , 1 ] )$ , then $f _ { i } ^ { 2 }$ converges strongly to $f ^ { 2 }$ in $L ^ { 1 } ( [ 0 , 1 ] )$ .

6. Let $\{ g _ { k } \} _ { k = 1 } ^ { \infty }$ be a sequence in $L ^ { 1 } ( \mathbb { R } ^ { n } )$ with $\sum \left| \left| g _ { k } \right| \right| _ { L ^ { 1 } ( \mathbb { R } ^ { n } ) } < \infty$

a. Show that $\textstyle \sum _ { k = 1 } ^ { \infty } g _ { k }$ converges a.e. to a function $g \in L ^ { 1 } ( \mathbb { R } ^ { n } )$

b. Show that lim $\begin{array} { r } { { \bf \Phi } _ { N  \infty } \vert \vert g - \sum _ { k = 1 } ^ { N } g _ { k } \vert \vert _ { L ^ { 1 } ( \mathbb { R } ^ { n } ) } = 0 . } \end{array}$

7. Let $f \in L ^ { 1 } ( \mathbb { R } )$ and set $\begin{array} { r } { h ( x ) = \int _ { [ x , x + 1 ] } f ( t ) \ d t } \end{array}$

a. Show that $h ( x )$ is absolutely continuous.

b. Show that $\scriptstyle \operatorname* { l i m } _ { x \to \infty } h ( x ) = 0$

8. Let $f \in L ^ { 1 } ( \mathbb { R } )$ . Define its Fourier transform $\begin{array} { r } { \hat { f } ( \xi ) = \int f ( x ) e ^ { - 2 \pi i x \cdot \xi } d x } \end{array}$ Show that $\hat { f } ( \xi ) \in C _ { 0 } ( \mathbb { R } )$ , that is the Fourier transform is continuous and vanishes at infinity. You may not quote the Riemann-Lebesgue lemma without sketching a proof.

# ANALYSIS QUALIFYING EXAM SEPTEMBER 2011

All problems are equally weighted. Show all your work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

Time: 3 hours.

Part I. Complex Analysis.

Notation: $D = \{ z \in \mathbb { C } : | z | < 1 \}$

1. Determine the value of the integral

$$
\int _ { \gamma } \frac { d z } { z ^ { 3 } \cos z } ,
$$

where $\gamma$ is the circle $\{ | z - 1 | < 2 \}$ traversed counterclockwise.

2. Let $h : \mathbb { C } \to \mathbb { R }$ be a harmonic function such that h is bounded below. Prove that h is constant.

3. Let f be a holomorphic function on $D \setminus \{ 0 \}$ . Suppose that there exists a positive integer n such that $f ^ { - 1 } ( w )$ contains at most n points for all $w \in \mathbb { C }$ . Prove that 0 is a removable singularity or pole.

4. Suppose that U is a simply connected bounded domain in $\mathbb { C } .$ and let $P \in U$ . Prove that for all $t \in \mathbb { R }$ , there exists a unique holomorphic function $f : U \to U$ such that $f ( P ) = P$ and $f ^ { \prime } ( P ) = e ^ { i t }$

## Part II. Real Analysis.

Notation: |A| denotes the Lebesgue measure of a measurable set $A \subset \mathbb { R } ^ { n }$

5. Give an example of a sequence of functions $\{ f _ { j } \}$ satisfying $\| f _ { j } \| _ { L ^ { 2 } ( \mathbb { R } ) } = 1$ for which $\{ f _ { j } \}$ has no convergent subsequence in $L ^ { 2 } ( \mathbb { R } )$ .

6. a) Let $f _ { j } \in L ^ { 2 } ( \mathbb { R } ^ { n } )$ and suppose that

$$
\int _ { \mathbb { R } ^ { n } } | f _ { j } ( x ) - f ( x ) | ^ { 2 } d x \to 0 .
$$

If $\Omega \subset \mathbb { R } ^ { n }$ has finite Lebesgue measure, i.e., $| \Omega | < \infty$ , show that the Fourier transforms satisfy

$$
\int _ { \Omega } { \widehat { f } } _ { j } ( \xi ) d \xi \to \int _ { \Omega } { \widehat { f } } ( \xi ) d \xi .\tag{1}
$$

b) If $| \Omega | = \infty$ , is (1) still always valid? Give a proof or counterexample.

7. Let $\omega ( \alpha ) = | \{ x : | f ( x ) | > \alpha \} | , \alpha > 0$ , be the distribution function of a given $f \in$ $L ^ { p } ( \mathbb { R } ^ { n } )$ , where $p > 0$ Does $\alpha ^ { p } \omega ( \alpha )$ tend to a limit as $\alpha  0 + ?$ Give a proof or counterexample.

8. Show that there does not exist a function $I \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ such that

$$
f * I = f \qquad { \mathrm { f o r ~ a l l ~ } } f \in L ^ { 1 } ( \mathbb { R } ^ { n } ) .
$$

(Here $\begin{array} { r } { ( f * I ) ( x ) = \int f ( y ) I ( x - y ) } \end{array}$ dy is the convolution of f and I.)

# ANALYSIS QUALIFYING EXAM MAY 2011

All problems are equally weighted. Show all your work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

Time: 3 hours.

Part I. Complex Analysis.

Notation: $D = \{ z \in \mathbb { C } : | z | < 1 \}$

1. Find all entire functions f such that $| f ( z ) | = 1$ whenever $| z | = 1$ . Give explicit formulas for the functions and give a proof for your answer. (An entire function is a holomorphic function on C.)

2. Let $f : D \to \mathbb { C }$ be a holomorphic function with simple zeros at the points $1 / 3 , 2 / 3 , i / 4$ and no other zeros. Determine the value of the integral

$$
\int _ { \{ | z | = 1 / 2 \} } ( z ^ { 2 } - 1 ) e ^ { z } { \frac { f ^ { \prime } ( z ) } { f ( z ) } } d z ,
$$

where the direction of integration is counterclockwise.

3. Let U be a bounded domain in C, and let $f : U \to U$ such that f is holomorphic. Let $P \in U$ and suppose that $f ( P ) = P$ . Prove that $| f ^ { \prime } ( P ) | \leq 1$

Hint: Consider the sequence of iterates $f _ { n } = f \circ f \circ \cdot \cdot \cdot \circ f \ ( n { \mathrm { ~ t i m e s } } )$

4. Suppose that $u : \mathbb { C } \to \mathbb { R }$ is a harmonic function such that

$$
u ( z ) \leq 1 0 \log ( | z | + 2 ) ,
$$

for all $z \in \mathbb { C }$ . Prove that u is constant.

## Part II. Real Analysis.

5. Let $f _ { n } : [ 0 , 1 ] \to \mathbb { R }$ , for $n = 1 , 2 , \ldots ,$ , be a sequence of $\mathcal { C } ^ { 1 }$ functions such that $f _ { n } ( t ) \leq 5$ and $| f _ { n } ^ { \prime } ( t ) | \leq 1$ for all $n , t$ . Define the functions $g _ { n } : [ 0 , 1 ] \to \mathbb { R }$ by

$$
g _ { n } ( t ) = \operatorname* { m a x } \{ f _ { 1 } ( t ) , \ldots , f _ { n } ( t ) \}
$$

for $n = 1 , 2 , \dots$ . Prove that the sequence $\left\{ g _ { n } \right\}$ converges uniformly on [0, 1].

6. Let $f \in L ^ { 1 } ( S ^ { 1 } )$ such that ${ \widehat { f } } \in \ell ^ { 1 } ( \mathbb { Z } )$ . Prove that $f \in { \mathcal { C } } ( S ^ { 1 } )$ (continuous functions on the circle S1).

7. Suppose that $f \in L ^ { \infty } ( [ 0 , 1 ] )$

a) Prove that if 1 $< p < \infty$ then $\| f \| _ { p } \leq \| f \| _ { \infty }$

b) Show that $\begin{array} { r } { \| f \| _ { \infty } \leq \operatorname* { l i m } _ { p \longrightarrow \infty } \| f \| _ { p } } \end{array}$ and therefore conclude that $\begin{array} { r } { \operatorname* { l i m } _ { p \to \infty } \| f \| _ { p } = \| f \| _ { \infty } } \end{array}$ Hint: Given $\varepsilon > 0$ , consider $A _ { \varepsilon } = \{ x \in [ 0 , 1 ] : | f ( x ) | > \| f \| _ { \infty } - \varepsilon \}$

8. a) Let $f _ { j } : \mathbb { R } ^ { n } \longrightarrow \mathbb { R }$ , for $j = 1 , 2 , \dots$ , be a sequence of $L ^ { 2 }$ functions. Suppose that there is a function $f \in L ^ { 2 } ( \mathbb { R } ^ { n } )$ such that

$$
\int _ { \mathbb { R } ^ { n } } f _ { j } g \to \int _ { \mathbb { R } ^ { n } } f g , \quad \forall g \in L ^ { 2 } ( \mathbb { R } ^ { n } ) .
$$

Show that

$$
\| f \| _ { 2 } \leq \operatorname* { l i m } _ { j \to \infty } \| f _ { j } \| _ { 2 } .
$$

Also, give an example showing that strict inequality can occur.

b) Suppose also that $\| f _ { j } \| _ { 2 } \to \| f \| _ { 2 }$ . Show that in this case $\| f _ { j } - f \| _ { 2 } \to 0 { \mathrm { ~ a s ~ } } j \to \infty .$

Instructions: Do all eight problems. Each problem will be scored out of 10 points.

1. Suppose that $f _ { j } \in L ^ { 2 } ( \mathbb { R } ^ { n } ) , j = 1 , 2 , 3 , . .$ . and that $f _ { j } \to f$ in $L ^ { 2 }$ . Suppose further that there is a constant $M < \infty$ so that

$$
\int e ^ { 1 0 0 | x | ^ { 2 } } | f _ { j } ( x ) | ^ { 2 } d x \leq M , \quad j = 1 , 2 , 3 , \ldots .
$$

Is it true that $\begin{array} { r } { \int e ^ { 9 9 | x | ^ { 2 } } | f ( x ) | ^ { 2 } d x < \infty ? } \end{array}$ Give a proof or counterexample.

2. Let $E , F \subset \mathbb { R }$ be two Lebesgue-measurable subsets of R, each of finite measure, and let $\chi _ { E }$ and $\chi _ { F }$ denote their respective characteristic functions.

(a) Prove that the convolution $\chi _ { E } * \chi _ { F }$ defined by

$$
\chi _ { E } * \chi _ { F } ( x ) = \int _ { \mathbb { R } } \chi _ { E } ( y ) \chi _ { F } ( x - y ) d y
$$

is a continuous function of $x .$

(b) Show that as $n \to \infty$

$$
n \big ( \chi _ { E } * \chi _ { [ 0 , 1 / n ] } \big ) \longrightarrow \chi _ { E }
$$

pointwise almost everywhere.

3. Let $\begin{array} { r } { T f ( x ) = \int _ { \mathbb { R } ^ { n } } K ( x , y ) f ( y ) d y } \end{array}$ , where $K ( x , y )$ is a nonnegative measurable function on $\mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ . Suppose that there are measurable functions $p ( x ) > 0$ and $q ( x ) > 0$ o n $\mathbb { R } ^ { n }$ and real numbers $\alpha , \beta > 0$ for which

$$
\int K ( x , y ) q ( y ) d y \leq \alpha p ( x ) ,
$$

for almost all x and

$$
\int p ( x ) K ( x , y ) d x \leq \beta q ( y )
$$

for almost all y. Show that for $f \in L ^ { 2 } ( \mathbb { R } ^ { n } )$ we have

$$
\| T f \| _ { L ^ { 2 } } \leq \sqrt { \alpha \beta } \| f \| _ { L ^ { 2 } } .
$$

(This is called Schur’s test.)

4. Define $U : L ^ { 2 } ( \mathbb { R } ) \to L ^ { 2 } ( \mathbb { R } )$ by

$$
U f ( x ) = f ( x - 1 ) .
$$

Show that if $f \in L ^ { 2 }$ satisfies $U f = \lambda f$ , for some $\lambda \in \mathbb { R } \ ( \mathrm { i . e . , } \ f$ is an eigenvector of U ) then f must be the zero element, i.e., $f = 0$ almost everywhere.

[cont’d on other side]

5. Let $\gamma$ be the closed curve in the complex plane that is given in polar coordinates by $r = 2 + 3$ cos θ, $0 \leq \theta \leq 4 \pi$ , oriented in the direction of increasing θ. Let

$$
f ( z ) = \frac { e ^ { z } } { 2 z - 1 } + \frac { \sin ( 2 z ) } { ( z - 2 ) ^ { 2 } } + \frac { \cos ( 5 z ) } { ( z + 5 i ) ^ { 3 } } .
$$

Calculate $\int _ { \gamma } f ( z ) d z$

[Recall that in polar coordinates, $( - r , \theta )$ and $( r , \theta + \pi )$ give the same point in the plane.]

6. Let D denote the open unit disc in C. Let $f : D  \mathbb { C }$ be a $C ^ { 1 }$ function, and consider the property: $f$ has a double zero at $\textstyle z = { \frac { 1 } { n } }$ for all natural numbers n.

(a) Determine all holomorphic functions f with this property. [The terms “holomorphic” and “complex analytic” have the same meaning.]

(b) Give an example of a non-holomorphic $C ^ { 1 }$ function with this property. (You must explain why your example has this property.)

7. Determine all entire functions $f \ ( \mathrm { i . e . } , \ f ( z )$ is holomorphic and is defined for all $z \in \mathbb { C } )$ that satisfy the inequality:

$$
| f ( z ) | \leq | \mathrm { R e } z | ^ { 2 } + | z | ^ { \frac { 3 } { 2 } } \quad \mathrm { w h e n e v e r ~ } | z | > 1 .
$$

8. Let D denote the open unit disc, as in $\# 6$ . Let $g : D  D$ be a surjective holomorphic mapping for which $g ( 0 ) = 0$ . Suppose that $z = g ( w )$ gives a two-sheeted branched covering of the image with exactly one branch point at $w = 0$ . An example of such a function g is $g ( w ) = \bar { w ^ { 2 } }$

(a) Express the given conditions explicitly in terms of $g$ and its derivatives.

(b) Show that $| g ( w ) | \leq | w | ^ { 2 }$ for all $| w | < 1$

(c) Suppose that $g ( 1 / 2 ) = i / 4$ . What is the strongest statement about $g ( w )$ that follows from the assertion in (b)? Explain.

# ANALYSIS QUALIFYING EXAM MAY 2010

All problems are equally weighted. Show all your work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

Time: 3 hours.

## Part I. Complex Analysis.

1. Let f be a holomorphic function on the punctured disk

$$
U : = \left\{ z \in \mathbb { C } : 0 < | z | < 1 \right\} .
$$

Suppose that $| f ( z ) | \leq | z | ^ { - 1 / 2 }$ for all $z \in U$ . Prove that f has a removable singularity at 0.

2. Find all possible values of

$$
\int _ { \gamma } { \frac { e ^ { \pi z } } { ( z - 1 ) ( z - i ) ^ { 2 } } } d z
$$

where γ ranges over all simple closed smooth curves contained in $\mathbb { C } \setminus \{ 1 , i \}$ . (A simple closed curve is a closed curve that does not intersect itself; i.e., it is a homeomorphic image of the circle.)

You do not need to give a proof for your answer to this problem, but show all your work.

3. Let $\mathcal { O } ( D )$ denote the space of holomorphic functions on the unit disk D and let

$$
{ \mathcal H } = { \mathcal O } ( D ) \cap L ^ { 2 } ( D ) = \left\{ f \in { \mathcal O } ( D ) : \int _ { D } | f | ^ { 2 } d x d y < + \infty \right\} .
$$

a) Show that for all compact sets $K \subset D$ , there is a constant $C _ { K } \in \mathbb { R } ^ { + }$ such that

$$
\operatorname* { s u p } _ { z \in K } | f ( z ) | \leq C _ { K } \| f \| _ { L ^ { 2 } ( D ) } .
$$

b) Show that H is a closed subspace of $L ^ { 2 } ( D )$ and hence is a Hilbert space.

4. Let h be a harmonic function on the domain

$$
U : = \left\{ z \in \mathbb { C } : | z | > 1 \right\} .
$$

Show that there exists a constant $c \in \mathbb { R }$ and a holomorphic function $f$ on $U$ such that $\mathrm { R e } f ( z ) = h ( z ) + c \log | z |$ for all $z \in U$

5. Let $f _ { j } \in L ^ { 2 } ( \mathbb { R } ^ { n } )$ , and ${ \widehat { f } } _ { j }$ denote its Fourier transform for $j = 1 , 2 , 3 \ldots$ . Suppose that $f _ { j } \to f$ in $L ^ { 2 }$ and that there is a finite constant M so that

$$
\| f _ { j } \| _ { H ^ { \sigma } } \leq M , \quad j = 1 , 2 , 3 , \ldots ,
$$

for some $\sigma \in \mathbb { R }$ , where $\begin{array} { r } { \| g \| _ { H ^ { \sigma } } = \left( \int _ { \mathbb { R } ^ { n } } ( 1 + | \xi | ^ { 2 } ) ^ { \sigma } | \widehat { g } ( \xi ) | ^ { 2 } d \xi \right) ^ { 1 / 2 } } \end{array}$ denotes the $H ^ { \sigma }$ Sobolev norm of g. Is it necessarily true that $\| f \| _ { H ^ { \sigma } } < \infty ?$ Give a proof or counterexample.

6. Let $\varphi : \mathbb { R }  \mathbb { R }$ be a continuous function with compact support.

a) Prove that if $1 \leq p \leq q \leq \infty$ are fixed then there is a constant A such that

$$
\| f * \varphi \| _ { L ^ { q } } \leq A \| f \| _ { L ^ { p } } , \quad { \mathrm { f o r ~ a l l } } \quad f \in L ^ { p } .
$$

If you use Young’s (convolution) inequality, you should prove it.

b) Show by example that such a general inequality cannot hold for $p > q$

## 7. Suppose that

$$
f : [ 0 , 1 ] \times [ 0 , 1 ] \to \mathbb { R }
$$

is continuous and has the property that for each x the map $t \to f ( x , t )$ is differentiable and that $\begin{array} { r } { \left| \frac { \partial f } { \partial t } ( x , t ) \right| \le g ( x ) } \end{array}$ for some measurable function statisfying $\textstyle \int _ { 0 } ^ { 1 } g ( x ) d x < \infty$ Carefully prove that $\textstyle F ( t ) = \int _ { 0 } ^ { 1 } f ( x , t )$ dx satisfies

$$
F ^ { \prime } ( t ) = \int _ { 0 } ^ { 1 } { \frac { \partial f } { \partial t } } ( x , t ) d x .
$$

## 8. Let E be a measurable subset of the line.

a) Let $\chi _ { E } : \mathbb { R } \to \mathbb { R }$ be the characteristic function of $E ~ ( \mathrm { i . e . } ~ \chi _ { E } ( x ) = 1$ when $x \in E$ and $\chi _ { E } ( x ) = 0$ when $x \notin E )$ . If E has finite Lebesgue measure, show that the function $f : \mathbb { R } \to \mathbb { R }$ defined by

$$
f ( x ) = \int _ { \mathbb { R } } \chi _ { E } ( y ) \chi _ { E } ( y - x ) d y
$$

is continuous.

b) Suppose instead that E has positive Lebesgue measure $0 < | E | \le \infty$ . Using a), show that the set $E - E = \{ x - y : x , y \in E \}$ contains an open interval $( - \varepsilon , \varepsilon )$ for some $\varepsilon > 0$

# ANALYSIS QUALIFYING EXAM SEPTEMBER 2009

All problems are equally weighted. Show all your work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

Time: 3 hours.

Part I. Real Analysis. Do 3 out of the following 4 problems.

1. Suppose $f _ { n }$ is a sequence of continuous functions on [0, 1] which converges to a continuous function $f$ on [0, 1]. Does it follow that $f _ { n }$ converge uniformly? Give a proof or provide a counterexample.

2. For which values of $\sigma \in \mathbb { R }$ does there exist a constant $C _ { \sigma } < + \infty$ such that

$$
\left| \sum _ { j , k = 1 } ^ { \infty } ( 1 + | j - k | ) ^ { \sigma } a _ { j } b _ { k } \right| \leq C _ { \sigma } ( \sum _ { j = 1 } ^ { \infty } | a _ { j } | ^ { 2 } ) ^ { 1 / 2 } ( \sum _ { k = 1 } ^ { \infty } | b _ { k } | ^ { 2 } ) ^ { 1 / 2 }
$$

Prove your assertion.

3. Let I be the unit interval [0, 1], and for $n = 1 , 2 , 3 , . . .$ . and $0 \leq j \leq 2 ^ { n } - 1$ let

$$
I _ { n , j } = [ j 2 ^ { - n } , ( j + 1 ) 2 ^ { - n } ] .
$$

For $f \ \in \ L ^ { 1 } ( I , d x )$ define $\begin{array} { r } { E _ { n } f ( x ) \ = \ \sum _ { j = 0 } ^ { 2 ^ { n } - 1 } ( 2 ^ { n } \int _ { I _ { n , j } } f d t ) \chi _ { I _ { n , j } } ( x ) } \end{array}$ , where $\chi _ { I _ { n , j } }$ is the characteristic function of $I _ { n , j }$ . Prove that if $f \in L ^ { 1 } ( \bar { I } , d x )$ then lim $\mathfrak { l } _ { n \to \infty } E _ { n } f ( x ) = f ( x )$ almost everywhere in I.

4. Let $f ( x )$ be a non-decreasing function on [0, 1]. You may assume that f is differentiable almost everywhere. Prove that

$$
\int _ { 0 } ^ { 1 } f ^ { \prime } ( x ) d x \leq f ( 1 ) - f ( 0 ) .
$$

## Part II. Complex Analysis. Do 3 out of the following 4 problems.

5. Let

$$
f ( x + i y ) = x ^ { 3 } - 3 x y ^ { 2 } + i y ^ { 3 } .
$$

State whether each of the following is true or false and give proofs for your answers:

a) the complex derivative $f ^ { \prime } ( 0 )$ exists;

b) f is holomorphic in a neighborhood of 0.

6. Let

$$
f ( z ) = { \frac { z } { \tan z } } \qquad { \mathrm { f o r } } ~ z \neq 0 .
$$

a) Prove that f has a removable singularity at 0.

b) What is the radius of convergence of the power series for f centered at 0? Justify your answer.

7. Let $f : H  D$ be a holomorphic map from the upper half plane

$H = \left\{ z \in \mathbb { C } : \operatorname { I m } z > 0 \right\}$ to the unit disk $D = \{ z \in \mathbb { C } : | z | < 1 \}$

Suppose that $f ( i ) = 1 / 2$ . Determine the maximal possible value of $| f ^ { \prime } ( i ) |$

8. Let h be a harmonic function on the punctured disk

$$
U : = \left\{ z \in \mathbb { C } : 0 < | z | < 1 \right\} .
$$

Show that there exists a constant $c \in \mathbb { R }$ and a holomorphic function f on U such that $\mathrm { R e } f ( z ) = h ( z ) + c \log | z |$ for all $z \in U$

# ANALYSIS QUALIFYING EXAM MAY 2009

Do all 8 problems. All problems are equally weighted. Show all your work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

## Time: 3 hours.

1. Find all meromorphic functions f on C such that

$$
| f ( z ) | \leq { \frac { \log ( 2 + | z | ^ { 2 } ) } { | z | } } \qquad { \mathrm { f o r ~ a l l ~ } } z \neq 0 .
$$

Give explicit formulas for the functions and give a proof for your answer.

2. How many solutions does the equation

$$
z + e ^ { - z } = 2 + i
$$

have in the half-plane Re $z > 0 ?$ Prove that your answer is correct.

3. Let $f _ { n } : U \to \mathbb { C } , n = 1 , 2 , 3 , . . . ,$ be a sequence of holomorphic functions such that $f _ { n } ^ { - 1 } ( 0 ) = \{ c _ { n } \}$ , where $c _ { n } \in U$ , and U is a connected open set. Suppose that $f _ { n }  f _ { 0 }$ uniformly, where $f _ { 0 }$ is not constant.

a) Prove that $f _ { 0 }$ has at most one zero in $U$

b) Can $f _ { 0 }$ have no zeros? If so, give a necessary and sufficient condition on the $c _ { n }$ for this to happen.

4. Let $f ( x ) = { \frac { 1 } { x ^ { 2 } + 1 } }$ . Use a contour integral consisting of the interval $[ - R , R ] \subset \mathbb { R }$ and a semicircle of radius R to compute the Fourier transform

$$
{ \widehat { f } } ( 1 ) = \int _ { \mathbb { R } } f ( x ) e ^ { - i x } d x ~ .
$$

Show that the contour integral converges to your answer as $R \to + \infty$

5. Let $f , g \in L ^ { 2 } ( \mathbb { R } )$ be two square-integrable functions on R (with the usual Lebesgue measure). Show that the convolution

$$
f * g ( x ) = \int _ { \mathbb { R } } f ( y ) g ( x - y ) d y
$$

of $f$ and g is a bounded continuous function on $\mathbb { R } .$

6. Let $\mathbb { R } / \mathbb { Z }$ be the unit circle with the usual Lebesgue measure. For each $n = 1 , 2 , 3 , . . .$ let $K _ { n } : \mathbb { R } / \mathbb { Z } \to \mathbb { R } _ { + }$ be a nonnegative integrable function such that $\begin{array} { r } { \int _ { \mathbb { R } / \mathbb { Z } } K _ { n } ( t ) d t = 1 } \end{array}$ and lim $\begin{array} { r } { { \bf \delta } _ { \cdot n \longrightarrow \infty } \int _ { \varepsilon \le | t | \le 1 / 2 } K _ { n } ( t ) d t = 0 } \end{array}$ for every $0 < \varepsilon < 1 / 2$ , where we identify R $/ \mathbb { Z }$ with $( - 1 / 2 , 1 / 2 ]$ in the usual way. (Such a sequence of $K _ { n }$ are called approximations to the identity.) Let $f : \mathbb { R } / \mathbb { Z } \to \mathbb { R }$ be continuous, and define the convolutions $f * K _ { n } : \mathbb { R } / \mathbb { Z } \to$ R by

$$
f * K _ { n } ( x ) = \int _ { \mathbb { R } / \mathbb { Z } } f ( x - t ) K _ { n } ( t ) d t .
$$

Show that $f * K _ { n }$ converges uniformly to $f$ .

7. Fix $1 \leq p < \infty$ and let $\{ f _ { n } \} _ { n = 1 } ^ { \infty }$ be a sequence of Lebesgue measurable functions $f _ { n } : [ 0 , 1 ] \to \mathbb { C }$ . Suppose there exists $f \in L ^ { p } ( [ 0 , 1 ] )$ such that $f _ { n }  f$ in $L ^ { p }$ , that is,

$$
\int _ { [ 0 , 1 ] } | f _ { n } ( x ) - f ( x ) | ^ { p } d x \to 0 .
$$

a) Show that $f _ { n } \to f$ in measure, that is,

$$
\operatorname* { l i m } _ { n \to \infty } \mu ( \{ x \in [ 0 , 1 ] : | f _ { n } ( x ) - f ( x ) | \geq \varepsilon \} ) = 0
$$

for all $\varepsilon > 0$ . (Here $\mu = \mathrm { L e b e s g u e }$ measure.)

b) Show that there is a subsequence $f _ { n _ { k } }$ such that $f _ { n _ { k } } ( x )  f ( x )$ almost everywhere.

8. Consider [0, 1] with Lebesgue measure. Let $f \in L ^ { \infty } ( [ 0 , 1 ] )$ and define

$$
a _ { n } = \int _ { [ 0 , 1 ] } | f | ^ { n } d x .
$$

Show that

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { a _ { n + 1 } } { a _ { n } } } = \| f \| _ { \infty } .
$$

# PROBLEMS FOR ANALYSIS QUALIFYING EXAM Fall 2008

Do all seven problems. Show all work and state any theorems you are using.   
Time: 3 hours.

1) (15 points) Consider the mapping $F : [ 0 , 1 ]  [ 0 , 1 ]$ given by $F ( s ) = s ^ { 2 }$

Let $F ^ { - j } ( A )$ be the inverse image of j iterates of F applied to a measurable subset $A \subset [ 0 , 1 ]$ . That is, if $F = F ^ { 1 }$ and $F ^ { j } , j = 2 , 3 , . .$ . is defined inductively as $F ^ { j } = F ^ { j - 1 } \circ F$ then $F ^ { - j } ( A ) = \{ x : F ^ { j } x = y$ , some $y \in A \}$

a) Given $N = 1 , 2 , \dots$ show that $\begin{array} { r } { \mu _ { N } ( A ) = N ^ { - 1 } \sum _ { j < N } | F ^ { - j } ( A ) | } \end{array}$ is a measure which is absolutely continuous with respect to Lebesgue measure. Here |B| denotes the Lebesgue measure of a measurable set.

b) Show that $\mu _ { N } ( [ a , b ] ) \to 0 { \mathrm { ~ i f ~ } } 0 < a < b \leq 1$

c) If f is a continuous function on [0, 1] does lim $\begin{array} { r } { \int _ { [ 0 , 1 ] } f ( s ) d \mu _ { N } ( s ) } \end{array}$ tend to a limit? If so, what is the limit?

2) (10 points) Let $( X , { \mathcal { M } } , \mu )$ and $( Y , \mathcal { N } , \nu )$ be σ-finite measure spaces and let $K ( x , y )$ be a measurable function with respect to the product σ-algebra $\mathcal { M } \times \mathcal { N }$ . Assume that there is a constant $0 < A <$ ∞ so that for all $x \in X$

$$
\int _ { Y } | K ( x , y ) | d \nu ( y ) \leq A ,
$$

and for all $y \in Y$

$$
\int _ { X } | K ( x , y ) | d \mu ( x ) \leq A .
$$

Let $1 \leq p \leq \infty$ and for $f \in L ^ { p } ( X , \mathcal { M } , \mu )$ define

$$
T f ( y ) = \int _ { X } f ( x ) K ( x , y ) d \mu ( x ) .
$$

Prove that

$$
\| T F \| _ { L ^ { p } ( \nu ) } \leq A \| f \| _ { L ^ { p } ( \mu ) } .
$$

3) (10 points) Is the Banach space $\ell ^ { \infty }$ of bounded complex sequences $a = \{ a _ { n } \} _ { n = 1 } ^ { \infty }$ with the supremum norm $\left\| a \right\| _ { \infty } = \operatorname* { s u p } _ { n } \left| a _ { n } \right|$ separable? Prove your assertion.

4) (10 points) Use residues to verify that

$$
\int _ { 0 } ^ { \infty } \frac { \ln x } { ( x ^ { 2 } + 4 ) ^ { 2 } } d x = \frac { \pi } { 3 2 } ( \ln 2 - 1 ) .
$$

5) (10 points) How many solutions does the equation

$$
e ^ { z } = 3 z ^ { 7 }
$$

have in the unit disk $D = \{ x \in \mathbb { C } : | z | < 1 \} ?$ Justify your answer.

6) (10 points) Let $f : \mathbb { C } \to \mathbb { C }$ be an entire function. Prove that if there exists some real number C and some positive integer k so that

$$
| f ( z ) | \leq C | z | ^ { k }
$$

for all z with $| z | > 1$ , then f is a polynomial in z of degree at most $k .$

7) (10 points) Let $D \subset \mathbb { C }$ be the unit disk and $\Omega \subset \mathbb { C }$ a bounded, simply connected domain. If $f _ { 1 } : D \to \Omega$ and $f _ { 2 } : D \to \Omega$ are holomorphic bijections so that $f _ { 1 } ( 0 ) = f _ { 2 } ( 0 )$ 2 then how are $f _ { 1 }$ and $f _ { 2 }$ related to each other?

# PROBLEMS FOR ANALYSIS QUALIFYING EXAM SPRING 2008

Do all eight problems. Show all work and state any theorems you are using. Time: 3 hours.

1) Let $E , F$ be two Lebesgue measurable subsets of R of finite measure, and let $\chi _ { E } , \chi _ { F }$ be their respective characteristic functions.

a) Show that the convolution $\chi _ { E } * \chi _ { F }$ defined by

$$
\chi _ { E } * \chi _ { F } ( x ) = \int _ { \mathbb { R } } \chi _ { E } ( y ) \chi _ { F } ( x - y ) d y
$$

is a continuous function.

b) Show that

$$
n \big ( \chi _ { E } * \chi _ { [ 0 , 1 / n ] } \big ) \to \chi _ { E }
$$

as $n \to \infty$ pointwise almost everywhere.

2) Consider $L ^ { \infty } ( [ 0 , 1 ] )$

a) If f belongs to this space prove that

$$
\operatorname* { l i m } _ { p \to \infty } \left( \int _ { 0 } ^ { 1 } | f | ^ { p } d x \right) ^ { 1 / p } = \| f \| _ { \infty } .
$$

b) Give an example showing that this is false if we replace $L ^ { \infty } ( [ 0 , 1 ] )$ by $L ^ { \infty } ( \mathbb { R } )$

3) Assume that $f$ is a continuously differentiable 2π periodic function on R. Show that the Fourier series

$$
\sum _ { n = - \infty } ^ { \infty } \hat { f } ( n ) e ^ { i n t }
$$

is absolutely convergent for every t (here $\begin{array} { r } { { \hat { f } } ( n ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } f ( t ) e ^ { - i n t } d t ) } \end{array}$

4) Let $\ell ^ { 2 }$ be the space of all square-summable sequences of complex numbers, and let $T : \ell ^ { 2 } \to \ell ^ { 2 }$ be a linear operator. Let $e _ { n }$ be the sequence

$$
e _ { n } = ( 0 0 \cdot \cdot \cdot 0 1 0 \cdot \cdot \cdot ) ,
$$

where 1 is in the n-th position. Let $\boldsymbol { a } _ { m n } = \langle T \boldsymbol { e } _ { m } , \boldsymbol { e } _ { n } \rangle$ be the “matrix coefficients” of T .

a) Assume that $\begin{array} { r } { \sum _ { n , m = 1 } ^ { \infty } | a _ { m n } | ^ { 2 } < \infty } \end{array}$ . Show that T is a bounded operator on $\ell ^ { 2 }$

b) Assume instead that sup $\left\{ \left| a _ { m n } \right| : 1 \leq n , m < \infty \right\}$ is finite. Must T be bounded? Explain.

5) Prove the following statement: If f and g are entire functions, $g ( z ) \neq 0$ and $| f ( z ) | \leq | g ( z ) |$ for all $z \in \mathbf { C } .$ , then $f ( z ) = C g ( z )$ for some constant C.

6) Let $D = \{ z \in \mathbf { C } : | z | < 1 \}$ and P and Q be distinct points in D. Prove the following statement: If f and g are conformal (or equivalently biholomorphic) self-maps of D, $f ( P ) = g ( P )$ and $f ( Q ) = g ( Q )$ , then $f \equiv g$

7) Let $U \subset \mathbf { C }$ be an open set, $P \in U$ and f a holomorphic function defined on U so that $f ( P ) = f ^ { \prime } ( P ) = 0$ . Use the Argument Principle to prove the following statement: There exists $\delta > 0$ so that if $0 < | Q | < \delta ,$ , then $f ^ { - 1 } ( Q )$ contains at least two points.

8) Let $U \subset \mathbf { C }$ be an open set and $P \in U$ . Let F be a family of holomorphic functions from U into the unit disc $D = \{ z \in \mathbf { C } : | z | < 1 \}$ that take P to 0.

(a) Show that sup $\{ | f ^ { \prime } ( P ) | : f \in { \mathcal { F } } \} < \infty$

(b) Show that there exists a sequence $\{ f _ { n } \} \subset \mathcal { F }$ and a holomorphic function $f _ { 0 } : U \to D$ so that $\left\{ f _ { n } \right\}$ converges uniformly to $f _ { 0 }$ on every compact subset of U and $f _ { 0 } ^ { \prime } ( P ) = \operatorname* { s u p } \{ | f ^ { \prime } ( P ) | : f \in \mathcal { F } \}$ .

# ANALYSIS QUALIFYING EXAM FALL 2007

(1) Is the function

$$
f ( x , y ) = x ^ { 3 } + 3 x y ^ { 2 } - 3 x ^ { 2 } y - 1 0 + i ( y ^ { 3 } + 3 x ^ { 2 } y - 3 y ^ { 2 } x + 5 )
$$

complex analytic? Prove that your answer is correct.

(2) Find all entire analytic functions satisfying $| f ( z ) | \leq | e ^ { z } |$ for all $z \in \mathbb { C }$

(3) Let A be the annulus $A = \left\{ z \in \mathbb { C } : 1 < | z | < 2 \right\}$ Let f be a non-constant holomorphic function in a neighborhood of A, and suppose that $| f ( z ) | = 1$ on ∂A (the boundary of A). Prove that f has at least 2 zeros in A.

(4) Use the residue calculus to compute $\int _ { 0 } ^ { \infty } { \frac { d x } { 1 + x ^ { n } } }$

(5) Give examples of functions f and g on R so that $f \in L ^ { 1 } \setminus L ^ { 2 }$ and $g \in L ^ { 2 } \setminus L ^ { 1 }$

(6) Does there exist an open dense subset of R with Lebesgue measure equal to one? Either construct an example or prove that one does not exist.

(7) Let $f _ { n }$ be a sequence of measurable real-valued functions on [0, 1] with

$$
\sum _ { n = 1 } ^ { \infty } \left( \int _ { 0 } ^ { 1 } | f _ { n } | \right) \leq 1 .
$$

Prove that $f _ { n }$ converges to zero almost everywhere.

(8) Suppose that f and g are R $L ^ { 1 } ( \mathbb { R } )$ functions with compact support and let h be the convolution $\begin{array} { r } { f \star g \ ( \mathrm { i . e . , \ } h ( x ) = \int f ( x - y ) g ( y ) d y ) } \end{array}$ . Prove that h is uniformly continuous.

# PROBLEMS FOR ANALYSIS QUALIFYING EXAM SPRING 2007

(1) How many zeros does the polynomial $z ^ { 6 } - 2 z ^ { 5 } + 7 z ^ { 4 } + z ^ { 3 } - z + 1$ have in the open unit disc $D = \{ z : | z | < 1 \} ?$

(2) Calculate the integral $\textstyle \int _ { 0 } ^ { 2 \pi } { \frac { d \theta } { 1 - 2 a \cos \theta + a ^ { 2 } } }$ , where $0 < a < 1$

(3) Let $f : D  D$ be a holomorphic map of the unit disc with $f ( 0 ) = 0$ , and suppose that $f$ is not a rotation (a rotation is a map $r _ { \theta } ( z ) = e ^ { i \theta } z )$ . Let $w \in D$ and consider the sequence $\{ w _ { n } \}$ defined by ${ w _ { n + 1 } } = f ( w _ { n } )$ . Show: $\scriptstyle \operatorname* { l i m } _ { n \to \infty } w _ { n } = 0$

(4) Does there exist a surjective holomorphic map $f : D \to \mathbb { C }$ from the unit disc to the whole complex plane? Prove that your answer is correct.

(5) For which $p \mathrm { ^ s }$ is the function $1 / x$ in $L ^ { p } ( 0 , \infty ) ?$

(6) Suppose that $f _ { n } : [ 0 , 1 ] \to \mathbb { R }$ is a sequence of $L ^ { 4 }$ functions with $\textstyle \int f _ { n } ^ { 4 } \leq 1$ for every n and so that $\begin{array} { r } { \operatorname* { l i m } _ { n \longrightarrow \infty } \int \left| f _ { n } \right| = 0 } \end{array}$ . Show that $f _ { n }$ goes to 0 weakly in $L ^ { 4 }$

(7) Suppose that $f _ { n }$ is a sequence of functions in $L ^ { 2 } ( \mathbb { R } )$ that converges weakly in $L ^ { 2 }$ to a function $f \in L ^ { 2 } ( \mathbb { R } )$ . Is it possible to have

$$
\operatorname* { l i m } _ { n \to \infty } | | f _ { n } | | _ { L ^ { 2 } } = \infty ?
$$

(8) Suppose that $f \in L ^ { 1 } ( \mathbb { R } )$ and $\begin{array} { r } { \widehat { f } ( z ) = \int _ { \mathbb { R } } e ^ { - i x z } f ( x ) } \end{array}$ dx. Show that $f$ and $\widehat { f }$ cannot both have compact support (except if $f$ is identically zero).

# ANALYSIS QUALIFYING EXAM SEPTEMBER 2006

Do all 8 problems. All problems are equally weighted. Time: 3 hours.

Show all work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

Notation: $D = \{ z \in \mathbb { C } : | z | < 1 \}$

1. Use residues to calculate the integral

$$
\int _ { 0 } ^ { \infty } { \frac { d x } { x ^ { 4 } + 4 } } .
$$

2. Let $f _ { n } : D \to \mathbb { C } , n = 1 , 2 , 3 , . . . ,$ be a sequence of holomorphic functions on the unit disk D such that $f _ { n } ^ { - 1 } ( 0 ) = \{ c _ { n } \}$ , where $c _ { n } \in D$ . Suppose that $f _ { n }  f _ { 0 }$ uniformly, where $f _ { 0 }$ is not constant.

a) Prove that $f _ { 0 }$ has at most one zero in $D$

b) Can $f _ { 0 }$ have no zeros? If so, give a necessary and sufficient condition on the $c _ { n }$ for this to happen.

3. State whether each of the following two statements is true or false, and give either a proof or counterexample for each.

a) All holomorphic functions $f : \mathbb { C } \setminus \{ 0 \} \to H$ are constant, where $H = \{ z \in \mathbb { C }$ Im $z > 0 \}$ denotes the upper half plane.

b) All harmonic functions $h : \mathbb { C } \setminus [ 0 , + \infty ) \to [ 0 , 1 ]$ are constant.

4. Let $f : D  H$ be a holomorphic map from the unit disk D to the upper half plane $H = \left\{ z \in \mathbb { C } : \operatorname { I m } z > 0 \right\}$

Suppose that $f ( 0 ) = 3 i$ . Find the maximal possible value of $\left| f ^ { \prime } ( 0 ) \right|$

5. Let X be the Banach space of continuous real-valued functions on [0, π] that vanish at 0 and $\pi ,$ equipped with the sup norm. Suppose that Y is a closed subspace of X where every element of $Y$ can be written as a trigonometric polynomial, i.e., as a finite linear combination of the functions sin(kx) and $\cos ( k x )$ , for $k = 0 , 1 , 2 , 3 , \ldots$ . Prove that $Y$ is finite dimensional.

CONTINUED ON NEXT PAGE

6. Suppose that f is a $C ^ { 1 }$ function on $[ 0 , 2 ]$ and $f ( 0 ) = f ^ { \prime } ( 0 ) = f ( 2 ) = f ^ { \prime } ( 2 ) = 0$ . Prove that for any $\varepsilon > 0$ there exists $T _ { \varepsilon }$ so that for all $t > T _ { \varepsilon }$

$$
\left| \int _ { 0 } ^ { 2 } f ( x ) e ^ { i t x } d x \right| \leq { \frac { \varepsilon } { t } } .
$$

7. Suppose that $f _ { j }$ is a sequence of $L ^ { 2 }$ functions on [0, 1] with

$$
\int _ { 0 } ^ { 1 } | f _ { j } | \leq 1 / j \quad \mathrm { a n d } \quad \int _ { 0 } ^ { 1 } f _ { j } ^ { 2 } \leq 1 .
$$

Prove that $f _ { j }$ goes to zero weakly in $L ^ { 2 } ( [ 0 , 1 ] )$

8. Suppose that X is a real Banach space and, for all $x , y \in X$ , the norm $\| \cdot \|$ satisfies

$$
\| x + y \| ^ { 2 } + \| x - y \| ^ { 2 } \leq 2 \| x \| ^ { 2 } + 2 \| y \| ^ { 2 } .
$$

Suppose also that $f : X \to \mathbb { R }$ is a linear functional with norm 1; that is,

$$
\operatorname* { s u p } _ { \| \boldsymbol { x } \| = 1 } | f ( \boldsymbol { x } ) | = 1 .
$$

Prove that there exists a unique point $x \in X$ with $\| { \boldsymbol x } \| = 1$ and $f ( x ) = 1$

# ANALYSIS QUALIFYING EXAM MAY 2006

All problems are equally weighted. Time: 3 hours.

Show all work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

Part I. Complex Analysis. Do 5 out of the following 6 problems.

1. Let P be a point in an open set U in C, and suppose that f is a meromorphic function on U with a pole at P . Prove that there is no holomorphic function $g : U \setminus \{ P \} \to \mathbb { C }$ such that $e ^ { g ( z ) } = f ( z )$ for all $z \in U \setminus \{ P \}$

2. How many zeros does the polynomial

$$
z ^ { 7 } - 4 z ^ { 3 } + z - { \textstyle { \frac { 1 } { 2 } } }
$$

have in the unit disk $\{ | z | < 1 \} \stackrel { . } { : }$ How many zeros does it have in the disk $\{ | z | < 2 \}$ of radius 2? Justify your answers.

3. Find all entire functions f such that $| f ( z ) | \le | z | ^ { 3 / 2 }$ whenever $| z | \geq 1$ . Give explicit formulas for the functions and give a proof for your answer. (An entire function is a holomorphic function on C.)

4. Let $f _ { n } : D \to ( - \infty , 1 ) , n = 1 , 2 , . . . ,$ be an increasing sequence of harmonic functions on the unit disk D such that $f _ { n } ( 0 ) \to 1$ as $n \to \infty$ . (I.e., $f _ { n } ( z ) \leq f _ { n + 1 } ( z ) < 1 , \forall n \geq 1 . )$ Prove that $f _ { n } ( z ) \to 1$ as $n \to \infty$ , for all $z \in D$

5. Let H denote the upper half plane $\{ z \in \mathbb { C } : \operatorname { I m } z > 0 \}$ . Suppose that $f : H \to H$ is holomorphic, and $f ( 3 + 1 7 i ) = 3 + 1 7 i$ What is the maximum possible value of $f ^ { \prime } ( 3 { + } 1 7 i )$ . Give a reason for your answer (and try not to do any lengthy computations).

6. Find all the poles of the function

$$
f ( z ) = \frac { e ^ { \pi z } } { ( z ^ { 2 } + 1 ) ^ { 2 } } .
$$

Determine the residue of f at each pole.

Part II. Real Analysis. Do 5 out of the following 6 problems.

7. Quickies:

a) Give an example of a function that is in $L ^ { 2 } ( \mathbb { R } )$ but not in $L ^ { 1 } ( \mathbb { R } )$

b) Give an example of a function that is in $L ^ { 1 } ( ( 0 , 1 ) )$ but not in $L ^ { 2 } ( ( 0 , 1 ) )$ .