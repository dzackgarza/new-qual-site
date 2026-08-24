---
schema: qual/card@1
id: P-3A7RU
kind: problem
title: "Question 2.4"
classification:
  areas:
  - real-analysis
  topics: []
solved: false
relations: []
---

Question 2.4. Show that the punctured unit disk $\{ z \ : \ 0 < \ | z | < 1 \}$ and the annulus $\{ z : 1 < | z | < 2 \}$ cannot be conformally equivalent.

Name:

Date:

## Problem 1

Let $I = [ 0 , 1 ]$ and for $n \in \mathbb { N } .$ , consider $0 \leq j \leq 2 ^ { n } - 1$ . Define

$$
I _ { n j } = [ j 2 ^ { - n } , ( j + 1 ) 2 ^ { - n } ] .
$$

Let $f \in L ^ { 1 } ( I )$ and define

$$
E _ { n } ( f ) ( x ) = \sum _ { j = 0 } ^ { 2 ^ { n } - 1 } { \Big ( } 2 ^ { n } \int _ { I _ { n j } } f d t { \Big ) } \chi _ { I _ { n j } } ( x ) .
$$

Prove that li $\mathrm { a } _ { n  \infty } E _ { n } ( f ) ( x ) = f ( x )$ a.e. in I .

## Problem 2

Prove that the unit ball of $L ^ { 2 }$ endowed with its natural strong topology is not compact.

## Problem 3

Prove that a normed vector space (X, k.k) is Banach if and only if every normally (sometimes called also absolutely) convergent series is convergent.

## Problem 4

Suppose that $f , g$ are entire functions with $| f ( z ) | \leq | g ( z ) |$ for all $z \in \mathbb { C }$ . Prove that there is a constant $c \in \mathbb { C }$ such that $f = c g$

## Problem 5

This problem is about the integral

$$
I = \int _ { - \infty } ^ { \infty } { \frac { \sin { x } } { x } } d x .
$$

• Show directly that I is a convergent improper Riemann integral.

• Use a contour integral to evaluate I.

## Problem 6

Let $f$ and $g$ be functions holomorphic defined on a domain $U \subseteq \mathbb { C } .$ . Set $\varphi ( z ) = | f ( z ) | + | g ( z ) |$ for $z \in U$ . If $\varphi$ assumes a maximum value on $U ,$ show that both f and g are constants on U.

## Problem 7

Let $U \subseteq \mathbb { C }$ be an open set and

$$
A ^ { 2 } ( U ) = \{ f { \mathrm { ~ h o m o l o r p h i c ~ o n ~ } } U : \int _ { U } | f ( z ) | ^ { 2 } d x d y < \infty \} .
$$

Define

$$
( f , g ) = \int _ { U } f ( z ) { \overline { { g ( z ) } } } d x d y , \quad \forall f , g \in A ^ { 2 } ( U ) .
$$

Prove that $A ^ { 2 } ( U )$ is a Hilbert space when equipped with this inner product.

Name: Date:

## Problem 1

Let $I = [ 0 , 1 ]$ and for $n \in \mathbb { N } .$ , consider $0 \leq j \leq 2 ^ { n } - 1$ . Define

$$
I _ { n j } = [ j 2 ^ { - n } , ( j + 1 ) 2 ^ { - n } ] .
$$

Let $f \in L ^ { 1 } ( I )$ and define

$$
E _ { n } ( f ) ( x ) = \sum _ { j = 0 } ^ { 2 ^ { n } - 1 } { \Big ( } 2 ^ { n } \int _ { I _ { n j } } f d t { \Big ) } \chi _ { I _ { n j } } ( x ) .
$$

Prove that lim $1 _ { n \to \infty } E _ { n } ( f ) ( x ) = f ( x )$ a.e. in I .

## Problem 2

Let $L ^ { 2 } = L ^ { 2 } ( \mathbb R ^ { d } )$ be the real Hilbert space endowed with its natural norm k.k derived from the real inner product $( f , g ) = \textstyle \int f g$ dm (where dm is Lebesgue measure on $\mathbb { R } ^ { d } )$ . We say that $f _ { n } \in L ^ { 2 }$ converges weakly to $f \ \operatorname { i f } \ ( f _ { n } , g )  ( f , \overbrace { g } )$ for every $g \in L ^ { 2 }$

• Prove that if $f _ { n }$ converges weakly to f and $\| f _ { n } \| \to \| f \|$ then $f _ { n }$ converges to $f$ in the strong topology.

• Prove that there exists a sequence of bounded functions in $L ^ { 2 }$ which is not converging in $L ^ { 2 }$ but weakly converging up to a subsequence possibly. What do you conclude on the unit ball of $L ^ { 2 }$ endowed with the strong topology ?

## Problem 3

Let $I = [ 0 , 1 ]$ and denote $\| . \| _ { p }$ the p-norm $\begin{array} { r } { \| f \| _ { p } = \bigg ( \int _ { I } | f | ^ { p } \bigg ) ^ { 1 / p } } \end{array}$ for $1 \leq p < \infty$ (we admit this is a norm) and $\| f \| _ { \infty } = \csc \operatorname* { s u p } | f |$

• Show that the space of continuous functions on I endowed with the norm $\| . \| _ { p }$ for $1 \leq p < \infty$ is not a Banach space.

• Prove that the space of (Lebesgue) measurable functions on I such that their p-norm is finite is a Banach space for $1 \leq p \leq \infty$

• Prove that there is no smooth function h such that $f * h = f$ for every $f \in L ^ { 1 } ( I )$

• Prove the H¨older inequality: for $p , q \geq 1$ such that $\textstyle { \frac { 1 } { p } } + { \frac { 1 } { q } } = 1$

$$
\int _ { I } f g \leq \| f \| _ { p } \| g \| _ { q }
$$

One can use the inequality $\textstyle a b \leq { \frac { a ^ { p } } { p } } + { \frac { a ^ { q } } { q } }$ for any $a , b \geq 0$

• Deduce the Young inequality: $L ^ { p } * L ^ { q } \subset L ^ { r }$ for $\begin{array} { r } { \frac { 1 } { p } + \frac { 1 } { q } = 1 + \frac { 1 } { r } } \end{array}$

## Problem 4

Let f be an entire function. Suppose that for each $z _ { 0 } \in \mathbb { C }$ , the power series expansion

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } ( z - z _ { 0 } ) ^ { n }
$$

has at least one coefficient $c _ { n } = 0$ . Show that f is a polynomial.

## Problem 5

Let U be an open subset of C. Let $z _ { \mathrm { 0 } }$ be a point in U, and suppose that f is a meromorphic function on U with a pole at $z _ { \mathrm { 0 } }$ . Prove that there is no holomorphic function $g : U \setminus \{ z _ { 0 } \}  \mathbb { C }$ such that $e ^ { g ( z ) } = f ( z )$ for all $z \in U \setminus \{ z _ { 0 } \}$

## Problem 6

Suppose f is holomorphic in an annulus $r < | z | < R ,$ and there exists a sequence of holomorphic polynomials $p _ { n }$ converging to f uniformly on compact subset of the annulus. Show that f can be extended to the disc $\{ | z | < R \}$ as a holomorphic function.

## Problem 7

Let U be an open subset of C. We use the notion

$$
\| f \| _ { L ^ { 2 } ( U ) } = \left( \int _ { U } | f | ^ { 2 } d x d y \right) ^ { 1 / 2 } .
$$

• Let $f : U \to \mathbb { C }$ be a holomorphic function. Show that for any compact set $K \subset U$ , there is a constant $C _ { K } .$ , such that

$$
\operatorname* { s u p } _ { z \in K } | f ( z ) | \leq C _ { K } \| f \| _ { L ^ { 2 } ( U ) } .
$$

• Prove that {f is holomorphic on $U : \| f \| _ { L ^ { 2 } ( U ) } \leq 1 \}$ is a normal family.

• Suppose U is the punctured disc $D ( 0 , 1 ) - \{ 0 \}$ . If f is holomorphic on U and $\| f \| _ { L ^ { 2 } ( U ) } < \infty$ , prove that $z = 0$ is a removable singularity of f .
