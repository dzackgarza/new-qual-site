---
schema: qual/card@1
id: E-SS5.PR-4
kind: problem
title: Growth order of an entire function from its Taylor coefficients
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there, with one substantive change of
    route in part (b): the card previously closed by citing Problem 3 of the same chapter.
    The bound it needs is now proved here instead, by splitting the factorial series at
    N = ceil(r^(rho+2 eps)) and bounding the two pieces separately, so the card no longer
    depends on another card's result. Part (a) keeps the Cauchy estimate and the choice of
    the radius attaining the minimum of u^(-n)e^(u^rho), with the arithmetic of that
    substitution written out. Not checked: the book's own text of the problem, since no copy
    of Stein and Shakarchi is retained in this checkout; the statement is as transcribed on
    the card. No retained solution set covers the exercise (the collection's provenance is a
    Google Books record), so the argument is the card's own. No statement repair.
---

::: {.exercise}
Let

$$
F(z)=\sum_{n=0}^{\infty}a_nz^n
$$

be an entire function of finite order.
The growth order of $F$ is linked with the growth of the coefficients $a_n$ as $n\to\infty$.

(a) Suppose that

$$
\abs{F(z)}\leq Ae^{a\abs{z}^\rho}.
$$

Show that

$$
\limsup_{n\to\infty}\abs{a_n}^{1/n}n^{1/\rho}<\infty.
\tag{8}
$$

(b) Conversely, if (8) holds, show that

$$
\abs{F(z)}\leq A_\varepsilon e^{a_\varepsilon\abs{z}^{\rho+\varepsilon}}
$$

for every $\varepsilon>0$.

*Hint.* For part (a), use Cauchy's inequality

$$
\abs{a_n}\leq \frac{A}{r^n}e^{ar^\rho}
$$

and the fact that $u^{-n}e^{u^\rho}$, for $u>0$, has minimum

$$
e^{n/\rho}\left(\frac{\rho}{n}\right)^{n/\rho}
$$

at $u=n^{1/\rho}/\rho^{1/\rho}$.
Choose $r$ in terms of $n$ to attain this minimum.

For part (b), note that for $\abs{z}=r$,

$$
\abs{F(z)}
\leq \sum_n\frac{c^nr^n}{n^{n/\rho}}
\leq \sum_n\frac{c^nr^n}{(n!)^{1/\rho}}
$$

for some constant $c$, since $n^n\geq n!$.
This reduces the problem to Problem 3.
:::

::: {.solution}
No retained solution set covers this problem: the collection's provenance is a Google Books record, so the argument is the card's own. Let $F(z)=\sum_{n\ge0}a_nz^n$ be entire with $\abs{F(z)}\le Ae^{a\abs{z}^\rho}$ for some $A,a,\rho>0$.

::: pf

::: {.pf-step #cauchy}
(a) For every $r>0$ and $n\ge0$, $\abs{a_n}\le\dfrac{A}{r^n}e^{ar^\rho}$.

::: pf-proof
By Cauchy's integral formula for the circle $\abs{z}=r$, $a_n=\frac{1}{2\pi i}\oint_{\abs{z}=r}\frac{F(z)}{z^{n+1}}dz$, so
$$
\abs{a_n}\le\frac{1}{2\pi}\cdot2\pi r\cdot\frac{\sup_{\abs{z}=r}\abs{F}}{r^{n+1}}\le\frac{Ae^{ar^\rho}}{r^n},
$$
using the growth hypothesis to bound $\abs{F}$ on that circle. This is Cauchy's inequality.
:::

:::

::: {.pf-step #choose}
(a) With $r_n=\bigl(n/(a\rho)\bigr)^{1/\rho}$, for $n\ge1$,
$$
\abs{a_n}\le Ae^{n/\rho}\Bigl(\frac{a\rho}{n}\Bigr)^{n/\rho}.
$$

::: pf-proof
Here $ar_n^\rho=a\cdot\frac{n}{a\rho}=\frac{n}{\rho}$ and $r_n^n=\bigl(n/(a\rho)\bigr)^{n/\rho}$, so $1/r_n^n=(a\rho/n)^{n/\rho}$; substituting into step [](#cauchy){.pf-ref} gives the display. The radius $r_n$ is where $u^{-n}e^{au^\rho}$ is smallest: its log is $-n\log u+au^\rho$, with derivative $-n/u+a\rho u^{\rho-1}$, which vanishes at $u^\rho=n/(a\rho)$.
:::

:::

::: {.pf-step #part_a}
(a) $\displaystyle\limsup_{n\to\infty}\abs{a_n}^{1/n}n^{1/\rho}\le e^{1/\rho}(a\rho)^{1/\rho}<\infty$.

::: pf-proof
Take the $n$-th root of the display in step [](#choose){.pf-ref}: $\abs{a_n}^{1/n}\le A^{1/n}e^{1/\rho}\bigl(\frac{a\rho}{n}\bigr)^{1/\rho}=A^{1/n}e^{1/\rho}(a\rho)^{1/\rho}n^{-1/\rho}$. Multiplying by $n^{1/\rho}$ gives $\abs{a_n}^{1/n}n^{1/\rho}\le A^{1/n}e^{1/\rho}(a\rho)^{1/\rho}$ for every $n\ge1$, and $A^{1/n}\to1$, so the limsup is at most $e^{1/\rho}(a\rho)^{1/\rho}$, which is finite. This is (8).
:::

:::

::: {.pf-step #coeffs}
(b) If (8) holds, there is $C>0$ with $\abs{a_n}\le C^n n^{-n/\rho}$ for every $n\ge1$.

::: pf-proof
By (8) there are $C_0$ and $N_0$ with $\abs{a_n}^{1/n}n^{1/\rho}\le C_0$ for $n\ge N_0$, that is $\abs{a_n}\le C_0^nn^{-n/\rho}$. For the finitely many $n<N_0$ replace $C_0$ by a larger $C\ge1$ such that also $\abs{a_n}\le C^nn^{-n/\rho}$: since $n^{-n/\rho}\ge n^{-n/\rho}$ is positive, it suffices to take $C^n\ge\abs{a_n}n^{n/\rho}$ for those $n$, which finitely many conditions allow.
:::

:::

::: {.pf-step #series}
(b) $\abs{F(z)}\le\abs{a_0}+\displaystyle\sum_{n\ge1}\frac{(C\abs{z})^n}{n^{n/\rho}}$ for every $z$.

::: pf-proof
$\abs{F(z)}\le\sum_n\abs{a_n}\abs{z}^n$ since the series converges absolutely on every disc, and step [](#coeffs){.pf-ref} bounds each term for $n\ge1$; the $n=0$ term is $\abs{a_0}$.
:::

:::

::: {.pf-step #split}
(b) For $\varepsilon>0$, $r=\abs{z}$ and $N=\lceil r^{\rho+2\varepsilon}\rceil$,
$$
\sum_{n\ge1}\frac{(Cr)^n}{n^{n/\rho}}\le N\bigl(Ce^{1/\rho}r\bigr)^{N}+\sum_{n>N}\Bigl(\frac{Ce^{1/\rho}r}{N^{1/\rho}}\Bigr)^{n}.
$$

::: pf-proof
Bound $n^{-n/\rho}\le(e/n)^{n/\rho}$ in two steps: $n!\le n^n$ gives $1/n^{n/\rho}\le1/(n!)^{1/\rho}$, and $n!\ge(n/e)^n$ gives $1/(n!)^{1/\rho}\le(e/n)^{n/\rho}$. So the $n$-th term is at most $\bigl(Ce^{1/\rho}r/n^{1/\rho}\bigr)^n$. For $n\le N$ the factor $n^{-1/\rho}\le1$ gives the bound $(Ce^{1/\rho}r)^n\le(Ce^{1/\rho}r)^N$, and there are $N$ such terms; for $n>N$ the factor $n^{-n/\rho}\le N^{-n/\rho}$ gives $\bigl(Ce^{1/\rho}r/N^{1/\rho}\bigr)^n$.
:::

:::

::: {.pf-step #bounds}
(b) The two pieces of step [](#split){.pf-ref} are $O(e^{a_\varepsilon r^{\rho+3\varepsilon}})$ and $O(1)$.

::: pf-proof
Let $K=Ce^{1/\rho}$. First piece: for $r\ge1$, $\log\bigl(N(Kr)^N\bigr)=N\log N+N\log(Kr)\le a_\varepsilon r^{\rho+2\varepsilon}\log r$ for a suitable $a_\varepsilon$, because $N\le r^{\rho+2\varepsilon}+1$ and $\log(Kr)\le c_\varepsilon r^{\varepsilon}$; so the piece is at most $e^{a_\varepsilon r^{\rho+3\varepsilon}}$.
Second piece: $N^{1/\rho}\ge r^{1+2\varepsilon/\rho}$, so $Kr/N^{1/\rho}\le Kr^{-2\varepsilon/\rho}\le\frac12$ for $r\ge r_0(\varepsilon)$, and then the sum is at most $\sum_{n>N}2^{-n}\le1$.
:::

:::

::: {.pf-step #part_b}
(b) For every $\varepsilon>0$ there are $A_\varepsilon,a_\varepsilon>0$ with $\abs{F(z)}\le A_\varepsilon e^{a_\varepsilon\abs{z}^{\rho+\varepsilon}}$.

::: pf-proof
Let $\varepsilon>0$ and put $\varepsilon'=\varepsilon/3$. Steps [](#series){.pf-ref}, [](#split){.pf-ref} and [](#bounds){.pf-ref} give, for $r=\abs{z}\ge r_0$, $\abs{F(z)}\le\abs{a_0}+e^{a_{\varepsilon'}r^{\rho+3\varepsilon'}}+1\le A_\varepsilon e^{a_\varepsilon r^{\rho+\varepsilon}}$ after absorbing the additive constant into $A_\varepsilon$ and enlarging $a_\varepsilon$ so that the bound holds for all $r$, including $r<r_0$ where a continuous function on a compact set is bounded. Since $\varepsilon$ was arbitrary, this is the asserted conclusion.
:::

:::

:::

:::
