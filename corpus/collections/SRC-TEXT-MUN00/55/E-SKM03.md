---
schema: qual/card@1
id: E-SKM03
kind: problem
title: Positive eigenvalues for nonnegative matrices
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 55: Problem 3 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-55-retractions-and-fixed-points/problem-3-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-55-retractions-and-fixed-points/problem-3-solution.txt), and against Munkres,
    Topology (2000), Section 55 Exercise 3, printed p. 353. This is the one card of the six in Sections 54 to 56 whose dbFin page is not a proof: dbFin writes "the proof is no different from Corollary 55.7 with the only difference in arguing why $\norm{T(x)}>0$", which is a pointer to the book's corollary and not a written argument, so the card keeps a proof of its own and the exercise is listed in the COMPLAINTS.md entry. The card's argument is the standard one and was checked against the book: on the standard simplex $\Delta^2$, a nonnegative nonsingular $A$ sends $x\ne0$ to $Ax\ne0$, since $Ax=0$ with $x\ge0$ forces every column indexed by the support of $x$ to vanish and $A$ to be singular; so $F(x)=Ax/\sum(Ax)_i$ is a continuous self-map of $\Delta^2$, Brouwer gives $Ax=s(x)x$ with $s(x)>0$, and $x\ne0$ because $\sum x_i=1$. This covers nonnegative entries, which the book's Corollary 55.7 does not, and the corollary's extra step is the one dbFin leaves unstated.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published proof has now been located: Pearse, *Topology (2nd ed.) — James R. Munkres*,
    solutions, Cornell, 2005, §55 Exercise 3, printed pp. 18-19, held at
    tmp/sources/cornell-erin-munkres.md (its PDF pages are its printed pages). The solution is
    that proof transcribed, checked against the book: the exercise text on printed p. 353,
    Theorem 55.6 (Brouwer) on printed p. 351, and Corollary 55.7 with its proof on printed
    pp. 351-352. Pearse writes the set as $B=S^2\cap O_1$, the octant, which the card writes
    out. Pearse's proof is correct and nothing in
    it needed repair. What Pearse leaves implicit, and the card states as its own step, is the
    half of well-definedness that the book gets free from positivity of the entries: $x\in B$
    gives $x\ne0$, so $Ax\ne0$ by nonsingularity, so $\norm{Ax}>0$ and $Ax/\norm{Ax}$ has
    nonnegative entries and norm one. Not claimed: that the pages 18-19 are pages of Munkres's
    book -- they are the pages of Pearse's document, whose footers print them; the book's page for
    the exercise is cited separately. Read in the MinerU extraction of
    `tmp/sources/cornell-erin-munkres.pdf`; the pages checked against the PDF's own footers.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription above, in Lamport form, with the source and
    its pages named in its own text. The earlier proof on this card (a fixed point of
    $x\mapsto Ax/\sum_i(Ax)_i$ on the simplex) was correct and was removed only because the card
    is to carry the published proof.
---

::: {.exercise}

Show that if $A$ is a nonsingular 3 by 3 matrix having nonnegative entries, then $A$ has a positive real eigenvalue.
:::

::: {.solution}
The exercise is §55 Exercise 3, printed p. 353. The proof is transcribed from
Erin P. J. Pearse, *Topology (2nd ed.) — James R. Munkres*, solutions, Cornell,
2005, §55 Exercise 3, printed pp. 18–19. It is the book's proof of Corollary
55.7 (printed p. 352) run on the part of $S^2$ in the closed first octant
instead of on all of it, so that nonnegative matrices are covered; the entries
of $A$ being nonnegative is what keeps that octant invariant, and the
nonsingularity of $A$ is what keeps the image away from $\mathbf 0$ there. The
book's corollary assumes strictly positive entries, and the corresponding step
is the one a reader has to supply for this exercise; it is step
[](#image-avoids-zero){.pf-ref}.

Write $\bar{\RR}_+=\{t\in\RR:t\ge0\}$, and put
$$
B=S^2\cap\big(\bar{\RR}_+\times\bar{\RR}_+\times\bar{\RR}_+\big)
=\{x\in\RR^3:\norm x=1,\ x_1,x_2,x_3\ge0\}.
$$

::: pf

::: {.pf-step #ball}
$B$ is homeomorphic to $B^2$, so the Brouwer fixed-point theorem (Theorem
55.6, printed p. 351) holds for continuous self-maps of $B$.

::: pf-proof
Let
$$
\Delta^2=\{y\in\RR^3:y_1,y_2,y_3\ge0,\ y_1+y_2+y_3=1\}
$$
be the standard $2$-simplex, and let $\sigma(x)=x_1+x_2+x_3$. Every $x\in B$
has $\sigma(x)>0$, since $\norm x=1$, so
$$
\varphi:B\to\Delta^2,\qquad \varphi(x)=\frac{x}{\sigma(x)},
$$
is defined, continuous, and has coordinates $\ge0$ summing to $1$; and
$$
\psi:\Delta^2\to B,\qquad \psi(y)=\frac{y}{\norm y},
$$
is defined and continuous, because $\norm y\ge 1/\sqrt3>0$ for $y\in\Delta^2$.
For $x\in B$ we have $\norm{\varphi(x)}=1/\sigma(x)$ and hence
$\psi(\varphi(x))=x$; for $y\in\Delta^2$ we have $\sigma(y)=1$ and hence
$\varphi(\psi(y))=y$. Thus $\varphi$ is a homeomorphism with inverse $\psi$, and
$B$ is homeomorphic to $\Delta^2$, which is homeomorphic to $B^2$ by convexity
of $\Delta^2$ and its compactness. Theorem 55.6 asserts the fixed-point
property for continuous maps of $B^2$ into itself; a homeomorphism carries that
property to $B$.
:::

:::

::: {.pf-step #image-avoids-zero}
For $x\in B$ the vector $Ax$ has nonnegative coordinates and is not
$\mathbf 0$, so
$$
S:B\to B,\qquad S(x)=\frac{Ax}{\norm{Ax}},
$$
is a well-defined continuous self-map of $B$.

::: pf-proof
Since $A$ has nonnegative entries and $x\ge0$ coordinatewise, every coordinate
$(Ax)_i=\sum_j a_{ij}x_j$ of $Ax$ is a sum of nonnegative terms, hence is
$\ge0$. Since $x\in B\subseteq S^2$ we have $x\ne\mathbf 0$; and $A$ is
nonsingular, so $Ax\ne\mathbf 0$ whenever $x\ne\mathbf 0$. Hence $\norm{Ax}>0$,
$S$ is defined, and $S(x)$ has nonnegative coordinates, being $Ax$ divided by
the positive number $\norm{Ax}$, and norm $\norm{Ax}/\norm{Ax}=1$; so
$S(x)\in B$. The map $x\mapsto Ax$ is continuous and linear, $\norm\cdot$ is
continuous and nonzero on the image of $B$, so $S$ is continuous.
:::

:::

::: {.pf-step #fixed-point}
There is $x_0\in B$ with $S(x_0)=x_0$.

::: pf-proof
By step [](#ball){.pf-ref} the fixed-point property holds for continuous
self-maps of $B$, and by step [](#image-avoids-zero){.pf-ref} the map $S$ is
one.
:::

:::

::: {.pf-step}
$\boxed{\lambda=\norm{Ax_0}}$ is a positive real eigenvalue of $A$.

::: pf-proof
From $S(x_0)=x_0$ and the definition of $S$,
$$
\frac{Ax_0}{\norm{Ax_0}}=x_0,
\qquad\text{so}\qquad
Ax_0=\norm{Ax_0}\,x_0 .
$$
Here $x_0\ne\mathbf 0$, because $\norm{x_0}=1$, so $x_0$ is an eigenvector of
$A$; and $\norm{Ax_0}>0$ by step [](#image-avoids-zero){.pf-ref}, so the
eigenvalue $\lambda=\norm{Ax_0}$ is a positive real number.
:::

:::

:::
:::
