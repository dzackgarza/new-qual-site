---
schema: qual/card@1
id: P-TRIV-DE14
kind: problem
title: Initial value problem $y''-6y'+15y=2\sin 3t$
classification:
  areas: [prelim]
  topics:
  - Laplace Transform
  - Initial Value Problems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 14, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash renders derivative primes as hyphens (`y--`, `y-`). The damaged notation is retained rather than silently reconstructed.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the garbled primes against Differential Equations Problem 14 on page 22 of the source PDF.
---

::: {.problem}
Solve $y'' - 6y' + 15y = 2\sin 3t$ with $y(0) = -1$ and $y'(0) = 4$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The homogeneous characteristic polynomial is
$$
\lambda^2-6\lambda+15,
$$
with roots
$$
\lambda=3\pm i\sqrt6.
$$


::: pf-proof

Apply the quadratic formula:
$$
\lambda
=
\frac{6\pm\sqrt{36-60}}2
=
3\pm i\sqrt6.
$$

:::

:::

::: {.pf-step #s1-2}

Hence
$$
y_h(t)
=
e^{3t}
\left[
C_1\cos(\sqrt6,t)
+
C_2\sin(\sqrt6,t)
\right].
$$


::: pf-proof

Use the standard real basis associated with the conjugate roots in step [](#s1-1){.pf-ref}.

:::

:::

::: pf-step

Seek a particular solution
$$
y_p=A\sin3t+B\cos3t.
$$


::: pf-proof

The forcing has frequency $3$, and $\pm3i$ are not characteristic roots.

:::

:::

::: {.pf-step #s1-4}

Substitution gives
$$
A+3B=\frac13,
\qquad
B-3A=0.
$$


::: pf-proof

For the ansatz,
$$
y_p'=3A\cos3t-3B\sin3t,
$$
$$
y_p''=-9A\sin3t-9B\cos3t.
$$
Thus
$$
y_p''-6y_p'+15y_p
=
(6A+18B)\sin3t
+
(6B-18A)\cos3t.
$$
Match coefficients with $2\sin3t$ and divide by $6$.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
A=\frac1{30},
\qquad
B=\frac1{10},
$$
so
$$
y_p
=
\frac1{30}\sin3t
+
\frac1{10}\cos3t.
$$


::: pf-proof

From $B-3A=0$, one has $B=3A$. Substitution into the first equation of step [](#s1-4){.pf-ref} gives $10A=1/3$.

:::

:::

::: {.pf-step #s1-6}

Thus
$$
y(t)
=
e^{3t}
\left[
C_1\cos(\sqrt6,t)
+
C_2\sin(\sqrt6,t)
\right]
+
\frac1{30}\sin3t
+
\frac1{10}\cos3t.
$$


::: pf-proof

Add the homogeneous solution from step [](#s1-2){.pf-ref} and the particular solution from step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

The condition $y(0)=-1$ gives
$$
C_1=-\frac{11}{10}.
$$


::: pf-proof

At $t=0$, the sine terms vanish and the cosine terms equal $1$, so
$$
C_1+\frac1{10}=-1.
$$

:::

:::

::: {.pf-step #s1-8}

The derivative at $t=0$ is
$$
y'(0)
=
3C_1
+
\sqrt6,C_2
+
\frac1{10}.
$$


::: pf-proof

Differentiate step [](#s1-6){.pf-ref}. At $t=0$, the homogeneous derivative contributes $3C_1+\sqrt6 C_2$, while the derivative of the particular part contributes $1/10$.

:::

:::

::: {.pf-step #s1-9}

The condition $y'(0)=4$ therefore gives
$$
C_2
=
\frac{6\sqrt6}{5}.
$$


::: pf-proof

Substitute $C_1=-11/10$ from step [](#s1-7){.pf-ref} into step [](#s1-8){.pf-ref}:
$$
4
=
-\frac{33}{10}
+
\sqrt6,C_2
+
\frac1{10}.
$$
Thus
$$
\sqrt6,C_2
=
\frac{36}{5},
$$
so
$$
C_2
=
\frac{36}{5\sqrt6}
=
\frac{6\sqrt6}{5}.
$$

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\boxed{
\begin{aligned}
y(t)
&=
e^{3t}
\left[
-\frac{11}{10}\cos(\sqrt6,t)
+
\frac{6\sqrt6}{5}\sin(\sqrt6,t)
\right]\\
&\quad
+
\frac1{30}\sin3t
+
\frac1{10}\cos3t.
\end{aligned}
}
$$


::: pf-proof

Substitute steps [](#s1-7){.pf-ref} and [](#s1-9){.pf-ref} into step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the unique solution satisfying the differential equation and both initial conditions.

:::

:::

:::
