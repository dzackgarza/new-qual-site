---
schema: qual/card@1
id: P-TRIV-DE48
kind: problem
title: Struck string with fixed ends
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 48, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains a leading nonprinting control byte at this source position; the byte was removed from the authored card as a nonsemantic extraction artifact.
---

::: {.problem}
A string has endpoints which are fixed at $x = 0$ and $x = L$. At $t = 0$, the string is hit at $x = a$ so it starts vibrating:
$$
y(x, 0) = 0 \qquad \partial_t y(x, 0) = Lv_0\delta(x - a) \tag{42}
$$
where $y$ is the amplitude of the oscillations (assume the amplitude to be small and the wave velocity to be $v$). Find $y(x, t)$.
:::

::: {.solution}

The string satisfies
$$
y_{tt}=v^2y_{xx},
\qquad
y(0,t)=y(L,t)=0.
$$

::: pf

::: {.pf-step #s1-1}

A fixed-end solution with zero initial displacement has the expansion
$$
y(x,t)=\sum_{n=1}^{\infty}B_n
\sin\frac{n\pi x}{L}
\sin\frac{n\pi vt}{L}.
$$


::: pf-proof

The Dirichlet eigenfunctions are $\sin(n\pi x/L)$. For each spatial eigenvalue $(n\pi/L)^2$, the temporal equation is
$$
T_n''+v^2\frac{n^2\pi^2}{L^2}T_n=0.
$$
Zero initial displacement removes the cosine term, leaving the displayed sine-in-time expansion.

:::

:::

::: {.pf-step #s1-2}

Its initial velocity is
$$
y_t(x,0)=\sum_{n=1}^{\infty}B_n\frac{n\pi v}{L}
\sin\frac{n\pi x}{L}.
$$


::: pf-proof

Differentiate the series in step [](#s1-1){.pf-ref} with respect to $t$ and set $t=0$.

:::

:::

::: pf-step

On $(0,L)$, the delta distribution has the sine-series expansion
$$
\delta(x-a)=\frac2L\sum_{n=1}^{\infty}
\sin\frac{n\pi a}{L}
\sin\frac{n\pi x}{L}.
$$


::: pf-proof

For the sine basis, the coefficient of a distribution $g$ is
$$
c_n=\frac2L\left\langle g,\sin\frac{n\pi x}{L}\right\rangle.
$$
Taking $g=\delta_a$ gives $c_n=(2/L)\sin(n\pi a/L)$.

:::

:::

::: {.pf-step #s1-4}

Matching the prescribed initial velocity gives
$$
B_n=\frac{2Lv_0}{n\pi v}
\sin\frac{n\pi a}{L}.
$$


::: pf-proof

The initial condition is
$$
y_t(x,0)=Lv_0\delta(x-a)
=2v_0\sum_{n=1}^{\infty}
\sin\frac{n\pi a}{L}
\sin\frac{n\pi x}{L}.
$$
Compare this with step [](#s1-2){.pf-ref} and solve
$$
B_n\frac{n\pi v}{L}=2v_0\sin\frac{n\pi a}{L}.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
y(x,t)=\frac{2Lv_0}{\pi v}
\sum_{n=1}^{\infty}\frac1n
\sin\frac{n\pi a}{L}
\sin\frac{n\pi x}{L}
\sin\frac{n\pi vt}{L}.}
$$


::: pf-proof

Insert the coefficients from step [](#s1-4){.pf-ref} into step [](#s1-1){.pf-ref}. The series satisfies the wave equation and fixed-end conditions termwise, has zero initial displacement, and step [](#s1-4){.pf-ref} verifies its initial velocity distributionally.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the displacement of the struck string.

:::

:::

:::
