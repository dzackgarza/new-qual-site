---
schema: qual/card@1
id: E-HAT-4.2-1
kind: problem
title: "No retraction $\\RP^n \\to \\RP^k$ via homotopy groups"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 1; the stored statement matches.
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
    Proof read against Hatcher Sec. 4.2 Exercise 1 (AT.txt 19332-19333) and correct as it stands. The
    argument is right in both cases: for k>=2 a retraction would make i_*: pi_k(RP^k) -> pi_k(RP^n)
    injective, but pi_k(RP^k) = pi_k(S^k) = Z and pi_k(RP^n) = pi_k(S^n) = 0 since k<n; for k=1,
    pi_1(RP^1) = Z and pi_1(RP^n) = Z_2 for n>1, and no injection Z -> Z_2 exists. Checked that the
    identifications used are covering-space invariance (S^m -> RP^m is the universal cover for m>=2) and
    need no further hypothesis. Not checked: nothing outside this exercise.

---

::: {.problem}
Use homotopy groups to show there is no retraction $\RP^n \to \RP^k$ if $n > k > 0$.
:::

::: {.solution}
Suppose there were a retraction
$$
r:\RP^n\to\RP^k,
\qquad n>k>0,
$$
of the standard inclusion $i:\RP^k\hookrightarrow\RP^n$. Then
$$
r_*i_*=\operatorname{id}
$$
on every homotopy group, so $i_*$ would be injective.

If $k\ge2$, covering-space invariance of higher homotopy groups gives
$$
\pi_k(\RP^k)\cong\pi_k(S^k)\cong\ZZ,
$$
whereas, since $k<n$,
$$
\pi_k(\RP^n)\cong\pi_k(S^n)=0.
$$
Thus $i_*:\ZZ\to0$ cannot be injective.

If $k=1$, then $\RP^1\cong S^1$, so
$$
\pi_1(\RP^1)\cong\ZZ,
\qquad
\pi_1(\RP^n)\cong\ZZ_2
\quad(n>1).
$$
Again no injection $\ZZ\hookrightarrow\ZZ_2$ exists.

Therefore
$$
\boxed{\RP^n\text{ does not retract onto }\RP^k\text{ for }n>k>0.}
$$
:::
