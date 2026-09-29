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

::: pf

::: {.pf-step #automorphism-properties}
For $a\in\DD$, define
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

::: pf-proof
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

:::

::: {.pf-step #g-fixes-origin}
Fix $z\in\DD$ and set
$$
g
\coloneqq
\phi_{f(z)}\circ f\circ\phi_z^{-1}.
$$
Then $g:\DD\to\DD$ is analytic and
$$
g(0)=0.
$$

::: pf-proof
By step [](#automorphism-properties){.pf-ref}, both disk automorphisms are analytic self-maps of
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

:::

::: {.pf-step #schwarz-lemma-bound}
One has
$$
\abs{g'(0)}\leq1.
$$

::: pf-proof
This is Schwarz's lemma applied to the analytic self-map $g$ of the
unit disk with $g(0)=0$.
:::

:::

::: {.pf-step #g-prime-formula}
The derivative in step [](#schwarz-lemma-bound){.pf-ref} is
$$
g'(0)
=
\frac{1-\abs z^2}{1-\abs{f(z)}^2}\,f'(z).
$$

::: pf-proof
By the chain rule,
$$
g'(0)
=
\phi_{f(z)}'(f(z))\,f'(z)\,(\phi_z^{-1})'(0).
$$
Step [](#automorphism-properties){.pf-ref} gives
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

:::

::: {.pf-step #intermediate-bound}
Therefore
$$
\abs{f'(z)}
\leq
\frac{1-\abs{f(z)}^2}{1-\abs z^2}.
$$

::: pf-proof
Take absolute values in step [](#g-prime-formula){.pf-ref} and apply step [](#schwarz-lemma-bound){.pf-ref}.
:::

:::

::: {.pf-step #final-bound-boxed}
Hence, for every $z\in\DD$,
$$
\boxed{
\abs{f'(z)}
\leq
\frac1{1-\abs z^2}.
}
$$

::: pf-proof
Because $f(z)\in\DD$,
$$
0<1-\abs{f(z)}^2\leq1.
$$
Apply this inequality to the numerator in step [](#intermediate-bound){.pf-ref}.
:::

:::

::: pf-qed
Step [](#final-bound-boxed){.pf-ref} is the required estimate.
:::

:::
:::
