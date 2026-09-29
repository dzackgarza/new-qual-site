---
schema: qual/card@1
id: P-AZOFF-I10
kind: problem
title: Schwarz--Pick inequality for the derivative
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Schwarz lemma and reflection principle, Problem 10, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-corrected
  by: chatgpt
  date: 2026-09-21
  note: >-
    The retained PDF prints f:D→D. The extracted card had lost the arrow;
    the statement now restores it.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Conjugated f by disk automorphisms sending a and f(a) to zero. Schwarz's
    lemma bounds the derivative of the conjugated map at zero, and the chain
    rule gives the stated Schwarz--Pick derivative inequality.
---

::: {.problem}
[Fall 1998, Problem #5] Suppose $f : \mathbb { D } \to \mathbb { D }$ is analytic.
Prove that for any $a \in \mathbb { D }$

$$
{ \frac { | f ^ { \prime } ( a ) | } { 1 - | f ( a ) | ^ { 2 } } } \leq { \frac { 1 } { 1 - | a | ^ { 2 } } } .
$$
:::

::: {.solution}
For $c\in\DD$, define the disk automorphism
$$
\phi_c(z)=\frac{z-c}{1-\bar c z}.
$$

::: pf

::: {.pf-step #s1}

The map $\phi_c$ is an automorphism of $\DD$ satisfying
$$
\phi_c(c)=0
$$
and
$$
\phi_c'(c)=\frac1{1-\abs{c}^2}.
$$

::: pf-proof

The standard disk automorphism formula shows that $\phi_c$ maps $\DD$
biholomorphically onto itself and sends $c$ to $0$. Differentiating gives
$$
\phi_c'(z)
=
\frac{1-\abs{c}^2}{(1-\bar c z)^2}.
$$
Evaluating at $z=c$ yields
$$
\phi_c'(c)
=
\frac{1-\abs{c}^2}{(1-\abs{c}^2)^2}
=
\frac1{1-\abs{c}^2}.
$$

:::

:::

::: {.pf-step #s2}

Fix $a\in\DD$, put
$$
b=f(a),
$$
and define
$$
F=\phi_b\circ f\circ\phi_a^{-1}.
$$
Then $F:\DD\to\DD$ is analytic and $F(0)=0$.

::: pf-proof

By step [](#s1){.pf-ref}, both $\phi_a^{-1}$ and $\phi_b$ are disk automorphisms.
Since $f$ is an analytic self-map of $\DD$, their composition $F$ is also
an analytic self-map of $\DD$. Moreover,
$$
F(0)
=
\phi_b\bigl(f(\phi_a^{-1}(0))\bigr)
=
\phi_b(f(a))
=
\phi_b(b)
=
0.
$$

:::

:::

::: {.pf-step #s3}

One has
$$
\abs{F'(0)}\leq1.
$$

::: pf-proof

This is Schwarz's lemma applied to the function in step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

The derivative of $F$ at the origin is
$$
F'(0)
=
\frac{1-\abs{a}^2}
{1-\abs{f(a)}^2}
f'(a).
$$

::: pf-proof

By the chain rule,
$$
F'(0)
=
\phi_b'(b)\,
f'(a)\,
(\phi_a^{-1})'(0).
$$
Step [](#s1){.pf-ref} gives
$$
\phi_b'(b)
=
\frac1{1-\abs{b}^2}.
$$
Since $\phi_a(a)=0$, the inverse function theorem gives
$$
(\phi_a^{-1})'(0)
=
\frac1{\phi_a'(a)}
=
1-\abs{a}^2.
$$
Substituting $b=f(a)$ gives the displayed formula.

:::

:::

::: {.pf-step #s5}

For every $a\in\DD$,
$$
\boxed{
\frac{\abs{f'(a)}}{1-\abs{f(a)}^2}
\leq
\frac1{1-\abs{a}^2}.
}
$$

::: pf-proof

Taking absolute values in step [](#s4){.pf-ref} and using step [](#s3){.pf-ref} gives
$$
\frac{1-\abs{a}^2}
{1-\abs{f(a)}^2}
\abs{f'(a)}
\leq1.
$$
Both denominators are positive because $a,f(a)\in\DD$. Dividing by
$1-\abs{a}^2$ yields the required inequality.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the claimed Schwarz--Pick derivative inequality.

:::

:::

:::
