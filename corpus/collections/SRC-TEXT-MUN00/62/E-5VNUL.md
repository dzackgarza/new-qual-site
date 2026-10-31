---
schema: qual/card@1
id: E-5VNUL
kind: problem
title: The Borsuk lemma fails without injectivity
classification:
  areas:
  - topology
  topics:
  - Invariance of Domain
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Give an example to show that the conclusion of the Borsuk lemma need not hold if $f$ is not injective.
:::

::: {.solution}

::: pf

::: pf-step

Statement of the Borsuk lemma:
    Munkres Lemma 62.2 says that if $a,b\in S^2$, $A$ is compact, and $f:A\to S^2\setminus\{a,b\}$ is continuous, injective, and nullhomotopic, then $a$ and $b$ lie in the same component of $S^2\setminus f(A)$.

:::

::: pf-step

Construction of non-injective counterexample:
    *Proof:*

::: pf-proof

::: pf-step

Identify $S^2$ with $\RR^2\cup\{\infty\}$, and take $a=(0,0)$, $b=\infty$, and $A=[0,1]$.

:::

::: pf-step

$A$ is compact and contractible.

:::

::: pf-step

Every map from $A$ into a path-connected space is nullhomotopic.

:::

::: pf-step

Define the continuous map $f:A\to S^2\setminus\{a,b\}$ by
        $$f(t)=(\cos2\pi t,\sin2\pi t).$$

:::

::: pf-step

The map is nullhomotopic because $A$ is contractible, but it is not injective since $f(0)=f(1)=(1,0)$.

:::

:::

:::

::: pf-step

Failure of the Borsuk conclusion for the image:
    *Proof:*

::: pf-proof

::: pf-step

The image $f(A)$ is the unit circle $S^1 = \{(x, y) \in \RR^2 \mid x^2 + y^2 = 1\}$.

:::

::: pf-step

The circle separates $a=(0,0)$ from $b=\infty$ in $S^2$. They lie in different components of $S^2\setminus f(A)$.

:::

::: pf-step

Thus the conclusion of Lemma 62.2 fails for this continuous nullhomotopic map when injectivity is removed.

:::

:::

:::

::: pf-step

Conclusion:

:::

:::

    The conclusion of the Borsuk lemma fails without the hypothesis of injectivity. Q.E.D.
:::
