---
schema: qual/card@1
id: P-RVMWA
kind: problem
title: Antiderivatives of powers of $\sin x$ and $\cos x$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometry
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
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
    its answer: the power-reduction identities, the two substitutions for odd powers, the expansions of the two cubes, the fourth-power reductions and the difference of squares, each primitive checked by differentiating
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. Power-reduction identities for the even powers, substitutions for the odd powers, expansion for the cubes of sums, and one substitution for the nested-radical integral.
---

::: {.problem}
Evaluate the antiderivatives
$$
\int\sin^2x\,dx,\quad \int\cos^2x\,dx,\quad
\int\sin^3x\,dx,\quad \int\cos^3x\,dx,
$$
$$
\int(1+\sin x)^3\,dx,\quad
\int(1+\cos x)^3\,dx,
$$
$$
\int\sin^4x\,dx,\quad \int\cos^4x\,dx,
\quad \int(\cos^4x-\sin^4x)\,dx,
$$
and
$$
\int \frac{\sin^3\sqrt x}{2\sqrt x}\,dx.
$$
:::

::: {.solution}

All integrands are continuous on $\RR$ except the last, which is continuous on
$x>0$; the identities used are the power-reduction formulas and
$\sin^2x+\cos^2x=1$.

::: pf

::: {.pf-step #square}

$\displaystyle\int\sin^2x\,dx=\frac12(x-\sin x\cos x)+C$ and
$\displaystyle\int\cos^2x\,dx=\frac12(x+\sin x\cos x)+C$.

::: pf-proof

From $\cos2x=1-2\sin^2x$ and $\cos2x=2\cos^2x-1$, $\sin^2x=\frac12(1-\cos2x)$
and $\cos^2x=\frac12(1+\cos2x)$; integrating gives $\frac12x-\frac14\sin2x$
and $\frac12x+\frac14\sin2x$, and $\frac14\sin2x=\frac12\sin x\cos x$ rewrites
these as stated. Differentiating the first gives
$\frac12-\frac12(\cos^2x-\sin^2x)=\frac12(1-\cos2x)=\sin^2x$.

:::

:::

::: {.pf-step #cube}

$\displaystyle\int\sin^3x\,dx=\frac13\cos^3x-\cos x+C$ and
$\displaystyle\int\cos^3x\,dx=\sin x-\frac13\sin^3x+C$.

::: pf-proof

$\sin^3x=(1-\cos^2x)\sin x$, so with $u=\cos x$, $du=-\sin x\,dx$ the first
integral is $\int(u^2-1)du=\frac13u^3-u$, giving the stated form.
$\cos^3x=(1-\sin^2x)\cos x$ with $v=\sin x$ gives
$\int(1-v^2)dv=v-\frac13v^3$. Differentiating the first answer gives
$\cos^2x(-\sin x)+\sin x=(1-\cos^2x)\sin x$; similarly for the second.

:::

:::

::: {.pf-step #cubes-of-sums}

$\displaystyle\int(1+\sin x)^3dx=\frac52x+\frac13\cos^3x-4\cos
x-\frac34\sin2x+C$ and $\displaystyle\int(1+\cos
x)^3dx=\frac52x-\frac13\sin^3x+4\sin x+\frac34\sin2x+C$.

::: pf-proof

Expanding, $(1+\sin x)^3=1+3\sin x+3\sin^2x+\sin^3x$; integrating termwise
with steps [](#square){.pf-ref} and [](#cube){.pf-ref} gives $x-3\cos
x+3\cdot\frac12(x-\sin x\cos x)+\frac13\cos^3x-\cos
x=\frac52x+\frac13\cos^3x-4\cos x-\frac34\sin2x$, using $\frac32\sin x\cos
x=\frac34\sin2x$. The second is the same computation with $\sin$ and $\cos$
exchanged and the two signs in step [](#square){.pf-ref} swapped, giving the
stated form.

:::

:::

::: {.pf-step #fourth}

$\displaystyle\int\sin^4x\,dx=\frac38x-\frac38\sin x\cos x-\frac14\sin^3x\cos
x+C$ and $\displaystyle\int\cos^4x\,dx=\frac38x+\frac38\sin x\cos
x+\frac14\sin x\cos^3x+C$.

::: pf-proof

Write
$\sin^4x=\left(\frac{1-\cos2x}{2}\right)^2=\frac14-\frac12\cos2x+\frac14\cos^22x$
and use $\cos^22x=\frac{1+\cos4x}{2}$: then
$\sin^4x=\frac38-\frac12\cos2x+\frac18\cos4x$, whose primitive is
$\frac38x-\frac14\sin2x+\frac1{32}\sin4x$. The stated form equals it, because
$\frac38\sin x\cos x=\frac3{16}\sin2x$ and $\frac14\sin^3x\cos
x=\frac18\sin^2x\sin2x=\frac1{16}(1-\cos2x)\sin2x=\frac1{16}\sin2x-\frac1{32}\sin4x$,
so the trigonometric part is
$-\frac3{16}\sin2x-\frac1{16}\sin2x+\frac1{32}\sin4x=-\frac14\sin2x+\frac1{32}\sin4x$.
The cosine case is the same with $\frac{1+\cos2x}{2}$, and the corresponding
computation gives $\frac38x+\frac14\sin2x+\frac1{32}\sin4x$, which the stated
form equals by the same two identities with $\frac14\sin
x\cos^3x=\frac18\sin2x\cos^2x=\frac1{16}\sin2x+\frac1{32}\sin4x$.

:::

:::

::: {.pf-step #difference}

$\displaystyle\int(\cos^4x-\sin^4x)\,dx=\frac12\sin2x+C$, and with $u=\sqrt
x$, $\displaystyle\int\frac{\sin^3\sqrt x}{2\sqrt x}dx=\frac13\cos^3\sqrt
x-\cos\sqrt x+C$.

::: pf-proof

$\cos^4x-\sin^4x=(\cos^2x-\sin^2x)(\cos^2x+\sin^2x)=\cos2x$, whose primitive
is $\frac12\sin2x$. For the second, $u=\sqrt x$ gives $du=\frac{dx}{2\sqrt
x}$, so the integral is $\int\sin^3u\,du=\frac13\cos^3u-\cos u$, which is step
[](#cube){.pf-ref} with $u$ in place of $x$.

:::

:::

:::


:::
