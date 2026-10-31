---
schema: qual/card@1
id: P-TRIV-DE36
kind: problem
title: Boundary value problem $y''-3y'+2y=\delta(x-1)$
classification:
  areas: [prelim]
  topics:
  - Dirac Delta
  - Boundary Value Problems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 36, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $y''(x) - 3y'(x) + 2y(x) = \delta(x - 1)$ with $y(0) = 0$ and $y(1) = 1$.
:::

::: {.solution}

Interpret the equation distributionally on the real line and require $y$ to be continuous at $x=1$.

::: pf

::: pf-step

On each side of $x=1$, the solution has the form
$$
y_-(x)=Ae^x+Be^{2x}\quad(x<1),
\qquad
y_+(x)=Ce^x+De^{2x}\quad(x>1).
$$


::: pf-proof

Away from $x=1$ the delta distribution vanishes, so the homogeneous equation is
$$
y''-3y'+2y=0.
$$
Its characteristic polynomial $(r-1)(r-2)$ has roots $1$ and $2$.

:::

:::

::: {.pf-step #s1-2}

The conditions $y(0)=0$ and $y(1)=1$ determine the left branch uniquely as
$$
\boxed{y_-(x)=\frac{e^{2x}-e^x}{e^2-e}}.
$$


::: pf-proof

From $y_-(0)=0$ one gets $A+B=0$. Continuity together with the prescribed value $y(1)=1$ gives
$$
Ae+Be^2=1.
$$
Solving yields $B=(e^2-e)^{-1}$ and $A=-B$.

:::

:::

::: {.pf-step #s1-3}

The delta forcing imposes the jump condition
$$
y_+'(1)-y_-'(1)=1.
$$


::: pf-proof

Integrate the differential equation from $1-\epsilon$ to $1+\epsilon$. The $y''$ term gives the derivative jump. Because $y$ is continuous, the integrals of $y'$ and $y$ tend to zero as $\epsilon\to0^+$. The right side integrates to $1$.

:::

:::

::: {.pf-step #s1-4}

The conditions at $x=1$ determine the right branch as
$$
\boxed{
y_+(x)=-\frac{e}{e-1}e^{x-1}
+\frac{2e-1}{e-1}e^{2(x-1)}}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives
$$
y_-'(1)=\frac{2e^2-e}{e^2-e}=\frac{2e-1}{e-1}.
$$
Hence step [](#s1-3){.pf-ref} gives
$$
y_+'(1)=\frac{3e-2}{e-1}.
$$
Write $y_+(x)=Pe^{x-1}+Qe^{2(x-1)}$. Then continuity and the derivative condition are
$$
P+Q=1,
\qquad
P+2Q=\frac{3e-2}{e-1}.
$$
Thus $Q=(2e-1)/(e-1)$ and $P=-e/(e-1)$, which is the displayed expression after simplification.

:::

:::

::: {.pf-step #s1-5}

Therefore the distributional solution is
$$
\boxed{
y(x)=
\begin{cases}
\dfrac{e^{2x}-e^x}{e^2-e},&x\leq1,\\[6pt]
-\dfrac{e}{e-1}e^{x-1}+\dfrac{2e-1}{e-1}e^{2(x-1)},&x\geq1.
\end{cases}}
$$


::: pf-proof

Steps [](#s1-2){.pf-ref} and [](#s1-4){.pf-ref} give the two homogeneous branches. They both equal $1$ at $x=1$, and step [](#s1-3){.pf-ref} gives the unit derivative jump required to produce exactly $\delta(x-1)$ and no $\delta'(x-1)$ term.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} satisfies the differential equation distributionally and both prescribed values.

:::

:::

:::
