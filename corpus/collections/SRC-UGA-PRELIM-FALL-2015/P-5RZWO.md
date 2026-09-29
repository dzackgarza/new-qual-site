---
schema: qual/card@1
id: P-5RZWO
kind: problem
title: Composition of injective maps is injective
classification:
  areas:
  - prelim
  topics:
  - Functions and Relations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Suppose $f$ and $g$ are injective maps of a set $S$ into itself.
Show that the composite function $f\circ g$ is also injective.
:::

::: {.solution}
1. Lemma: $f$ is injective $\iff f$ has a left inverse $\inverseof{f}$ satisfying $\inverseof{f} f(a) = a$.

   Suppose $f,g: A \to A$ are injective and $x,y \in A$, we want to show that $(f\circ g)(x) = (f\circ g)(y) \implies x = y$.
   So suppose $f(g(x)) = f(g(y))$.
   Since $f$ is injective, $f$ has a left inverse, so $g(x) = g(y)$, and since $g$ is injective $x = y$.
   $\qed$
:::

::: {.solution}
**Goal:** Prove that if $A$ is a set and $f, g: A \to A$ are injective functions, then their composition $f \circ g: A \to A$ is injective.

::: pf

::: {.pf-step #s1}

Definition: A function $h: A \to A$ is injective if for all $x, y \in A$, $h(x) = h(y) \implies x = y$.

::: pf-proof

By the standard definition of injectivity.

:::

:::

::: {.pf-step #s2}

Assume $f: A \to A$ and $g: A \to A$ are injective functions.
Let $x, y \in A$ and assume $(f \circ g)(x) = (f \circ g)(y)$.

::: pf-proof

By setting up the hypothesis of the implication in step [](#s1){.pf-ref} for $h = f \circ g$.

:::

:::

::: {.pf-step #s3}

$f(g(x)) = f(g(y))$.

::: pf-proof

By definition of function composition, $(f \circ g)(x) = f(g(x))$ and $(f \circ g)(y) = f(g(y))$, so this follows from step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

$g(x) = g(y)$.

::: pf-proof

By step [](#s2){.pf-ref}, $f$ is injective.

Applying the definition of injectivity to the elements $g(x), g(y) \in A$ with $f(g(x)) = f(g(y))$ from step [](#s3){.pf-ref} yields $g(x) = g(y)$.

:::

:::

::: {.pf-step #s5}

$x = y$.

::: pf-proof

By step [](#s2){.pf-ref}, $g$ is injective.

Applying the definition of injectivity to $x, y \in A$ with $g(x) = g(y)$ from step [](#s4){.pf-ref} yields $x = y$.

:::

:::

::: pf-step

Conclusion: $f \circ g$ is injective.

::: pf-proof

We showed in steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} that for all $x, y \in A$, $(f \circ g)(x) = (f \circ g)(y) \implies x = y$.

:::

:::

:::

By step [](#s1){.pf-ref}, $f \circ g$ is injective.
Q.E.D.
:::
