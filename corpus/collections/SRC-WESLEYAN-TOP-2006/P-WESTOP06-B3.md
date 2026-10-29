---
schema: qual/card@1
id: P-WESTOP06-B3
kind: problem
title: Explicit deformation retraction of punctured Euclidean space onto the sphere
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $A\subset X$.

1. Define what it means for $A$ to be a deformation retract of $X$.
2. Construct explicitly a deformation retraction
   \[
   \RR^n\setminus\{0\}\longrightarrow S^{n-1}.
   \]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A subspace \(A\subseteq X\) is a deformation retract of \(X\) if there is a retraction \(r:X\to A\) and a homotopy
\[
H:X\times I\to X
\]
from \(\operatorname{id}_X\) to the composite \(i\circ r\), where \(i:A\hookrightarrow X\) is the inclusion, such that
\[
H(a,t)=a
\]
for every \(a\in A\) and \(t\in I\).


::: pf-proof

The condition \(r|_A=\operatorname{id}_A\) says that \(r\) is a retraction. The additional condition on \(H\) says that the homotopy from \(X\) onto \(A\) fixes \(A\) pointwise throughout.

:::

:::

::: {.pf-step #s1-2}

The map
\[
\boxed{r:\RR^n\setminus\{0\}\to S^{n-1},\qquad
r(x)=\frac{x}{\|x\|}}
\]
is a retraction.


::: pf-proof

For \(x\ne0\), one has \(\|x/\|x\|\|=1\), so \(r(x)\in S^{n-1}\). The map is continuous because the norm is continuous and \(\|x\|>0\) on the domain. If \(x\in S^{n-1}\), then \(\|x\|=1\), hence
\[
r(x)=x.
\]
Thus \(r|_{S^{n-1}}=\operatorname{id}_{S^{n-1}}\).

:::

:::

::: {.pf-step #s1-3}

Define
\[
H:(\RR^n\setminus\{0\})\times I\to\RR^n\setminus\{0\}
\]
by
\[
\boxed{H(x,t)=\left((1-t)+\frac{t}{\|x\|}\right)x.}
\]
Then \(H\) is a homotopy from \(\operatorname{id}\) to \(i\circ r\).


::: pf-proof

The scalar
\[
(1-t)+\frac{t}{\|x\|}
\]
is strictly positive for every \(x\ne0\) and \(t\in I\). Hence \(H(x,t)\ne0\), so the formula takes values in \(\RR^n\setminus\{0\}\). It is continuous because it is assembled from continuous operations on this domain.

At \(t=0\),
\[
H(x,0)=x,
\]
while at \(t=1\),
\[
H(x,1)=\frac{x}{\|x\|}=r(x)=i(r(x)).
\]
Therefore \(H\) is a homotopy from \(\operatorname{id}\) to \(i\circ r\).

:::

:::

::: {.pf-step #s1-4}

The homotopy \(H\) fixes \(S^{n-1}\) pointwise.


::: pf-proof

If \(x\in S^{n-1}\), then \(\|x\|=1\), so for every \(t\in I\),
\[
H(x,t)=((1-t)+t)x=x.
\]
Thus every point of the sphere remains fixed during the homotopy.

:::

:::

::: {.pf-step #s1-5}

\(S^{n-1}\) is a deformation retract of \(\RR^n\setminus\{0\}\).


::: pf-proof

Step [](#s1-2){.pf-ref} gives a retraction onto \(S^{n-1}\), step [](#s1-3){.pf-ref} gives a homotopy from the identity to that retraction followed by inclusion, and step [](#s1-4){.pf-ref} shows that this homotopy fixes \(S^{n-1}\) pointwise. These are exactly the conditions in step [](#s1-1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the requested definition, and step [](#s1-5){.pf-ref} gives the requested explicit deformation retraction.

:::

:::

:::
