---
schema: qual/card@1
id: P-UCLAB06W-04
kind: problem
title: Uniform convergence of a decreasing sequence of continuous functions
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 of the official UCLA Basic Qual Winter 2006 PDF.
---

::: {.problem}
Let $(f_n)$ be a decreasing sequence of continuous functions $f_n:[0,1]\to\RR$ satisfying the uniform bound $|f_n|\leq M$ for some $M\in(0,1)$.
Suppose the pointwise limit
\[
f(x)=\lim_{n\to\infty}f_n(x)
\]
is continuous on $[0,1]$.
Prove that $f_n\to f$ uniformly on $[0,1]$.

You may use without proof that $[0,1]$ is compact and sequentially compact.
:::

::: {.solution}

Since $(f_n)$ decreases pointwise to $f$, one has
$$
f_n(x)\ge f(x)
$$
for every $n$ and every $x\in[0,1]$.

::: pf

::: {.pf-step #s1-1}

Suppose, for contradiction, that $f_n\not\to f$ uniformly. Then there exist $\varepsilon>0$, a strictly increasing sequence of indices $(n_k)$, and points $x_k\in[0,1]$ such that
$$
f_{n_k}(x_k)-f(x_k)\ge\varepsilon
$$
for every $k$.


::: pf-proof

Failure of uniform convergence means that there is $\varepsilon>0$ such that for every $N$ there exist $n\ge N$ and $x\in[0,1]$ with
$$
\abs{f_n(x)-f(x)}\ge\varepsilon.
$$
Because $f_n(x)\ge f(x)$, the absolute value may be removed. Choosing successively with $n_k>n_{k-1}$ gives the required sequences.

:::

:::

::: {.pf-step #s1-2}

After passing to a subsequence, there is $x\in[0,1]$ such that
$$
x_k\longrightarrow x.
$$


::: pf-proof

The interval $[0,1]$ is sequentially compact, so the sequence $(x_k)$ has a convergent subsequence. Relabel that subsequence as $(x_k)$.

:::

:::

::: {.pf-step #s1-3}

For every fixed $m\ge1$,
$$
f_m(x)\ge f(x)+\varepsilon.
$$


::: pf-proof

Fix $m$. Since $n_k\to\infty$, one has $n_k\ge m$ for all sufficiently large $k$. Because the sequence $(f_n)$ is decreasing,
$$
f_m(x_k)\ge f_{n_k}(x_k).
$$
By step [](#s1-1){.pf-ref},
$$
f_m(x_k)
\ge
f_{n_k}(x_k)
\ge
f(x_k)+\varepsilon.
$$
Let $k\to\infty$. Both $f_m$ and $f$ are continuous, and step [](#s1-2){.pf-ref} gives $x_k\to x$, so
$$
f_m(x)\ge f(x)+\varepsilon.
$$

:::

:::

::: {.pf-step #s1-4}

Step [](#s1-3){.pf-ref} contradicts pointwise convergence $f_m(x)\to f(x)$.


::: pf-proof

The inequality from step [](#s1-3){.pf-ref} holds for every $m$:
$$
f_m(x)-f(x)\ge\varepsilon.
$$
But by the definition of $f$ as the pointwise limit,
$$
f_m(x)-f(x)\longrightarrow0
$$
as $m\to\infty$. This is impossible for a fixed $\varepsilon>0$.

:::

:::

::: pf-qed

The contradiction in step [](#s1-4){.pf-ref} shows that the assumption in step [](#s1-1){.pf-ref} was false. Therefore $f_n\to f$ uniformly on $[0,1]$.

:::

:::

:::
