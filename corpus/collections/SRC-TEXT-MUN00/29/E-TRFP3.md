---
schema: qual/card@1
id: E-TRFP3
kind: problem
title: Directed sets without antisymmetry
classification:
  areas:
  - topology
  topics:
  - Nets
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    No published set for this exercise was located. The sources searched, the pages they
    cover and the conclusion are recorded in COMPLAINTS.md under the entry for the net
    exercises of §29; the card's own proof is kept. The statement was read against Munkres,
    Topology (2000), §29 supplementary exercises on nets, printed pp. 187-188.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Transcribed from dbFin, "Supplementary Exercises*: Nets: Problem 12 Solution",
    https://dbfin.com/topology/munkres/chapter-3/supplementary-exercises-nets/problem-12-solution/,
    read 2026-11-15, text at tmp/sources/dbfin/supplementary-exercises-nets/problem-12.md, which
    answers the exercise by passing to the classes of mutually comparable indices, a partially
    ordered directed set, and checking the earlier exercises one by one. The card keeps that shape;
    its version of the passage to classes proves well-definedness, monotonicity and cofinality of
    the choice map, where dbFin calls them straightforward, and its check of Exercise 2 follows the
    order-theoretic statement rather than dbFin's remark about equivalent indices alone. Martin
    Sleziak's question 84994 on Math StackExchange (2011-11-23),
    https://math.stackexchange.com/questions/84994, and GEdgar's answer there record that the
    preorder form is the one used by Kelley and by Moore and Smith, and that the constructions do
    not need antisymmetry; nothing from that page is transcribed. This supersedes the 2026-11-10
    note above.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Step 2 claimed that the subnet obtained by choosing one representative per class has the same
    limits as the net, and the same accumulation points. Both claims are false, and the step now
    states the one-way transfers it can carry and exhibits the failure. Counterexample: the
    two-element set with its two points mutually comparable below one another is directed in the
    wider sense and has a single class, so a net with values 0 and 1 at the two points has the
    subnet constantly 0, which converges to 0 while the net does not, and 1 is an accumulation
    point of the net but not of that subnet. The reduction to the partially ordered case that step
    3 rested on is therefore unavailable, and Exercise 9 is now proved directly on the preordered
    index set of its hint, whose upper bound argument uses reflexivity, transitivity and upper
    bounds of two indices alone; Exercise 10 needs no reduction either, and Exercise 11 runs on
    the partially ordered index sets its proof builds. Step 3 also cited Theorem 26.6 for the finite
    intersection property characterization of compactness, which is Theorem 26.9; the citation is
    corrected.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    The steps are reordered so that nothing is used before it is proved, as a reader of this card
    reported and as a re-reading of the proof confirmed. The lemma of Exercise 9, proved directly on
    the index set of its hint, was inside the step that checks the exercises, and the step before it
    derived the one-way transfer of accumulation points through a subnet from the lemma in its
    partially ordered form; the lemma is now the first step, and the two places that use it refer to
    it. The last step, which said only that the preceding exercises remain correct and cited the
    first two steps, is deleted: after the 2026-11-15 correction above no exercise is settled through
    the passage to the classes of indices, so that citation was stale, and the goal of the proof is
    the step that checks the exercises, which the proof renderer marks as the QED. The mathematics of
    the steps is unchanged by the reordering; what changed is which of them comes first and what the
    last one says.
---

::: {.exercise}

Check that the preceding exercises remain correct if condition (2) is omitted from the definition of directed set.
Many mathematicians use the term "directed set" in this more general sense.
:::

::: {.solution}

Call a directed set in the wider sense a set $J$ with a relation $\preceq$ that is reflexive and transitive, such that each pair of elements has an upper bound in $J$; condition (2), antisymmetry, is not required.

::: pf

::: {.pf-step #s1}
The lemma of Exercise 9 holds for a net indexed by a set directed in the wider sense: $x$ is an accumulation point of the net if and only if some subnet converges to $x$.

::: pf-proof
Let $K$ be the set of pairs $(\alpha, U)$ with $\alpha \in J$, $U$ a neighborhood of $x$ and $x_\alpha \in U$, ordered by $(\alpha, U) \preceq (\beta, V)$ when $\alpha \preceq \beta$ and $V \subset U$. This relation is reflexive and transitive, and not antisymmetric here. Given $(\alpha_1, U_1)$ and $(\alpha_2, U_2)$ in $K$, choose $\delta \in J$ with $\alpha_1 \preceq \delta$ and $\alpha_2 \preceq \delta$; the set $U_1 \cap U_2$ is a neighborhood of $x$, and since $x$ is an accumulation point some $\alpha \succeq \delta$ has $x_\alpha \in U_1 \cap U_2$, so that $(\alpha, U_1 \cap U_2)$ lies in $K$ and dominates both. Nothing in this uses antisymmetry: the two indices are compared, their upper bound is taken, and a third element above it is chosen. The projection $g(\alpha, U) = \alpha$ is order preserving, and its image is cofinal in $J$; the subnet it defines converges to $x$; and the converse direction, that a subnet converging to $x$ puts the net frequently in each neighborhood of $x$, uses order preservation, cofinality and upper bounds of two indices in the subnet's index set.
:::

:::

::: {.pf-step #s2}
If $J$ is directed in the wider sense, then $\alpha \sim \beta$ defined by $\alpha \preceq \beta$ and $\beta \preceq \alpha$ is an equivalence relation, and the classes form a directed set $\bar{J}$ under $[\alpha] \preceq [\beta]$ if and only if $\alpha \preceq \beta$.

::: pf-proof
Reflexivity and symmetry are immediate, and transitivity follows from transitivity of $\preceq$. If $\alpha \sim \alpha'$ and $\beta \sim \beta'$, then $\alpha' \preceq \alpha \preceq \beta \preceq \beta'$ shows $\alpha \preceq \beta$ implies $\alpha' \preceq \beta'$, and the converse holds by symmetry, so the relation on classes is well defined. It is reflexive and transitive because $\preceq$ is, and $[\alpha] \preceq [\beta]$ with $[\beta] \preceq [\alpha]$ says $\alpha \sim \beta$, that is $[\alpha] = [\beta]$, so it is a partial order. An upper bound of $\alpha, \beta$ in $J$ is one for $[\alpha], [\beta]$ in $\bar J$, so $\bar J$ is directed.
:::

:::

::: {.pf-step #s3}
Choosing one representative per class gives a subnet indexed by the partially ordered set $\bar J$; every limit of the net is a limit of that subnet, and every accumulation point of that subnet is an accumulation point of the net. Neither converse holds.

::: pf-proof
Choose $f([\alpha]) \in [\alpha]$ for each class. If $[\alpha] \preceq [\beta]$, then $f([\alpha]) \sim \alpha \preceq \beta \sim f([\beta])$, so $f$ is order preserving, and $f(\bar J)$ is cofinal in $J$ because $\alpha \preceq f([\alpha])$. Hence $(x_{f([\alpha])})_{[\alpha] \in \bar J}$ is a subnet of $(x_\alpha)_{\alpha \in J}$ in the sense of the preceding exercise, and that exercise gives that it converges to every limit of $(x_\alpha)$. A subnet of this subnet is again a subnet of $(x_\alpha)_{\alpha \in J}$, a composite of two order preserving maps with cofinal image being order preserving with cofinal image, so if $y$ is an accumulation point of the subnet on $\bar J$, the lemma of [step 1](#s1) applied to the net on $\bar J$ supplies a subnet of the subnet converging to $y$, and that is a subnet of $(x_\alpha)$ converging to $y$; so $y$ is an accumulation point of $(x_\alpha)$.

The two converses fail, and the failure is the reason the wider setting cannot be settled by this passage alone. Let $J = \{a, b\}$ carry the preorder with $a \preceq b$ and $b \preceq a$, a directed set in the wider sense whose classes are the single class $[a] = [b]$, and let $x_a = p$ and $x_b = q$ be two distinct points of $\RR$, say $p = 0$ and $q = 1$. Then $f([a]) = a$ and the subnet on $\bar J$ is constantly $p = 0$, so it converges to $0$; but the net does not converge to $0$, since $x_b = 1$ lies outside the neighborhood $(-1, 1)$ of $0$. And $q = 1$ is an accumulation point of the net, because $\{b\}$ is cofinal in $J$ and $x_b = 1$ lies in every neighborhood of $1$; while $1$ is not an accumulation point of the subnet, whose values are all $0$, a neighborhood of $1$ disjoint from $0$ containing none of them. So limits pass from the net to the subnet, and accumulation points pass from the subnet to the net; a limit of the subnet and an accumulation point of the net carry over to nothing.
:::

:::

::: {.pf-step #s4}
Exercises 1 to 11 remain correct in the wider sense.

::: pf-proof
Exercise 1 asks for directed sets under a relation that is already a partial order in all four parts, so its answers are unchanged; Exercise 2 uses only that a restriction of a reflexive, transitive relation is one and that an upper bound in $J$ of two elements of the cofinal subset $K$ is dominated by an element of $K$, both of which hold without antisymmetry; Exercise 3 has $J = \ZZ_+$, whose order is a partial order. Exercises 4, 5, 6 and 7 argue only from reflexivity, transitivity and the existence of an upper bound of two indices, and the index sets they build, neighborhoods under reverse inclusion and products of two such sets, are partially ordered. Exercise 8 is a statement about all subnets of a net and its proof uses only order preservation and cofinality.

Exercise 9 is [step 1](#s1), the index set its hint builds being directed in the wider sense by the argument given there. Exercise 10 then needs no reduction for the implication from compactness. For a net indexed by a wider directed set, put $B_\alpha = \theset{x_\beta \mid \alpha \preceq \beta}$ and let $F_\alpha = \overline{B_\alpha}$. The family $\theset{F_\alpha}$ has the finite intersection property, an upper bound of finitely many indices lying in each of the corresponding $B_\alpha$; compactness gives a point $x$ of $\bigcap_\alpha F_\alpha$, and $x$ is an accumulation point of the net, since for a neighborhood $U$ of $x$ and $\alpha \in J$ the set $U$ meets $B_\alpha$ and so contains some $x_\beta$ with $\alpha \preceq \beta$. The lemma of [step 1](#s1) turns the accumulation point into a convergent subnet. For the converse, a family of closed sets with the finite intersection property is indexed by its nonempty finite subsets under inclusion, which is a partial order; the net has a convergent subnet by hypothesis, a subnet converging to $x$ makes $x$ an accumulation point of the net by [step 1](#s1), and then for a member $A$ of the family and a neighborhood $U$ of $x$ there is an index $\alpha$ above $\{A\}$ with $x_\alpha \in U$, so that $x_\alpha \in \bigcap_{B \in \alpha} B \subset A$ and $U$ meets $A$; hence $x$ lies in the closed set $A$, the family has nonempty intersection, and Theorem 26.9 gives compactness.

Exercise 11's proof also runs on partially ordered index sets. If $x$ lies in the closure of $A \cdot B$, then the neighborhoods of $x$ under reverse inclusion index a net in $A \cdot B$ converging to $x$, written $a_U b_U$ with $a_U \in A$ and $b_U \in B$; compactness of $B$ and the implication of Exercise 10 just checked pass to a subnet on which the net $(b_U)$ converges, to $b$ say, and then $(a_U)$ converges to $x b^{-1}$ by continuity of multiplication and inversion, so that $x b^{-1} \in A$ because $A$ is closed, and $x = (x b^{-1}) b \in A \cdot B$.

The passage to the classes of [step 2](#s2) and the two one-way transfers of [step 3](#s3) settle none of the exercises by themselves: the counterexample there shows that limits and accumulation points do not carry over in both directions, so each exercise is checked on the index set its own proof builds, as above.
:::

:::
:::

:::
