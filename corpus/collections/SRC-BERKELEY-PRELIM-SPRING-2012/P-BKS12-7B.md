---
schema: qual/card@1
id: P-BKS12-7B
kind: problem
title: Comparison of real parts of entire functions from the unit circle
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the real-part symbol read as < against s12solutions.pdf page 6 problem 7B, keeping the source calligraphic C.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the exponential reduction and maximum-modulus argument.
---

::: {.problem}
Let $f, g : \CC \to \CC$ be entire functions. Write $\Re$ for the real part of a complex number. Assume $\Re(f(z)) \geq \Re(g(z))$ for all $z$ such that $|z| = 1$. Show $\Re(f(z)) \geq \Re(g(z))$ for all $z$ such that $|z| < 1$.
:::

::: {.solution}
Define
$$
h(z)\coloneqq e^{g(z)-f(z)}.
$$

::: pf

::: {.pf-step #h-entire}
The function $h$ is entire.

::: pf-proof
The difference $g-f$ is entire, and the exponential function is entire.
Therefore their composition is entire.
:::

:::

::: {.pf-step #bound-on-circle}
If $\abs{z}=1$, then
$$
\abs{h(z)}\leq1.
$$

::: pf-proof
For every complex number $w$,
$$
\abs{e^w}=e^{\operatorname{Re}w}.
$$
Hence
$$
\abs{h(z)}
=
e^{\operatorname{Re}(g(z)-f(z))}
=
e^{\operatorname{Re}g(z)-\operatorname{Re}f(z)}.
$$
The hypothesis on the unit circle makes the exponent nonpositive, giving
the claimed bound.
:::

:::

::: {.pf-step #bound-in-disk}
If $\abs{z}<1$, then
$$
\abs{h(z)}\leq1.
$$

::: pf-proof
The function $h$ is holomorphic on a neighborhood of the closed unit disk
by step [](#h-entire){.pf-ref}. Step [](#bound-on-circle){.pf-ref} bounds its modulus by $1$ on the boundary.
The maximum modulus theorem therefore gives the same bound throughout the
closed disk, in particular on its interior.
:::

:::

::: {.pf-step #conclusion}
For every $\abs{z}<1$,
$$
\boxed{
\operatorname{Re}f(z)
\geq
\operatorname{Re}g(z)
}.
$$

::: pf-proof
By step [](#bound-in-disk){.pf-ref},
$$
e^{\operatorname{Re}g(z)-\operatorname{Re}f(z)}
=
\abs{h(z)}
\leq
1.
$$
Since the real exponential is strictly increasing,
$$
\operatorname{Re}g(z)-\operatorname{Re}f(z)
\leq
0,
$$
which is equivalent to the displayed inequality.
:::

:::

::: pf-qed
Step [](#conclusion){.pf-ref} is exactly the required conclusion.
:::

:::

:::
