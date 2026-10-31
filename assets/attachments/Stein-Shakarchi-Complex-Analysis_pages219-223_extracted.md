2. The following links the multiplication of Dirichlet series with the divisibility properties of their coefficients.

(a) Show that if $\{ a _ { m } \}$ and $\{ b _ { k } \}$ are two bounded sequences of complex numbers, then

$$
\left( \sum _ { m = 1 } ^ { \infty } { \frac { a _ { m } } { m ^ { s } } } \right) \left( \sum _ { k = 1 } ^ { \infty } { \frac { b _ { k } } { k ^ { s } } } \right) = \sum _ { n = 1 } ^ { \infty } { \frac { c _ { n } } { n ^ { s } } } \quad { \mathrm { ~ w h e r e ~ } } c _ { n } = \sum _ { m k = n } a _ { m } b _ { k } .
$$

The above series converge absolutely when $\operatorname { R e } ( s ) > 1$

(b) Prove as a consequence that one has

$$
( \zeta ( s ) ) ^ { 2 } = \sum _ { n = 1 } ^ { \infty } { \frac { d ( n ) } { n ^ { s } } } \quad { \mathrm { ~ a n d ~ } } \quad \zeta ( s ) \zeta ( s - a ) = \sum _ { n = 1 } ^ { \infty } { \frac { \sigma _ { a } ( n ) } { n ^ { s } } }
$$

for $\operatorname { R e } ( s ) > 1$ and $\operatorname { R e } ( s - a ) > 1$ , respectively. Here $d ( n )$ equals the number of divisors of $n _ { \mathrm { : } }$ , and $\sigma _ { a } ( n )$ is the sum of the $a ^ { \mathrm { t h } }$ powers of divisors of $n$ . In particular, one has $\sigma _ { 0 } ( n ) = d ( n )$

3. In line with the previous exercise, we consider the Dirichlet series for $1 / \zeta$

(a) Prove that for $\operatorname { R e } ( s ) > 1$

$$
{ \frac { 1 } { \zeta ( s ) } } = \sum _ { n = 1 } ^ { \infty } { \frac { \mu ( n ) } { n ^ { s } } } ,
$$

where $\mu ( n )$ is the M¨obius function defined by

$$
\begin{array} { r l } & { \mu ( n ) = \left\{ \begin{array} { l l } { 1 } & { \mathrm { i f ~ } n = 1 , } \\ { ( - 1 ) ^ { k } } & { \mathrm { i f ~ } n = p _ { 1 } \cdots p _ { k } , \mathrm { a n d ~ t h e ~ } p _ { j } \mathrm { ~ a r e ~ d i s t i n c t ~ p r i m e s } , } \\ { 0 } & { \mathrm { o t h e r w i s e } . } \end{array} \right. } \end{array}
$$

Note that $\mu ( n m ) = \mu ( n ) \mu ( m )$ whenever n and m are relatively prime. [Hint: Use the Euler product formula for $\zeta ( s ) . ]$

(b) Show that

$$
\sum _ { k \mid n } \mu ( k ) = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } n = 1 , } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

4. Suppose $\{ a _ { n } \} _ { n = 1 } ^ { \infty }$ is a sequence of complex numbers such that $a _ { n } = a _ { m }$ if $n \equiv m$ mod $q$ for some positive integer $q .$ Define the Dirichlet L-series associated to $\left\{ a _ { n } \right\}$ by

$$
L ( s ) = \sum _ { n = 1 } ^ { \infty } { \frac { a _ { n } } { n ^ { s } } } \quad { \mathrm { ~ f o r ~ R e } } ( s ) > 1 .
$$

Also, with $a _ { 0 } = a _ { q }$ , let

$$
Q ( x ) = \sum _ { m = 0 } ^ { q - 1 } a _ { q - m } e ^ { m x } .
$$

Show, as in Exercises 15 and 16 of the previous chapter, that

$$
L ( s ) = { \frac { 1 } { \Gamma ( s ) } } \int _ { 0 } ^ { \infty } { \frac { Q ( x ) x ^ { s - 1 } } { e ^ { q x } - 1 } } d x , \quad \quad \mathrm { f o r ~ R e } ( s ) > 1 .
$$

Prove as a result that $L ( s )$ is continuable into the complex plane, with the only possible singularity a pole at $s = 1$ . In fact, $L ( s )$ is regular at $s = 1$ if and only if $\textstyle \sum _ { m = 0 } ^ { q - 1 } a _ { m } = 0$ . Note the connection with the Dirichlet $L ( s , \chi )$ series, taken up in Book I, Chapter 8, and that as a consequence, $L ( s , \chi )$ is regular at $s = 1$ if and only if χ is a non-trivial character.

## 5. Consider the following function

$$
\tilde { \zeta } ( s ) = 1 - { \frac { 1 } { 2 ^ { s } } } + { \frac { 1 } { 3 ^ { s } } } - \cdot \cdot \cdot = \sum _ { n = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { n + 1 } } { n ^ { s } } } .
$$

(a) Prove that the series defining $\tilde { \zeta } ( s )$ converges for $\operatorname { R e } ( s ) > 0$ and defines a holomorphic function in that half-plane.

(b) Show that for $s > 1$ one has $\tilde { \zeta } ( s ) = ( 1 - 2 ^ { 1 - s } ) \zeta ( s )$

(c) Conclude, since $\tilde { \zeta }$ is given as an alternating series, that ζ has no zeros on the segment $0 < \sigma < 1$ Extend this last assertion to $\sigma = 0$ by using the functional equation.

6. Show that for every $c > 0$

$$
\operatorname* { l i m } _ { N \to \infty } { \frac { 1 } { 2 \pi i } } \int _ { c - i N } ^ { c + i N } a ^ { s } { \frac { d s } { s } } = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } a > 1 , } \\ { 1 / 2 } & { { \mathrm { i f ~ } } a = 1 , } \\ { 0 } & { { \mathrm { i f ~ } } 0 \leq a < 1 . } \end{array} \right. }
$$

The integral is taken over the vertical segment from $c - i N$ to $c + i N$

7. Show that the function

$$
\xi ( s ) = \pi ^ { - s / 2 } \Gamma ( s / 2 ) \zeta ( s )
$$

is real when s is real, or when $\operatorname { R e } ( s ) = 1 / 2$

8. The function $\zeta$ has infinitely many zeros in the critical strip. This can be seen as follows.

(a) Let

$$
F ( s ) = \xi ( 1 / 2 + s ) , ~ \mathrm { w h e r e } ~ \xi ( s ) = \pi ^ { - s / 2 } \Gamma ( s / 2 ) \zeta ( s ) .
$$

Show that F (s) is an even function of s, and as a result, there exists G so that $G ( s ^ { 2 } ) = { \dot { F } } ( s )$

(b) Show that the function $( s - 1 ) \zeta ( s )$ is an entire function of growth order 1, that is

$$
| ( s - 1 ) \zeta ( s ) | \leq A _ { \epsilon } e ^ { a _ { \epsilon } | s | ^ { 1 + \epsilon } } .
$$

As a consequence $G ( s )$ is of growth order $1 / 2 .$

(c) Deduce from the above that ζ has infinitely many zeros in the critical strip.

[Hint: To prove (a) and (b) use the functional equation for $\zeta ( s )$ . For (c), use a result of Hadamard, which states that an entire function with fractional order has infinitely many zeros (Exercise 14 in Chapter 5).]

9. Refine the estimates in Proposition 2.7 in Chapter 6 and Proposition 1.6 to show that

(a) $| \zeta ( 1 + i t ) | \leq A \log | t | ,$

(b) $| \zeta ^ { \prime } ( 1 + i t ) | \leq A ( \log | t | ) ^ { 2 } ,$

(c) $1 / | \zeta ( 1 + i t ) | \leq A ( \log | t | ) ^ { a } ,$

when $| t | \geq 2 \ \mathrm { ( w i t h } \ a = 7 $

10. In the theory of primes, a better approximation to $\pi ( x )$ (instead of $x / \log x )$ turns out to be Li(x) defined by

$$
\operatorname { L i } ( x ) = \int _ { 2 } ^ { x } { \frac { d t } { \log t } } .
$$

(a) Prove that

$$
\operatorname { L i } ( x ) = { \frac { x } { \log x } } + O \left( { \frac { x } { ( \log x ) ^ { 2 } } } \right) \qquad { \mathrm { a s ~ } } x \to \infty ,
$$

and that as a consequence

$$
\pi ( x ) \sim \operatorname { L i } ( x ) \quad { \mathrm { ~ a s ~ } } x \to \infty .
$$

[Hint: Integrate by parts in the definition of Li(x) and observe that it suffices to prove

$$
\int _ { 2 } ^ { x } \frac { d t } { ( \log t ) ^ { 2 } } = O \left( \frac { x } { ( \log x ) ^ { 2 } } \right) .
$$

To see this, split the integral from 2 to $\sqrt { x }$ and from $\sqrt { x }$ to x.]

(b) Refine the previous analysis by showing that for every integer $N > 0$ one has the following asymptotic expansion

$$
\operatorname { L i } ( x ) = { \frac { x } { \log { x } } } + { \frac { x } { ( \log { x } ) ^ { 2 } } } + 2 { \frac { x } { ( \log { x } ) ^ { 3 } } } \cdots + ( N - 1 ) ! { \frac { x } { ( \log { x } ) ^ { N } } } + O \left( { \frac { x } { ( \log { x } ) ^ { N + 1 } } } \right)
$$

as $x \longrightarrow \infty .$

11. Let

$$
\varphi ( x ) = \sum _ { p \leq x } \log p
$$

where the sum is taken over all primes $\leq x$ . Prove that the following are equivalent as $x \to \infty ;$

(i) $\varphi ( x ) \sim x ,$

(ii) $\pi ( x ) \sim x / \log x .$

(iii) $\psi ( x ) \sim x ,$

(iv) $\psi _ { 1 } ( x ) \sim x ^ { 2 } / 2 .$

12. If $p _ { n }$ denotes the $n ^ { \mathrm { t h } }$ prime, the prime number theorem implies that $p _ { n } \sim n$ log n as $n \to \infty$

(a) Show that $\pi ( x ) \sim x /$ log x implies that

$$
\log \pi ( x ) + \log \log x \sim \log x .
$$

(b) As a consequence, prove that log $\pi ( x ) \sim \log x .$ , and take $x = p _ { n }$ to conclude the proof.

## 4 Problems

1. Let $\textstyle F ( s ) = \sum _ { n = 1 } ^ { \infty } a _ { n } / n ^ { s }$ , where $| a _ { n } | \leq M$ for all n.

(a) Then

$$
\operatorname* { l i m } _ { T \to \infty } \frac { 1 } { 2 T } \int _ { - T } ^ { T } | F ( \sigma + i t ) | ^ { 2 } d t = \sum _ { n = 1 } ^ { \infty } \frac { | a _ { n } | ^ { 2 } } { n ^ { 2 \sigma } } \qquad \mathrm { i f } \ \sigma > 1 .
$$

How is this reminiscent of the Parseval-Plancherel theorem? See e.g. Chapter 3 in Book I.

(b) Show as a consequence the uniqueness of Dirichlet series: If $\scriptstyle F ( s ) = \sum _ { n = 1 } ^ { \infty } a _ { n } n ^ { - s }$ where the coefficients are assumed to satisfy $| a _ { n } | \leq c n ^ { k }$ for some k, and $F ( s ) \equiv 0$ , then $a _ { n } = 0$ for all n.

Hint: For part (a) use the fact that

$$
{ \frac { 1 } { 2 T } } \int _ { - T } ^ { T } ( n m ) ^ { - \sigma } n ^ { - i t } m ^ { i t } d t \to { \left\{ \begin{array} { l l } { n ^ { - 2 \sigma } } & { { \mathrm { i f ~ } } n = m , } \\ { 0 } & { { \mathrm { i f ~ } } n \neq m . } \end{array} \right. }
$$

2.∗ One of the “explicit formulas” in the theory of primes is as follows: if $\psi _ { 1 }$ is the integrated Tchebychev function considered in Section 2, then

$$
\psi _ { 1 } ( x ) = { \frac { x ^ { 2 } } { 2 } } - \sum _ { \rho } { \frac { x ^ { \rho } } { \rho ( \rho + 1 ) } } - E ( x )
$$

where the sum is taken over all zeros $\rho$ of the zeta function in the critical strip. The error term is given by $\begin{array} { r } { E ( x ) = \dot { c _ { 1 } } x + c _ { 0 } + \sum _ { k = 1 } ^ { \infty } x ^ { 1 - 2 k } / ( 2 k ( 2 k - 1 ) ) } \end{array}$ , where $c _ { 1 } = \zeta ^ { \prime } ( 0 ) / \zeta ( 0 )$ and $c _ { 0 } = \zeta ^ { \prime } ( - 1 ) / \zeta ( - 1 )$ Note that $\textstyle \sum _ { \rho } 1 / | \rho | ^ { 1 + \epsilon } < \infty$ for every $\epsilon > 0$ , because $( 1 - s ) \zeta ( s )$ has order of growth 1. (See Exercise 8.) Also, obviously $E ( x ) = O ( x )$ as $x \to \infty$

3.∗ Using the previous problem one can show that

$$
\pi ( x ) - \operatorname { L i } ( x ) = O ( x ^ { \alpha + \epsilon } ) \quad { \mathrm { ~ a s ~ } } x \to \infty
$$

for every $\epsilon > 0$ , where α is fixed and $1 / 2 \le \alpha < 1$ if and only ${ \mathrm { i f ~ } } \zeta ( s )$ has no zeros in the strip $\alpha < \mathrm { R e } ( s ) < 1$ . The case $\alpha = 1 / 2$ corresponds to the Riemann hypothesis.

4.∗ One can combine ideas from the prime number theorem with the proof of Dirichlet’s theorem about primes in arithmetic progression (given in Book I) to prove the following. Let q and ℓ be relatively prime integers. We consider the primes belonging to the arithmetic progression $\{ q k + \ell \} _ { k = 1 } ^ { \infty }$ , and let $\pi _ { q , \ell } ( x )$ denote the number of such primes $\leq x$ . Then one has

$$
\pi _ { q , \ell } ( x ) \sim { \frac { x } { \varphi ( q ) \log x } } \quad { \mathrm { ~ a s ~ } } x \to \infty ,
$$

where $\varphi ( q )$ denotes the number of positive integers less than $q$ and relatively prime to $q .$