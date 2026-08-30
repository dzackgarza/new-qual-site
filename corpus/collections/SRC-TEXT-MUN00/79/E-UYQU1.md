---
schema: qual/card@1
id: E-UYQU1
kind: exercise
title: Covering homomorphisms of abelian topological groups
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Topological Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Let $p: \overline{G} \to G$ be a homomorphism of topological groups that is a covering map.
Show that if $G$ is abelian, so is $\overline{G}$.
:::

::: {.solution}
<1>1. Definition and continuity of the commutator map:
<2>1. Define the commutator mapping $\phi: \overline{G} \times \overline{G} \to \overline{G}$ by:
\[
\phi(x, y) = [x, y] = x y x^{-1} y^{-1}.
\]
Because $\overline{G}$ is a topological group, the multiplication and inversion operations are continuous, so $\phi$ is continuous.
Proof: continuity of group operations in topological groups.
<2>2. Since $\overline{G}$ is connected, the product space $\overline{G} \times \overline{G}$ is connected, so its image $\phi(\overline{G} \times \overline{G})$ is a connected subset of $\overline{G}$.
Proof: continuous image of a connected space is connected.

<1>2. Fiber containment and discreteness:
<2>1. For any $(x, y) \in \overline{G} \times \overline{G}$, apply the covering homomorphism $p$:
\[
p(\phi(x, y)) = p\left(x y x^{-1} y^{-1}\right) = p(x) p(y) p(x)^{-1} p(y)^{-1} = [p(x), p(y)].
\]
Proof: $p$ is a group homomorphism.
<2>2. Because $G$ is abelian, $[p(x), p(y)] = e_G$ for all $x, y \in \overline{G}$.
Therefore:
\[
\phi(\overline{G} \times \overline{G}) \subseteq p^{-1}(e_G) = \ker(p).
\]
Proof: abelian group commutators are trivial.
<2>3. Because $p: \overline{G} \to G$ is a covering map, the fiber $p^{-1}(e_G)$ is a discrete subspace of $\overline{G}$.
Proof: fibers of covering spaces are discrete.

<1>3. Evaluation and conclusion:
<2>1. The connected set $\phi(\overline{G} \times \overline{G})$ is contained in the discrete space $\ker(p)$, so it must consist of a single point.
Proof: connected subsets of discrete topological spaces are singletons.
<2>2. Evaluating at the identity $(e_{\overline{G}}, e_{\overline{G}})$:
\[
\phi\left(e_{\overline{G}}, e_{\overline{G}}\right) = e_{\overline{G}}.
\]
Hence $\phi(x, y) = e_{\overline{G}}$ for all $x, y \in \overline{G}$.
Proof: identity evaluation.
<2>3. This gives $x y x^{-1} y^{-1} = e_{\overline{G}}$, which is equivalent to $xy = yx$ for all $x, y \in \overline{G}$.
Thus $\overline{G}$ is abelian.
Proof: definition of abelian group.

<1>4. Conclusion:
$\overline{G}$ is abelian. Q.E.D.
Proof: <1>1 through <1>3.
:::
