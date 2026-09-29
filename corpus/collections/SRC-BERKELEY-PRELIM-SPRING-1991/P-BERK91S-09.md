---
schema: qual/card@1
id: P-BERK91S-09
kind: problem
title: Iterating a strict norm decrease on the unit ball converges to the origin
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-23
  note: Compared the open unit ball, continuity, strict norm decrease away from zero, and iteration with Problem 9 in the retained MinerU Flash extraction of Spring91.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let
$$
B_n=\{x\in\RR^n:\norm{x}<1\}
$$
and let $f:B_n\to B_n$ be continuous. Suppose
$$
\norm{f(x)}<\norm{x}
$$
for every nonzero $x\in B_n$. For nonzero $x_0\in B_n$, define
$$
x_k=f(x_{k-1}).
$$
Prove that
$$
x_k\to0.
$$
:::

::: {.solution}
For $k\ge0$, put $r_k\coloneqq\norm{x_k}$, and let
$$
K\coloneqq\{x\in\RR^n:\norm{x}\le r_0\}.
$$
Since $r_0<1$, the closed ball $K$ is contained in $B_n$.

::: pf

::: {.pf-step #s1}

The origin is fixed by $f$.

::: pf-proof

For $0<t\le1$, the point $t x_0$ is nonzero and lies in $B_n$.
The hypothesis gives
$$
0\le\norm{f(t x_0)}<t\norm{x_0}.
$$
Letting $t\to0$ and using continuity of $f$ at $0$ yields
$\norm{f(0)}=0$, so $f(0)=0$.

:::

:::

::: {.pf-step #s2}

The sequence $(r_k)$ converges to a number $L\ge0$, and
$x_k\in K$ for every $k\ge0$.

::: pf-proof

The norm-decrease hypothesis and step [](#s1){.pf-ref} give
$$
0\le r_{k+1}=\norm{f(x_k)}\le\norm{x_k}=r_k
\qquad(k\ge0),
$$
including at any index with $x_k=0$. Thus $(r_k)$ is nonincreasing
and bounded below, so it converges to some $L\ge0$. Since
$r_k\le r_0$, all iterates lie in $K$.

:::

:::

::: {.pf-step #s3}

The limit $L$ is zero.

::: pf-proof

The set $K$ is closed and bounded in $\RR^n$. By the
[[T-YKVFQ|Bolzano--Weierstrass theorem]], there is a subsequence
$(x_{k_j})$ converging to a point $p\in K$. By step [](#s2){.pf-ref} and
continuity of the norm,
$$
\norm{p}=\lim_{j\to\infty}r_{k_j}=L.
$$
Since $p\in K\subseteq B_n$, continuity of $f$ at $p$ gives
$$
\norm{f(p)}
=\lim_{j\to\infty}\norm{f(x_{k_j})}
=\lim_{j\to\infty}r_{k_j+1}
=L.
$$
If $L>0$, then $p\ne0$ and the strict norm-decrease hypothesis
requires $\norm{f(p)}<\norm{p}$, contradicting these equalities.
Therefore $L=0$.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give $\norm{x_k}\to0$, which is exactly
$x_k\to0$ in $\RR^n$.

:::

:::

:::
