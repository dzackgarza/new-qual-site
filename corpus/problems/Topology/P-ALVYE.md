---
schema: qual/card@1
id: P-ALVYE
kind: problem
title: $T\cup_f D^2$ with $f$ attaching inside the torus (question unrecovered)
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The problem list of the Topology Problems (Solutions) extraction has no Simplicial Homology section; solutions item 2.5.5 is only the phrase quoted on the card. No copy of the question was found in assets/ or ~/gitclones (qual-wiki holds the same solutions file). The statement is marked unrecovered, not reconstructed."
---

::: {.problem}
The question is unrecovered. The source retains only the item "$T\cup_f D^2$, where $f$ attaches inside the torus" in a list of spaces under the heading Simplicial Homology. It gives no instruction and does not specify the attaching curve.
:::

::: {.solution}

The argument is the card's own; the exercise as retained supplies no attaching curve, and the two computations below are what shows that the missing datum changes the answer.

Let $T^{2}=S^{1}\times S^{1}$ and, for a continuous $f:S^{1}\to T^{2}$, let $X_{f}=T^{2}\cup_{f}D^{2}$ be the adjunction space, that is the quotient of the disjoint union $T^{2}\sqcup D^{2}$ by the identification of $z\in\partial D^{2}$ with $f(z)$.

::: pf

::: {.pf-step #null}
If $f$ is null-homotopic then $X_{f}$ has $\pi_{1}(X_{f})\cong\ZZ^{2}$ and $H_{1}(X_{f})\cong\ZZ^{2}$, the homology of $T^{2}\vee S^{2}$.

::: pf-proof
$\pi_{1}(T^{2})=\ZZ^{2}$ (Theorem 60.1). Attaching a $2$-cell along $f$ adds the single relation $[f]=1$ to the fundamental group: by van Kampen applied to the open cover by a small neighbourhood of $T^{2}$ and the interior of the attached disc, whose intersection is an annulus homotopy equivalent to $S^{1}$, the group is $\pi_{1}(T^{2})*_{\ZZ}1=\pi_{1}(T^{2})/\langle[f]\rangle$. If $f$ is null-homotopic then $[f]=1$, so the relation is vacuous and $\pi_{1}(X_{f})=\ZZ^{2}$. Its abelianisation gives $H_{1}(X_{f})=\ZZ^{2}$ by the Hurewicz theorem in dimension one.
:::

:::

::: {.pf-step #primitive}
If $f$ represents a primitive class of $\ZZ^{2}$, then $\pi_{1}(X_{f})\cong\ZZ$ and $H_{1}(X_{f})\cong\ZZ$.

::: pf-proof
Let $f$ be the standard inclusion of the first factor, whose class in $\pi_{1}(T^{2})=\langle a,b\rangle$ is $a$. The same van Kampen computation gives
$$
\pi_{1}(X_{f})\cong\langle a,b\mid a=1\rangle\cong\langle b\rangle\cong\ZZ,
$$
and $H_{1}(X_{f})=\ZZ$ by abelianisation (Corollary 75.2), the presentation having the single relator $a$.
:::

:::

::: {.pf-step #answer}
The two spaces are not homotopy equivalent, so the homology of $T^{2}\cup_{f}D^{2}$ depends on the attaching map, and the retained question does not determine it.

::: pf-proof
Steps [](#null){.pf-ref} and [](#primitive){.pf-ref} give $\pi_{1}$ of order type $\ZZ^{2}$ in one case and $\ZZ$ in the other. A homotopy equivalence would induce an isomorphism of fundamental groups (Corollary 52.5 and homotopy invariance), and $\ZZ^{2}\not\cong\ZZ$; so $X_{f}$ is not homotopy equivalent to $X_{f'}$ for the two choices, and their first homology groups $\ZZ^{2}$ and $\ZZ$ differ as well. Since the retained item records only "attaches inside the torus", which does not specify the class of $f$, no homology group is determined by the data on the card.
:::

:::

:::
:::
