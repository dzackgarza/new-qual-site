---
schema: qual/card@1
id: E-SS6.EX-9
kind: problem
title: "The hypergeometric series  was defined in Exercise 16 of Chapter 1"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
9. The hypergeometric series $F ( \alpha , \beta , \gamma ; z )$ was defined in Exercise 16 of Chapter 1. Show that

$$
F (\alpha , \beta , \gamma ; z) = \frac {\Gamma (\gamma)}{\Gamma (\beta) \Gamma (\gamma - \beta)} \int_ {0} ^ {1} t ^ {\beta - 1} (1 - t) ^ {\gamma - \beta - 1} (1 - z t) ^ {- \alpha} d t.
$$

Here $\alpha > 0 , \beta > 0 , \gamma > \beta$ , and $| z | < 1$

Show as a result that the hypergeometric function, initially defined by a power series convergent in the unit disc, can be continued analytically to the complex plane slit along the half-line $\lbrack 1 , \infty )$

Note that

$$
\log (1 - z) = - z F (1, 1, 2; z),
$$

$$
e ^ {z} = \lim _ {\beta \rightarrow \infty} F (1, \beta , 1; z / \beta),
$$

$$
(1 - z) ^ {- \alpha} = F (\alpha , 1, 1; z).
$$

[Hint: To prove the integral identity, expand $( 1 - z t ) ^ { - \alpha }$ as a power series.]
:::

::: {.solution}
Recall
\[
F(\alpha,\beta,\gamma;z)
=\sum_{n=0}^\infty
\frac{(\alpha)_n(\beta)_n}{(\gamma)_n\,n!}z^n.
\]
For $|z|<1$,
\[
(1-zt)^{-\alpha}
=\sum_{n=0}^\infty\frac{(\alpha)_n}{n!}(zt)^n,
\]
uniformly for $0\le t\le1$ on compact subsets of the unit disc. Hence termwise integration gives
\[
\int_0^1 t^{\beta-1}(1-t)^{\gamma-\beta-1}(1-zt)^{-\alpha}\,dt
=\sum_{n=0}^\infty\frac{(\alpha)_n z^n}{n!}
B(\beta+n,\gamma-\beta).
\]
Using the beta-gamma identity,
\[
B(\beta+n,\gamma-\beta)
=\frac{\Gamma(\beta+n)\Gamma(\gamma-\beta)}{\Gamma(\gamma+n)}
=\frac{\Gamma(\beta)\Gamma(\gamma-\beta)}{\Gamma(\gamma)}
\frac{(\beta)_n}{(\gamma)_n}.
\]
Multiplying by the prefactor yields exactly the hypergeometric series, proving the integral formula.

Now let
\[
\Omega=\mathbb C\setminus[1,\infty).
\]
For $z\in\Omega$ and $0\le t\le1$, the number $1-zt$ never lies on the nonpositive real axis, so the principal branch of $(1-zt)^{-\alpha}$ is holomorphic in $z$. On every compact $K\subset\Omega$ it is uniformly bounded for $0\le t\le1$. Since
\[
t^{\beta-1}(1-t)^{\gamma-\beta-1}
\]
is integrable, differentiation under the integral is valid locally uniformly on $\Omega$. Thus the integral defines a holomorphic function on $\Omega$ agreeing with the original power series on $|z|<1$. It is therefore the desired analytic continuation to the slit plane.
:::
