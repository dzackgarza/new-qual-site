# UGA Qualifying Exam Questions

D. Zack Garza

Monday 18th May, 2020

## Contents

1 Spring 2019 3   
1.1 1 3   
1.2 2 3   
1.3 3 3   
1.4 4 4   
1.5 5 4   
2 Fall 2019 4   
2.1 1. . 4   
2.2 2. 5   
2.3 3. . 5   
2.4 4. 5   
2.5 5. . 6   
3 Spring 2018 6   
3.1 1 6   
3.2 2 6   
3.3 3 6   
3.4 4 7   
3.5 5 7   
4 Fall 2018 7   
4.1 1 . 7   
4.2 2 7   
4.3 3 7   
4.4 4 7   
4.5 5 8   
4.6 6 8   
5 Spring 2017 8   
5.1 1 8   
5.2 2 8   
5.3 3 8   
5.4 4 9   
5.5 5 . 9   
5.6 5 9   
6 Fall 2017 9   
6.1 1 9   
6.2 2 10   
6.3 3 10   
6.4 4 10   
6.5 5 10   
6.6 6 11   
7 Spring 2016 (Neil-ish) 11   
7.1 1 11   
7.2 2 11   
7.3 3 12   
7.4 4 12   
7.5 5 12   
7.6 6 12   
8 Fall 2016 (Neil-ish) 13   
8.1 1 13   
8.2 2 13   
8.3 3 13   
8.4 4 13   
8.5 5 14   
8.6 6 14   
9 Spring 2015 14   
9.1 1 14   
9.2 2 14   
9.3 3 14   
9.4 4 15   
9.5 5 15   
9.6 6 15   
10 Fall 2015 15   
10.1 1 15   
10.2 2 15   
10.3 3 16   
10.4 4 16   
10.5 5 16   
10.6 6 16   
11 Spring 2014 16   
11.1 1 16   
11.2 2 17   
11.3 3 17   
11.4 4 17   
11.5 5 17   
12 Fall 2014 17   
12.1 1 17   
12.2 2 18   
12.3 3 18   
12.4 4 18   
12.5 5 18   
12.6 6 18

## List of Definitions

## List of Theorems

## 1 Spring 2019

## 1.1 1

Let $C ( [ 0 , 1 ] )$ denote the space of all continuous real-valued functions on $[ 0 , 1 ]$

a. Prove that $C ( [ 0 , 1 ] )$ is complete under the uniform norm

$$
\| f \| _ { u } : = \operatorname* { s u p } _ { x \in [ 0 , 1 ] } | f ( x ) |
$$

b. Prove that $C ( [ 0 , 1 ] )$ is not complete under the $L ^ { 1 } .$ -norm $\| f \| _ { 1 } = \int _ { 0 } ^ { 1 } | f ( x ) | ~ d x .$

## 1.2 2

Let B denote the set of all Borel subsets of R and $\mu : B \longrightarrow [ 0 , \infty )$ denote a finite Borel measure on R.

a. Prove that if $\left\{ F _ { k } \right\}$ is a sequence of Borel sets for which $F _ { k } \supseteq F _ { k + 1 }$ for all $k ,$ then

$$
\operatorname* { l i m } _ { k \to \infty } \mu \left( F _ { k } \right) = \mu \left( \bigcap _ { k = 1 } ^ { \infty } F _ { k } \right)
$$

b. Suppose $\mu$ has the property that $\mu ( E ) = 0$ for every $E \in B$ with Lebesgue measure $m ( E ) = 0$ Prove that for every $\varepsilon > 0$ there exists $\delta > 0$ so that if $E \in B$ with $m ( E ) < \delta _ { \mathrm { { f } } }$ , then $\mu ( E ) < \varepsilon$

## 1.3 3

Let $\{ f _ { k } \}$ be any sequence of functions in $L ^ { 2 } ( [ 0 , 1 ] )$ satisfying $\| f _ { k } \| _ { 2 } \leq M$ for all $k \in \mathbb N$

Prove that if $f _ { k } \longrightarrow f$ almost everywhere, then $f \in L ^ { 2 } ( [ 0 , 1 ] )$ with $\| f \| _ { 2 } \leq M$ and

$$
\operatorname* { l i m } _ { k \to \infty } \int _ { 0 } ^ { 1 } f _ { k } ( x ) d x = \int _ { 0 } ^ { 1 } f ( x ) d x
$$

Hint: Try using Fatou’s Lemma to show that $\| f \| _ { 2 } \leq M$ and then try applying Egorov’s Theorem.

## 1.4 4

Let f be a non-negative function on $\mathbb { R } ^ { n }$ and $\mathcal { A } = \{ ( x , t ) \in \mathbb { R } ^ { n } \times \mathbb { R } : 0 \leq t \leq f ( x ) \}$

Prove the validity of the following two statements:

a. f is a Lebesgue measurable function on $\mathbb { R } ^ { n } \iff A$ is a Lebesgue measurable subset of $\mathbb { R } ^ { n + 1 }$

b. If f is a Lebesgue measurable function on $\mathbb { R } ^ { n }$ , then

$$
m ( A ) = \int _ { \mathbb { R } ^ { n } } f ( x ) d x = \int _ { 0 } ^ { \infty } m \left( \{ x \in \mathbb { R } ^ { n } : f ( x ) \geq t \} \right) d t
$$

## 1.5 5

a. Show that $L ^ { 2 } ( [ 0 , 1 ] ) \subseteq L ^ { 1 } ( [ 0 , 1 ] )$ and argue that $L ^ { 2 } ( [ 0 , 1 ] )$ in fact forms a dense subset of $L ^ { 1 } ( [ 0 , 1 ] )$

b. Let Λ be a continuous linear functional on $L ^ { 1 } ( [ 0 , 1 ] )$

Prove the Riesz Representation Theorem for $L ^ { 1 } ( [ 0 , 1 ] )$ by following the steps below:

i. Establish the existence of a function $g \in L ^ { 2 } ( [ 0 , 1 ] )$ which represents Λ in the sense that

$$
\Lambda ( f ) = f ( x ) g ( x ) d x { \mathrm { ~ f o r ~ a l l ~ } } f \in L ^ { 2 } ( [ 0 , 1 ] ) .
$$

Hint: You may use, without proof, the Riesz Representation Theorem for $L ^ { 2 } ( [ 0 , 1 ] )$

ii. Argue that the g obtained above must in fact belong to $L ^ { \infty } ( [ 0 , 1 ] )$ and represent Λ in the sense that

$$
\Lambda ( f ) = \int _ { 0 } ^ { 1 } f ( x ) { \overline { { g ( x ) } } } d x \quad { \mathrm { ~ f o r ~ a l l ~ } } f \in L ^ { 1 } ( [ 0 , 1 ] )
$$

with

$$
\| g \| _ { L ^ { \infty } ( [ 0 , 1 ] ) } = \| \Lambda \| _ { L ^ { 1 } ( [ 0 , 1 ] ) ^ { \vee } }
$$

## 2 Fall 2019

## 2.1 1.

Let $\{ a _ { n } \} _ { n = 1 } ^ { \infty }$ be a sequence of real numbers.

a. Prove that ${ \mathrm { i f } } \operatorname* { l i m } _ { n \longrightarrow \infty } a _ { n } = 0 , { \mathrm { t h e n } } \operatorname* { l i m } _ { n \longrightarrow \infty } a _ { 1 } + \cdots + a _ { n } = 0 .$

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { a _ { 1 } + \cdots + a _ { n } } { n } } = 0
$$

b. Prove that if $\sum _ { n = 1 } ^ { \infty } { \frac { a _ { n } } { n } }$ converges, then

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { a _ { 1 } + \cdots + a _ { n } } { n } } = 0
$$

## 2.2 2.

Prove that

$$
\left| { \frac { d ^ { n } } { d x ^ { n } } } { \frac { \sin x } { x } } \right| \leq { \frac { 1 } { n } }
$$

for all $x \neq 0$ and positive integers n.

Hint: Consider $\int _ { 0 } ^ { 1 } \cos ( t x ) d t$

## 2.3 3.

Let $( X , B , \mu )$ be a measure space with $\mu ( X ) = 1$ and $\{ B _ { n } \} _ { n = 1 } ^ { \infty }$ be a sequence of B-measurable subsets of X , and

$$
B : = \left\{ x \in X \ \left| \ x \in B _ { n } { \mathrm { ~ f o r ~ i n f i n i t e l y ~ m a n y ~ } } n \right. \right\} .
$$

a. Argue that B is also a B-measurable subset of X.

b. Prove that if $\sum _ { n = 1 } ^ { \infty } \mu ( B _ { n } ) < \infty$ then $\mu ( B ) = 0 .$

c. Prove that if $\sum _ { n = 1 } ^ { \infty } \mu ( B _ { n } ) = \infty$ and the sequence of set complements $\{ B _ { n } ^ { c } \} _ { n = 1 } ^ { \infty }$ satisfies

$$
\mu \left( \bigcap _ { n = k } ^ { K } B _ { n } ^ { c } \right) = \prod _ { n = k } ^ { K } \left( 1 - \mu \left( B _ { n } \right) \right)
$$

for all positive integers k and K with $k < K$ , then $\mu ( B ) = 1$

Hint: Use the fact that $1 - x \leq e ^ { - x }$ for all x.

## 2.4 4.

Let $\{ u _ { n } \} _ { n = 1 } ^ { \infty }$ be an orthonormal sequence in a Hilbert space H.

a. Prove that for every $x \in \mathcal H$ one has

$$
\sum _ { n = 1 } ^ { \infty } | \langle x , u _ { n } \rangle | ^ { 2 } \leq \| x \| ^ { 2 }
$$

b. Prove that for any sequence $\{ a _ { n } \} _ { n = 1 } ^ { \infty } \in \ell ^ { 2 } ( \mathbb { N } )$ there exists an element $x \in \mathcal H$ such that

$$
a _ { n } = \left. x , \ u _ { n } \right. { \mathrm { ~ f o r ~ a l l ~ } } n \in \mathbb { N }
$$

and

$$
\| x \| ^ { 2 } = \sum _ { n = 1 } ^ { \infty } \left| \langle x , u _ { n } \rangle \right| ^ { 2 }
$$

## 2.5 5.

a. Show that if f is continuous with compact support on R, then

$$
\operatorname* { l i m } _ { y \to 0 } \int _ { \mathbb { R } } | f ( x - y ) - f ( x ) | d x = 0
$$

b. Let $f \in L ^ { 1 } ( \mathbb { R } )$ and for each $h > 0$ let

$$
A _ { h } f ( x ) : = \frac { 1 } { 2 h } \int _ { | y | \leq h } f ( x - y ) d y
$$

c. Prove that $\| \mathcal { A } _ { h } f \| _ { 1 } \leq \| f \| _ { 1 }$ for all $h > 0$

ii. Prove that $A _ { h } f \longrightarrow f$ in $L ^ { 1 } ( \mathbb { R } )$ as $h \longrightarrow 0 ^ { + }$

## 3 Spring 2018

## 3.1 1

Define

$$
E : = \left\{ x \in \mathbb { R } : \left| x - { \frac { p } { q } } \right| < q ^ { - 3 } { \mathrm { ~ f o r ~ i n f i n i t e l y ~ m a n y ~ } } p , q \in \mathbb { N } \right\}
$$

Prove that $m ( E ) = 0$

## 3.2 2

Let

$$
f _ { n } ( x ) : = { \frac { x } { 1 + x ^ { n } } } , \quad x \geq 0 .
$$

a. Show that this sequence converges pointwise and find its limit. Is the convergence uniform on $\lbrack 0 , \infty ) ?$

b. Compute

$$
\operatorname* { l i m } _ { n  \infty } \int _ { 0 } ^ { \infty } f _ { n } ( x ) d x
$$

## 3.3 3

Let $f$ be a non-negative measurable function on [0, 1].

Show that

$$
\operatorname* { l i m } _ { p \to \infty } { \left( \int _ { [ 0 , 1 ] } f ( x ) ^ { p } d x \right) ^ { \frac { 1 } { p } } } = \| f \| _ { \infty } .
$$

## 3.4 4

Let $f \in L ^ { 2 } ( [ 0 , 1 ] )$ and suppose

$$
\int _ { [ 0 , 1 ] } f ( x ) x ^ { n } d x = 0 { \mathrm { ~ f o r ~ a l l ~ i n t e g e r s ~ } } n \geq 0 .
$$

Show that $f = 0$ almost everywhere.

## 3.5 5

Suppose that

• $f _ { n } , f \in L ^ { 1 }$

$f _ { n } \longrightarrow f$ almost everywhere, and

$\int | f _ { n } | \to \int | f | .$

Show that $\int f _ { n } \to \int f$

## 4 Fall 2018

## 4.1 1

Let $f ( x ) = { \frac { 1 } { x } } .$ . Show that f is uniformly continuous on $( 1 , \infty )$ but not on $( 0 , \infty )$

## 4.2 2

Let $E \subset$ R be a Lebesgue measurable set. Show that there is a Borel set $B \subset E$ such that $m ( E \setminus B ) = 0$

## 4.3 3

Suppose f(x) and $x f ( x )$ are integrable on R. Define F by

$$
F ( t ) : = \int _ { - \infty } ^ { \infty } f ( x ) \cos ( x t ) d x
$$

Show that

$$
F ^ { \prime } ( t ) = - \int _ { - \infty } ^ { \infty } x f ( x ) \sin ( x t ) d x .
$$

## 4.4 4

Let $f \in L ^ { 1 } ( [ 0 , 1 ] )$ . Prove that

$$
\operatorname* { l i m } _ { n \longrightarrow \infty } \int _ { 0 } ^ { 1 } f ( x ) | \sin n x | \ d x = { \frac { 2 } { \pi } } \int _ { 0 } ^ { 1 } f ( x ) \ d x
$$

Hint: Begin with the case that f is the characteristic function of an interval.

## 4.5 5

Let $f \geq 0$ be a measurable function on R. Show that

$$
\int _ { \mathbb { R } } f = \int _ { 0 } ^ { \infty } m ( \{ x : f ( x ) > t \} ) d t
$$

## 4.6 6

Compute the following limit and justify your calculations:

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { 1 } ^ { n } { \frac { d x } { \left( 1 + { \frac { x } { n } } \right) ^ { n } { \sqrt [ n ] { x } } } }
$$

## 5 Spring 2017

## 5.1 1

Let K be the set of numbers in [0, 1] whose decimal expansions do not use the digit 4.

We use the convention that when a decimal number ends with 4 but all other digits are different from 4, we replace the digit 4 with 399 · · ·. For example, $0 . 8 7 5 4 = 0 . 8 7 5 3 9 9 9 \cdots .$

Show that K is a compact, nowhere dense set without isolated points, and find the Lebesgue measure $m ( K )$ .

## 5.2 2

a. Let $\mu$ be a measure on a measurable space $( X , M )$ and $f \mathrm { ~ a ~ }$ positive measurable function.

Define a measure λ by

$$
\lambda ( E ) : = \int _ { E } f \ d \mu , \quad E \in { \mathcal { M } }
$$

Show that for g any positive measurable function,

$$
\int _ { X } g \ d \lambda = \int _ { X } f g \ d \mu
$$

b. Let $E \subset \mathbb { R }$ be a measurable set such that

$$
\int _ { E } x ^ { 2 } \ d m = 0 .
$$

Show that $m ( E ) = 0$

## 5.3 3

Let

$$
f _ { n } ( x ) = a e ^ { - n a x } - b e ^ { - n b x } \quad { \mathrm { ~ w h e r e ~ } } 0 < a < b .
$$

Show that

a. $\sum _ { n = 1 } ^ { \infty } \left| f _ { n } \right|$ is not in $L ^ { 1 } ( [ 0 , \infty ) , m )$

Hint: $f _ { n } ( x )$ has a root $x _ { n } .$

b.

$$
\sum _ { n = 1 } ^ { \infty } f _ { n } { \mathrm { ~ i s ~ i n ~ } } L ^ { 1 } ( [ 0 , \infty ) , m ) \quad { \mathrm { ~ a n d ~ } } \quad \int _ { 0 } ^ { \infty } \sum _ { n = 1 } ^ { \infty } f _ { n } ( x ) d m = \ln { \frac { b } { a } }
$$

## 5.4 4

Let $f ( x , y )$ on $[ - 1 , 1 ] ^ { 2 }$ be defined by

$$
f ( x , y ) = { \left\{ \begin{array} { l l } { \displaystyle { \frac { x y } { \left( x ^ { 2 } + y ^ { 2 } \right) ^ { 2 } } } } & { ( x , y ) \neq ( 0 , 0 ) } \\ { 0 } & { ( x , y ) = ( 0 , 0 ) } \end{array} \right. }
$$

Determine if f is integrable.

## 5.5 5

Let $f , g \in L ^ { 2 } ( \mathbb { R } )$ . Prove that the formula

$$
h ( x ) : = \int _ { - \infty } ^ { \infty } f ( t ) g ( x - t ) d t
$$

defines a uniformly continuous function h on $\mathbb { R }$

## 5.6 5

Show that the space $C ^ { 1 } ( [ a , b ] )$ is a Banach space when equipped with the norm

$$
\| f \| : = \operatorname* { s u p } _ { x \in [ a , b ] } | f ( x ) | + \operatorname* { s u p } _ { x \in [ a , b ] } \left| f ^ { \prime } ( x ) \right| .
$$

## 6 Fall 2017

## 6.1 1

Let

$$
f ( x ) = s \sum _ { n = 0 } ^ { \infty } { \frac { x ^ { n } } { n ! } } .
$$

Describe the intervals on which f does and does not converge uniformly.

## 6.2 2

Let $f ( x ) = x ^ { 2 }$ and $E \subset [ 0 , \infty ) : = \mathbb { R } ^ { + }$

1. Show that

$$
m ^ { * } ( E ) = 0 \Longleftrightarrow m ^ { * } ( f ( E ) ) = 0 .
$$

2. Deduce that the map

$$
\begin{array} { r } { \phi : \mathcal { L } ( \mathbb { R } ^ { + } ) \longrightarrow \mathcal { L } ( \mathbb { R } ^ { + } ) } \\ { E \mapsto f ( E ) } \end{array}
$$

is a bijection from the class of Lebesgue measurable sets of $[ 0 , \infty )$ to itself.

## 6.3 3

Let

$$
S = \mathrm { s p a n } _ { \mathbb { C } } \left\{ \chi _ { ( a , b ) } \ \middle | \ a , b \in \mathbb { R } \right\} ,
$$

the complex linear span of characteristic functions of intervals of the form $( a , b )$

Show that for every $f \in L ^ { 1 } ( \mathbb { R } )$ , there exists a sequence of functions $\{ f _ { n } \} \subset S$ such that

$$
\operatorname* { l i m } _ { n \to \infty } \| f _ { n } - f \| _ { 1 } = 0
$$

## 6.4 4

Let

$$
f _ { n } ( x ) = n x ( 1 - x ) ^ { n } , \quad n \in \mathbb { N } .
$$

1. Show that $f _ { n } \longrightarrow 0$ pointwise but not uniformly on $[ 0 , 1 ]$

Hint: Consider the maximum of $f _ { n } .$

2.

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { 1 } n ( 1 - x ) ^ { n } \sin { x } d x = 0
$$

## 6.5 5

Let φ be a compactly supported smooth function that vanishes outside of an interval $[ - N , N ]$ such that $\int _ { \mathrm { R } } \phi ( x ) d x = 1$

For $f \in L ^ { 1 } ( \mathbb { R } )$ , define

$$
K _ { j } ( x ) : = j \phi ( j x ) , \qquad f * K _ { j } ( x ) : = \int _ { \mathbb { R } } f ( x - y ) K _ { j } ( y ) \ d y
$$

and prove the following:

1. Each $f * K _ { j }$ is smooth and compactly supported.

2.

$$
\operatorname* { l i m } _ { j \to \infty } \| f * K _ { j } - f \| _ { 1 } = 0
$$

Hint:

$$
\operatorname* { l i m } _ { y \to 0 } \int _ { \mathbb { R } } | f ( x - y ) - f ( x ) | d y = 0
$$

## 6.6 6

Let X be a complete metric space and define a norm

$$
\| f \| : = \operatorname* { m a x } \{ | f ( x ) | : x \in X \} .
$$

Show that $( C ^ { 0 } ( \mathbb { R } ) , \| \cdot \| )$ (the space of continuous functions $f : X \longrightarrow \mathbb { R } )$ is complete.

## 7 Spring 2016 (Neil-ish)

## 7.1 1

For $n \in \mathbb { N } .$ , define

$$
e _ { n } = \left( 1 + { \frac { 1 } { n } } \right) ^ { n } \quad { \mathrm { ~ a n d ~ } } \quad E _ { n } = \left( 1 + { \frac { 1 } { n } } \right) ^ { n + 1 }
$$

Show that $e _ { n } < E _ { n }$ , and prove Bernoulli’s inequality:

$$
( 1 + x ) ^ { n } \geq 1 + n x { \mathrm { ~ f o r ~ } } - 1 < x < \infty { \mathrm { ~ a n d ~ } } n \in \mathbb { N }
$$

Use this to show the following:

1. The sequence $e _ { n }$ is increasing.

2. The sequence $E _ { n }$ is decreasing.

3. $2 < e _ { n } < E _ { n } < 4 .$

4. $\operatorname* { l i m } _ { n \to \infty } e _ { n } = \operatorname* { l i m } _ { n \to \infty } E _ { n } .$

## 7.2 2

Let $0 < \lambda < 1$ and construct a Cantor set $C _ { \lambda }$ by successively removing middle intervals of length λ. Prove that $m ( C _ { \lambda } ) = 0$

## 7.3 3

Let f be Lebesgue measurable on R and $E \subset \mathbb { R }$ be measurable such that

$$
0 < A = \int _ { E } f ( x ) d x < \infty .
$$

Show that for every $0 < t < 1$ , there exists a measurable set $E _ { t } \subset E$ such that

$$
\int _ { E _ { t } } f ( x ) d x = t A .
$$

## 7.4 4

Let $E \subset \mathbb { R }$ be measurable with $m ( E ) < \infty$ . Define

$$
f ( x ) = m ( E \cap ( E + x ) ) .
$$

Show that

1. $f \in L ^ { 1 } ( \mathbb { R } )$

2. f is uniformly continuous.

3. $\operatorname* { l i m } _ { | x | \to \infty } f ( x ) = 0$

Hint:

$$
\chi _ { E \cap ( E + x ) } ( y ) = \chi _ { E } ( y ) \chi _ { E } ( y - x )
$$

## 7.5 5

Let $( X , { \mathcal { M } } , \mu )$ be a measure space. For $f \in L ^ { 1 } ( \mu )$ and $\lambda > 0$ , define

$$
\phi ( \lambda ) = \mu ( \{ x \in X | f ( x ) > \lambda \} ) \quad { \mathrm { ~ a n d ~ } } \quad \psi ( \lambda ) = \mu ( \{ x \in X | f ( x ) < - \lambda \} )
$$

Show that $\phi , \psi$ are Borel measurable and

$$
\int _ { X } | f | ~ d \mu = \int _ { 0 } ^ { \infty } [ \phi ( \lambda ) + \psi ( \lambda ) ] ~ d \lambda
$$

## 7.6 6

Without using the Riesz Representation Theorem, compute

$$
\operatorname* { s u p } \left\{ \left| \int _ { 0 } ^ { 1 } f ( x ) e ^ { x } d x \right| \ \middle | \ f \in L ^ { 2 } ( [ 0 , 1 ] , m ) , \ \| f \| _ { 2 } \leq 1 \right\}
$$

## 8 Fall 2016 (Neil-ish)

## 8.1 1

Define

$$
f ( x ) = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { x } } } .
$$

Show that f converges to a differentiable function on (1, ∞) and that

$$
f ^ { \prime } ( x ) = \sum _ { n = 1 } ^ { \infty } \left( \frac { 1 } { n ^ { x } } \right) ^ { \prime } .
$$

Hint:

$$
\left( { \frac { 1 } { n ^ { x } } } \right) ^ { \prime } = - { \frac { 1 } { n ^ { x } } } \ln n
$$

## 8.2 2

Let $f , g : [ a , b ] \longrightarrow \mathbb { R }$ be measurable with

$$
\int _ { a } ^ { b } f ( x ) \ d x = \int _ { a } ^ { b } g ( x ) \ d x .
$$

Show that either

1. $f ( x ) = g ( x )$ almost everywhere, or

2. There exists a measurable set $E \subset [ a , b ]$ such that

$$
\int _ { E } f ( x ) \ d x > \int _ { E } g ( x ) \ d x
$$

## 8.3 3

Let $f \in L ^ { 1 } ( \mathbb { R } )$ . Show that

$$
\operatorname* { l i m } _ { x \to 0 } \int _ { \mathbb { R } } | f ( y - x ) - f ( y ) | d y = 0
$$

## 8.4 4

Let $( X , { \mathcal { M } } , \mu )$ be a measure space and suppose $\{ E _ { n } \} \subset { \mathcal { M } }$ satisfies

$$
\operatorname* { l i m } _ { n \to \infty } \mu \left( X \backslash E _ { n } \right) = 0 .
$$

Define

$$
G : = \left\{ x \in X \Big \vert x \in E _ { n } \mathrm { ~ f o r ~ o n l y ~ f i n i t e l y ~ m a n y ~ } n \right\} .
$$

Show that $G \in { \mathcal { M } }$ and $\mu ( G ) = 0$

## 8.5 5

Let $\phi \in L ^ { \infty } ( \mathbb { R } )$ . Show that the following limit exists and satisfies the equality

$$
\operatorname* { l i m } _ { n \to \infty } \left( \int _ { \mathbb { R } } \frac { | \phi ( x ) | ^ { n } } { 1 + x ^ { 2 } } d x \right) ^ { \frac { 1 } { n } } = \| \phi \| _ { \infty } .
$$

## 8.6 6

Let $f , g \in L ^ { 2 } ( \mathbb { R } )$ . Show that

$$
\operatorname* { l i m } _ { n  \infty } \int _ { \mathbb { R } } f ( x ) g ( x + n ) d x = 0
$$

## 9 Spring 2015

## 9.1 1

Let $( X , d )$ and $( Y , \rho )$ be metric spaces, $f : X \longrightarrow Y$ , and $x _ { 0 } \in X$

Prove that the following statements are equivalent:

1. For every $\varepsilon > 0 \quad \exists \delta > 0$ such that $\rho ( f ( x ) , f ( x _ { 0 } ) ) < \varepsilon$ whenever $d ( x , x _ { 0 } ) < \delta$

2. The sequence $\{ f ( x _ { n } ) \} _ { n = 1 } ^ { \infty } \longrightarrow f ( x _ { 0 } )$ for every sequence $\left\{ x _ { n } \right\} \longrightarrow x _ { 0 }$ in $X$

## 9.2 2

Let $f : \mathbb { R } \longrightarrow \mathbb { C }$ be continuous with period 1. Prove that

$$
\operatorname* { l i m } _ { N \to \infty } \frac { 1 } { N } \sum _ { n = 1 } ^ { N } f ( n \alpha ) = \int _ { 0 } ^ { 1 } f ( t ) d t \quad \forall \alpha \in \mathbb { R } \setminus \mathbb { Q } .
$$

Hint: show this first for the functions $f ( t ) = e ^ { 2 \pi i k t } { \mathrm { ~ f o r ~ } } k \in \mathbb { Z } .$

## 9.3 3

Let $\mu$ be a finite Borel measure on R and $E \subset \mathbb { R }$ Borel. Prove that the following statements are equivalent:

1. $\forall \varepsilon > 0$ there exists G open and F closed such that

$$
F \subseteq E \subseteq G \quad { \mathrm { a n d } } \quad \mu ( G \setminus F ) < \varepsilon .
$$

2. There exists a $V \in G _ { \delta }$ and $H \in F _ { \sigma }$ such that

$$
H \subseteq E \subseteq V \quad { \mathrm { a n d } } \quad \mu ( V \setminus H ) = 0
$$

## 9.4 4

Define

$$
f ( x , y ) : = { \left\{ \begin{array} { l l } { \displaystyle { \frac { x ^ { 1 / 3 } } { ( 1 + x y ) ^ { 3 / 2 } } } } & { { \mathrm { ~ i f ~ } } 0 \leq x \leq y } \\ { 0 } & { { \mathrm { ~ o t h e r w i s e } } } \end{array} \right. }
$$

Carefully show that $f \in L ^ { 1 } ( \mathbb { R } ^ { 2 } )$

## 9.5 5

Let H be a Hilbert space.

1. Let $x \in \mathcal H$ and $\{ u _ { n } \} _ { n = 1 } ^ { N }$ be an orthonormal set. Prove that the best approximation to x in H by an element in spa $\operatorname { 1 } _ { C } C \left\{ u _ { n } \right\}$ is given by

$$
\widehat { x } : = \sum _ { n = 1 } ^ { N } \langle x , \ u _ { n } \rangle u _ { n } .
$$

2. Conclude that finite dimensional subspaces of H are always closed.

## 9.6 6

Let $f \in L ^ { 1 } ( \mathbb { R } )$ and g be a bounded measurable function on $\mathbb { R } .$ .

1. Show that the convolution $f * g$ is well-defined, bounded, and uniformly continuous on R.

2. Prove that one further assumes that $g \in C ^ { 1 } ( \mathbb { R } )$ with bounded derivative, then $f * g \in C ^ { 1 } ( \mathbb { R } )$ and

$$
{ \frac { d } { d x } } ( f * g ) = f * \left( { \frac { d } { d x } } g \right)
$$

## 10 Fall 2015

## 10.1 1

Define

$$
f ( x ) = c _ { 0 } + c _ { 1 } x ^ { 1 } + c _ { 2 } x ^ { 2 } + \ldots + c _ { n } x ^ { n } { \mathrm { ~ w i t h ~ } } n { \mathrm { ~ e v e n ~ a n d ~ } } c _ { n } > 0 .
$$

Show that there is a number $x _ { m }$ such that $f ( x _ { m } ) \leq f ( x )$ for all $x \in \mathbb { R }$

## 10.2 2

Let f : R −→ R be Lebesgue measurable.

1. Show that there is a sequence of simple functions $s _ { n } ( x )$ such that $s _ { n } ( x ) \longrightarrow f ( x )$ for all $x \in \mathbb { R }$

2. Show that there is a Borel measurable function g such that $g = f$ almost everywhere.

## 10.3 3

Compute the following limit:

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { 1 } ^ { n } { \frac { n e ^ { - x } } { 1 + n x ^ { 2 } } } \ \sin \left( { \frac { x } { n } } \right) \ d x
$$

## 10.4 4

Let $f : [ 1 , \infty ) \longrightarrow \mathbb { R }$ such that $f ( 1 ) = 1$ and

$$
f ^ { \prime } ( x ) = { \frac { 1 } { x ^ { 2 } + f ( x ) ^ { 2 } } }
$$

Show that the following limit exists and satisfies the equality

$$
\operatorname* { l i m } _ { x \to \infty } f ( x ) \leq 1 + { \frac { \pi } { 4 } }
$$

## 10.5 5

Let $f , g \in L ^ { 1 } ( \mathbb { R } )$ be Borel measurable.

1. Show that

• The function

$$
F ( x , y ) : = f ( x - y ) g ( y )
$$

is Borel measurable on $\mathbb { R } ^ { 2 }$ , and

• For almost every $y \in \mathbb { R } .$

$$
F _ { y } ( x ) : = f ( x - y ) g ( y )
$$

is integrable with respect to y.

2. Show that $f \ast g \in L ^ { 1 } ( \mathbb { R } )$ and

$$
\| f \ast g \| _ { 1 } \leq \| f \| _ { 1 } \| g \| _ { 1 }
$$

## 10.6 6

Let $f : [ 0 , 1 ] \longrightarrow \mathbb { R }$ be continuous. Show that

$$
\operatorname* { s u p } \left\{ \| f g \| _ { 1 } ~ { \Big | } ~ g \in L ^ { 1 } [ 0 , 1 ] , ~ \| g \| _ { 1 } \leq 1 \right\} = \| f \| _ { \infty }
$$

## 11 Spring 2014

## 11.1 1

1. Give an example of a continuous $f \in L ^ { 1 } ( \mathbb { R } )$ such that $f ( x ) \longleftrightarrow 0 { \mathrm { ~ a s } } | x | \longrightarrow \infty$

2. Show that if f is uniformly continuous, then

$$
\operatorname * { l i m } | x | \longrightarrow \infty f ( x ) = 0 .
$$

## 11.2 2

Let $\left\{ a _ { n } \right\}$ be a sequence of real numbers such that

$$
\left\{ b _ { n } \right\} \in \ell ^ { 2 } ( \mathbb { N } ) \implies \sum a _ { n } b _ { n } < \infty .
$$

Show that $\sum a _ { n } ^ { 2 } < \infty$

Note: Assume $a _ { n } , b _ { n }$ are all non-negative.

## 11.3 3

Let $f : \mathbb { R } \longrightarrow \mathbb { R }$ and suppose

$$
\forall x \in \mathbb { R } , \quad f ( x ) \geq \operatorname* { l i m } _ { y \to x } f ( y )
$$

Prove that f is Borel measurable.

## 11.4 4

Let $( X , { \mathcal { M } } , \mu )$ be a measure space and suppose f is a measurable function on X. Show that

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { X } f ^ { n } d \mu = { \left\{ \begin{array} { l l } { \infty } & { o r } \\ { \mu ( f ^ { - 1 } ( 1 ) ) , } \end{array} \right. }
$$

and characterize the collection of functions of each type.

## 11.5 5

Let $f , g \in L ^ { 1 } ( [ 0 , 1 ] )$ and for all $x \in [ 0 , 1 ]$ define

$$
F ( x ) : = \int _ { 0 } ^ { x } f ( y ) d y \quad { \mathrm { ~ a n d ~ } } \quad G ( x ) : = \int _ { 0 } ^ { x } g ( y ) d y .
$$

Prove that

$$
\int _ { 0 } ^ { 1 } F ( x ) g ( x ) d x = F ( 1 ) G ( 1 ) - \int _ { 0 } ^ { 1 } f ( x ) G ( x ) d x
$$

## 12 Fall 2014

## 12.1 1

Let $\left\{ f _ { n } \right\}$ be a sequence of continuous functions such that $\sum f _ { n }$ converges uniformly.

Prove that $\sum f _ { n }$ is also continuous.

## 12.2 2

Let I be an index set and $\alpha : I \longrightarrow ( 0 , \infty )$

1. Show that

$$
\sum _ { i \in I } a ( i ) : = \operatorname* { s u p } _ { J \subset I \atop J { \mathrm { f i n i t e } } } \sum _ { i \in J } a ( i ) < \infty \implies I { \mathrm { ~ i s ~ c o u n t a b l e . } }
$$

2. Suppose I = Q and $\sum _ { q \in \mathbb { Q } } a ( q ) < \infty$ . Define

$$
f ( x ) : = \sum _ { { q \in \mathbb { Q } } \atop { q \leq x } } a ( q ) .
$$

Show that f is continuous at $x \iff x \notin \mathbb { Q }$

## 12.3 3

Let $f \in L ^ { 1 } ( \mathbb { R } )$ . Show that

$$
\forall \varepsilon > 0 \exists \delta > 0 { \mathrm { ~ s u c h ~ t h a t ~ } } m ( E ) < \delta \implies \int _ { E } | f ( x ) | d x < \varepsilon
$$

## 12.4 4

Let $g \in L ^ { \infty } ( [ 0 , 1 ] )$ Prove that

$\int _ { [ 0 , 1 ] } f ( x ) g ( x ) d x = 0$ for all continuous $f : [ 0 , 1 ] \longrightarrow \mathbb { R } \implies g ( x ) = 0$ almost everywhere.

## 12.5 5

1. Let $f \in C _ { c } ^ { 0 } ( \mathbb { R } ^ { n } )$ , and show

$$
\operatorname* { l i m } _ { t \to 0 } \int _ { \mathbb { R } ^ { n } } | f ( x + t ) - f ( x ) | d x = 0 .
$$

2. Extend the above result to $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ and show that

$f \in L ^ { 1 } ( \mathbb { R } ^ { n } ) , \ g \in L ^ { \infty } ( \mathbb { R } ^ { n } ) \implies f * g$ is bounded and uniformly continuous.

## 12.6 6

Let $1 \leq p , q \leq \infty$ be conjugate exponents, and show that

$$
f \in L ^ { p } ( \mathbb { R } ^ { n } ) \implies \| f \| _ { p } = \operatorname* { s u p } _ { \| g \| _ { q } = 1 } \left| \int f ( x ) g ( x ) d x \right|
$$