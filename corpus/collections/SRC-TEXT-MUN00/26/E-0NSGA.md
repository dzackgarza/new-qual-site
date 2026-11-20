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

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.13** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); parts (b) and (c) are transcribed from it as they stand. Its one sentence for (a) separates $A$ from $c\cdot B^{-1}$ by Exercise 26.5, which requires *both* subspaces compact, whereas $A$ is only closed; step [](#a-tube){.pf-ref} runs the book's hint instead and separates the two sets directly by the tube lemma.

Let $G$ be a topological group with identity $e$, and put $A\cdot B=\theset{a\cdot b\mid a\in A,\ b\in B}$ and $B^{-1}=\theset{b^{-1}\mid b\in B}$.

::: pf

::: {.pf-step #compact-images}
If $B\subseteq G$ is compact then $g\cdot B$ and $B^{-1}$ are compact, and $(x,y)\mapsto x\cdot y^{-1}$ is continuous; also $G$ is Hausdorff.

::: pf-proof
Multiplication $m:G\times G\to G$ and inversion $\iota:G\to G$ are continuous, so $m\circ(\mathrm{id}\times\iota)$ is continuous, which is $(x,y)\mapsto x\cdot y^{-1}$. Left translation $h\mapsto g\cdot h$ is a homeomorphism with inverse $h\mapsto g^{-1}\cdot h$, and inversion is its own inverse homeomorphism, so $g\cdot B$ and $B^{-1}$ are continuous images of the compact space $B$, hence compact (Theorem 26.5). A topological group is Hausdorff (Supplementary Exercise TG.7(b)).
:::

:::

::: {.pf-step #part-a}
(a) If $A$ is closed and $B$ is compact, then $A\cdot B$ is closed.

:::: {.pf-proof}

::: {.pf-step #a-tube}
For $c\notin A\cdot B$ there is a neighbourhood $W$ of $c$ with $W\cdot B^{-1}\cap A=\varnothing$.

::: pf-proof
Let $\Omega=\theset{(g,b)\in G\times B \mid g\cdot b^{-1}\notin A}$. It is open in $G\times B$, being the preimage of the open set $G\setminus A$ under the continuous map $(g,b)\mapsto g\cdot b^{-1}$ of step [](#compact-images){.pf-ref}, and it contains the slice $\{c\}\times B$: if $c\cdot b^{-1}\in A$ for some $b\in B$, then $c=(c\cdot b^{-1})\cdot b\in A\cdot B$, contrary to the choice of $c$. As $B$ is compact, the tube lemma (Lemma 26.8) applies to $\Omega$ in $G\times B$ and gives a neighbourhood $W$ of $c$ with $W\times B\subseteq\Omega$, that is $W\cdot B^{-1}\subseteq G\setminus A$.
:::

:::

::: {.pf-step #a-outside}
$W\cap A\cdot B=\varnothing$, so $G\setminus A\cdot B$ is open.

::: pf-proof
If $w\in W\cap A\cdot B$, write $w=a\cdot b$ with $a\in A$, $b\in B$. Then $w\cdot b^{-1}=a\in A$, while $w\in W$ gives $w\cdot b^{-1}\in W\cdot B^{-1}\subseteq G\setminus A$ by step [](#a-tube){.pf-ref}, a contradiction. Every point of the complement of $A\cdot B$ thus has a neighbourhood inside that complement.
:::

:::

::::

:::

::: {.pf-step #part-b}
(b) If $H$ is a subgroup and $p:G\to G/H$ is the quotient map, then $p$ is closed when $H$ is compact.

::: pf-proof
Let $A\subseteq G$ be closed. By step [](#part-a){.pf-ref} with $B=H$ compact, $A\cdot H$ is closed, and $p^{-1}\big(p(A)\big)=A\cdot H$: an element $g$ satisfies $gH=xH$ for some $x\in A$ exactly when $g=x\cdot h$ for some $x\in A$ and $h\in H$, since $g\in gH=xH$ and $x\in xH=gH$. A quotient map pulls closed sets back to closed sets, and $p^{-1}\big(p(A)\big)$ is closed, so $p(A)$ is closed.
:::

:::

::: {.pf-step #part-c}
(c) If $H$ is a compact subgroup and $G/H$ is compact, then $G$ is compact.

::: pf-proof
By step [](#part-b){.pf-ref} the quotient map $p$ is closed; it is continuous and surjective, and for $x\in G$ the fibre $p^{-1}\big(\{xH\}\big)=xH$ is a homeomorphic image of $H$ under left translation, hence compact (Supplementary Exercise TG.4, and step [](#compact-images){.pf-ref}). So $p$ is a perfect map, and Exercise 26.12  gives that $G$ is compact because $G/H$ is.
:::

:::

::: {.pf-qed}
Parts (a), (b) and (c) are steps [](#part-a){.pf-ref}, [](#part-b){.pf-ref} and [](#part-c){.pf-ref}.
:::

:::

:::
