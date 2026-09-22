---
schema: qual/card@1
id: P-BERK85S-20
kind: problem
title: Derivative bound for an analytic self-map of the unit disk
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Conjugated f by automorphisms of the unit disk carrying a chosen
    point z to zero and f(z) to zero. Schwarz's lemma then gives the
    Schwarz-Pick derivative estimate, whose numerator is at most one.
---

::: {.problem}
Let $f$ be analytic from the open unit disk into itself. Prove that
\[
|f'(z)|\le\frac1{1-|z|^2}
\]
for every $|z|<1$.
:::

::: {.solution}
Let
$$
\DD=\{z\in\CC:\abs z<1\}.
$$

<1>1. For $a\in\DD$, define
$$
\phi_a(w)
\coloneqq
\frac{w-a}{1-\overline a w}.
$$
Then $\phi_a$ is an automorphism of $\DD$ satisfying
$$
\phi_a(a)=0,
\qquad
\phi_a'(a)=\frac{1}{1-\abs a^2}.
$$

::: {.proof}
For $w\in\DD$,
$$
\abs{1-\overline a w}^2-\abs{w-a}^2
=
(1-\abs a^2)(1-\abs w^2)>0,
$$
so $\abs{\phi_a(w)}<1$. Solving
$$
\zeta=\frac{w-a}{1-\overline a w}
$$
for $w$ gives
$$
w=\frac{\zeta+a}{1+\overline a\zeta},
$$
which also maps $\DD$ to itself by the same calculation. Hence
$\phi_a$ is a biholomorphic self-map of $\DD$. Differentiating,
$$
\phi_a'(w)
=
\frac{1-\abs a^2}{(1-\overline a w)^2},
$$
and evaluation at $w=a$ gives the stated derivative.
:::

<1>2. Fix $z\in\DD$ and set
$$
g
\coloneqq
\phi_{f(z)}\circ f\circ\phi_z^{-1}.
$$
Then $g:\DD\to\DD$ is analytic and
$$
g(0)=0.
$$

::: {.proof}
By step <1>1, both disk automorphisms are analytic self-maps of
$\DD$, and $f$ maps $\DD$ into itself. Since
$$
\phi_z^{-1}(0)=z,
$$
we obtain
$$
g(0)
=
\phi_{f(z)}(f(z))
=
0.
$$
:::

<1>3. One has
$$
\abs{g'(0)}\leq1.
$$

::: {.proof}
This is Schwarz's lemma applied to the analytic self-map $g$ of the
unit disk with $g(0)=0$.
:::

<1>4. The derivative in step <1>3 is
$$
g'(0)
=
\frac{1-\abs z^2}{1-\abs{f(z)}^2}\,f'(z).
$$

::: {.proof}
By the chain rule,
$$
g'(0)
=
\phi_{f(z)}'(f(z))\,f'(z)\,(\phi_z^{-1})'(0).
$$
Step <1>1 gives
$$
\phi_{f(z)}'(f(z))
=
\frac1{1-\abs{f(z)}^2}.
$$
Since
$$
\phi_z'(z)=\frac1{1-\abs z^2},
$$
the inverse-function derivative formula gives
$$
(\phi_z^{-1})'(0)
=
1-\abs z^2.
$$
Substitution yields the formula.
:::

<1>5. Therefore
$$
\abs{f'(z)}
\leq
\frac{1-\abs{f(z)}^2}{1-\abs z^2}.
$$

::: {.proof}
Take absolute values in step <1>4 and apply step <1>3.
:::

<1>6. Hence, for every $z\in\DD$,
$$
\boxed{
\abs{f'(z)}
\leq
\frac1{1-\abs z^2}.
}
$$

::: {.proof}
Because $f(z)\in\DD$,
$$
0<1-\abs{f(z)}^2\leq1.
$$
Apply this inequality to the numerator in step <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required estimate.
:::
:::
