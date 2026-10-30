---
schema: qual/card@1
id: P-UCLAB06S-06
kind: problem
title: Compactness of a set of Lipschitz functions with unit $L^2$ norm in $C[0,1]$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 6 of the retained UCLA Basic Examination Spring 2006 PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked Problem 6 on page 2 of basic-06S.pdf, cleaned the LaTeX, and added an erratum remark that the strict Lipschitz inequality makes W non-closed so (B) fails as stated.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The exam printed the strict inequality |f(x)-f(y)| < |x-y|, under which W is not closed (f_n = (1-1/n)x + c_n tends to x + c outside W), so part (B) failed; the condition is now the non-strict inequality for all x, y in [0,1].
---

::: {.problem}
Let $W$ be the subset of the space $C[0,1]$ of real-valued, continuous functions on $[0,1]$ satisfying the conditions:
$$
\abs{f(x) - f(y)} \le \abs{x - y} \quad (x, y \in [0,1]) \qquad \int_0^1 f(x)^2\,dx = 1
$$

(A) Prove that $W$ is uniformly bounded, i.e., there exists $M > 0$ such that $\abs{f(x)} \leq M$ for all $x \in [0,1]$. Hint: Show first that $\abs{f(0)} \leq 2$ for all $f \in W$.

(B) Prove that $W$ is a compact subset of $C[0,1]$ under the sup norm $\norm{f}_\infty = \sup_{x \in [0,1]} \abs{f(x)}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $f\in W$ and every $x\in[0,1]$,
$$
\abs{f(x)-f(0)}\le x,
$$
and hence
$$
\abs{f(x)}
\le
\abs{f(0)}+1.
$$


::: pf-proof

The defining inequality gives
$$
\abs{f(x)-f(0)}
\le
\abs{x-0}
=x.
$$
Since
$$
x\le1,
$$
the triangle inequality gives
$$
\abs{f(x)}
\le
\abs{f(0)}+\abs{f(x)-f(0)}
\le
\abs{f(0)}+1.
$$

:::

:::

::: {.pf-step #s1-2}

For every $f\in W$,
$$
\boxed{\abs{f(0)}\le2}.
$$


::: pf-proof

Suppose instead that
$$
\abs{f(0)}>2.
$$
Then for every
$$
x\in[0,1],
$$
step [](#s1-1){.pf-ref} gives
$$
\abs{f(x)}
\ge
\abs{f(0)}-\abs{f(x)-f(0)}
\ge
\abs{f(0)}-1
>
1.
$$
Therefore
$$
f(x)^2>1
$$
for every $x\in[0,1]$.
Integrating gives
$$
\int_0^1f(x)^2\,dx>1,
$$
contradicting the defining condition
$$
\int_0^1f(x)^2\,dx=1.
$$
Hence
$$
\abs{f(0)}\le2.
$$

:::

:::

::: {.pf-step #s1-3}

The family $W$ is uniformly bounded; for example,
$$
\boxed{\abs{f(x)}\le3}
$$
for every $f\in W$ and every $x\in[0,1]$.


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref},
$$
\abs{f(x)}
\le
\abs{f(0)}+1
\le
3.
$$
Thus the single constant
$$
M=3
$$
works for all $f\in W$ and all $x\in[0,1]$.
This proves part (A).

:::

:::

::: {.pf-step #s1-4}

The set $W$ is compact in $C[0,1]$ under the supremum norm.


::: pf-proof

By step [](#s1-3){.pf-ref}, $W$ is uniformly bounded.
Every $f\in W$ satisfies $\abs{f(x)-f(y)}\le\abs{x-y}$, so for $\varepsilon>0$ the choice $\delta=\varepsilon$ works for all $f\in W$ at once; thus $W$ is equicontinuous.

The set $W$ is closed.
Let $f_n\in W$ with $f_n\to f$ uniformly.
For fixed $x,y$, letting $n\to\infty$ in $\abs{f_n(x)-f_n(y)}\le\abs{x-y}$ gives $\abs{f(x)-f(y)}\le\abs{x-y}$.
Also $\abs{f_n^2-f^2}=\abs{f_n-f}\,\abs{f_n+f}\le 6\norm{f_n-f}_\infty$ on $[0,1]$, because $\abs{f_n}\le3$ and hence $\abs{f}\le3$; so $f_n^2\to f^2$ uniformly and
$$
\int_0^1f^2=\lim_{n\to\infty}\int_0^1f_n^2=1.
$$
Hence $f\in W$.

By the Arzelà--Ascoli theorem, a closed, uniformly bounded, equicontinuous subset of $C[0,1]$ is compact.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (A), and step [](#s1-4){.pf-ref} proves part (B).

:::

:::

:::
