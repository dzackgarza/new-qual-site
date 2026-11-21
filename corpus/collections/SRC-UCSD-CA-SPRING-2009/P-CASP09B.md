---
schema: qual/card@1
id: P-CASP09B
kind: problem
title: 'Zeros of $z^7+2z^3+4$ in the first quadrant'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, whose answer
    of two zeros is correct. Added: the explicit check that P has no zeros on the closed
    nonnegative axes (P(x) > 0 on the real axis, P(iy) with nonzero imaginary part), the factor
    R^-1 expansion on the quarter-circle with the uniformity that makes the bracketed factor
    contribute no argument variation, the description of the continuous lift on the imaginary
    segment from 7 pi/2 to 8 pi, and the closing step that the integral of P'/P over 2 pi i is
    an integer which converges to 2, hence equals 2 for large R. Not claimed: a retained
    solution set; the provenance names the examination paper.
---

::: {.problem}
Find the number of zeros of $f(z) = z^7 + 2z^3 + 4$ in the interior of the first quadrant (all $z = x + iy$ with $x$ and $y$ positive).
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Spring 2009 complex-analysis examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose.

Throughout $P(z)=z^7+2z^3+4$ and, for $R>0$, $Q_R=\theset{z:\abs z<R,\ 0<\arg z<\pi/2}$ is the open quarter-disk, whose boundary is the real segment, the quarter-circle and the imaginary segment.

::: pf

::: {.pf-step #axes}
$P$ has no zeros on the closed nonnegative real axis or the closed nonnegative imaginary axis.

::: pf-proof
$P(0)=4\ne0$. For $x>0$, $P(x)=x^7+2x^3+4>0$. For $y>0$, $i^7=-i$ and $i^3=-i$, so $P(iy)=4-i(y^7+2y^3)$, whose imaginary part is nonzero.

:::

:::

::: {.pf-step #arc}
Along the quarter-circle $z=Re^{i\theta}$, $0\le\theta\le\pi/2$, the change in the argument of $P$ tends to $7\pi/2$ as $R\to\infty$.

::: pf-proof
$P(Re^{i\theta})=(Re^{i\theta})^7\bigl(1+2R^{-4}e^{-4i\theta}+4R^{-7}e^{-7i\theta}\bigr)$, and the bracket tends to $1$ uniformly in $\theta$ as $R\to\infty$, so it contributes no argument variation in the limit. The first factor contributes $7\theta$, increasing from $0$ to $7\pi/2$; hence the limiting variation is $7\pi/2$.

:::

:::

::: {.pf-step #imaginary}
Along the imaginary segment traversed from $iR$ to $0$, the argument of $P$ varies by $\pi/2$ (with the continuous lift), from $7\pi/2$ to $4\pi$.

::: pf-proof
$P(iy)=4-i(y^7+2y^3)$ has argument in $(-\pi/2,0)$ for $y>0$, tending to $-\pi/2$ as $y\to\infty$ and to $0$ as $y\to0^+$. Traversing the segment downwards, i.e. $y$ from $R$ to $0$, the principal argument increases from about $-\pi/2$ to $0$; the continuous lift beginning at the value $7\pi/2=-\pi/2+4\pi$ at $y=R$ therefore ends at $8\pi=4\pi$, a change of $\pi/2$.

:::

:::

::: {.pf-step #total}
The total argument variation around $\partial Q_R$ tends to $4\pi$.

::: pf-proof
On the real segment $[0,R]$ the value $P(x)$ is real and positive for $x\ge0$, so its argument is constantly $0$ and contributes nothing. Adding the contributions of steps [](#arc){.pf-ref} and [](#imaginary){.pf-ref} gives $7\pi/2+\pi/2=4\pi$ in the limit.

:::

:::

::: {.pf-step #conclusion}
$P$ has exactly $2$ zeros in the open first quadrant.

::: pf-proof
For large $R$ the polynomial $P$ has no zeros on $\partial Q_R$ by step [](#axes){.pf-ref} and the estimate on the arc, and none on the arc for large $R$ since $\abs{z^7}>2\abs z^3+4$ there. The argument principle then gives $\#(\text{zeros in }Q_R)=(2\pi)^{-1}\cdot$ (variation of $\arg P$), which is an integer for each $R$ and tends to $4\pi/(2\pi)=2$; an integer-valued quantity converging to $2$ equals $2$ for large $R$. All zeros of $P$ lie in $\abs z<R$ for large $R$, so the count in the open first quadrant is $2$.

:::

:::

:::
:::
