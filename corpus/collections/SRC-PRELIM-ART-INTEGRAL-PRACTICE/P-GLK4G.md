---
schema: qual/card@1
id: P-GLK4G
kind: problem
title: Antiderivatives of $e^{x^{1/a}}$, $e^x\sin x$, and $e^x\cos x$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - u-Substitution
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Corrected the missing factor 3 in the cube-root exponential antiderivative.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    No source document is retained for this card. The collection
    SRC-PRELIM-ART-INTEGRAL-PRACTICE has an empty provenance list, its own
    remark records that the drill sheet's original paper was not found, and
    searching assets/attachments/ and the migration records finds no copy of the
    sheet, so there is no page to read and the printed statement could not be
    compared with a source document. What was checked here is the statement and
    its answer: the reduction by u = x^{1/a}, the two cases a = 2 and a = 3, and all three remaining primitives, each checked by differentiating
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. A substitution reducing the first three to polynomial-times-exponential integrals, the standard by-parts pair for e^x sin x and e^x cos x, and a substitution for the last.
---

::: {.problem}
Use $u=x^{1/a}$ to reduce
$$
\int e^{x^{1/a}}\,dx,
$$
and evaluate the special cases
$$
\int e^{\sqrt x}\,dx,
\qquad
\int e^{\sqrt[3]x}\,dx.
$$
Also evaluate
$$
\int e^x\sin x\,dx,
\qquad
\int \frac{\sin(\sqrt x)e^{\sqrt x}}{\sqrt x}\,dx,
\qquad
\int e^x\cos x\,dx.
$$
:::

::: {.solution}

All the integrands are continuous on their domains: $x^{1/a}$ requires $x\ge0$
for the stated real powers, and the last integrand requires $x>0$.

::: pf

::: {.pf-step #reduction}

With $u=x^{1/a}$, $x=u^a$ and $dx=au^{a-1}du$, so $\displaystyle\int
e^{x^{1/a}}dx=a\int u^{a-1}e^u\,du$.

::: pf-proof

The substitution $x=u^a$ has $\frac{dx}{du}=au^{a-1}$, and $x^{1/a}=u$; so the
integrand $e^{x^{1/a}}dx$ becomes $e^u\cdot au^{a-1}du$. For $a$ a positive
integer the resulting integral $\int u^{a-1}e^u\,du$ is computed by $a-1$
integrations by parts, each reducing the power of $u$ by one.

:::

:::

::: {.pf-step #second-and-third}

$\displaystyle\int e^{\sqrt x}\,dx=2(\sqrt x-1)e^{\sqrt x}+C$ and
$\displaystyle\int
e^{\sqrt[3]x}\,dx=3\left(x^{2/3}-2x^{1/3}+2\right)e^{x^{1/3}}+C$.

::: pf-proof

For $a=2$, step [](#reduction){.pf-ref} gives $2\int ue^u\,du=2(u-1)e^u+C$ by
one integration by parts. For $a=3$ it gives $3\int u^2e^u\,du$, and two
integrations by parts give $\int u^2e^u\,du=(u^2-2u+2)e^u+C$; substituting
$u=x^{1/3}$ gives the stated form. Both answers are checked by
differentiating: $\frac{d}{dx}2(\sqrt x-1)e^{\sqrt x}=2\left(\frac{1}{2\sqrt
x}e^{\sqrt x}+(\sqrt x-1)\frac{e^{\sqrt x}}{2\sqrt x}\right)=\frac{e^{\sqrt
x}}{\sqrt x}\left(1+\sqrt x-1\right)=e^{\sqrt x}$.

:::

:::

::: {.pf-step #byparts}

$\displaystyle\int e^x\sin x\,dx=\frac12e^x(\sin x-\cos x)+C$ and
$\displaystyle\int e^x\cos x\,dx=\frac12e^x(\cos x+\sin x)+C$.

::: pf-proof

Let $I=\int e^x\sin x\,dx$ and $J=\int e^x\cos x\,dx$. Integrating by parts
gives $I=e^x\sin x-J$ and $J=e^x\cos x+I$; solving the pair, $I+J=e^x\sin x$
and $J-I=e^x\cos x$, gives $I=\frac12e^x(\sin x-\cos x)$ and
$J=\frac12e^x(\cos x+\sin x)$. Differentiating the first, $\frac12e^x(\sin
x-\cos x)+\frac12e^x(\cos x+\sin x)=e^x\sin x$, and the second similarly.

:::

:::

::: {.pf-step #square-root}

$\displaystyle\int\frac{\sin(\sqrt x)e^{\sqrt x}}{\sqrt x}\,dx=e^{\sqrt
x}\left(\sin\sqrt x-\cos\sqrt x\right)+C$.

::: pf-proof

Put $u=\sqrt x$, so $x=u^2$ and $dx=2u\,du$, and the integrand becomes
$\frac{\sin u\,e^u}{u}\cdot2u\,du=2e^u\sin u\,du$. By step
[](#byparts){.pf-ref} this is $2\cdot\frac12e^u(\sin u-\cos u)+C=e^u(\sin
u-\cos u)+C$, and substituting $u=\sqrt x$ gives the answer; differentiating
it checks it, since $\frac{d}{dx}\left(e^{\sqrt x}(\sin\sqrt x-\cos\sqrt
x)\right)=\frac{e^{\sqrt x}}{2\sqrt x}\left[(\sin\sqrt x-\cos\sqrt
x)+(\cos\sqrt x+\sin\sqrt x)\right]=\frac{\sin(\sqrt x)e^{\sqrt x}}{\sqrt x}$.

:::

:::

:::


:::
