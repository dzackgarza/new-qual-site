---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-01
kind: problem
title: Kronecker pairing descends to homology and cohomology
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 1 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
---

::: {.problem}
Let $R$ be a ring.
If
$$
z=\sum_i r_i\sigma_i
$$
is a $k$-cycle in $C_k(X;R)$ and $\alpha\in C^k(X;R)$, define
$$
\langle z,\alpha\rangle=\sum_i r_i\,\alpha(\sigma_i).
$$
Prove that if $z-z'$ is a boundary, then $\langle z,\alpha\rangle=\langle z',\alpha\rangle$.
Likewise, prove that if $\alpha$ is a coboundary and $z$ is a cycle, then $\langle z,\alpha\rangle=0$.
Deduce that there is a well-defined bilinear pairing
$$
H_k(X;R)\times H^k(X;R)\longrightarrow R.
$$
This pairing is sometimes called the Kronecker product.
:::

The first assertion in the source needs the standard missing hypothesis
$$
\delta\alpha=0.
$$
Without it, the assertion is false.

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The literal first assertion fails for an arbitrary cochain.


::: pf-proof

Take
$$
X=[0,1],
\qquad
R=\ZZ,
\qquad
k=0.
$$
Let
$$
z=[1],
\qquad
z'=[0].
$$
Both are $0$-cycles, and if
$$
\sigma:[0,1]\to[0,1],
\qquad
\sigma(t)=t,
$$
is the standard singular $1$-simplex, then
$$
z-z'
=
\partial\sigma.
$$

Choose a $0$-cochain
$$
\alpha\in C^0(X;\ZZ)
$$
with
$$
\alpha([1])=1,
\qquad
\alpha([0])=0.
$$
Then
$$
\langle z,\alpha\rangle=1
$$
while
$$
\langle z',\alpha\rangle=0.
$$
Thus boundary-equivalent cycles need not pair equally with an arbitrary
cochain.

:::

:::

::: {.pf-step #s1-2}

For a singular chain
$$
c\in C_k(X;R)
$$
and a cochain
$$
\beta\in C^{k-1}(X;R),
$$
the chain--cochain pairing satisfies
$$
\boxed{
\langle c,\delta\beta\rangle
=
\langle\partial c,\beta\rangle.
}
$$


::: pf-proof

By definition, the singular coboundary
$$
\delta\beta\in C^k(X;R)
$$
is the cochain
$$
(\delta\beta)(\sigma)
=
\beta(\partial\sigma)
$$
on each singular $k$-simplex $\sigma$.

If
$$
c=\sum_i r_i\sigma_i,
$$
then
$$
\begin{aligned}
\langle c,\delta\beta\rangle
&=
\sum_i r_i(\delta\beta)(\sigma_i)\\
&=
\sum_i r_i\beta(\partial\sigma_i)\\
&=
\beta\left(
\sum_i r_i\partial\sigma_i
\right)\\
&=
\beta(\partial c)\\
&=
\langle\partial c,\beta\rangle.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

If
$$
z-z'=\partial w
$$
and
$$
\alpha\in Z^k(X;R)
$$
is a cocycle, then
$$
\boxed{
\langle z,\alpha\rangle
=
\langle z',\alpha\rangle.
}
$$


::: pf-proof

Since
$$
\delta\alpha=0,
$$
step [](#s1-2){.pf-ref} gives
$$
\begin{aligned}
\langle z,\alpha\rangle
-
\langle z',\alpha\rangle
&=
\langle z-z',\alpha\rangle\\
&=
\langle\partial w,\alpha\rangle\\
&=
\langle w,\delta\alpha\rangle\\
&=
0.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

If
$$
\alpha=\delta\beta
$$
is a coboundary and
$$
z\in Z_k(X;R)
$$
is a cycle, then
$$
\boxed{
\langle z,\alpha\rangle=0.
}
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\langle z,\alpha\rangle
=
\langle z,\delta\beta\rangle
=
\langle\partial z,\beta\rangle.
$$
Since
$$
\partial z=0,
$$
the right-hand side is zero.

:::

:::

::: {.pf-step #s1-5}

If
$$
z,z'\in Z_k(X;R)
$$
represent the same homology class and
$$
\alpha,\alpha'\in Z^k(X;R)
$$
represent the same cohomology class, then
$$
\langle z,\alpha\rangle
=
\langle z',\alpha'\rangle.
$$


::: pf-proof

Because
$$
[z]=[z'],
$$
one has
$$
z-z'=\partial w
$$
for some
$$
w\in C_{k+1}(X;R).
$$
Step [](#s1-3){.pf-ref} gives
$$
\langle z,\alpha\rangle
=
\langle z',\alpha\rangle.
$$

Because
$$
[\alpha]=[\alpha'],
$$
there is
$$
\beta\in C^{k-1}(X;R)
$$
with
$$
\alpha-\alpha'=\delta\beta.
$$
Then step [](#s1-4){.pf-ref}, applied to the cycle $z'$, gives
$$
\langle z',\alpha-\alpha'\rangle=0.
$$
Hence
$$
\langle z',\alpha\rangle
=
\langle z',\alpha'\rangle.
$$
Combining the two equalities proves the claim.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\langle-,-\rangle:
H_k(X;R)\times H^k(X;R)
\longrightarrow
R,
\qquad
([z],[\alpha])
\longmapsto
\langle z,\alpha\rangle
}
$$
is well defined.


::: pf-proof

Step [](#s1-5){.pf-ref} shows independence of both the cycle representative and the
cocycle representative.

:::

:::

::: {.pf-step #s1-7}

The pairing is bilinear.


::: pf-proof

On chain and cochain representatives,
$$
\left\langle
z_1+z_2,\alpha
\right\rangle
=
\langle z_1,\alpha\rangle
+
\langle z_2,\alpha\rangle,
$$
and
$$
\left\langle
z,\alpha_1+\alpha_2
\right\rangle
=
\langle z,\alpha_1\rangle
+
\langle z,\alpha_2\rangle.
$$
Scalar multiplication behaves compatibly as well.
These identities descend through the quotient groups by step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} records the defect in the literal source statement.
Steps [](#s1-2){.pf-ref} through [](#s1-7){.pf-ref} prove the corrected Kronecker pairing on homology and
cohomology.

:::

:::

:::
