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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.2, printed pp. 2--5** (`tmp/sources/munkres-solutions-whitman.pdf`), which decides each of the seventeen parts and, where a double implication fails, gives the direction that holds and an example killing the other. The answers below are his, with the counterexamples written out.

(a) False as an equivalence.
The forward implication holds:
$$
A\subset B\text{ and }A\subset C\Longrightarrow A\subset B\cup C.
$$
The converse fails, for example with $A=\{1\}$, $B=\{1\}$, $C=\varnothing$.

(b) False as an equivalence.
The forward implication holds.
The converse fails for
$$
A=\{1,2\},\qquad B=\{1\},\qquad C=\{2\}.
$$

(c) True:
$$
A\subset B\text{ and }A\subset C\iff A\subset B\cap C.
$$

(d) False.
If $A\subset B\cap C$, then in fact $A\subset B$ and $A\subset C$, so the right-to-left implication holds.
The other implication fails, e.g. $A=B=\{1\}$, $C=\varnothing$.

(e) False.
In fact
$$
A-(A-B)=A\cap B\subset B,
$$
and the reverse inclusion need not hold.

(f) False.
Since $B-A$ is disjoint from $A$,
$$
A-(B-A)=A\supset A-B,
$$
and equality need not hold.

(g) True:
$$
A\cap(B-C)=A\cap B\cap C^c=(A\cap B)-(A\cap C).
$$

(h) False.
One always has
$$
A\cup(B-C)\supset (A\cup B)-(A\cup C),
$$
since the right-hand side is $B\cap A^c\cap C^c$. Equality fails whenever $A\ne\varnothing$.

(i) True, since $A\cap B$ and $A-B$ partition $A$:
$$
(A\cap B)\cup(A-B)=A.
$$

(j) True.
If $(a,b)\in A\times B$, then $a\in A\subset C$ and $b\in B\subset D$, hence $(a,b)\in C\times D$.

(k) False.
For example, if $A=\varnothing$, then $A\times B=\varnothing\subset C\times D$ regardless of whether $B\subset D$.

(l) True.
Suppose $A,B\ne\varnothing$ and $A\times B\subset C\times D$. Fix $b_0\in B$. For every $a\in A$,
$$
(a,b_0)\in C\times D,
$$
so $a\in C$, hence $A\subset C$. Similarly, fixing $a_0\in A$ gives $B\subset D$.

(m) False.
Always
$$
(A\times B)\cup(C\times D)\subset (A\cup C)\times(B\cup D),
$$
and the right-hand side also contains $A\times D$ and $C\times B$, which need not lie in the left-hand side. For example take $A=D=\{1\}$ and $B=C=\varnothing$.

(n) True:
$$
(A\times B)\cap(C\times D)=(A\cap C)\times(B\cap D).
$$

(o) True:
$$
A\times(B-C)=(A\times B)-(A\times C).
$$

(p) True.
First
$$
(A\times C)-(B\times C)=(A-B)\times C.
$$
Subtracting $A\times D$ then gives
$$
((A-B)\times C)-(A\times D)=(A-B)\times(C-D).
$$

(q) False.
One always has
$$
(A-C)\times(B-D)\subset (A\times B)-(C\times D),
$$
since $x\in A-C$ and $y\in B-D$ give $x\in A$, $y\in B$, $x\notin C$, and therefore $(x,y)\notin C\times D$.
Equality need not hold: with
$$
A=\{1,2\},\quad B=\{a,b\},\quad C=\{2,3\},\quad D=\{b,c\}
$$
one computes
$$
(A\times B)-(C\times D)=\{(1,a),(1,b),(2,a)\},
\qquad
(A-C)\times(B-D)=\{(1,a)\},
$$
so $(1,b)$ lies on the left and not on the right.
More generally $(A\times B)-(C\times D)$ contains $(A-C)\times(B\cap D)$, which is disjoint from $(A-C)\times(B-D)$ whenever $B\cap D\ne(B-D)$.
:::
