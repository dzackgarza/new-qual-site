---
schema: qual/card@1
id: P-AMD-6ESY7G3W
kind: problem
title: Ideals, quotients, and simplicity of the matrix ring $M_n(R)$
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Ideals
  - Semisimplicity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 6, Exercise 7. Restored
    both source parts, the two-sided ideal hypothesis in part (a), the quotient
    isomorphism, and the concluding definition of simplicity over a division
    ring.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Entrywise reduction modulo I has kernel M_n(I), giving the quotient
    isomorphism. For an arbitrary two-sided ideal J of M_n(R), define I by the
    possible (1,1)-entries rE_11 in J. Matrix-unit multiplication extracts every
    entry of a matrix in J and rebuilds every rE_ij from rE_11, proving
    J=M_n(I). A division ring has only the zero and unit two-sided ideals, so its
    full matrix ring is simple.
---

::: {.problem}
Let $R$ be a ring and let $M_n(R)$ be the matrix ring for some $n\ge1$.

(a) Given a two-sided ideal $I\trianglelefteq R$, prove that
\[
M_n(I)=\{(a_{ij})\in M_n(R):a_{ij}\in I\text{ for every }i,j\}
\]
is a two-sided ideal of $M_n(R)$ and that
\[
M_n(R)/M_n(I)\cong M_n(R/I).
\]

(b) Prove that every two-sided ideal of $M_n(R)$ has the form $M_n(I)$ for some two-sided ideal $I\trianglelefteq R$.
Conclude that if $R$ is a division ring, then $M_n(R)$ is a simple ring; that is, its only two-sided ideals are $0$ and $M_n(R)$.
:::

::: {.solution}
<1>1. If $I\trianglelefteq R$ is a two-sided ideal, then $M_n(I)$ is a two-sided ideal of $M_n(R)$.
::: {.proof}
It is an additive subgroup because addition and additive inverses are taken entrywise.

Let
\[
A=(a_{ij})\in M_n(R),
\qquad
B=(b_{ij})\in M_n(I).
\]
The $(i,j)$-entry of $AB$ is
\[
(AB)_{ij}=\sum_{k=1}^n a_{ik}b_{kj}.
\]
Since each $b_{kj}\in I$ and $I$ is a left ideal, every summand lies in $I$, hence $(AB)_{ij}\in I$.
Thus
\[
AB\in M_n(I).
\]
Similarly,
\[
(BA)_{ij}=\sum_{k=1}^n b_{ik}a_{kj}\in I
\]
because $I$ is a right ideal.
Hence
\[
BA\in M_n(I).
\]
Therefore $M_n(I)$ is a two-sided ideal.
:::

<1>2. Entrywise reduction modulo $I$ defines a surjective ring homomorphism
\[
\rho:M_n(R)\longrightarrow M_n(R/I)
\]
whose kernel is $M_n(I)$.
::: {.proof}
Define
\[
\rho((a_{ij}))=(a_{ij}+I).
\]
Entrywise addition is plainly preserved.
For multiplication,
\[
\rho(AB)_{ij}
 =\sum_k a_{ik}b_{kj}+I
 =\sum_k(a_{ik}+I)(b_{kj}+I)
 =(\rho(A)\rho(B))_{ij}.
\]
Thus $\rho$ is a ring homomorphism.

It is surjective because any matrix over $R/I$ admits entrywise lifts to $R$.
Moreover,
\[
\rho((a_{ij}))=0
\quad\Longleftrightarrow\quad
a_{ij}\in I\text{ for every }i,j,
\]
so
\[
\ker\rho=M_n(I).
\]
:::

<1>3. There is an isomorphism
\[
M_n(R)/M_n(I)\cong M_n(R/I).
\]
::: {.proof}
Apply the first isomorphism theorem to the surjection $\rho$ from <1>2. This completes part (a).
:::

<1>4. Let $J\trianglelefteq M_n(R)$ be a two-sided ideal.
Define
\[
I=\{r\in R:rE_{11}\in J\},
\]
where $E_{ij}$ denotes the usual matrix unit.
Then $I$ is a two-sided ideal of $R$.
::: {.proof}
If $r,s\in I$, then
\[
(r+s)E_{11}=rE_{11}+sE_{11}\in J,
\]
and
\[
(-r)E_{11}=-(rE_{11})\in J.
\]
Thus $I$ is an additive subgroup.

Let $a\in R$ and $r\in I$.
Since $J$ is a two-sided ideal,
\[
(aE_{11})(rE_{11})=(ar)E_{11}\in J
\]
and
\[
(rE_{11})(aE_{11})=(ra)E_{11}\in J.
\]
Hence $ar,ra\in I$, so $I\trianglelefteq R$ is two-sided.
:::

<1>5. Every entry of every matrix in $J$ belongs to $I$.
::: {.proof}
Let
\[
A=(a_{ij})\in J.
\]
For every $i,j$, two-sidedness of $J$ gives
\[
E_{1i}AE_{j1}\in J.
\]
Direct matrix-unit multiplication yields
\[
E_{1i}AE_{j1}=a_{ij}E_{11}.
\]
Therefore $a_{ij}\in I$ by the definition of $I$.
Hence
\[
A\in M_n(I).
\]
Thus
\[
J\le M_n(I).
\]
:::

<1>6. For every $r\in I$ and every $i,j$,
\[
rE_{ij}\in J.
\]
::: {.proof}
Since $r\in I$,
\[
rE_{11}\in J.
\]
Because $J$ is a two-sided ideal,
\[
E_{i1}(rE_{11})E_{1j}\in J.
\]
The left side is exactly
\[
rE_{ij}.
\]
Hence $rE_{ij}\in J$.
:::

<1>7. Every two-sided ideal $J$ of $M_n(R)$ is of the form $M_n(I)$ for a two-sided ideal $I$ of $R$.
::: {.proof}
For the ideal $I$ defined in <1>4, <1>5 gives
\[
J\le M_n(I).
\]
Conversely, if
\[
B=(b_{ij})\in M_n(I),
\]
then
\[
B=\sum_{i,j}b_{ij}E_{ij}.
\]
Each summand belongs to $J$ by <1>6, hence $B\in J$.
Thus
\[
M_n(I)\le J.
\]
Therefore
\[
J=M_n(I).
\]
:::

<1>8. A division ring has no two-sided ideals other than $0$ and itself.
::: {.proof}
Let $D$ be a division ring and let $0\ne I\trianglelefteq D$.
Choose $0\ne r\in I$.
Since $r$ is invertible and $I$ is a left ideal,
\[
r^{-1}r=1\in I.
\]
Hence every $d\in D$ satisfies
\[
d=d\cdot1\in I,
\]
so $I=D$.
:::

<1>9. If $R$ is a division ring, then $M_n(R)$ is simple.
::: {.proof}
Let $J\trianglelefteq M_n(R)$ be a two-sided ideal.
By <1>7,
\[
J=M_n(I)
\]
for some two-sided ideal $I\trianglelefteq R$.
By <1>8,
\[
I=0
\qquad\text{or}\qquad
I=R.
\]
Therefore
\[
J=0
\qquad\text{or}\qquad
J=M_n(R).
\]
Thus $M_n(R)$ is simple, completing part (b).
:::

<1>10. Q.E.D.
::: {.proof}
Parts (a) and (b) are <1>3 and <1>9.
:::
:::
