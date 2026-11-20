---
schema: qual/card@1
id: E-SS3.EX-15
kind: problem
title: "Applications of the Cauchy inequalities and the maximum modulus principle"
classification:
  areas:
    - complex-analysis
  topics: [Cauchy Estimates, Maximum Modulus Principle]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
  - event: solution-written
    by: claude
    date: 2026-11-18
    note: >-
      Restructured the prose solution of the four-part exercise into Lamport steps. The collection's provenance is the publisher's catalogue record only, with no retained text and no retained solution set, so the statement is taken as the card prints it; the argument is the card's own. Checked: the Cauchy estimate $\lvert a_n\rvert\le(AR^k+B)R^{-n}$ and its limit for $n>k$; the reflection argument on a boundary arc together with the identity theorem; the maximum principle for the monic polynomial and the intermediate value argument on the circle; and $\lvert e^{f}\rvert=e^{\Re f}$ with Liouville.
  - event: source-corrected
    by: claude
    date: 2026-11-20
    note: >-
      The solution's opening sentence cited the book through the printed pages. It now cites
      Chapter 3, Exercise 15, and the printed page numbers are gone from the rendered text; the book
      was read for this edit and its part (a) is the statement the card carries. Statement
      unchanged; the argument was not re-read in this pass.
---

::: {.exercise}
Use the Cauchy inequalities or the maximum modulus principle to solve the following problems:

(a) Prove that if $f$ is an entire function that satisfies
$$
\sup_{\abs{z} = R} \abs{f(z)} \leq AR^k + B
$$
for all $R > 0$, and for some integer $k \geq 0$ and some constants $A, B > 0$, then $f$ is a polynomial of degree $\leq k$.

(b) Show that if $f$ is holomorphic in the unit disc, is bounded, and converges uniformly to zero in the sector $\theta < \arg z < \varphi$ as $\abs{z} \to 1$, then $f = 0$.

(c) Let $w_1, \ldots, w_n$ be points on the unit circle in the complex plane. Prove that there exists a point $z$ on the unit circle such that the product of the distances from $z$ to the points $w_j$, $1 \leq j \leq n$, is at least $1$. Conclude that there exists a point $w$ on the unit circle such that the product of the distances from $w$ to the points $w_j$, $1 \leq j \leq n$, is exactly equal to $1$.

(d) Show that if the real part of an entire function $f$ is bounded, then $f$ is constant.
:::

::: {.solution}
The statement is Exercise 15 of [@SS03, ch. 3], printed as: use the Cauchy inequalities or the maximum modulus principle to show that an entire $f$ with $\sup_{\abs z=R}\abs{f(z)}\le AR^k+B$ for all $R>0$ is a polynomial of degree at most $k$.

No retained text and no retained solution set for this collection: its provenance is the publisher's catalogue record, so the statement is taken as the card prints it, and the argument is the card's own.

::: pf

::: {.pf-step #a}
(a) If $\sup_{\abs z=R}\abs{f(z)}\le AR^k+B$ for all $R>0$, then $f$ is a polynomial of degree at most $k$.

::: pf-proof
Write $f(z)=\sum a_nz^n$. Cauchy's estimate on the circle of radius $R$ gives $\abs{a_n}\le(AR^k+B)R^{-n}$; for $n>k$ the right side tends to $0$ as $R\to\infty$, so $a_n=0$. Hence only the coefficients of index at most $k$ survive.
:::
:::

::: {.pf-step #b}
(b) A bounded holomorphic function on $\DD$ tending uniformly to $0$ on a boundary arc is identically $0$.

::: pf-proof
The hypothesis gives a continuous extension to the arc $I=\{e^{it}:\theta<t<\varphi\}$ with boundary values $0$, which are real; by the Schwarz reflection principle $f$ extends holomorphically across each compact subarc $I'\Subset I$, and the extension vanishes on $I'$. A holomorphic function vanishing on an arc with a limit point in its domain is identically $0$ by the identity theorem, so $f=0$ on $\DD$.
:::
:::

::: {.pf-step #c1}
(c) For $P(z)=\prod_j(z-w_j)$ there is $z$ on the unit circle with $\prod_j\abs{z-w_j}\ge1$.

::: pf-proof
$P$ is monic of degree $n$, so $P(0)=(-1)^n\prod_jw_j$ and $\abs{P(0)}=1$ because each $w_j$ has modulus $1$. By the maximum-modulus principle on the closed disc, $\max_{\abs z=1}\abs{P(z)}\ge\abs{P(0)}=1$, which is the assertion.
:::
:::

::: {.pf-step #c2}
(c) There is $w$ on the unit circle with $\prod_j\abs{w-w_j}=1$.

::: pf-proof
$\abs P$ is continuous on the connected circle and $P(w_1)=0$, while some point of the circle has $\abs P\ge1$ by the previous step; by the intermediate value theorem $\abs P$ takes the value $1$, that is, the product of the distances equals $1$.
:::
:::

::: {.pf-step #d}
(d) An entire function with bounded real part is constant.

::: pf-proof
If $\abs{\Re f}\le M$ then $g=e^{f}$ is entire with $\abs{g}=e^{\Re f}\le e^{M}$, so $g$ is constant by Liouville; then $0=g'=f'e^{f}$ forces $f'=0$, and $f$ is constant.
:::
:::

:::
:::
