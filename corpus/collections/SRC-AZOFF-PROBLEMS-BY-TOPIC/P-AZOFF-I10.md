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

<1>1. The map $\phi_c$ is an automorphism of $\DD$ satisfying
$$
\phi_c(c)=0
$$
and
$$
\phi_c'(c)=\frac1{1-\abs{c}^2}.
$$

::: {.proof}
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

<1>2. Fix $a\in\DD$, put
$$
b=f(a),
$$
and define
$$
F=\phi_b\circ f\circ\phi_a^{-1}.
$$
Then $F:\DD\to\DD$ is analytic and $F(0)=0$.

::: {.proof}
By step <1>1, both $\phi_a^{-1}$ and $\phi_b$ are disk automorphisms.
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

<1>3. One has
$$
\abs{F'(0)}\leq1.
$$

::: {.proof}
This is Schwarz's lemma applied to the function in step <1>2.
:::

<1>4. The derivative of $F$ at the origin is
$$
F'(0)
=
\frac{1-\abs{a}^2}
{1-\abs{f(a)}^2}
f'(a).
$$

::: {.proof}
By the chain rule,
$$
F'(0)
=
\phi_b'(b)\,
f'(a)\,
(\phi_a^{-1})'(0).
$$
Step <1>1 gives
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

<1>5. For every $a\in\DD$,
$$
\boxed{
\frac{\abs{f'(a)}}{1-\abs{f(a)}^2}
\leq
\frac1{1-\abs{a}^2}.
}
$$

::: {.proof}
Taking absolute values in step <1>4 and using step <1>3 gives
$$
\frac{1-\abs{a}^2}
{1-\abs{f(a)}^2}
\abs{f'(a)}
\leq1.
$$
Both denominators are positive because $a,f(a)\in\DD$. Dividing by
$1-\abs{a}^2$ yields the required inequality.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the claimed Schwarz--Pick derivative inequality.
:::
:::
