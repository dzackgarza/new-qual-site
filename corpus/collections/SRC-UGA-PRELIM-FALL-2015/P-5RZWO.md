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
---

::: problem
Suppose $f$ and $g$ are injective maps of a set $S$ into itself. Show that the composite function $f\circ g$ is also injective.
:::

::: solution
1. Lemma: $f$ is injective $\iff f$ has a left inverse $f\inv$ satisfying $f\inv f(a) = a$.

   Suppose $f,g: A \to A$ are injective and $x,y \in A$, we want to show that $(f\circ g)(x) = (f\circ g)(y) \implies x = y$.
   So suppose $f(g(x)) = f(g(y))$.
   Since $f$ is injective, $f$ has a left inverse, so $g(x) = g(y)$, and since $g$ is injective $x = y$.
   $\qed$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Prove that if $A$ is a set and $f, g: A \to A$ are injective functions, then their composition $f \circ g: A \to A$ is injective.

<1>1. Definition: A function $h: A \to A$ is injective if for all $x, y \in A$, $h(x) = h(y) \implies x = y$.
Proof: By the standard definition of injectivity.

<1>2. Assume $f: A \to A$ and $g: A \to A$ are injective functions.
Let $x, y \in A$ and assume $(f \circ g)(x) = (f \circ g)(y)$.
Proof: By setting up the hypothesis of the implication in <1>1 for $h = f \circ g$.

<1>3. $f(g(x)) = f(g(y))$.
Proof: By definition of function composition, $(f \circ g)(x) = f(g(x))$ and $(f \circ g)(y) = f(g(y))$, so this follows from <1>2.

<1>4. $g(x) = g(y)$.
Proof: By <1>2, $f$ is injective.
Applying the definition of injectivity to the elements $g(x), g(y) \in A$ with $f(g(x)) = f(g(y))$ from <1>3 yields $g(x) = g(y)$.

<1>5. $x = y$.
Proof: By <1>2, $g$ is injective.
Applying the definition of injectivity to $x, y \in A$ with $g(x) = g(y)$ from <1>4 yields $x = y$.

<1>6. Conclusion: $f \circ g$ is injective.
Proof: We showed in <1>2–<1>5 that for all $x, y \in A$, $(f \circ g)(x) = (f \circ g)(y) \implies x = y$.
By <1>1, $f \circ g$ is injective.
Q.E.D.
:::
