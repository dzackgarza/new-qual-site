---
schema: qual/card@1
id: P-PRACT20-W5-20
kind: problem
title: A polynomial in the primitive fifth root of unity $e^{2\pi i/5}$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 20).
---

::: {.problem}
Let $z = e^{2\pi i/5}$. Evaluate $1 + z + z^2 + z^3 + 5z^4 + 4z^5 + 4z^6 + 4z^7 + 4z^8 + 5z^9$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Since
$$
z=e^{2\pi i/5},
$$
one has
$$
z^5=1.
$$


::: pf-proof

Indeed,
$$
z^5=e^{2\pi i}=1.
$$

:::

:::

::: {.pf-step #s1-2}

The given expression simplifies to
$$
5+5z+5z^2+5z^3+10z^4.
$$


::: pf-proof

Using step [](#s1-1){.pf-ref},
$$
z^5=1,\qquad
z^6=z,\qquad
z^7=z^2,\qquad
z^8=z^3,\qquad
z^9=z^4.
$$
Substitution and collection of like powers gives
$$
5+5z+5z^2+5z^3+10z^4.
$$

:::

:::

::: {.pf-step #s1-3}

One has
$$
1+z+z^2+z^3+z^4=0.
$$


::: pf-proof

Since $z\ne1$ and $z^5=1$,
$$
1+z+z^2+z^3+z^4
=\frac{z^5-1}{z-1}
=0.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore the value of the expression is
$$
\boxed{5z^4=5e^{8\pi i/5}}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\begin{aligned}
5+5z+5z^2+5z^3+10z^4
&=
5(1+z+z^2+z^3+z^4)+5z^4\\
&=5z^4
\end{aligned}
$$
by step [](#s1-3){.pf-ref}. Finally,
$$
z^4=e^{8\pi i/5}.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested value.

:::

:::

:::
