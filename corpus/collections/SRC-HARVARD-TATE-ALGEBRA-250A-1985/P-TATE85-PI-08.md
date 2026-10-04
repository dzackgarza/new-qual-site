---
schema: qual/card@1
id: P-TATE85-PI-08
kind: problem
title: Prime ideals of convergent and formal power series rings
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
(8) Let A be the ring of power series$c _ { 0 } + c _ { 1 } z + c _ { 2 } z ^ { 2 } + . .$. with complex coefficients$c _ { i }$which have a nonzero radius of convergence (ring of germs of analytic functions at the origin$z = 0$in the complex z-plane). Discuss the prime ideals in$A .$. Do the same for the ring of formal power series$\dot { \boldsymbol { A } } = \boldsymbol { K } [ [ \boldsymbol { z } ] ]$in one variable z over any field.
:::

::: {.solution}
Treat first the ring $\mathcal O_0$ of convergent complex power-series germs at $0$, and then $K[[z]]$.

<1>1. Every nonzero element of $\mathcal O_0$ has a unique factorization
$$
f=z^n u
$$
with $n\ge0$ and $u$ a unit of $\mathcal O_0$.

::: {.proof}
Let
$$
f(z)=\sum_{j\ge0}c_jz^j
$$
be nonzero, and let $n$ be the least index with $c_n\ne0$. Then
$$
f=z^n u,
\qquad
u(z)=c_n+c_{n+1}z+\cdots.
$$
Since $u(0)=c_n\ne0$, the holomorphic function $u$ is nonvanishing on some neighborhood of $0$. Hence $1/u$ is holomorphic there and defines a convergent power-series germ. Thus $u$ is a unit.

The integer $n$ is uniquely determined as the order of vanishing of $f$ at $0$.
:::

<1>2. Every nonzero ideal of $\mathcal O_0$ is of the form
$$
\boxed{(z^n)}
$$
for a unique $n\ge0$.

::: {.proof}
Let $I\ne(0)$, and choose an element $f\in I$ with minimal order of vanishing $n$. By step <1>1,
$$
f=z^n u
$$
with $u$ a unit, so $z^n\in I$. Hence
$$
(z^n)\subseteq I.
$$

Every nonzero $g\in I$ has order at least $n$ by minimality, so step <1>1 gives
$$
g=z^m v=z^n(z^{m-n}v)\in(z^n).
$$
Thus $I=(z^n)$.
:::

<1>3. The prime ideals of $\mathcal O_0$ are exactly
$$
\boxed{(0)\quad\text{and}\quad(z)}.
$$

::: {.proof}
The ring $\mathcal O_0$ is an integral domain, so $(0)$ is prime. Also
$$
\mathcal O_0/(z)\cong\CC,
$$
so $(z)$ is maximal and hence prime.

If $n\ge2$, then
$$
z\notin(z^n)
$$
but
$$
z\cdot z^{n-1}\in(z^n),
$$
so $(z^n)$ is not prime. Step <1>2 lists all nonzero ideals, proving the claim.
:::

<1>4. Every nonzero element of $K[[z]]$ has a unique factorization
$$
f=z^n u
$$
with $u\in K[[z]]^\times$.

::: {.proof}
For
$$
f=\sum_{j\ge0}c_jz^j\ne0,
$$
let $n$ be the least index with $c_n\ne0$. Then
$$
f=z^n u
$$
with $u(0)=c_n\ne0$.

A formal power series is invertible exactly when its constant term is nonzero: if
$$
u=c_0+c_1z+\cdots,\qquad c_0\ne0,
$$
the coefficients of an inverse
$$
v=d_0+d_1z+\cdots
$$
are determined recursively from $uv=1$, starting with $d_0=c_0^{-1}$. Hence $u$ is a unit.

Again $n$ is uniquely the least exponent with nonzero coefficient.
:::

<1>5. Every nonzero ideal of $K[[z]]$ is
$$
\boxed{(z^n)}
$$
for a unique $n\ge0$.

::: {.proof}
The proof of step <1>2 applies verbatim using the factorization from step <1>4: choose an element of minimal $z$-adic order in the ideal, remove its unit factor, and compare the orders of all remaining elements.
:::

<1>6. The prime ideals of $K[[z]]$ are exactly
$$
\boxed{(0)\quad\text{and}\quad(z)}.
$$

::: {.proof}
The ring $K[[z]]$ is a domain, so $(0)$ is prime, and
$$
K[[z]]/(z)\cong K
$$
is a field, so $(z)$ is maximal. For $n\ge2$, the same factorization
$$
z\cdot z^{n-1}\in(z^n),
\qquad
z,z^{n-1}\notin(z^n)
$$
shows that $(z^n)$ is not prime. Step <1>5 exhausts all nonzero ideals.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 determine the prime ideals of the convergent-germ ring, and steps <1>4--<1>6 determine those of $K[[z]]$.
:::
:::
