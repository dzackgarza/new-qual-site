---
schema: qual/card@1
id: P-CASP04A
kind: problem
title: "True or False: Möbius transformations, Cauchy sequences, contour integrals, limits of functions missing values, and lacunary series"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
For each of the following, determine if the statement is true or false.

(a) There is a Möbius (linear fractional) transformation sending the triangle with vertices at $\{0, i, 1\}$ to that with vertices at $\{0, i, 2\}$.

(b) Let $(X, d)$ be a metric space.
If a Cauchy sequence $\{x_n\}_{n=1}^{\infty}$ in $X$ has a convergent subsequence, then $\{x_n\}_{n=1}^{\infty}$ is convergent.

(c) Let $\gamma_+(t) = e^{i\pi t}$ and $\gamma_-(t) = e^{-i\pi t}$, for $t \in [0, 1]$.
Then $\int_{\gamma_+} \frac{2}{(2z-1)^2}\,dz = \int_{\gamma_-} \frac{2}{(2z-1)^2}\,dz$.

(d) Let $f_n \in \mathcal{O}(G)$ be a sequence such that $f_n(G) \subset \DD \setminus \{0\}$ for $n = 1, 2, \ldots$, and assume that $f_n \to f$ in $\mathcal{O}(G)$.
Then either $f$ is constant or $f(G) \subset \DD \setminus \{0\}$.

(e) There is a sequence of complex numbers $\{a_n\}_{n=0}^{\infty}$ and strictly increasing sequence of integers $\{p_n\}_{n=0}^{\infty}$ with $p_n \geq n$ such that the radius of convergence of $\sum_{n=0}^{\infty} a_n z^n$ is one but that of $\sum_{n=0}^{\infty} a_n z^{p_n}$ is less than one.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own five answers are settled here, each in one step, with the reason the truth value turns on (angles, Cauchy, endpoints, Hurwitz, the exponent inequality) made explicit.

::: pf

::: {.pf-step #a}
(a) False.

::: pf-proof
Viewing a triangle as the closed region bounded by its three sides: a Möbius map that carried one region onto the other is conformal, and by Carathéodory's theorem for Jordan domains it extends to a homeomorphism of the closed regions, so it permutes the three corners. Hence the multisets of interior angles must agree. The triangle with vertices $0,i,1$ has angles $90^{\circ},45^{\circ},45^{\circ}$ (right angle at $0$, and equal angles at $i$ and $1$ by symmetry), whereas $0,i,2$ has $90^{\circ}$ at $0$ and the unequal pair $\arctan(1/2)$ and $90^{\circ}-\arctan(1/2)$ at $2$ and $i$. The multisets differ, so no such map exists.
:::

:::

::: {.pf-step #b}
(b) True.

::: pf-proof
Let $x_{n_{k}}\to x$. Given $\varepsilon>0$ choose $N$ with $d(x_{m},x_{n})<\varepsilon/2$ for $m,n\ge N$ (Cauchy) and $K\ge N$ with $d(x_{n_{k}},x)<\varepsilon/2$ for $n_{k}\ge K$. For $n\ge\max(N,n_{K})$ pick a subsequence index $n_{k}\ge n$; then $d(x_{n},x)\le d(x_{n},x_{n_{k}})+d(x_{n_{k}},x)<\varepsilon$. So $x_{n}\to x$, and the limit is the subsequential limit.
:::

:::

::: {.pf-step #c}
(c) True.

::: pf-proof
$\dfrac{2}{(2z-1)^{2}}$ has the antiderivative $F(z)=-\dfrac{1}{2z-1}$ on $\CC\setminus\{\tfrac12\}$, and neither arc $\gamma_{\pm}$ meets $\tfrac12$ since $\abs{\gamma_{\pm}(t)}=1$. An integral of a derivative along a path depends only on its endpoints, so both integrals equal $F(-1)-F(1)=\frac13+1=\frac43$. (Equivalently, the closed curve $\gamma_{+}*\gamma_{-}^{-1}$ avoids the pole, so Cauchy gives equality.)
:::

:::

::: {.pf-step #d}
(d) True.

::: pf-proof
$f_{n}\to f$ locally uniformly, so $f$ is holomorphic on $G$. If $f$ is nonconstant, Hurwitz's theorem applies: a locally uniform limit of functions with no zeros in $G$ is either identically zero or has no zeros in $G$, and $f\not\equiv0$ here. So $f$ has no zeros, and $\abs{f}\le1$ by continuity of the limit on compacts, hence $f(G)\subseteq\overline\DD\setminus\{0\}$; the maximum modulus principle applied on each component of $G$ rules out $\abs{f}=1$ at an interior point unless $f$ is constant, so a nonconstant $f$ maps into $\DD\setminus\{0\}$.
:::

:::

::: {.pf-step #e}
(e) False, for the stated conclusion "less than one".

::: pf-proof
Let $b_{m}=a_{n}$ when $m=p_{n}$ and $b_{m}=0$ otherwise, so the second series is $\sum b_{m}z^{m}$ with radius $1/\limsup\abs{b_{m}}^{1/m}$. If $\limsup\abs{b_{m}}^{1/m}>1$ then $\abs{a_{n}}^{1/p_{n}}>1$ for infinitely many $n$, so $\abs{a_{n}}>1$ there; since $p_{n}\ge n$ we then have $\abs{a_{n}}^{1/p_{n}}\le\abs{a_{n}}^{1/n}$, giving $\limsup\abs{b_{m}}^{1/m}\le\limsup\abs{a_{n}}^{1/n}=1$, which contradicts the previous inequality. So the radius of the second series is at least the radius of the first, here at least $1$, and cannot be less than one.
:::

:::

::: {.pf-qed}
(a) false by step [](#a){.pf-ref}, (b), (c), (d) true by steps [](#b){.pf-ref}, [](#c){.pf-ref}, [](#d){.pf-ref}, and (e) false by step [](#e){.pf-ref}.
:::

:::

:::
