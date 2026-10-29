---
schema: qual/card@1
id: P-WESCA12-II3
kind: problem
title: 'Derivative and function ratios at equal-order zeros'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $D\subset\CC$ be a domain containing $0$ and let $f,g$ be analytic on $D$.
Suppose both have zeros of order $7$ at $0$.
Prove that
\[
\lim_{z\to0}\frac{f'(z)}{g'(z)}
\quad\text{and}\quad
\lim_{z\to0}\frac{f(z)}{g(z)}
\]
both exist and are equal.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Since $f$ and $g$ both have zeros of order $7$ at $0$, there are
analytic functions
\[
F,G
\]
near $0$ such that
\[
f(z)=z^7F(z),
\qquad
g(z)=z^7G(z),
\]
with
\[
F(0)\ne0,
\qquad
G(0)\ne0.
\]


::: pf-proof

Having a zero of order exactly $7$ means precisely that the first nonzero
Taylor coefficient occurs in degree $7$.
Factoring out
\[
z^7
\]
leaves analytic functions that are nonzero at the origin.

:::

:::

::: {.pf-step #s1-2}

For $z\ne0$ sufficiently near $0$,
\[
\frac{f(z)}{g(z)}
=
\frac{F(z)}{G(z)}.
\]


::: pf-proof

Using step [](#s1-1){.pf-ref},
\[
\frac{f(z)}{g(z)}
=
\frac{z^7F(z)}{z^7G(z)}
=
\frac{F(z)}{G(z)}.
\]
Since
\[
G(0)\ne0,
\]
continuity implies that $G$ is nonzero on some neighborhood of $0$.

:::

:::

::: {.pf-step #s1-3}

Therefore
\[
\boxed{
\lim_{z\to0}
\frac{f(z)}{g(z)}
=
\frac{F(0)}{G(0)}.
}
\]


::: pf-proof

The quotient
\[
\frac{F}{G}
\]
is analytic, hence continuous, near $0$.
Apply step [](#s1-2){.pf-ref} and take the limit.

:::

:::

::: {.pf-step #s1-4}

Differentiating the factorizations gives
\[
f'(z)
=
z^6
\bigl(
7F(z)+zF'(z)
\bigr)
\]
and
\[
g'(z)
=
z^6
\bigl(
7G(z)+zG'(z)
\bigr).
\]


::: pf-proof

Apply the product rule to
\[
f(z)=z^7F(z)
\]
and
\[
g(z)=z^7G(z).
\]

:::

:::

::: {.pf-step #s1-5}

The function
\[
7G(z)+zG'(z)
\]
is nonzero for all sufficiently small $z$.


::: pf-proof

At
\[
z=0,
\]
its value is
\[
7G(0),
\]
which is nonzero by step [](#s1-1){.pf-ref}.
Continuity therefore gives a neighborhood on which it does not vanish.

:::

:::

::: {.pf-step #s1-6}

For $z\ne0$ sufficiently near $0$,
\[
\frac{f'(z)}{g'(z)}
=
\frac{
7F(z)+zF'(z)
}{
7G(z)+zG'(z)
}.
\]


::: pf-proof

Cancel the common factor
\[
z^6
\]
from the formulas in step [](#s1-4){.pf-ref}.
Step [](#s1-5){.pf-ref} guarantees the remaining denominator is nonzero near $0$.

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
\boxed{
\lim_{z\to0}
\frac{f'(z)}{g'(z)}
=
\frac{F(0)}{G(0)}.
}
\]


::: pf-proof

Take the limit in step [](#s1-6){.pf-ref}:
\[
7F(z)+zF'(z)
\longrightarrow
7F(0),
\]
and
\[
7G(z)+zG'(z)
\longrightarrow
7G(0).
\]
Thus
\[
\lim_{z\to0}
\frac{f'(z)}{g'(z)}
=
\frac{7F(0)}{7G(0)}
=
\frac{F(0)}{G(0)}.
\]

:::

:::

::: {.pf-step #s1-8}

The two limits exist and are equal:
\[
\boxed{
\lim_{z\to0}
\frac{f'(z)}{g'(z)}
=
\lim_{z\to0}
\frac{f(z)}{g(z)}
=
\frac{F(0)}{G(0)}.
}
\]


::: pf-proof

Combine steps [](#s1-3){.pf-ref} and [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is exactly the desired conclusion.

:::

:::

:::
