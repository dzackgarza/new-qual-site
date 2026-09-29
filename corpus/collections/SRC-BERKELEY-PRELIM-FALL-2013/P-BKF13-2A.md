---
schema: qual/card@1
id: P-BKF13-2A
kind: problem
title: Grönwall's inequality
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 2A in the retained Fall 2013 Berkeley prelim exam
    and independently reviewed the retained solution packet F13_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the integrating-factor derivative and the sign-preserving
    multiplication used to recover the stated inequality.
---

::: {.problem}
Suppose that $x$ is a smooth real-valued function of the real number $t$, satisfying $dx/dt\le b(t)x(t)$ for some continuous function $b$. Prove that if $s\le t$ then $x(t)\le x(s)\exp\int_s^t b(t)\,dt$.
:::

::: {.solution}
Fix $s$, and for $u\ge s$ define
$$
B(u)\coloneqq\int_s^u b(v)\,dv,
\qquad
y(u)\coloneqq x(u)e^{-B(u)}.
$$

::: pf

::: {.pf-step #s1}

The function $y$ is nonincreasing on $[s,\infty)$.

::: pf-proof

Since $b$ is continuous,
$$
B'(u)=b(u).
$$
Therefore
$$
\begin{aligned}
y'(u)
&=e^{-B(u)}
\left(x'(u)-b(u)x(u)\right).
\end{aligned}
$$
The exponential factor is positive, while the hypothesis gives
$$
x'(u)-b(u)x(u)\le0.
$$
Hence $y'(u)\le0$, so $y$ is nonincreasing.

:::

:::

::: {.pf-step #s2}

If $s\le t$, then
$$
\boxed{
x(t)
\le
x(s)\exp\left(\int_s^t b(u)\,du\right)
}.
$$

::: pf-proof

By step [](#s1){.pf-ref},
$$
y(t)\le y(s).
$$
Since $B(s)=0$, this is
$$
x(t)e^{-B(t)}\le x(s).
$$
Multiplying by the positive number $e^{B(t)}$ gives
$$
x(t)\le x(s)e^{B(t)}
=x(s)\exp\left(\int_s^t b(u)\,du\right).
$$

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} is the required inequality.

:::

:::

:::
