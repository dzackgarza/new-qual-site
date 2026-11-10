---
schema: qual/card@1
id: E-0NSGA
kind: problem
title: Products of compact sets in topological groups
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Topological Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 13, printed p. 172, with Lemma 26.4,
    Exercise 26.5, Exercise 26.9 (the tube lemma), Exercise 26.12, TG.4 and TG.7(b); the
    three parts are stored as printed and each is answered.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.13, PDF p. 15. All three parts are theirs: (a)
    A.B is closed for A closed and B compact, the compact set c B^{-1} being separated from
    A and the tube lemma producing a neighbourhood of c, whose construction the card writes
    out; (b) p is closed, since the preimage of p(A) is A.H, closed by (a) with H compact;
    (c) p is perfect — closed by (b), with fibres xH homeomorphic to H — so Exercise 26.12
    makes G compact when G/H is. An earlier note on this card wrongly reported (b) and (c)
    as answering other questions; that report is withdrawn: the set's (b) and (c) are the
    printed ones, and only its sentence for (a) needed expanding. (tmp/sources/munkres-
    solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $G$ be a topological group.

(a) Let $A$ and $B$ be subspaces of $G$.
If $A$ is closed and $B$ is compact, show $A \cdot B$ is closed.
[Hint: If $c$ is not in $A \cdot B$, find a neighborhood $W$ of $c$ such that $W \cdot B^{-1}$ is disjoint from $A$.]

(b) Let $H$ be a subgroup of $G$; let $p: G \to G/H$ be the quotient map.
If $H$ is compact, show that $p$ is a closed map.

(c) Let $H$ be a compact subgroup of $G$.
Show that if $G/H$ is compact, then $G$ is compact.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.13, PDF p. 15** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all three parts are theirs. Their argument in (a) is compressed into one sentence, so the neighbourhood is constructed explicitly below; (b) and (c) are transcribed as they stand.

Let $G$ be a topological group with identity $e$, $H$ a compact subgroup, $p:G\to G/H$ the quotient map.

(a) *If $A$ is closed and $B$ compact then $A\cdot B$ is closed.* Let $c\notin A\cdot B$. The set $c\cdot B^{-1}=\{cb^{-1}\mid b\in B\}$ is compact, being a homeomorphic image of $B$, and it is disjoint from $A$: $cb^{-1}=a$ would give $c=ab\in A\cdot B$. A topological group is Hausdorff (Supplementary Exercise TG.7(b)), so Exercise 26.5 gives disjoint open sets $U\supset A$ and $V\supset c\cdot B^{-1}$.

The set $\Omega=\{(g,b)\mid gb^{-1}\in V\}$ is open in $G\times G$ — it is the preimage of $V$ under the continuous map $(g,b)\mapsto gb^{-1}$ — and it contains $\{c\}\times B$. Since $B$ is compact, the tube lemma gives a neighbourhood $W$ of $c$ with $W\times B\subset\Omega$, that is $W\cdot B^{-1}\subset V$. Then $W\cap A\cdot B=\varnothing$: a point $w=ab$ would satisfy $wb^{-1}=a\in A$ and $wb^{-1}\in V$, contradicting $U\cap V=\varnothing$. So $A\cdot B$ is closed.

(b) *If $H$ is compact then $p$ is closed.* Let $A\subset G$ be closed. By (a), with $B=H$ compact, the set $A\cdot H$ is closed. And
$$
p^{-1}\big(p(A)\big)=\{g\mid gH=xH \text{ for some } x\in A\}=\{g\mid g\in A\cdot H\}=A\cdot H,
$$
because $gH=xH$ with $x\in A$ means $g=xh$ for some $h\in H$, and conversely. Since $p$ is a quotient map and $p^{-1}(p(A))$ is closed, $p(A)$ is closed. So $p$ is a closed map.

(c) *If $H$ is compact and $G/H$ is compact then $G$ is compact.* By (b) $p$ is closed; it is continuous and surjective, and each fibre $p^{-1}(\{xH\})=xH$ is compact, being a homeomorphic image of $H$ (Supplementary Exercise TG.4). So $p$ is a perfect map, and Exercise 26.12 applied with $Y=G/H$ compact gives that $G$ is compact.
:::
