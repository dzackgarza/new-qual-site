---
schema: qual/card@1
id: P-MAXAT-4-10
kind: problem
title: Maxim algebraic topology 4.10
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 4, problem 10 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Where does the $7\text{-torsion}$ appear first in the homotopy groups of $S ^ { n }  { ? }$
:::

::: {.solution}
<1>1. Serre's first-$p$-torsion theorem states that for every prime $p$
and every $n\ge3$,
\[
\pi_{n+k}(S^n)
\]
has no $p$-torsion when
\[
0<k<2p-3,
\]
whereas the $p$-primary subgroup of
\[
\pi_{n+2p-3}(S^n)
\]
is
\[
\mathbb Z/p.
\]

::: {.proof}
This is Serre's theorem on the first occurrence of prime-primary torsion
in the homotopy groups of spheres. It is obtained by applying the
Hurewicz theorem modulo the Serre class of finite groups of order prime
to $p$ to the appropriate stage of the Whitehead tower of $S^n$.

For $n=3$, the calculation is exactly the one carried out in the preceding
problem:
\[
\pi_{2p}(S^3)_{(p)}
\cong
\mathbb Z/p.
\]
The general Whitehead-tower argument gives the displayed shift
\[
2p-3
\]
for every $n\ge3$.
:::

<1>2. For $p=7$,
\[
2p-3
=
11.
\]

::: {.proof}
Direct calculation gives
\[
2\cdot7-3=14-3=11.
\]
:::

<1>3. Therefore, for every $n\ge3$, the first $7$-torsion in the
homotopy groups of $S^n$ occurs in
\[
\boxed{
\pi_{n+11}(S^n),
}
\]
and its $7$-primary subgroup there is
\[
\boxed{
\mathbb Z/7.
}
\]

::: {.proof}
Substitute $p=7$ into step <1>1 and use step <1>2. There is no
$7$-torsion in
\[
\pi_{n+k}(S^n)
\qquad
(0<k<11),
\]
while
\[
\pi_{n+11}(S^n)
\]
contains a unique first $7$-primary subgroup isomorphic to
\[
\mathbb Z/7.
\]
:::

<1>4. For $S^2$, the first $7$-torsion occurs instead in
\[
\boxed{
\pi_{14}(S^2),
}
\]
whose $7$-primary subgroup is $\mathbb Z/7$.

::: {.proof}
The Hopf fibration
\[
S^1
\longrightarrow
S^3
\longrightarrow
S^2
\]
gives, for every $i\ge3$, an isomorphism
\[
\pi_i(S^3)
\xrightarrow{\cong}
\pi_i(S^2),
\]
because
\[
\pi_i(S^1)=\pi_{i-1}(S^1)=0.
\]

By the preceding problem with $p=7$, the first $7$-torsion in
\[
\pi_i(S^3)
\]
occurs at
\[
i=2p=14
\]
and is $\mathbb Z/7$. The same is therefore true for $S^2$.
:::

<1>5. For $S^1$, no homotopy group contains $7$-torsion.

::: {.proof}
One has
\[
\pi_1(S^1)\cong\mathbb Z
\]
and
\[
\pi_i(S^1)=0
\qquad
(i>1).
\]
All these groups are $7$-torsion-free.
:::

<1>6. Q.E.D.

::: {.proof}
For the usual range $n\ge3$, step <1>3 gives the answer
\[
\pi_{n+11}(S^n)
\]
with first $7$-primary subgroup $\mathbb Z/7$. Steps <1>4--<1>5 record
the low-dimensional exceptions.
:::
:::
