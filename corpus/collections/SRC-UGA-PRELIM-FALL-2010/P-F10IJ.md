---
schema: qual/card@1
id: P-F10IJ
kind: problem
title: Injectivity of $g\circ f$ versus injectivity of $f$ and $g$
classification:
  areas:
  - prelim
  topics:
  - Functions and Relations
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Suppose $f: A \to B$ and $g: B \to C$ are functions.
Prove or give a counterexample:

(a) If $f$ and $g$ are injective (one-to-one), then $g \circ f$ is injective.

(b) If $g \circ f$ is injective, then $f$ and $g$ are injective.
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper (`assets/attachments/grad_prelim_Fall10.pdf`) and no solutions sheet accompanies it, so the argument and the counterexample below are the card's own. The problem asks to prove or refute each assertion, and the answer is that (a) is true and (b) is false, the second refuted by an explicit pair of functions.

Throughout, $f\colon A\to B$ and $g\colon B\to C$ are functions, and injective means that $x\ne y$ implies $f(x)\ne f(y)$.

::: pf

::: {.pf-step #composite-injective}
(a) If $f$ and $g$ are injective, then $g\circ f$ is injective.

::: pf-proof
Let $a_{1},a_{2}\in A$ with $(g\circ f)(a_{1})=(g\circ f)(a_{2})$. Then $g\big(f(a_{1})\big)=g\big(f(a_{2})\big)$, and injectivity of $g$ gives $f(a_{1})=f(a_{2})$; injectivity of $f$ then gives $a_{1}=a_{2}$. So the composite never takes the same value twice.
:::

:::

::: {.pf-step #f-injective}
(b) If $g\circ f$ is injective, then $f$ is injective.

::: pf-proof
Let $f(a_{1})=f(a_{2})$ for some $a_{1},a_{2}\in A$. Applying $g$ to both sides gives $(g\circ f)(a_{1})=(g\circ f)(a_{2})$, and injectivity of the composite gives $a_{1}=a_{2}$.
:::

:::

::: {.pf-step #counterexample}
(b) If $g\circ f$ is injective, $g$ need not be injective, so assertion (b) is false.

:::: pf-proof

::: {.pf-step #data}
Let $A=\theset{0}$, $B=\theset{0,1}$, $C=\theset{0}$, let $f(0)=0$ and let $g(0)=g(1)=0$.

::: pf-proof
These are legitimate functions: $f$ maps the single element of $A$ into $B$ and $g$ maps both elements of $B$ into the single element of $C$.
:::

:::

::: {.pf-step #properties}
$g\circ f$ is injective and $g$ is not.

::: pf-proof
$g\circ f\colon A\to C$ has domain $A=\theset{0}$ with a single element, and a function with a one-element domain is injective, since the hypothesis $a_{1}\neq a_{2}$ is never satisfied. On the other hand $g(0)=g(1)=0$ with $0\neq1$, so $g$ is not injective.
:::

:::

::::

:::

::: pf-step
Therefore (a) holds and (b) fails.

::: pf-proof
Step [](#composite-injective){.pf-ref} proves the assertion (a). Assertion (b) is a conjunction, that $f$ and $g$ are both injective; step [](#f-injective){.pf-ref} gives the first conjunct and step [](#counterexample){.pf-ref} exhibits a case where the second fails, so the conjunction is false and (b) is refuted. The correct statement in the direction of (b) is that $g\circ f$ injective forces $f$ injective, while $g$ need only be injective on the image of $f$.
:::

:::

:::

:::
