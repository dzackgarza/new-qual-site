---
schema: qual/card@1
id: P-UCLAB11F-07
kind: problem
title: Lower semicontinuity of matrix rank
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Fall 2011.
---

::: {.problem}
Let $f:\RR\to M_{n\times n}$ be continuous, where $M_{n\times n}$ is the space of $n\times n$ matrices.
Show that
$$
g(t)=\operatorname{rank}(f(t))
$$
is lower semicontinuous: if $t_k\to t$, then
$$
g(t)\le \liminf_{k\to\infty}g(t_k).
$$
Is $g$ always continuous?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Fix $t\in\RR$ and let
$$
r=\operatorname{rank}(f(t)).
$$
If $r=0$, then
$$
r\le\liminf_{k\to\infty}\operatorname{rank}(f(t_k))
$$
for every sequence $t_k\to t$.


::: pf-proof

Every matrix rank is a nonnegative integer, so the liminf on the right is at least $0=r$.

:::

:::

::: {.pf-step #s1-2}

Suppose $r>0$. Then $f(t)$ has an $r\times r$ minor with nonzero determinant.


::: pf-proof

The rank of a matrix is the largest size of a square minor with nonzero determinant. Since
$$
\operatorname{rank}(f(t))=r,
$$
such an $r\times r$ minor exists.

:::

:::

::: {.pf-step #s1-3}

The determinant of the corresponding $r\times r$ minor of $f(s)$ is nonzero for every $s$ sufficiently close to $t$.


::: pf-proof

Fix the row and column indices of the nonzero minor from step [](#s1-2){.pf-ref}. Its determinant is a polynomial in the corresponding entries of $f(s)$. Since $f:\RR\to M_{n\times n}$ is continuous, every matrix entry is continuous, so this minor determinant is a continuous scalar function of $s$.

Its value at $s=t$ is nonzero. Hence it remains nonzero on some neighborhood of $t$.

:::

:::

::: {.pf-step #s1-4}

For every $s$ sufficiently close to $t$,
$$
\operatorname{rank}(f(s))\ge r.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, $f(s)$ has a nonzero $r\times r$ minor. Therefore its rank is at least $r$.

:::

:::

::: {.pf-step #s1-5}

If $t_k\to t$, then
$$
\boxed{
g(t)\le\liminf_{k\to\infty}g(t_k)
}.
$$


::: pf-proof

If $g(t)=0$, apply step [](#s1-1){.pf-ref}. Otherwise let
$$
r=g(t)>0.
$$
By step [](#s1-4){.pf-ref}, there is a neighborhood of $t$ on which $g(s)\ge r$. Since $t_k\to t$, all sufficiently large $k$ lie in this neighborhood. Thus
$$
g(t_k)\ge r=g(t)
$$
eventually, and hence
$$
\liminf_{k\to\infty}g(t_k)\ge g(t).
$$

:::

:::

::: {.pf-step #s1-6}

The function $g$ need not be continuous.


::: pf-proof

Take
$$
f(t)=
\begin{pmatrix}
t&0\\
0&0
\end{pmatrix}.
$$
This matrix-valued function is continuous. Its rank is
$$
g(t)=
\begin{cases}
0,&t=0,\\
1,&t\ne0.
\end{cases}
$$
Thus $g$ is discontinuous at $0$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves lower semicontinuity, and step [](#s1-6){.pf-ref} answers the continuity question negatively.

:::

:::

:::
