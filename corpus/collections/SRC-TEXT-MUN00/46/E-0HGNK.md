---
schema: qual/card@1
id: E-0HGNK
kind: problem
title: Continuity of evaluation forces the compact-open topology
classification:
  areas:
  - topology
  topics:
  - Function Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §46 Exercise 8 (printed p. 289) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked against the definition of the compact-open
    subbasis in §46 and the Tube Lemma (Lemma 26.8), which reads: if N is an open set of X x Y containing
    the slice x_0 x Y and Y is compact, then W x Y is contained in N for some neighbourhood W of x_0. The
    card applies it with the factors interchanged, the compact set C playing the role of the compact factor
    and f_0 the role of the point: the open set N' = (C x C'(X,Y)) cap e^{-1}(U) of the space C x C'(X,Y)
    contains the slice {f_0} x C, so N' contains W x C for a neighbourhood W of f_0, that is, C x W is
    contained in e^{-1}(U); the card's text now says which role each factor plays. Then W lies
    in S(C,U) since for f in W and x in C the pair (x,f) lies in e^{-1}(U). The card's closing references to
    three step labels that no step carried are replaced by the prose sentence that closes the argument.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). The AoPS blog post by cinnamon_e, "Topology by
    Munkres Chapter 7 | Day 17" (2025-09-10,
    https://artofproblemsolving.com/community/c3401823h3646977, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day17.md), answers this exercise at its item 8 of
    §46, and the extraction dropped every inline formula, so the answer cannot be transcribed; the
    site answers an automated request with a Cloudflare human check, which is not worked around.
    Murayama's selection stops at Chapter 4, dbFin has no chapter-7 page, and the Math StackExchange
    searches of this pass on the evaluation map in the compact-open topology, recorded in the
    COMPLAINTS.md entry for §43--§50, returned pages on the admissibility of that topology rather
    than on this exercise. The card keeps its own proof.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Rewrote the solution's frame on 2026-11-19, leaving every argument as it was.
    Each step's body was an indented block opening with a run-in title and a
    "Proof:" line, two of them carrying the proof inline and two a nested proof
    block, and the solution closed with a paragraph outside the proof repeating the
    conclusion. Each step is now a labelled claim (subbasis, preimage, tube,
    inclusion) with its proof in a pf-proof, the trailing paragraph is gone, and the
    preamble names the exercise at printed p. 289 and says that the argument is the
    card's own, as the audit of 2026-11-15 records. No statement, argument or
    citation changes.

- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The argument is correct. It is enough to show that each subbasis element
    S(C,U) of the compact-open topology is open in T. For f_0 in S(C,U), the
    preimage of U under the evaluation map is open and contains the slice
    C x {f_0}; the Tube Lemma, applied with the compact factor C playing the
    role of the space and f_0 the role of the point, gives a T-open
    neighbourhood W of f_0 with C x W inside that preimage; and any f in W then
    satisfies f(C) contained in U, so W lies in S(C,U). Nothing was changed.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Issue #169 read. The argument is right: it suffices to open the subbasis elements
    $S(C,U)$; the preimage $e^{-1}(U)$ is open and contains the slice $C\times\{f_0\}$; the tube
    lemma, with $C$ compact and the point $f_0$, gives $W\in\mathcal T$ containing $f_0$ with
    $C\times W\subseteq e^{-1}(U)$; and every $f\in W$ then has $f(C)\subseteq U$. Citation by
    number: §46 Exercise 8, Lemma 26.8.

- event: solution-written
  by: GPT-6.2
  date: 2026-11-25
  note: >-
    Issue #169. Located Yang Di, Munkres Topology Solution: Chapter 7,
    §46 Exercise 8 (2025-01-15). Checked the actual textbook statement on
    printed p. 289 and Theorem 46.11 on p. 287 against the UCR copy.
    The former direct proof omitted the passage to the subspace
    C x C'(X,Y) before invoking the tube lemma; X itself need not be
    compact. Follow the published solution using the induced-map theorem,
    and give the correct direct tube-lemma argument as well. Preserve the
    earlier audit events and the exercise.

---

::: {.exercise}

Let $\mathcal{C}'(X, Y)$ denote the set $\mathcal{C}(X, Y)$ in some topology $\mathcal{T}$.
Show that if the evaluation map

$$
e: X \times \mathcal{C}'(X, Y) \to Y
$$

is continuous, then $\mathcal{T}$ contains the compact-open topology.
[Hint: The induced map $E: \mathcal{C}'(X, Y) \to \mathcal{C}(X, Y)$ is continuous.]
:::

::: {.solution}
The exercise is Munkres, *Topology* (2000), Section 46, Exercise 8. See [Yang Di's solution, §46, Exercise 8](https://hexo.yougi.top/2025/01/15/Munkres-Topology-Solution-Chapter-7/#Ex-46-8), using Munkres, Theorem 46.11.

Let $\mathcal C(X,Y)$ carry the compact-open topology. By Theorem 46.11 the continuous evaluation map $e:X\times\mathcal C'(X,Y)\to Y$ induces a continuous map
$$
E:\mathcal C'(X,Y)\longrightarrow \mathcal C(X,Y),\qquad E(f)(x)=e(x,f)=f(x).
$$
Thus $E$ is the identity on the underlying set of continuous functions. Continuity of this identity means that every compact-open open set belongs to $\mathcal T$, as required.

For the direct subbasis argument, take a compact subspace $C\subseteq X$, an open set $U\subseteq Y$, and $f_0\in S(C,U)=\{f:f(C)\subseteq U\}$. Continuity of $e$ makes
$$
N=e^{-1}(U)\cap(C\times\mathcal C'(X,Y))
$$
open in $C\times\mathcal C'(X,Y)$, and $C\times\{f_0\}\subseteq N$. Apply the Tube Lemma (Munkres, Lemma 26.8) in that subspace, with the factors interchanged: $C$ is compact, so there is a $\mathcal T$-open neighbourhood $W$ of $f_0$ such that $C\times W\subseteq N$. Consequently $f(C)\subseteq U$ for every $f\in W$. Every point of $S(C,U)$ has a $\mathcal T$-open neighbourhood contained in it, so all the subbasic compact-open sets are $\mathcal T$-open.

Neither argument requires local compactness or the Hausdorff condition on $X$.
:::
