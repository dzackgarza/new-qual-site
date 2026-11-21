---
schema: qual/card@1
id: P-BKS03-7B
kind: problem
title: Two fixed points force a disk self-map to be the identity
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the retained sheet's argument (Spring 2003
    prelim solutions, Problem 7B, PDF p. 6, the file named in the collection's provenance),
    now cited on the body; the card previously carried no citation. Added: the explicit
    automorphism $S(\zeta)=(\zeta+z_1)/(1+\bar z_1\zeta)$, the removability of the singularity
    of $g(z)/z$ at $0$ with $h(0)=g'(0)$, and the two uses of the maximum principle kept
    apart — first on the closed disk of radius $1-\varepsilon$ to get $|h|\le1/(1-\varepsilon)$
    and then at the interior point $y$ where $|h(y)|=1$ — instead of the sheet's single
    sentence. Also noted: the sheet prints $S(0)=x_1$ where its notation has $z_1$. The
    statement and the conclusion are unchanged.
---

::: {.problem}
Let $f$ be analytic on the unit disk with $\abs{f(z)}\le1$.
If $f$ has two distinct fixed points in the disk, prove that $f(z)=z$ identically.
:::

::: {.solution}
The published solution is the collection's own retained sheet, **Spring 2003 prelim solutions, Problem 7B** (`assets/attachments/s03solution.pdf`, the file named in this collection's `provenance`): the normalization by a disk automorphism, the function $h=g/z$, the bound $\abs h\le1$ by the maximum principle, and the conclusion $h\equiv1$ are that solution's. The sheet prints "$S(0)=x_1$" where its own notation has $z_1$; the card uses $z_1$. The card also separates the two uses of the maximum principle, which the sheet invokes twice in one sentence.

Throughout $f$ is analytic on $\DD=\theset{\abs z<1}$ with $\abs{f(z)}\le1$ there, and $z_1\ne z_2$ are the two fixed points, $f(z_j)=z_j$.

::: pf

::: {.pf-step #normalize}
There is a disk automorphism $S$ with $S(0)=z_1$, and $g\coloneqq S^{-1}\circ f\circ S$ is analytic on $\DD$ with $\abs{g}\le1$ and fixed points $0$ and $y\coloneqq S^{-1}(z_2)\ne0$.

::: pf-proof
For $z_1\in\DD$ the map $S(\zeta)=(\zeta+z_1)/(1+\bar z_1\zeta)$ is a biholomorphic automorphism of $\DD$ with $S(0)=z_1$ and inverse of the same form. Then $g$ is a composite of analytic maps, so analytic; $\abs g\le1$ because $\abs f\le1$ and $S,S^{-1}$ preserve $\DD$; and
$$
g(0)=S^{-1}f(S(0))=S^{-1}f(z_1)=S^{-1}(z_1)=0,\qquad g(y)=S^{-1}f(S(y))=S^{-1}f(z_2)=S^{-1}(z_2)=y .
$$
Finally $y\ne0$ because $z_2\ne z_1=S(0)$ and $S^{-1}$ is injective.

:::

:::

::: {.pf-step #h}
$h(z)\coloneqq g(z)/z$ extends to an analytic function on $\DD$.

::: pf-proof
$g$ is analytic on $\DD$ and $g(0)=0$ by step [](#normalize){.pf-ref}, so the quotient $g(z)/z$ is analytic on $\DD-\theset{0}$ and bounded near $0$ — indeed $g(z)/z\to g'(0)$ — so $0$ is a removable singularity (Riemann's theorem) and $h$ extends analytically, with $h(0)=g'(0)$.

:::

:::

::: {.pf-step #bound}
$\abs{h(z)}\le1$ for all $z\in\DD$.

::: pf-proof
Fix $\varepsilon\in(0,1)$ and consider the closed disk $\abs z\le1-\varepsilon$. On its boundary $\abs z=1-\varepsilon$ we have
$$
\abs{h(z)}=\frac{\abs{g(z)}}{\abs z}\le\frac{1}{1-\varepsilon},
$$
so by the maximum modulus principle $\abs{h(z)}\le1/(1-\varepsilon)$ on the whole disk. Letting $\varepsilon\to0$ gives $\abs{h(z)}\le1$ at each fixed $z\in\DD$.

:::

:::

::: {.pf-step #constant}
$h\equiv1$ on $\DD$.

::: pf-proof
By step [](#normalize){.pf-ref} and step [](#h){.pf-ref},
$$
h(y)=\frac{g(y)}{y}=\frac{y}{y}=1 .
$$
So the maximum of $\abs h$ on $\DD$, which is at most $1$ by step [](#bound){.pf-ref}, is attained at the interior point $y$. The maximum modulus principle then forces $h$ to be constant, and since $h(y)=1$ the constant is $1$.

:::

:::

::: {.pf-step #conclusion}
$f(z)=z$ for all $z\in\DD$.

::: pf-proof
$h\equiv1$ means $g(z)=z$ for $z\ne0$ and, by continuity, also at $0$. Then $f=S\circ g\circ S^{-1}$ is $S\circ S^{-1}=\mathrm{id}$ on $\DD$.

:::

:::

:::
:::
