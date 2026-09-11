---
schema: qual/card@1
id: E-SS9.EX-5
kind: problem
title: "SS 9.5: The Weierstrass sigma function"
classification:
  areas:
  - complex-analysis
  topics: ['Elliptic Functions', 'Weierstrass P', 'Lattices']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
5. Let $\sigma ( z )$ be the canonical product

$$
\sigma (z) = z \prod_ {j = 1} ^ {\infty} E _ {2} (z / \tau_ {j}),
$$

where $\tau _ { j }$ is an enumeration of the periods $\{ n + m \tau \}$ with $( n , m ) \neq ( 0 , 0 )$ , and $E _ { 2 } ( z ) = ( 1 - z ) e ^ { z + z ^ { 2 } / 2 }$

(a) Show that $\sigma ( z )$ is an entire function of order 2 that has simple zeros at all the periods $n + m \tau$ , and vanishes nowhere else.

(b) Show that

$$
\frac {\sigma^ {\prime} (z)}{\sigma (z)} = \frac {1}{z} + \sum_ {(n, m) \neq (0, 0)} \left[ \frac {1}{z - n - m \tau} + \frac {1}{n + m \tau} + \frac {z}{(n + m \tau) ^ {2}} \right],
$$

and that this series converges whenever z is not a lattice point.

(c) Let $L ( z ) = - \sigma ^ { \prime } ( z ) / \sigma ( z )$ . Then

$$
L ^ {\prime} (z) = \frac {(\sigma^ {\prime} (z)) ^ {2} - \sigma (z) \sigma^ {\prime \prime} (z)}{(\sigma (z)) ^ {2}} = \wp (z).
$$
:::

::: solution
Let \(\Lambda=\{n+m\tau:n,m\in\mathbb Z\}\), with \(\Im\tau>0\). The number of lattice points in \(|\omega|\le R\) is \(O(R^2)\). Hence
\[
\sum_{\omega\in\Lambda\setminus\{0\}}|\omega|^{-3}<\infty,
\]
so the canonical product
\[
\sigma(z)=z\prod_{\omega\in\Lambda\setminus\{0\}}E_2(z/\omega),
\qquad E_2(w)=(1-w)e^{w+w^2/2},
\]
converges locally uniformly and defines an entire function. Its only zeros are \(0\) and the nonzero lattice points, and each is simple, since each factor \(E_2(z/\omega)\) has a simple zero at \(z=\omega\) and all remaining factors are nonzero there.

The exponent of convergence of the lattice is \(2\): \(\sum_{\omega\ne0}|\omega|^{-s}\) converges for \(s>2\) and diverges for \(s\le2\). Thus any entire function with these zeros has order at least \(2\). On the other hand, the standard canonical-product estimate for a genus-two product with counting function \(N(R)=O(R^2)\) gives, for every \(\varepsilon>0\),
\[
\log M_\sigma(R)=O(R^{2+\varepsilon}).
\]
Hence the order of \(\sigma\) is at most \(2\), and therefore exactly \(2\).

For part (b), logarithmic differentiation is legitimate locally uniformly away from \(\Lambda\). Since
\[
\frac{E_2'(w)}{E_2(w)}=-\frac1{1-w}+1+w,
\]
we obtain
\[
\frac{\sigma'(z)}{\sigma(z)}
=\frac1z+\sum_{\omega\ne0}
\left(\frac1{z-\omega}+\frac1\omega+\frac z{\omega^2}\right).
\]
Indeed, on a compact set \(|z|\le R\) avoiding \(\Lambda\), the summand for \(|\omega|>2R\) equals
\[
\frac{z^2}{\omega^2(z-\omega)},
\]
so it is \(O_R(|\omega|^{-3})\), and the series converges normally.

Finally let \(L=-\sigma'/\sigma\). Differentiating the normally convergent series gives
\[
L'(z)=\frac1{z^2}+\sum_{\omega\ne0}
\left(\frac1{(z-\omega)^2}-\frac1{\omega^2}\right).
\]
Because \(\Lambda=-\Lambda\), this is exactly the defining series for the Weierstrass function \(\wp(z)\). Hence
\[
L'(z)=\wp(z)
=\frac{(\sigma'(z))^2-\sigma(z)\sigma''(z)}{\sigma(z)^2}.
\]
:::
