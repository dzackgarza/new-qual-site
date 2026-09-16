---
schema: qual/card@1
id: E-SS4.PR-1
kind: problem
title: "Exponential decay of the Fourier transform gives holomorphy"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 4 source; repaired the statement where needed.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
1. Suppose ${ \hat { f } } ( \xi ) = O ( e ^ { - a | \xi | ^ { p } } )$ as $| \xi | \to \infty$ , for some $p > 1$ . Then f is holomorphic for all z and satisfies the growth condition

$$
| f (z) | \leq A e ^ {C | z | ^ {q}}
$$

for some $A,C>0$, where $1 / p + 1 / q = 1$

Note that on the one hand, when $p \longrightarrow \infty$ then $q \to 1$ , and this limiting case can be interpreted as part of Theorem 3.3. On the other hand, when $p \to 1$ then $q \to \infty$ , and this limiting case in a sense brings us back to Theorem 2.1.

[Hint: To prove the result, use the inequality $- \xi ^ { p } + \xi u \le u ^ { q }$ , which is valid when ξ and u are non-negative. To establish this inequality, examine separately the cases $\xi ^ { p } \ge \xi u$ and $\xi ^ { p } < \xi u ;$ note also that the functions $\xi = u ^ { q - 1 }$ and $u = \xi ^ { p - 1 }$ are inverses of each other because $( p - 1 ) ( q - 1 ) = 1 . ]$
:::

::: {.solution}
Let $q$ be determined by
\[
\frac1p+\frac1q=1.
\]
From the hypothesis there are constants $C_0,a_0>0$ such that, after increasing $C_0$ if necessary,
\[
|\widehat f(\xi)|\le C_0e^{-a_0|\xi|^p}
\qquad(\xi\in\mathbb R).
\tag{1}
\]
By Fourier inversion,
\[
f(z)=\int_{\mathbb R}\widehat f(\xi)e^{2\pi i\xi z}\,d\xi
\tag{2}
\]
for real $z$, and the right-hand side will provide the desired entire extension.

Fix $z=x+iy$. By Young's inequality, for every $u,v\ge0$,
\[
uv\le \frac{u^p}{p}+\frac{v^q}{q}.
\]
Apply this after scaling to obtain a constant $C_1>0$, depending only on $a_0,p$, such that
\[
2\pi |y||\xi|
\le \frac{a_0}{2}|\xi|^p+C_1|y|^q.
\tag{3}
\]
Combining (1) and (3),
\[
|\widehat f(\xi)e^{2\pi i\xi z}|
\le C_0e^{-a_0|\xi|^p+2\pi|y||\xi|}
\le C_0e^{-a_0|\xi|^p/2}e^{C_1|y|^q}.
\tag{4}
\]
The first factor on the right is integrable in $\xi$. On every compact set of $z$ the second factor is uniformly bounded, so (2) converges locally uniformly and may be differentiated under the integral sign to every order. Hence it defines an entire function agreeing with the original $f$ on $\mathbb R$.

Integrating (4) gives
\[
|f(z)|\le
C_0\left(\int_{\mathbb R}e^{-a_0|\xi|^p/2}\,d\xi\right)
e^{C_1|y|^q}
\le A e^{C_1|z|^q}.
\]
Thus
\[
|f(z)|\le A e^{C|z|^q}
\]
for suitable constants $A,C>0$.
:::
