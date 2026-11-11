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
    Topology (2000), Section 55 Exercise 3, printed p. 353. This is the one card of the six in Sections 54 to 56 whose dbFin page is not a proof: dbFin writes "the proof is no different from Corollary 55.7 with the only difference in arguing why $\|T(x)\|>0$", which is a pointer to the book's corollary and not a written argument, so the card keeps a proof of its own and the exercise is listed in the COMPLAINTS.md entry. The card's argument is the standard one and was checked against the book: on the standard simplex $\Delta^2$, a nonnegative nonsingular $A$ sends $x\ne0$ to $Ax\ne0$, since $Ax=0$ with $x\ge0$ forces every column indexed by the support of $x$ to vanish and $A$ to be singular; so $F(x)=Ax/\sum(Ax)_i$ is a continuous self-map of $\Delta^2$, Brouwer gives $Ax=s(x)x$ with $s(x)>0$, and $x\ne0$ because $\sum x_i=1$. This covers nonnegative entries, which the book's Corollary 55.7 does not, and the corollary's extra step is the one dbFin leaves unstated.
---

::: {.exercise}

Show that if $A$ is a nonsingular 3 by 3 matrix having nonnegative entries, then $A$ has a positive real eigenvalue.
:::

::: {.solution}
Let
$$
\Delta^2=\{x=(x_1,x_2,x_3)\in\RR^3:x_i\ge0,\ x_1+x_2+x_3=1\}
$$
be the standard $2$-simplex. Since $A$ has nonnegative entries, $Ax$ has nonnegative coordinates for every $x\in\Delta^2$. Since $A$ is nonsingular and $x\ne0$, we also have $Ax\ne0$. Hence
$$
s(x)=\sum_{i=1}^3(Ax)_i>0.
$$
Define
$$
F:\Delta^2\to\Delta^2,
\qquad
F(x)=\frac{Ax}{s(x)}.
$$
This map is continuous. By the Brouwer fixed-point theorem, there exists $x\in\Delta^2$ with $F(x)=x$. Therefore
$$
Ax=s(x)x.
$$
Thus $x\ne0$ is an eigenvector of $A$ with real eigenvalue
$$
\lambda=s(x)>0.
$$
Hence every nonsingular $3\times3$ matrix with nonnegative entries has a positive real eigenvalue.
:::
