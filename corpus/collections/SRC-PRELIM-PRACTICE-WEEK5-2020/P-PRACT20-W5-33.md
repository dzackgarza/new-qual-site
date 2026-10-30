---
schema: qual/card@1
id: P-PRACT20-W5-33
kind: problem
title: Contour integral of $e^{1/(1-z)}/z$ around $\abs{z}=3$
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
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 33).
---

::: {.problem}
Evaluate the integral $\oint_{\{\abs{z} = 3\}} \frac{e^{\frac{1}{1 - z}}}{z}\,dz$.
:::

::: {.solution}

Let
$$
F(z)=\frac{e^{1/(1-z)}}{z}.
$$

::: pf

::: {.pf-step #s1-1}

The finite singularities of $F$ are
$$
z=0
\qquad\text{and}\qquad
z=1,
$$
and both lie inside $\abs{z}=3$.


::: pf-proof

The factor $1/z$ gives a simple pole at $0$. The exponent
$$
\frac1{1-z}
$$
has a pole at $1$, so its exponential has an essential singularity there.
There are no other finite singularities.

:::

:::

::: {.pf-step #s1-2}

As $z\to\infty$,
$$
F(z)=\frac1z+O\!\left(\frac1{z^2}\right).
$$


::: pf-proof

One has
$$
\frac1{1-z}
=
-\frac1z\frac1{1-1/z}
=
-\frac1z+O\!\left(\frac1{z^2}\right).
$$
Therefore
$$
e^{1/(1-z)}
=
1+O\!\left(\frac1z\right),
$$
and division by $z$ gives the stated expansion.

:::

:::

::: {.pf-step #s1-3}

The residue of $F$ at infinity is
$$
\operatorname{Res}_\infty F=-1.
$$


::: pf-proof

The residue at infinity is the negative of the coefficient of $z^{-1}$ in
the Laurent expansion at infinity. By step [](#s1-2){.pf-ref}, that coefficient is $1$.

:::

:::

::: {.pf-step #s1-4}

The sum of the residues at the two finite singularities is
$$
1.
$$


::: pf-proof

For a function holomorphic on the Riemann sphere away from isolated
singularities, the sum of all residues, including the residue at infinity,
is zero. Hence by step [](#s1-3){.pf-ref},
$$
\operatorname{Res}(F,0)+\operatorname{Res}(F,1)
=
-\operatorname{Res}_\infty F
=1.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\oint_{\abs{z}=3}\frac{e^{1/(1-z)}}{z}\,dz
=2\pi i }.
$$


::: pf-proof

The positively oriented circle encloses exactly the two singularities in
step [](#s1-1){.pf-ref}. By the residue theorem and step [](#s1-4){.pf-ref},
$$
\oint_{\abs{z}=3}F(z)\,dz
=
2\pi i\cdot1
=2\pi i.
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the requested value.

:::

:::

:::
