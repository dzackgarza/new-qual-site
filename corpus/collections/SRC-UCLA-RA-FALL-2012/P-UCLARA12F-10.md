---
schema: qual/card@1
id: P-UCLARA12F-10
kind: problem
title: Pointwise convergence on an accumulating set determines a normal family
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $(f_n)$ be a sequence of holomorphic functions on $\mathbb D$ satisfying $|f_n(z)|\le1$ for every $z\in\mathbb D$ and every $n$.
Let
\[
A=\{z\in\mathbb D:\lim_{n\to\infty}f_n(z)\text{ exists}\}.
\]
Show that if $A$ has an accumulation point in $\mathbb D$, then there exists a holomorphic function $f$ on $\mathbb D$ such that $f_n\to f$ locally uniformly on $\mathbb D$.
:::

::: {.solution}
<1>1. The family $\{f_n:n\ge1\}$ is normal on $\mathbb D$.

::: {.proof}
The functions satisfy
$$
|f_n(z)|\le1
$$
for every $z\in\mathbb D$ and every $n$. Thus the family is locally uniformly bounded. By Montel's theorem, every sequence in this family has a subsequence that converges locally uniformly on $\mathbb D$ to a holomorphic function.
:::

<1>2. Any two locally uniform subsequential limits of $(f_n)$ are equal.

::: {.proof}
Let $(f_{n_k})$ converge locally uniformly to a holomorphic function $g$, and let $(f_{m_j})$ converge locally uniformly to a holomorphic function $h$.

For every $z\in A$, the full scalar sequence $(f_n(z))$ converges by definition of $A$. Therefore both subsequences have the same pointwise limit at $z$, and local uniform convergence gives
$$
g(z)=\lim_{k\to\infty}f_{n_k}(z)
=\lim_{n\to\infty}f_n(z)
=\lim_{j\to\infty}f_{m_j}(z)
=h(z).
$$
Hence $g=h$ on $A$. Since $A$ has an accumulation point in $\mathbb D$, the identity theorem gives
$$
g\equiv h
$$
on $\mathbb D$.
:::

<1>3. There exists a holomorphic function $f$ on $\mathbb D$ that is the locally uniform limit of some subsequence of $(f_n)$.

::: {.proof}
Apply step <1>1 to the sequence $(f_n)$ itself. Montel's theorem gives a subsequence $(f_{n_k})$ converging locally uniformly to some holomorphic function $f$.
:::

<1>4. The full sequence $(f_n)$ converges locally uniformly to the function $f$ from step <1>3.

::: {.proof}
Suppose not. Then there exist a compact set $K\subset\mathbb D$, a number $\varepsilon>0$, and a subsequence $(f_{m_j})$ such that
$$
\sup_{z\in K}|f_{m_j}(z)-f(z)|\ge\varepsilon
$$
for every $j$.

By step <1>1, the subsequence $(f_{m_j})$ has a further subsequence $(f_{m_{j_\ell}})$ converging locally uniformly to some holomorphic function $g$. By step <1>2, every locally uniform subsequential limit equals $f$, so $g=f$. Therefore
$$
\sup_{z\in K}|f_{m_{j_\ell}}(z)-f(z)|\longrightarrow0,
$$
contradicting the displayed lower bound by $\varepsilon$.
:::

<1>5. Therefore there exists a holomorphic function $f$ on $\mathbb D$ such that
$$
\boxed{f_n\to f\text{ locally uniformly on }\mathbb D.}
$$

::: {.proof}
Step <1>3 constructs a holomorphic candidate, and step <1>4 proves convergence of the full sequence to it.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
