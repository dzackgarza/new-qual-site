---
schema: qual/card@1
id: E-MUN-1-2
kind: problem
title: Subset membership under union and intersection
classification:
  areas:
  - topology
  topics:
  - Fundamental Concepts
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §1 Exercise 2, printed p. 14: all seventeen
    parts (a)-(q) are stated as the book prints them, including (k) and (l) as "the
    converse of (j)" and (l) with the hypothesis that A and B are nonempty.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 1.2,
    printed pp. 2-5 (tmp/sources/munkres-solutions-whitman.pdf), part by part. Repaired
    the one place where the card did not answer the printed question as asked: part (q)
    asserted that (A x B) - (C x D) contains (A - C) x (B meet D) without giving sets,
    so "equality need not hold" did not follow from a counterexample; the card now
    carries Whitman's explicit sets (printed p. 5) with both sides computed.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: one step per printed part (a)-(q), each
    saying whether the double implication holds, which direction survives, and — where an
    equality fails — which inclusion survives together with the sets that kill it. The
    answers and the counterexamples are the retained solution's, unchanged; its cited pages
    were not re-read in this pass, and the printed statement was not re-read either, its
    source check being the earlier event above.
---

::: {.exercise}

Determine which of the following statements are true for all sets A, B, C, and D. If a double implication fails, determine whether one or the other of the possible implications holds.
If an equality fails, determine whether the statement becomes true if the “equals” symbol is replaced by one or the other of the inclusion symbols $\subset$ or $\supset$.

(a) $A \subset B$ and $A \subset C \Leftrightarrow A \subset (B \cup C)$ .

(b) $A \subset B$ or $A \subset C \Leftrightarrow A \subset (B \cup C)$ .

(c) $A \subset B$ and $A \subset C \Leftrightarrow A \subset (B \cap C)$ .

(d) $A \subset B$ or $A \subset C \Leftrightarrow A \subset (B \cap C)$ .

(e) $A - (A - B) = B$ .

(f) $A - (B - A) = A - B$ .

(g) $A \cap (B - C) = (A \cap B) - (A \cap C)$ .

(h) $A \cup (B - C) = (A \cup B) - (A \cup C)$ .

(i) $(A\cap B)\cup (A - B) = A.$

(j) $A \subset C$ and $B \subset D \Rightarrow (A \times B) \subset (C \times D)$ .

(k) The converse of (j).

(l) The converse of (j), assuming that $A$ and $B$ are nonempty.

(m) $(A\times B)\cup (C\times D) = (A\cup C)\times (B\cup D).$

(n) $(A\times B)\cap (C\times D) = (A\cap C)\times (B\cap D).$

(o) $A \times (B - C) = (A \times B) - (A \times C)$ .

(p) $(A - B)\times (C - D) = (A\times C - B\times C) - A\times D.$

(q) $(A\times B) - (C\times D) = (A - C)\times (B - D).$
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.2, printed pp. 2--5** (`tmp/sources/munkres-solutions-whitman.pdf`). It decides each of the seventeen parts and, where a double implication fails, gives the direction that holds and an example killing the other; the answers below are his, one step per part, with the counterexamples written out.

Throughout, $\subset$ is the book's non-strict inclusion, and a claim of the form “$P\iff Q$” is refuted by one example with $P$ true and $Q$ false, or the reverse.

::: pf

::: {.pf-step}
(a) False as a double implication: $A\subset B$ and $A\subset C$ imply $A\subset B\cup C$, but the converse fails.

::: pf-proof
The implication holds because $B\subset B\cup C$ and $C\subset B\cup C$, so any $A$ contained in both is contained in the union. The converse fails for $A=\{1\}$, $B=\{1\}$, $C=\varnothing$: here $A\subset B\cup C=\{1\}$ while $A\not\subset C$.
:::

:::

::: {.pf-step}
(b) False as a double implication: $A\subset B$ or $A\subset C$ implies $A\subset B\cup C$, but the converse fails.

::: pf-proof
The implication holds since either hypothesis already puts $A$ inside a subset of $B\cup C$. The converse fails for $A=\{1,2\}$, $B=\{1\}$, $C=\{2\}$: the union is $A$ itself, while $A$ is contained in neither $B$ nor $C$.
:::

:::

::: {.pf-step}
(c) True: $A\subset B$ and $A\subset C$ if and only if $A\subset B\cap C$.

::: pf-proof
If $A$ lies in both $B$ and $C$ then every element of $A$ lies in the intersection. Conversely $B\cap C\subset B$ and $B\cap C\subset C$, so $A\subset B\cap C$ gives $A\subset B$ and $A\subset C$ by transitivity of inclusion.
:::

:::

::: {.pf-step}
(d) False as a double implication: $A\subset B\cap C$ implies $A\subset B$ or $A\subset C$, but not conversely.

::: pf-proof
The forward direction holds because $B\cap C$ lies in each of $B$ and $C$. The other fails for $A=B=\{1\}$, $C=\varnothing$: then $A\subset B$, while $B\cap C=\varnothing$ does not contain $A$.
:::

:::

::: {.pf-step}
(e) False: $A-(A-B)=A\cap B$, which lies in $B$ and need not equal it.

::: pf-proof
An element of $A-(A-B)$ is in $A$ and not in $A-B$, so it is in $B$; conversely an element of $A\cap B$ is in $A$ but not in $A-B$. So $A-(A-B)=A\cap B\subset B$. Equality fails for $A=\{1\}$, $B=\{1,2\}$: then $A-(A-B)=\{1\}-\varnothing=\{1\}\ne B$.
:::

:::

::: {.pf-step}
(f) False: $A-(B-A)=A$, which contains $A-B$ and need not equal it.

::: pf-proof
$B-A$ is disjoint from $A$, so removing it from $A$ changes nothing and $A-(B-A)=A$. Since $A-B\subset A$, the inclusion $A-(B-A)\supset A-B$ always holds, and equality fails for $A=\{1,2\}$, $B=\{1\}$: then $B-A=\varnothing$ and $A-(B-A)=\{1,2\}$, while $A-B=\{2\}$.
:::

:::

::: {.pf-step}
(g) True: $A\cap(B-C)=(A\cap B)-(A\cap C)$.

::: pf-proof
Both sides equal $A\cap B\cap C^{c}$, the set of points lying in $A$ and in $B$ but not in $C$: the left side by the definition of set difference, and the right side because $A\cap C$ is exactly the part of $A$ excluded.
:::

:::

::: {.pf-step}
(h) False: $A\cup(B-C)$ contains $(A\cup B)-(A\cup C)$, and the inclusion can be proper.

::: pf-proof
$(A\cup B)-(A\cup C)=(A\cup B)\cap A^{c}\cap C^{c}=B\cap A^{c}\cap C^{c}=B-(A\cup C)$, which lies in $B-C$ and hence in $A\cup(B-C)$. The inclusion is proper whenever $A\ne\varnothing$ and $B$ meets $A$: for $A=\{1\}$, $B=\{1,2\}$, $C=\{2\}$ the left side is $\{1\}\cup\{1\}=\{1\}$ and the right side is $\{1,2\}-\{1,2\}=\varnothing$.
:::

:::

::: {.pf-step}
(i) True: $(A\cap B)\cup(A-B)=A$.

::: pf-proof
$A\cap B$ and $A-B$ are disjoint subsets of $A$, and every $a\in A$ lies in exactly one of them according as $a\in B$ or $a\notin B$; so their union is $A$.
:::

:::

::: {.pf-step #j-product}
(j) True: $A\subset C$ and $B\subset D$ imply $A\times B\subset C\times D$.

::: pf-proof
If $(a,b)\in A\times B$ then $a\in A\subset C$ and $b\in B\subset D$, so $(a,b)\in C\times D$.
:::

:::

::: {.pf-step}
(k) False: the converse of (j) fails.

::: pf-proof
Take $A=\varnothing$, $C=\varnothing$, $B=\{1,2\}$ and $D=\{1\}$. Then $A\times B=\varnothing=C\times D$, so $A\times B\subset C\times D$ holds, while $B\subset D$ is false. So the converse of step [](#j-product){.pf-ref} fails when a factor is empty.
:::

:::

::: {.pf-step}
(l) True: if $A$ and $B$ are nonempty, the converse of (j) holds.

::: pf-proof
Suppose $A,B\ne\varnothing$ and $A\times B\subset C\times D$. Fix $b_{0}\in B$; for each $a\in A$ the pair $(a,b_{0})$ lies in $A\times B\subset C\times D$, so $a\in C$, and $A\subset C$. Symmetrically, fixing $a_{0}\in A$ gives $B\subset D$.
:::

:::

::: {.pf-step}
(m) False: $(A\times B)\cup(C\times D)$ lies in $(A\cup C)\times(B\cup D)$, and the inclusion can be proper.

::: pf-proof
Each of $A\times B$ and $C\times D$ lies in $(A\cup C)\times(B\cup D)$, so the union does too. The right side also contains $A\times D$ and $C\times B$, which need not lie in the union: with $A=D=\{1\}$ and $B=C=\varnothing$ the left side is $\varnothing$ and the right side is $\{1\}\times\{1\}=\{(1,1)\}$.
:::

:::

::: {.pf-step}
(n) True: $(A\times B)\cap(C\times D)=(A\cap C)\times(B\cap D)$.

::: pf-proof
A pair $(x,y)$ lies in the left side exactly when $x\in A$, $y\in B$, $x\in C$ and $y\in D$, which is exactly $x\in A\cap C$ and $y\in B\cap D$, that is $(x,y)$ in the right side.
:::

:::

::: {.pf-step #o-difference}
(o) True: $A\times(B-C)=(A\times B)-(A\times C)$.

::: pf-proof
A pair $(x,y)$ lies in $A\times(B-C)$ exactly when $x\in A$, $y\in B$ and $y\notin C$; that is exactly when $(x,y)\in A\times B$ and $(x,y)\notin A\times C$.
:::

:::

::: {.pf-step}
(p) True: $(A-B)\times(C-D)=\bigl((A\times C)-(B\times C)\bigr)-(A\times D)$.

::: pf-proof
By step [](#o-difference){.pf-ref} with the roles of the factors exchanged, $(A\times C)-(B\times C)=(A-B)\times C$. Subtracting $A\times D$ removes exactly the pairs whose second coordinate lies in $D$: a pair $(x,y)\in(A-B)\times C$ has $x\in A-B\subset A$, so it lies in $A\times D$ precisely when $y\in D$. Hence the two subtractions leave the pairs with $x\in A-B$ and $y\in C-D$, which is $(A-B)\times(C-D)$.
:::

:::

::: {.pf-step}
(q) False: $(A-C)\times(B-D)$ lies in $(A\times B)-(C\times D)$, and the inclusion can be proper.

::: pf-proof
If $x\in A-C$ and $y\in B-D$ then $x\in A$, $y\in B$, $x\notin C$, so $(x,y)\in A\times B$ and $(x,y)\notin C\times D$; hence $(A-C)\times(B-D)\subset(A\times B)-(C\times D)$. Equality fails for $A=\{1,2\}$, $B=\{a,b\}$, $C=\{2,3\}$, $D=\{b,c\}$: then $(A\times B)-(C\times D)=\{(1,a),(1,b),(2,a)\}$ while $(A-C)\times(B-D)=\{(1,a)\}$, so $(1,b)$ lies on the left and not on the right. More generally $(A\times B)-(C\times D)$ contains $(A-C)\times(B\cap D)$, which is disjoint from $(A-C)\times(B-D)$ whenever $B\cap D\ne B-D$.
:::

:::

:::
:::
