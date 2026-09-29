---
schema: qual/card@1
id: P-AGGOINGUP
kind: problem
title: Going up, read geometrically
classification:
  areas:
  - algebraic-geometry
  topics:
  - Integral Extensions
  - Going Up
  - Finite Morphisms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Hartshorne's question asking for the geometric meaning of going up.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
What does the going up theorem mean in algebraic geometry?
:::

::: {.solution}
Let
\[
A\longrightarrow B
\]
be an integral ring map and let
\[
f:\operatorname{Spec}B\longrightarrow\operatorname{Spec}A
\]
be the induced morphism.

::: pf

::: {.pf-step #specialization-order}
For primes
\[
\mathfrak p_1\subseteq\mathfrak p_2
\]
of $A$, the point $\mathfrak p_2$ is a specialization of $\mathfrak p_1$ in $\operatorname{Spec}A$.

::: pf-proof
The closure of the point $\mathfrak p_1$ is
\[
\overline{\{\mathfrak p_1\}}
=V(\mathfrak p_1)
=\{\mathfrak p:\mathfrak p\supseteq\mathfrak p_1\}.
\]
Thus $\mathfrak p_2\in\overline{\{\mathfrak p_1\}}$ exactly when $\mathfrak p_1\subseteq\mathfrak p_2$.
:::

:::

::: {.pf-step #going-up-statement}
Going up says that specializations lift along an integral morphism.
More precisely, if
\[
\mathfrak p_1\subseteq\mathfrak p_2
\]
and $\mathfrak q_1\in\operatorname{Spec}B$ lies over $\mathfrak p_1$, then there exists
\[
\mathfrak q_2\supseteq\mathfrak q_1
\]
lying over $\mathfrak p_2$:
\[
\mathfrak q_i\cap A=\mathfrak p_i.
\]

::: pf-proof
This is exactly the going-up theorem for the integral extension $A\to B$ applied to the prime chain
\[
\mathfrak p_1\subseteq\mathfrak p_2
\]
and the already chosen lift $\mathfrak q_1$ of its first term.

By step [](#specialization-order){.pf-ref}, the inclusion $\mathfrak q_1\subseteq\mathfrak q_2$ says geometrically that $\mathfrak q_2$ is a specialization of $\mathfrak q_1$.
:::

:::

::: {.pf-step #integral-closed-map}
Equivalently, integral morphisms are closed maps on underlying topological spaces.

::: pf-proof
Let
\[
Z=V(J)\subseteq\operatorname{Spec}B
\]
be closed.  The quotient map
\[
A/(J\cap A)\longrightarrow B/J
\]
is injective and integral.  By lying over,
\[
\operatorname{Spec}(B/J)\longrightarrow
\operatorname{Spec}(A/(J\cap A))
\]
is surjective.  Therefore
\[
f(V(J))
=V(J\cap A),
\]
which is closed in $\operatorname{Spec}A$.

Conversely, the specialization-lifting statement in step [](#going-up-statement){.pf-ref} explains why an image cannot lose a specialization: once a point lies in the image of a closed subset, every specialization of that point also lies in the image.
:::

:::

::: {.pf-step #geometric-reading}
Thus the geometric reading of going up is
\[
\boxed{
\text{integral morphisms lift specializations and are closed.}
}
\]
For a finite morphism, this is the algebraic-geometric analogue of a finite branched covering being a closed map.

::: pf-proof
A finite ring map is integral, so steps [](#going-up-statement){.pf-ref} and [](#integral-closed-map){.pf-ref} apply.  Finite morphisms are also affine and of finite type; in particular they are proper, and the closed-map behavior supplied by integrality is the topological part of that picture.
:::

:::

::: {.pf-step #dimension-preservation}
Going up also explains why finite surjective morphisms do not decrease dimension.

::: pf-proof
Given a chain
\[
\mathfrak p_0\subsetneq\cdots\subsetneq\mathfrak p_r
\]
in the base, lying over chooses a prime above $\mathfrak p_0$, and repeated going up lifts the whole chain to
\[
\mathfrak q_0\subsetneq\cdots\subsetneq\mathfrak q_r.
\]
Thus every prime-chain length in the base occurs upstairs.  For an integral extension, incomparability supplies the reverse dimension inequality, yielding equality of dimensions in the usual integral-surjective setting.
:::

:::

::: pf-qed
Steps [](#going-up-statement){.pf-ref}, [](#integral-closed-map){.pf-ref} and [](#geometric-reading){.pf-ref} give the requested geometric interpretation; step [](#dimension-preservation){.pf-ref} records its standard dimension consequence.
:::

:::
:::
