---
schema: qual/card@1
id: P-YEZTR
kind: problem
title: $\lim a_n/a_{n+1}=z_0$ for the power series of a function with a pole at $z_0\in\partial\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Poles
  - Convergence Tests
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Suppose that $f$ is holomorphic on an open set containing the closed unit disk $\overline{\DD} = \{z \in \CC \mid \abs{z} \le 1\}$ except for a single pole at $z_0 \in \partial\DD$ ($\abs{z_0} = 1$).
Let $\sum_{n=0}^\infty a_n z^n$ be the Maclaurin series expansion of $f$ in $\DD$.
Prove that:
$$\lim_{n \to \infty} \frac{a_n}{a_{n+1}} = z_0.$$
:::

::: {.solution}
Let the pole at $z_0$ have order $m$, with principal part
$$
Q(z)=\sum_{j=1}^m\frac{c_j}{(z_0-z)^j},
\qquad c_m\ne0.
$$
The function $g=f-Q$ is holomorphic on a neighborhood of the closed unit disk, hence on $D_R(0)$ for some $R>1$.
Write $Q(z)=\sum q_nz^n$ and $g(z)=\sum b_nz^n$ for $\abs{z}<1$, so $a_n=q_n+b_n$.

::: pf

::: {.pf-step #q-asym}
$q_n=\dfrac{c_m}{(m-1)!}n^{m-1}z_0^{-(n+m)}\qty(1+O(n^{-1}))$.

::: pf-proof
For $\abs{z}<1$,
$$
\frac1{(z_0-z)^j}
=\sum_{n=0}^\infty
\binom{n+j-1}{j-1}z_0^{-(n+j)}z^n,
\qquad\text{so}\qquad
q_n=\sum_{j=1}^m c_j\binom{n+j-1}{j-1}z_0^{-(n+j)}.
$$
Since $\abs{z_0}=1$ and $\binom{n+j-1}{j-1}$ is a polynomial in $n$ of degree $j-1$ with leading coefficient $1/(j-1)!$, the term $j=m$ dominates.
:::

:::

::: {.pf-step #b-small}
$b_n=O(r^{-n})$ for some $r>1$.

::: pf-proof
Cauchy's estimates for $g$ on a circle of radius $r$ with $1<r<R$.
:::

:::

::: {.pf-step #a-asym}
$a_n=\dfrac{c_m}{(m-1)!}n^{m-1}z_0^{-(n+m)}\qty(1+O(n^{-1}))$.

::: pf-proof
By steps [](#q-asym){.pf-ref} and [](#b-small){.pf-ref}, $b_n/q_n=O(n^{1-m}r^{-n})=O(n^{-1})$, since the leading term of $q_n$ has modulus $\abs{c_m}n^{m-1}/(m-1)!$ with $c_m\ne0$.
:::

:::

::: pf-step
$\displaystyle\lim_{n\to\infty}\frac{a_n}{a_{n+1}}=z_0$.

::: pf-proof
By step [](#a-asym){.pf-ref}, $a_{n+1}\ne0$ for all large $n$, and
$$
\frac{a_n}{a_{n+1}}
=z_0\qty(\frac{n}{n+1})^{m-1}
\frac{1+O(n^{-1})}{1+O((n+1)^{-1})}
\longrightarrow z_0.
$$
:::

:::

:::

:::
