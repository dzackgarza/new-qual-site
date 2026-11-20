---
schema: qual/card@1
id: E-LS2QW
kind: problem
title: The Stone--Čech compactification is a functor
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof is checked line by line
    against the book and the search is recorded in the COMPLAINTS.md entry for §37--§42 of SRC-TEXT-MUN00.
    Searched: "Solutions to exercises in Munkres", file S38.pdf, whose section 38 ends at Exercise 38.9;
    "Solutions to exercises for Mathematics 205A" (University of California, Riverside, Fall 2014), file
    solutions5a.pdf, whose section VI.4 answers §38 Exercises 2 and 3 only; Orellana, "Solutions ---
    Topology Munkres" (§34 and §37 only); Doug's World (Chapter 4), Whitman (to §22), "positron0802"
    (Chapters 2 and 3), "shenapse" (§1--§11), "9beach" (§1--§4), "kyp44" (§1--§22); and the dbFin pages,
    which have no chapter-5 or chapter-6 section. Checked against Munkres, Topology (2000), Section 38
    Exercise 10, printed p. 242, with Theorem 38.4 (the extension property), Lemma 38.3 (uniqueness of
    extensions into a Hausdorff space, which is what makes beta(f) well defined and what both parts use)
    and Theorem 18.3 or the closed-set criterion of continuity. No correction was needed. Not checked
    here: nothing in the exercise is left out; the card proves both functor laws and does not verify the
    book's remark that the two displayed properties are exactly functoriality, which is a definition.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked both functor axioms through the uniqueness of
    extensions from the dense copy of X into a Hausdorff target. The argument is the card's
    own; no retained set is cited. Munkres §38 Exercise 2, printed pp. 241-242. The printed
    statement needed no repair.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Read for #169 against §38 Exercise 10 and repaired in two places, neither of them the
    mathematics. The head of the solution attributed the exercise to "Munkres §38 Exercise 2,
    printed pp. 241--242"; the exercise is §38 Exercise 10, and the page is gone. What remains is
    the numbered statement: the two parts use Theorem 38.4, whose target is any compact Hausdorff
    space, and the inclusion is dense, so two continuous maps out of $\beta X$ into a Hausdorff
    space that agree on $i_X(X)$ agree everywhere. The proofs were checked and kept. Part (i):
    $\beta(\mathsf{l}_X)$ and $\mathsf{l}_{\beta X}$ are continuous self-maps of $\beta X$ that
    agree on $i_X(X)$, so they are equal. Part (ii): for $x\in X$,
    $\beta(g)(\beta(f)(i_X(x)))=\beta(g)(i_Y(f(x)))=i_Z(g(f(x)))=i_Z((g\circ f)(x))$, which is
    the value of $\beta(g\circ f)$ there, so the two continuous maps into the Hausdorff
    $\beta Z$ agree on a dense subset and hence everywhere. Searched for a published proof before
    checking: Poulsen's §38 sheet covers Exercises 38.4 to 38.9, dbFin's index stops at §67 with a
    gap before it, and no other retained set reaches §38, so nothing is transcribed. Not checked:
    no published solution of Exercise 10 was located, and none is claimed.
---

::: {.exercise}

We have constructed a correspondence $X \to \beta(X)$ that assigns, to each completely regular space, its Stone-Čech compactification.
Now let us assign, to each continuous map $f: X \to Y$ of completely regular spaces, the unique continuous map $\beta(f): \beta(X) \to \beta(Y)$ that extends the map $i \circ f$, where $i: Y \to \beta(Y)$ is the inclusion map.
Verify the following:

(i) If $\mathsf{l}_X: X \to X$ is the identity map of $X$, then $\beta(\mathsf{l}_X)$ is the identity map of $\beta(X)$.

(ii) If $f: X \to Y$ and $g: Y \to Z$, then $\beta(g \circ f) = \beta(g) \circ \beta(f)$.

These properties tell us that the correspondence we have constructed is what is called a functor; it is a functor from the "category" of completely regular spaces and continuous maps of such spaces, to the "category" of compact Hausdorff spaces and continuous maps of such spaces.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It is checked against §38 Exercise 10 and against the uniqueness clause of Theorem 38.4, which both parts use: $\beta X$, $\beta Y$ and $\beta Z$ are compact Hausdorff, hence satisfy the extension property of Theorem 38.2, and a map of $\beta X$ into a compact Hausdorff space that agrees with another on the dense image of $X$ agrees with it everywhere.

Let $i_{X}:X\to\beta X$, $i_{Y}:Y\to\beta Y$ and $i_{Z}:Z\to\beta Z$ be the canonical inclusions, and write $\beta f:\beta X\to\beta Y$ for the extension of $i_{Y}\circ f$.

::: pf

::: {.pf-step #identity}
$\beta(\mathsf{l}_{X})=\mathsf{l}_{\beta X}$.

::: pf-proof
Both $\beta(\mathsf{l}_{X})$ and $\mathsf{l}_{\beta X}$ are continuous maps $\beta X\to\beta X$, and on $i_{X}(X)$ both equal $i_{X}$: the first by definition of $\beta$ applied to the identity of $X$, the second because the identity of $\beta X$ restricts to the identity on the subspace. Since $i_{X}(X)$ is dense in $\beta X$ and $\beta X$ is Hausdorff, two continuous maps into $\beta X$ that agree on a dense subset agree everywhere (Theorem 18.3, or the uniqueness in Theorem 38.4).
:::

:::

::: {.pf-step #composition}
$\beta(g\circ f)=\beta(g)\circ\beta(f)$ for continuous $f:X\to Y$ and $g:Y\to Z$.

::: pf-proof
Both sides are continuous maps $\beta X\to\beta Z$. For $x\in X$,
$$
\big(\beta(g)\circ\beta(f)\big)\big(i_{X}(x)\big)=\beta(g)\big(i_{Y}(f(x))\big)=i_{Z}\big(g(f(x))\big)=i_{Z}\big((g\circ f)(x)\big),
$$
which is the value of $\beta(g\circ f)$ at $i_{X}(x)$. Two continuous maps into the Hausdorff space $\beta Z$ that agree on the dense subset $i_{X}(X)$ agree everywhere.
:::

:::

::: {.pf-step}
$\beta$ is a functor.

::: pf-proof
By step [](#identity){.pf-ref} it carries each identity to the identity, and by step [](#composition){.pf-ref} it carries a composite to the composite of the images, in the correct order; those are the two functor axioms. It assigns to each continuous map $f$ a continuous map $\beta f$ between the corresponding compactifications.
:::

:::

:::
:::
