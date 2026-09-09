---
schema: qual/card@1
id: E-75GIT
kind: problem
title: $a$ is algebraic over $K(b)$ if $b$ is algebraic over $K(a)$ and transcendental
  over $K$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Transcendence
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
1. Suppose that for an extension field $F$ over $K$ and for $a \in F$, we have that
   $b \in F$ is algebraic over $K(a)$ but transcendental over $K$. Prove that $a$ is
   algebraic over $K(b)$.
:::

::: {.solution}
<1>1. Since $b$ is algebraic over $K(a)$, the extension $K(a,b)/K(a)$ is algebraic.
::: {.proof}
By hypothesis $b$ is algebraic over $K(a)$, so adjoining $b$ gives an algebraic
extension.
:::

<1>2. Hence
\[
\operatorname{trdeg}_K K(a,b)=\operatorname{trdeg}_K K(a).
\]
Moreover $a$ is transcendental over $K$.
::: {.proof}
Algebraic extensions do not change transcendence degree. If $a$ were algebraic over $K$,
then $K(a)/K$ would be algebraic, and since $b$ is algebraic over $K(a)$, transitivity
of algebraicity would make $b$ algebraic over $K$, contradicting the hypothesis. Thus
$a$ is transcendental over $K$.
:::

<1>3. Therefore
\[
\operatorname{trdeg}_K K(a,b)=1.
\]
::: {.proof}
By <1>2, $a$ is transcendental over $K$, so $K(a)$ has transcendence degree $1$ over
$K$; combine this with the equality in <1>2.
:::

<1>4. The element $a$ is algebraic over $K(b)$.
::: {.proof}
Suppose instead that $a$ were transcendental over $K(b)$. Since $b$ is transcendental
over $K$, the singleton $\{b\}$ is algebraically independent over $K$, and $a$
transcendental over $K(b)$ implies that $\{a,b\}$ is algebraically independent over $K$.
Hence
\[
\operatorname{trdeg}_K K(a,b)\ge 2,
\]
contradicting <1>3. Therefore $a$ is algebraic over $K(b)$.
:::
:::
