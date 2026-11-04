---
schema: qual/card@1
id: P-FHW1-03
kind: problem
title: Irreducibility of $x^3+x^2+x+3$ and inversion in $\QQ(\alpha)$
classification:
  areas: [algebra]
  topics: [Field Extensions, Irreducibility Criteria]
relations: []
review: draft
audit:
- event: source-checked
  by: Claude Opus 5.5
  date: 2026-10-30
  note: Transcribed from the MinerU Flash extraction of assets/attachments/fields-homework-1.pdf and checked against the page image.
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
(a) Show that $f(x)=x^3+x^2+x+3$ is irreducible over $\QQ$.

(b) Consider the field $F=\QQ(\alpha)$, where $\alpha$ is a root of $f(x)$. Express $\dfrac{1}{2-\alpha+\alpha^2}$ as a $\QQ$-linear combination of $1$, $\alpha$, and $\alpha^2$.
:::

::: {.solution}
Write $\overline{a}$ for the class of $a\in\QQ$ in $\QQ(\alpha)$, so that $\alpha^3+\alpha^2+\alpha+3=0$.

::: pf

::: {.pf-step #a-irreducible}
(a) $f(x)=x^3+x^2+x+3$ is irreducible over $\QQ$.

::: pf-proof
A cubic over a field is irreducible exactly when it has no root in that field, since a nontrivial factorization of a cubic has a linear factor.
A rational root of a monic polynomial with integer coefficients is an integer dividing the constant term, so the only candidates are $1,-1,3,-3$, and
$$
f(1)=6,\qquad f(-1)=2,\qquad f(3)=42,\qquad f(-3)=-18,
$$
none of which is zero.
Hence $f$ has no rational root and is irreducible over $\QQ$.
:::

:::

::: {.pf-step #b-inverse}
(b) $\dfrac{1}{2-\alpha+\alpha^2}=\boxed{\dfrac{1+2\alpha+\alpha^2}{2}}$.

::: pf-proof
Since $f$ is irreducible and $3=\deg f$, the powers $1,\alpha,\alpha^2$ are $\QQ$-linearly independent, so it is enough to compute in $\QQ[\alpha]$ modulo $f$.
Dividing $f$ by $x^2-x+2$ gives
$$
x^3+x^2+x+3=(x^2-x+2)(x+2)+(x-1),
$$
and dividing $x^2-x+2$ by $x-1$ gives $x^2-x+2=x(x-1)+2$.
Eliminating $x-1$ from the two identities yields
$$
2=(x^2-x+2)\bigl(1+x(x+2)\bigr)-xf,
$$
so modulo $f$ the class of $x^2-x+2$ is invertible with inverse the class of $\tfrac12(x^2+2x+1)$.
Substituting $x=\alpha$ gives $(2-\alpha+\alpha^2)\cdot\tfrac12(1+2\alpha+\alpha^2)=1$ in $\QQ(\alpha)$.
:::

:::

:::

:::
