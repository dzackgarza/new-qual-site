# Math 8100 Assignment 4 Lebesgue Integration

Due date: Tuesday the 1st of October 2019

Definition.
Let E be a Lebesgue measurable subset of $\mathbb { R } ^ { n }$

We say that a measurable function $f : E \to \mathbb { C }$ is integrable on E if $\int _ { E } \left| f ( x ) \right| d x < \infty ,$

1. (a) Give an example of a continuous integrable function f on R for which $f ( x ) \not \to 0 { \mathrm { ~ a s ~ } } | x | \to \infty$

(b) Prove that if $f$ is integrable on R and uniformly continuous, then $\operatorname* { l i m } _ { | x | \to \infty } f ( x ) = 0$

2. Let f be an integrable function on $\mathbb { R } ^ { n }$

(a) Prove that $\{ x : | f ( x ) | = \infty \}$ has measure equal to zero.

(b) Let $\varepsilon > 0$ . Prove that there exists a measurable set E with $m ( E ) < \infty$ for which

$$
\int _ { E } | f | > \left( \int | f | \right) - \varepsilon .
$$

3. Let f be a function in $L ^ { + } ( \mathbb { R } ^ { n } )$ that is finite almost everywhere.

Let $E _ { 2 ^ { k } } = \{ x : f ( x ) > 2 ^ { k } \} { \mathrm { , ~ } } F _ { k } = \{ x : 2 ^ { k } < f ( x ) \leq 2 ^ { k + 1 } \}$ , and note that since f is finite almost everywhere it follows that $\bigcup _ { k = - \infty } ^ { \infty } F _ { k } = \{ x : f ( x ) > 0 \}$ , and the sets $F _ { k }$ are disjoint.
Prove that

$$
\int f ( x ) < \infty \iff \sum _ { k = - \infty } ^ { \infty } 2 ^ { k } m ( F _ { k } ) < \infty \iff \sum _ { k = - \infty } ^ { \infty } 2 ^ { k } m ( E _ { 2 ^ { k } } ) < \infty .
$$

4. Prove the following:

(a)

$$
\int _ { \{ x \in \mathbb { R } ^ { n } : | x | \leq 1 \} } | x | ^ { - p } d x < \infty \quad { \mathrm { i f ~ a n d ~ o n l y ~ i f } } \quad p < n .
$$

(b)

$$
\int _ { \{ x \in \mathbb { R } ^ { n } : | x | \geq 1 \} } | x | ^ { - p } d x < \infty \quad { \mathrm { i f ~ a n d ~ o n l y ~ i f } } \quad p > n .
$$

Hint: One possible approach is to use the first equivalence in Question 3 above.
I suggest however that in this case you also try simply writing $\mathbb { R } ^ { n }$ as a disjoint union of the annuli $A _ { k } = \{ \bar { 2 } ^ { k } < | x | \leq 2 ^ { k + 1 } \}$

5. Given any integrable function f on $\mathbb { R } ^ { n }$ , the Fourier transform of f is defined by

$$
{ \widehat { f } } ( \xi ) = \int _ { \mathbb { R } ^ { n } } f ( x ) e ^ { - 2 \pi i x \cdot \xi } d x
$$

where $x \cdot \xi = x _ { 1 } \xi _ { 1 } + \cdot \cdot \cdot + x _ { n } \xi _ { n }$ . Show that $\widehat { f }$ is a bounded continuous function of $\xi .$ .

6. Let $\{ f _ { k } \}$ be a sequence of integrable functions on $\mathbb { R } ^ { n } , f$ be integrable on $\mathbb { R } ^ { n }$ , and $\operatorname* { l i m } _ { k \to \infty } f _ { k } = f { \mathrm { ~ a . e } }$

(a) Suppose further that

$$
\operatorname* { l i m } _ { k \to \infty } \int | f _ { k } ( x ) | d x = A < \infty \qquad { \mathrm { a n d } } \qquad \int | f ( x ) | d x = B .
$$

i. Prove that

$$
\operatorname* { l i m } _ { k \to \infty } \int | f _ { k } ( x ) - f ( x ) | d x = A - B .
$$

Hint: Use the fact that

$$
| f _ { k } ( x ) | - | f ( x ) | \leq | f _ { k } ( x ) - f ( x ) | \leq | f _ { k } ( x ) | + | f ( x ) | .
$$

ii.
Give an example of a sequence $\{ f _ { k } \}$ of such functions for which $A \neq B .$

(b) Deduce that

$$
\int | f - f _ { k } | \to 0 \quad \Longleftrightarrow \quad \int | f _ { k } | \to \int | f | .
$$

7. (a) Suppose that $f ( x )$ and $x f ( x )$ are both integrable functions on R. Prove that the function

$$
F ( t ) = \int _ { \mathbb { R } } f ( x ) \cos ( t x ) d x .
$$

is differentiable at every t and find a formula for $F ^ { \prime } ( t )$

(b) Giving complete justification, evaluate

$$
\operatorname* { l i m } _ { t \to 0 } \int _ { 0 } ^ { 1 } { \frac { e ^ { t { \sqrt { x } } } - 1 } { t } } d x .
$$

## Extra Challenge Problems

## Not to be handed in with the assignment

1. Assume Fatou’s theorem and deduce the monotone convergence theorem from it.

2. A sequence $\{ f _ { k } \}$ of integrable functions on $\mathbb { R } ^ { n }$ is said to converge in measure to f if for every $\varepsilon > 0 .$

$$
\operatorname* { l i m } _ { k \to \infty } m ( \{ x \in \mathbb { R } ^ { n } : | f _ { k } ( x ) - f ( x ) | \geq \varepsilon \} ) = 0 .
$$

(a) Prove that if $f _ { k }  f$ in $L ^ { 1 }$ then $f _ { k }  f$ in measure.

(b) Give an example to show that the converse of Question 2a is false.

(c) Prove that if we make the additional assumption that there exists an integrable function g such that $| f _ { k } | \le g$ for all k, then $f _ { k }  f$ in measure implies that

i. \* (Bonus points) $f \in L ^ { 1 }$

Hint: First show that $\{ f _ { k } \}$ contains a subsequence which converges to f almost everywhere.
ii.
$f _ { k }  f$ in L 1 .

Hint: Try using absolute continuity and “small tails property” of the Lebesgue integral.

3. Let $\Omega \subseteq \mathbb { R } ^ { n }$ be measurable with $m ( \Omega ) < \infty$ . A set $\Phi \subseteq L ^ { 1 } ( \Omega )$ is said to be uniformly integrable if, for any $\varepsilon > 0$ there exists $\delta > 0$ such that whenever $f \in \Phi$ and $E \subseteq \Omega$ is measurable with $m ( E ) < \delta _ { \mathrm { { \scriptsize { i } } } }$ , then

$$
\int _ { E } \left| f ( x ) \right| d x < \varepsilon .
$$

(a) Prove that if $f \in L ^ { 1 } ( \Omega )$ and $\{ f _ { k } \}$ is a uniformly integrable sequence of functions in $L ^ { 1 } ( \Omega )$ such that $f _ { k }  f$ almost everywhere on Ω, then $f _ { k }  f$ in $L ^ { 1 } ( \Omega )$ .

(b) Is it necessary to assume that $f \in L ^ { 1 } ( \Omega ) \colon$
