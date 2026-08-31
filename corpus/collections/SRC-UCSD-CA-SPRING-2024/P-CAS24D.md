---
schema: qual/card@1
id: P-CAS24D
kind: problem
title: 'Positive harmonic function as $e^u\sin v$ on a simply connected region'
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $\phi$ be a positive harmonic function on a simply connected region $G$.
Prove that there are two harmonic functions $u,v$ on $G$ such that $\phi = e^u \sin v$.
:::

::: {.solution}
<1>1. Since $G$ is simply connected and $\phi > 0$ is harmonic, $\phi$ has a harmonic conjugate $\psi$, so $F = \phi + i\psi$ is analytic on $G$.
::: {.proof}
a positive harmonic function on a simply connected region has a harmonic conjugate (its harmonic conjugate is obtained by integrating the closed form $-\phi_y\, dx + \phi_x\, dy$).
:::

<1>2. $F$ is nowhere zero on $G$.
::: {.proof}
$\operatorname{Re} F = \phi > 0$, so $F \neq 0$.
:::

<1>3. Since $G$ is simply connected and $F$ is nowhere zero, $F$ has an analytic logarithm: $F = e^H$ for some analytic $H$ on $G$.
::: {.proof}
a nowhere-vanishing analytic function on a simply connected region has an analytic logarithm.
:::

<1>4. Write $H = u + iv$ with $u, v$ harmonic (the real and imaginary parts of an analytic function are harmonic).
::: {.proof}
real and imaginary parts of an analytic function are harmonic.
:::

<1>5. Then $\phi = \operatorname{Re} F = \operatorname{Re}(e^{u + iv}) = e^u \cos v$.
::: {.proof}
$e^{u+iv} = e^u(\cos v + i\sin v)$, so its real part is $e^u \cos v$.
:::

<1>6. Replace $v$ by $v + \pi/2$ (equivalently, absorb a constant into $H$) to get $\phi = e^u \sin v$.
::: {.proof}
$\cos v = \sin(v + \pi/2)$, and $v + \pi/2$ is still harmonic.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
