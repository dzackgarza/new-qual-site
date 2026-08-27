# Theorems Real Analysis

## Joshua Ruiter

## 1 Chapter 1

## 1.1 Topology

Theorem 1.1. The closure of a set is a closed set.

Theorem 1.2. A set is closed if and only if it contains all of its limit points.

Theorem 1.3 (Heine-Borel). A subset of $\mathbb { R } ^ { n }$ is compact if and only if it is both closed and bounded.

Theorem 1.4. In a metric space, sequential compactness is equivalent to compactness.

## 1.2 Rectangles in $\mathbb { R } ^ { d }$

Theorem 1.5. If a rectangle is the almost disjoint union of finitely many other rectangles, then the volume is the sum of the volumes. Symbolically, if $\textstyle R = \bigcup _ { k = 1 } ^ { N } R _ { k }$ , then

$$
| R | = \sum _ { k = 1 } ^ { N } | R _ { k } |
$$

Theorem 1.6. If a rectangle R is contained in a union of rectangles, then the volume of R does not exceed the sum of the volumes. Symbolically, if $R , R _ { 1 } , \ldots R _ { N }$ are rectangles such that $R \subset \textstyle \bigcup _ { k = 1 } ^ { N } R _ { k }$ then

$$
| R | \leq \sum _ { k = 1 } ^ { N } | R _ { k } |
$$

Theorem 1.7. Any collection of disjoint open intervals in R is countable.

Proof. Let $\{ I _ { \alpha } \} _ { \alpha \in A }$ be a collection of disjoint open intervals. Each $I _ { \alpha }$ is nontrivial, so there is a rational $q _ { \alpha } \in I _ { \alpha }$ . Thus we have $q _ { \alpha }$ distinct rational numbers, since the $I _ { \alpha } { ' } \mathrm { s }$ are disjoint. There cannot be more than a countable number of rationals, so A is countable. □

Theorem 1.8. Every open subset $\mathcal { O } \subset \mathbb { R }$ can be written uniquely as a countable union of disjoint open intervals.

Theorem 1.9. Every open set $\mathcal { O } \subset \mathbb { R } ^ { d }$ can be written as a countable union of almost disjoint closed cubes.

Theorem 1.10. The Cantor middle-thirds set is compact, totally disconnected, and perfect.

## 1.3 Exterior Lebesgue Measure

Theorem 1.11. The exterior measure of a rectangle is equal to is volume.

Theorem 1.12. The exterior measure of $\mathbb { R } ^ { d }$ is infinite.

Theorem 1.13. The exterior measure of the Cantor (middle-thirds) set is zero.

Theorem 1.14. Let $E \subset \mathbb { R } ^ { d }$ . For $\epsilon > 0$ , there exists a covering $E \subset | \cup _ { j = 1 } ^ { \infty } Q _ { j }$ such that

$$
\sum _ { j = 1 } ^ { \infty } | Q _ { j } | \leq m _ { * } ( E ) + \epsilon
$$

Theorem 1.15. The exterior measure of a subset does not exceed the exterior measure of the containing set. Symbolically,

$$
E _ { 1 } \subset E _ { 2 } \implies m _ { * } ( E _ { 1 } ) \leq m _ { * } ( E _ { 2 } )
$$

Theorem 1.16. Exterior measure is countably sub-additive. Symbolically,

$$
E = \bigcup _ { j = 1 } ^ { \infty } E _ { j } \implies m _ { * } ( E ) \leq \sum _ { j = 1 } ^ { \infty } m _ { * } ( E _ { j } )
$$

Theorem 1.17. The exterior measure of E is equal to the infimum over the exterior measures of all open sets containing E. Symbolically,

$$
m _ { * } ( E ) = \operatorname* { i n f } \{ m _ { * } ( \mathcal { O } ) : E \subset \mathcal { O } \ a n d \mathcal { O } \ i s \ o p e n \}
$$

Theorem 1.18. If two sets have positive distance from each other, then the exterior measure of the union is the sum of the exterior measures. Symbolically,

$$
d ( E _ { 1 } , E _ { 2 } ) < 0 \implies m _ { * } ( E _ { 1 } \cup E _ { 2 } ) = m _ { * } ( E _ { 1 } ) + m _ { * } ( E _ { 2 } )
$$

Theorem 1.19. The exterior measure of a countable union of almost disjoint cubes is equal to the sum of the measures of the cubes. Symbolically, if $\{ Q _ { j } \} _ { j = 1 } ^ { \infty }$ is a collection of almost disjoint cubes, then

$$
m _ { * } \left( \bigcup _ { j = 1 } ^ { \infty } Q _ { j } \right) = \sum _ { j = 1 } ^ { \infty } | Q _ { j } |
$$

## 1.4 Lebesgue Measurable Sets

Theorem 1.20. Open and closed sets in $\mathbb { R } ^ { d }$ are measurable.

Theorem 1.21. Any set with exterior measure zero is measurable, and has measure zero. More generally, any subset of a set of exterior measure zero is measurable and has measure zero. Symbolically,

$$
m _ { * } ( E ) = 0 \ a n d \ F \subset E \implies m ( F ) = 0
$$

In other words, Lebesgue measure is complete. (See chapter 6 for definition of complete.)

Theorem 1.22. The collection of measurable subsets of $\mathbb { R } ^ { d }$ forms a σ-algebra. That is, countable unions and intersections of measurable sets are measurable and the complement of a measurable set is measurable.

Theorem 1.23. The distance between a disjoint pair of a closed and a compact set is positive. Symbolically, if F is closed, K is compact, and $F \cap K = \emptyset$ , then $d ( F , K ) > 0$

Theorem 1.24. Lebesgue measure is σ-additive. That is, the measure of a countable union of disjoint measurable sets is the sum of the measures. Symbolically, if $\{ E _ { n } \} _ { n = 1 } ^ { \infty }$ is a collection of disjoint measurable sets, then

$$
m \left( \bigcup _ { n = 1 } ^ { \infty } E _ { n } \right) = \sum _ { n = 1 } ^ { \infty } m ( E _ { n } )
$$

Theorem 1.25. The measure of the limit of an increasing sequence of measurable sets is the limit of the measures of the sets. Symbolically,

$$
E _ { n } \nearrow E \implies m ( E ) = \operatorname* { l i m } _ { n  \infty } m ( E _ { n } )
$$

where each $E _ { n }$ is assumed to be measurable.

Theorem 1.26. The measure of the limit of a decreasing sequence of measurable sets is the limit of the measures of the sets, provided that the limit sets eventually have finite measure. Symbolically,

$$
E _ { n } \searrow E a n d \exists k \ s u c h \ t h a t \ m ( E _ { k } ) < \infty \implies m ( E ) = \operatorname* { l i m } _ { n \to \infty } m ( E _ { n } )
$$

where each $E _ { n }$ is assumed to be measurable. (Note that if there is some k such that $m ( E _ { k } ) <$ ∞, then every $E _ { k + j }$ also has finite measure.)

Theorem 1.27 (Borel-Cantelli Lemma). Let $\{ E _ { k } \} _ { k = 1 } ^ { \infty }$ be a countable family of measurable subsets $o f \mathbb { R } ^ { d }$ such that $\begin{array} { r } { \sum _ { k } m ( E _ { k } ) < \infty } \end{array}$ , and let $\begin{array} { r } { E = \operatorname* { l i m } \operatorname* { s u p } _ { k \to \infty } E _ { k } = \bigcap _ { n } \bigcup _ { k > n } E _ { k } } \end{array}$ . Then $m ( E ) = 0$

Theorem 1.28 (Theorem 3.4 and Exercise 26). Let $E \subset \mathbb { R } ^ { d }$ . The following are equivalent:

1. E is measurable.

2. For every $\epsilon > 0$ , there exists an open set O such that $E \subset { \mathcal { O } }$ and $m ( { \mathcal { O } } \backslash E ) < \epsilon$

3. For every $\epsilon > 0$ , there exists a closed set F such that $F \subset E$ and $m ( E \setminus F ) < \epsilon$

Theorem 1.29. Let $E \subset \mathbb { R } ^ { d }$ be measurable with $m ( E ) < \infty$ . Then for $\epsilon > 0$

1. There exists a compact set K with $K \subset E$ and $m ( E \setminus K ) < \epsilon$

2. There exists a finite union $\textstyle F = \bigcup _ { j = 1 } ^ { N } Q _ { j }$ of closed cubes such that $m ( E { \triangle } F ) < \epsilon$

Theorem 1.30 (Invariance Properties of Lebesgue Measure). Lebesgue measure is translation invariant, relatively dilation invariant, and reflection invariant. Symbolically, for $E \subset \mathbb { R } ^ { d } , h \in \mathbb { R } ^ { d } , \delta > 0$ ,

$$
\begin{array} { c } { { m ( E + h ) = m ( E ) } } \\ { { m ( \delta E ) = \delta ^ { d } m ( E ) } } \\ { { m ( - E ) = m ( E ) } } \end{array}
$$

More generally, if $\boldsymbol { \delta } = ( \delta _ { 1 } , \dots , \delta _ { d } )$ is a d-tuple of positive real numbers then

$$
m ( \delta E ) = ( \delta _ { 1 } \dots \delta _ { d } ) m ( E )
$$

Theorem 1.31. Let $E \subset \mathbb { R } ^ { d }$ be measureable and $L : \mathbb { R } ^ { d } \to \mathbb { R } ^ { d } \ a$ linear transformation.   
Then $L ( E )$ is measurable.

Theorem 1.32. Let B be a ball in $\mathbb { R } ^ { d }$ with radius r. Then $m ( B ) = v _ { d } r ^ { d }$ where $v _ { d }$ is the measure of the unit ball centered at the origin.

Theorem 1.33. $G _ { \delta }$ sets and $F _ { \sigma }$ sets are Borel sets.

Theorem 1.34. Let $E \subset \mathbb { R } ^ { d }$ . The following are equivalent:

1. E is measurable.

2. There exists $G \in G _ { \delta }$ such that $m ( E \setminus G ) = 0$

3. There exists $F \in F _ { \sigma }$ such that $m ( E \setminus F ) = 0$

Theorem 1.35. Let A, B, E be subset of $\mathbb { R } ^ { d }$ such that $A \subset E \subset B$ , the sets A and B are measurable, and $m ( A ) = m ( B )$ . Then E is measurable, and thus $m ( E ) = m ( A ) = m ( B )$

Theorem 1.36. Let $E \subset \mathbb { R }$ where $m _ { * } ( E ) > 0$ . For each $\alpha \in ( 0 , 1 )$ , there exists an open interval I so that $m _ { * } ( E \cap I ) \geq \alpha m _ { * } ( I )$

Theorem 1.37. There exists a non-measurable subset of $\mathbb { R }$ .

Theorem 1.38. Every subset of $\mathbb { R } ^ { d }$ with strictly positive outer measure contains a nonmeasurable subset.

Theorem 1.39. The axiom of choice and the well-ordering principle are equivalent.

## 1.5 Measurable Functions

Theorem 1.40. If f is measurable, then −f is measurable.

Theorem 1.41. Let $f : E \to \mathbb { R }$ . The following are equivalent:

1. f is measurable.

2. $f ^ { - 1 } ( { \mathcal { O } } )$ is measurable for every open set O.

3. $f ^ { - 1 } ( F )$ is measurable for every closed set F .

Theorem 1.42. Continuous functions are measurable.

Theorem 1.43. The composition of a measurable and finite-valued function with a continuous function on the right is measurable. That is, if f is measurable and finite-valued and φ is continuous, then φ ◦ f is measurable.

Theorem 1.44. Let $\{ f _ { n } \} _ { n = 1 } ^ { \infty }$ be a sequence of measurable functions. Then

$$
\operatorname* { s u p } _ { n } f _ { n } \qquad \operatorname* { i n f } _ { n } f _ { n } \qquad \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { } f _ { n } \qquad \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } _ { } f _ { n }
$$

are also measurable functions.

Theorem 1.45. If f is the limit of a sequence of measurable functions, then f is measurable. Symbolically,

$$
f ( x ) = \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x ) \implies f \ i s \ m e a s u r a b l e
$$

Theorem 1.46. The sum or pointwise multiplication of finite-valued measurable functions is measurable. Symbolically, if f, g are measurable and finite-valued, then $f + g$ and fg are measurable.

Theorem 1.47. Let f be a measurable function and suppose g is a function such that $f ( x ) = g ( x )$ almost everywhere. Then g is measurable.

Theorem 1.48. Suppose f is a non-negative measurable function on $\mathbb { R } ^ { d }$ . Then there exists an increasing sequence of non-negative simple functions $\{ \phi _ { k } \} _ { k = - } ^ { \infty } .$ 1 that converges pointwise to f , that is,

$$
\phi _ { k } ( x ) \leq \phi _ { k + 1 } ( x ) \qquad \operatorname* { l i m } _ { k \to \infty } \phi _ { k } ( x ) = f ( x )
$$

for all x.

Theorem 1.49. Suppoet f is measurable on $\mathbb { R } ^ { d }$ . Then there is a sequence of simple functions $\phi _ { k }$ such that

$$
| \phi _ { k } ( x ) | \leq | \phi _ { k + 1 } ( x ) | \qquad \operatorname* { l i m } _ { k \to \infty } \phi _ { k } ( x ) = f ( x ) \qquad | \phi _ { k } ( x ) | \leq | f ( x ) |
$$

for all x. Note that this generalizes the above result.

Theorem 1.50. Let f be measurable on $\mathbb { R } ^ { d }$ . Then there exists a sequence of step functions $\psi _ { k }$ that converges pointwise to $f ( x )$ for almost every x. That is,

$$
\operatorname* { l i m } _ { k \to \infty } \psi _ { k } ( x ) = f ( x ) \quad a . e . \ x
$$

Theorem 1.51. Let f be measurable on $\mathbb { R } ^ { d }$ . Then there exists a sequence $f _ { k }$ of continuous functions such that $f _ { k }  f$ pointwise for a.e. x.

## Littlewood’s Three Principles

1. Every measurable set is nearly a finite union of intervals.

2. Every measurable function is nearly continuous. (see Lusin’s Theorem)

3. Every convergent sequence of measurable functions is nearly uniformly continuous. (see Egorov’s Theorem)

Theorem 1.52 (Egorov’s Theorem). Suppose $f _ { k }$ is a sequence of measurable functions defined on a measurable set E with $m ( E ) < \infty$ , such that $f _ { k } \to f \ u . e$ . on E. Then for every $\epsilon > 0$ , there is a closed set $A _ { \epsilon } \subset E$ such that m $( E \setminus A _ { \epsilon } ) < \epsilon$ and $f _ { k }  f$ uniformly on $A _ { \epsilon }$

Theorem 1.53 (Lusin’s Theorem). Suppose f is measurable and finite-valued on E with $m ( E ) < \infty$ Then for every $\epsilon > 0$ there exists a closed set $F _ { \epsilon }$ such that $F _ { \epsilon } ~ \subset ~ E$ and $m ( E \setminus F _ { \epsilon } )$ such that $f | _ { F _ { \epsilon } }$ is continuous.

Theorem 1.54 (Brunn-Minkowski Inequality). Let A, B be measurable sets in $\mathbb { R } ^ { d }$ so that $A + B$ is measurable. Then

$$
m ( A + B ) ^ { 1 / d } \geq m ( A ) ^ { 1 / d } + m ( B ) ^ { 1 / d }
$$

## 2 Chapter 2

## 2.1 The Lebesuge Integral

Theorem 2.1 (Bounded Convergence Theorem). Suppose $f _ { n }$ is a sequence of measurable functions that are all bounded by M and supported on a set E of finite measure and $f _ { n } ( x ) $ $f ( x )$ a.e. as $n \to \infty$ . Then f is measurable, bounded, supported on E, and

$$
\operatorname* { l i m } _ { n \to \infty } \int | f _ { n } - f | = 0
$$

As a result,

$$
\operatorname* { l i m } _ { n \to \infty } \int f _ { n } = \int f
$$

Theorem 2.2. If $f \geq 0$ and $\textstyle \int f = 0$ , then $f = 0$ almost everywhere.

Theorem 2.3. If f is integrable, then $f ( x ) < \infty$ almost everywhere.

Theorem 2.4 (Agreement with Riemann Integral). If f is Riemann integrable on $[ a , b ]$ then f is measurable and the Riemann integral $\textstyle \int _ { a } ^ { b } f$ is equal to the Lebesgue integral $\int _ { [ a , b ] } f$

Theorem 2.5. Define the functions

$$
f _ { a } ( x ) = { \left\{ \begin{array} { l l } { | x | ^ { - a } } & { | x | \leq 1 } \\ { 0 } & { | x | > 1 } \end{array} \right. }
$$

$$
F _ { a } ( x ) = { \frac { 1 } { 1 + | x | ^ { a } } }
$$

Then $f _ { a }$ is integrable if and only if $a < d . \ F _ { a }$ is integrable if an only if $a > d .$

Theorem 2.6 (Properties of Lebesgue Integral). Let f, g be integrable functions. Then

$$
{ \begin{array} { r l } { a , b \in \mathbb { R } } & { \Longrightarrow \displaystyle \int ( a f + b g ) = a \int f + b \int g } \\ { E \cap F = \emptyset \Longrightarrow \displaystyle \int _ { E \cup F } f = \int _ { E } f + \int _ { F } f } \\ { f \leq g \Longrightarrow \displaystyle \int f \leq \int g } \\ & { \quad \quad \quad \quad \quad \displaystyle \left| \int f \right| \leq \int | f | } \end{array} }
$$

Theorem 2.7 (Fatou’s Lemma). Let $f _ { n }$ be a sequence of nonnegative measurable functions. $I f \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x ) = f ( x )$ for a.e. x, then

$$
\int f \leq \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } _ { } \int f _ { n }
$$

Theorem 2.8 (Corollary to Fatou’s Lemma). Let f be a nonnegative measurable function and $f _ { n }$ a sequence of nonnegative measurable functions with $f _ { n } \leq f$ and $f _ { n }  f$ for a.e. x. Then

$$
\operatorname* { l i m } _ { n \to \infty } \int f _ { n } = \int f
$$

Theorem 2.9 (Monotone Convergence Theorem). Suppose that $\left\{ f _ { n } \right\}$ is a sequence of nonnegative measurable functions with $f _ { n } \nearrow f$ (that is, $f _ { n } \leq f _ { n + 1 } ~ a . e$ . and $\operatorname* { l i m } _ { n \to \infty } f _ { n } ( x ) = f ( x )$ $a . e . \jmath$ . Then

$$
\operatorname* { l i m } _ { n \to \infty } \int f _ { n } = \int f
$$

Theorem 2.10. Let $\scriptstyle \sum _ { k = 1 } ^ { \infty } a _ { k } ( x )$ be a series where each $a _ { k }$ is a nonnegative measurable function. Then

$$
\int \sum _ { k = 1 } ^ { \infty } a _ { k } ( x ) d x = \sum _ { k = 1 } ^ { \infty } \int a _ { k } ( x ) d x
$$

Consequently, $\begin{array} { r } { i f \sum _ { k } \int a _ { k } ( x ) d x } \end{array}$ is finite, the series $\textstyle \sum _ { k } a _ { k } ( x )$ converges for a.e. x.

Theorem 2.11. Let f be integrable on $\mathbb { R } ^ { d }$ . For every $\epsilon > 0$ , there exists a set B of finite measure such that

$$
\int _ { \mathbb { R } ^ { d } \backslash B } | f | < \epsilon
$$

Theorem 2.12. Let f be integrable on $\mathbb { R } ^ { d }$ . Then for every $\epsilon > 0$ , there exists $\delta > 0$ such that

$$
m ( E ) < \delta \implies \int _ { E } | f | < \epsilon
$$

Theorem 2.13 (Dominated Convergence Theorem). Let $\left\{ f _ { n } \right\}$ be a sequence of measurable functions such that $f _ { n } ( x ) \to f ( x )$ a.e. and there exists an integrable function g such that $| f _ { n } ( x ) | \leq g ( x )$ . Then

$$
\begin{array} { l } { \displaystyle \operatorname* { l i m } _ { n \to \infty } \int | f _ { n } - f | = 0 } \\ { \displaystyle \operatorname* { l i m } _ { n \to \infty } \int f _ { n } = \int f } \end{array}
$$

## 2.2 The Banach Space of Integrable Functions

Theorem 2.14 (Properties of $L ^ { 1 } )$ . Let $f , g \in L ^ { 1 }$ and $a \in \mathbb { R }$ . Then

$$
\begin{array} { c } { \| a f \| = | a | \ \| f \| } \\ { \| f + g \| \leq \| f \| + \| g \| } \\ { \| f \| = 0 \iff f = 0 \ a . e . } \end{array}
$$

That is, the map $f \mapsto \int | f |$ is a norm on $L ^ { 1 }$ . Additionally, $d ( f , g ) = \| f - g \|$ defines a metric on $L ^ { 1 }$

Theorem 2.15 (Riesz-Fischer Theorem, for $p = 1 )$ . The vector space $L ^ { 1 }$ is complete in its metric.

Theorem 2.16. $L ^ { 1 }$ is a Banach space.

Theorem 2.17. If fn is a sequence of $L ^ { 1 }$ functions that converges to f in the $L ^ { 1 }$ norm, then there is a subsequence $f _ { n _ { k } }$ such that $f _ { n _ { k } } ( x )  f ( x )$ a.e.

Theorem 2.18. The following families of functions are dense in $L ^ { 1 }$ : simple functions, step functions, and continuous functions of compact support.

Theorem 2.19 (Transformation Invariance Properties of the Integral). Let $f \in L ^ { 1 }$ . Then for $h \in \mathbb { R } ^ { d }$ and $\delta > 0$ we have

$$
\begin{array} { l } { \displaystyle \int _ { \mathbb R ^ { d } } f ( \boldsymbol x - h ) d \boldsymbol x = \int _ { \mathbb R ^ { d } } f ( \boldsymbol x ) d \boldsymbol x } \\ { \displaystyle \int _ { \mathbb R ^ { d } } f ( \delta \boldsymbol x ) d \boldsymbol x = \delta ^ { - d } \int _ { \mathbb R ^ { d } } f ( \boldsymbol x ) d \boldsymbol x } \\ { \displaystyle \int _ { \mathbb R ^ { d } } f ( - \boldsymbol x ) d \boldsymbol x = \int _ { \mathbb R ^ { d } } f ( \boldsymbol x ) d \boldsymbol x } \end{array}
$$

Theorem 2.20. Let $f \in L ^ { 1 }$ and $h \in \mathbb { R } ^ { d }$ . Then $\| f _ { h } - f \| \to 0$ as $h  0$ . Analogously, for $\delta > 0 , \| f ( \delta x ) - f ( x ) \| \to 0 \ a s \ \delta \to 1$

## 2.3 Fubini’s Theorem and Consequences

Theorem 2.21 (Fubini’s Theorem). Let $f ( x , y )$ be integrable on $\mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }$ . Then for almost every $\boldsymbol { y } \in \mathbb { R } ^ { d _ { 2 } }$

1. The slice $f ^ { y }$ is integrable on $\mathbb { R } ^ { d _ { 1 } }$

2. The function $g : \mathbb { R } ^ { d _ { 2 } }  \mathbb { R }$ define by $\begin{array} { r } { g ( y ) = \int _ { \mathbb { R } ^ { d _ { 1 } } } f ^ { y } ( x ) d x } \end{array}$ is integrable on $\mathbb { R } ^ { d _ { 2 } }$

3. Integrating g gives the integral of f , that is,

$$
\int _ { \mathbb { R } ^ { d _ { 2 } } } g ( y ) d y = \int _ { \mathbb { R } ^ { d _ { 2 } } } \left( \int _ { \mathbb { R } ^ { d _ { 1 } } } f ( x , y ) d x \right) d y = \int _ { \mathbb { R } ^ { d _ { 1 } + d _ { 2 } } } f
$$

Consequently, we can interchange the order of integration as follows:

$$
\int _ { \mathbb { R } ^ { d _ { 2 } } } \left( \int _ { \mathbb { R } ^ { d _ { 1 } } } f ( x , y ) d x \right) d y = \int _ { \mathbb { R } ^ { d _ { 1 } } } \left( \int _ { \mathbb { R } ^ { d _ { 2 } } } f ( x , y ) d y \right) d x
$$

Theorem 2.22 (Tonelli’s Theorem, AKA Fubini’s Theorem Part Two). Let f be a nonneagative measurable function on $\mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }$ . Then for almost every $\boldsymbol { y } \in \mathbb { R } ^ { d _ { 2 } }$

1. The slice $f ^ { y }$ is integrable on $\mathbb { R } ^ { d _ { 1 } }$

2. The function $g : \mathbb { R } ^ { d _ { 2 } }  \mathbb { R }$ define by $\begin{array} { r } { g ( y ) = \int _ { \mathbb { R } ^ { d _ { 1 } } } f ^ { y } ( x ) d x } \end{array}$ is integrable on $\mathbb { R } ^ { d _ { 2 } }$

3. Integrating g gives the integral of f , that $i s ,$

$$
\int _ { \mathbb { R } ^ { d _ { 2 } } } g ( y ) d y = \int _ { \mathbb { R } ^ { d _ { 2 } } } \left( \int _ { \mathbb { R } ^ { d _ { 1 } } } f ( x , y ) d x \right) d y = \int _ { \mathbb { R } ^ { d _ { 1 } + d _ { 2 } } } f
$$

Consequently, we can interchange the order of integration as follows:

$$
\int _ { \mathbb { R } ^ { d _ { 2 } } } \left( \int _ { \mathbb { R } ^ { d _ { 1 } } } f ( x , y ) d x \right) d y = \int _ { \mathbb { R } ^ { d _ { 1 } } } \left( \int _ { \mathbb { R } ^ { d _ { 2 } } } f ( x , y ) d y \right) d x
$$

Theorem 2.23. Let E be a measurable subset of $\mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }$ . Then for almost every $\boldsymbol { y } \in \mathbb { R } ^ { d _ { 2 } }$ the slice

$$
E ^ { y } = \{ x \in \mathbb { R } ^ { d _ { 1 } } : ( x , y ) \in E \}
$$

is a measurable subset of $\mathbb { R } ^ { d _ { 1 } }$ . Moreover, $m ( E ^ { y } )$ is a measurable function of y and

$$
m ( E ) = \int _ { \mathbb { R } ^ { d _ { 1 } } } m ( E ^ { y } ) d y
$$

A symmetric result holds for x-slices of R $^ { \cdot d _ { 2 } }$ .

Theorem 2.24. If $E = E _ { 1 } \times E _ { 2 }$ is a measurable subset of $\mathbb { R } _ { d } .$ and $m _ { * } ( E _ { 2 } ) > 0$ , then $E _ { 1 }$ is measurable.

Theorem 2.25. For $E _ { 1 } \subset \mathbb { R } ^ { d _ { 1 } }$ and $E _ { 2 } \subset \mathbb { R } ^ { d _ { 2 } }$ , we have $m _ { * } ( E _ { 1 } \times E _ { 2 } ) \leq m _ { * } ( E _ { 1 } ) m _ { * } ( E _ { 2 } )$ (Note that for this inequality, we interpret the product of zero and infinity to be zero.)

Theorem 2.26. Let $E _ { 1 } \subset \mathbb { R } ^ { d _ { 1 } }$ and $E _ { 2 } \subset \mathbb { R } ^ { d _ { 2 } }$ be measurable sets. Then $E _ { 1 } \times E _ { 2 }$ is measurable in $\mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }$ and $m ( E ) = m ( E _ { 1 } ) m ( E _ { 2 } )$ . (we interpret zero times infinity to be zero.)

Theorem 2.27. Let $f : \mathbb { R } ^ { d _ { 1 } }  [ - \infty , \infty ] ]$ be a measurable function. Then the function $\widetilde { f } : \mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } } \to \left[ - \infty , \infty \right]$ defined by $\widetilde f ( x , y ) = f ( x )$ is measurable on $\mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }$

Theorem 2.28 (Area Under a Curve). Let $f : \mathbb { R } ^ { d }  [ 0 , \infty ]$ be a non-negative measurable function. Let

$$
A = \{ ( x , y ) \in \mathbb { R } ^ { d } \times \mathbb { R } : 0 \leq y \leq f ( x ) \}
$$

Then f is measurable on $\mathbb { R } ^ { d }$ if and only if A is measurable in $\mathbb { R } ^ { d + 1 }$ , and $i f f$ is measurable, then

$$
\int _ { \mathbb { R } ^ { d } } f ( x ) d x = m ( A )
$$

This says that the measure of the area under an integrable function is equal to the integral of that function.

Theorem 2.29. If f is a measurable function on $\mathbb { R } ^ { d }$ , then the function $\widetilde f ( x , y ) = f ( x - y )$ is measurable on $\mathbb { R } ^ { d } \times \mathbb { R } ^ { d }$

Theorem 2.30. Let f be integrable on R. Then $\textstyle F ( x ) = \int _ { - \infty } ^ { x } f ( t ) d t$ is uniformly continuous.

Theorem 2.31 (Tchebychev Inequality). Let $f \geq 0$ and f be integrable. For $\alpha > 0$ and $E _ { \alpha } = \{ x : f ( x ) > \alpha \}$ , we have

$$
m ( E _ { \alpha } ) \leq { \frac { 1 } { \alpha } } \int _ { E _ { \alpha } } f
$$

## 3 Chapter 3

Theorem 3.1 (Hardy-Littlewood Maximal Function). Let $f \in L ^ { 1 } ( \mathbb { R } ^ { d } )$ . Then $f ^ { * }$ is measurable, $f ^ { \ast } ( x ) < \infty$ for a.e. x, and for all $\alpha > 0$

$$
m ( \{ x \in \mathbb { R } ^ { d } : f ^ { * } ( x ) > \alpha \} \leq \frac { 3 ^ { d } } { \alpha } \int _ { \mathbb { R } ^ { d } } | f ( y ) | d y
$$

Compare this to the Tchebychev inequality, which says

$$
m ( \{ x \in \mathbb { R } ^ { d } : f ( x ) > \alpha \} \leq \frac { 1 } { \alpha } \int _ { \mathbb { R } ^ { d } } | f ( y ) | d y
$$

Theorem 3.2 (Vitality Covering Lemma). Let $\{ B _ { 1 } , \ldots , B _ { N } \}$ be a finite collection of open balls $i n \mathbb { R } ^ { d }$ . There exists a disjoint subcollection $B _ { i _ { 1 } } , \ldots , B _ { i _ { k } }$ such that

$$
\bigcup _ { n = 1 } ^ { N } B _ { n } \subset \bigcup _ { j = 1 } ^ { k } 3 B _ { i j }
$$

Thus

$$
m \left( \bigcup _ { n = 1 } ^ { N } B _ { n } \right) \leq 3 ^ { d } \sum _ { j = 1 } ^ { k } m ( B _ { i _ { j } } )
$$

Theorem 3.3 (Lebesgue Differentiation Theorem). $I f f \in L ^ { 1 } ( \mathbb { R } ^ { d } )$ , then

$$
\operatorname* { l i m } _ { m ( B ) \to 0 } { \frac { 1 } { m ( B ) } } \int _ { B } f ( y ) d y = f ( x )
$$

for almost every x. In fact, the result holds if we only assume that f is locally integrable.

Theorem 3.4. Let E be a measurable subset or $\mathbb { R } ^ { d }$ and let A be the set of Lebesgue density points of E. Then almost every $x \in E$ is in A and almost every $x \in E ^ { c }$ is in $A ^ { c }$ . Equivalently,

$$
m ( E \setminus A ) = 0 \qquad m ( A \setminus E ) = 0 \qquad m ( E ) = m ( A ) = m ( E \cap A )
$$

## 3.1 Bounded Variation and Absolute Continuity

Theorem 3.5. If F is real-valued, monotonic, and bounded, then F is of bounded variation.

Theorem 3.6. If F if differentiable everywhere and $F ^ { \prime }$ is bounded, then F is of bounded variation. Furthermore, F is absolutely continuous.

Theorem 3.7. Every BV function can be written as a difference of two increasing functions.

Theorem 3.8. Every BV function is differentiable almost everywhere.

Theorem 3.9 (Rising Sun Lemma). Let G be real-valued and continuous on R, and let

$$
E = \{ x : G ( x + h ) > G ( x ) \ f o r \ s o m e \ h > 0 \}
$$

If E is nonempty, then it is open. In this case, E can be written as a countable disjoint union of open intervals $E = \bigcup ( a _ { k } , b _ { k } )$ such that

$$
G ( b _ { k } ) = G ( a _ { k } )
$$

Theorem 3.10. If F is increasing and continuous, then $F ^ { \prime }$ exists almost everywhere. Additionally, $F ^ { \prime }$ is measurable and nonnegative and

$$
\int _ { a } ^ { b } F ^ { \prime } ( x ) d x \leq F ( b ) - F ( a )
$$

Note: To get equality, we need stronger conditions on F . Specifically, we need absolute continuity.

Relevant “counter-example” to the obvious stronger version of the previous theorem: Let F be the Cantor-Lebesgue function. Then $F ^ { \prime } ( x ) = 0 { \mathrm { ~ a . e . } }$ , so $\textstyle \int _ { a } ^ { b } F ^ { \prime } ( x ) { \dot { d } } x = 0$ , but $F ( 1 ) = 1$ and $F ( 0 ) = 0$

Theorem 3.11. Absolutely continuous functions are uniformly continuous.

Theorem 3.12. Absolutely continuous functions are of bounded variation.

Theorem 3.13. If F is absolutely continuous on $[ a , b ]$ , then $T _ { F }$ is absolutely continuous on $[ a , b ]$

Theorem 3.14. If f is integrable and $\textstyle F ( x ) = \int _ { a } ^ { x } f ( y ) d y$ , then F is absolutely continuous.

Theorem 3.15. If F is absolutely continuous on $[ a , b ]$ , then $F ^ { \prime } ( x )$ exists almost everywhere.   
If $F ^ { \prime } ( x ) = 0$ for a.e. x, then F is constant.

Theorem 3.16. Suppose E is a set of finite measure and B is a Vitali covering of E. Then for any $\delta > 0$ there is a finite, disjoint, collection of balls $B _ { 1 } , \ldots , B _ { N }$ in B such that

$$
\sum _ { i = 1 } ^ { N } m ( B _ { i } ) \geq m ( E ) - \delta
$$

That is, we can “approximate” the E with coverings of balls whose total measure only barely exceeds that of E.

Theorem 3.17. Suppose E is a set of finite measure and B is a Vitali covering of E. Then $f o r$ any $\delta > 0$ there is a finite, disjoint, collection of balls $B _ { 1 } , \ldots , B _ { N }$ in B such that

$$
m \left( E \setminus \bigcup _ { i = 1 } ^ { N } B _ { i } \right) < 2 \delta
$$

Theorem 3.18. Suppose F is absolutely continuous on $[ a , b ]$ . Then $F ^ { \prime }$ exists almost everywhere and is integrable. Moreover,

$$
\int _ { a } ^ { x } F ^ { \prime } ( y ) d y = F ( x ) - F ( a )
$$

for all $a \leq x \leq b$ . In particular, we can choose $x = b$ to get

$$
\int _ { a } ^ { b } F ^ { \prime } ( y ) d y = F ( b ) - F ( a )
$$

Conversely, if f is integrable on $[ a , b ]$ then if we define $\textstyle F ( x ) = \int _ { a } ^ { x } f ( y ) d y$ , then $F ^ { \prime } ( x ) = f ( x )$ almost everywhere.

Theorem 3.19. A bounded increasing function on $[ a , b ]$ has at most countably many jump discontinuities.

Theorem 3.20. Let F be increasing and bounded on $[ a , b ]$ . Then $J _ { F } ( x )$ is discontinuous exactly at the points $\{ x _ { n } \}$ and has a jump at $x _ { n }$ equal that of F . Furthermore, the function $F ( x ) - J _ { F } ( x )$ is increasing and continuous.

Theorem 3.21. Let F be increasing and bounded on $[ a , b ]$ and let $J _ { F } ( x )$ be its jump function. Then $J ^ { \prime } ( x )$ exists a.e. and $J ^ { \prime } ( x ) = 0 \ a . e .$

Theorem 3.22. If $F \in \mathrm { B V } [ a , b ]$ , then

$$
\int _ { a } ^ { b } | F ^ { \prime } ( x ) | d x \leq T _ { F } ( b )
$$

Equality holds if and only if F is absolutely continuous.

Theorem 3.23. If $f : \mathbb { R } \to \mathbb { R }$ is absolutely continuous, then f maps sets of measure zero to sets of measure zero, and f maps measurable sets to measurable sets.

Theorem 3.24 (Change of Variable Formula). Let F be absolutely continuous and increasing on $\left\lceil a , b \right\rceil$ and set $A = F ( a )$ and $B = F ( b )$ . Let f be a measurable function on $[ A , B ]$ . Then $f ( F ( x ) ) F ^ { \prime } ( x )$ is measurable on $[ a , b ]$ , and if f is integrable on $[ A , B ]$ then

$$
\int _ { A } ^ { B } f ( y ) d y = \int _ { a } ^ { b } f ( F ( x ) ) F ^ { \prime } ( x ) d x
$$

## 4 Chapter 6

## 4.1 Abstract Measure Spaces

Theorem 4.1. Let m∗ denote the Lebesgue outer measure. Then $m _ { * }$ is an outer measure.

Theorem 4.2. Let $m _ { * }$ denote the Lebesgue outer measure. Then a set $E \subset \mathbb { R } ^ { d }$ is Carath´eodory measurable with respect to $m _ { * }$ if and only if E is Lebesgue measurable.

Theorem 4.3. Let X be a set and $\mu _ { * }$ be an outer measure. Then the collection M of Carath´eodory measurable sets forms a σ-algebra, and $\mu _ { * } | _ { \mathcal { M } }$ is a measure.

Theorem 4.4. If $\mu _ { * }$ is a metric exterior measure on a metric space X, then the Borel sets in X are measurable. Therefore, $\mu _ { * } { \big | } _ { B _ { X } }$ is a measure.

Theorem 4.5. Let $( X , d )$ be a measure set and µ is a Borel measure on X such that for a ball B of finite radius, $\mu ( B )$ is finite. Then µ is a regular measure.

Theorem 4.6. If $\mu _ { 0 }$ is a premeasure on an algebra A, define $\mu _ { * }$ on any subset E of X by

$$
\mu _ { * } ( E ) = \operatorname* { i n f } \left\{ \sum _ { j = 1 } ^ { \infty } \mu _ { 0 } ( E _ { j } ) : E \subset \bigcup _ { j = 1 } ^ { \infty } E _ { j } , E _ { j } \in { \mathcal { A } } \right\}
$$

Then $\mu _ { * }$ is an exterior measure on X that satisfies $\mu _ { * } ( E ) = \mu _ { 0 } ( E )$ for $E \in { \mathcal { A } }$ , and all sets in A are Carath´eodory measurable.

Theorem 4.7. Let A be an algebra of sets in X and $\mu _ { 0 }$ a premeasure on A and M the σ-algebra generated by A. Then there is a measure µ on M that extends $\mu _ { 0 }$

## 4.2 Integration in Abstract Measure Spaces

All of the following definitions, concepts, and theorems are easily generalized from the development of Lebesgue measure and Lebesgue integration on $\mathbb { R } ^ { d }$ to a general σ-finite measure space.

1. Almost everywhere

2. Measurable functions, simple functions

3. Every non-negative measurable function can be approximated by an increasing sequence of simple functions.

4. Every measurable function can be approximated by a sequence of simple functions.

5. Egorov’s Theorem

6. Integrable functions

7. Fatou’s Lemma, Monotone Convergence Theorem, Dominated Convergence Theorem

8. The space $L ^ { 1 } ( X , \mu )$ of integrable functions is a Banach space.

9. Fubini and Tonelli Theorems

Theorem 4.8. Let F be an increasing and normalized function on R. Then there is a unique measure µ (also denoted dF ) on the Borel sets of R such that $\mu ( ( a , b ] ) = F ( b ) - F ( a )$ for $a < b$ Conversely, if µ is a measure on the Borel sets of R that is finite on bounded intervals, then F defined by

$$
F ( x ) = { \left\{ \begin{array} { l l } { - \mu ( ( - x , 0 ] ) } & { x < 0 } \\ { 0 } & { x = 0 } \\ { \mu ( ( 0 , x ] ) } & { x > 0 } \end{array} \right. }
$$

is increasing and normalized.

Theorem 4.9. Two increasing functions F and G give the same measure $i f F { - } G$ is constant.

Theorem 4.10. If F is absolutely continuous on $[ a , b ]$ , then

$$
\int _ { a } ^ { b } f ( x ) d F ( x ) = \int _ { a } ^ { b } f ( x ) F ^ { \prime } ( x ) d x
$$

for every Borel measurable function f that is integrable with respect to $d \mu$

Theorem 4.11. Let ν be a signed measure. Then the total variation of $\nu ,$ denoted $| \nu |$ , is a positive measure, and satisfies $\nu \leq | \nu |$

Theorem 4.12. If $\nu \ll \mu$ and $\nu \perp \mu _ { : }$ , then $\nu ( E ) = 0$ for all E.

Theorem 4.13. Let $( X , { \mathcal { M } } , \mu )$ be a measure space and let $f \in L ^ { 1 } ( X , \mu )$ . Then ν defined by

$$
\nu ( E ) = \int _ { E } f d \mu
$$

is a signed measure on X. Furthermore, $\nu \ll \mu$

Theorem 4.14 (Radon-Nikodym Theorem). Let µ be a σ-finite positive measure on the measure space $( X , M )$ and let ν be a σ-finite signed measure on M. Then there exist unique signed measure $\nu _ { a }$ and $\nu _ { s }$ so that $\nu _ { a } \ll \mu$ and $\nu _ { s } \perp \mu$ and $\nu = \nu _ { a } + \nu _ { s }$ . In addition, the measure $\nu _ { a }$ is of the form $d \nu _ { a } = f d \mu$ , that is,

$$
\nu _ { a } ( E ) = \int _ { E } f ( x ) d \mu
$$

for some extended µ-integrable function $f$ .

Theorem 4.15. Let $C ( [ a , b ] )$ denote the vector space of continuous functions on the compact interval $[ a , b ]$ . If µ is a Borel measure on $[ a , b ]$ with $\mu ( [ a , b ] ) < \infty$ , then $\ell : C ( [ a , b ] ) \to [ \infty , \infty ]$ given by

$$
\ell ( f ) = \int _ { a } ^ { b } f ( x ) d \mu
$$

is a linear functional. It is positive $( f \geq 0 \implies \ell ( f ) \geq 0 )$ . Conversely, if \` is a positive linear functional on $C ( [ a , b ] )$ , then there is a unique Borel measure µ so that $\textstyle \ell ( f ) = \int _ { a } ^ { b } f d \mu$ for $f \in C ( [ a , b ] )$ ).