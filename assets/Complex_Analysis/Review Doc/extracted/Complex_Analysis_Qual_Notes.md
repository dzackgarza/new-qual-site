Complex Analysis Qualifying Exam Review

## Table of Contents

## Contents

Table of Contents 2   
1 General Info / Tips / Techniques 4   
1.1 Greatest Hits 4   
1.2 Common Tricks 4   
1.3 Basic but Useful Facts 5   
1.3.1 Arithmetic 5   
1.3.2 Calculus . 6   
1.4 Series 6   
2 Calculus Preliminaries 9   
2.1 Definitions . 9   
2.2 Theorems 10   
2.3 Convergence 10   
2.4 Integrals . 11   
2.5 Series and Sequences 11   
2.6 Exercises 13   
3 Preliminaries 13   
3.1 Complex Log 13   
3.2 Complex Calculus 15   
3.2.1 Holomorphy and Cauchy-Riemann 16   
3.2.2 Delbar and the Laplacian 19   
3.2.3 Harmonic Functions and the Laplacian 19   
3.2.4 Exercises 20   
3.3 Power Series . 21   
3.3.1 Exercises: Series 25   
4 Cauchy’s Theorem 26   
4.1 Complex Integrals 2727   
4.2 Applications of Cauchy’s Theorem   
4.2.1 Integral Formulas and Estimates 27   
4.2.2 Liouville 30   
4.2.3 Continuation Principle 31   
4.3 Exercises 31   
4.4 Morera’s Theorem 33   
4.4.1 Symmetric Regions 34   
5 Zeros and Singularities 34   
6 Counting Zeros and Poles 38   
6.1 Argument Principle . 38   
6.2 Rouché 39   
6.3 Counting Zeros 41   
7 Residues 41   
7.1 Basics 41   
7.2 Estimates 42   
7.3 Residue Formulas 45   
7.3.1 Exercises 46   
8 Integrals 51   
8.1 Branch Cuts . 53   
9 Conformal Maps / Linear Fractional Transformations 55   
9.1 By Type . 56   
9.2 Exercises 62   
10 Schwarz Reflection 62   
10.1 Schwarz 62   
11 Schwarz Lemma 63   
12 Unsorted Theorems 63   
13 Proofs of the Fundamental Theorem of Algebra 64   
13.0.1 Argument Principle 64   
13.0.2 Rouche’s Theorem 65   
13.0.3 Liouville’s Theorem 66   
13.0.4 Open Mapping Theorem 66   
13.0.5 Generalized Liouville . 67   
14 Appendix 67   
14.1 Misc Basic Algebra 68

A great deal of content borrowed from the following: https: // web. stanford. edu/ \~chriseur/ notes_ pdf/ Eur_ ComplexAnalysis_ Notes. pdf

# 1 General Info / Tips / Techniques

## 1.1 Greatest Hits

<!-- image-->

Things to know well:

• Estimates for derivatives, mean value theorem

• ??CauchyTheorem]Cauchy’s Theorem

• ??CauchyIntegral]Cauchy’s Integral Formula

• ??CauchyInequality]Cauchy’s Inequality

• ??Morera]Morera’s Theorem

• ??Liouville]Liouville’s Theorem

• ??MaximumModulus]Maximum Modulus Principle

• ??Rouche]Rouché’s Theorem

• ??SchwarzReflection]The Schwarz Reflection Principle

• ??SchwarzLemma]The Schwarz Lemma

• ??Casorati]Casorati-Weierstrass Theorem

• Properties of linear fractional transformations

• Automorphisms of D, C, CP1.

<!-- image-->

## 1.2 Common Tricks

• Virtually any time: consider 1/f(z) and f(1/z).

• Setting $w = e ^ { z }$ is useful.

Remark 1.2.1(Showing a function is constant): If you want to show that a function $f$ is constant, try one of the following:

• Write $f = u + i v$ and use Cauchy-Riemann to show $u _ { x } , u _ { y } = 0$ , etc.

• Show that f is entire and bounded.

– If you additionally want to show f is zero, show $\operatorname* { l i m } _ { z \to \infty } f ( z ) = 0 .$

Fact 1.2.2

To show a function is holomorphic,

• Use Morera’s theorem

• Find a primitive (sufficient but not necessary)

Fact 1.2.3

To count zeros:

• Rouche’s theorem

• The argument principle

<!-- image-->

## 1.3 Basic but Useful Facts

## 1.3.1 Arithmetic

Fact 1.3.1 (Some useful facts about basic complex algebra)

$$
z { \bar { z } } = | z | ^ { 2 }
$$

$$
\operatorname { A r g } ( z / w ) = \operatorname { A r g } ( z ) - \operatorname { A r g } ( w )
$$

$$
\Re ( z ) = { \frac { z + { \bar { z } } } { 2 } }
$$

$$
\Im ( z ) = \frac { z - \hat { z } } { 2 i } .
$$

Exponential forms of cosine and sine, where it’s sometimes useful to set $w : = e ^ { i z }$

$$
\cos ( z ) = { \frac { 1 } { 2 } } \left( e ^ { i z } + e ^ { - i z } \right) = { \frac { 1 } { 2 } } ( w + w ^ { - 1 } )
$$

$$
\sin ( z ) = { \frac { 1 } { 2 i } } \left( e ^ { i z } - e ^ { - i z } \right) = { \frac { 1 } { 2 i } } ( w - w ^ { - 1 } ) .
$$

Exponential forms of hyperbolic cosine and sin:

$$
\cosh ( z ) = \cos ( i z ) = \frac { 1 } { 2 } ( e ^ { z } + e ^ { - z } )
$$

$$
\sinh ( z ) = - i \sin ( i z ) = { \frac { 1 } { 2 } } \left( e ^ { z } - e ^ { - z } \right) .
$$

Some other useful facts about the hyperbolic exponentials:

• They are periodic with period 2πi.

$\frac { \partial } { \partial z }$ cosh(z) = sinh(z) and $\frac { \partial } { \partial z } \sinh ( z ) = \cosh ( z ) .$

• sinh is odd and cosh is even.

$\cosh ( z + i \pi ) = - \cosh ( z )$ and sinh(z + iπ) = − sinh(z).

• cosh has zeros at $\left\{ i \pi \left( { \frac { 2 k + 1 } { 2 } } \right) \right\} = \{ i \left( \pi / 2 + k \pi \right) \} , { \mathrm { ~ i . e . ~ } } \cdots , - \pi / 2 , \pi / 2 , 3 \pi / 2 , \cdots ,$ the halfintegers.

• sinh has zeros at {iπk}, i.e. the integers.

Fact 1.3.2

Some computations that come up frequently:

$$
| z \pm w | ^ { 2 } = | z | ^ { 2 } + | w | ^ { z } + 2 \Re ( \overline { { w } } z )
$$

$$
( a + b i ) ( c + d i ) = ( a c - b d ) + ( a d + b c )
$$

$$
{ \frac { 1 } { | a + b | } } \leq { \frac { 1 } { | a | - | b | } }
$$

$$
| e ^ { z } | = e ^ { \Re ( z ) } , \quad \arg ( e ^ { z } ) = \Im ( z ) .
$$

## 1.3.2 Calculus

Fact 1.3.3

Various differentials:

$$
d z = d x + i \ d y
$$

$$
d \bar { z } = d x - i \ d y
$$

$$
f _ { z } = f _ { x } = f _ { y } / i .
$$

Integral of a complex exponential:

$$
\int _ { 0 } ^ { 2 \pi } e ^ { i \ell x } d x = \left\{ \begin{array} { l l } { { 2 \pi } } & { { \ell = 0 } } \\ { { 0 } } & { { \mathrm { e l s e } } } \end{array} \right. .
$$

## 1.4 Series

## Fact 1.4.1 (Generalized Binomial Theorem)

Define $( n ) _ { k }$ to be the falling factorial

$$
\prod _ { j = 0 } ^ { k - 1 } ( n - k ) = n ( n - 1 ) \cdots ( n - k + 1 )
$$

and set ${ \binom { n } { k } } : = { ( n ) } _ { k } / k ! ,$ , then

$$
( x + y ) ^ { n } = \sum _ { k \geq 0 } { \binom { n } { k } } x ^ { k } y ^ { n - k } .
$$

Fact 1.4.2 (Some useful series)

$$
\begin{array} { r l } { \frac { \sqrt { 3 } } { 2 } } & { \frac { \sqrt { 6 } } { 3 } - \frac { \sqrt { 6 } } { 3 } } \\ { \frac { \sqrt { 6 } } { 5 } } & { \frac { \sqrt { 6 } } { 5 } - \frac { \sqrt { 6 } } { 3 } \frac { \sqrt { 5 } } { 2 } } \\ { \frac { \sqrt { 6 } } { 5 } } & { \frac { \sqrt { 6 } } { 5 } - \frac { \sqrt { 6 } } { 3 } \frac { \sqrt { 5 } } { 2 } } \\ { \frac { \sqrt { 6 } } { 5 } } & { \frac { \sqrt { 6 } } { 5 } - \frac { \sqrt { 6 } } { 3 } \frac { \sqrt { 5 } } { 2 } } \\ { \frac { \sqrt { 6 } } { 5 } } & { \frac { \sqrt { 6 } } { 5 } } \\ { \frac { \sqrt { 6 } } { 5 } } & { \frac { \sqrt { 6 } } { 5 } } \\ { \frac { \sqrt { 6 } } { 5 } } & { \frac { \sqrt { 6 } } { 5 } } \\ { \frac { \sqrt { 6 } } { 5 } } & { \frac { \sqrt { 6 } } { 5 } } \\ { \frac { \sqrt { 6 } } { 5 } } & { \frac { \sqrt { 6 } } { 5 } } \\ { \frac { \sqrt { 6 } } { 5 } } & { \frac { \sqrt { 6 } } { 5 } } \\ { \frac { \sqrt { 6 } } { 5 } } & { \frac { \sqrt { 6 } } { 5 } } \end{array}
$$

$$
\begin{array} { r l } & { \qquad \displaystyle \cosh ( z ) = \sum _ { k \geq 0 } \frac { z ^ { 2 k } } { ( 2 k ) ! } } \\ & { \qquad \displaystyle \sinh ( z ) = \sum _ { k \geq 0 } \frac { z ^ { 2 k + 1 } } { ( 2 k + 1 ) ! } } \\ & { \displaystyle \log ( 1 - x ) = \sum _ { k \geq 0 } \frac { z ^ { 2 k } } { ( k ) ! } \ | z | < 1 } \\ & { \displaystyle \partial _ { z } \sum _ { k = 0 } ^ { \infty } \alpha _ { k } z ^ { k } = \sum _ { k + 1 } ^ { \infty } a _ { k + 1 } z ^ { k } } \\ & { \qquad \displaystyle ( 1 + x ) ^ { 1 / 2 } = 1 + ( 1 / 2 ) x + \frac { ( 1 / 2 ) ( - 1 / 2 ) } { 2 ! } x ^ { 2 } + \frac { ( 1 / 2 ) ( - 1 / 2 ) ( - 3 / 2 ) } { 3 ! } x ^ { 3 } + \cdots } \\ & { \qquad \displaystyle = 1 + \frac { 1 } { 2 } x - \frac { 1 } { 8 } x ^ { 2 } + \frac { 1 } { 1 6 } x ^ { 3 } - \cdots . } \end{array}
$$

Fact 1.4.3

Useful trick for expanding square roots:

$$
\begin{array} { r } { \sqrt { z } = \sqrt { z _ { 0 } + z - z _ { 0 } } = \sqrt { z _ { 0 } \left( 1 + \frac { z - z _ { 0 } } { z } \right) } = \sqrt { z _ { 0 } } \sqrt { 1 + u } , \quad u : = \frac { z - z _ { 0 } } { z } } \\ { \implies \sqrt { z } = \sqrt { z _ { 0 } } \sum _ { k \geq 0 } \left( 1 / 2 \right) \left( \frac { z - z _ { 0 } } { z } \right) ^ { k } . } \end{array}
$$

Add series tricks.

## 2 Calculus Preliminaries

## 2.1 Definitions

A sequence of functions $f _ { n }$ is said to converge locally uniformly on $\Omega \subseteq \mathbb { C }$ iff $f _ { n }  f$ uniformly on every compact subset $K \subseteq \Omega$

Definition 2.1.2 (Equicontinuous Family)   
A family of functions $f _ { n }$ is equicontinuous iff for every ε there exists a $\delta = \delta ( \varepsilon )$ (not depending on n or $f _ { n } )$ such that $| x - y | < \varepsilon \implies | f _ { n } ( x ) - f _ { n } ( y ) | < \varepsilon$ for all n.

Remark 2.1.3: Recall Arzelà-Ascoli, an analog of Heine-Borel: for X compact Hausdorff, consider the the Banach space $C ( X ; \mathbb { R } )$ equipped with the uniform norm $\| f \| _ { \infty , X } : = \operatorname* { s u p } _ { x \in X } | f ( x ) |$ Then a subset $A \subseteq X$ is compact iff A is closed, uniformly bounded, and equicontinuous. As a consequence, if A is a sequence, it contains a subsequence converging uniformly to a continuous function. The proof is an $\varepsilon / 3$ argument.

Definition 2.1.4 (Normal Family)

Remark 2.1.5: A continuous function on a compact set is uniformly continuous.

Definition 2.1.6 (Univalent functions)   
A function $f \in { \mathrm { H o l } } ( U ; \mathbb { C } )$ is called univalent if f is injective.

Remark 2.1.7: If $f : \Omega \to \Omega ^ { \prime }$ is a univalent surjection, f is invertible on Ω and $f ^ { - 1 }$ is holomorphic. Compare to real functions: $f ( x ) = x ^ { 3 }$ is injective on $( - c , c )$ for any c but $f ^ { \prime } ( 0 ) = 0$ and $f ^ { - 1 } ( x ) : =$ $x ^ { 1 / 3 }$ is not differentiable at zero.

## 2.2 Theorems

Theorem 2.2.1(Implicit Function Theorem).   
Theorem 2.2.2(Inverse Function Theorem).   
For $f \in C ^ { 1 } ( \mathbb { R } ; \mathbb { R } )$ with $f ^ { \prime } ( a ) \neq 0 .$ then $f$ is invertible in a neighborhood $U \ni a , g : = f ^ { - 1 } \in$   
$C ^ { 1 } ( U ; \mathbb { R } )$ , and at $b : = f ( a )$ the derivative of $g$ is given by   
$g ^ { \prime } ( b ) = { \frac { 1 } { f ^ { \prime } ( a ) } } .$   
For $F \in C ^ { 1 } ( \mathbb { R } ^ { n } , \mathbb { R } ^ { n } )$ with $D _ { f }$ invertible in a neighborhood of $^ { a , }$ so $\operatorname* { d e t } ( J _ { f } ) \neq 0 .$ , then setting   
$b : = F ( a )$   
$J _ { F ^ { - 1 } } ( q ) = ( J _ { F } ( p ) ) ^ { - 1 } .$   
The version for holomorphic functions: if $f \in \operatorname { H o l } ( \mathbb { C } ; \mathbb { C } )$ with $f ^ { \prime } ( p ) \neq 0$ then there is a   
neighborhood $V \ni p$ with that $f \in \operatorname { B i H o l } ( V , f ( V ) )$   
Theorem 2.2.3(Green’s Theorem).   
If $\Omega \subseteq \mathbb { C }$ is bounded with ∂Ω piecewise smooth and $f , g \in C ^ { 1 } ( \overline { { \Omega } } )$ then   
$\int _ { \partial \Omega } f d x + g d y = \iint _ { \Omega } \left( { \frac { \partial g } { \partial x } } - { \frac { \partial f } { \partial y } } \right) d A .$   
In vector form,   
$\int _ { \gamma } F \cdot \ d r = \int \int _ { R } \mathrm { c u r l } F d A .$

## 2.3 Convergence

Remark 2.3.1: Recall that absolutely convergent implies convergent, but not conversely: $\sum k ^ { - 1 } =$ $\infty$ but $\sum ( - 1 ) ^ { k } k ^ { - 1 } < \infty$ This converges because the even (odd) partial sums are monotone increasing/decreasing respectively and in (0, 1), so they converge to a finite number. Their difference converges to 0, and their common limit is the limit of the sum.

Proposition 2.3.2(Uniform Convergence of Series).

A series of functions $\sum _ { n = 1 } ^ { \infty } f _ { n } ( x )$ converges uniformly iff

$$
\operatorname* { l i m } _ { n \to \infty } \left\| \sum _ { k \geq n } f _ { k } \right\| _ { \infty } = 0 .
$$

Theorem 2.3.3(Weierstrass $\mathbf { \Psi } _ { M - \mathbf { \mathit { T e s t } } ) }$

If $\left\{ f _ { n } \right\}$ with $f _ { n } : \Omega \to \mathbb { C }$ and there exists a sequence $\left\{ M _ { n } \right\}$ with $\| f _ { n } \| _ { \infty } \leq M _ { n }$ and $\sum _ { n \in \mathbb { N } } M _ { n } < \infty$ , then $f ( x ) : = \sum _ { n \in \mathbb { N } } f _ { n } ( x )$ converges absolutely and uniformly on Ω. Moreover, if the $f _ { n }$ are continuous, by the uniform limit theorem, $f$ is again continuous.

## 2.4 Integrals

Remark 2.4.1: Some basic facts needed for line integrals in the plane:

• grad $f = \left[ { \frac { \partial f } { \partial x } } , { \frac { \partial f } { \partial y } } \right]$

$\operatorname { I f } F = \operatorname { g r a d } f$ for some f, F is a vector field.

• Given $f ( x , y )$ and $\gamma ( t )$ , the chain rule yields $\frac { \partial } { \partial t } \left( f \circ \gamma \right) ( t ) = \langle \operatorname { g r a d } f \circ \gamma ) ( t ) , \ \gamma ^ { \prime } ( t ) \rangle$

• For $F ( x , y ) = [ M ( x , y ) , N ( x , y ) ]$ , curl $F = \frac { \partial \check { N } } { \partial x } - \frac { \partial M } { \partial y }$ and Div $F = { \frac { \partial M } { \partial x } } + { \frac { \partial N } { \partial y } }$

$\int _ { \gamma } F \cdot d r = \int _ { a } ^ { b } F ( \gamma ( t ) ) \cdot \gamma ^ { \prime } ( t ) d t .$

## 2.5 Series and Sequences

Remark 2.5.1: Note that if a power series converges uniformly, then summing commutes with integrating or differentiating.

Proposition 2.5.2(Ratio Test).

Consider $\sum c _ { k } z ^ { k }$ , set $R = \operatorname* { l i m } \left| { \frac { c _ { k + 1 } } { c _ { k } } } \right|$ , and recall the ratio test:

$R \in ( 0 , 1 ) \implies \mathrm { c o n v e r g e n c e } .$

$R \in ( 1 , \infty ] \implies \mathrm { d i v e r g e n c e } .$

$R = 1$ yields no information.

Theorem 2.2 (Root Test). Suppose $\sum a _ { n } ( z - z _ { 0 } ) ^ { n }$ is a formal power series. Let

$$
R = \operatorname* { l i m } _ { n \to \infty } | \operatorname* { m i n f } _ { \mathbf { \theta } _ { n } \to \infty } - { \frac { 1 } { \operatorname* { l i m } _ { n \to \infty } | a _ { n } | ^ { \frac { 1 } { n } } } } \in [ 0 , + \infty ] .
$$

Then $\scriptstyle \sum _ { n = 0 } ^ { \infty } a _ { n } ( z - z _ { 0 } ) ^ { n }$

(a) converges absolutely in $\{ z : | z - z _ { 0 } | < R \}$ ,

(b) converges uniformly in $\{ z : | z - z _ { 0 } | \leq r \}$ for all $r < R ,$ and

(c) diverges in $\{ z : | z - z _ { 0 } | > R \}$

Figure 1: image_2021-05-27-15-40-58

Proposition 2.5.3(Root Test).

Proposition 2.5.4(Radius of Convergence by the Root Test). For ${ \overline { { f } } } ( z ) = \sum _ { k \in \mathbb { N } } c _ { k } z ^ { k } ,$ , defining

$$
{ \frac { 1 } { R } } : = \operatorname* { l i m } _ { k } \operatorname* { s u p } | a _ { k } | ^ { \frac { 1 } { k } } ,
$$

then $f$ converges absolutely and uniformly for $D _ { R } : = | z | < R$ and diverges for $| z | > R .$ Moreover f is holomorphic in $D _ { R }$ , can be differentiated term-by-term, and ${ \check { f } } ^ { \prime } = \sum _ { k \in \mathbb { N } } { \overset { \cdot } { n } } c _ { k } z ^ { k } .$

## Fact 2.5.5

Recall the p-test:

$$
\sum n ^ { - p } < \infty \Longleftrightarrow p \in ( 1 , \infty ) .
$$

## Fact 2.5.6

The product of two sequences is given by the Cauchy product

$$
\sum a _ { k } z ^ { k } \cdot et { } { ' } \sum b _ { k } z ^ { k } = \sum c _ { k } z ^ { k } , \quad c _ { k } : = \sum _ { j \leq k } a _ { k } b _ { k - j } .
$$

## Fact 2.5.7

Recall how to carry out polynomial long division:

Polynomial long division

## Fact 2.5.8 (Partial Fraction Decomposition)

• For every root $r _ { i }$ of multiplicity 1, include a term $A / ( x - r _ { i } )$

• For any factors $g ( x )$ of multiplicity k, include terms $\dot { A } _ { 1 } / g ( x ) , A _ { 2 } / g ( x ) ^ { 2 } , \cdot \cdot \cdot , A _ { k } / g ( x ) ^ { k }$

• For irreducible quadratic factors $h _ { i } ( x )$ , include terms of the form $\frac { A x + B } { h _ { i } ( x ) }$

## 2.6 Exercises

Exercise 2.6.1 (?)

Find the radius of convergences for the power series expansion of $\sqrt { z }$ about $z _ { 0 } = 4 + 3 i .$

## 3 Preliminaries

## Definition 3.0.1 (Toy contour)

A closed Jordan curve that separates C into an exterior and interior region is referred to as a toy contour.

## Fact 3.0.2 (Complex roots of a number)

The complex nth roots of $z : = r e ^ { i \theta }$ are given by

$$
\left\{ \omega _ { k } : = r ^ { 1 / n } e ^ { i \left( \frac { \theta + 2 k \pi } { n } \right) } \ \Big | \ 0 \leq k \leq n - 1 \right\} .
$$

Note that one root is $r ^ { 1 / n } \in \mathbb { R }$ , and the rest are separated by angles of $2 \pi / n$ . Mnemonic:

$$
z = r e ^ { i \theta } = r e ^ { i ( \theta + 2 k \pi ) } \implies z ^ { 1 / n } = \cdot \cdot \cdot .
$$

## 3.1 Complex Log

Fact 3.1.1 (Complex Log)

For $z = r e ^ { i \theta } \neq 0 , \theta$ is of the form $\Theta +$ 2kπ where $\Theta = \operatorname { A r g } z$ We define

$$
\log ( z ) = \ln \left( | z | \right) + i \operatorname { A r g } ( z )
$$

and $z ^ { c } : = e ^ { c \log ( z ) }$ . Thus

$$
\log ( r e ^ { i \theta } ) = \ln | r | + i \theta .
$$

Fact 3.1.2

Common trick:

$$
f ^ { 1 / n } = e ^ { { \frac { 1 } { n } } \log ( f ) } ,
$$

taking (say) a principal branch of log given by $\mathbb { C } \setminus \left( - \infty , 0 \right] \times 0$

## Proposition 3.1.3(Existence of complex log).

Suppose Ω is a simply-connected region such that $1 \in \Omega , 0 \not \in \Omega$ . Then there exists a branch of $F ( z ) : = \log ( z )$ such that

$F$ is holomorphic on $\Omega ,$

$e ^ { F ( z ) } = z { \mathrm { ~ f o r ~ a l l ~ } } z \in \Omega$

$F ( x ) = \log ( x )$ for $x \in \mathbb { R }$ in a neighborhood of 1.

## Definition 3.1.4 (Principal branch and exponential)

Take C and delete $\dot { \mathbb R } ^ { \le 0 }$ to obtain the principal branch of the logarithm. Equivalently, this is define for all $z = r e ^ { i \theta }$ where $\theta \in ( - \pi , \pi )$

Here the log is defined as

$$
\operatorname { L o g } ( z ) : = \log ( r ) + i \theta
$$

$$
| \theta | < \pi .
$$

Similarly define

$$
z ^ { \alpha } : = e ^ { \alpha \log ( z ) } .
$$

4! Warning 3.1.5

It’s tempting to define

$$
z ^ { \frac { 1 } { n } } : = ( r e ^ { i \theta } ) ^ { \frac { 1 } { n } } = r ^ { { \frac { 1 } { n } } } e ^ { \frac { i \theta } { n } } ,
$$

but this requires a branch cut to ensure continuity.

Remark 3.1.6: Note the problem: for $z : = x + i 0 \in \mathbb { R } ^ { \leq 0 }$ , just above the axis consider $z _ { + } : = x + i \varepsilon$ and $z _ { - } : = x - i \varepsilon$ . Then

$\log ( z _ { + } ) = \log | x | + i \pi ,$ and

$\log ( z _ { - } ) = \log | x | - i \pi .$

So log can’t even be made continuous if one crosses the branch. The issue is the branch point or branch singularity at $z = 0$ •

Theorem 3.1.7(Existence of log of a function).

If f is holomorphic and nonvanishing on a simply-connected region Ω, then there exists a holomorphic G on Ω such that

$$
f ( z ) = e ^ { G ( z ) } .
$$

## 3.2 Complex Calculus

Remark 3.2.1: When parameterizing integrals $\int _ { \gamma } f ( z ) d z$ , parameterize $\gamma$ by θ and write $z = r e ^ { i \theta }$ so $d z = i r e ^ { i \theta } d \theta .$

4! Warning 3.2.2

$f ( z ) = \sin ( z ) , \cos ( z )$ are unbounded on C! An easy way to see this: they are nonconstant and entire, thus unbounded by Liouville.

Example 3.2.3(?): You can show $f ( z ) = { \sqrt { z } }$ is not holomorphic by showing its integral over $S ^ { 1 }$ is nonzero. This is a direct computation:

$$
\begin{array} { l l l } { { \displaystyle \int _ { S ^ { 1 } } z ^ { 1 / 2 } d z = \int _ { 0 } ^ { 2 \pi } ( c ^ { i \theta } ) ^ { 1 / 2 } i c ^ { i \theta } d \theta } } \\ { { \displaystyle \qquad = i \int _ { 0 } ^ { 2 \pi } e ^ { \frac { i 3 \theta } { 2 } } d \theta } } \\ { { \displaystyle \qquad = i \left( \frac { 2 } { 3 i } \right) e ^ { \frac { i 3 \theta } { 2 } } \Big \vert _ { 0 } ^ { \pi } } } \\ { { \displaystyle \qquad = \frac { 2 } { 3 } \left( e ^ { 3 \pi i - 1 } \right) } } \\ { { \displaystyle \qquad = - \frac { 4 } { 3 } . } } \end{array}
$$

Note an issue: a different parameterization yields a different (still nonzero) number

$$
{ \begin{array} { r l } & { \cdots = \displaystyle \int _ { - \pi } ^ { \pi } ( e ^ { i \theta } ) ^ { 1 / 2 } i e ^ { i \theta } d \theta } \\ & { \quad = \displaystyle { \frac { 2 } { 3 } } \left( e ^ { \frac { 3 \pi i } { 2 } } - e ^ { \frac { - 3 \pi i } { 2 } } \right) } \\ & { \quad = \displaystyle - { \frac { 4 i } { 3 } } . } \end{array} }
$$

This is these are paths that don’t lift to closed loops on the Riemann surface defined by $z \mapsto z ^ { 2 }$

## 3.2.1 Holomorphy and Cauchy-Riemann

## Definition 3.2.4 (Analytic)

A function $f : \Omega \to \mathbb { C }$ is analytic at $z _ { 0 } \in \Omega$ iff there exists a power series $g ( z ) = \sum a _ { n } ( z - z _ { 0 } ) ^ { n }$ with radius of convergence $R > 0$ and a neighborhood $U \ni z _ { 0 }$ such that $f ( z ) = g ( z )$ on U .

Definition 3.2.5 (Complex differentiable / holomorphic /entire)   
A function $f : \mathbb { C } \to \mathbb { C }$ is complex differentiable or holomorphic at $z _ { \mathrm { 0 } }$ iff the following limit   
exists:   
lim f (z0 + h) − f (h) .   
h → 0 h   
A function that is holomorphic on C is said to be entire.   
Equivalently, there exists an $\alpha \in \mathbb { C }$ such that   
f (z0 + h) − f (z0) = αh + R(h) R(h) h→0−→ 0.   
In this case, $\alpha = f ^ { \prime } ( z _ { 0 } )$

Example 3.2.6(Holomorphic vs non-holomorphic):

$f ( z ) : = | z |$ is not holomorphic.

$f ( z ) : = \arg z$ is not holomorphic.

$f ( z ) : = \Re z$ is not holomorphic.

$f ( z ) : = \mathfrak { T } z$ is not holomorphic.

$f ( z ) = { \frac { 1 } { z } }$ is holomorphic on $\mathbb { C } \setminus \{ 0 \}$ but not holomorphic on C

$\begin{array} { r } { f ( z ) = \tilde { { z } } } \end{array}$ is not holomorphic, but is real differentiable:

$$
{ \frac { f ( z _ { 0 } + h ) - f ( z _ { 0 } ) } { h } } = { \frac { { \overline { { z _ { 0 } } } } + { \bar { h } } - { \overline { { z _ { 0 } } } } } { h } } = { \frac { \bar { h } } { h } } = { \frac { r e ^ { - i \theta } } { r e ^ { i \theta } } } = e ^ { - 2 i \theta } \ { \xrightarrow { h \to 0 } } \ e ^ { - 2 i \theta } ,
$$

which is a complex number that depends on θ and is thus not a single value.

A function $F : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is real-differentiable at p iff there exists a linear transformation A such that

$$
{ \frac { \left\| F ( \mathbf { p } + \mathbf { h } ) - F ( \mathbf { p } ) - A ( \mathbf { h } ) \right\| } { \left\| \mathbf { h } \right\| } } \ { \stackrel { \| \mathbf { h } \| \to 0 } { \longrightarrow } } \ 0 .
$$

Rewriting,

$$
\| F ( \mathbf { p } + \mathbf { h } ) - F ( \mathbf { p } ) - A ( \mathbf { h } ) \| = \| \mathbf { h } \| \| R ( \mathbf { h } ) \|
$$

$$
\| R ( \mathbf { h } ) \| \stackrel { \| \mathbf { h } \|  0 } { \longrightarrow } 0 .
$$

Equivalently,

$$
F ( \mathbf { p } + \mathbf { h } ) - F ( \mathbf { p } ) = A ( \mathbf { h } ) + \| \mathbf { h } \| R ( \mathbf { h } )
$$

$$
\| R ( \mathbf { h } ) \| \stackrel { \| \mathbf { h } \| \to 0 } { \longrightarrow } 0 .
$$

Or in a slightly more useful form,

$$
F ( \mathbf { p } + \mathbf { h } ) = F ( \mathbf { p } ) + A ( \mathbf { h } ) + R ( \mathbf { h } )
$$

$$
R \in o ( \| \mathbf { h } \| ) , { \mathrm { ~ i . e . ~ } } { \frac { \| R ( \mathbf { h } ) \| } { \| \mathbf { h } \| } } { \stackrel { \mathbf { h } \to 0 } { \longrightarrow } } 0 .
$$

## Proposition 3.2.8(Complex differentiable implies Cauchy-Riemann).

If f is differentiable at $z _ { 0 } .$ , then the limit defining $f ^ { \prime } ( z _ { 0 } )$ must exist when approaching from any direction. Identify $f ( z ) = f ( x , y )$ and write $z _ { 0 } = x + i y .$ , then first consider $h \in R R ,$ so $h = h _ { 1 } + i h _ { 2 }$ with $h _ { 2 } = 0$ . Then

$$
f ^ { \prime } ( z _ { 0 } ) = \operatorname* { l i m } _ { h _ { 1 } \to 0 } \frac { f ( x + h _ { 1 } , y ) - f ( x , y ) } { h _ { 1 } } : = \frac { \partial f } { \partial x } ( x , y ) .
$$

Taking $h \in i \mathbb { R }$ purely imaginary, so $h = i h _ { 2 }$

$$
f ^ { \prime } ( z _ { 0 } ) = \operatorname* { l i m } _ { i h _ { 2 } \to 0 } \frac { f ( x , y + h _ { 2 } ) - f ( x , y ) } { i h _ { 2 } } : = \frac { 1 } { i } \frac { \partial f } { \partial y } ( x , y ) .
$$

Equating,

$$
{ \frac { \partial f } { \partial x } } = { \frac { 1 } { i } } { \frac { \partial f } { \partial y } } ,
$$

and writing $f = u + i v$ and $1 / i = - i$ yields

$$
{ \frac { \partial f } { \partial x } } = { \frac { \partial u } { \partial x } } + i { \frac { \partial v } { \partial x } }
$$

$$
{ \frac { 1 } { i } } { \frac { \partial f } { \partial y } } = { \frac { 1 } { i } } \left( { \frac { \partial u } { \partial y } } + i { \frac { \partial v } { \partial y } } \right) = { \frac { \partial v } { \partial y } } - i { \frac { \partial u } { \partial y } } .
$$

Thus

$$
{ \frac { \partial u } { \partial x } } = { \frac { \partial v } { \partial y } }
$$

$$
\frac { \partial u } { \partial y } = - \frac { \partial v } { \partial x } .
$$

Proposition 3.2.9(Polar Cauchy-Riemann equations).

$$
{ \frac { \partial u } { \partial r } } = { \frac { 1 } { r } } { \frac { \partial v } { \partial \theta } }
$$

and

$$
{ \frac { 1 } { r } } { \frac { \partial u } { \partial \theta } } = - { \frac { \partial v } { \partial r } } .
$$

Proof .

Setting

$$
z = r e ^ { i \theta } = r ( \cos ( \theta ) + i \sin ( \theta ) ) = x + i y
$$

yields $x = r \cos ( \theta ) , y = r$ sin(θ), one can identify

$$
x _ { r } = \cos ( \theta ) , x _ { \theta } = - r \sin ( \theta )
$$

$$
y _ { r } = \sin ( \theta ) , y _ { \theta } = r \cos ( \theta ) .
$$

Now apply the chain rule:

$$
\begin{array} { r l } & { u _ { r } = u _ { x } x _ { r } + u _ { y } y _ { r } } \\ & { \quad = v _ { y } x _ { r } - v _ { x } y _ { r } } \\ & { \quad = v _ { y } \cos ( \theta ) - v _ { x } \sin ( \theta ) } \\ & { \quad = \frac { 1 } { r } \left( v _ { y } r \cos ( \theta ) - v _ { x } r \sin ( \theta ) \right) } \\ & { \quad = \frac { 1 } { r } \left( v _ { y } y _ { \theta } + v _ { x } x _ { \theta } \right) } \\ & { \quad = \frac { 1 } { r } v _ { \theta } . } \end{array}\tag{CR}
$$

Similarly,

$$
\begin{array} { r l } & { v _ { r } = v _ { x } x _ { r } + v _ { y } y _ { r } } \\ & { \quad = v _ { x } \cos ( \theta ) + v _ { y } \sin ( \theta ) } \\ & { \quad = - u _ { y } \cos ( \theta ) + u _ { x } \sin ( \theta ) } \\ & { \quad = \frac { 1 } { r } \left( - u _ { y } r \cos ( \theta ) + u _ { x } r \sin ( \theta ) \right) } \\ & { \quad = \frac { 1 } { r } \left( - u _ { y } y _ { \theta } - u _ { x } x _ { 0 } \right) } \\ & { \quad = - \frac { 1 } { \tau } u _ { \theta } . } \end{array}\tag{CR}
$$

Thus

$$
{ \frac { \partial u } { \partial r } } = { \frac { 1 } { r } } { \frac { \partial v } { \partial \theta } } \quad { \mathrm { ~ a n d ~ } } \quad { \frac { \partial v } { \partial r } } = - { \frac { 1 } { r } } { \frac { \partial u } { \partial \theta } }
$$

## Proposition 3.2.10(Holomorphic functions are continuous.).

f is holomorphic at z0 iff there exists an $a \in \mathbb { C }$ such that

$$
f ( z _ { 0 } + h ) - f ( z _ { 0 } ) - a h = h \psi ( h ) , \quad \psi ( h ) \stackrel { h \to 0 } {  } 0 .
$$

In this case, $a = f ^ { \prime } ( z _ { 0 } )$

## 3.2.2 Delbar and the Laplacian

Definition 3.2.11 (del and delbar operators)

$$
\partial : = \partial _ { z } : = \frac 1 2 \left( \partial _ { x } - i \partial _ { y } \right) \mathrm { a n d } \bar { \partial } : = \partial _ { \bar { z } } = \frac 1 2 \left( \partial _ { x } + i \partial _ { y } \right) .
$$

Moreover, $f ^ { \prime } = \partial f + \bar { \partial } f .$

Proposition 3.2.12(Holomorphic $_ { i f f }$ delbar vanishes).

$$
\bar { \partial } f ( z _ { 0 } ) = 0 :
$$

$$
\begin{array} { r l } & { 2 \hat { \partial } f : = ( \partial _ { x } + i \partial _ { y } ) ( u + i v ) } \\ & { \quad \quad = u _ { x } + i v _ { x } + i u _ { y } - v _ { y } } \\ & { \quad \quad = ( u _ { x } - v _ { y } ) + i ( u _ { y } + v _ { x } ) } \\ & { \quad \quad = 0 } \end{array}
$$

by Cauchy-Riemann.

## 3.2.3 Harmonic Functions and the Laplacian

Definition 3.2.13 (Laplacian and Harmonic Functions)

A real function of two variables $u ( x , y )$ is harmonic iff it is in the kernel of the Laplacian operator:

$$
\Delta u : = \left( { \frac { \partial ^ { 2 } } { \partial x ^ { 2 } } } + { \frac { \partial ^ { 2 } } { \partial y ^ { 2 } } } \right) u = 0 .
$$

Proposition 3.2.14(Cauchy-Riemann implies holomorphic).

If $f = u +$ iv with $u , v \in C ^ { 1 } ( \mathbb { R } )$ satisfying the Cauchy-Riemann equations on $\Omega _ { ; }$ then $f$ is holomorphic on Ω and

$$
f ^ { \prime } ( z ) = \partial f = { \frac { 1 } { 2 } } \left( u _ { x } + i v _ { x } \right) .
$$

Proposition 3.2.15(Holomorphic functions have harmonic components).   
$\mathrm { I f } \ f ( z ) = u ( x , y ) + i v ( x , y )$ is holomorphic, then $u ,$ v are harmonic.

Proof (?).

• By CR,

$$
u _ { x } = v _ { y }
$$

$$
u _ { y } = - v _ { x } .
$$

• Differentiate with respect to x:

$$
u _ { x x } = v _ { y x }
$$

$$
u _ { y x } = - v _ { x x } .
$$

• Differentiate with respect to y:

$$
u _ { x y } = v _ { y y }
$$

$$
u _ { y y } = - v _ { x y } .
$$

• Clairaut’s theorem: partials are equal, so

$$
u _ { x x } - v _ { y x } = 0 \implies u _ { x x } + u _ { y y } = 0
$$

$$
v _ { x x } + u _ { y x } = 0 \implies v _ { x x } + v _ { y y } = 0
$$

## 3.2.4 Exercises

Proposition 3.2.16(Injectivity Relates to Derivatives). If z0 is a zero of $f ^ { \prime }$ of order n, then f is (n + 1)-to-one in a neighborhood of $z _ { 0 } .$

Proof .   
?

Exercise 3.2.17 (Zero derivative implies constant) Show that if $f ^ { \prime } = 0$ on a domain Ω, then f is constant on Ω

## Solution:

Write $f = u + i v$ , then $0 = 2 f ^ { \prime } = u _ { x } + i v _ { x } = u _ { y } - i u _ { y }$ , so grad u = grad v = 0. Show f is constant along every straight line segment L by computing the directional derivative grad $u \cdot \mathbf { v } = 0$ along L connecting $p , q .$ . Then $u ( p ) = u ( q ) = a$ some constant, and $v ( p ) = v ( q ) = b ,$ so $f ( z ) = a + b i$ everywhere.

Exercise 3.2.18 (f and fbar holomorphic implies constant) Show that if $f$ and $\bar { \boldsymbol { f } }$ are both holomorphic on a domain Ω, then $f$ is constant on Ω.

## Solution:

• Strategy: show $f ^ { \prime } = 0$

• Write $f = u + i v$ . Since f is analytic, it satisfies CR, so

$$
u _ { x } = v _ { y }
$$

$$
u _ { y } = - v _ { x } .
$$

• Similarly write ${ \overline { { f } } } = U + i V$ where $U = u$ and $V = - v$ . Since $\bar { \boldsymbol { f } }$ is analytic, it also satisfies CR , so

$$
U _ { x } = V _ { y }
$$

$$
U _ { y } = - V _ { x }
$$

$$
\implies u _ { x } = - v _ { y }
$$

$$
u _ { y } = v _ { x } .
$$

• Add the LHS of these two equations to get $2 u _ { x } = 0 \implies u _ { x } = 0$ . Subtract the right-hand side to get $- 2 v _ { x } = 0 \implies v _ { x } = 0$

• Since f is analytic, it is holomorphic, so $f ^ { \prime }$ exists and satisfies $f ^ { \prime } = u _ { x } + i v _ { x }$ . But by above, this is zero.

• By the previous exercise, $f ^ { \prime } = 0 \implies$ f is constant.

Exercise 3.2.19 (SS 1.13: Constant real/imaginary/magnitude implies constant) If f is holomorphic on Ω and any of the following hold, then f is constant:

1. $\Re ( f )$ is constant.

2. $\Im ( f )$ is constant.

3. $| f |$ is constant.

## Solution:

Part 3:

• Write $| f | = c \in \mathbb { R } .$

• If $c = 0$ , done, so suppose $c > 0 .$

• Use $f \overline { { f } } = \left| f \right| ^ { 2 } = c ^ { 2 }$ to write ${ \overline { { f } } } = c ^ { 2 } / f .$

• Since $| f ( z ) | = 0 \iff f ( z ) = 0$ , we have $f \neq 0$ on Ω, so $\bar { \boldsymbol { f } }$ is analytic.

• Similarly f is analytic, and $f , { \bar { f } }$ analytic implies $f ^ { \prime } = 0$ implies $f$ is constant.

Finish

## 3.3 Power Series

## Theorem 3.3.1(Improved Taylor’s Theorem).

If f is holomorphic on a region Ω with $\overline { { D _ { R } ( z _ { 0 } ) } } \subseteq \Omega$ , and for every $z \in D _ { r } ( z _ { 0 } )$ , f has a power series expansion of the following form:

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } \left( z - z _ { 0 } \right) ^ { n } \quad { \mathrm { ~ w h e r e ~ } } a _ { n } = { \frac { f ^ { ( n ) } \left( z _ { 0 } \right) } { n ! } } = { \frac { 1 } { 2 \pi r ^ { n } } } \int _ { 0 } ^ { 2 \pi } f ( z _ { 0 } + r e ^ { i \theta } ) e ^ { - i n \theta } d \theta .
$$

## Proposition 3.3.2(Power Series are Smooth).

Any power series is smooth (and thus holomorphic) on its disc of convergence, and its derivatives can be obtained using term-by-term differentiation:

$$
{ \frac { \partial } { \partial z } } f ( z ) = { \frac { \partial } { \partial z } } \sum _ { k \geq 0 } c _ { k } ( z - z _ { 0 } ) ^ { k } = \sum _ { k \geq 1 } k c _ { k } ( z - z _ { 0 } ) ^ { k } .
$$

Moreover, the coefficients are given by

$$
c _ { k } = \frac { f ^ { ( n ) } ( z _ { 0 } ) } { n ! } .
$$

Remark 3.3.3: By an application of the Cauchy integral formula (see S&S 7.1) if f is holomorphic on $D _ { R } ( z _ { 0 } )$ there is a formula for all $k \geq 0$ and all $0 < r < R :$

$$
c _ { k } = \frac { 1 } { 2 \pi r ^ { k } } \int _ { 0 } ^ { 2 \pi } f ( z _ { 0 } + r e ^ { i \theta } ) e ^ { - i n \theta } d \theta .
$$

Proposition 3.3.4(Exponential is uniformly convergent in discs).   
$f ( z ) = e ^ { z }$ is uniformly convergent in any disc in C.

Proof .

Apply the estimate

$$
\displaystyle | e ^ { z } | \leq \sum { \frac { | z | ^ { n } } { n ! } } = e ^ { | z | } .
$$

Now by the M -test,

$$
\begin{array} { r } { | z | \leq R < \infty \implies \left| \sum \frac { z ^ { n } } { n ! } \right| \leq e ^ { R } < \infty . } \end{array}
$$

## Lemma 3.3.5(Dirichlet’s Test).

Given two sequences of real numbers $\left\{ a _ { k } \right\} , \left\{ b _ { k } \right\}$ which satisfy

1. The sequence of partial sums $\left\{ A _ { n } \right\}$ is bounded,

2. $b _ { k } \ \searrow 0 .$

then

$$
\sum _ { k \geq 1 } a _ { k } b _ { k } < \infty .
$$

Proof (?).

Use summation by parts. For a fixed $\sum a _ { k } b _ { k }$ , write

$$
\sum _ { n = 1 } ^ { m } x _ { n } Y _ { n } + \sum _ { n = 1 } ^ { m } X _ { n } y _ { n + 1 } = X _ { m } Y _ { m + 1 } .
$$

Set $x _ { n } : = a _ { n } , y _ { N } : = b _ { n } - b _ { n - 1 } , \mathrm { s o } X _ { n } = A _ { n } { \mathrm { ~ a n d ~ } } Y _ { n } = b _ { n }$ as a telescoping sum. Importantly, all $y _ { n }$ are negative, so $| y _ { n } | = | b _ { n } - b _ { n - 1 } | = b _ { n - 1 } - b _ { n }$ and moreover $a _ { n } b _ { n } = x _ { n } Y _ { n }$ for all n. We have

$$
\begin{array} { l } { { \displaystyle \sum _ { n \geq 1 } a _ { n } b _ { n } = \operatorname* { l i m } _ { N \to \infty } \sum _ { n \leq N } x _ { n } Y _ { n } } } \\ { { \displaystyle \quad = \operatorname* { l i m } _ { N \to \infty } \sum _ { n \leq N } X _ { N } Y _ { N } - \sum _ { n \leq N } X _ { n } y _ { n + 1 } } } \\ { { \displaystyle \quad = - \sum _ { n \geq 1 } X _ { n } y _ { n + 1 } } , } \end{array}
$$

where in the last step we’ve used that

$$
| X _ { N } | = | A _ { N } | \leq M \implies | X _ { N } Y _ { N } | = | X _ { N } | | b _ { n + 1 } | \leq M b _ { n + 1 } \to 0 .
$$

So it suffices to bound the latter sum:

$$
\begin{array} { r l r } {  { \sum _ { k \geq n }  X _ { k } y _ { k + 1 }  \leq { \cal M } \sum _ { k \geq 1 }  y _ { k + 1 }  } } \\ & { } & \\ & { } & { \leq { \cal M } \sum _ { k \geq 1 } b _ { k } - b _ { k + 1 } } \\ & { } & \\ & { } & { \leq 2 { \cal M } ( b _ { 1 } - b _ { n + 1 } ) } \\ & { } & { \leq 2 { \cal M } b _ { 1 } . } \end{array}
$$

## Theorem 3.3.6(Abel’s Theorem).

If $\sum _ { k = 1 } ^ { \infty } c _ { k } z ^ { j }$ converges on $| z | < 1$ then

$$
\operatorname* { l i m } _ { z  1 ^ { - } } \sum _ { k \in \mathbb { N } } c _ { k } z ^ { k } = \sum _ { k \in \mathbb { N } } c _ { k } .
$$

Lemma 3.3.7(Abel’s Test).

If $f ( z ) : = \sum c _ { k } { z } ^ { k }$ is a power series with $c _ { k } \in \mathbb { R } ^ { \ge 0 }$ and $c _ { k } \searrow 0$ , then f converges on $S ^ { 1 }$ except possibly at $z = 1$

Example 3.3.8(application of Abel’s theorem): What is the value of the alternating harmonic series? Integrate a geometric series to obtain

$$
\sum { \frac { ( - 1 ) ^ { k } z ^ { k } } { n } } = \log ( z + 1 )
$$

$$
| z | < 1 .
$$

Since $c _ { k } : = ( - 1 ) ^ { k } / k \searrow 0$ , this converges at $z = 1$ , and by Abel’s theorem $f ( 1 ) = \log ( 2 )$

Remark 3.3.9: The converse to Abel’s theorem is false: take $f ( z ) = \sum ( - z ) ^ { n } = 1 / ( 1 + z )$ . Then $f ( 1 ) = 1 - 1 + 1 - \cdot \cdot$ · diverges at 1, but $1 / 1 + 1 = 1 / 2$ . So the limit $s : = \operatorname* { l i m } _ { x  1 ^ { - } } f ( x ) 1 / 2$ , but $\sum a _ { n }$ doesn’t converge to s.

Proposition 3.3.10(Summation by Parts).

Setting $A _ { n } : = \sum _ { k = 1 } ^ { n } b _ { k }$ and $B _ { 0 } : = 0 .$

$$
\sum _ { k = m } ^ { n } a _ { k } b _ { k } = A _ { n } b _ { n } - A _ { m - 1 } b _ { m } - \sum _ { k = m } ^ { n - 1 } A _ { k } ( b _ { k + 1 } - b _ { k } ) .
$$

Compare this to integrating by parts:

$$
\int _ { a } ^ { b } f g = F ( b ) g ( b ) - F ( a ) g ( a ) - \int _ { a } ^ { b } F g ^ { \prime } .
$$

Note there is a useful form for taking the product of sums:

$$
A _ { n } B _ { n } = \sum _ { k = 1 } ^ { n } A _ { k } b _ { k } + \sum _ { k = 1 } ^ { n } a _ { k } B _ { k - 1 } .
$$

Proof (?).

An inelegant proof: define $A _ { n } : = \sum _ { k \leq n } a _ { k }$ , use that $a _ { k } = A _ { k } - A _ { k - 1 }$ , reindex, and peel a top/bottom term off of each sum to pattern-match.

Behold:

$$
\begin{array} { r l } { \underset { m \leq k \leq n } { \sum } ~ a _ { k } b _ { k } = } & { \underset { m \leq k \leq n } { \sum } ~ ( A _ { k } - A _ { k } ) ~ | b _ { k } ~ } \\ & { = ~ \underset { m \leq k \leq n } { \sum } ~ A _ { k } b _ { k } - \underset { m \leq k \leq n - 1 } { \sum } ~ A _ { k } ~ 1 \bar { h } _ { k } ~ } \\ & { = ~ \underset { m \leq k \leq n } { \sum } ~ A _ { k } b _ { k } - \underset { m \leq k \leq n - 1 } { \sum } ~ A _ { k } ~ B _ { k + 1 } ~ } \\ & { = ~ \underset { m \leq k \leq n - 1 } { \sum } ~ A _ { k } b _ { k } - \underset { m \leq k \leq n - 1 } { \sum } ~ A _ { k } b _ { k + 1 } ~ } \\ & { = ~ A _ { k } b _ { k } - \underset { m \leq k \leq n - 1 } { \sum } ~ A _ { k } b _ { k } - \underset { m \leq k \leq n - 1 } { \sum } ~ A _ { k } b _ { k } + 1 ~ } \\ & { = ~ A _ { k } b _ { k } - A _ { m - 1 } ~ \underset { m \leq k \leq n - 1 } { \sum } ~ A _ { k } b _ { k } - \underset { m \leq k \leq n - 1 } { \sum } ~ A _ { k } \bar { h } _ { k + 1 } ~ } \\ & { = ~ A _ { k } b _ { k } - A _ { m - 1 } ~ \underset { m \leq k \leq n - 1 } { \sum } ~ A _ { k } ( b _ { k } - \bar { b } _ { k + 1 } ) ~ } \\ & { = ~ A _ { k } b _ { k } - A _ { m - 1 } b _ { k } + \underset { m \leq k \leq n - 1 } { \sum } ~ A _ { k } ( b _ { k } - \bar { b } _ { k + 1 } ) ~ } \\ & { = ~ A _ { k } b _ { k } - A _ { m - 1 } b _ { k } - \underset { m \leq k \leq n - 1 } { \sum } ~ A _ { k } ( b _ { k } + 1 - b _ { k } ) . } \end{array}
$$

Proposition 3.3.11(?).   
If f is non-constant, then $f ^ { \prime }$ is analytic and the zeros of $f ^ { \prime }$ are isolated. If $f , g$ are analytic   
with $f ^ { \prime } = g ^ { \prime }$ , then $f - g$ is constant.

## 3.3.1 Exercises: Series

Exercise 3.3.12 (Application of summation by parts)   
Use summation by parts to show that sin $( n ) / n$ converges.   
Exercise 3.3.13 (1.20: Series convergence on the circle)   
Show that   
1. $\sum k z ^ { k }$ diverges on $S ^ { 1 }$   
2. $\overline { { \sum } } k ^ { - 2 } z ^ { k }$ converges on $S ^ { 1 }$   
3. $\overline { { \sum } } k ^ { - 1 } z ^ { k }$ converges on $S ^ { 1 } \setminus \{ 1 \}$ and diverges at 1.

Solution: 1. Use that $\left| z ^ { k } \right| = 1$ and $\sum c _ { k } z ^ { k } < \infty \implies \vert c _ { k } \vert  0 ;$ but $| k z ^ { k } | = | k | $ ∞ here.   
2. Use that absolutely convergent implies convergent, and $\sum \left| k ^ { - 2 } z ^ { k } \right| = \sum \left| k ^ { - 2 } \right|$ converges   
by the p-test.   
3. If $z = 1$ , this is the harmonic series. Otherwise take $a _ { k } = 1 / k , b _ { k } = e ^ { i k \theta }$ where $\theta \in ( 0 , 2 \pi )$   
is some constant, and apply Dirichlet’s test. It suffices to bound the partial sums of the   
$b _ { k }$ . Recalling that $\sum \hat { r } ^ { k } \overset { \sim } { = } ( 1 - r ^ { N + 1 } ) / ( 1 - r )$ 2   
k≤N   
$\left. \sum _ { k \leq m } e ^ { i k \theta } \right. = \left. { \frac { 1 - e ^ { i ( m + 1 ) \theta } } { 1 - e ^ { i \theta } } } \right. \leq { \frac { 2 } { \| 1 - e ^ { i \theta } \| } } : = M ,$   
which is a constant. Here we’ve used that two points on $S ^ { 1 }$ are at most distance 2 from   
each other.

Exercise 3.3.14 (Laurent expansions inside and outside of a disc)   
Expand $f ( z ) = { \frac { 1 } { z ( z - 1 ) } }$ in both   
• $\begin{array} { c } { { | z | < 1 } } \\ { { | z | > 1 } } \end{array}$

$$
{ \frac { 1 } { z ( z - 1 ) } } = - { \frac { 1 } { z } } { \frac { 1 } { 1 - z } } = - { \frac { 1 } { z } } \sum z ^ { k } .
$$

and

$$
{ \frac { 1 } { z ( z - 1 ) } } = { \frac { 1 } { z ^ { 2 } ( 1 - { \frac { 1 } { z } } ) } } = { \frac { 1 } { z ^ { 2 } } } \sum \left( { \frac { 1 } { z } } \right) ^ { k } .
$$

Exercise 3.3.15 (Laurent expansions about different points) Find the Laurent expansion about $z = 0$ and $z = 1$ respectively of the following function:

$$
f ( z ) : = { \frac { z + 1 } { z ( z - 1 ) } } .
$$

## Solution:

Note: once you see that everything is in terms of powers of $( z - z _ { 0 } )$ , you’re essentially done. For $z = 0$ :

$$
\begin{array} { r l r } {  { \frac { z + 1 } { z ( z - 1 ) } = \frac { 1 } { z } \frac { z + 1 } { z - 1 } } } \\ & { } & { = - \frac { z + 1 } { z } \frac { 1 } { 1 - z } } \\ & { } & { = - ( 1 + \frac { 1 } { z } ) \sum _ { k \geqslant 0 } z ^ { k } . } \end{array}
$$

For $z = 1$

$$
\begin{array} { l } { \displaystyle \frac { z + 1 } { z ( z - 1 ) } = \frac { 1 } { z - 1 } \left( 1 + \frac { 1 } { z } \right) } \\ { \displaystyle = \frac { 1 } { z - 1 } \left( 1 + \frac { 1 } { 1 - ( 1 - z ) } \right) } \\ { \displaystyle = \frac { 1 } { z - 1 } \left( 1 + \sum _ { k \geq 0 } ( 1 - z ) ^ { k } \right) } \\ { \displaystyle = \frac { 1 } { z - 1 } \left( 1 + \sum _ { k \geq 0 } ( - 1 ) ^ { k } ( z - 1 ) ^ { k } \right) . } \end{array}
$$

Exercise 3.3.16 (?)

Show that a real-valued holomorphic function must be constant.

## Cauchy’s Theorem

<!-- image-->

## 4.1 Complex Integrals

<!-- image-->

Definition 4.1.1 (Complex Integral)

$$
\int _ { \gamma } f d z : = \int _ { I } f ( \gamma ( t ) ) \gamma ^ { \prime } ( t ) d t = \int _ { \gamma } ( u + i v ) d x \wedge ( - v + i u ) d y .
$$

Theorem 4.1.2(Cauchy-Goursat Theorem).

If f is holomorphic on a region Ω with $\pi _ { 1 } \Omega = 1$ , then for any closed path $\gamma \subseteq \Omega$

$$
\int _ { \gamma } f ( z ) d z = 0 .
$$

Slogan 4.1.3

Closed path integrals of holomorphic functions vanish.

<!-- image-->

## 4.2 Applications of Cauchy’s Theorem

## 4.2.1 Integral Formulas and Estimates

Suppose f is holomorphic on Ω, then for any $z _ { 0 } \in \Omega$ and any open disc $\overline { { D _ { R } ( z _ { 0 } ) } }$ such that $\gamma : = \partial \overline { { D _ { R } ( z _ { 0 } ) } } \subseteq \Omega$

$$
f ( z _ { 0 } ) = { \frac { 1 } { 2 \pi i } } \int _ { \gamma } { \frac { f ( \xi ) } { \xi - z _ { 0 } } } ~ d \xi
$$

and

$$
{ \frac { \partial ^ { n } f } { \partial z ^ { n } } } \left( z _ { 0 } \right) = { \frac { n ! } { 2 \pi i } } \int _ { \gamma } { \frac { f ( \xi ) } { ( \xi - z _ { 0 } ) ^ { n + 1 } } } d \xi .
$$

Proof. It follows from a consequence of Cauchy's theorem (see above) that if $C ( z _ { 0 } , r )$ denotes the circle of radius r around $z _ { \mathrm { 0 } }$ for a sufficiently small $r > 0$ then

$$
\begin{array} { r c l } { | \displaystyle \frac { 1 } { 2 \pi i } \int _ { C } \frac { f ( z ) } { z - z _ { 0 } } d z - f ( z _ { 0 } ) | } & { = } & { | \displaystyle \frac { 1 } { 2 \pi i } \int _ { C ( z _ { 0 } , r ) } \frac { f ( z ) - f ( z _ { 0 } ) } { z - z _ { 0 } } d z | } \\ & { = } & { | \displaystyle \frac { 1 } { 2 \pi i } \int _ { 0 } ^ { 2 \pi } \frac { f ( z _ { 0 } + r e ^ { i \theta } ) - f ( z _ { 0 } ) } { r e ^ { i \theta } } i r e ^ { i \theta } d \theta | } \\ & { \leq } & { \displaystyle \frac { 1 } { 2 \pi } 2 \pi \times \operatorname* { s u p } _ { \theta \in [ 0 , 2 \pi ) } | f ( z _ { 0 } + r e ^ { i \theta } ) - f ( z _ { 0 } ) | } \\ & & { \displaystyle \qquad ( \mathrm { ~ b y ~ } M L \mathrm { ~ i n e q u a l i t y } ) . } \end{array}
$$

As f is continuous it follows that the righthand side goes to zero as r tends to zero.   
This completes the proof.

## Figure 2: image_2021-05-27-16-54-06

Proof (?).

## Proof (?).

Proof. (\*) Using Cauchy's integral formula we can write that

$$
\begin{array} { r c l } { { f ^ { \prime } ( z _ { 0 } ) } } & { { = } } & { { \displaystyle \operatorname* { l i m } _ { h  0 } \frac { f ( z _ { 0 } + h ) - f ( z _ { 0 } ) } { h } = \operatorname* { l i m } _ { h  0 } \frac { 1 } { 2 \pi i h } \int _ { C } ( \frac { f ( z ) } { z - z _ { 0 } - h } - \frac { f ( z ) } { z - z _ { 0 } } ) d z } } \\ { { } } & { { } } & { { ( C \ \mathrm { i s ~ s o ~ c h o s e n ~ t h a t ~ t h e ~ p o i n t ~ } z _ { 0 } + h \mathrm { ~ i s ~ e n c l o s e d ~ b y ~ } C ) } } \\ { { } } & { { = } } & { { \displaystyle \operatorname* { l i m } _ { h  0 } \frac { 1 } { 2 \pi i h } \int _ { C } \frac { f ( z ) h } { ( z - z _ { 0 } - h ) ( z - z _ { 0 } ) } d z . } } \end{array}
$$

So we need to prove that

$$
\begin{array} { c l } { { } } & { { \displaystyle | \int _ { C } \frac { f ( z ) } { ( z - z _ { 0 } - h ) ( z - z _ { 0 } ) } d z - \int _ { C } \frac { f ( z ) } { ( z - z _ { 0 } ) ^ { 2 } } d z | } } \\ { { } } & { { = } } \\ { { } } & { { \displaystyle | \int _ { C } \frac { f ( z ) h } { ( z - z _ { 0 } - h ) ( z - z _ { 0 } ) ^ { 2 } } d z \Big |  0 , \mathrm { ~ a s ~ } h  0 . } } \end{array}
$$

We will basically use ML inequality to prove this. Note that, as f is continuous it is bounded on C by M (say). Let α = min $\{ | z - z _ { 0 } | : z \in C \}$ . Then $| z - z _ { 0 } | ^ { 2 } \geq \alpha ^ { 2 }$ and $\alpha \leq | z - z _ { 0 } | = | z - z _ { 0 } - h + h | \leq | z - z _ { 0 } - h | + | h |$ and hence for $| h | \leq { \frac { \alpha } { 2 } }$ (after all h is going to be small) we get $\begin{array} { r } { | z - z _ { 0 } - h | \ge \alpha - | h | \ge \frac { \alpha } { 2 } } \end{array}$ . Therefore

$$
{ \biggl | } \int _ { C } { \frac { f ( z ) h } { ( z - z _ { 0 } - h ) ( z - z _ { 0 } ) ^ { 2 } } } d z { \biggr | } \leq { \frac { M | h | l } { { \frac { \alpha } { 2 } } \alpha ^ { 2 } } } = { \frac { 2 M | h | l } { \alpha ^ { 3 } } } \to 0 ,
$$

as $h  0$ . By repeating exactly the same technique we get $\begin{array} { r } { f ^ { 2 } ( z _ { 0 } ) = \frac { 2 ! } { 2 \pi i } \int _ { C } \frac { f ( z ) } { ( z - z _ { 0 } ) ^ { 3 } } d z } \end{array}$ and so on.

## Theorem 4.2.2(Cauchy’s Inequality / Cauchy’s Estimate).

For $z _ { 0 } \in D _ { R } ( z _ { 0 } ) \subset \Omega$ , setting $M : = \operatorname* { s u p } _ { z \in \gamma } | f ( z ) | \ \mathrm { s o } \ | f ( z ) | \leq M$ on γ

$$
\left| f ^ { ( n ) } ( z _ { 0 } ) \right| \le \frac { n ! } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \frac { M } { R ^ { n + 1 } } R d \theta = \frac { M n ! } { R ^ { n } } .
$$

Proof (of Cauchy’s inequality).

• Given $z _ { 0 } \in \Omega$ , pick the largest disc $D _ { R } ( z _ { 0 } ) \subset \Omega$ and let $C = \partial D _ { R }$

• Then apply the integral formula.

$$
{ \begin{array} { r l } { \left| f ^ { ( n ) } ( z _ { 0 } ) \right| = \left| { \frac { n ! } { 2 \pi i } } \int _ { C } { \frac { f ( z ) } { ( z - z _ { 0 } ) ^ { n + 1 } } } d z \right| } \\ & { = \left| { \frac { n ! } { 2 \pi i } } \int _ { 0 } ^ { z _ { 0 } } { \frac { f \left( z _ { 1 } + r < i ^ { n } \right) r - i ^ { n } d ^ { n } } { ( r - i ^ { n } ) ^ { 1 / 2 } } } d \theta \right| } \\ & { \leq { \frac { n ! } { 2 \pi i } } \int _ { 0 } ^ { z _ { 0 } } \left| { \frac { f \left( z _ { 0 } + r < i ^ { n } \right) r - i ^ { n } d ^ { n } } { ( r - i ^ { n } ) ^ { 1 / 2 } } } \right| d \theta } \\ & { = { \frac { n ! } { 2 \pi i } } \int _ { 0 } ^ { z _ { 0 } } { \frac { \left| f \left( z _ { 0 } + r < i ^ { n } \right) \right| } { r ^ { n } } } d \theta } \\ & { \leq { \frac { n ! } { 2 \pi i } } \int _ { 0 } ^ { z _ { 0 } } { \frac { \lambda d } { i ^ { n } } } d \theta } \\ & { = { \frac { M \pi } { 2 } } ~ } \end{array} }
$$

## Slogan 4.2.3

The nth Taylor coefficient of an analytic function is at most sup $| f | / R ^ { n }$

If $f$ is holomorphic on $D _ { r } ( z _ { 0 } )$

$$
f ( z _ { 0 } ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } f ( z _ { 0 } + r e ^ { i \theta } ) d \theta = \frac { 1 } { \pi r ^ { 2 } } \iint _ { D _ { r } ( z _ { 0 } ) } f ( z ) d A .
$$

Taking the real part of both sides, one can replace $f = u +$ iv with u.

## 4.2.2 Liouville

Theorem 4.2.5(Liouville’s Theorem).   
If f is entire and bounded, f is constant.

Proof (of Liouville).

• Since f is bounded, $f ( z ) \leq M$ uniformly on $\mathbb { C } .$

• Apply Cauchy’s estimate for the 1st derivative:

$$
\left. f ^ { \prime } ( z ) \right. \le \frac { 1 ! \| f \| _ { C _ { R } } } { R } \le \frac { M } { R } \overset { R \to \infty } { \longrightarrow } 0 ,
$$

so $f ^ { \prime } ( z ) = 0$ for all z.

Exercise 2.E. [SSh03, 2.15] Suppose f is continuous and non-zero on $\overline { { \mathbb { D } } }$ and holomorphic on D such that $| f ( z ) | = 1$ for all $| z | = 1$ . Show that f is then constant.

Figure 3: image_2021-05-17-11-54-14

Exercise 4.2.6 (?)

## 4.2.3 Continuation Principle

Theorem 4.2.7(Continuation Principle / Identity Theorem).

If f is holomorphic on a bounded connected domain Ω and there exists a sequence $\left\{ z _ { i } \right\}$ with a limit point in Ω such that $f ( z _ { i } ) = 0$ , then $f \equiv 0$ on Ω.

## Slogan 4.2.8

Two functions agreeing on a set with a limit point are equal on a domain.

Proof (?).

Apply Improved Taylor Theorem? todo

Exercise 2.D. [SSh03, 2.13] If f is holomorphic on a region Ω and for each $z _ { 0 } \in \Omega$ at least one coefficient in the power series expansion $\begin{array} { r } { f ( z ) \bar { \mathbf { \Psi } } = \sum _ { n = 0 } ^ { \infty } c _ { n } ( z - z _ { 0 } ) ^ { n } } \end{array}$ is zero. Then show that f is a polynomial.

Figure 4: image_2021-05-17-11-53-33

Exercise 4.2.9 (?)

## 4.3 Exercises

$$
\int _ { \gamma } f = 0
$$

$$
\gamma \subseteq \Omega .
$$

## Exercise 4.3.2 (?)

Prove the uniform limit theorem for holomorphic functions: if $f _ { n } $ f locally uniformly and each $f _ { n }$ is holomorphic then f is holomorphic.

## Solution:

This is S&S Theorem 5.2. Statement: if $f _ { n }  f$ uniformly locally uniformly on Ω then f is holomorphic on Ω.

• Let $D \subset \Omega$ with $\overline { { \mathbb { D } } } \subset \Omega$ and $\Delta \subset D$ be a triangle.

• Apply Goursat: $\int _ { \Delta } f _ { n } = 0 .$

$f _ { n }  f$ uniformly on $\Delta$ since it is closed and bounded and thus compact by Heine-Borel, so f is continuous and

$$
\operatorname* { l i m } _ { n } \int _ { \Delta } f _ { n } = \int _ { \Delta } \operatorname* { l i m } _ { n } f _ { n } : = \int _ { \Delta } f .
$$

• Apply Morera’s theorem: $\int _ { \Delta } f$ vanishes on every triangle in Ω, so f is holomorphic on Ω.

## Exercise 4.3.3 (?)

Prove that if $f _ { n }  f$ locally uniformly with $f _ { n }$ holomorphic, then $f _ { n } ^ { \prime }  f ^ { \prime }$ locally uniformly and $f ^ { \prime }$ is holomorphic.

## Solution:

• Simplifying step: for some reason, it suffices to assume $f _ { n }  f$ uniformly on all of Ω?

• Take $\Omega _ { R }$ to be Ω with a buffer of R, so $d ( z , \partial \Omega ) > R$ for every $z \in \overline { { \Omega _ { R } } }$

• It suffices to show the following bound for F any holomorphic function on Ω:

$$
\operatorname* { s u p } _ { z \in \Omega _ { R } } | F ^ { \prime } ( z ) | \leq \frac { 1 } { R } \operatorname* { s u p } _ { \zeta \in \Omega } | F ( \zeta ) |
$$

$$
\forall R ,
$$

where on the right we take the sup over all Ω.

– Then take $F : = f _ { n } - f$ and $R  0$ to conclude, since the right-hand side is a constant not depending on $\Omega _ { R }$

• For any $z \in \Omega _ { R }$ , we have ${ \overline { { D _ { R } ( z ) } } } \subseteq \Omega _ { R } .$ , so Cauchy’s integral formula can be applied:

$$
\begin{array} { r l }   \begin{array} { r l } {  \begin{array} { r l } { F ( \xi ) } & { = | \displaystyle { \frac { 1 } { 2 \pi \sqrt { 3 } \pi } } \int _ { \alpha \xi \xi \xi } d \xi | } \\ & { = | \displaystyle { \frac { 1 } { 2 \pi \sqrt { 3 } \pi } } \int _ { \alpha \xi \xi \xi } d \xi | } \end{array} } & { \mathbb { E } ( \xi ) } \\ & { \le \frac { 1 } { 2 \pi \sqrt { 3 } \pi } \int _ { \alpha \xi \xi \xi } | | \xi | ^ { 2 } \mathbb { E } ( \xi ) | } \\ & { \le \frac { 1 } { 2 \pi \sqrt { 3 } \pi } \int _ { \alpha \xi \xi \xi } \frac { \xi \nabla \xi ( \xi ) \big | \xi ( \xi ) \big | } { | \xi | ^ { 2 } \mathbb { E } ^ { 2 } | \xi | ^ { 3 } } d \xi } \\ & { - \frac { 1 } { 2 \pi \sqrt { 3 } \pi } | \xi \xi | \Big | \int _ { \alpha \xi \xi \xi \xi } \frac { 1 } { \sqrt { 3 } \pi } \int _ { \alpha \xi \xi \xi \xi } \frac { 1 } { \sqrt { 3 } \pi } d \xi } \\ & { - \frac { 1 } { 2 \pi \sqrt { 3 } \pi } | \xi \xi | \Big | \frac { 1 } { 2 \pi } \int _ { \alpha \xi \xi \xi \xi \xi } \frac { 1 } { \sqrt { 3 } \pi } d \xi } \\ & { = \frac { 1 } { 2 \pi \sqrt { 3 } \pi } | \xi \xi | \Big | \frac { 1 } { 2 \pi } \int _ { \alpha \xi \xi \xi \xi } \frac { 1 } { 2 \pi \xi } d \xi } \\ & { \le \frac { 1 } { 2 \pi \sqrt { 3 } \pi } | \xi | \frac { 1 } { 2 \pi } \int _ { \alpha \xi \xi \xi } \frac { 1 } { \sqrt { 3 } \pi } ( \xi ) \frac { 1 } { 2 \pi \xi } \frac { \xi } { \sqrt { 3 } \pi } } \\ &  - \frac { 1 }  2 \pi \sqrt  3  \end{array} \end{array}
$$

• Now

$$
\left\| f _ { n } ^ { \prime } - f ^ { \prime } \right\| _ { \infty , \Omega _ { R } } \leq \frac { 1 } { R } \| f _ { n } - f \| _ { \infty , \Omega } ,
$$

where if R is fixed then by uniform convergence of $f _ { n }  f .$ , for n large enough $\| f _ { n } - f \| <$ $\varepsilon / R .$

## 4.4 Morera’s Theorem

## Theorem 4.4.1(Morera’s Theorem).

If f is continuous on a domain Ω and $\int _ { T } f = 0$ for every triangle $T \subset \Omega$ , then f is holomorphic.

## Slogan 4.4.2

If every integral along a triangle vanishes, implies holomorphic.

## Corollary 4.4.3(Sufficient condition for a sequence to converge to a holomorphic function).

If $\{ f _ { n } \} _ { n \in \mathbb { N } }$ is a holomorphic sequence on a region Ω which uniformly converges to $f$ on every compact subset $K \subseteq \Omega$ , then $f$ is holomorphic, and $f _ { n } ^ { \prime } \to f ^ { \prime }$ uniformly on every such compact subset K.

Proof (?).

Commute limit with integral and apply Morera’s theorem.

Remark 4.4.4: This can be applied to series of the form $\sum _ { k } f _ { k } ( z )$

## 4.4.1 Symmetric Regions

In this section, take Ω to be a region symmetric about the real axis, so $z \in \Omega \iff \bar { z } \in \Omega$ . Partition this set as $\Omega ^ { + } \subseteq \mathbb { H } , I \subseteq \mathbb { R } , \Omega ^ { - } \subseteq \overline { { \mathbb { H } } }$

## Theorem 4.4.5(Symmetry Principle).

Suppose that $f ^ { + }$ is holomorphic on $\Omega ^ { + }$ and $f ^ { - }$ is holomorphic on $\Omega ^ { - }$ , and f extends continuously to I with $f ^ { + } ( x ) = f ^ { - } ( x )$ for $x \in I$ Then the following piecewise-defined function is holomorphic on Ω:

$$
f ( z ) : = \left\{ { \begin{array} { l l } { f ^ { + } ( z ) } & { z \in \Omega ^ { + } } \\ { f ^ { - } ( z ) } & { z \in \Omega ^ { - } } \\ { f ^ { + } ( z ) = f ^ { - } ( z ) } & { z \in I . } \end{array} } \right.
$$

Proof (?).

Apply Morera?

## Theorem 4.4.6(Schwarz Reflection ).

If f is continuous and holomorphic on $\mathbb { H } ^ { + }$ and real-valued on R, then the extension defined by $F ^ { - } ( z ) = \overline { { f ( \bar { z } ) } }$ for $z \in \mathbb { H } ^ { - }$ is a well-defined holomorphic function on C.

Proof (?).

Apply the symmetry principle.

Remark 4.4.7: $\mathbb { H } ^ { + } , \mathbb { H } ^ { - }$ can be replaced with any region symmetric about a line segment $L \subseteq \mathbb { R }$

## 5 Zeros and Singularities

## Definition 5.0.1 (Singularity)

A point $z _ { \mathrm { 0 } }$ is an isolated singularity if $f ( z _ { 0 } )$ is undefined but $f ( z )$ is defined in a punctured neighborhood $D ( z _ { 0 } ) \setminus \{ z _ { 0 } \}$ of $z _ { \mathrm { 0 } }$

There are three types of isolated singularities:

• Removable singularities

• Poles

• Essential singularities

## Definition 5.0.2 (Removable Singularities)

If $z _ { \mathrm { 0 } }$ is a singularity of f. then z0 is a removable singularity iff there exists a holomorphic function $g$ such that $f ( z ) = g ( z )$ in a punctured neighborhood of $z _ { \mathrm { 0 } }$ . Equivalently,

$$
\operatorname* { l i m } _ { z  z _ { 0 } } ( z - z _ { 0 } ) f ( z ) = 0 .
$$

Equivalently, f is bounded on a neighborhood of $z _ { \mathrm { 0 } }$

Remark 5.0.3: Singularities can be classified by Laurent expansions $f ( z ) = \sum _ { k \in \mathbb { Z } } c _ { k } z ^ { k } { \mathrm { : } }$

• Essential singularity: infinitely many negative terms.

• Pole of order N : truncated at $k = - N$ , so $c _ { N - \ell } = 0$ for all $\ell .$

• Removable singularity: truncated at $k = 0 ,$ , so $c _ { \leq - 1 } = 0 .$

Example 5.0.4(Removable singularities):

$f ( z ) : = \sin ( z ) / z$ has a removable singularity at $z = 0$ , and one can redefine $f ( 0 ) : = 1$

$\mathrm { ~ I f ~ } f ( z ) = p ( z ) / q ( z )$ with $q ( z _ { 0 } ) = 0$ and $p ( z _ { 0 } ) = 0$ , then $z _ { \mathrm { 0 } }$ is removable with $f ( z _ { 0 } ) : =$ $p ^ { \prime } ( z _ { 0 } ) / q ^ { \prime } ( z _ { 0 } )$

Example 5.0.5(Essential singularities): $f ( z ) : = e ^ { 1 / z }$ has an essential singularity at $z = 0$ , since we can expand and pick up infinitely many negative terms:

$$
e ^ { 1 / z } = 1 + \frac { 1 } { z } + \frac { 1 } { 2 ! z ^ { 2 } } + \cdot \cdot \cdot .
$$

In fact there exists a neighborhood of zero such that $f ( U ) = \mathbb { C } \backslash \{ 0 \}$ . Similarly $g ( z ) : = \sin \left( \frac { 1 } { z } \right)$ has an essential singularity at $z = 0$ , and there is a neighborhood V of zero such that $g ( V ) = \dot { \mathbb { C } }$

Example ${ \bf 5 . 0 . 6 } ( \vartheta . { \bf \ell } ) .$ The singularities of a rational function are always isolated, since there are finitely many zeros of any polynomial. The function $F ( z ) : = \log ( z )$ has a singularity at $z = 0$ that is not isolated, since every neighborhood intersects the branch cut $( - \infty , 0 ) \times \{ 0 \}$ , where F is not even defined. The function $G ( z ) : = 1 / \sin ( \pi / z )$ has a non-isolated singularity at 0 and isolated singularities at $1 / n$ for all n.

## 4! Warning 5.0.7

$f ( z ) : = z ^ { \frac { 1 } { 2 } }$ has a singularity at zero that does not fall under this classification $- \ z = 0$ is a branch singularity and admits no Laurent expansion around $z = 0$

A similar example: $( z ( z - 1 ) ) ^ { \frac { 1 } { 2 } }$ has two branch singularities at $z = 0 , 1$

## Theorem 5.0.8(Extension over removable singularities).

If f is holomorphic on $\Omega \setminus \{ z _ { 0 } \}$ where $z _ { \mathrm { 0 } }$ is a removable singularity, then there is a unique holomorphic extension of f to all of Ω.

## Proof (?).

Take γ to be a circle centered at $z _ { \mathrm { 0 } }$ and use

$$
f ( z ) : = \int _ { \gamma } { \frac { f ( \xi ) } { \xi - z } } d x .
$$

This is valid for $z \neq z _ { 0 }$ , but the right-hand side is analytic. (?)

## Theorem 5.0.9(Improved Taylor Remainder Theorem).

If $f$ is analytic on a region Ω containing $z _ { 0 } .$ , then $f$ can be written as

$$
f ( z ) = \left( \sum _ { k = 0 } ^ { n - 1 } \frac { f ^ { ( k ) } \left( z _ { 0 } \right) } { k ! } \left( z - z _ { 0 } \right) ^ { k } \right) + R _ { n } ( z ) \left( z - z _ { 0 } \right) ^ { n } ,
$$

where $R _ { n }$ is analytic.

## Definition 5.0.10 (Zeros)

If f is analytic and not identically zero on Ω with $f ( z _ { 0 } ) = 0$ , then there exists a nonvanishing holomorphic function $g$ such that

$$
f ( z ) = ( z - z _ { 0 } ) ^ { n } g ( z ) .
$$

We refer to $z _ { \mathrm { 0 } }$ as a zero of order n.

## Definition 5.0.11 (Poles (and associated terminology))

A pole $z _ { \mathrm { 0 } }$ of a function $f ( z )$ is a zero of $g ( z ) : = { \frac { 1 } { f ( z ) } } .$ . Equivalently, $\operatorname* { l i m } _ { z \to z _ { 0 } } f ( z ) = \infty$ In this case there exists a minimal n and a holomorphic h such that

$$
f ( z ) = ( z - z _ { 0 } ) ^ { - n } h ( z ) .
$$

Such an n is the order of the pole. A pole of order 1 is said to be a simple pole.

## Definition 5.0.12 (Principal Part and Residue)

If f has a pole of order n at $z _ { 0 } .$ , then there exist a holomorphic G in a neighborhood of $z _ { \mathrm { 0 } }$ such that

$$
f ( z ) = { \frac { a _ { - n } } { ( z - z _ { 0 } ) ^ { n } } } + \cdots + { \frac { a _ { - 1 } } { z - z _ { 0 } } } + G ( z ) : = P ( z ) + G ( z ) .
$$

The term $P ( z )$ is referred to as the principal part of f at $z _ { \mathrm { 0 } }$ consists of terms with negative degree, and the residue of f at $z _ { \mathrm { 0 } }$ is the coefficient $a _ { - 1 }$

## Definition 5.0.13 (Essential Singularity)

A singularity $z _ { \mathrm { 0 } }$ is essential iff it is neither removable nor a pole. Equivalently, a Laurent series expansion about $z _ { \mathrm { 0 } }$ has a principal part with infinitely many terms.

Theorem 5.0.14(Casorati-Weierstrass).   
If f is holomorphic on $\Omega \setminus \{ z _ { 0 } \}$ where $z _ { \mathrm { 0 } }$ is an essential singularity, then for every $V \subset \Omega \setminus \{ z _ { 0 } \}$   
$f ( V )$ is dense in $\mathbb { C } .$

## Slogan 5.0.15

The image of a punctured disc at an essential singularity is dense in $\mathbb { C } .$

Proof (of Casorati-Weierstrass).   
Pick $w \in \mathbb { C }$ and suppose toward a contradiction that $D _ { R } ( w ) \cap f ( V )$ is empty. Consider   
g(z) := f (z) − w , 1   
and use that it’s bounded to conclude that $z _ { \mathrm { 0 } }$ is either removable or a pole for $f .$

## Definition 5.0.16 (Singularities at infinity)

For any $f$ holomorphic on an unbounded region, we say $z = \infty$ is a singularity (of any of the above types) of $f$ if $g ( z ) : = f ( 1 / z )$ has a corresponding singularity at $z = 0$

## Definition 5.0.17 (Meromorphic)

A function $f : \Omega \to \mathbb { C }$ is meromorphic iff there exists a sequence $\left\{ z _ { n } \right\}$ such that

• $\left\{ z _ { n } \right\}$ has no limit points in Ω.

$f$ is holomorphic in $\Omega \setminus \{ z _ { n } \}$ .

• f has poles at the points $\left\{ z _ { n } \right\}$

Equivalently, $f$ is holomorphic on Ω with a discrete set of points delete which are all poles of $f .$

## Theorem 5.0.18(Meromorphic implies rational).

Meromorphic functions on C are rational functions.

## Proof (?).

Consider $f ( z ) - P ( z )$ , subtracting off the principal part at each pole $z _ { \mathrm { 0 } }$ , to get a bounded entire function and apply Liouville.

## Theorem 5.0.19(Riemann Extension Theorem).

A singularity of a holomorphic function is removable if and only if the function is bounded in some punctured neighborhood of the singular point.

## 6 Counting Zeros and Poles

## 6.1 Argument Principle

Definition 6.1.1 (The logarithmic derivative) The logarithmic derivative is defined as

$$
\partial _ { \log } f : = { \frac { f ^ { \prime } } { f } } .
$$

It converts all poles and zeros of f into simple poles of $\partial _ { \log f } .$

Exercise 6.1.2 (?)

Show that $\partial _ { \log } ( f g ) = \partial _ { \log } f + \partial _ { \log } g ,$ i.e.

$$
\frac { ( f g ) ^ { \prime } } { f g } = \frac { f ^ { \prime } } { f } + \frac { g ^ { \prime } } { g } .
$$

Definition 6.1.3 (Winding Number)

For $\gamma \subseteq \Omega$ a closed curve not passing through a point $z _ { \mathrm { 0 } }$ , the winding number of $\gamma$ about z0 (or the index) is defined as

$$
\operatorname { I n d } _ { z = z _ { 0 } } ( \gamma ) : = { \frac { 1 } { 2 \pi i } } \int _ { \gamma } { \frac { 1 } { \xi - z _ { 0 } } } d \xi .
$$

Theorem 6.1.4(Argument Principle, Zeros/Poles Version).

For $f$ meromorphic in Ω with multisets of zeros $Z _ { f } : = \{ z _ { j } \}$ and poles $P _ { f } : = \{ p _ { k } \}$ (so repeated with multiplicity) for $\gamma : = \partial \Omega$ not intersect

$$
\frac { 1 } { 2 \pi i } \int _ { \gamma } \partial _ { \log } f ( z ) d z = \# Z _ { f } - \# P _ { f } ,
$$

where $\# Z _ { f }$ and $\# P _ { f }$ are the number of zeros and poles respectively, counted with multiplicity.

Proof (?).

• If $z _ { \mathrm { 0 } }$ is a zero of $f$ of order $m _ { \colon }$ , write $f ( z ) = ( z - z _ { 0 } ) ^ { m } g ( z )$ with $g ( z )$ holomorphic and nonzero on some neighborhood of $z _ { \mathrm { 0 } }$

• Compute

$$
\begin{array} { c l c r } { { \partial _ { \log } f ( z ) = { \displaystyle \frac { m ( z - z _ { 0 } ) ^ { m - 1 } g ( z ) + ( z - z _ { 0 } ) ^ { m } g ^ { \prime } ( z ) } { ( z - z _ { 0 } ) ^ { m } g ( z ) } } } } \\ { { = { \displaystyle \frac { m } { z - z _ { 0 } } } + \partial _ { \log } g ( z ) , } } \end{array}
$$

so $z _ { \mathrm { 0 } }$ is a simple pole of $\partial _ { \log } f$ and res $\partial _ { \log } f = m$ z=z0

$\operatorname { I f } z _ { 0 }$ is a pole of $f$ of order m, write $f ( z ) = ( z - z _ { 0 } ) ^ { - m } g ( z )$ , then

$$
\partial _ { \log } f = \frac { - m } { z - z _ { 0 } } + \partial _ { \log } g ,
$$

so $z _ { \mathrm { 0 } }$ is a simple pole and $\operatorname { R e s } _ { z = z _ { 0 } } \partial _ { \log f } = - m$

• Now apply the residue theorem, and group residues according to sign:

$$
\begin{array} { r l } { \displaystyle \frac { 1 } { 2 \pi i } \int _ { \gamma } \partial _ { \log } f ( z ) d z = \sum _ { z _ { i } \in P _ { \partial _ { \log } } } \underset { z = z _ { i } } { \mathrm { R e s } } \partial _ { \log } f ( z ) } & { } \\ { \displaystyle } & { = \sum _ { z _ { k } \in Z _ { f } } \underset { z = z _ { k } } { \mathrm { R e s } } f ( z ) - \sum _ { z _ { j } \in P _ { f } } \underset { z = z _ { j } } { \mathrm { R e s } } f ( z ) . } \end{array}
$$

Theorem 6.1.5(Argument Principle, Index Version).

With the same setup as above,

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \gamma } \partial _ { \log } f ( z ) d z = \operatorname { I n d } _ { w = 0 } ( f \circ \gamma ) ( w ) .
$$

Proof (?).

Make the change of variables $w = f ( z )$ , then $z = \gamma ( t ) \mapsto w = ( f \circ \gamma ) ( t )$ and $d w = f ^ { \prime } ( z ) d z ,$ s o

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \gamma } \partial _ { \log } f ( z ) d z = { \frac { 1 } { 2 \pi i } } \int _ { f \circ \gamma } { \frac { 1 } { w } } d w : = \operatorname { I n d } _ { w = 0 } ( f \circ \gamma ) ( w ) .
$$

Example 6.1.6(Using the index version of the argument principle): Let $f ( z ) = z ^ { 2 } + z =$ $z ( z + 1 )$

$\gamma _ { 1 } : = \{ | z | = 2 \}$ contains 2 zeros and 0 poles, so $f \circ \gamma$ winds twice around zero counterclockwise.

$\gamma _ { 2 } : = \left\{ | z | = \frac { 1 } { 2 } \right\}$ contains 1 zero and 0 poles, so $f \circ \gamma$ winds once.

## 6.2 Rouché

If

$f , g$ are meromorphic on Ω

• $\gamma \subset \Omega$ is a toy contour winding about each zero/pole of $f , g$ exactly once,

$\vert g \vert < \vert f \vert$ on γ

then

$$
{ \underset { z = 0 } { \mathrm { I n d } } } ( f \circ \gamma ) ( z ) = { \underset { z = 0 } { \mathrm { I n d } } } ( ( f + g ) \circ \gamma ) ( z ) \implies Z _ { f } - P _ { f } = Z _ { f + g } - P _ { f + g } .
$$

In particular, if $f , g$ are holomorphic, they have the same number of zeros in Ω.

## Slogan 6.2.2

The number of zeros/poles are determined by a dominating function.

Prove

Exercise 6.2.3 (?)

Show that $h ( z ) = z ^ { 5 } + 3 z + 1$ has 5 zeros in $| z | \leq 2 .$

Exercise 6.2.4 (?)

Show that $h ( z ) = z + 3 + 2 e ^ { z }$ has one root in $\{ \Re ( z ) \le 0 \}$

## Solution:

Use the following contour:

<!-- image-->

Take $g ( z ) : = 2 e ^ { z } < f ( z ) : = f ( z ) : = z + 3 .$

Corollary 6.2.5(Open Mapping).

Any holomorphic non-constant map is an open map.

Prove

## Corollary 6.2.6(Maximum Modulus).

If f is holomorphic and nonconstant on an open connected region Ω, then |f| can not attain a maximum on Ω. If Ω is bounded and f is continuous on Ω, then max |f| occurs on ∂Ω. Ω Conversely, if f attains a local supremum at $z _ { 0 } \in \Omega$ , then f is constant on Ω.

## Corollary 6.2.7(?).

If f is nonzero on Ω, then f attains a minimum on ∂Ω. This follows from applying the MMP to 1/f .

## 6.3 Counting Zeros

## Example 6.3.1:

• Take $P ( z ) = z ^ { 4 } + 6 z + 3 .$

• On $| z | < 2 \colon$

– Set f(z) = z4 and g(z) = 6z + 3, then |g(z)| ≤ 6|z| + 3 = 15 < 16 = |f(z)|.   
– So P has 4 zeros here.

• On |z| < 1:

– Set f(z) = 6z and g(z) = z4 + 3.

– So P has 1 zero here.

## Example 6.3.2:

• Claim: the equation $\alpha z e ^ { z } = 1$ where $| \alpha | > e$ has exactly one solution in D.

• Set f(z) = αz and $g ( z ) = e ^ { - z }$

• Estimate at |z| = 1 we have $| g | = { \big | } e ^ { - z } { \big | } = e ^ { - \Re ( z ) } \leq e ^ { 1 } < | \alpha | = | f ( z ) |$

• f has one zero at z0 = 0, thus so does $f + g .$

<!-- image-->

## Residues

## 7.1 Basics

Remark 7.1.1: Check: do you need residues at all?? You may be able to just compute an integral!

• Directly by parameterization:

$$
\int _ { \gamma } f d z = \int _ { a } ^ { b } f ( z ( t ) ) z ^ { \prime } ( t ) d t
$$

for z(t) a parameterization of $\gamma ,$

• Finding a primitive $F ,$ then

$$
\int _ { \gamma } f = F ( b ) - F ( a ) .
$$

– Note: you can parameterize a circle around $z _ { \mathrm { 0 } }$ using

$$
z = z _ { 0 } + r e ^ { i \theta } .
$$

Fact 7.1.2 (Integrating $z ^ { k }$ around $S ^ { 1 }$ powers residues)

The major fact that reduces integrals to residues:

$$
\int _ { \gamma } z ^ { k } d z = \int _ { 0 } ^ { 2 \pi } e ^ { i k \theta } i e ^ { i \theta } d \theta = i \int _ { 0 } ^ { 2 \pi } e ^ { i ( k + 1 ) \theta d \theta } = \left\{ { 2 \pi i \quad k = - 1 } \atop { \mathrm { e l s e . } }  \right.
$$

Thus

$$
\int \sum _ { k \geq - M } c _ { k } z ^ { k } = \sum _ { k \geq - M } \int c _ { k } z ^ { k } = 2 \pi i c _ { - 1 } ,
$$

i.e. the integral picks out the $c _ { - 1 }$ coefficient in a Laurent series expansion.

Example 7.1.3(?): Consider

$$
f ( z ) : = { \frac { e ^ { i z } } { 1 + z ^ { 2 } } }
$$

where $z \neq \pm i$ , and attempt to integrate

$$
\int _ { \mathbb { R } } f ( z ) d z .
$$

Use a semicircular contour $\gamma _ { R }$ where $z = R e ^ { i t }$ and check

$$
\begin{array} { l } { \displaystyle \operatorname* { s u p } _ { z \in \gamma _ { R } } | f ( z ) | = \displaystyle \operatorname* { m a x } _ { t \in [ 0 , \pi } \frac { 1 } { 1 + ( R e ^ { i t } ) ^ { 2 } } } \\ { \displaystyle \quad = \operatorname* { m a x } _ { t \in [ 0 , \pi } \frac { 1 } { 1 + R ^ { 2 } e ^ { 2 i t } } } \\ { \displaystyle \quad = \frac { 1 } { R ^ { 2 } - 1 } . } \end{array}
$$

## 7.2 Estimates

Proposition 7.2.1(Length bound / ML Estimate).

$$
\left| \int _ { \gamma } f \right| \leq M L : = \operatorname* { s u p } _ { z \in \gamma } \left| f \right| \cdot \operatorname { l e n g t h } ( \gamma ) .
$$

Proof (?).

$$
\left| { \int _ { \gamma } f ( z ) d z } \right| \leq \operatorname* { s u p } _ { t \in [ a , b ] } | f ( z ( t ) ) | \int _ { a } ^ { b } | z ^ { \prime } ( t ) | d t \leq \operatorname* { s u p } _ { z \in \gamma } | f ( z ) | \cdot \mathrm { l e n g t h } ( \gamma ) .
$$

## Proposition 7.2.2(Jordan’s Lemma).

Suppose that $f ( z ) = e ^ { i a z } g ( z )$ for some $^ { g , }$ and let $C _ { R } : = \left\{ z = R e ^ { i t } \ \big | \ t \in [ 0 , \pi ] \right\}$ . Then

$$
\left| \int _ { C _ { R } } f ( z ) d z \right| \leq { \frac { \pi M _ { R } } { a } }
$$

where $M _ { R } : = \operatorname* { s u p } _ { t \in [ 0 , \pi ] } \left| g ( R e ^ { i t } ) \right| .$

Proof (?).

$$
\begin{array} { r l } { \int _ { \Delta x } \rho ( x ) = } & { \int _ { 0 } ^ { x } \exp \{ 2 \pi \} } \\ & { = \int _ { 0 } ^ { x } \exp \{ 2 \pi \} } \\ & { = \int _ { 0 } ^ { x } \exp \{ 2 \pi \} } \\ & { = \int _ { 0 } ^ { x } \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \\ & { = \exp \{ 2 \pi \} } \end{array}
$$

where we’ve used that on $[ 0 , \pi / 2 ]$ , there is an inequality $2 t / \pi \leq \sin ( t )$ . This is obvious from a picture, since sin(t) is a height on $S ^ { 1 }$ and $2 t / \pi$ is a height on a diagonal line:

<!-- image-->  
Figure 5: image_2021-06-09-01-29-22

## 7.3 Residue Formulas

## Theorem 7.3.1(The Residue Theorem).

Let f be meromorphic on a region Ω with poles $\{ z _ { 1 } , z _ { 2 } , \cdots , z _ { N } \}$ Then for any $\gamma \in \Omega ^ { \mathrm { ~ \backslash ~ } }$ $\{ z _ { 1 } , z _ { 2 } , \cdots , z _ { N } \}$

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \gamma } f ( z ) d z = \sum _ { j = 1 } ^ { N } n _ { \gamma } ( z _ { j } ) \operatorname { R e s } _ { z = z _ { j } } f .
$$

If γ is a toy contour, then

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \gamma } f d z = \sum _ { j = 1 } ^ { N } \mathop { \mathrm { R e s } } _ { z = z _ { j } } f .
$$

Proposition 7.3.2(Residue formula for higher order poles).

If f has a pole $z _ { \mathrm { 0 } }$ of order n, then

$$
\operatorname { R e s } _ { z = z _ { 0 } } f = \operatorname * { l i m } _ { z \to z _ { 0 } } { \frac { 1 } { ( n - 1 ) ! } } \left( { \frac { \partial } { \partial z } } \right) ^ { n - 1 } ( z - z _ { 0 } ) ^ { n } f ( z ) .
$$

Proposition 7.3.3(Residue formula for simple poles).

As a special case, if z0 is a simple pole of $f ,$ then

$$
\operatorname { R e s } _ { z = z _ { 0 } } f = \operatorname * { l i m } _ { z  z _ { 0 } } ( z - z _ { 0 } ) f ( z ) .
$$

Corollary 7.3.4(Better derivative formula that sometimes works for simple poles). If additionally $f = g / h$ where $h ( z _ { 0 } ) = 0$ and $h ^ { \prime } ( z _ { 0 } ) \neq 0$ ,

$$
{ \underset { z = z _ { 0 } } { \mathrm { R e s } } } { \frac { g ( z ) } { h ( z ) } } = { \frac { g ( z _ { 0 } ) } { h ^ { \prime } ( z _ { 0 } ) } } .
$$

Proof (?).

Apply L’Hopital:

$$
( z - z _ { 0 } ) \frac { g ( z ) } { h ( z ) } = \frac { ( z - z _ { 0 } ) g ( z ) } { h ( z ) } \overset { L H } { = } \frac { g ( z ) + ( z - z _ { 0 } ) g ^ { \prime } ( z ) } { h ^ { \prime } ( z ) } \overset { z  z _ { 0 } } { \longrightarrow } \frac { g ( z _ { 0 } ) } { h ^ { \prime } ( z _ { 0 } ) } .
$$

Example 7.3.5(Residue of a simple pole (order 1)): Let $f ( z ) = { \frac { 1 } { 1 + z ^ { 2 } } }$ , then $g ( z ) = 1 , h ( z ) =$ $1 + z ^ { 2 }$ , and $h ^ { \prime } ( z ) = 2 z$ so that $h ^ { \prime } ( i ) = 2 i \neq 0$ . Thus

$$
\operatorname { R e s } _ { z = i } { \frac { 1 } { 1 + z ^ { 2 } } } = { \frac { 1 } { 2 i } } .
$$

Proposition 7.3.6(Residue at infinity).

$$
\operatorname { R e s } _ { z = \infty } f ( z ) = \operatorname { R e s } _ { z = 0 } g ( z )
$$

$$
g ( z ) : = - { \frac { 1 } { z ^ { 2 } } } f \left( { \frac { 1 } { z } } \right) .
$$

## 7.3.1 Exercises

## Some good computations here.

## Exercise 7.3.7

Show that the complex zeros of $f ( z ) : = \sin ( \pi z )$ are exactly $\mathbb { Z } ,$ and each is order 1. Calculate the residue of 1/ sin(πx) at $z = n \in \mathbb { Z }$

Exerci

Exercise 3.A. [SSh03, 3.1] Show that the complex zeros of sinπz are exactly at the integers, and are each of order 1. Calculate the residue of 1/sin πx are $z = n \in \mathbb { Z } .$

Exercise 3.C. [SSh03, 3.8] Prove that

$$
\int _ { 0 } ^ { 2 \pi } { \frac { d \theta } { a + b \cos \theta } } = { \frac { 2 \pi } { \sqrt { a ^ { 2 } - b ^ { 2 } } } }
$$

Exe

Exercise 7.3.8 (?)

$$
\int _ { \mathbb { R } } { \frac { 1 } { ( 1 + x ^ { 2 } ) ^ { 2 } } } d x .
$$

Solution:

• Factor $( 1 + z ^ { 2 } ) ^ { 2 } = ( ( z - i ) ( z + i ) ) ^ { 2 }$ , so $f$ has poles at ±i of order 2.

• Take a semicircular contour $\gamma : = I _ { R } \cup D _ { R }$ , then $f ( z ) \approx 1 / z ^ { 4 } \to 0$ for large R and $\int _ { D _ { R } } f \to 0 .$

• Note $\int _ { I _ { R } } f \to \int _ { \mathbb { R } } f , \operatorname { s o } \int _ { \gamma } f \to \int _ { \mathbb { R } } f .$

$\int _ { \gamma } f = 2 \pi i \sum _ { z _ { 0 } } { \underset { z = z _ { 0 } } { \mathrm { R e s } } } f ,$ and $z _ { 0 } = i$ is the only pole in this region.

• Compute

$$
{ \begin{array} { r l } & { { \frac { \operatorname { R e s } } { z = i } } f = \displaystyle { \operatorname* { l i m } _ { z \to i } { \frac { 1 } { ( 2 - 1 ) ! } } { \frac { \partial } { \partial z } } ( z - i ) ^ { 2 } f ( z ) } } \\ & { \qquad = \displaystyle { \operatorname* { l i m } _ { z \to i } { \frac { \partial } { \partial z } } { \frac { 1 } { ( z + i ) ^ { 2 } } } } } \\ & { \qquad = \displaystyle { \operatorname* { l i m } _ { z \to i } { \frac { - 2 } { ( z + i ) ^ { 3 } } } } } \\ & { \qquad = - { \frac { 2 } { ( 2 i ) ^ { 3 } } } } \\ & { \qquad = \displaystyle { \frac { 1 } { 4 i } } } \end{array} }
$$

$$
\implies \int _ { \gamma } f = \frac { 2 \pi i } { 4 i } = \pi / 2 ,
$$

Exercise 7.3.9 (?)

Use a direct Laurent expansion to show

$$
\operatorname { R e s } _ { z = 0 } { \frac { 1 } { z - \sin ( z ) } } = { \frac { 3 ! } { 5 \cdot 4 } } .
$$

Note the necessity: one doesn’t know the order of the pole at zero, so $\romannumeral 3$ unclear how many derivatives to take.

## Solution:

Expand:

$$
\begin{array} { r l } { \frac { 1 } { S } - \frac { 1 } { 8 ( k + \ell ) ^ { 2 } } } & { = \frac { 1 } { S } ^ { - 1 } \left( 1 - \frac { - 2 \ell + 3 } { 8 ( k ) ^ { 2 } } \right) ^ { \frac { 1 } { 2 } } } \\ & { \quad \quad - s ^ { - 1 } \left( 1 - - \frac { 2 } { 1 7 k ^ { 2 } } \left( s - \frac { 1 } { 3 k ^ { 2 } } s ^ { 2 } - \frac { 1 } { 3 k ^ { 3 } } s ^ { 2 } - \cdots \right) \right) ^ { \frac { 1 } { 2 } } } \\ & { \quad \quad = z ^ { - 1 } \left( 1 - \frac { 1 } { 3 k ^ { 2 } } s ^ { 2 } + \frac { 1 } { 9 k ^ { 2 } } s ^ { 2 } + \cdots \right) ^ { \frac { 1 } { 2 } } } \\ & { \quad \quad = z ^ { - 1 } \left( \frac { 1 } { 3 k ^ { 2 } } s ^ { 2 } - \frac { 1 } { 5 k ^ { 2 } } s ^ { 4 } + \cdots \right) ^ { - 1 } } \\ & { \quad \quad = z ^ { - 1 } \cdot \frac { 2 1 \ell ^ { 2 } } { 1 7 k ^ { 2 } } \left( 1 - \frac { 1 } { 8 k ^ { 2 } / k ^ { 2 } } z ^ { 2 } + \cdots \right) ^ { - 1 } } \\ & { \quad \quad - \frac { 3 } { 8 } \left( 1 - \frac { 2 } { 1 7 k ^ { 2 } } \left( s - \frac { 1 } { 3 k ^ { 2 } } \right) \right) } \\ & { \quad \quad = \frac { 3 } { 2 } \left( 1 + \left( \frac { 1 } { 1 7 k ^ { 2 } } z ^ { 2 } \right) + \left( \frac { 1 } { 1 7 k ^ { 2 } } z ^ { 2 } \right) ^ { 2 } + \cdots \right) } \\ & { \quad \quad = 3 z ^ { - 1 } \left( 3 z ^ { - 1 } z ^ { 2 } + 1 0 z \right) } \end{array}
$$

Exercise 7.3.10 (?)

Compute

$$
\operatorname { R e s } { \frac { 1 } { z = 0 } } { \frac { 1 } { z ^ { 2 } \sin ( z ) } } .
$$

Solution:

First expand $( \sin ( z ) ) ^ { - 1 }$

$$
\begin{array} { l } { { \displaystyle { \frac { 1 } { \sin ( z ) } } = \left( z - { \frac { 1 } { 3 ! } } z ^ { 3 } + { \frac { 1 } { 5 ! } } z ^ { 5 } - \cdots \right) ^ { - 1 } } } \\ { { \displaystyle ~ = z ^ { - 1 } \left( 1 - { \frac { 1 } { 3 ! } } z ^ { 2 } + { \frac { 1 } { 5 ! } } z ^ { 4 } - \cdots \right) ^ { - 1 } } } \\ { { \displaystyle ~ = z ^ { - 1 } \left( 1 + \left( { \frac { 1 } { 3 ! } } z ^ { 2 } - { \frac { 1 } { 5 ! } } z ^ { 4 } + \cdots \right) + \left( { \frac { 1 } { 3 ! } } z ^ { 2 } - \cdots \right) ^ { 2 } + \cdots \right) } } \\ { { \displaystyle ~ = z ^ { - 1 } \left( 1 + { \frac { 1 } { 3 ! } } z ^ { 2 } \pm { \cal O } ( z ^ { 4 } ) \right) , } } \end{array}
$$

using that $( 1 - x ) ^ { - 1 } = 1 + x + x ^ { 2 } + \cdot \cdot \cdot$

Thus

$$
\begin{array} { c } { { z ^ { - 2 } \left( \sin ( z ) \right) ^ { - 1 } = z ^ { - 2 } \cdot z ^ { - 1 } \left( 1 + \displaystyle \frac { 1 } { 3 ! } z ^ { 2 } \pm { \cal O } ( z ^ { 4 } ) \right) } } \\ { { = z ^ { - 3 } + \displaystyle \frac { 1 } { 3 ! } z ^ { - 1 } + { \cal O } ( z ) . } } \end{array}
$$

## Exercise 7.3.11 (Keyhole contour and ML estimate)

Compute

$$
\int _ { [ 0 , \infty ] } { \frac { \log ( x ) } { ( 1 + x ^ { 2 } ) ^ { 2 } } } d x .
$$

Solution:

Factor $( 1 + z ^ { 2 } ) ^ { 2 } = ( z + i ^ { 2 } ( z - i ) ^ { 2 }$ . Take a keyhole contour similar to the following:

<!-- image-->  
Figure 6: image_2021-06-09-02-11-59

Show that outer radius R and inner radius $\rho$ circles contribute zero in the limit by the ML estimate? Compute the residues by just applying the formula and manually computing derivatives:

$$
\begin{array} { l } { { \displaystyle \operatorname* { R e s } _ { z = \pm i } f ( z ) = \operatorname* { l i m } _ { z \to \pm i } \frac { \partial } { \partial z } \frac { \log ^ { 2 } ( z ) } { ( z \pm i ) ^ { 2 } } } } \\ { { \displaystyle \quad = \operatorname* { l i m } _ { z \to \pm i } \frac { 2 \log ( z ) ( z \pm i ) ^ { 2 } - 2 ( z \pm i ) ^ { 2 } \log ^ { 2 } ( z ) } { ( ( z \pm i ) ^ { 2 } ) ^ { 2 } } } } \\ { { \displaystyle \quad = \frac { 2 \log ( \pm i ) ( \pm 2 i ) ^ { 2 } - 2 ( \pm 2 i ) ^ { 2 } \log ^ { 2 } ( \pm i ) } { ( \pm 2 i ) ^ { 4 } } } } \\ { { \displaystyle = _ { ? } \frac { \pi } { 4 } \pm \frac { i \pi ^ { 2 } } { 1 6 } . } } \end{array}
$$

See p.4: http: // www. math. toronto. edu/ mnica/ complex1. pdf

Exercise 7.3.12 (Sinc Function) Show

$$
\int _ { ( 0 , \infty ) } { \frac { \sin ( x ) } { x } } d x = { \frac { \pi } { 2 } } .
$$

## Solution:

Take an indented semicircle. Let I be the original integral, then

$$
I = \frac { 1 } { 2 i } \int _ { \mathbb { R } } \frac { e ^ { i z } - 1 } { z } d z .
$$

Exercise 3.E. [SSh03, 3.14] Prove that all entire functions that are also injective take the form $ f ( z ) = a z + b$ with $a , b \in \mathbb { C }$ and $a \neq 0$ •

Figure 7: image_2021-05-17-13-33-55

## 8 Integrals

See this very detailed note.

• For integrals that decay faster than $1 / z ^ { \alpha } , \alpha > 1$ : semicircular contours.

<!-- image-->

<!-- image-->

• For integrals that decay like $1 / z \colon$ rectangular contours.

<!-- image-->  
Rectangular paths of height and width $x _ { 1 } + x _ { 2 }$

• If a trigonometric function is in the numerator, check if $I \approx \Re ( \tilde { I } )$ where $\tilde { I }$ replaces cosines/sines with $e ^ { i z }$

• For rational functions of cos, sin: set $2 \cos ( z ) = z + z ^ { - 1 } , 2 \sin ( z ) = z - z ^ { - 1 } , d \theta = { \frac { d z } { i z } }$ to reduce to a residue count in $| z | \le 1$

Exercise 8.0.1 (?)

$$
\int _ { \mathbb { R } } { \frac { 1 } { ( 1 + x ) ^ { 2 } } } = { \frac { \pi } { 2 } } .
$$

Use that $f ( z ) \sim 1 / z ^ { 4 }$

Solution:

<!-- image-->

Exercise 8.0.2 (?)

$$
\int _ { \mathbb { R } } { \frac { 1 } { x ^ { 4 } + 1 } } = { \frac { \pi { \sqrt { 2 } } } { 2 } } .
$$

Solution:

<!-- image-->

Exercise 8.0.3 (?)

$$
\int _ { 0 } ^ { \infty } { \frac { \cos ( x ) } { x ^ { 2 } + b ^ { 2 } } } d x = { \frac { \pi \mathrm { e } ^ { - b } } { 2 b } } . .
$$

Solution:

Extend to $\int _ { \mathbb { R } }$ using that $f$ is even.

<!-- image-->

Exercise 8.0.4 (Trigonometric functions)

$$
\int _ { 0 } ^ { 2 \pi } { \frac { d \theta } { 1 + a ^ { 2 } - 2 a \cos ( \theta ) } } = { \Bigg \{ } { \frac { 2 \pi } { a ^ { 2 } - 1 } } { \quad } { \mathrm { i f ~ } } | a | > 1 { \mathrm { ~ } } .
$$

Solution:

Write $2 \cos ( z ) = z + z ^ { - 1 }$ on $S ^ { 1 }$ to get

$$
= \int _ { | z | = 1 } { \frac { 1 } { i \left( \left( 1 + a ^ { 2 } \right) z - a \left( z ^ { 2 } + 1 \right) \right) } } d z .
$$

## 8.1 Branch Cuts

Exercise 8.1.1 (?)

$$
\int _ { 0 } ^ { \infty } { \frac { x ^ { \frac { 1 } { 3 } } } { 1 + x ^ { 2 } } } d x = { \frac { \pi } { \sqrt { 3 } } } .
$$

Solution:

<!-- image-->

Exercise 8.1.2 (?)

$$
\int _ { 1 } ^ { \infty } { \frac { d x } { x { \sqrt { x ^ { 2 } - 1 } } } } = { \frac { \pi } { 2 } } .
$$

Solution:

<!-- image-->

<!-- image-->

## Conformal Maps / Linear Fractional Transformations

## Definition 9.0.1 (Conformal Map / Biholomorphism)

A map f is conformal on Ω iff f is complex-differentiable, $f ^ { \prime } ( z ) \neq 0$ for $z \in \Omega .$ , and f preserves signed angles (so f is orientation-preserving). Conformal implies holomorphic, and a bijective conformal map has conformal inverse automatically.

A bijective conformal map $f : U \to V$ biholomorphism, and we say U and V are biholomorphic. Importantly, bijective holomorphic maps always have holomorphic inverses. Self-biholomorphisms of a domain Ω form a group Aut(Ω).

Remark 9.0.2: There is an oft-used weaker condition that $f ^ { \prime } ( z ) \neq 0$ for any point. Note that that this condition alone doesn’t necessarily imply f is holomorphic, since anti-holomorphic maps may have nonzero derivatives. For example, take $\begin{array} { r } { f ( z ) = \bar { z } . } \end{array}$ , so $f ( x + i y ) = x - i y -$ this does not satisfy the Cauchy-Riemann equations.

Remark 9.0.3: A bijective holomorphic map automatically has a holomorphic inverse. This can be weakened: an injective holomorphic map satisfies $f ^ { \prime } ( z ) \neq 0$ and $f ^ { - 1 }$ is well-defined on its range and holomorphic.

Definition 9.0.4 (Linear fractional transformation / Mobius transformation) A map of the following form is a linear fractional transformation:

$$
T ( z ) = { \frac { a z + b } { c z + d } } ,
$$

where the denominator is assumed to not be a multiple of the numerator. These have inverses given by

$$
T ^ { - 1 } ( w ) = { \frac { d w - b } { - c w + a } } .
$$

## Proposition 9.0.5(?).

Given any three points $z _ { 1 } , z _ { 2 } , z _ { 3 }$ , the following Möbius transformation sends them to $1 , 0 , \infty$ respectively:

$$
T ( z ) : = { \frac { ( z - z _ { 1 } ) ( z _ { 2 } - z _ { 3 } ) } { ( z - z _ { 3 } ) ( z _ { 2 } - z _ { 1 } ) } }
$$

$$
z _ { 1 } \mapsto 0
$$

$$
z _ { 2 } \mapsto 1
$$

$$
z _ { 3 } \mapsto \infty .
$$

Such a map is sometimes denoted $( z ; z _ { 1 } , z _ { 2 } , z _ { 3 } )$ . One can use this to produce a map sending any three points to any other three points:

$$
\begin{array} { r } { T ( z ) : = ( w ; w _ { 1 } , w _ { 2 } , w _ { 3 } ) ^ { - 1 } \circ ( z ; z _ { 1 } , z _ { 2 } , z _ { 3 } ) . } \end{array}
$$

Example 9.0.6(?):

$( z , i , 1 , - 1 ) : \mathbb { D } \to \mathbb { H }$

$( z , 0 , - 1 , 1 ) : \mathbb { D } \cap \mathbb { H } \to Q _ { 1 } .$

Theorem 9.0.7(Cayley Transform).

The fractional linear transformation given by $F ( z ) = { \frac { i - z } { i + z } }$ maps D → H with inverse $G ( w ) =$ $i \frac { 1 - w } { 1 + w } .$

Theorem 9.0.8(Characterization of conformal maps).

Conformal maps D → D have the form

$$
g ( z ) = \lambda \frac { 1 - a } { 1 - \bar { a } z } , \quad \vert a \vert < 1 , \quad \vert \lambda \vert = 1 .
$$

Theorem 9.0.9(Riemann Mapping).

If Ω is simply connected, nonempty, and not C, then for every $z _ { 0 } \in \Omega$ there exists a unique conformal map $F : \Omega  \mathbb { D }$ such that $F ( z _ { 0 } ) = 0$ and $F ^ { \prime } ( z _ { 0 } ) > 0$   
Thus any two such sets $\Omega _ { 1 } , \Omega _ { 2 }$ are conformally equivalent.

9.1 By Type
<table><tr><td>Notation</td><td></td><td>Definition</td></tr><tr><td>D :</td><td> $= \left\{ z \mid | z | \leq 1 \right\}$ </td><td>The unit disc</td></tr><tr><td>H :=</td><td> $\left\{ x + i y { \big | } y > 0 \right\}$ </td><td>The upper half-plane</td></tr><tr><td> $X _ { \frac { 1 } { 2 } }$ </td><td></td><td>A &quot;half version of  $X ^ { \mathfrak { n } } ;$  see examples</td></tr><tr><td> $\mathbb { H } _ { \frac { 1 } { 2 } }$ </td><td></td><td>The first quadrant</td></tr><tr><td> $\mathbb { D } _ { \frac { 1 } { 2 } } ^ { \overline { { } } }$ </td><td></td><td>The portion of the first quadrant</td></tr><tr><td></td><td></td><td>inside the unit disc The horizontal strip</td></tr><tr><td></td><td> $L : = \left\{ x + i y \bigm | x \in \mathbb { R } , 0 < y < \pi \right\}$ </td><td></td></tr></table>

Remark 9.1.1(Notation):

Theorem 9.1.2(Classification of Conformal Maps). There are 8 major types of conformal maps:

<table><tr><td>Type/Domains</td><td>Formula</td></tr><tr><td>Translation</td><td> $z \mapsto z + h$ </td></tr><tr><td>Dilation</td><td> $z \mapsto c z$ </td></tr><tr><td>Rotation</td><td> $z \mapsto e ^ { i \theta }$ </td></tr></table>

## Sectors to sectors

$$
z \mapsto z ^ { n }
$$

$\mathbb { D } _ { \frac { 1 } { 2 } } \to \mathbb { H } _ { \frac { 1 } { 2 } }$ , the first quadrant

$$
\mathbb { H }  S
$$

$$
z \mapsto { \frac { 1 + z } { 1 - z } }
$$

$$
\mathbb { D } _ { \frac { 1 } { 2 } } \to L _ { \frac { 1 } { 2 } }
$$

$$
z \mapsto \log ( z )
$$

$$
z \mapsto \log ( z )
$$

$$
S _ { \frac { 1 } { 2 } } \to \mathbb { D } _ { \frac { 1 } { 2 } }
$$

$$
z \mapsto e ^ { i z }
$$

$$
\mathbb { D } _ { \frac { 1 } { 2 } } \to \mathbb { H }
$$

$$
z \mapsto { \frac { 1 } { 2 } } \left( z + { \frac { 1 } { z } } \right)
$$

$$
\underline { { L _ { \frac { 1 } { 2 } }  \mathbb { H } } }
$$

$$
z \mapsto \sin ( z )
$$

## Proposition 9.1.3(Half-plane to Disc).

$$
F : \mathbb { H } ^ { \circ }  \mathbb { D } ^ { \circ }
$$

$$
\{ z \ \middle | \ \Im ( z ) > 0 \}  \{ w \ \middle | \ | w | < 1 \}
$$

$$
z \mapsto { \frac { i - z } { i + z } }
$$

$$
i ( \frac { 1 - w } { 1 + w } )  w .
$$

## Boundary behavior:

• This maps $\mathbb { R }  \partial \mathbb { D }$ , where $F ( \infty ) = - 1$ , and as $x \in \mathbb { R }$ ranges from $- \infty  \infty , F ( x )$ travels from $z = - 1$ counter-clockwise through $S ^ { 1 }$ (starting at $z = - 1$ and moving through the lower half first).

<!-- image-->

<!-- image-->  
So this extends to a map H → D.  
Mnemonic: every z ∈ H is closer to i than −i.

Remark 9.1.4: Some write a similar map:

$$
\mathbb { H } ^ { \circ }  \mathbb { D } ^ { \circ }
$$

$$
z \mapsto { \frac { z - i } { z + i } } .
$$

This is just a composition of the above map with the flip $z \mapsto - z \colon$

$$
- { \frac { i - z } { i + z } } = { \frac { z - i } { i + z } } = { \frac { z - i } { z + i } } .
$$

Proposition 9.1.5(Right half-plane to Disc).

$$
\mathbb { H } _ { R }  \mathbb { D }
$$

$$
\{ z \ \middle | \ \Re ( z ) > 0 \}  \{ w \ \middle | \ | w | < 1 \}
$$

$$
z \mapsto { \frac { 1 - z } { 1 + z } }
$$

$$
{ \frac { 1 - w } { 1 + w } }  w .
$$

Just map the right half-plane $\mathbb { H } _ { R }$ to the disc D by precomposing with a rotation $e ^ { i \pi / 2 } = i \colon$

$$
\mathbb { H } _ { R }  \mathbb { H }  \mathbb { D }
$$

$$
z \mapsto i z \mapsto { \frac { i - ( i z ) } { i + ( i z ) } } = { \frac { i ( 1 - z ) } { i ( 1 + z ) } } = { \frac { 1 - z } { 1 + z } } .
$$

This can easily be inverted:

$$
w = \frac { 1 + z } { 1 + z }
$$

$$
\implies - ( 1 - w ) + z ( w + 1 ) = 0
$$

$$
\implies z = \frac { 1 - w } { 1 + w } .
$$

Boundary behavior: Just a rotated version of H → D!

Mnemonic: every $z \in \mathbb { H } _ { R }$ is closed to 1 than −1.

Proposition 9.1.6(Sector to sector).

For $0 < \alpha < 2 \colon$

$$
F _ { \alpha } : S _ { \frac { \pi } { \alpha } } ^ { \circ }  S _ { \pi } ^ { \circ } = \mathbb { H } ^ { \circ }
$$

$$
\{ z \Big \vert 0 < \mathrm { A r g } ( z ) < \frac { \pi } { \alpha } \}  \{ w \Big \vert 0 < \mathrm { A r g } ( w ) < \pi \}
$$

$$
z \mapsto z ^ { \alpha }
$$

$$
w ^ { \frac { 1 } { \alpha } }  \boldsymbol { w } .
$$

Note that if you look at the image of H under $z \mapsto z ^ { \alpha }$ , you get

$$
\left\{ z \Big | 0 < \mathrm { A r g } ( z ) < \pi \right\} = \left\{ 0 < \mathrm { A r g } ( w ) < \alpha \pi \right\} .
$$

For the inverse, choose a branch cut of log deleting the negative real axis, or more generally fix $0 <$ arg $w <$ απ .

Boundary behavior:

$\operatorname { A s } x$ travels from − $\cdot \infty  0 , F _ { \alpha } ( x )$ travels away from infinity along the ray $\theta = \alpha \pi ,$ so $L = \left\{ e ^ { t \alpha \pi } \ : \left| \ : t \in ( 0 , \infty ) \right. \right\}$ , from $\infty  0$

• As x travels from $0 \to \overleftarrow { \infty } , F _ { \alpha } ( x )$ travels from $0  \infty$ along R.

Proposition 9.1.7(Sector to Disc).

The unmotivated formula first:

$$
F : S _ { \alpha } \to { \mathbb { D } }
$$

$$
\left\{ z \ \middle | \ 0 < \mathrm { A r g } ( z ) < \alpha \right\} = \left\{ w \ \middle | \ | w | < 1 \right\}
$$

$$
z \equiv { \frac { z ^ { \frac { \pi } { \alpha } } - i } { z ^ { \frac { \pi } { \alpha } } + i } } .
$$

Idea: compose some known functions.

<!-- image-->

<!-- image-->  
z-plane

<!-- image-->

<!-- image-->

ζ-plane  
<!-- image-->  
w-plane

$$
S _ { \alpha } \to S _ { \pi } = \mathbb { H } \to \mathbb { D }
$$

$$
z \mapsto z ^ { \frac { \pi } { \alpha } } \mapsto \frac { z - i } { z + i } \Big | _ { z = z ^ { \frac { \pi } { \alpha } } } .
$$

Proposition 9.1.8(Upper half-disc to first quadrant).

$$
\left\{ z \ { \Big | } \ | z | < 1 , \ \mathbb { S } ( z ) > 0 \right\} = \left\{ w \ { \Big | } \ \Re ( w ) > 0 , \ \mathbb { S } ( w ) > 0 \right\}
$$

$$
z \mapsto { \frac { 1 + z } { 1 - z } }
$$

$$
\frac { w - 1 } { w + 1 }  w .
$$

• Why this lands in the first quadrant:

– Use that squares are non-negative and $z = x + i y \in \mathbb { D } \implies x ^ { 2 } + y ^ { 2 } < 1$

$$
f ( z ) = { \frac { 1 - ( x ^ { 2 } + y ^ { 2 } ) } { ( 1 - x ) ^ { 2 } + y ^ { 2 } } } + i { \frac { 2 y } { ( 1 - x ) ^ { 2 } + y ^ { 2 } } } .
$$

• Why the inverse lands in the unit disc:

– For w in Q1, the distance from w to 1 is smaller than from w to −1.

– Check that if $w = u +$ iv where $u , v > 0$ , the imaginary part of the image is positive:

$$
\begin{array} { l } { { \displaystyle { \frac { w - 1 } { w + 1 } } = { \frac { ( w - 1 ) ( w + 1 ) } { \left| w + 1 \right| ^ { 2 } } } } } \\ { { \displaystyle ~ = { \frac { \left( u - 1 + i v \right) ( u + 1 - i v ) } { ( u + 1 ) ^ { 2 } + v ^ { 2 } } } } } \\ { { \displaystyle ~ = { \frac { u ^ { 2 } + v ^ { 2 } + 1 } { ( u + 1 ) ^ { 2 } + v ^ { 2 } } } + i \left( { \frac { 2 v } { ( u + 1 ) ^ { 2 } + v ^ { 2 } } } \right) . } } \end{array}
$$

Boundary behavior:

• On the upper half circle $\left\{ e ^ { i t } \Big | t \in ( 0 , \pi ) \right\}$ , write

$$
f ( z ) = { \frac { 1 + e ^ { i \theta } } { 1 - e ^ { i \theta } } } = { \frac { e ^ { - i \theta / 2 } + e ^ { i \theta / 2 } } { e ^ { - i \theta / 2 } - e ^ { i \theta / 2 } } } = { \frac { i } { \tan ( \theta / 2 ) } } ,
$$

so as t ranges $0  \pi$ we have $f ( z )$ ranging from 0 → i∞ along the imaginary axis.

• As x ranges from $- 1  1$ in $\mathbb { R } , f ( z )$ ranges from $0  \infty$ with $f ( 0 ) = 1$

Proposition 9.1.9(Log: Upper half-plane to horizontal strip).

$$
\mathbb { H }  \mathbb { R } \times ( 0 , \pi )
$$

$$
\{ z \ \middle | \ \Im ( z ) > 0 \}  \{ w \ \middle | \ \Im ( z ) \in ( 0 , \pi ) \}
$$

$$
z \mapsto \log ( z )
$$

$$
e ^ { w }  \mid w .
$$

• Why this lands in a strip: use that $\arg ( z ) \in ( 0 , \pi )$ and $\log ( z ) = | z | + i \arg ( z )$

## Boundary behavior:

• As x travels from $- \infty  0 , F ( x )$ travels horizontally from $\infty + i \pi \ \mathrm { t o } \ - \infty + i \pi .$

• As x travels from $o  \infty , F ( x )$ travels from $- \infty  \infty$ in R.

Remark 9.1.10: This extends to a function $\mathbb { C } \backslash \mathbb { R } ^ { \leq 0 }  \mathbb { R } \times ( - \pi , \pi )$ . Circles of radius R are mapped to vertical line segments connecting ln $( R ) + i \pi$ to l $\mathrm { n } ( R ) - i \pi$ , and rays are mapped to horizontal lines.

Remark 9.1.11: One can find other specific images of the logarithm:

$$
\left\{ z \Big \vert \vert z \vert < 1 , \Im ( z ) > 0 \right\} = \mathbb { R } ^ { < 0 } \times ( 0 , \pi )
$$

$$
\left\{ z \mid \left| z \right| > 1 , \Im ( z ) > 0 \right\} = \mathbb { R } ^ { > 0 } \times ( 0 , \pi )
$$

For the upper half-disc to the negative horizontal half-strip: - As x travels $0  1$ in R, log(x) travels from $- \infty  0 . \mathrm { ~ - ~ } \mathrm { A s } ~ ;$ x travels from −1 to 1 along $S ^ { 1 } \cap$ H, log(x) travels from $0  i \pi$ vertically. - As x travels from $- 1  0 .$ , log(x) travels from $0 + i \pi  i - \infty + i \pi$ along the top of the strip.

Proposition 9.1.12(Half-discs to half strips).

$$
F : ( - \frac { \pi } { 2 } , \frac { \pi } { 2 } ) \times \mathbb { R } ^ { > 0 }  \mathbb { D } \cap \mathbb { H }
$$

$$
z \mapsto e ^ { i z }
$$

$$
\frac { \log ( w ) } { i } ?  w .
$$

This uses that $e ^ { i z } = e ^ { - \Im ( z ) } e ^ { i \Re ( z ) }$

Boundary behavior:

Proposition 9.1.13(Half-disc to upper half-plane).

$$
F : ?  ?
$$

$$
z \mapsto - { \frac { 1 } { 2 } } \left( z + z ^ { - 1 } \right)
$$

Proposition 9.1.14(Upper half-plane to vertical half-strip).

$$
?  ?
$$

$$
z \mapsto \sin ( z )
$$

## 9.2 Exercises

## Exercise 9.2.1 (?)

Find a conformal map from the upper half-disc to the upper half-plane.

## Solution:

Solution: The map $T _ { 0 } ^ { - 1 }$ (z) maps B to the second quadrant. Then multiplying by -i maps this to the first quadrant. Then squaring maps this to the upper half-plane. In the end we have

$$
f ( z ) = \left( - i \left( \frac { i z + i } { - z + 1 } \right) \right) ^ { 2 } .
$$

## 10 Schwarz Reflection

## 10.1 Schwarz

```latex
Theorem 10.1.1(Schwarz Lemma).
If f : D → D is holomorphic with f (0) = 0, then
1. |f (z)| ≤ |z| for all z ∈ D
2. $| f ^ { \prime } ( 0 ) | \leq 1 .$
Moreover, if
$\begin{array} { l } { { \left| f ( z _ { 0 } ) \right| = \left| z _ { 0 } \right| } } \\ { { \left| f ^ { \prime } ( 0 ) \right| = 1 , } } \end{array}$ for any z0 ∈ D, or
then f is a rotation.
```

Proof (?).   
Apply the maximum modulus principle to $f ( z ) / z .$

Exercise 10.1.2 (?)   
Show that $\operatorname { A u t } ( \mathbb { C } ) = \left\{ z \mapsto a z + b \ \Big | \ a \in \mathbb { C } ^ { \times } , b \in \mathbb { C } \right\}$

Theorem 10.1.3(Biholomorphisms of the disc).

$$
\underset { \mathbb { C } } { \mathrm { A u t } } ( \mathbb { D } ) = \left\{ z \mapsto e ^ { i \theta } \left( \frac { \alpha - z } { 1 - \overline { { \alpha } } z } \right) \right\} .
$$

Proof (?).   
Schwarz lemma.

Theorem 10.1.4(?).

$$
\underset { \mathbb { C } } { \mathrm { A u t } } ( \mathbb { H } ) = \left\{ z \mapsto \frac { a z + b } { c z + d } \ \Big \vert \ a , b , c , d \in \mathbb { C } , a d - b c = 1 \right\} \cong \mathrm { P S L } _ { 2 } ( \mathbb { R } ) .
$$

## 11 Schwarz Lemma

Montel’s theorem

Normal families

Schwarz lemma

Equicontinuity

## 12 Unsorted Theorems

Theorem 12.0.1(Riemann’s Removable Singularity Theorem). If f is holomorphic on Ω except possibly at z0 and f is bounded on Ω \ {z0}, then z0 is a removable singularity.

Theorem 12.0.2(Little Picard).   
If f : C → C is entire and nonconstant, then im(f ) is either C or C \ {z0} for some point z0.

Corollary 12.0.3.   
The ring of holomorphic functions on a domain in C has no zero divisors.

Proof .   
???

Find the proof!

Morera

Proposition 12.0.4(Bounded Complex Analytic Functions form a Banach Space).   
For $\Omega \subseteq \mathbb { C } ,$ show that $A ( \mathbb { C } ) : = \left\{ f : \Omega \to \mathbb { C } \ \right|$ f is boundedo is a Banach space.

Proof . ?

Apply Morera’s Theorem and Cauchy’s Theorem

# 13 Proofs of the Fundamental Theorem of Algebra

## 13.0.1 Argument Principle

Proof (using the argument principle).

• Let $P ( z ) = a _ { n } z ^ { n } + \cdot \cdot \cdot + a _ { 0 }$ and $g ( z ) = P ^ { \prime } ( z ) / P ( z )$ , note P is holomorphic

${ \mathrm { S i n c e ~ } } \operatorname* { l i m } _ { | z | \to \infty } P ( z ) = \infty$ , there exist an $R > 0$ such that $P$ has no roots in $\{ | z | \geq R \}$

• Apply the argument principle:

$$
N ( 0 ) = { \frac { 1 } { 2 \pi i } } \oint _ { | \xi | = R } g ( \xi ) d \xi .
$$

• Check that $\operatorname* { l i m } _ { | z \to \infty | } z g ( z ) = n ,$ so g has a simple pole at ∞

• Then g has a Laurent series $\frac { n } { z } + \frac { c _ { 2 } } { z ^ { 2 } } + \cdots$

• Integrate term-by-term to get $N ( 0 ) = n$

## 13.0.2 Rouche’s Theorem

Proof (using Rouche’s theorem).   
$P ( z ) = z ^ { n } + a _ { n - 1 } z ^ { n - 1 } + \ldots + a _ { 0 }$   
be an nth order polynomial. Let $f ( z ) ~ = ~ z ^ { n }$ and $h = P - f . $ Choose an R such that   
$R > \operatorname* { m a x } ( 1 , n | a _ { n - 1 } | , . . . , n | a _ { 0 } | )$ .Then on $| z | = R$ we have   
$| h | \leq | a _ { n - 1 } | R ^ { n - 1 } + | a _ { n - 2 } | R ^ { n - 2 } + \ldots + | a _ { 0 } | \leq { \frac { R } { n } } R ^ { n - 1 } + { \frac { R } { n } } R ^ { n - 2 } + \ldots + { \frac { R } { n } } < R ^ { n } .$   
On $| z | = R$ we have $| f ( z ) | = R ^ { n }$ , so we have shown $| h | < | f |$ on the curve. Thus, the   
corollary to Rouchés theorem says $f + h$ and f have the same number of zeros inside   
$| z | = R .$ Since we know f has exactly n zeros inside the curve the same is true for the   
polynomial $f + h .$ Now let R go to infinity, we've shown that $f + h$ has exactly n zeros in   
the entire plane.   
Note. The proof gives a simple bound on the size of the zeros: they are all have magnitude   
less than or equal to max $\left( 1 , n | a _ { n - 1 } | , \ldots , n | a _ { 0 } | \right)$   
• Let $P ( z ) = a _ { n } z ^ { n } + \cdot \cdot \cdot + a _ { 0 }$   
• Set $f ( z ) = a _ { n } z ^ { n } { \mathrm { ~ a n d ~ } } g ( z ) = P ( z ) - f ( z ) = a _ { n - 1 } z ^ { n - 1 } + \cdot \cdot \cdot + a _ { 0 } , { \mathrm { ~ s o ~ } } f + g = P .$   
• Choose $R >$ max $\left( \frac { | a _ { n - 1 } | + \cdot \cdot \cdot + | a _ { 0 } | } { | a _ { n } | } , 1 \right)$ , then   
|g(z)| := |an−1zn−1 + · · · + a1z + a0|   
$\leq | a _ { n - 1 } z ^ { n - 1 } | + \cdot \cdot \cdot + | a _ { 1 } z | + | a _ { 0 } |$ by the triangle inequality   
= |an−1| · |zn−1| + · · · + |a1| · |z| + |a0|   
= |an−1| · Rn−1 + · · · + |a1|R + |a0|   
$\leq | a _ { n - 1 } | \cdot R ^ { n - 1 } + | a _ { n - 2 } | \cdot R ^ { n - 1 } + \cdot \cdot \cdot + | a _ { 1 } | \cdot R ^ { n - 1 } + | a _ { 0 } | \cdot R ^ { n - 1 } \quad { \mathrm { s i n c e ~ } } R > 1 \implies R ^ { a + b } \preceq R ^ { a }$   
$= R ^ { n - 1 } \left( \left| a _ { n - 1 } \right| + \left| a _ { n - 2 } \right| + \cdot \cdot \cdot + \left| a _ { 1 } \right| + \left| a _ { 0 } \right| \right)$   
$\leq R ^ { n - 1 } \left( \left| a _ { n } \right| \cdot R \right)$ by choice of R   
$= R ^ { n } | a _ { n } |$   
$\textstyle = \left| a _ { n } z ^ { n } \right|$   
$: = | f ( z ) |$   
• Then $a _ { n } z ^ { n }$ has n zeros in $| z | < R ,$ , so $f + g$ also has n zeros.

## 13.0.3 Liouville’s Theorem

Proof (using Liouville’s theorem).

• Suppose p is nonconstant and has no roots, then $\frac { 1 } { p }$ is entire. We will show it is also bounded and thus constant, a contradiction.

• Write $p ( z ) = z ^ { n } \left( a _ { n } + { \frac { a _ { n - 1 } } { z } } + \cdot \cdot \cdot + { \frac { a _ { 0 } } { z ^ { n } } } \right)$

• Outside a disc:

– Note that $p ( z ) \stackrel { z  \infty } {  } \infty .$ . so there exists an R large enough such that $| p ( z ) | \geq { \frac { 1 } { A } }$ for any fixed chosen constant A. Then $| 1 / p ( z ) | \le A$ outside of $| z | > R , { \mathrm { i . e . ~ } } 1 / p ( z )$ is bounded there.

• Inside a disc:

– $p$ is continuous with no roots and thus must be bounded below on $| z | < R .$

$p$ is entire and thus continuous, and since $\overline { { D } } _ { r } ( 0 )$ is a compact set, p achieves a min A there

Set $C : = \operatorname* { m i n } ( A , B )$ , then $| p ( z ) | \geq C$ on all of $\mathbb { C }$ and thus $| 1 / p ( z ) | \le C$ everywhere. So $1 / p ( z )$ is bounded an entire and thus constant by Liouville’s theorem – but this forces $p$ to be constant. E

## 13.0.4 Open Mapping Theorem

## Proof (using the Open Mapping theorem).

• p induces a continuous map $\mathbb { C P } ^ { 1 } \to \mathbb { C P } ^ { 1 }$

• The continuous image of compact space is compact;

• Since the codomain is Hausdorff space, the image is closed.

• p is holomorphic and non-constant, so by the Open Mapping Theorem, the image is open.

• Thus the image is clopen in $\mathbb { C P } ^ { 1 }$

• The image is nonempty, since $p ( 1 ) = \sum a _ { i } \in \mathbb { C }$

$\mathbb { C P } ^ { 1 }$ is connected

• But the only nonempty clopen subset of a connected space is the entire space.

• So $p$ is surjective, and $p ^ { - 1 } ( 0 )$ is nonempty.

• So p has a root.

## 13.0.5 Generalized Liouville

Theorem 13.0.1(Generalized Liouville).   
If X is a compact complex manifold, any holomorphic $f : X \to \mathbb { C }$ is constant.

Lemma 13.0.2(?).

If $f : X \to Y$ is a nonconstant holomorphic map between Riemann surfaces with X compact, then

• f must be surjective,

• Y must be compact,

$f ^ { - 1 } ( q )$ is finite for all $q \in Y$

• The branch and ramification loci consist of finitely many points.

Proof (of FTA, using Generalized Liouville).

Given a nonconstant $p \in \mathbb { C } [ x ]$ , regard it as a function $p : \mathbb { P } ^ { 1 } ( \mathbb { C } ) \to \mathbb { P } ^ { 1 } ( \mathbb { C } )$ by extending so that $p ( \infty ) = \infty$ Since p is nonconstant, by the lemma p is surjective, so there exists some $x \neq \infty$ in $\mathbb { P } ^ { 1 } ( \mathbb { C } )$ with $p ( x ) = 0$

## 14 Appendix

Definition 14.0.1 (Gamma function)

$$
\Gamma ( z ) = \int _ { 0 } ^ { \infty } t ^ { z - 1 } e ^ { - t } d t .
$$

Remark 14.0.2: Some interesting properties of Γ: $\Gamma ( z + 1 ) = z \Gamma ( z )$ and has simple poles at $z = 0 , - 1 , - 2 , \cdot \cdot { }$ · with residues $\operatorname { R e s } _ { z = - m } \Gamma ( z ) = ( - 1 ) ^ { m } / m !$ . There is also a factorization

$$
\Gamma ( z ) = { \frac { 1 } { z e ^ { \gamma z } \prod _ { n = 1 } ^ { \infty } \left( 1 + { \frac { z } { n } } \right) e ^ { \frac { - z } { n } } } }
$$

where $\gamma : = \operatorname* { l i m } _ { N \to \infty } \sum _ { n = 1 ^ { N } } { \frac { 1 } { n } } - \log ( N ) \qquad $

$$
\Gamma ( z ) \Gamma ( 1 - z ) = \frac { \pi } { \sin ( \pi z ) } ,
$$

which yields a product factorization for sin(πz).

$$
\begin{array} { r } { \mathcal L ( t ^ { z - 1 } , s = 1 ) = \Gamma ( z ) \mathrm { ~ a n d ~ } \mathcal L ( t ^ { n } , s = 1 ) = \Gamma ( n + 1 ) . } \end{array}
$$

Theorem 14.0.3(Uniformization).

Every Riemann surface S is the quotient of a free proper holomorphic action of a group G on the universal cover $\tilde { S }$ of $S ,$ so $S \cong { \tilde { S } } / G$ is a biholomorphism. Moreover, $\tilde { S }$ is biholomorphic to either

$\mathbb { C P } ^ { 1 }$

• C

• D

## 14.1 Misc Basic Algebra

Fact 14.1.1 (Standard forms of conic sections)

• Circle: $x ^ { 2 } + y ^ { 2 } = r ^ { 2 }$

• Ellipse: $\left( { \frac { x } { a } } \right) ^ { 2 } + \left( { \frac { y } { b } } \right) ^ { 2 } = 1$

• Hyperbola: $\left( { \frac { x } { a } } \right) ^ { 2 } - \left( { \frac { y } { b } } \right) ^ { 2 } = 1$

– Rectangular Hyperbola: $x y = { \frac { c ^ { 2 } } { 2 } }$

• Parabola: $- 4 a x + y ^ { 2 } = 0 .$

Mnemonic: Write $f ( x , y ) = A x ^ { 2 } + B x y + C y ^ { 2 } + \cdot \cdot \cdot$ , then consider the discriminant $\Delta = B ^ { 2 }$ − 4AC:

$\Delta < 0 \iff$ ellipse

$- \ \Delta < 0$ and $A = C , B = 0 \iff { \mathrm { c i r c l e } }$

$\Delta = 0 \iff$ parabola

$\Delta > 0 \iff$ hyperbola

Fact 14.1.2 (Completing the square)

$$
x ^ { 2 } - b x = ( x - s ) ^ { 2 } - s ^ { 2 } \quad { \mathrm { w h e r e } } s = { \frac { b } { 2 } }
$$

$$
x ^ { 2 } + b x = ( x + s ) ^ { 2 } - s ^ { 2 } \quad { \mathrm { w h e r e } } s = { \frac { b } { 2 } } .
$$

Fact 14.1.3

The sum of the interior angles of an n-gon is $( n - 2 ) \pi$ , where each angle is ${ \frac { n - 2 } { n } } \pi$

## Definition 14.1.4 (The Dirichlet Problem)

Given a bounded piecewise continuous function $u : S ^ { 1 } \to \mathbb { R }$ , is there a unique extension to a continuous harmonic function $\tilde { u } : \mathbb { D } \to \mathbb { R } ?$

Remark 14.1.5: More generally, this is a boundary value problem for a region where the values of the function on the boundary are given. Compare to prescribing conditions on the normal vector on the boundary, which would be a Neumann BVP. Why these show up: a harmonic function on a simply connected region has a harmonic conjugate, and solutions of BVPs are always analytic functions with harmonic real/imaginary parts.

Example 14.1.6(Dirichlet problem on the strip): See section 27, example 1 in Brown and Churchill. On the strip $( x , y ) \in ( 0 , \pi ) \times ( 0 , \infty )$ , set up the BVP for temperature on a thin plate with no sinks/sources:

$$
\Delta T = 0
$$

$$
T ( 0 , y ) = 0 , T ( \pi , y ) = 0 \ \forall y
$$

$$
T ( x , 0 ) = \sin ( x )
$$

$$
T ( x , y ) \stackrel { y \to \infty } { \longrightarrow } 0 .
$$

Then the following function is harmonic on $\mathbb { R } ^ { 2 }$ and satisfies that Dirichlet problem:

$$
T ( x , y ) = e ^ { - y } \sin ( x ) = \Re ( - i e ^ { i z } ) = \Im ( e ^ { i z } ) .
$$

Exercise 14.1.7 (?) Show that there is no continuous square root function defined on all of C.

Solution:   
Suppose $f ( z ) ^ { 2 } = z ,$ . Then f is a section to the covering map   
p : C× → C×   
z 7→ z 2 ,   
so p ◦ f = id. Using $\pi _ { 1 } ( \mathbb { C } ^ { \times } ) = \mathbb { Z }$ , the induced maps are $p _ { * } ( 1 ) = 2$ and $f _ { * } ( 1 ) = n$ for some   
$n \in \mathbb { Z }$ . But then $p _ { * } \circ f _ { * }$ is multiplication by $2 n .$ contradicting $p _ { * } \circ f _ { * } = \mathrm { i d }$ by functoriality.

Remark 14.1.8:

$$
{ \widehat { f } } ( \xi ) : = { \mathcal { L } } ( f , i \xi ) : = \int _ { \mathbb { R } } f ( x ) e ^ { - i \xi x } d x .
$$

Basics

• Show that ${ \frac { 1 } { z } } \sum _ { k = 1 } ^ { \infty } { \frac { z ^ { k } } { k } }$ converges on $S ^ { 1 } \setminus \{ 1 \}$ using summation by parts.

• Show that any power series is continuous on its domain of convergence.

• Show that a uniform limit of continuous functions is continuous.

• Show that if f is holomorphic on D then f has a power series expansion that converges uniformly on every compact $K \subset \mathbb { D }$

• Show that any holomorphic function f can be uniformly approximated by polynomials.

• Show that if f is holomorphic on a connected region Ω and $f ^ { \prime } \equiv 0$ on Ω, then f is constant on Ω.

• Show that if $| f | = 0$ on ∂Ω then either f is constant or f has a zero in Ω.

• Show that if $\left\{ f _ { n } \right\}$ is a sequence of holomorphic functions converging uniformly to a function f on every compact subset of Ω, then f is holomorphic on Ω and $\left\{ f _ { n } ^ { \prime } \right\}$ converges uniformly to $f ^ { \prime }$ on every such compact subset.

• Show that if each $f _ { n }$ is holomorphic on Ω and $F : = \sum f _ { n }$ converges uniformly on every compact subset of Ω, then F is holomorphic.

• Show that if f is once complex differentiable at each point of Ω, then f is holomorphic.
