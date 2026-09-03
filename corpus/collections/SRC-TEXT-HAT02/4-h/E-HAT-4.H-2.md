---
schema: qual/card@1
id: E-HAT-4.H-2
kind: problem
title: "Cofibrations are preserved by pushout"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

Consider a pushout diagram where $B$ is $B$ with $X$ attached along $A$ via $f$.
Show that if $A \hookrightarrow X$ is a cofibration, so is $B \hookrightarrow B \sqcup_f X$.

::: {.solution}
<1>1. Homotopy Extension Property (HEP) setup for the pushout:
<2>1. Let $i: A \hookrightarrow X$ be a closed cofibration and let $f: A \to B$ be the attaching map.
Let $P = B \sqcup_f X$ be the pushout space, with canonical inclusions $j: B \hookrightarrow P$ and $q: X \to P$.
::: {.proof}
definition of adjunction space / pushout.
:::
<2>2. To show $j: B \hookrightarrow P$ is a cofibration, let $Y$ be an arbitrary topological space, $u: P \to Y$ a continuous map, and $H: B \times I \to Y$ a continuous homotopy such that $H(b, 0) = u(j(b))$ for all $b \in B$.
::: {.proof}
test data for the Homotopy Extension Property.
:::

<1>2. Lifting to $X$ via the cofibration $A \hookrightarrow X$:
<2>1. Define the initial map on $X$: $u_X = u \circ q: X \to Y$.
::: {.proof}
composition of continuous maps.
:::
<2>2. Define the homotopy on $A$: $h_A = H \circ (f \times \operatorname{id}_I): A \times I \to Y$.
For $t = 0$: $h_A(a, 0) = H(f(a), 0) = u(j(f(a))) = u(q(i(a))) = u_X(i(a))$.
::: {.proof}
pushout identification $j(f(a)) = q(i(a))$ in $P$.
:::
<2>3. Since $i: A \hookrightarrow X$ is a cofibration, the pair $(u_X, h_A)$ satisfies the HEP for $(X, A)$.
Thus there exists a continuous homotopy $H_X: X \times I \to Y$ such that:
\[
H_X(x, 0) = u_X(x) \quad \text{for all } x \in X, \qquad H_X(i(a), t) = h_A(a, t) = H(f(a), t) \quad \text{for all } (a, t) \in A \times I.
\]
::: {.proof}
definition of cofibration for $A \hookrightarrow X$.
:::

<1>3. Pasting homotopies on the pushout $P \times I$:
<2>1. Since $P \times I \cong (B \times I) \sqcup_{f \times \operatorname{id}_I} (X \times I)$ is the pushout of $B \times I$ and $X \times I$ along $A \times I$, define $\widetilde{H}: P \times I \to Y$ by:
\[
\widetilde{H}(p', t) = \begin{cases}
H(b, t) & \text{if } p' = j(b) \in j(B), \\
H_X(x, t) & \text{if } p' = q(x) \in q(X).
\end{cases}
\]
::: {.proof}
universal property of pushouts.
:::
<2>2. On the overlap $A \times I$, $H(f(a), t) = H_X(i(a), t)$ by <1>2 step <2>3, so $\widetilde{H}$ is well-defined and continuous on $P \times I$.
::: {.proof}
Gluing Lemma for pushouts.
:::
<2>3. Verify the initial condition:
For $b \in B$, $\widetilde{H}(j(b), 0) = H(b, 0) = u(j(b))$.
For $x \in X$, $\widetilde{H}(q(x), 0) = H_X(x, 0) = u_X(x) = u(q(x))$.
Thus $\widetilde{H}(\cdot, 0) = u$.
::: {.proof}
evaluation at $t = 0$.
:::
<2>4. Furthermore, $\widetilde{H}(j(b), t) = H(b, t)$, so $\widetilde{H}$ extends $H$.
::: {.proof}
definition of $\widetilde{H}$.
:::

<1>4. Conclusion:
$j: B \hookrightarrow B \sqcup_f X$ satisfies the Homotopy Extension Property, so cofibrations are preserved under pushouts. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
