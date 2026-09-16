---
schema: qual/card@1
id: E-SS7.PR-1
kind: problem
title: "Dirichlet series with bounded coefficients converge in a half-plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: The extracted card appends distinct later starred source problems after indexed Problem 1; the solution addresses the indexed problem.
---

::: exercise
1. Let $\textstyle F ( s ) = \sum _ { n = 1 } ^ { \infty } a _ { n } / n ^ { s }$ , where $| a _ { n } | \leq M$ for all n.

(a) Then

$$
\lim _ {T \to \infty} \frac {1}{2 T} \int_ {- T} ^ {T} | F (\sigma + i t) | ^ {2} d t = \sum_ {n = 1} ^ {\infty} \frac {| a _ {n} | ^ {2}}{n ^ {2 \sigma}} \quad \text { if } \sigma > 1.
$$

How is this reminiscent of the Parseval-Plancherel theorem?
See e.g. Chapter 3 in Book I.

(b) Show as a consequence the uniqueness of Dirichlet series: If $\scriptstyle F ( s ) = \sum _ { n = 1 } ^ { \infty } a _ { n } n ^ { - s }$ where the coeficients are assumed to satisfy $| a _ { n } | \leq c n ^ { k }$ for some k, and $F ( s ) \equiv 0$ , then $a _ { n } = 0$ for all n.

Hint: For part (a) use the fact that

$$
\frac {1}{2 T} \int_ {- T} ^ {T} (n m) ^ {- \sigma} n ^ {- i t} m ^ {i t}   d t \to \left\{ \begin{array}{l l} n ^ {- 2 \sigma} & \text {if} n = m, \\ 0 & \text {if} n \neq m. \end{array} \right.
$$

2. $^\ast$ One of the “explicit formulas” in the theory of primes is as follows: if $\psi _ { 1 }$ is the integrated Tchebychev function considered in Section 2, then

$$
\psi_ {1} (x) = \frac {x ^ {2}}{2} - \sum_ {\rho} \frac {x ^ {\rho}}{\rho (\rho + 1)} - E (x)
$$

where the sum is taken over all zeros $\rho$ of the zeta function in the critical strip.
The error term is given by $\begin{array} { r } { E ( x ) = \dot { c _ { 1 } } x + c _ { 0 } + \sum _ { k = 1 } ^ { \infty } x ^ { 1 - 2 k } / ( 2 k ( 2 k - 1 ) ) } \end{array}$ , where $c _ { 1 } = \zeta ^ { \prime } ( 0 ) / \zeta ( 0 )$ and $c _ { 0 } = \zeta ^ { \prime } ( - 1 ) / \zeta ( - 1 )$ . Note that $\textstyle \sum _ { \rho } 1 / | \rho | ^ { 1 + \epsilon } < \infty$ for every $\epsilon > 0$ , because $( 1 - s ) \zeta ( s )$ has order of growth 1. (See Exercise 8.) Also, obviously $E ( x ) = O ( x )$ as $x \to \infty$

3. $^\ast$ Using the previous problem one can show that

$$
\pi (x) - \operatorname{Li} (x) = O (x ^ {\alpha + \epsilon}) \quad \mathrm{as} x \to \infty
$$

for every $\epsilon > 0$ , where $\alpha$ is fixed and $1 / 2 \le \alpha < 1$ if and only ${ \mathrm { i f ~ } } \zeta ( s )$ has no zeros in the strip $\alpha < \mathrm { R e } ( s ) < 1$ . The case $\alpha = 1 / 2$ corresponds to the Riemann hypothesis.

4. $^\ast$ One can combine ideas from the prime number theorem with the proof of Dirichlet’s theorem about primes in arithmetic progression (given in Book I) to prove the following.
   Let $q$ and $\ell$ be relatively prime integers.
   We consider the primes belonging to the arithmetic progression $\{ q k + \ell \} _ { k = 1 } ^ { \infty }$ , and let $\pi _ { q , \ell } ( x )$ denote the number of such primes $\leq x$ . Then one has

$$
\pi_ {q, \ell} (x) \sim \frac {x}{\varphi (q) \log x} \quad \mathrm{as} x \to \infty ,
$$
:::

::: solution
For Problem 1(a), assume first $\sigma>1$.
Since $|a_n|\le M$, the series for $F(\sigma+it)$ converges absolutely and uniformly in $t$.
Hence
\[
|F(\sigma+it)|^2
=\sum_{n,m\ge1}a_n\overline{a_m}(nm)^{-\sigma}e^{-it\log(n/m)},
\]
and the double series is absolutely summable because
\[
\sum_{n,m\ge1}|a_na_m|(nm)^{-\sigma}
\le M^2\zeta(\sigma)^2<\infty.
\]
Therefore we may integrate termwise:
\[
\frac1{2T}\int_{-T}^T|F(\sigma+it)|^2\,dt
=\sum_{n,m\ge1}a_n\overline{a_m}(nm)^{-\sigma}K_T(n,m),
\]
where
\[
K_T(n,m)=\frac1{2T}\int_{-T}^Te^{-it\log(n/m)}\,dt.
\]
If $n=m$, then $K_T(n,n)=1$.
If $n\ne m$, then
\[
K_T(n,m)=\frac{\sin(T\log(n/m))}{T\log(n/m)}\longrightarrow0.
\]
Also $|K_T(n,m)|\le1$.
Dominated convergence for the absolutely summable double series therefore gives
\[
\lim_{T\to\infty}\frac1{2T}\int_{-T}^T|F(\sigma+it)|^2\,dt
=\sum_{n=1}^\infty\frac{|a_n|^2}{n^{2\sigma}}.
\]
This is the Dirichlet-series analogue of Parseval--Plancherel: averaging in the vertical variable kills the cross terms and leaves the square sum of the coefficients.

For Problem 1(b), suppose
\[
F(s)=\sum_{n\ge1}a_nn^{-s}\equiv0,
\qquad |a_n|\le cn^k.
\]
Set $b_n=a_nn^{-k}$ and
\[
G(s)=F(s+k)=\sum_{n\ge1}b_nn^{-s}.
\]
Then $|b_n|\le c$ and $G\equiv0$.
Applying part (a), for every $\sigma>1$,
\[
0=\lim_{T\to\infty}\frac1{2T}\int_{-T}^T|G(\sigma+it)|^2\,dt
=\sum_{n=1}^\infty\frac{|b_n|^2}{n^{2\sigma}}.
\]
Every term on the right is nonnegative, so every $b_n=0$, hence every $a_n=0$.
This proves uniqueness of Dirichlet series under the stated polynomial growth condition.

The appended numbered items $2^*$--$4^*$ are separate subsequent source problems that were absorbed into this card by extraction; the indexed card `E-SS7.PR-1` is Problem 1 above.
:::
