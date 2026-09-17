---
schema: qual/card@1
id: P-AGH33LOCALRINGS
kind: problem
title: Morphisms and the induced maps on local rings
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms
  - Local Rings
  - Dominant Morphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all three parts with Hartshorne I.3.3. The proof constructs the stalk map on germs, proves the homeomorphism-plus-stalk criterion locally, and proves injectivity for dense image using density of the image of every nonempty open subset.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Reviewed the germ construction and both converse arguments against the source exercise and published solution notes. In part (c), the proof avoids assuming that the image of a neighborhood is open: it proves directly that its image is dense.'
---

::: {.problem}
(a) Let $\phi: X \to Y$ be a morphism.
Show that for each $P \in X$, $\phi$ induces a homomorphism of local rings $\phi_P^* : \mco_{\phi(P), Y} \to \mco_{P, X}$.

(b) Show that a morphism $\phi$ is an isomorphism if and only if $\phi$ is a homeomorphism and the induced map $\phi_P^*$ on local rings is an isomorphism for all $P \in X$.

(c) Show that if $\phi(X)$ is dense in $Y$, then $\phi_P^*$ is injective for all $P \in X$.
:::

::: {.solution}
For a point $P\in X$, write $Q=\phi(P)$.
A germ in $\mco_{Q,Y}$ will be represented by a regular function $f$ on an open neighborhood $U$ of $Q$.

<1>1. The rule
$$
\phi_P^*([f]_Q)=[f\circ\phi]_P
$$
defines a homomorphism of local rings $\phi_P^*: \mco_{Q,Y}\to\mco_{P,X}$, proving (a).

::: {.proof}
Because $\phi$ is a morphism, $f\circ\phi$ is regular on the open neighborhood $\phi^{-1}(U)$ of $P$.
If two representatives $f$ on $U$ and $g$ on $V$ determine the same germ at $Q$, then they agree on some open neighborhood $W\subseteq U\cap V$ of $Q$.
Their pullbacks therefore agree on the neighborhood $\phi^{-1}(W)$ of $P$, so the displayed rule is independent of the representative.
It plainly preserves sums, products, and $1$.

The maximal ideal of $\mco_{Q,Y}$ consists of germs vanishing at $Q$, and similarly at $P$.
Since
$$
(f\circ\phi)(P)=f(Q),
$$
we have
$$
(\phi_P^*)^{-1}(\mathfrak m_{P,X})=\mathfrak m_{Q,Y}.
$$
Thus $\phi_P^*$ is a local homomorphism.
:::

<1>2. If $\phi$ is an isomorphism, then it is a homeomorphism and every $\phi_P^*$ is an isomorphism.

::: {.proof}
Let $\psi=\phi^{-1}$ be the inverse morphism.
The underlying continuous maps $\phi$ and $\psi$ are inverse to one another, hence $\phi$ is a homeomorphism.
Pullback of germs is functorial under composition, so
$$
\psi_Q^*\circ\phi_P^*=\operatorname{id}_{\mco_{Q,Y}},
\qquad
\phi_P^*\circ\psi_Q^*=\operatorname{id}_{\mco_{P,X}}.
$$
Hence $\phi_P^*$ is an isomorphism with inverse $\psi_Q^*$.
:::

<1>3. Conversely, if $\phi$ is a homeomorphism and every $\phi_P^*$ is an isomorphism, then the inverse homeomorphism $\psi=\phi^{-1}:Y\to X$ is a morphism.

::: {.proof}
It is enough to check locally that pullback by $\psi$ preserves regular functions.
Let $Q\in Y$, put $P=\psi(Q)$, and let $f$ be regular on an open neighborhood $U$ of $P$.
Because $\phi_P^*$ is surjective, there is a germ $[g]_Q\in\mco_{Q,Y}$ with
$$
\phi_P^*([g]_Q)=[f]_P.
$$
Choose $g$ regular on an open neighborhood $V$ of $Q$.
Equality of these germs means that, after shrinking to an open neighborhood
$$
U'\subseteq U\cap\phi^{-1}(V)
$$
of $P$, we have $g\circ\phi=f$ on $U'$.

Because $\phi$ is a homeomorphism, $W=\phi(U')$ is an open neighborhood of $Q$ contained in $V$.
On $W$ we therefore have
$$
f\circ\psi=g,
$$
so $f\circ\psi$ is regular near $Q$.
Since $Q$ and $f$ were arbitrary, $\psi$ is a morphism.
Thus $\phi$ is an isomorphism, completing (b).
:::

<1>4. If $\phi(X)$ is dense in $Y$, then the image of every nonempty open subset of $X$ is dense in $Y$.

::: {.proof}
Let $U\subseteq X$ be nonempty and open.
Since a variety is irreducible, $U$ is dense in $X$.
Let $C=\overline{\phi(U)}\subseteq Y$.
Then $\phi^{-1}(C)$ is a closed subset of $X$ containing $U$, so density of $U$ gives $\phi^{-1}(C)=X$.
Hence $\phi(X)\subseteq C$.
By hypothesis $\phi(X)$ is dense in $Y$, and therefore $C=Y$.
:::

<1>5. Under the hypothesis of (c), the map $\phi_P^*$ is injective for every $P\in X$.

::: {.proof}
Fix $P\in X$, put $Q=\phi(P)$, and suppose $[f]_Q\in\mco_{Q,Y}$ satisfies
$$
\phi_P^*([f]_Q)=0.
$$
Choose a representative $f$ regular on an open neighborhood $V$ of $Q$.
The vanishing of the pullback germ gives a nonempty open neighborhood
$$
U\subseteq\phi^{-1}(V)
$$
of $P$ on which $f\circ\phi=0$.
By step <1>4, $\phi(U)$ is dense in $Y$, hence dense in the open subspace $V$.
The zero set of the regular function $f$ is closed in $V$ and contains $\phi(U)$, so it is all of $V$.
Thus $f=0$ on $V$, whence $[f]_Q=0$.
Therefore $\phi_P^*$ is injective.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>1 proves (a), steps <1>2--<1>3 prove (b), and steps <1>4--<1>5 prove (c).
:::
:::
