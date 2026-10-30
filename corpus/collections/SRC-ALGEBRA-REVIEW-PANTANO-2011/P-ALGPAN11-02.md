---
schema: qual/card@1
id: P-ALGPAN11-02
kind: problem
title: Which listed subsets of the reals are subfields
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the retained Pantano 2011 algebra-review source scan and verified from the stated algebraic criterion.
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-31
  note: Statement and choices transcribed from the ALGEBRA_REVIEW1.pdf page render; the machine extractions were garbled at this item.
---
::: {.problem}
Let $\RR$ denote the field of real numbers, $\QQ$ the field of rational numbers, and $\ZZ$ the ring of integers.
Which of the following subsets $F_i$ of $\RR$, $1\le i\le4$, are subfields of $\RR$?

$F_1=\{a/b:a,b\in\ZZ\text{ and }b\text{ is odd}\}$,

$F_2=\{a+b\sqrt2:a,b\in\ZZ\}$,

$F_3=\{a+b\sqrt2:a,b\in\QQ\}$,

$F_4=\{a+b\sqrt[4]2:a,b\in\QQ\}$.

(A) No $F_i$ is a subfield of $\RR$.

(B) $F_3$ only

(C) $F_2$ and $F_3$ only

(D) $F_1$, $F_2$, and $F_3$ only

(E) $F_1$, $F_2$, $F_3$, and $F_4$
:::

::: {.solution}
Only $F_3$ is a subfield of $\RR$, choice (B).

::: pf

::: {.pf-step #s1}

$F_1$ is not a field.

::: pf-proof

The element $2=2/1$ belongs to $F_1$, but its inverse $1/2$ cannot be written with odd denominator after reduction.
Thus $F_1$ is not closed under inverses of nonzero elements.

:::

:::

::: {.pf-step #s2}

$F_2$ is not a field.

::: pf-proof

The integer $2$ belongs to $F_2$, whereas $1/2$ does not, since an equality
$$
\frac12=a+b\sqrt2,
\qquad a,b\in\ZZ,
$$
would force $b=0$ and then $a=1/2\notin\ZZ$.

:::

:::

::: {.pf-step #s3}

$F_3$ is a field.

::: pf-proof

It is $\QQ(\sqrt2)$.
Addition and multiplication preserve the form $a+b\sqrt2$.
If $a+b\sqrt2\ne0$, then
$$
(a+b\sqrt2)^{-1}=\frac{a-b\sqrt2}{a^2-2b^2}.
$$
The denominator is nonzero (otherwise $a/b=\pm\sqrt2$ when $b\ne0$), and the coefficients of the displayed inverse are rational.

:::

:::

::: {.pf-step #s4}

$F_4$ is not a field.

::: pf-proof

It contains $\alpha=\sqrt[4]{2}$, but closure under multiplication would require
$$
\alpha^2=\sqrt2=a+b\alpha
$$
for some $a,b\in\QQ$.
This would give the nontrivial $\QQ$-linear relation $\alpha^2-a-b\alpha=0$ among $1,\alpha,\alpha^2$.
But $T^4-2$ is irreducible over $\QQ$ by Eisenstein at $2$, so $1,\alpha,\alpha^2,\alpha^3$ are linearly independent over $\QQ$.
Hence $\sqrt2\notin\operatorname{span}_{\QQ}\{1,\alpha\}$.

:::

:::

::: pf-step

Therefore the answer is $\boxed{F_3\text{ only}}$.

::: pf-proof

Step [](#s1){.pf-ref}, step [](#s2){.pf-ref}, and step [](#s4){.pf-ref} rule out the other three subsets, while step [](#s3){.pf-ref} proves that $F_3$ is a field.

:::

:::

::: pf-qed

The preceding conclusion gives the complete classification.

:::

:::

:::
