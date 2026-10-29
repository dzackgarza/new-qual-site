---
schema: qual/card@1
id: P-TIE-S15-20
kind: problem
title: Harnack-type bounds for $|f(z)|$ for self-maps of the disk
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 20.
---

::: {.problem}
Let f be a non-constant analytic function on D with $f ( \DD ) \subseteq \DD . { \mathrm { ~ U s e ~ } } \psi _ { a } ( f ( z ) )$ (where $a = f ( 0 )$ $\psi _ { a } ( z ) = \frac { a - z } { 1 - \bar { a } z } )$ to prove that ${ \frac { | f ( 0 ) | - | z | } { 1 + | f ( 0 ) | | z | } } \leq | f ( z ) | \leq { \frac { | f ( 0 ) | + | z | } { 1 - | f ( 0 ) | | z | } } ,$
:::

::: {.solution}

Set $a\coloneqq f(0)$ and $\phi_a(w)\coloneqq(a-w)/(1-\overline a w)$.

::: pf

::: {.pf-step #s1-1}

The function $g\coloneqq\phi_a\circ f$ is a holomorphic self-map of $\DD$ satisfying $g(0)=0$.


::: pf-proof

Since $\abs a<1$, the map $\phi_a$ is a holomorphic automorphism of $\DD$. Because $f(\DD)\subseteq\DD$, the composition maps $\DD$ into itself, and $g(0)=\phi_a(a)=0$.

:::

:::

::: {.pf-step #s1-2}

For every $z\in\DD$,
$$
\abs{\frac{a-f(z)}{1-\overline a f(z)}}\le\abs z.
$$


::: pf-proof

This is Schwarz's lemma applied to $g$ from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Put $A\coloneqq\abs a$, $r\coloneqq\abs z$, and $s\coloneqq\abs{f(z)}$. Then
$$
\abs{a-f(z)}\le r(1+As).
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives $\abs{a-f(z)}\le r\abs{1-\overline a f(z)}$, while the triangle inequality gives $\abs{1-\overline a f(z)}\le1+As$.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\boxed{\abs{f(z)}\le\frac{\abs{f(0)}+\abs z}{1-\abs{f(0)}\abs z}}.
$$


::: pf-proof

By the reverse triangle inequality and step [](#s1-3){.pf-ref},
$$
s-A\le\abs{f(z)-a}\le r(1+As).
$$
Thus $s(1-Ar)\le A+r$. Since $1-Ar>0$, division gives $s\le(A+r)/(1-Ar)$.

:::

:::

::: {.pf-step #s1-5}

One has
$$
\boxed{\frac{\abs{f(0)}-\abs z}{1+\abs{f(0)}\abs z}\le\abs{f(z)}}.
$$


::: pf-proof

Again by the reverse triangle inequality and step [](#s1-3){.pf-ref},
$$
A-s\le\abs{a-f(z)}\le r(1+As).
$$
Hence $A-r\le s(1+Ar)$, so $s\ge(A-r)/(1+Ar)$. When $A<r$, the right-hand side is negative and the same inequality is automatic from $s\ge0$.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref} are the two requested inequalities.

:::

:::

:::
