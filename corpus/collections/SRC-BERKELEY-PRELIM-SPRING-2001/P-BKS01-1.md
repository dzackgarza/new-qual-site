---
schema: qual/card@1
id: P-BKS01-1
kind: problem
title: Number of endomorphisms of $\FF_q^2$ fixing a nonzero vector
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    An endomorphism fixes a nonzero vector exactly when A-I is singular.
    Translation by I is a bijection on M_2(F), so the count is the
    number of singular 2 by 2 matrices: q^4-|GL_2(F_q)|.
---

::: {.problem}
Let $F$ be a finite field with $q$ elements and let $V$ be a two-dimensional vector space over $F$.
Find the number of endomorphisms of $V$ that fix at least one nonzero vector.
:::

::: {.solution}
Choose a basis of $V$, so that
$$
\operatorname{End}_F(V)\cong M_2(F).
$$

::: pf

::: {.pf-step #s1}

A matrix $A\in M_2(F)$ fixes a nonzero vector if and only if
$A-I$ is singular.

::: pf-proof

The matrix $A$ fixes a nonzero vector $v$ exactly when
$$
Av=v,
$$
equivalently
$$
(A-I)v=0
$$
for some $v\ne0$. This happens exactly when $A-I$ has nontrivial
kernel, hence exactly when it is singular.

:::

:::

::: {.pf-step #s2}

The number sought equals
$$
q^4-\abs{GL_2(F)}.
$$

::: pf-proof

The translation
$$
M_2(F)\longrightarrow M_2(F),
\qquad
A\longmapsto A-I
$$
is a bijection. By step [](#s1){.pf-ref}, the desired matrices correspond exactly
to the singular matrices. There are $q^4$ total $2\times2$ matrices,
and the nonsingular ones form $GL_2(F)$.

:::

:::

::: {.pf-step #s3}

One has
$$
\abs{GL_2(F)}
=
(q^2-1)(q^2-q).
$$

::: pf-proof

The first column of an invertible matrix may be any nonzero vector in
$F^2$, giving $q^2-1$ choices. Once the first column is chosen, the
second may be any vector outside its one-dimensional span, giving
$q^2-q$ choices.

:::

:::

::: {.pf-step #s4}

The required number of endomorphisms is
$$
\boxed{q^3+q^2-q}.
$$

::: pf-proof

By steps [](#s2){.pf-ref} and [](#s3){.pf-ref},
$$
\begin{aligned}
q^4-(q^2-1)(q^2-q)
&=
q^4-(q^4-q^3-q^2+q)\\
&=
q^3+q^2-q.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the requested count.

:::

:::

:::
