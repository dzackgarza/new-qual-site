---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-09
kind: problem
title: A unital multiplication on a positive-dimensional sphere forces odd dimension
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 9 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The source omits the explicit hypothesis n>0, but its parenthetical conclusion “n must be 1, 3, or 7” makes the intended positive-dimensional range clear; n=0 would otherwise be a counterexample.
---

::: {.problem}
Let $n>0$ and let $e\in S^n$.
Suppose there is a map
\[
\mu:S^n\times S^n\longrightarrow S^n
\]
such that
\[
\mu(x,e)=x=\mu(e,x)
\]
for every $x\in S^n$.
Prove that $n$ is odd.

(In fact $n$ must be $1$, $3$, or $7$, but this stronger result is considerably harder.)
:::

Let
\[
u\in H^n(S^n;\mathbb Z)
\cong
\mathbb Z
\]
be a generator.

Let
\[
a=\pi_1^*u,
\qquad
b=\pi_2^*u
\]
in
\[
H^n(S^n\times S^n;\mathbb Z).
\]

::: pf

::: pf-step

By the Künneth theorem,
\[
\boxed{
H^n(S^n\times S^n;\mathbb Z)
\cong
\mathbb Z a\oplus\mathbb Z b}.
\]


::: pf-proof

The only nonzero cohomology groups of \(S^n\) are in degrees \(0\) and \(n\). Thus in total degree \(n\), the Künneth decomposition has exactly the two summands
\[
H^n(S^n)\otimes H^0(S^n)
\]
and
\[
H^0(S^n)\otimes H^n(S^n).
\]

:::

:::

::: pf-step

Therefore there exist integers \(r,s\) such that
\[
\mu^*u
=
ra+sb.
\]


::: pf-proof

Use the basis from step <1>1.

:::

:::

::: pf-step

One has
\[
\boxed{
\mu\circ i_1=\operatorname{id}_{S^n}}.
\]


::: pf-proof

By hypothesis,
\[
\mu(x,e)=x.
\]

:::

:::

::: pf-step

Hence
\[
i_1^*\mu^*u=u.
\]


::: pf-proof

By functoriality,
\[
i_1^*\mu^*
=
(\mu\circ i_1)^*
=
\operatorname{id}^*.
\]

:::

:::

::: pf-step

One has
\[
i_1^*a=u
\qquad\text{and}\qquad
i_1^*b=0.
\]


::: pf-proof

Since
\[
\pi_1\circ i_1=\operatorname{id},
\]
\[
i_1^*a=u.
\]
Since
\[
\pi_2\circ i_1
\]
is the constant map at \(e\), its induced map in positive-degree cohomology is zero, so
\[
i_1^*b=0.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{r=1}.
\]


::: pf-proof

Apply \(i_1^*\) to
\[
\mu^*u=ra+sb.
\]
Using steps <1>4--<1>5 gives
\[
u=ru.
\]
Since \(u\) generates an infinite cyclic group, \(r=1\).

:::

:::

::: pf-step

Similarly,
\[
\boxed{s=1}.
\]


::: pf-proof

The identity
\[
\mu(e,x)=x
\]
gives
\[
\mu\circ i_2=\operatorname{id}.
\]
Also
\[
i_2^*a=0,
\qquad
i_2^*b=u.
\]
Applying \(i_2^*\) to step <1>2 yields
\[
u=su,
\]
hence \(s=1\).

:::

:::

::: pf-step

Thus
\[
\boxed{
\mu^*u=a+b}.
\]


::: pf-proof

Combine steps <1>2, <1>6, and <1>7.

:::

:::

::: pf-step

Since
\[
H^{2n}(S^n;\mathbb Z)=0,
\]
one has
\[
\boxed{u\smile u=0}.
\]


::: pf-proof

The sphere has no cohomology in degree \(2n>n\), because \(n>0\).

:::

:::

::: pf-step

Therefore
\[
\boxed{
0
=
\mu^*(u\smile u)
=
\mu^*u\smile\mu^*u}.
\]


::: pf-proof

Cup product is natural:
\[
\mu^*(u\smile u)
=
\mu^*u\smile\mu^*u.
\]
Use step <1>9.

:::

:::

::: pf-step

Using step <1>8,
\[
0
=
(a+b)^2
=
a^2+a\smile b+b\smile a+b^2.
\]


::: pf-proof

Expand bilinearly.

:::

:::

::: pf-step

One has
\[
\boxed{
a^2=b^2=0}.
\]


::: pf-proof

Since
\[
a=\pi_1^*u,
\]
\[
a^2=\pi_1^*(u^2)=0
\]
by step <1>9. The same argument gives \(b^2=0\).

:::

:::

::: pf-step

Graded commutativity gives
\[
\boxed{
b\smile a
=
(-1)^{n^2}a\smile b
=
(-1)^n a\smile b}.
\]


::: pf-proof

For degree-\(n\) cohomology classes,
\[
\beta\smile\alpha
=
(-1)^{n\cdot n}\alpha\smile\beta.
\]
Since \(n^2\) and \(n\) have the same parity,
\[
(-1)^{n^2}=(-1)^n.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
0
=
\bigl(1+(-1)^n\bigr)
a\smile b}.
\]


::: pf-proof

Substitute steps <1>12--<1>13 into step <1>11.

:::

:::

::: pf-step

By the Künneth theorem,
\[
\boxed{
H^{2n}(S^n\times S^n;\mathbb Z)
\cong
\mathbb Z}
\]
with generator
\[
\boxed{a\smile b}.
\]


::: pf-proof

In total degree \(2n\), the only nonzero Künneth term is
\[
H^n(S^n)\otimes H^n(S^n)
\cong
\mathbb Z,
\]
and the cross product corresponds to
\[
a\smile b.
\]

:::

:::

::: pf-step

If \(n\) were even, then
\[
1+(-1)^n=2,
\]
so step <1>14 would give
\[
2(a\smile b)=0.
\]


::: pf-proof

For even \(n\),
\[
(-1)^n=1.
\]

:::

:::

::: pf-step

This is impossible because
\[
a\smile b
\]
generates an infinite cyclic group.


::: pf-proof

By step <1>15,
\[
H^{2n}(S^n\times S^n;\mathbb Z)\cong\mathbb Z
\]
has no nonzero torsion.

:::

:::

::: pf-step

Therefore \(n\) is not even.


::: pf-proof

The assumption of evenness led to the contradiction in step <1>17.

:::

:::

::: pf-step

Since \(n>0\),
\[
\boxed{n\text{ is odd}}.
\]


::: pf-proof

Every positive integer is either even or odd, and step <1>18 excludes the even case.

:::

:::

::: pf-qed

Step <1>19 is the required conclusion.

:::

:::
