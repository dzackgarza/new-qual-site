---
schema: qual/card@1
id: P-BERK89S-16
kind: problem
title: If $f\circ g$ tends to infinity, both entire functions are polynomials
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used the characterization of polynomials as entire functions with a pole
    at infinity: the composition forces $g$ to escape to infinity, and
    surjectivity of the resulting polynomial $g$ then forces the same for $f$.
---

::: {.problem}
Let $f,g$ be entire and suppose
\[
f(g(z))\longrightarrow\infty
\qquad(z\to\infty).
\]
Prove that both $f$ and $g$ are polynomials.
:::

::: {.solution}
<1>1. If an entire function $H$ satisfies
$$
H(z)\longrightarrow\infty
\qquad(z\to\infty),
$$
then $H$ is a nonconstant polynomial.

::: {.proof}
For sufficiently small nonzero $w$, the function $H(1/w)$ is nonzero and
$$
\frac{1}{H(1/w)}\longrightarrow0
\qquad(w\to0).
$$
Thus $1/H(1/w)$ has a removable singularity at $0$, and its extension has a
zero there. Hence $H(1/w)$ has a pole at $w=0$. Equivalently, the entire
function $H$ has a pole at infinity. An entire function with a pole at
infinity is a polynomial. The displayed limit excludes a constant polynomial.
:::

<1>2. One has
$$
g(z)\longrightarrow\infty
\qquad(z\to\infty).
$$

::: {.proof}
Suppose not. Then there are a sequence $z_j$ with $\abs{z_j}\to\infty$ and
a constant $M$ such that $\abs{g(z_j)}\leq M$ for every $j$. Passing to a
subsequence, we may assume that $g(z_j)\to w$ for some $w\in\CC$. Continuity
of $f$ then gives
$$
f(g(z_j))\longrightarrow f(w),
$$
contradicting the hypothesis that $f(g(z))\to\infty$ as $z\to\infty$.
:::

<1>3. The function $g$ is a nonconstant polynomial.

::: {.proof}
This follows immediately from steps <1>1 and <1>2.
:::

<1>4. One has
$$
f(w)\longrightarrow\infty
\qquad(w\to\infty).
$$

::: {.proof}
Suppose not. Then there are $w_j\in\CC$ with $\abs{w_j}\to\infty$ and a
constant $M$ such that
$$
\abs{f(w_j)}\leq M
$$
for every $j$.

By step <1>3, $g$ is a nonconstant complex polynomial. Hence for each $j$,
the fundamental theorem of algebra gives $z_j\in\CC$ such that
$$
g(z_j)=w_j.
$$
The sequence satisfies $\abs{z_j}\to\infty$: otherwise a bounded subsequence
would have a convergent subsequence $z_{j_k}\to z$, and continuity would give
$w_{j_k}=g(z_{j_k})\to g(z)$, contradicting $\abs{w_j}\to\infty$.

Consequently
$$
\abs{f(g(z_j))}=\abs{f(w_j)}\leq M,
$$
which contradicts $f(g(z))\to\infty$ as $z\to\infty$. Thus the stated limit
for $f$ holds.
:::

<1>5. Both $f$ and $g$ are polynomials.

::: {.proof}
Step <1>3 gives the assertion for $g$. Applying step <1>1 to the limit in
step <1>4 gives the assertion for $f$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
