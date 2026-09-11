---
schema: qual/card@1
id: E-SS9.PR-1
kind: problem
title: "Besides the approach in Section 1"
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
1. Besides the approach in Section 1.2, there are several alternate ways of dealing with the sum $\textstyle \sum { 1 } / ( z + \omega ) ^ { 2 }$ , where $\omega = n + m \tau$ . For example, one may sum either (a) circularly, (b) first in n then in m, (c) or first in m then in n.

(a) Prove that ${ \mathrm { i f ~ } } z \notin \Lambda$ , then

$$
\lim _ {R \to \infty} \sum_ {n ^ {2} + m ^ {2} \leq R ^ {2}} \frac {1}{(z + n + m \tau) ^ {2}} = S _ {1} (z)
$$

exists and $S _ { 1 } ( z ) = \wp ( z ) + c _ { 1 }$

(b) Similarly,

$$
\sum_ {m} \left(\sum_ {n} \frac {1}{(z + n + m \tau) ^ {2}}\right) = S _ {2} (z)
$$

exists and $S _ { 2 } ( z ) = \wp ( z ) + c _ { 2 } , { \mathrm { w h e r e ~ } } c _ { 2 } = F ( \tau )$ , and F is the forbidden Eisenstein series.

(c) Also

$$
\sum_ {n} \left(\sum_ {m} \frac {1}{(z + n + m \tau) ^ {2}}\right) = S _ {3} (z)
$$

exists with $S _ { 3 } ( z ) = \wp ( z ) + c _ { 3 }$ , and $c _ { 3 } = \tilde { F } ( \tau )$ , the reverse of $F ,$

[Hint: To prove (a), it sufices to show that lim $. R { \longrightarrow } \infty$ $\sum { \begin{array} { r l } \end{array} } \quad 1 / ( n + m \tau ) ^ { 2 } = c _ { 1 }$ $1 \leq n ^ { 2 } + m ^ { 2 } \leq R ^ { 2 }$ exists. This is proved by a comparision with $\begin{array} { r } { \int _ { 1 \leq x ^ { 2 } + y ^ { 2 } \leq R ^ { 2 } } \frac { d x } { ( x + y \tau ) ^ { 2 } } = I ( R ) } \end{array}$ . It can be shown that $I ( R ) = 0$ , which follows because $( \overline { { x } } + y \tau ) ^ { - 2 } = - ( \partial / \partial x ) ( x + y \tau ) ^ { - 1 } . ]$
:::

::: solution
Write \(\Lambda=\{n+m\tau:n,m\in\mathbb Z\}\), with \(\Im\tau\ne0\). Recall
\[
\wp(z)=\frac1{z^2}+\sum_{\omega\in\Lambda\setminus\{0\}}
\left(\frac1{(z+\omega)^2}-\frac1{\omega^2}\right).
\tag{1}
\]
The series in parentheses converges absolutely and locally uniformly away from \(\Lambda\), because its summand is \(O_z(|\omega|^{-3})\). Hence any admissible summation convention for the raw series differs from \(\wp(z)\) only by the same convention applied to \(\sum_{\omega\ne0}\omega^{-2}\).

For circular summation, put
\[
C_R=\sum_{1\le n^2+m^2\le R^2}\frac1{(n+m\tau)^2}.
\]
We show \(C_R\) converges. Since \(\Im\tau\ne0\), there is \(c>0\) such that
\[
|x+y\tau|\ge c\sqrt{x^2+y^2}.
\]
Set \(\phi(x,y)=(x+y\tau)^{-2}\). On the unit square centered at \((n,m)\), with \(n^2+m^2\) large, the mean-value theorem gives
\[
|\phi(x,y)-\phi(n,m)|\le C(n^2+m^2)^{-3/2}.
\]
The sum of these errors over \((n,m)\ne(0,0)\) converges, since the number of lattice points with radius comparable to \(r\) is \(O(r)\).

Thus \(C_R\) differs by a convergent quantity from the integral of \(\phi\) over the corresponding union of unit squares. Replacing that union by the annulus
\[
1\le x^2+y^2\le R^2
\]
changes the integral by \(O(R^{-1})\), because only an \(O(R)\)-area boundary layer is changed and \(|\phi|=O(R^{-2})\) there. But
\[
I(R)=\int_{1\le x^2+y^2\le R^2}\frac{dx\,dy}{(x+y\tau)^2}=0.
\]
Indeed, in polar coordinates,
\[
I(R)=\log R\int_0^{2\pi}\frac{d\theta}{(\cos\theta+\tau\sin\theta)^2},
\]
and the angular integral is zero because
\[
\frac{d}{d\theta}
\left(\frac{\sin\theta}{\cos\theta+\tau\sin\theta}\right)
=\frac1{(\cos\theta+\tau\sin\theta)^2}.
\]
(The denominator never vanishes because \(\Im\tau\ne0\).) Therefore \(C_R\to c_1\), and by (1)
\[
S_1(z)=\wp(z)+c_1.
\]

For summation first in \(n\), define
\[
F(\tau):=\sum_{m\in\mathbb Z}\left(\sum_{n\in\mathbb Z}^{\!*}\frac1{(n+m\tau)^2}\right),
\]
where the star omits \((n,m)=(0,0)\). For \(m=0\), the inner sum is \(2\zeta(2)=\pi^2/3\). For \(m\ne0\),
\[
\sum_{n\in\mathbb Z}\frac1{(n+m\tau)^2}
=\pi^2\csc^2(\pi m\tau).
\]
Because \(|\csc(\pi m\tau)|=O(e^{-\pi|m|\,|\Im\tau|})\), the outer sum converges absolutely. Thus \(F(\tau)\) exists, and absolute convergence of the corrected series in (1) gives
\[
S_2(z)=\wp(z)+F(\tau).
\]
This is the forbidden Eisenstein series.

Similarly, summing first in \(m\),
\[
\widetilde F(\tau)
:=\sum_{n\in\mathbb Z}\left(\sum_{m\in\mathbb Z}^{\!*}\frac1{(n+m\tau)^2}\right).
\]
For \(n\ne0\), factor out \(\tau^{-2}\):
\[
\sum_{m\in\mathbb Z}\frac1{(n+m\tau)^2}
=\tau^{-2}\pi^2\csc^2\!\left(\frac{\pi n}{\tau}\right),
\]
while the \(n=0\) term is \(\tau^{-2}\pi^2/3\). Since \(\Im(-1/\tau)>0\) when \(\Im\tau>0\), these terms again decay exponentially in \(|n|\). Hence \(\widetilde F(\tau)\) converges and
\[
S_3(z)=\wp(z)+\widetilde F(\tau).
\]
Thus all three summation procedures exist, and they differ only by the constants produced by the corresponding summations of \(\sum_{\omega\ne0}\omega^{-2}\).
:::
