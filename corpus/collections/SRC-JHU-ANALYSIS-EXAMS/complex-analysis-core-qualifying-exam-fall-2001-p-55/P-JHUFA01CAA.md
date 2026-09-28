---
schema: qual/card@1
id: P-JHUFA01CAA
kind: problem
title: Meromorphic functions on the Riemann sphere are rational
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the definition of meromorphicity at infinity and the rationality conclusion with Fall 2001 Complex Analysis problem 1."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Used meromorphicity at infinity to confine finite poles to a compact disk, subtracted their finite principal parts, and showed the remaining entire function is a polynomial or constant according to the behavior at infinity."
---

::: {.problem}
Problem 1. A meromorphic function on $\mathbb { C } \cup \{ \infty \}$ is a meromorphic function $f ( z )$ on C such that $g ( z ) = f ( 1 / z )$ is also meromorphic.
Show that a meromorphic function on $\mathbb { C } \cup \{ \infty \}$ must be rational, i.e. one can express it as the quotient of two polynomials.
:::

::: {.solution}
<1>1. There are only finitely many finite poles.
::: {.proof}
By hypothesis $g(w)=f(1/w)$ is meromorphic near $w=0$. Hence for some
$R>0$, the function $f$ is holomorphic on $|z|>R$ except possibly for the
behavior corresponding to $w=0$ itself. Thus every finite pole of $f$ lies in
the compact disk $|z|\le R$.

Poles of a meromorphic function are isolated. If there were infinitely many
finite poles in that compact disk, compactness would give an accumulation point
in $\mathbb C$, contradicting isolatedness. Therefore the finite poles are
$a_1,\dots,a_m$ for some finite $m$.
:::

<1>2. Subtracting all finite principal parts leaves an entire function with at most polynomial growth.
::: {.proof}
At each pole $a_j$, let
$$
P_j(z)=\sum_{k=1}^{N_j}\frac{c_{jk}}{(z-a_j)^k}
$$
be the principal part of the Laurent expansion of $f$. Define
$$
h(z)=f(z)-\sum_{j=1}^mP_j(z).
$$
Every finite pole is removable for $h$, so $h$ extends to an entire function.
Each $P_j(z)$ tends to zero as $z\to\infty$.

Since $f(1/w)$ is meromorphic at $w=0$, it has either a removable singularity
or a pole there. In the removable case, $f(z)$ is bounded for large $|z|$; in
the pole case of order $N$, one has $|f(z)|\le C|z|^N$ for sufficiently large
$|z|$. The same corresponding bound holds for $h$, because the subtracted
principal parts tend to zero at infinity. Thus $h$ has at most polynomial
growth.
:::

<1>3. The entire remainder is a polynomial, so $f$ is rational.
::: {.proof}
Write
$$
h(z)=\sum_{n=0}^\infty b_nz^n.
$$
If $|h(z)|\le C(1+|z|^N)$ for large $|z|$, Cauchy's coefficient estimate on
large circles gives, for every $n>N$,
$$
|b_n|\le \frac{C(1+R^N)}{R^n}\longrightarrow0
\qquad(R\to\infty).
$$
Hence $b_n=0$ for all $n>N$, so $h$ is a polynomial. In the bounded case this
is simply Liouville's theorem and $h$ is constant.

Therefore
$$
f(z)=h(z)+\sum_{j=1}^mP_j(z)
$$
is a finite sum of rational functions, hence itself a rational function. This
proves the assertion.
:::
:::
