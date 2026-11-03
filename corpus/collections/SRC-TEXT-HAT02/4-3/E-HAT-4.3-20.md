---
schema: qual/card@1
id: E-HAT-4.3-20
kind: problem
title: "Postnikov towers for $\\Omega X$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 20; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof repaired: the card displayed the three-term sequence Omega X_{n+1} -> Omega X_n -> Omega X_{n-1} and called it principal with an Eilenberg--MacLane loop space as fibre. In the book's indexing that is misaligned: AT.txt:20426-20430 has the Postnikov fibration K(pi_{n+1}X, n+1) -> X_{n+1} -> X_n, whose loop is K(pi_{n+1}X, n) -> Omega X_{n+1} -> Omega X_n, whereas the fibre of Omega X_n -> Omega X_{n-1} is K(pi_n X, n-1). The display now names the correct spaces.
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

---

::: {.problem}
Show that by applying the loop space functor to a Postnikov tower for $X$ one obtains a Postnikov tower of principal fibrations for $\Omega X$.
:::

::: {.solution}
Let
$$
\cdots\to X_n\to X_{n-1}\to\cdots
$$
be a Postnikov tower for $X$. Looping preserves fibrations, so
$$
\cdots\to\Omega X_n\to\Omega X_{n-1}\to\cdots
$$
is a tower of fibrations. Since
$$
\pi_i(\Omega X_n)=\pi_{i+1}(X_n),
$$
the space $\Omega X_n$ has the correct truncated homotopy groups to be the corresponding Postnikov stage of $\Omega X$.

The successive Postnikov fibration is classified by a $k$-invariant. Looping its classifying map expresses
$$
\Omega X_{n+1}\to\Omega X_n
$$
as a pullback of a path-space fibration. Equivalently, the three-term sequence
$$
K(\pi_{n+1}X,n)=\Omega K(\pi_{n+1}X,n+1)\longrightarrow\Omega X_{n+1}\longrightarrow\Omega X_n
$$
is a principal fibration, with fiber an Eilenberg--MacLane loop space. Thus
$$
\boxed{\text{looping a Postnikov tower for }X\text{ gives a Postnikov tower of principal fibrations for }\Omega X.}
$$
:::
