---
schema: qual/card@1
id: E-SS8.EX-9
kind: problem
title: An unbounded harmonic function with zero boundary values
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The collection's provenance is the publisher's catalogue record only, with no retained text and no retained solution set, so the statement is taken as the card prints it; the argument is the card's own. Checked: the single pole of $F$ at $z=i$ lies on the boundary, so $F$ is holomorphic in $\DD$; on the unit circle $\overline{F(z)}=-F(z)$, so $F$ is purely imaginary there and $u$ vanishes; and along $z=ri$ the value is $(1+r)/(1-r)$, which is unbounded.
---

::: {.exercise}
Prove that the function $u$ defined by
$$
u(x, y) = \Re\left( \frac{i + z}{i - z} \right) \quad \text{and} \quad u(0, 1) = 0
$$
is harmonic in the unit disc and vanishes on its boundary. Note that $u$ is not bounded in $\DD$.
:::

::: {.solution}
No retained text and no retained solution set for this collection: its provenance is the publisher's catalogue record, so the statement is taken as the card prints it, and the argument is the card's own.

::: pf

::: {.pf-step #harmonic}
$F(z)=\frac{i+z}{i-z}$ is holomorphic on $\DD$, so $u(z)=\Re F(z)$ is harmonic there.

::: pf-proof
The only pole of $F$ is at $z=i$, where the denominator vanishes; that point lies on the unit circle and not in $\DD$, so $F$ is holomorphic on the disc. The real part of a holomorphic function is harmonic.
:::
:::

::: {.pf-step #boundary}
If $\abs z=1$ and $z\neq i$ then $F(z)$ is purely imaginary, so $u(z)=0$.

::: pf-proof
On the unit circle $\overline z=1/z$, hence $\overline{F(z)}=\frac{-i+\overline z}{-i-\overline z}=\frac{-iz+1}{-iz-1}=-\frac{i+z}{i-z}=-F(z)$: the conjugate of $F(z)$ is $-F(z)$, so the real part vanishes. With the stipulated value $u(i)=u(0,1)=0$, the boundary values vanish everywhere on the circle.
:::
:::

::: {.pf-step #unbounded}
$u$ is unbounded on $\DD$.

::: pf-proof
Along the radius $z=ri$ with $0<r<1$, $F(ri)=\frac{i+ri}{i-ri}=\frac{1+r}{1-r}$, a real number, so $u(ri)=\frac{1+r}{1-r}\to+\infty$ as $r\uparrow1$.
:::
:::

::: {.pf-step}
$u$ is harmonic in $\DD$, vanishes on the boundary, and is unbounded there.

::: pf-proof
Steps [](#harmonic){.pf-ref}, [](#boundary){.pf-ref} and [](#unbounded){.pf-ref} give the three assertions of the exercise.
:::
:::

:::
:::
