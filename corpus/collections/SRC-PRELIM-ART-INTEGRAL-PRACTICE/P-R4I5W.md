---
schema: qual/card@1
id: P-R4I5W
kind: problem
title: $\int\sqrt{1+\cos(2ax)}\,dx$
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
    its answer: the double-angle identity, the sign restriction of the square root, and the piecewise and global primitives, the last checked by differentiating H across the join points
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. The identity, the two local primitives and an explicit continuous global primitive whose derivative is checked off and across the join points.
---

::: {.problem}
Evaluate
$$
\int \sqrt{1+\cos(2ax)}\,dx.
$$
:::

::: {.solution}

Let $a$ be real and consider the integrand $\sqrt{1+\cos(2ax)}$, defined where
$1+\cos(2ax)\ge0$, that is everywhere.

::: pf

::: {.pf-step #identity}

$1+\cos(2u)=2\cos^2u$, hence $\sqrt{1+\cos(2ax)}=\sqrt2\,\abs{\cos(ax)}$.

::: pf-proof

The double angle formula gives $\cos(2u)=2\cos^2u-1$, so
$1+\cos(2u)=2\cos^2u$; taking square roots of both sides, which are
nonnegative, gives $\sqrt{1+\cos(2u)}=\sqrt2\abs{\cos u}$, and substituting
$u=ax$ gives the stated form.

:::

:::

::: {.pf-step #local}

If $a\ne0$, then on any interval on which $\cos(ax)$ has constant sign a
primitive is $\frac{\sqrt2}{a}\sin(ax)+C$ where $\cos(ax)\ge0$ and
$-\frac{\sqrt2}{a}\sin(ax)+C$ where $\cos(ax)\le0$.

::: pf-proof

The zeros of $\cos(ax)$ are at $ax=\pi/2+k\pi$, so $\cos(ax)$ has one sign on
each of the open intervals between consecutive zeros, and the integrand is one
of $\pm\sqrt2\cos(ax)$ there. Since $\frac{d}{dx}\sin(ax)=a\cos(ax)$, an
antiderivative of $\sqrt2\cos(ax)$ is $\frac{\sqrt2}{a}\sin(ax)$ and of
$-\sqrt2\cos(ax)$ is $-\frac{\sqrt2}{a}\sin(ax)$.

:::

:::

::: {.pf-step #global}

If $a\ne0$ a primitive on all of $\RR$ is $\frac{\sqrt2}{a}H(ax)+C$, where
$k(u)=\left\lfloor\frac{u+\pi/2}{\pi}\right\rfloor$ and
$H(u)=2k(u)+\sin(u-k(u)\pi)$; if $a=0$ the integrand is the constant $\sqrt2$
and the primitive is $\sqrt2x+C$.

::: pf-proof

On the interval $\pi k-\frac\pi2\le u\le\pi k+\frac\pi2$ the integer $k(u)$
equals $k$, and $\cos u$ has the sign $(-1)^k$ there, so
$H'(u)=\cos(u-k\pi)=(-1)^k\cos u=\abs{\cos u}$ on the interior of that
interval. At the join $u=\pi k+\frac\pi2$ the value of $H$ computed from the
$k$-th branch is $2k+\sin\frac\pi2=2k+1$ and from the $(k+1)$-st branch is
$2k+2+\sin(-\frac\pi2)=2k+1$, so $H$ is continuous; being continuous on $\RR$,
differentiable off the join points with derivative tending to $\abs{\cos u}$,
which is continuous, it is differentiable at the joins too with $H'=\abs{\cos
u}$. Composing with $u=ax$ and multiplying by $\sqrt2/a$ gives the derivative
$\frac{\sqrt2}{a}\cdot a\abs{\cos(ax)}=\sqrt2\abs{\cos(ax)}$, which is the
integrand by step [](#identity){.pf-ref}. For $a=0$ the formula $1+\cos0=2$
makes the integrand the constant $\sqrt2$.

:::

:::

:::


:::
