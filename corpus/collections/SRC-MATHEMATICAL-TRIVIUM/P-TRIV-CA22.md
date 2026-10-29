---
schema: qual/card@1
id: P-TRIV-CA22
kind: problem
title: $\int_0^1 (x^2-x^3)^{-1/3}\,dx$ by a dogbone contour
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 22, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. The source hint refers to Figure 4, whose graphical content is absent from Flash. The integral itself is fully extracted; only the hinted contour is unresolved.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced the missing-figure note with a description of Figure 4, against Complex Analysis Problem 22 on pages 15-16 of the source PDF.
---

::: {.problem}
Compute $\displaystyle\int_0^1 \frac{1}{\left(x^2 - x^3\right)^{1/3}}$ (**hint:** use the contour in figure 4);

Figure 4 of the source (integration contour for exercise 22) shows a dogbone contour around the segment $[0, 1]$: a segment just above $[0, 1]$ traversed from $0$ to $1$, a small circle around $1$, a segment just below $[0, 1]$ traversed from $1$ to $0$, and a small circle around $0$; this dogbone is enclosed by a large circle traversed counterclockwise.
:::

::: {.solution}

Write
$$
I=\int_0^1x^{-2/3}(1-x)^{-1/3}\,dx.
$$

::: pf

::: {.pf-step #s1-1}

The integral is the beta integral
$$
I=B\left(\frac13,\frac23\right).
$$


::: pf-proof

By definition,
$$
B(a,b)=\int_0^1x^{a-1}(1-x)^{b-1}\,dx.
$$
Taking $a=1/3$ and $b=2/3$ gives exactly the integrand $x^{-2/3}(1-x)^{-1/3}$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
B\left(\frac13,\frac23\right)
=\Gamma\left(\frac13\right)
\Gamma\left(\frac23\right).
$$


::: pf-proof

The beta--gamma identity gives
$$
B(a,b)=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}.
$$
Here $a+b=1$ and $\Gamma(1)=1$.

:::

:::

::: {.pf-step #s1-3}

Euler's reflection formula gives
$$
\Gamma\left(\frac13\right)
\Gamma\left(\frac23\right)
=\frac{2\pi}{\sqrt3}.
$$


::: pf-proof

Reflection states
$$
\Gamma(z)\Gamma(1-z)=\frac\pi{\sin(\pi z)}.
$$
Set $z=1/3$ and use $\sin(\pi/3)=\sqrt3/2$.

:::

:::

::: pf-step

The dogbone contour in the hint yields the same beta--reflection evaluation.


::: pf-proof

Choose a branch of
$$
f(z)=z^{-2/3}(1-z)^{-1/3}
$$
on the plane cut along $[0,1]$. The two boundary values along the cut differ by the monodromy factors obtained by circling the branch points $0$ and $1$. As the small circles about the endpoints shrink, their contributions vanish because the local exponents $-2/3$ and $-1/3$ are greater than $-1$. Deforming the resulting dogbone against the outer contour gives precisely the standard keyhole-contour proof of
$$
B(a,1-a)=\frac\pi{\sin(\pi a)}
$$
with $a=1/3$, hence the value in step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{I=\frac{2\pi}{\sqrt3}}.
$$


::: pf-proof

Combine steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the requested integral.

:::

:::

:::
