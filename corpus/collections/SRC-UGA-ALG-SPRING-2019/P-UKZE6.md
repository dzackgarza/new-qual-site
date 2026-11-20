---
schema: qual/card@1
id: P-UKZE6
kind: problem
title: Every proper ideal lies in a maximal ideal; $x\in J(R)$ iff $1+rx$ is a unit;
  $J(R)$ consists of the nilpotents when $R$ is finite
classification:
  areas:
  - algebra
  topics:
  - Jacobson Radical
  - Maximal Ideals
  - Nilpotence
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card carried no audit list; this one records the change. Thirteen steps asserted their claim with
    no justification and each now carries one: in part (a) the properness of $I$, the definition of the
    family, its non-emptiness and partial order, the chain, the union as an ideal using that a chain is
    totally ordered, its properness, the upper bound, and the step from Zorn's maximal element to a
    maximal ideal; in part (c) that a finite integral domain is a field through an injective self-map of a
    finite set, that a prime ideal of a finite ring is maximal through the field quotient, the equality of
    the two spectra, Krull's identification of the nilradical, and the substitution giving
    $J(R) = \operatorname{Nil}(R)$. Five steps had their argument inside the claim (steps 1.5, 1.6, 3.1,
    3.2 and 3.4) and now state the assertion with the argument in the proof; the claim of the last step
    was the truncated sentence "we have" with its display orphaned outside the step, so it now states
    $J(R) = \operatorname{Nil}(R)$ and the display is gone; and the closing pf-qed, whose whole content was
    that steps 1 to 3 answer parts (a) to (c), is removed so the final step carries the QED. Checked while
    writing: Zorn's maximal element is maximal in $R$, not merely among ideals containing $I$, because any
    proper ideal above it also contains $I$. Sources are cited by numbered statement: Zorn's lemma, and
    Krull's theorem for the nilradical; no page reference appears on the card or in its events. The
    statement is unchanged. The collection retains the UGA algebra qualifying exam of Spring 2019 and no
    solution sheet, so the argument is the card's own.
---
::: {.problem}
Let $R$ be a commutative ring with identity $1 \ne 0$.

(a) Show that every proper ideal of $R$ is contained in at least one maximal ideal.

(b) Let $J(R) = \bigcap_{\mathfrak{m} \in \operatorname{MaxSpec}(R)} \mathfrak{m}$ denote the Jacobson radical of $R$. Show that $x \in J(R)$ if and only if $1 + r x$ is a unit in $R$ for all $r \in R$.

(c) Suppose that $R$ is a finite ring. Show that $J(R) = \operatorname{Nil}(R)$, the set of all nilpotent elements of $R$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every proper ideal is contained in a maximal ideal.

::: pf-proof

::: pf-step

Let $I \subsetneq R$ be a proper ideal of $R$.


::: pf-proof
The hypothesis says $I$ is an ideal and $I \ne R$, which is what makes it a proper ideal; nothing further about $I$ is used, so the argument applies to every proper ideal at once.
:::

:::

::: pf-step

Define the family of proper ideals of $R$ containing $I$:
    $$\mathcal{S} = \{J \subseteq R : J \text{ is an ideal of } R, \, I \subseteq J, \text{ and } J \ne R\}.$$


::: pf-proof
The family collects the ideals of $R$ that contain $I$ and differ from $R$, so it is a subfamily of the power set of $R$ and each of its members is a proper ideal containing $I$ by definition.
:::

:::

::: pf-step

Since $I \in \mathcal{S}$, $\mathcal{S}$ is non-empty. Partially order $\mathcal{S}$ by inclusion $\subseteq$.


::: pf-proof
The ideal $I$ contains itself and is proper, so $I \in \mathcal{S}$ and the family is non-empty. Inclusion of subsets is reflexive, antisymmetric and transitive, so it is a partial order on any family of subsets, in particular on $\mathcal{S}$.
:::

:::

::: pf-step

Let $\mathcal{C} \subseteq \mathcal{S}$ be a non-empty totally ordered chain of ideals.


::: pf-proof
A chain in $\mathcal{S}$ is a subfamily totally ordered by inclusion, and it is non-empty by hypothesis; no other property of it is assumed, so whatever is proved below holds for every chain that Zorn's lemma requires.
:::

:::

::: pf-step

The union $J_0 = \bigcup_{J \in \mathcal{C}} J$ is an ideal of $R$ containing $I$.


::: pf-proof
The union $J_0$ is an ideal: given $x, y \in J_0$ choose members $J_1, J_2$ of the chain containing them, and since the chain is totally ordered one of the two contains the other, say $J_1 \subseteq J_2$; then $x, y \in J_2$ and $J_2$ an ideal give $x - y \in J_2 \subseteq J_0$ and $rx \in J_2 \subseteq J_0$ for every $r \in R$. It contains $I$ because each member does.
:::

:::

::: pf-step

$J_0$ is a proper ideal, so $J_0 \in \mathcal{S}$.


::: pf-proof
If $1 \in J_0$ then $1$ lies in some member $J'$ of the chain, and an ideal containing $1$ is all of $R$, so $J' = R$; that contradicts $J' \in \mathcal{S}$, whose members are proper. Hence $1 \notin J_0$, so $J_0 \ne R$ and $J_0$ is a proper ideal containing $I$.
:::

:::

::: pf-step

Thus $J_0$ is an upper bound for $\mathcal{C}$ in $\mathcal{S}$.


::: pf-proof
Every member of the chain is contained in its union, and the union lies in $\mathcal{S}$ by the two preceding steps, so it is an element of $\mathcal{S}$ above every member of the chain; that is what an upper bound in $\mathcal{S}$ is.
:::

:::

::: pf-step

By Zorn's Lemma, $\mathcal{S}$ contains a maximal element $\mathfrak{m}$, which is a maximal ideal of $R$ containing $I$.


::: pf-proof
Zorn's lemma applies because $\mathcal{S}$ is a non-empty partially ordered set in which every non-empty chain has an upper bound in $\mathcal{S}$, and it produces a maximal element $\mathfrak{m}$. That $\mathfrak{m}$ is a maximal ideal of $R$: it is a proper ideal containing $I$, and if $\mathfrak{m} \subsetneq J \subsetneq R$ with $J$ an ideal, then $J$ contains $I$ and is proper, so $J \in \mathcal{S}$ strictly above $\mathfrak{m}$, contradicting maximality.
:::

:::

:::

:::

::: {.pf-step #s2}

An element $x$ lies in $J(R)$ if and only if $1+rx$ is a unit for every $r\in R$.

::: pf-proof

::: pf-step

($\implies$): Assume $x \in J(R)$, so $x \in \mathfrak{m}$ for every maximal ideal $\mathfrak{m}$.

::: pf-proof

Let $r \in R$. Suppose for contradiction that $1 + r x$ is not a unit. Then the principal ideal $\langle 1 + r x \rangle$ is proper. By Part (a), $\langle 1 + r x \rangle \subseteq \mathfrak{m}_0$ for some maximal ideal $\mathfrak{m}_0$. Since $x \in J(R)$, $x \in \mathfrak{m}_0$, and hence $r x \in \mathfrak{m}_0$. Since $1 + r x \in \mathfrak{m}_0$ and $r x \in \mathfrak{m}_0$, we have $1 = (1 + r x) - r x \in \mathfrak{m}_0$, which implies $\mathfrak{m}_0 = R$, contradicting that $\mathfrak{m}_0$ is proper. Thus $1 + r x$ must be a unit.

:::

:::

::: pf-step

($\impliedby$): Assume $1 + r x \in R^\times$ for all $r \in R$.

::: pf-proof

Suppose for contradiction that $x \notin J(R)$. Then there exists a maximal ideal $\mathfrak{m}$ such that $x \notin \mathfrak{m}$. Since $\mathfrak{m}$ is maximal and $x \notin \mathfrak{m}$, the ideal $\mathfrak{m} + \langle x \rangle = R$. Thus $1 \in \mathfrak{m} + \langle x \rangle$, so there exist $m \in \mathfrak{m}$ and $s \in R$ such that $1 = m - s x$. Rearranging gives $m = 1 + s x$. By hypothesis, choosing $r = s \in R$, $1 + s x$ is a unit, so $m \in \mathfrak{m}$ is a unit. This implies $\mathfrak{m} = R$, contradicting that $\mathfrak{m}$ is a proper ideal. Thus $x \in \mathfrak{m}$ for all maximal ideals, so $x \in J(R)$.

:::

:::

:::

:::

::: {.pf-step #s3}

If $R$ is finite, then $J(R)=\operatorname{Nil}(R)$.

::: pf-proof

::: {.pf-step #s3-1}

A finite integral domain is a field.


::: pf-proof
A finite integral domain is a field: for $a \ne 0$ the map $y \mapsto ay$ is injective because $ay_1 = ay_2$ gives $a(y_1 - y_2) = 0$ and a domain has no zero divisors, and an injective self-map of a finite set is surjective, so $1 = ab$ for some $b$.
:::

:::

::: pf-step

Every prime ideal of a finite commutative ring is maximal.


::: pf-proof
For a prime ideal $\mathfrak{p}$ the quotient $R/\mathfrak{p}$ is an integral domain, and it is finite because $R$ is; by the previous step it is a field, and a commutative ring modulo an ideal is a field exactly when the ideal is maximal.
:::

:::

::: pf-step

Equality of prime and maximal spectra: Thus $\operatorname{Spec}(R) = \operatorname{MaxSpec}(R)$ for any finite commutative ring $R$.


::: pf-proof
Every maximal ideal is prime, since $R/\mathfrak{m}$ a field is an integral domain; and every prime ideal is maximal by the previous step, so over a finite ring the two families coincide.
:::

:::

::: pf-step

The nilradical is the intersection of the prime ideals, $\operatorname{Nil}(R) = \bigcap_{\mathfrak{p} \in \operatorname{Spec}(R)} \mathfrak{p}$.


::: pf-proof
Krull's theorem identifies the nilradical with the intersection of the prime ideals: an element is nilpotent exactly when it lies in every prime ideal, so the set of nilpotent elements is that intersection.
:::

:::

::: pf-step

$J(R) = \operatorname{Nil}(R)$.


::: pf-proof
The Jacobson radical is the intersection over the maximal ideals and the nilradical the intersection over the prime ideals; the two families of ideals are the same by the equality just established, so the two intersections are equal.
:::

:::

:::

:::

:::
:::
