---
schema: qual/card@1
id: T-FLATCRIT
kind: theorem
title: The local and infinitesimal criteria for flatness
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flatness
  - Tor Functors
  - Local Rings
relations:
- kind: uses
  target: D-DEFFLAT
- kind: uses
  target: D-DEFTOR
review: draft
prompts:
- What is the local criterion for flatness?
- What is the infinitesimal criterion for flatness?
---

::: {.theorem title="Local and infinitesimal criteria for flatness"}
Let $A$ be a Noetherian ring, $I \subseteq A$ an ideal, $B$ a Noetherian $A$-algebra with $IB$ contained in the Jacobson radical of $B$, and $M$ a finitely generated $B$-module.
The following are equivalent.

1. $M$ is flat over $A$.

2. $M/IM$ is flat over $A/I$ and $\Tor_1^A(A/I, M) = 0$.

3. $M/I^{n}M$ is flat over $A/I^{n}$ for every $n \geq 1$.

In particular, if $A \to B$ is a local homomorphism of Noetherian local rings with residue field $k$ of $A$ and $M$ is a finitely generated $B$-module, then $M$ is flat over $A$ if and only if $\Tor_1^A(k, M) = 0$.
:::

::: {.remark}
Condition 2 is the local criterion for flatness; with $I = \mathfrak{m}_A$ the hypothesis on $M/\mathfrak{m}_A M$ is automatic, because every module over the field $A/\mathfrak{m}_A$ is flat.
Condition 3 is the infinitesimal criterion for flatness: flatness over $A$ is detected on the infinitesimal thickenings $\Spec A/I^n$ of $\Spec A/I$.
Geometrically, for a morphism $f \colon X \to Y$ of locally Noetherian schemes, a point $x \in X$ and $y = f(x)$, a coherent sheaf $\mathcal{F}$ on $X$ is flat over $Y$ at $x$ if and only if $\Tor_1^{\OO_{Y,y}}(\kappa(y), \mathcal{F}_x) = 0$.
:::

::: {.example}
Let $A = k[t]_{(t)}$ and $B = (A[x]/(tx))_{(t, x)}$.
Then $\Tor_1^A(k, B)$ is the $t$-torsion of $B$, computed from $0 \to A \xrightarrow{t} A \to k \to 0$, and it contains $x \neq 0$.
So $B$ is not flat over $A$: the family $V(tx) \to \Spec k[t]$ has fibre the point $x = 0$ over $t \neq 0$ and the line $\AA^1$ over $t = 0$.
:::
