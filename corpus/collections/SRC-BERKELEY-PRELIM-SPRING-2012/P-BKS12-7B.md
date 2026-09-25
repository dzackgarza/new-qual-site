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
Let $f, g : \mathcal{C} \to \mathcal{C}$ be entire functions. Write $\Re$ for the real part of a complex number. Assume $\Re(f(z)) \geq \Re(g(z))$ for all $z$ such that $|z| = 1$. Show $\Re(f(z)) \geq \Re(g(z))$ for all $z$ such that $|z| < 1$.
:::

::: {.solution}
Define
$$
h(z)\coloneqq e^{g(z)-f(z)}.
$$

<1>1. The function $h$ is entire.

::: {.proof}
The difference $g-f$ is entire, and the exponential function is entire.
Therefore their composition is entire.
:::

<1>2. If $\abs{z}=1$, then
$$
\abs{h(z)}\leq1.
$$

::: {.proof}
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

<1>3. If $\abs{z}<1$, then
$$
\abs{h(z)}\leq1.
$$

::: {.proof}
The function $h$ is holomorphic on a neighborhood of the closed unit disk
by step <1>1. Step <1>2 bounds its modulus by $1$ on the boundary.
The maximum modulus theorem therefore gives the same bound throughout the
closed disk, in particular on its interior.
:::

<1>4. For every $\abs{z}<1$,
$$
\boxed{
\operatorname{Re}f(z)
\geq
\operatorname{Re}g(z)
}.
$$

::: {.proof}
By step <1>3,
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

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is exactly the required conclusion.
:::
:::
