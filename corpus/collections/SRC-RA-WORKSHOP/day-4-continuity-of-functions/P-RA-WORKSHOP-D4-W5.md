---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-W5
kind: problem
title: A liminf-limsup bound for real sequences
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
A useful lemma: Let $\{x_n\}$ be a real sequence with $\liminf_{n\to\infty}x_n$, $\limsup_{n\to\infty}x_n\in\mathbb R$.
Show that for any $\epsilon>0$ there exists some $N\in\mathbb N$ so that
$$
\left(\liminf_{n\to\infty}x_n\right)-\epsilon<x_n<
\left(\limsup_{n\to\infty}x_n\right)+\epsilon
\qquad\text{for all }n\ge N.
$$
What does this result imply if $\limsup_{n\to\infty}x_n<L$?
:::

::: {.solution}
Write $\ell=\liminf_{n\to\infty}x_n$ and $u=\limsup_{n\to\infty}x_n$, both finite by hypothesis.

<1>1. For every $\varepsilon>0$, there exists $N_1$ such that $x_n<u+\varepsilon$ whenever $n\geq N_1$.

::: {.proof}
By definition, $u=\inf_{N\geq1}\sup_{n\geq N}x_n$. The infimum property supplies $N_1$ with $\sup_{n\geq N_1}x_n<u+\varepsilon$. Every term of this tail is bounded above by its supremum, giving the assertion.
:::

<1>2. For every $\varepsilon>0$, there exists $N_2$ such that $x_n>\ell-\varepsilon$ whenever $n\geq N_2$.

::: {.proof}
By definition, $\ell=\sup_{N\geq1}\inf_{n\geq N}x_n$. The supremum property supplies $N_2$ with $\inf_{n\geq N_2}x_n>\ell-\varepsilon$. Every term of this tail is at least its infimum.
:::

<1>3. For every $\varepsilon>0$, there exists $N$ such that
\[
\boxed{\ell-\varepsilon<x_n<u+\varepsilon\quad(n\geq N)}.
\]

::: {.proof}
Choose $N=\max(N_1,N_2)$ with the indices from steps <1>1 and <1>2 for the same $\varepsilon$.
:::

<1>4. If $\limsup x_n<L$, then $x_n<L$ for every sufficiently large $n$.

::: {.proof}
Set $\varepsilon=L-u>0$. Step <1>1 gives an index $N$ such that $x_n<u+\varepsilon=L$ for every $n\geq N$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 gives the requested two-sided tail inequality, and step <1>4 establishes its consequence.
:::
:::
