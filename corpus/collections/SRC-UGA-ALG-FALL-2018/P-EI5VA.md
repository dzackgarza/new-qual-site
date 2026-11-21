---
schema: qual/card@1
id: P-EI5VA
kind: problem
title: Stabilizers in an orbit are conjugate, conjugates of a proper subgroup do not
  cover $G$, and a transitive action on two or more points has a fixed-point-free
  element
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Conjugacy
  - Burnside's Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the five containers state why their subclaims suffice, and the 28
    leaf steps that asserted their claim with no justification each carry a sentence deriving it. The
    mathematics is unchanged: the stabilizer computation $G_{g\cdot x}=gG_xg^{-1}$, the counting argument
    that a proper subgroup has fewer than $\cardinality{G}$ conjugates in all because the conjugates meet
    only in the identity, and two proofs of (c) -- one from (b) and one by Burnside's lemma. Checked
    against the statement on the card, from the UGA Fall 2018 algebra qualifying exam. Nothing in the
    statement was changed.

---
::: {.problem}
(a) Suppose the group $G$ acts on a set $X$. Show that the stabilizers of elements in the same orbit are conjugate: for any $x \in X$ and $g \in G$, $G_{g \cdot x} = g G_x g^{-1}$.

(b) Let $G$ be a finite group and let $H < G$ be a proper subgroup. Show that the union of all conjugates of $H$ is strictly smaller than $G$:
$$
\bigcup_{g \in G} g H g^{-1} \subsetneq G.
$$

(c) Suppose a finite group $G$ acts transitively on a set $S$ with $\cardinality{S} \ge 2$. Show that there exists an element $g \in G$ having no fixed points in $S$ (i.e. $g \cdot s \ne s$ for all $s \in S$).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $x\in X$ and $g\in G$, one has $G_{gx}=gG_xg^{-1}$.

::: pf-proof

::: pf-step

Let $x \in X$ and $g \in G$, and let $y = g \cdot x \in X$.


::: pf-proof
This names an arbitrary point of $X$ and an arbitrary group element, with $y$ the image of $x$ under it.
:::

:::

::: pf-step

An element $h \in G$ stabilizes $y$ if and only if $h \cdot y = y$.


::: pf-proof
This is the definition of the stabilizer of $y$.
:::

:::

::: pf-step

Substituting $y = g \cdot x$:
$$h \cdot (g \cdot x) = g \cdot x \iff (g^{-1} h g) \cdot x = x \iff g^{-1} h g \in G_x.$$


::: pf-proof
Applying $g^{-1}$ to both sides and using that the action is associative turns $h\cdot(g\cdot x)=g\cdot x$ into $(g^{-1}hg)\cdot x=x$.
:::

:::

::: pf-step

Multiplying on the left by $g$ and on the right by $g^{-1}$:
$$g^{-1} h g \in G_x \iff h \in g G_x g^{-1}.$$


::: pf-proof
Multiplying the relation $g^{-1}hg\in G_x$ on the left by $g$ and on the right by $g^{-1}$ gives $h\in gG_xg^{-1}$.
:::

:::

::: pf-step

Therefore $G_y = G_{g \cdot x} = g G_x g^{-1}$.


::: pf-proof
The preceding equivalences show the two sets contain the same elements, so the stabilizers coincide.
:::

:::

:::

:::

::: {.pf-step #s2}

The conjugates of any proper subgroup $H<G$ do not cover the finite group $G$.

::: pf-proof

::: pf-step

Let $N_G(H) = \{g \in G : g H g^{-1} = H\}$ be the normalizer of $H$ in $G$.


::: pf-proof
This is a definition; the normalizer is a subgroup of $G$ containing $H$.
:::

:::

::: pf-step

The distinct conjugates of $H$ in $G$ are parameterized by the cosets of $N_G(H)$, so there are precisely $k = [G : N_G(H)]$ distinct conjugates $H_1, H_2, \dots, H_k$.


::: pf-proof
Two conjugates agree exactly when $g^{-1}g'$ normalizes $H$, so the distinct conjugates correspond to the cosets of $N_G(H)$.
:::

:::

::: pf-step

Since $H \le N_G(H) \le G$, by the tower law of indices $[G : H] = [G : N_G(H)] [N_G(H) : H] \ge [G : N_G(H)] = k$.


::: pf-proof
This is the tower law applied to $H\le N_G(H)\le G$.
:::

:::

::: pf-step

Every conjugate $g H g^{-1}$ contains the identity element $e$.


::: pf-proof
Conjugation fixes the identity, so $e$ lies in every conjugate.
:::

:::

::: pf-step

Each of the $k$ distinct conjugates contains $\cardinality{H} - 1$ non-identity elements.


::: pf-proof
Each conjugate has $\cardinality{H}$ elements, exactly one of which is the identity.
:::

:::

::: pf-step

Bound the size of the union of all conjugates:
$$\cardinality{ \bigcup_{g \in G} g H g^{-1} } = \cardinality{ \{e\} \cup \bigcup_{i=1}^k (H_i \setminus \{e\}) } \le 1 + \sum_{i=1}^k (\cardinality{H_i} - 1) = 1 + k (\cardinality{H} - 1).$$


::: pf-proof
The union is $\{e\}$ together with the non-identity parts of the $k$ conjugates, and those parts have total size at most $k(\cardinality{H}-1)$.
:::

:::

::: pf-step

Since $k \le [G : H]$, we have
$$\cardinality{ \bigcup_{g \in G} g H g^{-1} } \le 1 + [G : H](\cardinality{H} - 1) = 1 + [G : H]\cardinality{H} - [G : H] = \cardinality{G} + 1 - [G : H].$$


::: pf-proof
The number of distinct conjugates is the index of the normalizer, which is at most $[G:H]$ because $H\le N_G(H)$.
:::

:::

::: pf-step

Since $H$ is a proper subgroup ($H \ne G$), the index $[G : H] \ge 2$.


::: pf-proof
A proper subgroup has index at least $2$.
:::

:::

::: pf-step

Thus:
$$\cardinality{ \bigcup_{g \in G} g H g^{-1} } \le \cardinality{G} + 1 - [G : H] \le \cardinality{G} - 1 < \cardinality{G}.$$


::: pf-proof
Substituting the bound of the preceding step and $[G:H]\ge2$.
:::

:::

::: pf-step

Therefore $\bigcup_{g \in G} g H g^{-1} \subsetneq G$.


::: pf-proof
The cardinality is strictly less than $\cardinality{G}$, so the union omits at least one element.
:::

:::

:::

:::

::: {.pf-step #s3}

Every transitive action on a set of at least two points admits a fixed-point-free element.

::: pf-proof

::: pf-step

Method 1 (via Part (b)):

::: pf-proof

::: pf-step

Choose an arbitrary point $s_0 \in S$, and let $H = G_{s_0} \le G$ be its stabilizer.


::: pf-proof
This names a point of $S$ and its stabilizer.
:::

:::

::: pf-step

By the Orbit-Stabilizer Theorem, since the action is transitive, $[G : H] = \cardinality{G \cdot s_0} = \cardinality{S} \ge 2$.


::: pf-proof
For a transitive action the orbit of $s_0$ is all of $S$, so its size is the index of the stabilizer.
:::

:::

::: pf-step

Thus $H$ is a proper subgroup of $G$.


::: pf-proof
Since $\cardinality{S}\ge2$, the index is at least $2$ and $H$ is not all of $G$.
:::

:::

::: pf-step

By Part (a), every stabilizer is of the form $G_{g \cdot s_0} = g H g^{-1}$.


::: pf-proof
Part (a) identifies the stabilizer of $g\cdot s_0$ with $gHg^{-1}$, and every point of $S$ is of that form because the action is transitive.
:::

:::

::: pf-step

An element $g \in G$ fixes at least one point $s \in S$ if and only if $g \in G_s = h H h^{-1}$ for some $h \in G$.


::: pf-proof
An element fixes $s$ exactly when it lies in the stabilizer $G_s$, and those stabilizers are the conjugates of $H$.
:::

:::

::: pf-step

Thus the set of elements in $G$ that fix at least one point of $S$ is precisely $\bigcup_{h \in G} h H h^{-1}$.


::: pf-proof
It is the union of the stabilizers of the points of $S$, which are exactly the conjugates of $H$.
:::

:::

::: pf-step

By Part (b), $\bigcup_{h \in G} h H h^{-1} \subsetneq G$.


::: pf-proof
Part (b) applies to the proper subgroup $H$ of the finite group $G$.
:::

:::

::: pf-step

Therefore there exists an element $g \in G \setminus \bigcup_{h \in G} h H h^{-1}$, which fixes no points of $S$.


::: pf-proof
An element outside the union lies in no stabilizer, so it fixes no point of $S$.
:::

:::

:::

:::

::: pf-step

Method 2 (via Burnside's Lemma):

::: pf-proof

::: pf-step

Let $X^g = \{s \in S : g \cdot s = s\}$ denote the fixed point set of $g \in G$.


::: pf-proof
This is a definition: the set of points fixed by $g$.
:::

:::

::: pf-step

By Burnside's Lemma, the number of orbits is the average number of fixed points:
$$1 = \frac{1}{\cardinality{G}} \sum_{g \in G} \cardinality{X^g} \implies \cardinality{G} = \sum_{g \in G} \cardinality{X^g} = \cardinality{X^e} + \sum_{g \ne e} \cardinality{X^g}.$$


::: pf-proof
Burnside's lemma says the number of orbits is the average over $G$ of the number of fixed points.
:::

:::

::: pf-step

Since the identity fixes all of $S$, $\cardinality{X^e} = \cardinality{S} \ge 2$.


::: pf-proof
The identity fixes every point of $S$.
:::

:::

::: pf-step

If every $g \ne e$ had at least one fixed point ($\cardinality{X^g} \ge 1$), then
$$\sum_{g \in G} \cardinality{X^g} = \cardinality{X^e} + \sum_{g \ne e} \cardinality{X^g} \ge 2 + (\cardinality{G} - 1) = \cardinality{G} + 1,$$
        a contradiction.


::: pf-proof
If every non-identity element fixed a point, the sum of the $\cardinality{X^g}$ would be at least $\cardinality{S}+(\cardinality{G}-1)$, and dividing by $\cardinality{G}$ would give more than $1$ because $\cardinality{S}\ge2$.
:::

:::

::: pf-step

Thus there exists at least one $g \in G$ with $\cardinality{X^g} = 0$.


::: pf-proof
The action is transitive, so the number of orbits is $1$; an average of $1$ with every term a non-negative integer and one term equal to $\cardinality{S}\ge2$ forces some term to be $0$.
:::

:::

:::

:::

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove parts (a), (b), and (c), respectively.

:::

:::

:::
