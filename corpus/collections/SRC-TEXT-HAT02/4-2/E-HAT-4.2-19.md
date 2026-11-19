---
schema: qual/card@1
id: E-HAT-4.2-19
kind: problem
title: "$\\pi_n(X^n)$ is free abelian for $K(\\pi,1)$'s"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 19; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, §4.2. Read against Hatcher, Exercise 19 of §4.2, printed p. 390, and
    the printed page is added, the card having had none. Checked: the universal cover of a $K(G,1)$
    is contractible and the preimage of $X^n$ is its $n$-skeleton; the pair has no relative cells in
    dimensions at most $n$, so $\pi_i(\widetilde X,\widetilde X^n)=0$ there, and the exact sequence
    of the pair with $\widetilde X$ contractible gives $\pi_i(\widetilde X^n)=0$ for $i<n$; Hurewicz
    then identifies $\pi_n(\widetilde X^n)$ with $H_n(\widetilde X^n)$, which is the kernel of
    $d_n:C_n\to C_{n-1}$ — there being no $(n+1)$-cells — and hence free abelian; and covering maps
    induce isomorphisms on $\pi_n$ for $n\ge2$. No defect.
---

::: {.problem}
If $X$ is a $K(G, 1)$ CW complex, show that $\pi_n(X^n)$ is free abelian for $n \geq 2$.
:::

::: {.solution}
The exercise is §4.2 Exercise 19, printed p. 390.

Let $p:\widetilde X\to X$ be the universal cover. Since $X$ is a $K(G,1)$, $\widetilde X$ is contractible. The inverse image $\widetilde X^{\,n}=p^{-1}(X^n)$ is the $n$-skeleton of $\widetilde X$.

The pair $(\widetilde X,\widetilde X^{\,n})$ has no relative cells in dimensions at most $n$. Hence
$$
\pi_i(\widetilde X,\widetilde X^{\,n})=0\qquad(i\le n).
$$
Since $\widetilde X$ is contractible, the long exact sequence gives
$$
\pi_i(\widetilde X^{\,n})=0\qquad(i<n).
$$
Thus $\widetilde X^{\,n}$ is $(n-1)$-connected. Hurewicz gives
$$
\pi_n(\widetilde X^{\,n})\cong H_n(\widetilde X^{\,n};\ZZ).
$$
Because $\widetilde X^{\,n}$ has no $(n+1)$-cells,
$$
H_n(\widetilde X^{\,n})=\ker\bigl(d_n:C_n\to C_{n-1}\bigr),
$$
a subgroup of the free abelian group $C_n$, hence itself free abelian.

Covering maps induce isomorphisms on $\pi_n$ for $n\ge2$, so
$$
\boxed{\pi_n(X^n)\cong\pi_n(\widetilde X^{\,n})\text{ is free abelian}.}
$$
:::
