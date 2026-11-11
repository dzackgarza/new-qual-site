---
schema: qual/card@1
id: E-DX7N2
kind: problem
title: The seventeen basic properties under continuous maps
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Supplementary Exercises: Review of the
    Basics, Exercise 6, printed p. 229, with Theorem 23.5, the remark after Example 5 of Section 24,
    Theorem 26.5, Exercise 28.3(a), Exercise 30.11 and one witness for each of the eleven properties
    that fail. No published solution was located (search recorded on E-PWXIV and in the
    COMPLAINTS.md entry). What was corrected: the eleven witnesses are now written out. An earlier
    revision said only that "quotient maps give failures of Hausdorffness, regularity, normality, the
    countability axioms, and metrizability", and named as the witness for the countability axioms and
    for metrizability the quotient of the disjoint union of countably many circles "onto the Hawaiian
    earring". That is wrong on three counts. The map described is not a quotient map: it is a
    continuous bijection from a countable disjoint union of circles onto the earring, and for a
    continuous bijection the quotient topology on the target is its own topology exactly when the
    bijection is a homeomorphism, which this one is not -- the image of a small neighbourhood of a
    base point is an arc of one circle, and no open set of the earring containing the common point is
    that. The earring itself is first countable, being a subspace of R^2, so it cannot witness the
    failure of either countability axiom. And the space which fails first countability is the wedge,
    the quotient of the disjoint union which identifies all the base points, which is not the
    earring. Each failure is now carried by an explicit witness of the form "identity from a finer
    topology", which needs no quotient.
---

::: {.exercise}

Consider the seventeen properties listed in Exercise 1 of the Supplementary Exercises (Review of the Basics).

Which of these properties are preserved by continuous maps?
:::

::: {.solution}
Exactly the following six properties of the list are preserved by continuous maps:
$$
\boxed{(1),\ (2),\ (5),\ (6),\ (14),\ (15).}
$$
That is: connectedness, path connectedness, compactness, limit point compactness, Lindelöfness, and the existence of a countable dense subset. None of the other eleven is preserved, and a witness is given for each below.

**The six positive entries.**
(1) The continuous image of a connected space is connected, Theorem 23.5.
(2) The continuous image of a path connected space is path connected: if $g: X \to Y$ is continuous and $f: [0,1] \to X$ is a path from $x$ to $x'$, then $g \circ f$ is a path from $g(x)$ to $g(x')$. This is the remark after Example 5 of §24.
(5) The continuous image of a compact space is compact, Theorem 26.5.
(6) The continuous image of a limit point compact space is limit point compact, Exercise 28.3(a): if $A \subseteq f(X)$ is infinite, choose a countably infinite $B \subseteq A$ and one point $x_b$ of each nonempty fibre $f^{-1}(b)$ over $B$; the set of the $x_b$ is infinite, so it has a limit point $x$ by hypothesis, and $f(x)$ is then a limit point of $f(\theset{x_b}) = B$, hence of $A$.
(14) If $f: X \to Y$ is continuous and $X$ is Lindelöf, pull an open cover of $f(X)$ back to $X$, take a countable subcover, and push it forward: $f(X)$ is Lindelöf.
(15) If $D \subseteq X$ is a countable dense subset then $f(D)$ is a countable dense subset of $f(X)$, since $f(\bar D) \subseteq \overline{f(D)}$.

**The eleven negative entries.** Each witness is a continuous surjection whose domain has the property and whose image does not. In every case the domain is a discrete space, which is the finest topology on its underlying set, so the identity map out of it is continuous; discreteness gives Hausdorffness, regularity, normality, first countability, local compactness, local connectedness, local path connectedness and local metrizability, so the domain is never the obstruction. The targets are spaces of this chapter.

- (3) Locally connected: the identity from $\NN$ with the discrete topology onto $\QQ$ with the usual topology. The rationals are neither connected nor locally connected, Example 3 of §25. The same map refutes (4) local path connectedness, a path connected neighbourhood being connected.
- (7) Locally compact Hausdorff: the identity from $\NN$ with the discrete topology onto $\QQ$. The rationals are not locally compact, Example 1 of §29, though $\QQ$ is Hausdorff.
- (8) Hausdorff: the identity from $\NN$ with the discrete topology onto $\NN$ with the finite complement topology. Any two nonempty open sets of that topology meet, since their complements are finite, so the space is not Hausdorff.
- (9) Regular: the identity from $\RR$ with the discrete topology onto $\RR_K$. The space $\RR_K$ is Hausdorff and not regular, Example 1 of §31.
- (10) Completely regular: the same map onto $\RR_K$. A completely regular space is regular, since the preimages of $[0,\frac{1}{2})$ and $(\frac{1}{2},1]$ under a separating function are disjoint open sets, so $\RR_K$ is not completely regular either.
- (11) Normal: the identity from $\RR$ with the discrete topology onto the Sorgenfrey plane $\RR_\ell^2$, which is not normal, Example 3 of §31.
- (12) First countable: the identity from $\RR$ with its usual topology — first countable, and a finer topology is not needed here because the target is coarser — onto $\RR$ with the co-countable topology, in which the open sets are the sets with countable complement. That identity is continuous, the co-countable topology being contained in the usual one. The image is not first countable: given countably many co-countable neighbourhoods $U_n$ of a point $x$, choose $y_n \in U_n$ with $y_n \neq x$; then $\RR - \theset{y_n}$ is a co-countable neighbourhood of $x$ containing none of the $U_n$, so no countable family of neighbourhoods of $x$ is a local base.
- (13) Second countable: the same map onto $\RR$ with the co-countable topology. That space has no countable basis: if $\mathcal{B} = \theset{B_n}$ were a countable basis, each $B_n$ is co-countable, and choosing $x_n \in B_n$ gives the open set $\RR - \theset{x_n}$, which must contain some $B_k$, whence $x_k \in B_k \subseteq \RR - \set{x_k}$, a contradiction.
- (16) Locally metrizable: the identity from $\RR$ with the discrete topology onto $\RR_\ell$. The Sorgenfrey line is regular and Lindelöf, Examples 2 of §31 and 3 of §30, so by Exercise 34.8 it would be metrizable if it were locally metrizable, and it is not metrizable, Exercise 30.6.
- (17) Metrizable: the same map onto $\RR_\ell$, which is not metrizable, Exercise 30.6.

A remark on the device. A finer topology inherits from a coarser one its closed sets, hence Hausdorffness, regularity and normality; that is why the domain of a witness above can be taken discrete, which is the finest topology on a set. It inherits neither countability axiom, nor compactness, nor local compactness, and the targets of the entries (12) and (13) are deliberately coarser than the usual topology of $\RR$ rather than finer.
:::
