---
schema: qual/card@1
id: P-QRCUN
kind: problem
title: The distance between compact sets in a metric space is attained
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked the statement against Section A, problem A4 of the January 18, 2002 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Minimized the continuous function (a,b) |-> d(a,b) on the compact product
    A x B. Continuity is justified directly from the triangle inequality, so
    the argument does not assume the desired attainment statement.
---

::: {.problem}
If $(X,d)$ is a metric space, and $A, B \subseteq X$ are non-empty, then we define the *distance between $A$ and $B$* by $$d(A,B) = \inf\{d(a,b) : a \in A, b \in B\}$$ where $d : X \times X \to \RR$ is the metric.
Show that if $A$ and $B$ are both compact and non-empty, then there are $a_0 \in A$ and $b_0 \in B$ so that $$d(A,B) = d(a_0,b_0).$$
:::

::: {.solution}
Define $F\colon A\times B\to\RR$ by $F(a,b)=d(a,b)$.

::: pf

::: {.pf-step #f-continuous}
$F$ is continuous.

::: pf-proof
For $(a,b),(a',b')\in A\times B$, the triangle inequality gives $d(a,b)\le d(a,a')+d(a',b')+d(b',b)$, so $d(a,b)-d(a',b')\le d(a,a')+d(b,b')$.
Interchanging $(a,b)$ and $(a',b')$ gives the reverse inequality, hence
$$\abs{d(a,b)-d(a',b')}\le d(a,a')+d(b,b').$$
Thus, if $d(a,a')<\varepsilon/2$ and $d(b,b')<\varepsilon/2$, then $\abs{F(a,b)-F(a',b')}<\varepsilon$, which is continuity in the product topology on $A\times B$.
:::

:::

::: {.pf-step #product-compact}
$A\times B$ is compact and nonempty.

::: pf-proof
A finite product of compact spaces is compact, and a product of nonempty sets is nonempty.
:::

:::

::: {.pf-step #f-attains-minimum}
$F$ attains a minimum at some $(a_0,b_0)\in A\times B$.

::: pf-proof
By steps [](#f-continuous){.pf-ref} and [](#product-compact){.pf-ref}, $F(A\times B)$ is a nonempty compact subset of $\RR$, so it has a least element.
Choose $(a_0,b_0)\in A\times B$ with $F(a_0,b_0)=\min F(A\times B)$.
:::

:::

::: pf-qed
By definition, $d(A,B)=\inf\{d(a,b):a\in A,\ b\in B\}=\inf F(A\times B)$.
By step [](#f-attains-minimum){.pf-ref} this set has minimum $d(a_0,b_0)$, and the infimum of a set with a minimum equals that minimum, so $d(A,B)=d(a_0,b_0)$.
:::

:::

:::
