# Real Analysis Qual Prep Week 2: Measure Theory, Fubini Tonelli

D. Zack Garza

## Table of Contents

## Contents

Table of Contents 2   
1 Study Guide 3   
1.1 Convergence Tips/Tricks . 3   
1.2 Measure Theory 5   
1.3 Fubini-Tonelli 8   
2 Qual Problems 13

## 1 Study Guide

References:

• Folland’s “Real Analysis: Modern Techniques”, Ch.1

• Stein and Shakarchi Ch.1, Ch.2

<!-- image-->

## 1.1 Convergence Tips/Tricks

• Our favorite tools: metrics and norms!

A metric on a set X is a function $\rho : X \times X \to [ 0 , \infty )$ such that

$$
\mathbf { \partial } \bullet \rho ( x , y ) = 0 \operatorname { i f f } x = y ;
$$

$\rho ( x , y ) = \rho ( y , x )$ for all $x , y \in X$

$\rho ( x , z ) \le \rho ( x , y ) + \rho ( y , z )$ for all $x , y , z \in X$

– So show things are equal by showing $| x - y | = 0$ . Know the triangle inequality by heart!

• Uniform convergence:

Definition 1.2.7 (Uniform Convergence)

$$
\left( \forall \varepsilon > 0 \right) \left( \exists n _ { 0 } = n _ { 0 } ( \varepsilon ) \right) \left( \forall x \in S \right) \left( \forall n > n _ { 0 } \right) \left( \left| f _ { n } ( x ) - f ( x ) \right| < \varepsilon \right) .
$$

$$
\left( \exists \varepsilon > 0 \right) \left( \forall n _ { 0 } = n _ { 0 } ( \varepsilon ) \right) \left( \exists x = x ( n _ { 0 } ) \in S \right) \left( \exists n > n _ { 0 } \right) \left( | f _ { n } ( x ) - f ( x ) | \geq \varepsilon \right) .
$$

"Slogan: to negate, find a bad x depending on no that are larger than some ε.

– Negating: find a bad $\varepsilon$ and a single bad point x.

– Showing a sum converges uniformly: remember that $\sum _ { k > 1 } a _ { k }$ is defined to be $\operatorname* { l i m } _ { N \to \infty } \sum _ { k \le N } a _ { k }$

So the trick is to define $f _ { n } ( x ) : = \sum _ { k \leq n } a _ { k }$ and then apply the usual criteria above.

– It’s sometimes useful to trade the $\forall x$ in the definition with sup |fn(x) − f (x)| < ε instead. x∈X

• Compare and contrast to pointwise convergence, which is strictly weaker:

Definition 1.2.8 (Pointwise Convergence)

A sequence of functions $\{ f _ { j } \}$ is said to converge pointwise to f if and only if

$$
\left( \forall \varepsilon > 0 \right) \left( \forall x \in S \right) \left( \exists n _ { 0 } = n _ { 0 } ( x , \varepsilon ) \right) \left( \forall n > n _ { 0 } \right) \left( \left| f _ { n } ( x ) - f ( x ) \right| < \varepsilon \right) .
$$

– The main difference: pointwise can depend on the x and the ε, but uniform needs one ε that works for all x simultaneously.

– Note uniform implies pointwise but not conversely.

• The sup norm: $\| f \| _ { \infty } : = \operatorname* { s u p } _ { x \in X } | f _ { n } ( x ) |$

– A useful way to force uniform convergence: bound your sequence uniformly by a sequence that goes to zero:

Proposition 1.4.1(Testing Uniform Convergence: The Sup Norm Test). $f _ { n }  f$ uniformly iff there exists an $M _ { n }$ such that $\left\| f _ { n } - f \right\| _ { \infty } \leq M _ { n } \to 0 .$

• Sups and infs: sup is the least upper bound, inf is the greatest lower bound.

• The p−test:

$$
\sum _ { n \geq 1 } { \frac { 1 } { n ^ { p } } } < \infty \iff p > 1
$$

• Useful fact: convergent sums have small tails, i.e.

$$
\sum _ { n \geq 1 } a _ { n } < \infty \implies \operatorname* { l i m } _ { N \to \infty } \sum _ { n \geq N } a _ { n } = 0
$$

• So try bounding things from above by the tail of a sum!

• If you can’t bound by a tail: as long as you have control over the coefficients, you can pick them to make the sum to converge “fast enough”.

– Example: for a fixed ε, choose $a _ { n } = 1 / 2 ^ { n }$ . Note that $\sum _ { n \geq 1 } 1 / 2 ^ { n } = 1$ , so choose $a _ { n } : = \varepsilon / 2 ^ { n }$

$$
\cdot \cdot \cdot \leq \sum _ { n \geq 1 } a _ { n } : = \sum _ { n \geq 1 } { \frac { \varepsilon } { 2 ^ { n } } } = \varepsilon \to 0
$$

• The $\varepsilon / 3$ trick:

## Theorem 1.4.4(Uniform Limit Theorem).

If $f _ { n }  f$ pointwise and uniformly with each $f _ { n }$ continuous, then f is continuous. a

aSlogan: a uniform limit of continuous functions is continuous.

##

Follows from an $\varepsilon / 3$ argument:

$$
| F ( x ) - F ( y | \le | F ( x ) - F _ { N } ( x ) | + | F _ { N } ( x ) - F _ { N } ( y ) | + | F _ { N } ( y ) - F ( y ) | \le \varepsilon \to 0 .
$$

The first and last $\varepsilon / 3$ come from uniform convergence of $F _ { N } \to F$

The middle $\varepsilon / 3$ comes from continuity of each $F _ { N }$

•So just need to choose N large enough and δ small enough to make all 3 ε bounds hold.

## • The M-test:

Weierstrass M-test. Suppose that $( f _ { n } )$ is a sequence of real- or complex-valued functions defined on a set A, and that there is a sequence of non-negative numbers (Mn) satisfying the conditions

$| f _ { n } ( x ) | \leq M _ { n }$ for all $\iota \geq 1$ and all $x \in A ,$ ,and

$\sum _ { n = 1 } ^ { \infty } M _ { n }$ converges.

Then the series

$$
\sum _ { n = 1 } ^ { \infty } f _ { n } ( x )
$$

converges absolutely and uniformly on A.

## 1.2 Measure Theory

$F _ { \sigma }$ sets: unions of closed sets $( F$ for fermi, French for closed. Sigma for sums, ie unions)

$G _ { \delta }$ sets: intersections of open sets

$\sigma$ algebras: closed under complements, countable intersections, countable unions

• Some of the most useful properties of measures:

Let X be a set equipped with a σ-algebra M.A measure on M (or on (X, M), or simply on X if M is understood) is a function $\mu : { \mathcal { M } } \to [ 0 , \infty ]$ such that

i. . $\mu ( \emptyset ) = 0$

ii. if $\{ E _ { j } \} _ { 1 } ^ { \infty }$ is a sequence of disjoint sets in M, then $\begin{array} { r } { \mu ( \bigcup _ { 1 } ^ { \infty } E _ { j } ) = \sum _ { 1 } ^ { \infty } \mu ( E _ { j } ) } \end{array}$

Property (i is called countable additivity. It implies finite additivity:

1.8 Theorem. Let $( X , { \mathcal { M } } , \mu )$ be a measure space.

a. (Monotonicity) $I f E , F \in { \mathcal { M } }$ and $E \subset F ,$ ,then $\mu ( E ) \leq \mu ( F )$

b. (Subadditivity) $I f \{ E _ { j } \} _ { 1 } ^ { \infty } \subset \mathbb { M } ,$ then $\begin{array} { r } { \mu ( \bigcup _ { 1 } ^ { \infty } E _ { j } ) \leq \sum _ { 1 } ^ { \infty } \mu ( E _ { j } ) . } \end{array}$

c. (Continuity from below) If $\{ E _ { j } \} _ { 1 } ^ { \infty } \subset \mathcal { M }$ and $E _ { 1 } ~ \subset ~ E _ { 2 } ~ \subset ~ \cdots ,$ , then $\mu ( \cup _ { 1 } ^ { \infty } E _ { j } ) = \operatorname* { l i m } _ { j \to \infty } \mu ( E _ { j } )$

d.(Continuity from above) If $\{ E _ { j } \} _ { 1 } ^ { \infty } \subset { \mathcal { M } } , E _ { 1 } \supset E _ { 2 } \supset \cdot \cdot \cdot , a n d \mu ( E _ { 1 } ) < \infty ,$ then $\begin{array} { r } { \mu ( \bigcap _ { 1 } ^ { \infty } E _ { j } ) = \operatorname* { l i m } _ { j \longrightarrow \infty } \mu ( E _ { j } ) } \end{array}$

• The proof of continuity of measure contains a very useful trick: replace a sequence of sets $\{ E _ { k } \}$ with a sequence of disjoint sets that either union or intersect to the same thing.

– Example: if $A _ { 1 } \subseteq A _ { 2 } \subseteq \cdots$ · ·, set $F _ { 1 } = A _ { 1 }$ and $F _ { k } = A _ { k } \backslash A _ { k - 1 }$ for $k \geq 2$ Then [ A k = a F k . k≥1 k≥1

• Occasionally you need some properties of outer measures:

containing E, tne inner area of E is just tne area of R minus tne outer area of $\kappa \backslash E$

The abstract generalization of the notion of outer area is as follows.An uter measure on a nonempty set X is a function $\mu ^ { * } : { \mathcal { P } } ( X ) \to [ 0 , \infty ]$ that satisfies

$\mu ^ { * } ( \varnothing ) = 0 ,$

$\mu ^ { * } ( A ) \leq \mu ^ { * } ( B ) { \mathrm { ~ i f ~ } } A \subset B ,$

$\begin{array} { r } { \mu ^ { * } ( \bigcup _ { 1 } ^ { \infty } A _ { j } ) \leq \sum _ { 1 } ^ { \infty } \mu ^ { * } ( A _ { j } ) . } \end{array}$

The most common wav to obtain outer measures is to start with a familv E. of

1.10 Proposition. Let $\mathcal E \subset \mathcal P ( X )$ and $\rho : { \mathcal { E } }  [ 0 , \infty ]$ be such that $\varnothing \in { \mathcal { E } } , X \in { \mathcal { E } } ,$ and $\rho ( { \emptyset } ) = 0 .$ For any $A \subset X$ ,define

$$
\mu ^ { * } ( A ) = \operatorname* { i n f } \Big \{ \sum _ { 1 } ^ { \infty } \mu ( E _ { j } ) : E _ { j } \in \mathcal { E } \mathrm { ~ } a n d A \subset \bigcup _ { 1 } ^ { \infty } E _ { j } \Big \} .
$$

Then $\mu ^ { * }$ is an outer measure.

• Outer measure for $\mathbb { R } ^ { n }$ : you consider all collections of cubes that cover your set, sum up their

volumes, and take the infimum over all such collections:

Definition 1.2.9 (Outer Measure)

The outer measure of a set is given by

$$
m _ { * } ( E ) : = \operatorname * { i n f } _ { \{ Q _ { i } \} \to E \atop \mathrm { c l o s e d ~ c u b e s } } \sum \vert Q _ { i } \vert .
$$

• ${ } ^ { 6 } \mathrm { A } { } \cdot$ lmost everywhere $b l a h ^ { \prime \prime }$ : the set where blah does not happen has measure zero.

• “Infinitely many/all but finitely many” types of sets, which show up in Borel-Cantelli style problems

and likewise for unions and intersections. In this situation, the notions of limit superior and limit inferior are sometimes useful:

$$
\operatorname* { l i m } \operatorname* { s u p } E _ { n } = \bigcap _ { k = 1 } ^ { \infty } \bigcup _ { n = k } ^ { \infty } E _ { n } , \qquad \operatorname* { l i m } \operatorname* { i n f } E _ { n } = \bigcup _ { k = 1 } ^ { \infty } \bigcap _ { n = k } ^ { \infty } E _ { n } .
$$

The reader may verify that

lim sup $E _ { n } = \{ x : x \in E _ { n }$ for infinitely many $n \}$

lim inf $E _ { n } = \{ x : x \in E _ { n }$ for all but finitely many }.

$$
\begin{array} { r } { \ v { x } } \\ { \ v { x } } \end{array} = \ v { x } \ \backslash \ \ v { x } .
$$

In this situation we have deMorgan's laws:

$$
{ \biggl ( } \bigcup _ { \alpha \in A } E _ { \alpha } { \biggr ) } ^ { c } = \bigcap _ { \alpha \in A } E _ { \alpha } ^ { c } , \qquad { \biggl ( } \bigcap _ { \alpha \in A } E _ { \alpha } { \biggr ) } ^ { c } = \bigcup _ { \alpha \in A } E _ { \alpha } ^ { c } .
$$

• Lemmas that sometimes show up on quals:

1.18 Theorem. If $E \in \mathcal { M } _ { \mu } ,$ , then

$$
\begin{array} { r l r } & { } & { \mu ( E ) = \operatorname* { i n f } \{ \mu ( U ) : U \supset E a n d U i s o p e n \} } \\ & { } & { = \operatorname* { s u p } \{ \mu ( K ) : K \subset E a n d K i s c o m p a c t \} . } \end{array}
$$

1.19 Theorem. $H E \subset \mathbb { R } ,$ , the following are equivalent.

a. $E \in \mathcal { M } _ { \mu } .$

b. $E = V \setminus N _ { 1 }$ where V is a $G _ { \delta }$ set and $\mu ( N _ { 1 } ) = 0 .$

c. $E = H \cup N _ { 2 }$ where H is an $F _ { \sigma }$ set and $\mu ( N _ { 2 } ) = 0 .$

## 1.3 Fubini-Tonelli

Quick statement:

Theorem 3.1.10(Tonelli (Non-Negative, Measurable)).

For $f ( x , y )$ non-negative and measurable, for almost every $x \in \mathbb { R } ^ { n }$

$f _ { x } ( y )$ is a measurable function

$F ( x ) = \int f ( x , y )$ dy is a measurable function,

• For E measurable, the slices $E _ { x } : = \left\{ y \biggm | ( x , y ) \in E \right\}$ are measurable.

$\int f = \int \int F ,$ i.e. any iterated integral is equal to the original.

Theorem 3.1.11(Fubini (Integrable)).

For $f ( x , y )$ integrable, for almost every $x \in \mathbb { R } ^ { n }$

$f _ { x } ( y )$ is an integrable function

$F ( x ) : = \int f ( x , y )$ dy is an integrable function,

• For E measurable, the slices $E _ { x } : = \left\{ y \Big | ( x , y ) \in E \right\}$ are measurable.

Explained in Stein and Shakarchi (Fubini, which requires integrability)

interesting issues arise.

In general, we may write $\mathbb { R } ^ { d }$ as a product

$$
\mathbb { R } ^ { d } = \mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } } \qquad \mathrm { w h e r e } \ d = d _ { 1 } + d _ { 2 } , \mathrm { a n d } \ d _ { 1 } , d _ { 2 } \geq 1 .
$$

A point in $\mathbb { R } ^ { d }$ then takes the form $( x , y )$ , where $\boldsymbol { x } \in \mathbb { R } ^ { d _ { 1 } }$ and $\boldsymbol { y } \in \mathbb { R } ^ { d _ { 2 } }$ With such a decomposition of $\mathbb { R } ^ { d }$ in mind, the general notion of a slice, formed by fixing one variable, becomes natural. If f is a function in $\mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }$ , the slice of f corresponding to $\boldsymbol { y } \in \mathbb { R } ^ { d _ { 2 } }$ is the function f  of the $\boldsymbol { x } \in \mathbb { R } ^ { d _ { 1 } }$ variable, given by

$$
f ^ { y } ( x ) = f ( x , y ) .
$$

Similarly, the slice of f for a fixed $\boldsymbol { x } \in \mathbb { R } ^ { d _ { 1 } }$ is $f _ { x } ( y ) = f ( x , y )$ In the case of a set $E \subset \mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }$ we define its slices by

$$
E ^ { y } = \{ x \in \mathbb { R } ^ { d _ { 1 } } : ~ ( x , y ) \in E \} ~ \mathrm { a n d } ~ E _ { x } = \{ y \in \mathbb { R } ^ { d _ { 2 } } : ~ ( x , y ) \in E \} .
$$

See Figure 1 for an illustration.

<!-- image-->  
Figure 1. Slices $E ^ { y }$ $E _ { x }$

The main theorem is as follows. We recall that by definition all integrable functions are measurable.

Theorem 3.1 Suppose $f ( x , y )$ is integrable on $\mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }$ . Then for almost every $\boldsymbol { y } \in \mathbb { R } ^ { d _ { 2 } } :$

(i) The slice fy is integrable on $\mathbb { R } ^ { d _ { 1 } } .$

(ii) The function defined by JRd1 f y(x) dx is integrable on Rd2.

Moreover:

$$
( { \mathrm { i i i } } ) \int _ { \mathbb { R } ^ { d _ { 2 } } } \left( \int _ { \mathbb { R } ^ { d _ { 1 } } } f ( x , y ) d x \right) d y = \int _ { \mathbb { R } ^ { d } } f .
$$

<!-- image-->

Clearly, the theorem is symmetric in x and y so that we also may conclude that the slice $f _ { x }$ is integrable on $\mathbb { R } ^ { d _ { 2 } }$ for a.e. x. Moreover, $\int _ { \mathbb { R } ^ { d _ { 2 } } } f _ { x } ( y ) d y$ is integrable, and

<!-- image-->

In particular, Fubini's theorem states that the integral of f on $\mathbb { R } ^ { d }$ can be computed by iterating lower-dimensional integrals, and that the iterations can be taken in any order

<!-- image-->

And Tonelli, which only requires measurability:

Theorem 3.2 Suppose $f ( x , y )$ is a non-negative measurable function on $\mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }$ $\boldsymbol { y } \in \mathbb { R } ^ { d _ { 2 } }$

<!-- image-->

$f ^ { y }$ is measurable on $\mathbb { R } ^ { d _ { 1 } }$

(ii) The function defined by $\int _ { \mathbb { R } ^ { d _ { 1 } } } f ^ { y } ( x )$ dx is measurable on $\mathbb { R } ^ { d _ { 2 } }$

Moreover:

$\int _ { \mathbb R ^ { d _ { 2 } } } \left( \int _ { \mathbb R ^ { d _ { 1 } } } f ( x , y ) d x \right) d y = \int _ { \mathbb R ^ { d } } f ( x , y )$ dx dy in the extended sense.

In practice, this theorem is often used in conjunction with Fubini's theorem.3 Indeed, suppose we are given a measurable function f on $\mathbb { R } ^ { d }$ and asked to compute $\int _ { \mathbb { R } ^ { d } } f .$ . To justify the use of iterated integration, we first apply the present theorem to |f ]. Using it, we may freely compute (or estimate) the iterated integrals of the non-negative function |f l. If these are finite, Theorem 3.2 guarantees that f is integrable, that is, $\textstyle \int \left| f \right| < \infty .$ Then the hypothesis in Fubini's theorem is verified, and we may use that theorem in the calculation of the integral of f.

A more precise statement from Folland:

In this section we fix a measure space $( X , { \mathcal { M } } , \mu )$ , and we define

L+ = the space of all measurable functions from X to $[ 0 , \infty ]$

2.37 The Fubini-Tonelli Theorem. Suppose that $( X , { \mathcal { M } } , \mu )$ and $( Y , \mathcal { N } , \nu )$ are $\varpi =$ finite measure spaces.

a. (Tonelli) $I f f \in L ^ { + } ( X \times Y )$ , then the functions $g ( x ) = \textstyle \int f _ { x }$ dν and $h ( y ) =$ ∫f dμ are in $L ^ { + } ( X )$ and ${ \dot { L } } ^ { + } ( Y )$ , respectively, and

$$
\begin{array} { r } { \int f d ( \mu \times \nu ) = \displaystyle \int \left[ \int f ( x , y ) d \nu ( y ) \right] d \mu ( x ) } \\ { = \displaystyle \int \left[ \int f ( x , y ) d \mu ( x ) \right] d \nu ( y ) . } \end{array}\tag{2.38}
$$

b. (Fubini) If $f \in L ^ { 1 } ( \mu \times \nu )$ , then $f _ { x } \in L ^ { 1 } ( \nu )$ for a.e. $x \in X , f ^ { y } \in L ^ { 1 } ( \mu )$ for a.e. $y \in Y ,$ , the a.e.-defined functions $g ( x ) = \int f _ { x }$ dv and $h ( x ) = \textstyle \int f ^ { y }$ dv are in $L ^ { 1 } ( \mu )$ and $L ^ { 1 } ( \nu )$ , respectively, and (2.38) holds.

Some things that qual questions are commonly based on:

Corollary 3.3 If E is a measurable set in $\mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }$ , then for almost every $\boldsymbol { y } \in \mathbb { R } ^ { d _ { 2 } }$ the slice

$$
E ^ { y } = \{ x \in \mathbb { R } ^ { d _ { 1 } } : ( x , y ) \in E \}
$$

is a measurable subset $o f \mathbb { R } ^ { d _ { 1 } }$ . Moreover $m ( E ^ { y } )$ is a measurable function of y and

$$
m ( E ) = \int _ { \mathbb { R } ^ { d _ { 2 } } } ( m ( E ^ { y } ) d y .
$$

This is an immediate consequence of the first part of Theorem 3.2 applied to the function $\chi _ { E }$ . Clearly a symmetric result holds for the x-slices in $\mathbb { R } ^ { d _ { 2 } }$

We have thus established the basic fact that if E is measurable on $\mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }$ , then for almost every $\boldsymbol { y } \in \mathbb { R } ^ { d _ { 2 } }$ the slice $E ^ { y }$ is measurable in $\mathbb { R } ^ { d _ { 1 } }$ (and also the symmetric statement with the roles of x and y interchanged). One might be tempted to think that the converse assertion holds. To see that this is not the case, note that if we let $\mathcal { N }$ denote a

Corollary 3.8 Suppose f (x) is a non-negative function on Rd, and let

$$
\mathcal { A } = \{ ( x , y ) \in \mathbb { R } ^ { d } \times \mathbb { R } : 0 \leq y \leq f ( x ) \} .
$$

Then:

(i) f is measurable on Rd if and only if A is measurable in Rd+1.

(ii) If the conditions in (i) hold, then

$$
\int _ { \mathbb R ^ { d } } f ( x ) d x = m ( \mathcal A ) .
$$

Proof. If f is measurable on $\mathbb { R } ^ { d }$ , then the previous proposition guarantees that the function

$$
F ( x , y ) = y - f ( x )
$$

is measurable on $\mathbb { R } ^ { d + 1 }$ , so we immediately see that $\mathcal { A } = \{ y \geq 0 \} \cap \{ F \leq$ 0} is measurable.

Conversely, suppose that A is measurable. We note that for each $\boldsymbol { x } \in \mathbb { R } ^ { d _ { 1 } }$ the slice $\mathcal { A } _ { x } = \{ y \in \mathbb { R } : ( x , y ) \in \mathcal { A } \}$ is a closed segment, namely $\mathcal { A } _ { x } = [ 0 , f ( x ) ]$ Consequently Corollary 3.3 (with the roles of x and y interchanged) yields the measurability of $m ( \mathcal { A } _ { x } ) = f ( x )$ . Moreover

$$
m ( A ) = \int \chi _ { A } ( x , y ) d x d y = \int _ { \mathbb { R } ^ { d _ { 1 } } } m ( A _ { x } ) d x = \int _ { \mathbb { R } ^ { d _ { 1 } } } f ( x ) d x ,
$$

as was to be shown.

## 2 Qual Problems

Spring 2012 #4

4. Let $f : \mathbb { R } \to \mathbb { R }$ be a nonnegative integrable function.

a. Show that sin of is integrable.

b. Use Fubini's theorem to show that

$$
\int _ { [ 0 , \infty ) } { m ( \{ x : f ( x ) \geq y \} ) \cos y d y } = \int _ { \mathbb { R } } \sin ( f ( x ) ) d x .
$$

Fall 2016 $\# 2$

2. Let f and g be real valued measurable functions on $[ a , b ]$ with $\textstyle \int _ { a } ^ { b } f ( x ) d x = \int _ { a } ^ { b } g ( x )$ Show that either $f ( x ) = g ( x )$ a.e., or there exists measurable subset E of $[ a , b ]$ such that $\textstyle \int _ { E } f ( x ) \ d x > \int _ { E } g ( x )$ dx.

Fall 2018 #5

Problem 5. Let $f \geq 0$ be a Lebesgue measurable function on $\mathbb { R }$ . Show that

$$
\int _ { \mathbb { R } } f = \int _ { 0 } ^ { \infty } m ( \{ x : f ( x ) > t \} ) d t .
$$

Spring 2019 $\# 4 \colon$ This is an expanded version of Fall 2018 $\# 5$ above.

4. Let f be a non-negative function on $\mathbb { R } ^ { n }$ and $\mathcal { A } = \{ ( x , t ) \in \mathbb { R } ^ { n } \times \mathbb { R } : 0 \leq t \leq f ( x ) \}$

Prove the validity of the following two statements:

(a) f is a Lebesgue measurable function on $\mathbb { R } ^ { n } \iff \ A$ is a Lebesgue measurable subset of $\mathbb { R } ^ { n + 1 }$

(b) If f is a Lebesgue measurable function on $\mathbb { R } ^ { n }$ , then

$$
m ( A ) = \int _ { \mathbb { R } ^ { n } } f ( x ) d x = \int _ { 0 } ^ { \infty } m ( \{ x \in \mathbb { R } ^ { n } : f ( x ) \geq t \} ) d t
$$