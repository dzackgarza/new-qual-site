---
schema: qual/card@1
id: E-8HR3A
kind: problem
title: Every basis of a second-countable space contains a countable basis
classification:
  areas:
  - topology
  topics:
  - Countability
  - Bases
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Amit Rajaraman, "Munkres Solutions" (MA 406
    course notes, last updated 31 March 2021), Exercise 4.30.2, printed p. 12
    (tmp/sources/munkres-solutions-amitrajaraman-ma406.pdf), checked against Munkres, Topology
    (2000), Section 30 Exercise 2, printed p. 194, and Lemma 13.2. Rajaraman's selection of the
    countable subcollection of C is indexed by the pairs (n, m) for which a member of C lies
    between B_n and B_m, exactly as the card writes it; no correction to the mathematics was
    needed, and the printed hint is followed literally.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the two containers state why their subsections suffice, and the 13
    leaf steps that asserted their claim with no justification each carry a sentence deriving it. The
    mathematics is unchanged: the index set $J$ of pairs of basis elements between which a member of
    $\mathcal{C}$ fits is countable, the chosen family $\mathcal{C}'$ is a subcollection of
    $\mathcal{C}$, and the three applications of the two basis properties at an arbitrary point of an
    arbitrary open set show that $\mathcal{C}'$ is a basis. Checked against Munkres, Topology (2000),
    section 30 Exercise 4, whose hint this is. Nothing in the statement was changed.

---

::: {.exercise}

Show that if $X$ has a countable basis $\theset{B_n}$, then every basis $\mathcal{C}$ for $X$ contains a countable basis for $X$.
[Hint: For every pair of indices $n, m$ for which it is possible, choose $C_{n,m} \in \mathcal{C}$ such that $B_n \subset C_{n,m} \subset B_m$.]
:::

::: {.solution}
Write $\mathcal{B} = \{B_n\}_{n \in \ZZ_+}$ for the given countable basis.

::: pf

::: pf-step
Selection of a countable subcollection $\mathcal{C}' \subseteq \mathcal{C}$:

::: pf-proof

::: pf-step
Define the index set of pairs:
$$J = \{(n, m) \in \ZZ_+ \times \ZZ_+ \mid \exists C \in \mathcal{C} \text{ such that } B_n \subseteq C \subseteq B_m\}.$$

::: pf-proof
This is a definition: the pairs of basis elements between which some member of $\mathcal{C}$ fits.
:::

:::

::: pf-step
For each pair $(n, m) \in J$, choose one basis element $C_{n, m} \in \mathcal{C}$ satisfying $B_n \subseteq C_{n, m} \subseteq B_m$.

::: pf-proof
The defining condition of $J$ says that such a member exists, and one is chosen for each pair.
:::

:::

::: pf-step
Define the subcollection:
$$\mathcal{C}' = \{C_{n, m} \mid (n, m) \in J\} \subseteq \mathcal{C}.$$

::: pf-proof
This is a definition of a subcollection of $\mathcal{C}$.
:::

:::

::: pf-step
Because $J \subseteq \ZZ_+ \times \ZZ_+$, $J$ is at most countable, and hence $\mathcal{C}'$ is a countable collection.

::: pf-proof
A subset of a countable product of countable sets is at most countable, and $\mathcal{C}'$ is the image of $J$ under the choice.
:::

:::

:::

:::

::: pf-step
Verification that $\mathcal{C}'$ is a basis for $X$:

::: pf-proof

::: pf-step
Let $U \subseteq X$ be an arbitrary open set, and let $x \in U$.

::: pf-proof
This is arbitrary data for the basis condition: an open set and a point of it.
:::

:::

::: pf-step
Since $\mathcal{B} = \{B_n\}$ is a basis and $U$ is open, there exists $m \in \ZZ_+$ such that $x \in B_m \subseteq U$.

::: pf-proof
Every open set containing a point contains a basis element that contains the point and lies inside the open set.
:::

:::

::: pf-step
Since $\mathcal{C}$ is a basis and $B_m$ is open, there exists $C \in \mathcal{C}$ such that $x \in C \subseteq B_m$.

::: pf-proof
The same property applied to the basis $\mathcal{C}$ and the open set $B_m$, which is open because it is a basis element.
:::

:::

::: pf-step
Since $\mathcal{B}$ is a basis and $C$ is open, there exists $n \in \ZZ_+$ such that $x \in B_n \subseteq C$.

::: pf-proof
The same property applied to $\mathcal{B}$ and the open set $C$.
:::

:::

::: pf-step
Thus we have $B_n \subseteq C \subseteq B_m$, which implies that the pair $(n, m)$ belongs to $J$.

::: pf-proof
The defining condition of $J$ is met, with $C$ as the witnessing member.
:::

:::

::: pf-step
By definition of $\mathcal{C}'$, there is an element $C_{n, m} \in \mathcal{C}'$ satisfying $B_n \subseteq C_{n, m} \subseteq B_m$.

::: pf-proof
The construction chose such an element for every pair in $J$.
:::

:::

::: pf-step
Consequently:
$$x \in B_n \subseteq C_{n, m} \subseteq B_m \subseteq U.$$

::: pf-proof
Chaining the containments, each of which was established in a preceding step.
:::

:::

::: pf-step
Thus $x \in C_{n, m} \subseteq U$ with $C_{n, m} \in \mathcal{C}'$.

::: pf-proof
Reading the chain from the point outwards.
:::

:::

:::

:::

::: pf-step
$\mathcal{C}'$ is a countable subset of $\mathcal{C}$ that forms a basis for the topology of $X$.

::: pf-proof
The basis condition was verified at an arbitrary point of an arbitrary open set.
:::

:::

:::

:::
