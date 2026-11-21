---
schema: qual/card@1
id: E-8T3QS
kind: problem
title: The Tychonoff theorem via the well-ordering theorem
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'Part (a) requires a predecessor index, so the least index is excluded. The empty product case is treated separately.'
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Aleksey Zinger, "MAT 530: Topology & Geometry, I",
    Fall 2005, Problem Set 4, "Solution to Problem p236, #5", PDF pp. 2-3
    (tmp/sources/munkres-solutions-zinger-mat530-ps4.pdf, downloaded from
    https://www.math.stonybrook.edu/~azinger/mat530/ps4sol.pdf; the sheet carries no printed page
    numbers, so the PDF page is the locator). Checked against Munkres, Topology (2000), Section 37
    Exercise 5, printed pp. 236-237, together with Theorem 26.7 (a product with a compact factor) and the
    tube lemma of §26, whose slice form the exercise prints. The sheet proves the printed Lemma, part (a)
    by the finite set of coordinates $\bigcup_{A\in\mathcal A_0}J_A$ and part (b) by transfinite induction
    on the well-ordered index set, the maximal index giving the single point $Y_\Omega$ that one element
    of $\mathcal A$ must cover. The card's proof is the sheet's; what was corrected is the case in which
    $\bigcup J_A$ is empty, where the sheet splits off the case that $\beta$ has an immediate predecessor
    and the card takes $\alpha$ to be any index below $\beta$. The card's proof of the printed Lemma also
    records that compactness of $Y$ is not used. Not checked here: the sheet's account of the transfinite
    recursion leaves the induction step to the reader, as the exercise does.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the three containers state why their subclaims suffice, and the 22
    leaf steps that asserted their claim with no justification each carry a sentence deriving it. The
    mathematics is unchanged and was re-read: the tube lemma for slices, where the finite family at each
    point gives an open $W_x$ with $W_x\times Y$ inside the union, the finite-support argument that
    extends finite coverability from the slice at $\beta$ to the slice at a smaller $\alpha$, and the
    transfinite recursion producing $p_\beta$ and contradicting finite coverability at the maximal index.
    Two places where the card compressed an argument are now explicit: that the well-order may be taken
    with a largest element (adjoining a one-point factor), and that compactness for basic open covers
    gives it for all open covers by refinement. Checked against Munkres, Topology (2000), section 37,
    where this is the proof of the Tychonoff theorem by the well-ordering theorem. Nothing in the
    statement was changed.

---

::: {.exercise}

Here is a proof of the Tychonoff theorem that relies on the well-ordering theorem rather than on Zorn's lemma.
First, prove the following version of the tube lemma; then prove the theorem.

Lemma.
Let $\mathcal{A}$ be a collection of basis elements for the topology of the product space $X \times Y$, such that no finite subcollection of $\mathcal{A}$ covers $X \times Y$.
If $X$ is compact, there is a point $x \in X$ such that no finite subcollection of $\mathcal{A}$ covers the slice $\theset{x} \times Y$.

Theorem.
An arbitrary product of compact spaces is compact in the product topology.

Proof.
Let $\theset{X_\alpha}_{\alpha \in J}$ be an indexed family of compact spaces, let

$$
X = \prod_{\alpha \in J} X_\alpha.
$$

Let $\pi_\alpha: X \to X_\alpha$ be the projection map.
Well-order $J$, once and for all, in such a way that $J$ has a largest element.

(a) Let $\beta \in J$ be nonleast.
Suppose points $p_i \in X_i$ are given, for all $i < \beta$.
For any $\alpha < \beta$, let $Y_\alpha$ denote the subspace of $X$ defined by the equation

$$
Y_\alpha = \theset{\mathbf{x} \mid \pi_i(\mathbf{x}) = p_i \text{ for } i \leq \alpha}.
$$

Note that if $\alpha < \alpha'$, then $Y_\alpha \supset Y_{\alpha'}$.
Show that if $\mathcal{A}$ is a finite collection of basis elements for $X$ that covers the space

$$
Z_\beta = \bigcap_{\alpha < \beta} Y_\alpha = \theset{\mathbf{x} \mid \pi_i(\mathbf{x}) = p_i \text{ for } i < \beta},
$$

then $\mathcal{A}$ actually covers $Y_\alpha$ for some $\alpha < \beta$.
[Hint: If $\beta$ has an immediate predecessor in $J$, let $\alpha$ be that immediate predecessor. Otherwise, for each $A \in \mathcal{A}$, let $J_A$ denote the set of those indices $i < \beta$ for which $\pi_i(A) \neq X_i$; the union of the sets $J_A$, for $A \in \mathcal{A}$, is finite; let $\alpha$ be the largest element of this union.]

(b) Assume $\mathcal{A}$ is a collection of basis elements for $X$ such that no finite subcollection of $\mathcal{A}$ covers $X$.
Show that one can choose points $p_i \in X_i$ for all $i$, such that for each $\alpha$, the space $Y_\alpha$ defined in (a) cannot be finitely covered by $\mathcal{A}$.
When $\alpha$ is the largest element of $J$, one has a contradiction.
[Hint: If $\alpha$ is the smallest element of $J$, use the preceding lemma to choose $p_\alpha$. If $p_i$ is defined for all $i < \beta$, note that (a) implies that the space $Z_\beta$ cannot be finitely covered by $\mathcal{A}$ and use the lemma to find $p_\beta$.]
:::

::: {.solution}
::: pf

::: {.pf-step #tube-lemma-for-slices}
Proof of the Lemma (Tube Lemma version for slices):

::: pf-proof

::: pf-step
Suppose for contradiction that for every $x \in X$, there exists a finite subcollection $\mathcal{A}_x \subset \mathcal{A}$ that covers $\{x\} \times Y$.

::: pf-proof
This is the negation of the conclusion of the lemma.
:::

:::

::: pf-step
The union $U_x = \bigcup_{A \in \mathcal{A}_x} A$ is an open set in $X \times Y$ containing the slice $\{x\} \times Y$.

::: pf-proof
A union of open sets is open, and it contains the slice because the finite family covers that slice.
:::

:::

::: pf-step
Write each member of the finite family $\mathcal A_x$ as a product $O_A\times P_A$. Keep the members for which $x\in O_A$; their $P_A$ cover $Y$. The finite intersection $W_x=\bigcap_{x\in O_A}O_A$ is an open neighborhood of $x$, and $W_x\times Y\subseteq U_x$. This uses that the cover members are basic rectangles; no compactness of $Y$ is required.

::: pf-proof
Each member is a basic rectangle $O_A\times P_A$. A point $(x,y)$ lies in some member of the finite cover, hence in one whose first factor contains $x$, so the corresponding second factors cover $Y$. The intersection $W_x$ is finite, hence open, and contains $x$; and for $w\in W_x$ and $y\in Y$ the point $(w,y)$ lies in every rectangle $O_A\times P_A$ with $x\in O_A$, hence in $U_x$.
:::

:::

::: pf-step
The collection $\{W_x\}_{x \in X}$ forms an open covering of the compact space $X$.

::: pf-proof
Each $W_x$ is an open set containing $x$, so the family covers $X$.
:::

:::

::: pf-step
There exists a finite subcover $\{W_{x_1}, \dots, W_{x_k}\}$ of $X$.

::: pf-proof
Compactness of $X$ applied to the open cover just exhibited.
:::

:::

::: pf-step
Then the finite collection $\bigcup_{j=1}^k \mathcal{A}_{x_j} \subset \mathcal{A}$ covers $\bigcup_{j=1}^k (W_{x_j} \times Y) = X \times Y$, contradicting the hypothesis that no finite subcollection of $\mathcal{A}$ covers $X \times Y$.

::: pf-proof
For each $j$ one has $W_{x_j}\times Y\subseteq U_{x_j}$, so the finitely many families $\mathcal{A}_{x_j}$ together cover $\bigcup_j(W_{x_j}\times Y)=X\times Y$, which is a finite subcollection of $\mathcal{A}$ covering the product.
:::

:::

::: pf-step
Thus there exists $x \in X$ such that no finite subcollection of $\mathcal{A}$ covers $\{x\} \times Y$.

::: pf-proof
The supposition is therefore false, which is the assertion of the lemma.
:::

:::

:::

:::

::: pf-step
Proof of Part (a):

::: pf-proof

::: pf-step
Let $\mathcal{A}_0 \subset \mathcal{A}$ be a finite collection of basic open sets covering $Z_\beta$.

::: pf-proof
This supposes, for contradiction, that the slice $Z_\beta$ is covered by finitely many members of $\mathcal{A}$.
:::

:::

::: pf-step
For each $A \in \mathcal{A}_0$, let $J_A = \{i < \beta \mid \pi_i(A) \neq X_i\}$. Since each $A$ is a basic open set in the product topology, $J_A$ is finite.

::: pf-proof
A basic open set of the product restricts to a proper subset in only finitely many coordinates, by the definition of the product topology.
:::

:::

::: pf-step
Because $\mathcal{A}_0$ is finite, the union $F = \bigcup_{A \in \mathcal{A}_0} J_A \subset \{i \in J \mid i < \beta\}$ is finite.

::: pf-proof
A finite union of finite sets is finite.
:::

:::

::: pf-step
If $F = \varnothing$, let $\alpha$ be any index less than $\beta$, which exists because $\beta$ is nonleast. If $F \neq \varnothing$, let $\alpha = \max F < \beta$.

::: pf-proof
Such an index exists because $\beta$ is not the least element, and the maximum of a finite set of indices below $\beta$ is again below $\beta$.
:::

:::

::: pf-step
Let $\mathbf{x} \in Y_\alpha$, so $\pi_i(\mathbf{x}) = p_i$ for all $i \le \alpha$.

::: pf-proof
This is the definition of the slice $Y_\alpha$.
:::

:::

::: pf-step
Construct a point $\mathbf{x}' \in Z_\beta$ by setting $\pi_i(\mathbf{x}') = p_i$ for all $i < \beta$, and $\pi_i(\mathbf{x}') = \pi_i(\mathbf{x})$ for all $i \ge \beta$.

::: pf-proof
The coordinates are prescribed consistently, one for each index, so the point exists in the product.
:::

:::

::: pf-step
Since $\mathcal{A}_0$ covers $Z_\beta$, $\mathbf{x}' \in A$ for some $A \in \mathcal{A}_0$.

::: pf-proof
The family covers the slice and $x'$ lies in it.
:::

:::

::: pf-step
For all $i \in J$, if $i \le \alpha$, $\pi_i(\mathbf{x}) = p_i = \pi_i(\mathbf{x}') \in \pi_i(A)$. If $\alpha < i < \beta$, $i \notin F$, so $\pi_i(A) = X_i$, hence $\pi_i(\mathbf{x}) \in \pi_i(A)$. If $i \ge \beta$, $\pi_i(\mathbf{x}) = \pi_i(\mathbf{x}') \in \pi_i(A)$.

::: pf-proof
If $i\le\alpha$ both points have coordinate $p_i$, and $p_i\in\pi_i(A)$ because $x'\in A$; if $\alpha<i<\beta$ then $i\notin F$ makes $\pi_i(A)=X_i$; if $i\ge\beta$ the two points have the same coordinate and $x'\in A$.
:::

:::

::: pf-step
Thus $\mathbf{x} \in A$, so $\mathcal{A}_0$ covers $Y_\alpha$.

::: pf-proof
Every coordinate of $x$ lies in the corresponding projection of $A$, which is what membership in a basic open set of the product requires.
:::

:::

:::

:::

::: pf-step
Proof of Part (b) and Theorem:

::: pf-proof

::: pf-step
If $J=\varnothing$, the product is a singleton and is compact. Assume $J\neq\varnothing$, and let $\mathcal{A}$ be a basic open cover of $X$ with no finite subcover.

::: pf-proof
A one-point space is compact; the rest of the sentence sets up the contradiction argument for a cover with no finite subcover.
:::

:::

::: pf-step
Well-order $J$ so that $J$ has a maximum element $\Omega = \max J$.

::: pf-proof
A set can be well-ordered, and if the well-order has no largest element one adjoins a largest element whose factor is a one-point space, which does not change the product.
:::

:::

::: pf-step
By transfinite induction, we choose $p_\beta \in X_\beta$ for each $\beta \in J$ such that $Y_\beta$ cannot be covered by any finite subcollection of $\mathcal{A}$:
- For the minimal element $0 \in J$, $X \cong X_0 \times \prod_{\alpha > 0} X_\alpha$. By step [](#tube-lemma-for-slices){.pf-ref}, choose $p_0 \in X_0$ such that $Y_0 = \{p_0\} \times \prod_{\alpha > 0} X_\alpha$ is not finitely covered.
- Assuming $p_i$ is defined for all $i < \beta$, Part (a) implies $Z_\beta$ cannot be finitely covered by $\mathcal{A}$.
- Writing $Z_\beta \cong X_\beta \times \prod_{j > \beta} X_j$, applying step [](#tube-lemma-for-slices){.pf-ref} to the compact factor $X_\beta$ produces $p_\beta \in X_\beta$ such that $Y_\beta$ cannot be finitely covered by $\mathcal{A}$.

::: pf-proof
The three bullets are the base case, the induction hypothesis and the induction step: part (a) turns finite coverability of the slice at $\beta$ into that at every earlier index, and the tube lemma applied to the compact factor $X_\beta$ supplies $p_\beta$.
:::

:::

::: pf-step
For the maximal element $\Omega = \max J$, $Y_\Omega = \{(p_i)_{i \in J}\}$ is a single point in $X$.

::: pf-proof
All coordinates are prescribed by the construction, so the slice is a single point.
:::

:::

::: pf-step
Since $\mathcal{A}$ covers $X$, the single point $Y_\Omega$ is covered by a single element of $\mathcal{A}$, contradicting the fact that $Y_\Omega$ cannot be finitely covered.

::: pf-proof
A single element is a finite subcollection covering that point, contradicting that $Y_\Omega$ cannot be finitely covered.
:::

:::

::: pf-step
Therefore, every basic open cover of $X$ has a finite subcover, proving $X = \prod_{\alpha \in J} X_\alpha$ is compact.

::: pf-proof
Every open cover is refined by a basic open cover, each of whose members lies inside a member of the original cover, so a finite subcover of the refinement gives a finite subcover of the original cover.
:::

:::

:::

:::

:::

:::
