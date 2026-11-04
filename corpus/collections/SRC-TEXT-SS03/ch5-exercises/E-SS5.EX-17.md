---
schema: qual/card@1
id: E-SS5.EX-17
kind: problem
title: Entire interpolation on a discrete sequence
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Weierstrass Products
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 5, §3, exercise 17, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise; the two defects the card's own remark records (coincident $a_k$, and $E'(z)$ printed
    where $E'(0)$ is meant) were confirmed against the print and are not new corrections.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    (a) is Lagrange interpolation, with the degree bound and the interpolation property checked.
    (b) uses the Weierstrass product $E$: $E(z)/z$ and $E(z)/(z-a_k)$ are entire with values
    $E'(0)\ne0$ at $0$ and $E'(a_k)\ne0$ at $a_k$, so with the printed $E'(z)$ replaced by $E'(0)$
    the $k$-th summand vanishes at $0$ and the whole sum takes the value $b_j$ at $a_j$; $m_k\ge1$
    is then chosen so that the summand is at most $2^{-k}$ on $|z|\le|a_k|/2$, which gives local
    uniform convergence. Nothing is left in outline.
---

::: {.exercise}
Given two countably infinite sequences of complex numbers $\{a_k\}_{k=0}^{\infty}$ and $\{b_k\}_{k=0}^{\infty}$ with $\lim_{k\to\infty}\abs{a_k}=\infty$, it is always possible to find an entire function $F$ satisfying $F(a_k)=b_k$ for all $k$.

(a) Given $n$ distinct complex numbers $a_1,\ldots,a_n$ and another $n$ complex numbers $b_1,\ldots,b_n$, construct a polynomial $P$ of degree at most $n-1$ with $P(a_i)=b_i$ for $i=1,\ldots,n$.

(b) Let $\{a_k\}_{k=0}^{\infty}$ be a sequence of distinct complex numbers with $a_0=0$ and $\lim_{k\to\infty}\abs{a_k}=\infty$. Let $E$ be a Weierstrass product associated with $\{a_k\}$. Given complex numbers $\{b_k\}_{k=0}^{\infty}$, show that integers $m_k\geq1$ can be chosen so that
$$
F(z)=\frac{b_0}{E'(z)}\frac{E(z)}{z}
+\sum_{k=1}^{\infty}\frac{b_k}{E'(a_k)}\frac{E(z)}{z-a_k}\left(\frac{z}{a_k}\right)^{m_k}
$$
defines an entire function with $F(a_k)=b_k$ for every $k\geq0$. This is the Pringsheim interpolation formula.
:::

::: {.remark}
The source's opening claim needs the interpolation values to agree whenever two $a_k$ coincide. Its formula in (b) prints $E'(z)$ in the first denominator. This makes that summand meromorphic at zeros of $E'$ and gives $F(0)=b_0$ only after replacing it with $E'(0)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Part (a): for distinct $a_1,\dots,a_n$ and arbitrary $b_1,\dots,b_n$ there is a polynomial $P$ of degree at most $n-1$ with $P(a_i)=b_i$.

::: pf-proof

Set
$$
P(z)=\sum_{i=1}^{n}b_i\prod_{j\ne i}\frac{z-a_j}{a_i-a_j},
$$
which is legitimate because $a_i-a_j\ne0$ for $j\ne i$. Each product is a polynomial of degree $n-1$, so $\deg P\le n-1$. For $z=a_i$ every product with $j\ne i$ contains the factor $a_i-a_i=0$, and the $i$-th product equals $1$; hence $P(a_i)=b_i$.

:::

:::

::: {.pf-step #s2}

Part (b): let $\{a_k\}_{k\ge0}$ be distinct with $a_0=0$ and $\abs{a_k}\to\infty$, and let $E$ be a Weierstrass product for $\{a_k\}$, so that $E$ is entire with simple zeros exactly at the $a_k$. Then $E(z)/z$ is entire with $E(z)/z\to E'(0)\ne0$ at $0$, and for $k\ge1$ the function $E(z)/(z-a_k)$ is entire with value $E'(a_k)\ne0$ at $z=a_k$.

::: pf-proof

$E$ has a simple zero at $a_0=0$, so $E(z)=z\,E_1(z)$ with $E_1$ entire and $E_1(0)=E'(0)\ne0$. For $k\ge1$, $E$ has a simple zero at $a_k$, so $E(z)=(z-a_k)E_k(z)$ with $E_k$ entire and $E_k(a_k)=E'(a_k)\ne0$.

:::

:::

::: {.pf-step #s3}

There are integers $m_k\ge1$ such that the $k$-th summand
$$
g_k(z)=\frac{b_k}{E'(a_k)}\,\frac{E(z)}{z-a_k}\Bigl(\frac{z}{a_k}\Bigr)^{m_k},\qquad k\ge1,
$$
satisfies $\sup_{\abs{z}\le\abs{a_k}/2}\abs{g_k(z)}\le2^{-k}$.

::: pf-proof

Put $M_k=\sup_{\abs{z}\le\abs{a_k}/2}\abs{E(z)}<\infty$. On $\abs{z}\le\abs{a_k}/2$ we have $\abs{z-a_k}\ge\abs{a_k}/2$ and $\abs{z/a_k}\le1/2$, so
$$
\abs{g_k(z)}\le\frac{\abs{b_k}}{\abs{E'(a_k)}}\cdot\frac{2M_k}{\abs{a_k}}\cdot2^{-m_k}.
$$
If $b_k=0$ take $m_k=1$. If $b_k\ne0$, the factor in front is a fixed positive number, and taking $m_k\ge1$ with
$$
2^{-m_k}\le 2^{-k}\,\frac{\abs{E'(a_k)}\,\abs{a_k}}{2\,\abs{b_k}\,M_k}
$$
gives the bound. Such an $m_k$ exists because the right-hand side is positive.

:::

:::

::: {.pf-step #s4}

With $E'(0)$ in place of the printed $E'(z)$, the function
$$
F(z)=\frac{b_0}{E'(0)}\,\frac{E(z)}{z}+\sum_{k\ge1}\frac{b_k}{E'(a_k)}\,\frac{E(z)}{z-a_k}\Bigl(\frac{z}{a_k}\Bigr)^{m_k}
$$
is entire and satisfies $F(a_k)=b_k$ for every $k\ge0$.

::: pf-proof

*Convergence.* Let $R>0$. For every $k$ with $\abs{a_k}\ge2R$ the estimate of step [](#s3){.pf-ref} applies on $\abs{z}\le R\subseteq\abs{z}\le\abs{a_k}/2$, so the tail over those $k$ is bounded by $\sum2^{-k}$ there; since $\abs{a_k}\to\infty$ only finitely many $k$ fail the condition, and each remaining $g_k$ is entire. So the series converges uniformly on $\abs{z}\le R$, and its sum is entire; the first term is entire by step [](#s2){.pf-ref}. Hence $F$ is entire.

*Values at the $a_k$.* At $z=0$ the first term equals $\frac{b_0}{E'(0)}E'(0)=b_0$ by step [](#s2){.pf-ref}, while every $g_k$ vanishes at $0$ because $E(0)=0$ and $m_k\ge1$. At $z=a_j$ with $j\ge1$ the first term vanishes since $E(a_j)=0$; every $g_k$ with $k\ne j$ vanishes at $a_j$ for the same reason; and
$$
g_j(a_j)=\frac{b_j}{E'(a_j)}\,E'(a_j)\cdot1^{m_j}=b_j,
$$
by step [](#s2){.pf-ref}. Hence $F(a_k)=b_k$ for all $k\ge0$.

:::

:::

:::

:::

::: {.remark}
The exercise's opening claim fails when two of the $a_k$ coincide with different prescribed values, so distinctness of $\{a_k\}$ is part of the hypothesis of part (b), as the card already records. The printed first denominator $E'(z)$ makes that summand meromorphic at the zeros of $E'$; the entire function is obtained by replacing it with the constant $E'(0)$, which is what step [](#s4){.pf-ref} uses and what keeps the value $b_0$ at the origin.
:::
