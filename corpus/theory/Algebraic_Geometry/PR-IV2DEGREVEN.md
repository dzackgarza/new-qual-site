---
schema: qual/card@1
id: PR-IV2DEGREVEN
kind: proposition
title: The ramification divisor has even degree
slogan: 'Riemann--Hurwitz makes ramification parity automatic: for a finite separable cover of curves, $\deg R$ is always even.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ramification
  - Riemann-Hurwitz
  - Curves
relations:
- kind: uses
  target: T-LKT0U
- kind: uses
  target: D-IV2RAM
review: draft
prompts:
- Show that $\deg R$ is even for a finite separable morphism of curves.
- A degree-$3$ cover of $\PP^1$ is branched at how many points, if the ramification is tame and simple?
---

::: {.proposition}
Let $k$ be an algebraically closed field and let $f\colon X\to Y$ be a finite nonconstant separable morphism of smooth projective curves over $k$. Let $R$ be its ramification divisor as in [[D-IV2RAM]].
Then $\deg R$ is even.
:::

::: {.proof}
Riemann--Hurwitz gives
$$
\deg R = (2 g_X - 2) - \deg(f)(2 g_Y - 2) ,
$$
a difference of two even integers.
:::

::: {.remark title="Parity consequences"}
Suppose the ramification is tame and simple, with exactly one point of ramification index $2$ above each branch point. Then every ramification point contributes $1$ to $R$, so $\deg R$ equals the number of branch points and is therefore even.

For a degree-$2$ morphism $X\to\PP^1$, Riemann--Hurwitz gives
$$
\deg R=2g_X+2.
$$
For a degree-$3$ morphism $X\to\PP^1$ with tame simple ramification, the number $b$ of branch points is
$$
b=\deg R=2g_X+4.
$$

Separability is required because it makes $f^*\Omega_Y\to\Omega_X$ injective and $\Omega_{X/Y}$ a torsion sheaf, so its stalk lengths define the divisor $R$ used by [[T-LKT0U]]. For an inseparable morphism this exact-sequence argument does not apply; see [[PR-IV2INSEP]].
:::
