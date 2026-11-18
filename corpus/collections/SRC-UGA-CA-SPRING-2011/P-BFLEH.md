---
schema: qual/card@1
id: P-BFLEH
kind: problem
title: $\int_0^\infty\frac{\cos x-\cos 4x}{x^2}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: integration by
    parts with the boundary term vanishing at both ends (at 0 because 1 - cos(ax) =
    a^2x^2/2 + O(x^4)), the reduction of the sine integral to the Dirichlet integral
    int sin t / t = pi/2 by the indented upper-half-plane contour for e^{iz}/z, the formula
    pi a / 2, and the identification cos x - cos 4x = (1 - cos 4x) - (1 - cos x) with the
    convergence that licenses subtracting. The answer 3 pi / 2 is unchanged. The collection's
    provenance is the examination paper only, so no retained solution set covers the
    exercise and the argument is the card's own.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    Review finding: the statement said only "Calculate", dropping the printed requirement.
    Read against the retained source assets/attachments/Complex_Analysis_Spring_2011.docx,
    whose problem 4 reads "Use methods of complex variables to evaluate the integral
    int_0^inf (cos x - cos 4x)/x^2 dx"; the statement now carries that clause in the
    source's own voice. The solution already meets it, the Dirichlet integral being obtained
    from the indented upper-half-plane contour for e^{iz}/z.
---

::: {.problem}
Use methods of complex variables to evaluate
$$
\int_0^\infty {\cos(x) - \cos(4x) \over x^2} \, dx
.$$
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #dirichlet}
$\displaystyle\int_0^{\infty}\frac{\sin t}{t}\,dt=\frac{\pi}{2}$.

::: pf-proof
Integrate $e^{iz}/z$ over the boundary of the upper half-disc of radius $R$ with a small semicircle of radius $r$ about $0$ removed, and let $r\to0$, $R\to\infty$. The function is holomorphic inside the contour, so the total integral vanishes; the integral over the large semicircle tends to $0$ by Jordan's lemma, the integral over the small semicircle tends to $-i\pi$ times the residue $1$ at $0$ (half the full residue, by the indentation), and the two radial pieces tend to $2i\int_0^\infty\frac{\sin t}{t}dt$. Hence $2i\int_0^\infty\frac{\sin t}{t}dt-i\pi=0$.
:::

:::

::: {.pf-step #parts}
For every $a>0$,
$$
\int_0^{\infty}\frac{1-\cos(ax)}{x^2}\,dx=a\int_0^{\infty}\frac{\sin(ax)}{x}\,dx .
$$

::: pf-proof
Integrate by parts with $u=1-\cos(ax)$ and $dv=x^{-2}dx$, so $v=-x^{-1}$ and $du=a\sin(ax)\,dx$:
$$
\int_0^{\infty}\frac{1-\cos(ax)}{x^2}\,dx=\left[-\frac{1-\cos(ax)}{x}\right]_0^{\infty}+a\int_0^{\infty}\frac{\sin(ax)}{x}\,dx .
$$
The bracket vanishes: at $x\to\infty$ because $1-\cos(ax)$ is bounded, and at $x\to0$ because $1-\cos(ax)=\frac{a^2x^2}{2}+O(x^4)$, so the quotient is $O(x)$.
:::

:::

::: {.pf-step #formula}
For every $a>0$, $\displaystyle\int_0^{\infty}\frac{1-\cos(ax)}{x^2}\,dx=\frac{\pi a}{2}$.

::: pf-proof
Substituting $t=ax$ in the integral of step [](#parts){.pf-ref} gives $\int_0^\infty\frac{\sin(ax)}{x}dx=\int_0^\infty\frac{\sin t}{t}dt$, which is $\frac{\pi}{2}$ by step [](#dirichlet){.pf-ref}; multiplying by $a$ gives $\frac{\pi a}{2}$.
:::

:::

::: {.pf-step}
$\displaystyle\int_0^{\infty}\frac{\cos x-\cos4x}{x^2}\,dx=\boxed{\frac{3\pi}{2}}$.

::: pf-proof
Since $\cos x-\cos4x=(1-\cos4x)-(1-\cos x)$ and each of the two integrals converges absolutely at $0$ (the numerators are $O(x^2)$) and absolutely at $\infty$ (the integrands are bounded by $2x^{-2}$), the difference of integrals is the integral of the difference. Steps [](#formula){.pf-ref} with $a=4$ and with $a=1$ give
$$
\int_0^{\infty}\frac{\cos x-\cos4x}{x^2}\,dx=\frac{4\pi}{2}-\frac{\pi}{2}=\frac{3\pi}{2}.
$$
:::

:::

:::
:::
