---
schema: qual/card@1
id: P-JHUSP02CAC
kind: problem
title: Classification of simply connected regions in the Riemann sphere
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Mapping Theorem
  - Conformal Maps
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the extended-plane scope, exhaustive classification request, and pairwise nonequivalence requirement with Spring 2002 Complex Analysis question 3."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Separated the whole sphere, one-point complement, and complement with at least two points; applied a Möbius normalization and the Riemann mapping theorem, then distinguished all three models by compactness and Liouville."
---

::: {.problem}
3. Classify all simply connected regions in the extended complex plane up to biholomorphic equivalence.
   i.e, give a list of simply connected region, prove that every simply connected region in the extended complex plane is biholomorphic equivalent to a member in your list.
   Prove also that no two members in your list are biholomorphic equivalent.
:::

::: {.solution}
Up to biholomorphic equivalence, the complete list is
$$
\boxed{\widehat{\CC},\qquad \CC,\qquad \Delta.}
$$

::: pf

::: pf-step

Every simply connected region in $\widehat{\CC}$ is equivalent to one of these three.

::: pf-proof

Let $U\subset\widehat{\CC}$ be a nonempty simply connected region.

If $U=\widehat{\CC}$, it is already the first model.

Suppose next that the complement consists of exactly one point $p$. A Möbius
transformation sending $p$ to $\infty$ maps $U$ biholomorphically onto
$\widehat{\CC}\setminus\{\infty\}=\CC$.

Finally suppose that $\widehat{\CC}\setminus U$ contains at least two
points. Choose $p$ in the complement and a Möbius transformation $M$ with
$M(p)=\infty$. Then
$$
V=M(U)\subset\CC
$$
is a simply connected plane domain. It is proper: a second point of the
complement is carried to a finite point outside $V$. By the Riemann mapping
theorem, every nonempty proper simply connected plane domain is biholomorphic
to the unit disk $\Delta$. Hence $U$ is biholomorphic to $\Delta$.

These three cases exhaust the possible complements.

:::

:::

::: pf-step

No two models in the list are biholomorphic.

::: pf-proof

The Riemann sphere is compact. A biholomorphism is in particular a
homeomorphism, so it preserves compactness. Neither $\CC$ nor $\Delta$
is compact; therefore the sphere is biholomorphic to neither of them.

It remains to distinguish $\CC$ and $\Delta$. If there were a
biholomorphism $F:\CC\to\Delta$, then $F$ would be a bounded entire
function. Liouville's theorem would force $F$ to be constant, contradicting
bijectivity. Thus $\CC$ and $\Delta$ are not biholomorphic.

Consequently the three displayed regions form a complete and irredundant
classification.

:::

:::

:::

:::
