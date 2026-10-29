---
schema: qual/card@1
id: P-WESTOP12-2
kind: problem
title: Construct the long exact homology sequence of a short exact sequence of chain complexes
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The source's short-exact-sequence diagram is an image placeholder in the retained Markdown extraction. The readable text identifies it only as a short exact sequence of chain complexes of abelian groups, so the diagram's original object and map labels are not reconstructed.
---

::: {.problem}
For the short exact sequence of chain complexes of abelian groups shown in the source, describe the induced long exact sequence on homology. Define every map in the long exact sequence and, where necessary, prove that the definitions are well-defined. You do not need to prove exactness of the resulting sequence.

The labels in the source diagram are unrecovered from the retained Markdown extraction.
:::

::: {.solution}

Write the unrecovered short exact sequence abstractly as
$$
0
\longrightarrow
A_\bullet
\xrightarrow{i}
B_\bullet
\xrightarrow{p}
C_\bullet
\longrightarrow
0.
$$
Thus for every $n$,
$$
0
\longrightarrow
A_n
\xrightarrow{i_n}
B_n
\xrightarrow{p_n}
C_n
\longrightarrow
0
$$
is exact, and $i,p$ are chain maps.

::: pf

::: {.pf-step #s1-1}

The induced long exact sequence is
$$
\boxed{
\cdots
\longrightarrow
H_n(A)
\xrightarrow{i_*}
H_n(B)
\xrightarrow{p_*}
H_n(C)
\xrightarrow{\delta_n}
H_{n-1}(A)
\xrightarrow{i_*}
H_{n-1}(B)
\longrightarrow
\cdots.
}
$$


::: pf-proof

This is the standard long exact homology sequence associated to a short
exact sequence of chain complexes.
The remaining steps define its maps.

:::

:::

::: {.pf-step #s1-2}

Define
$$
i_*:
H_n(A)
\to
H_n(B)
$$
by
$$
i_*([a])
\coloneqq
[i_n(a)].
$$


::: pf-proof

If
$$
a\in Z_n(A),
$$
then
$$
d_B(i_n(a))
=
i_{n-1}(d_Aa)
=
0,
$$
so
$$
i_n(a)
\in
Z_n(B).
$$

If
$$
a-a'
=
d_Au,
$$
then
$$
i_n(a)-i_n(a')
=
i_n(d_Au)
=
d_B(i_{n+1}u),
$$
so the two images differ by a boundary.
Hence the map is well defined on homology classes.

:::

:::

::: {.pf-step #s1-3}

Define
$$
p_*:
H_n(B)
\to
H_n(C)
$$
by
$$
p_*([b])
\coloneqq
[p_n(b)].
$$


::: pf-proof

The proof is identical to step [](#s1-2){.pf-ref}.
If
$$
b\in Z_n(B),
$$
then
$$
d_C(p_n(b))
=
p_{n-1}(d_Bb)
=
0.
$$
If
$$
b-b'
=
d_Bv,
$$
then
$$
p_n(b)-p_n(b')
=
d_C(p_{n+1}v).
$$
Thus $p_*$ is well defined.

:::

:::

::: {.pf-step #s1-4}

To define the connecting homomorphism, let
$$
[c]
\in
H_n(C)
$$
and choose a cycle representative
$$
c\in Z_n(C).
$$
Since
$$
p_n:B_n\to C_n
$$
is surjective, choose
$$
b\in B_n
$$
with
$$
p_n(b)=c.
$$


::: pf-proof

Surjectivity of $p_n$ follows from exactness of
$$
0\to A_n\to B_n\to C_n\to0.
$$

:::

:::

::: {.pf-step #s1-5}

One has
$$
d_Bb
\in
\ker p_{n-1}.
$$


::: pf-proof

Since $p$ is a chain map,
$$
p_{n-1}(d_Bb)
=
d_C(p_n b)
=
d_Cc.
$$
Because
$$
c\in Z_n(C),
$$
$$
d_Cc=0.
$$
Hence
$$
p_{n-1}(d_Bb)=0.
$$

:::

:::

::: {.pf-step #s1-6}

Exactness gives a unique element
$$
a\in A_{n-1}
$$
such that
$$
i_{n-1}(a)
=
d_Bb.
$$


::: pf-proof

Step [](#s1-5){.pf-ref} gives
$$
d_Bb
\in
\ker p_{n-1}.
$$
Exactness at $B_{n-1}$ gives
$$
\ker p_{n-1}
=
\operatorname{im}i_{n-1}.
$$
Thus such an $a$ exists.

It is unique because
$$
i_{n-1}
$$
is injective.

:::

:::

::: {.pf-step #s1-7}

The element
$$
a
$$
from step [](#s1-6){.pf-ref} is a cycle:
$$
d_Aa=0.
$$


::: pf-proof

Apply $d_B$ to
$$
i_{n-1}(a)
=
d_Bb.
$$
Then
$$
d_Bi_{n-1}(a)
=
d_B^2b
=
0.
$$
Since $i$ is a chain map,
$$
i_{n-2}(d_Aa)
=
0.
$$
Injectivity of
$$
i_{n-2}
$$
gives
$$
d_Aa=0.
$$

:::

:::

::: {.pf-step #s1-8}

Define
$$
\boxed{
\delta_n([c])
\coloneqq
[a]
\in
H_{n-1}(A).
}
$$


::: pf-proof

Step [](#s1-7){.pf-ref} shows that $a$ is a cycle.
The next steps verify independence of all choices.

:::

:::

::: {.pf-step #s1-9}

The class
$$
[a]
$$
is independent of the chosen lift
$$
b.
$$


::: pf-proof

Suppose
$$
b'
$$
is another lift of the same cycle $c$:
$$
p_n(b')
=
c
=
p_n(b).
$$
Then
$$
p_n(b'-b)=0,
$$
so exactness gives
$$
b'-b=i_n(x)
$$
for some
$$
x\in A_n.
$$

Let $a'$ be defined from $b'$:
$$
i_{n-1}(a')
=
d_Bb'.
$$
Then
$$
\begin{aligned}
i_{n-1}(a'-a)
&=
d_B(b'-b)\\
&=
d_Bi_n(x)\\
&=
i_{n-1}(d_Ax).
\end{aligned}
$$
Injectivity of $i_{n-1}$ gives
$$
a'-a
=
d_Ax.
$$
Thus
$$
[a']=[a].
$$

:::

:::

::: {.pf-step #s1-10}

The class
$$
[a]
$$
is independent of the chosen cycle representative of
$$
[c].
$$


::: pf-proof

Suppose
$$
c'
=
c+d_Cu
$$
for some
$$
u\in C_{n+1}.
$$
Choose
$$
v\in B_{n+1}
$$
with
$$
p_{n+1}(v)=u.
$$

If $b$ lifts $c$, then
$$
b'
\coloneqq
b+d_Bv
$$
lifts $c'$:
$$
\begin{aligned}
p_n(b')
&=
p_n(b)+p_n(d_Bv)\\
&=
c+d_Cp_{n+1}(v)\\
&=
c+d_Cu\\
&=
c'.
\end{aligned}
$$

But
$$
d_Bb'
=
d_Bb+d_B^2v
=
d_Bb.
$$
Therefore the corresponding element of
$$
A_{n-1}
$$
is exactly the same $a$.
Hence the homology class is independent of the representative.

:::

:::

::: {.pf-step #s1-11}

The connecting map
$$
\delta_n
$$
is a group homomorphism.


::: pf-proof

Let
$$
[c_1],[c_2]
\in
H_n(C).
$$
Choose lifts
$$
b_1,b_2
$$
and corresponding cycles
$$
a_1,a_2
$$
with
$$
i(a_j)=d_Bb_j.
$$
Then
$$
b_1+b_2
$$
lifts
$$
c_1+c_2,
$$
and
$$
\begin{aligned}
d_B(b_1+b_2)
&=
d_Bb_1+d_Bb_2\\
&=
i(a_1)+i(a_2)\\
&=
i(a_1+a_2).
\end{aligned}
$$
Thus
$$
\delta_n([c_1]+[c_2])
=
[a_1+a_2]
=
[a_1]+[a_2].
$$

:::

:::

::: {.pf-step #s1-12}

Hence every map in the long exact sequence
$$
\cdots
\to
H_n(A)
\xrightarrow{i_*}
H_n(B)
\xrightarrow{p_*}
H_n(C)
\xrightarrow{\delta_n}
H_{n-1}(A)
\to
\cdots
$$
is explicitly defined and well defined.


::: pf-proof

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} define and verify the induced maps.
Steps [](#s1-4){.pf-ref} through [](#s1-11){.pf-ref} define and verify the connecting homomorphism.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} states the requested long exact sequence, and step [](#s1-12){.pf-ref} supplies
all map definitions and well-definedness checks requested by the problem.

:::

:::

:::
