---
schema: qual/card@1
id: P-ALGF23A
kind: problem
title: "Proper subgroups of nilpotent groups and normality of maximal subgroups"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 1 of the official UCSD Algebra Qualifying Exam, Fall 2023 source; both normalizer and maximal-subgroup assertions agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the normalizer condition directly from the upper central series and deduced normality of maximal subgroups.
---

::: problem
Suppose $G$ is a nilpotent group.

(a) Prove that for every proper subgroup $H$ of $G$, $H \neq N_G(H)$.

(b) Prove that every maximal subgroup of $G$ is normal.
:::

::: {.solution}
Let
\[
1=Z_0(G)\le Z_1(G)\le\cdots\le Z_c(G)=G
\]
be the upper central series of the nilpotent group $G$.

<1>1. For every proper subgroup $H<G$, there exists an index $i\ge1$ such that
\[
Z_{i-1}(G)\le H
\quad\text{but}\quad
Z_i(G)\nleq H.
\]
::: {.proof}
Since $Z_0(G)=1\le H$ and $Z_c(G)=G\nleq H$, there is a least $i$ for which
\[
Z_i(G)\nleq H.
\]
Minimality gives $Z_{i-1}(G)\le H$.
:::

<1>2. Choose
\[
x\in Z_i(G)\setminus H.
\]
Then $x\in N_G(H)$.
::: {.proof}
For every $h\in H$, the image of $x$ in
\[
G/Z_{i-1}(G)
\]
is central, because $x\in Z_i(G)$.
Hence the commutator satisfies
\[
[x,h]\in Z_{i-1}(G)\le H.
\]
Therefore
\[
x h x^{-1}=[x,h]h\in H
\]
for every $h\in H$.
Thus
\[
xHx^{-1}\subseteq H.
\]
Applying the same argument to $x^{-1}\in Z_i(G)$ gives the reverse inclusion, so
\[
xHx^{-1}=H.
\]
Hence $x\in N_G(H)$.
:::

<1>3. Every proper subgroup $H<G$ is properly contained in its normalizer:
\[
H<N_G(H).
\]
::: {.proof}
One always has $H\le N_G(H)$.
By <1>2, the chosen element $x$ lies in $N_G(H)$ but not in $H$.
Thus the containment is strict.
This proves part (a).
:::

<1>4. Every maximal subgroup $M<G$ is normal in $G$.
::: {.proof}
By <1>3,
\[
M<N_G(M)\le G.
\]
Since $M$ is maximal among proper subgroups of $G$, the strict containment forces
\[
N_G(M)=G.
\]
By definition of the normalizer, this is equivalent to
\[
M\trianglelefteq G.
\]
This proves part (b).
:::
:::
