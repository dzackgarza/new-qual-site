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
Let $i_X:X\hookrightarrow\beta X$ denote the canonical embedding.

(i) Both $\beta(\mathsf l_X)$ and $\mathsf l_{\beta X}$ are continuous maps $\beta X\to\beta X$ whose restriction to the dense subspace $X$ is $i_X$. By uniqueness in the Stone--Čech extension property,
$$
\beta(\mathsf l_X)=\mathsf l_{\beta X}.
$$

(ii) Let $f:X\to Y$ and $g:Y\to Z$. The maps
$$
\beta(g\circ f),\qquad \beta(g)\circ\beta(f):\beta X\longrightarrow\beta Z
$$
are continuous. For $x\in X$,
$$
(\beta(g)\circ\beta(f))(i_X(x))
 =\beta(g)(i_Y(f(x)))
 =i_Z(g(f(x))),
$$
which is also the value of $\beta(g\circ f)$ at $i_X(x)$. Since $X$ is dense in $\beta X$ and $\beta Z$ is Hausdorff, two continuous maps $\beta X\to\beta Z$ agreeing on $X$ agree everywhere. Therefore
$$
\beta(g\circ f)=\beta(g)\circ\beta(f).
$$
Thus $\beta$ preserves identities and composition, so it is a functor.
:::
