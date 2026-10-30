---
schema: qual/card@1
id: P-TRIV-DE09
kind: problem
title: Forced equation $y''+3y'+2y=\tanh x$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 9, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $y'' + 3y' + 2y = \tanh x$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Factor the differential operator:
$$
D^2+3D+2
=
(D+1)(D+2),
$$
where $D=d/dx$.


::: pf-proof

Expand
$$
(D+1)(D+2)
=
D^2+3D+2.
$$

:::

:::

::: pf-step

Set
$$
z=(D+2)y
=
y'+2y.
$$
Then $z$ satisfies
$$
z'+z=\tanh x.
$$


::: pf-proof

Apply $D+1$ to the definition of $z$ and use step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Multiplying by $e^x$ gives
$$
\frac d{dx}(e^xz)
=
e^x\tanh x.
$$


::: pf-proof

The integrating factor for $z'+z=\tanh x$ is $e^x$.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\int e^x\tanh x\,dx
=
e^x
-
2\arctan(e^x)
+
C.
$$


::: pf-proof

Set
$$
u=e^x,
\qquad
du=e^x\,dx.
$$
Then
$$
\tanh x
=
\frac{u^2-1}{u^2+1},
$$
so
$$
\int e^x\tanh x\,dx
=
\int
\frac{u^2-1}{u^2+1}
\,du
=
\int
\left(
1-\frac2{u^2+1}
\right)du.
$$

:::

:::

::: {.pf-step #s1-5}

Hence
$$
z(x)
=
1
-
2e^{-x}\arctan(e^x)
+
C_1e^{-x}.
$$


::: pf-proof

Integrate step [](#s1-3){.pf-ref} using step [](#s1-4){.pf-ref} and divide by $e^x$.

:::

:::

::: {.pf-step #s1-6}

Now solve
$$
y'+2y=z(x).
$$
Multiplying by $e^{2x}$ gives
$$
\frac d{dx}(e^{2x}y)
=
e^{2x}z(x).
$$


::: pf-proof

The integrating factor for the first-order equation $y'+2y=z$ is $e^{2x}$.

:::

:::

::: {.pf-step #s1-7}

A particular antiderivative of the nonhomogeneous part is
$$
\int
\left[
e^{2x}
-
2e^x\arctan(e^x)
\right]dx
=
\frac12e^{2x}
-
2e^x\arctan(e^x)
+
\log(1+e^{2x}).
$$


::: pf-proof

For the second term, set $u=e^x$:
$$
2\int e^x\arctan(e^x)\,dx
=
2\int\arctan u\,du.
$$
Integration by parts gives
$$
\int\arctan u\,du
=
u\arctan u
-
\frac12\log(1+u^2).
$$
Substitute back $u=e^x$.

:::

:::

::: {.pf-step #s1-8}

The term $C_1e^{-x}$ in $z$ contributes a homogeneous-mode term proportional to $e^{-x}$ in $y$, and the integrating constant contributes a term proportional to $e^{-2x}$.


::: pf-proof

Under step [](#s1-6){.pf-ref},
$$
e^{2x}C_1e^{-x}=C_1e^x,
$$
whose antiderivative is $C_1e^x$, yielding $C_1e^{-x}$ after multiplication by $e^{-2x}$.
The final integration constant becomes $C_2e^{-2x}$.

:::

:::

::: {.pf-step #s1-9}

Therefore the general solution is
$$
\boxed{
\begin{aligned}
y(x)
&=
C_1e^{-x}
+
C_2e^{-2x}\\
&\quad
+
\frac12
-
2e^{-x}\arctan(e^x)
+
e^{-2x}\log(1+e^{2x}).
\end{aligned}
}
$$


::: pf-proof

Combine steps [](#s1-5){.pf-ref} through [](#s1-8){.pf-ref} and multiply the particular antiderivative from step [](#s1-7){.pf-ref} by $e^{-2x}$.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} gives the complete two-parameter solution family.

:::

:::

:::
