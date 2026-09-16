---
schema: qual/card@1
id: D-IV2ETCOV
kind: definition
title: Étale covers, trivial covers, and simple connectedness of $\PP^1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Étale Morphisms
  - Fundamental Group
  - Riemann-Hurwitz
relations:
- kind: uses
  target: D-MORETALE
- kind: uses
  target: T-LKT0U
review: draft
prompts:
- What is an étale cover, and what is a trivial one?
- What does it mean for a curve to be simply connected?
- Prove that $\PP^1$ has no nontrivial étale covers.
- Is $\AA^1$ simply connected?
---

::: {.definition title="Étale cover"}
A morphism $f : X \to Y$ is an \dfn{étale cover} if it is finite and étale.
It is a **trivial** cover if $X \cong \coprod_{i \in I} Y$ for a finite index set $I$, with $f$ the identity on each copy.
$Y$ is **simply connected** if every étale cover of $Y$ is trivial, equivalently $\pi_1^{\Et}(Y) = 0$.
:::

::: {.theorem}
$\PP^1_k$ over $k = \kbar$ is simply connected, in every characteristic.
:::

::: {.proof}
Let $f : X \to \PP^1$ be an étale cover; it is enough to treat $X$ connected, and then to show $f$ is an isomorphism.
$X$ is regular because $f$ is étale and $\PP^1$ is smooth over $k$, and a connected regular scheme is irreducible, so $X$ is a curve; $f$ is finite, so $X$ is projective; $f$ is unramified, so $k(X)/k(\PP^1)$ is separable.
Riemann--Hurwitz therefore applies, and $R = 0$ since $f$ is unramified, so with $n = \deg f$,
\[
2 g_X - 2 = n(2 \cdot 0 - 2) = -2n .
\]
Then $g_X \geq 0$ gives $-2n \geq -2$, so $n = 1$ and $g_X = 0$, and a finite morphism of degree $1$ between curves is an isomorphism.
:::

::: {.remark title="Reading the argument"}
Every hypothesis is spent in one place and the examiner asks for exactly that accounting: finiteness makes $X$ a projective curve so that the genus exists, étaleness supplies both the separability that lets Riemann--Hurwitz run and the vanishing $R = 0$ that makes it an equality with no correction term, and the inequality $g_X \geq 0$ is the only inequality used.
The argument is the algebraic analogue of the topological computation of $\pi_1(S^2)$ by Euler characteristic, with $2 - 2g$ in the role of $\chi$.

The characteristic plays no part, and that is the surprising half.
$\AA^1$ is *not* simply connected in characteristic $p$: the Artin--Schreier cover $y^p - y = x$ is finite étale of degree $p$ and connected, because $d(y^p - y) = -dy$ never vanishes.
So the projective line and the affine line separate here, the missing point at infinity is where the cover of $\AA^1$ ramifies wildly, and $\pi_1^{\Et}(\AA^1_{\overline{\FF}_p})$ is enormous while $\pi_1^{\Et}(\PP^1) = 0$.
Over $\CC$ both are topologically simply connected and the distinction is invisible, which is why the question is asked in characteristic $p$.
:::

::: {.remark title="Against the étale definition card"}
[[D-MORETALE]] names $\pi_1^{\Et}$ as the reason finite étale morphisms are the right notion of covering space but proves nothing about a particular curve.
This card is the computation that makes the name concrete, and it is also the first place where "étale cover" must be read as *finite* étale: an open immersion is étale and is not a cover, so dropping finiteness makes the statement false for trivial reasons.
:::
