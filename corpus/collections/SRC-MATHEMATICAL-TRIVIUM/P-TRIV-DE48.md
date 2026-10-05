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
A string has endpoints which are fixed at $x = 0$ and $x = L$ . At $t = 0$ , the string is hit at $x = a$ so it starts vibrating:

$$
y ( x , 0 ) = 0 \qquad \partial _ { t } y ( x , 0 ) = L v _ { 0 } \delta ( x - a )\tag{42}
$$

where y is the amplitude of the oscillations (assume the amplitude to be small and the wave velocity to be v). Find $y ( x , t )$
:::

::: {.solution}
The string satisfies
\[
y_{tt}=v^2y_{xx},
\qquad
y(0,t)=y(L,t)=0.
\]

<1>1. A fixed-end solution with zero initial displacement has the expansion
\[
y(x,t)=\sum_{n=1}^{\infty}B_n
\sin\frac{n\pi x}{L}
\sin\frac{n\pi vt}{L}.
\]

::: {.proof}
The Dirichlet eigenfunctions are $\sin(n\pi x/L)$. For each spatial eigenvalue $(n\pi/L)^2$, the temporal equation is
\[
T_n''+v^2\frac{n^2\pi^2}{L^2}T_n=0.
\]
Zero initial displacement removes the cosine term, leaving the displayed sine-in-time expansion.
:::

<1>2. Its initial velocity is
\[
y_t(x,0)=\sum_{n=1}^{\infty}B_n\frac{n\pi v}{L}
\sin\frac{n\pi x}{L}.
\]

::: {.proof}
Differentiate the series in step <1>1 with respect to $t$ and set $t=0$.
:::

<1>3. On $(0,L)$, the delta distribution has the sine-series expansion
\[
\delta(x-a)=\frac2L\sum_{n=1}^{\infty}
\sin\frac{n\pi a}{L}
\sin\frac{n\pi x}{L}.
\]

::: {.proof}
For the sine basis, the coefficient of a distribution $g$ is
\[
c_n=\frac2L\left\langle g,\sin\frac{n\pi x}{L}\right\rangle.
\]
Taking $g=\delta_a$ gives $c_n=(2/L)\sin(n\pi a/L)$.
:::

<1>4. Matching the prescribed initial velocity gives
\[
B_n=\frac{2Lv_0}{n\pi v}
\sin\frac{n\pi a}{L}.
\]

::: {.proof}
The initial condition is
\[
y_t(x,0)=Lv_0\delta(x-a)
=2v_0\sum_{n=1}^{\infty}
\sin\frac{n\pi a}{L}
\sin\frac{n\pi x}{L}.
\]
Compare this with step <1>2 and solve
\[
B_n\frac{n\pi v}{L}=2v_0\sin\frac{n\pi a}{L}.
\]
:::

<1>5. Therefore
\[
\boxed{
y(x,t)=\frac{2Lv_0}{\pi v}
\sum_{n=1}^{\infty}\frac1n
\sin\frac{n\pi a}{L}
\sin\frac{n\pi x}{L}
\sin\frac{n\pi vt}{L}.}
\]

::: {.proof}
Insert the coefficients from step <1>4 into step <1>1. The series satisfies the wave equation and fixed-end conditions termwise, has zero initial displacement, and step <1>4 verifies its initial velocity distributionally.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the displacement of the struck string.
:::
:::
