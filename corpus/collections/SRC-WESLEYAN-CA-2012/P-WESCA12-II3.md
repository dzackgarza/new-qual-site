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
Let $D\subset\mathbb C$ be a domain containing $0$ and let $f,g$ be analytic on $D$.
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
<1>1. Since $f$ and $g$ both have zeros of order $7$ at $0$, there are
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

::: {.proof}
Having a zero of order exactly $7$ means precisely that the first nonzero
Taylor coefficient occurs in degree $7$.
Factoring out
\[
z^7
\]
leaves analytic functions that are nonzero at the origin.
:::

<1>2. For $z\ne0$ sufficiently near $0$,
\[
\frac{f(z)}{g(z)}
=
\frac{F(z)}{G(z)}.
\]

::: {.proof}
Using step <1>1,
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

<1>3. Therefore
\[
\boxed{
\lim_{z\to0}
\frac{f(z)}{g(z)}
=
\frac{F(0)}{G(0)}.
}
\]

::: {.proof}
The quotient
\[
\frac{F}{G}
\]
is analytic, hence continuous, near $0$.
Apply step <1>2 and take the limit.
:::

<1>4. Differentiating the factorizations gives
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

::: {.proof}
Apply the product rule to
\[
f(z)=z^7F(z)
\]
and
\[
g(z)=z^7G(z).
\]
:::

<1>5. The function
\[
7G(z)+zG'(z)
\]
is nonzero for all sufficiently small $z$.

::: {.proof}
At
\[
z=0,
\]
its value is
\[
7G(0),
\]
which is nonzero by step <1>1.
Continuity therefore gives a neighborhood on which it does not vanish.
:::

<1>6. For $z\ne0$ sufficiently near $0$,
\[
\frac{f'(z)}{g'(z)}
=
\frac{
7F(z)+zF'(z)
}{
7G(z)+zG'(z)
}.
\]

::: {.proof}
Cancel the common factor
\[
z^6
\]
from the formulas in step <1>4.
Step <1>5 guarantees the remaining denominator is nonzero near $0$.
:::

<1>7. Therefore
\[
\boxed{
\lim_{z\to0}
\frac{f'(z)}{g'(z)}
=
\frac{F(0)}{G(0)}.
}
\]

::: {.proof}
Take the limit in step <1>6:
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

<1>8. The two limits exist and are equal:
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

::: {.proof}
Combine steps <1>3 and <1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is exactly the desired conclusion.
:::
:::
