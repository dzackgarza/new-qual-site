---
schema: qual/card@1
id: P-RASP22F
kind: problem
title: "A bounded density that integrates to the measure of every open set is 1 a.e."
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 6 of the official UCSD Spring 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, whose answer
    (f = 1 a.e.) is correct. Added: that mu(U) is finite for the open set produced by outer
    regularity, which is what lets the integral of f over U be subtracted; the finiteness of
    the sup norm from boundedness and nonnegativity; that the sets A_{k,n} increase to the
    level set, so continuity from below of the measure gives the level set measure zero, rather
    than summing over n; the same for the lower sets; and the description of {f != 1} as a
    countable union of level sets with the k chosen pointwise. Not claimed: a retained solution
    set; the provenance names the examination paper.
---

::: {.problem}
Let $X$ be an LCH space.
Let $\mu$ be a $\sigma$-finite measure on $X$ such that for any measurable set $E$, $\mu(E) = \inf\{\mu(U) : E \subset U, U \text{ open}\}$.
Let $f \geq 0$ be a bounded measurable function.
Prove that if $\mu(U) = \int_U f\,d\mu$ whenever $U$ is open, then $f = 1$ $\mu$-a.e.
:::


::: {.solution}
The published answer is the card's own argument; no retained solution set covers it — the collection's `provenance` names the Spring 2022 real-analysis examination paper, which carries no solutions. The answer is **yes**, and the numbered steps below are the card's previous prose with the two points it left implicit supplied: that $\mu(U)<\infty$ follows from the outer regularity, and that $\abs{1-f}\le M$ bounds the pieces.

Throughout $G$ is a finite group, $p$ is a fixed prime, and every element of $G$ has order $p^k$ for some $k\ge0$.

::: pf

::: {.pf-step #regularity}
For every measurable $E$ with $\mu(E)<\infty$ and every $\varepsilon>0$ there is open $U\supseteq E$ with $\mu(U)<\mu(E)+\varepsilon$, and then $\mu(U)<\infty$.

::: pf-proof
This is the outer-regularity hypothesis applied to $E$: $\mu(E)=\inf\theset{\mu(U):E\subseteq U,\ U\text{ open}}$, so some open $U$ has $\mu(U)$ below $\mu(E)+\varepsilon$. Since $\mu(E)$ is finite, so is $\mu(U)$.

:::

:::

::: {.pf-step #open-integral}
$\int_U(1-f)\,d\mu=0$ for every open $U$ of finite measure.

::: pf-proof
$\int_U(1-f)=\mu(U)-\int_Uf$, and $\int_Uf=\mu(U)$ by hypothesis, the integral being finite because $f$ is bounded and $\mu(U)<\infty$.

:::

:::

::: {.pf-step #general-integral}
$\int_E(1-f)\,d\mu=0$ for every measurable $E$ with $\mu(E)<\infty$.

::: pf-proof
Let $M=\norm{1-f}_\infty<\infty$, which is finite because $f$ is bounded and nonnegative. Fix such an $E$ and $\varepsilon>0$, and choose $U\supseteq E$ open with $\mu(U)<\mu(E)+\varepsilon$ by step [](#regularity){.pf-ref}. Then
$$
\abs{\int_E(1-f)}=\abs{\int_{U\setminus E}(1-f)}\le M\,\mu(U\setminus E)\le M\varepsilon,
$$
using step [](#open-integral){.pf-ref} for the first equality, $U\setminus E$ measurable with finite measure for the bound, and $\mu(U\setminus E)=\mu(U)-\mu(E)<\varepsilon$. Since $\varepsilon>0$ was arbitrary, the integral is $0$.

:::

:::

::: {.pf-step #sigma-finite}
There are measurable $X_n$ with $X_n\subseteq X_{n+1}$, $\mu(X_n)<\infty$ and $X=\bigcup_nX_n$.

::: pf-proof
$\sigma$-finiteness gives measurable sets $Y_n$ of finite measure covering $X$; set $X_n=Y_1\cup\cdots\cup Y_n$, which is measurable with $\mu(X_n)\le\sum_{k\le n}\mu(Y_k)<\infty$ and increasing.

:::

:::

::: {.pf-step #upper-set}
$\mu\theset{f\ge1+1/k}=0$ for every $k\ge1$.

::: pf-proof
Put $A_{k,n}=X_n\cap\theset{f\ge1+1/k}$, of finite measure. On $A_{k,n}$ one has $1-f\le-1/k$, so
$$
0=\int_{A_{k,n}}(1-f)\,d\mu\le-\frac1k\mu(A_{k,n})
$$
by step [](#general-integral){.pf-ref}, whence $\mu(A_{k,n})=0$. Since $A_{k,n}$ increases to $\theset{f\ge1+1/k}$ as $n\to\infty$ (by step [](#sigma-finite){.pf-ref}), continuity from below gives $\mu\theset{f\ge1+1/k}=0$.

:::

:::

::: {.pf-step #lower-set}
$\mu\theset{f\le1-1/k}=0$ for every $k\ge1$.

::: pf-proof
The same argument with $B_{k,n}=X_n\cap\theset{f\le1-1/k}$, on which $1-f\ge1/k$, gives $0=\int_{B_{k,n}}(1-f)\ge\frac1k\mu(B_{k,n})$, so $\mu(B_{k,n})=0$, and continuity from below gives $\mu\theset{f\le1-1/k}=0$.

:::

:::

::: {.pf-step #conclusion}
$f=1$ $\mu$-almost everywhere.

::: pf-proof
$\theset{f\ne1}=\bigcup_{k\ge1}\bigl(\theset{f\ge1+1/k}\cup\theset{f\le1-1/k}\bigr)$: a point with $f(x)>1$ satisfies $f(x)\ge1+1/k$ for some $k$, and a point with $f(x)<1$ satisfies $f(x)\le1-1/k$ for some $k$. This is a countable union of $\mu$-null sets by steps [](#upper-set){.pf-ref} and [](#lower-set){.pf-ref}, hence null.

:::

:::

:::
:::
