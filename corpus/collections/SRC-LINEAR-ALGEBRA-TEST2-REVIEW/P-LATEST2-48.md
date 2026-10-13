---
schema: qual/card@1
id: P-LATEST2-48
kind: problem
title: Commutator of differentiation and multiplication by $x$
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained PDF extraction for linear_algebra_from_test2.pdf; the source PDF has no usable text layer, so this audit is limited to the preserved extraction generated from that PDF.
---

::: {.problem}
Let $V$ be the vector space of all real polynomials $p(x)$.
Define $T,S:V\to V$ by
\[
T(p)(x)=xp(x),\qquad S(p)(x)=p'(x),
\]
and interpret $(ST)(p)$ as $S(T(p))$.
Which statement is true?

(A) $ST=0$  (B) $ST=T$  (C) $ST=TS$  (D) $ST-TS$ is the identity map of $V$  (E) $ST+TS$ is the identity map of $V$
:::

::: {.solution}
Let
$$
p\in V.
$$

<1>1. One has
$$
(ST)(p)(x)
=
p(x)+xp'(x).
$$

::: {.proof}
By definition,
$$
T(p)(x)=xp(x).
$$
Applying $S$ means differentiating:
$$
\begin{aligned}
(ST)(p)(x)
&=
S(T(p))(x)\\
&=
\frac{d}{dx}\bigl(xp(x)\bigr)\\
&=
p(x)+xp'(x),
\end{aligned}
$$
by the product rule.
:::

<1>2. One has
$$
(TS)(p)(x)
=
xp'(x).
$$

::: {.proof}
First,
$$
S(p)(x)=p'(x).
$$
Applying $T$ multiplies by $x$:
$$
(TS)(p)(x)
=
x p'(x).
$$
:::

<1>3. Therefore
$$
((ST-TS)(p))(x)
=
p(x).
$$

::: {.proof}
Subtract step <1>2 from step <1>1:
$$
\begin{aligned}
((ST-TS)(p))(x)
&=
\bigl(p(x)+xp'(x)\bigr)-xp'(x)\\
&=
p(x).
\end{aligned}
$$
:::

<1>4. Hence
$$
\boxed{ST-TS=\operatorname{id}_V}.
$$

::: {.proof}
Step <1>3 holds for every polynomial $p\in V$.
Thus the operator $ST-TS$ acts as the identity on every vector in $V$.
:::

<1>5. Q.E.D.

::: {.proof}
The correct answer is $\boxed{\text{(D)}}$.
:::
:::
