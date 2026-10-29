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
$$
\mu:S^n\times S^n\longrightarrow S^n
$$
such that
$$
\mu(x,e)=x=\mu(e,x)
$$
for every $x\in S^n$.
Prove that $n$ is odd.

(In fact $n$ must be $1$, $3$, or $7$, but this stronger result is considerably harder.)
:::

::: {.solution}

Let
$$
u\in H^n(S^n;\ZZ)
\cong
\ZZ
$$
be a generator.

Let
$$
a=\pi_1^*u,
\qquad
b=\pi_2^*u
$$
in
$$
H^n(S^n\times S^n;\ZZ).
$$

::: pf

::: {.pf-step #s1-1}

By the Künneth theorem,
$$
\boxed{
H^n(S^n\times S^n;\ZZ)
\cong
\ZZ a\oplus\ZZ b}.
$$


::: pf-proof

The only nonzero cohomology groups of $S^n$ are in degrees $0$ and $n$. Thus in total degree $n$, the Künneth decomposition has exactly the two summands
$$
H^n(S^n)\otimes H^0(S^n)
$$
and
$$
H^0(S^n)\otimes H^n(S^n).
$$

:::

:::

::: {.pf-step #s1-2}

Therefore there exist integers $r,s$ such that
$$
\mu^*u
=
ra+sb.
$$


::: pf-proof

Use the basis from step [](#s1-1){.pf-ref}.

:::

:::

::: pf-step

One has
$$
\boxed{
\mu\circ i_1=\operatorname{id}_{S^n}}.
$$


::: pf-proof

By hypothesis,
$$
\mu(x,e)=x.
$$

:::

:::

::: {.pf-step #s1-4}

Hence
$$
i_1^*\mu^*u=u.
$$


::: pf-proof

By functoriality,
$$
i_1^*\mu^*
=
(\mu\circ i_1)^*
=
\operatorname{id}^*.
$$

:::

:::

::: {.pf-step #s1-5}

One has
$$
i_1^*a=u
\qquad\text{and}\qquad
i_1^*b=0.
$$


::: pf-proof

Since
$$
\pi_1\circ i_1=\operatorname{id},
$$
$$
i_1^*a=u.
$$
Since
$$
\pi_2\circ i_1
$$
is the constant map at $e$, its induced map in positive-degree cohomology is zero, so
$$
i_1^*b=0.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{r=1}.
$$


::: pf-proof

Apply $i_1^*$ to
$$
\mu^*u=ra+sb.
$$
Using steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} gives
$$
u=ru.
$$
Since $u$ generates an infinite cyclic group, $r=1$.

:::

:::

::: {.pf-step #s1-7}

Similarly,
$$
\boxed{s=1}.
$$


::: pf-proof

The identity
$$
\mu(e,x)=x
$$
gives
$$
\mu\circ i_2=\operatorname{id}.
$$
Also
$$
i_2^*a=0,
\qquad
i_2^*b=u.
$$
Applying $i_2^*$ to step [](#s1-2){.pf-ref} yields
$$
u=su,
$$
hence $s=1$.

:::

:::

::: {.pf-step #s1-8}

Thus
$$
\boxed{
\mu^*u=a+b}.
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-6){.pf-ref}, and [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Since
$$
H^{2n}(S^n;\ZZ)=0,
$$
one has
$$
\boxed{u\smile u=0}.
$$


::: pf-proof

The sphere has no cohomology in degree $2n>n$, because $n>0$.

:::

:::

::: pf-step

Therefore
$$
\boxed{
0
=
\mu^*(u\smile u)
=
\mu^*u\smile\mu^*u}.
$$


::: pf-proof

Cup product is natural:
$$
\mu^*(u\smile u)
=
\mu^*u\smile\mu^*u.
$$
Use step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Using step [](#s1-8){.pf-ref},
$$
0
=
(a+b)^2
=
a^2+a\smile b+b\smile a+b^2.
$$


::: pf-proof

Expand bilinearly.

:::

:::

::: {.pf-step #s1-12}

One has
$$
\boxed{
a^2=b^2=0}.
$$


::: pf-proof

Since
$$
a=\pi_1^*u,
$$
$$
a^2=\pi_1^*(u^2)=0
$$
by step [](#s1-9){.pf-ref}. The same argument gives $b^2=0$.

:::

:::

::: {.pf-step #s1-13}

Graded commutativity gives
$$
\boxed{
b\smile a
=
(-1)^{n^2}a\smile b
=
(-1)^n a\smile b}.
$$


::: pf-proof

For degree-$n$ cohomology classes,
$$
\beta\smile\alpha
=
(-1)^{n\cdot n}\alpha\smile\beta.
$$
Since $n^2$ and $n$ have the same parity,
$$
(-1)^{n^2}=(-1)^n.
$$

:::

:::

::: {.pf-step #s1-14}

Therefore
$$
\boxed{
0
=
\bigl(1+(-1)^n\bigr)
a\smile b}.
$$


::: pf-proof

Substitute steps [](#s1-12){.pf-ref} through [](#s1-13){.pf-ref} into step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-15}

By the Künneth theorem,
$$
\boxed{
H^{2n}(S^n\times S^n;\ZZ)
\cong
\ZZ}
$$
with generator
$$
\boxed{a\smile b}.
$$


::: pf-proof

In total degree $2n$, the only nonzero Künneth term is
$$
H^n(S^n)\otimes H^n(S^n)
\cong
\ZZ,
$$
and the cross product corresponds to
$$
a\smile b.
$$

:::

:::

::: pf-step

If $n$ were even, then
$$
1+(-1)^n=2,
$$
so step [](#s1-14){.pf-ref} would give
$$
2(a\smile b)=0.
$$


::: pf-proof

For even $n$,
$$
(-1)^n=1.
$$

:::

:::

::: {.pf-step #s1-17}

This is impossible because
$$
a\smile b
$$
generates an infinite cyclic group.


::: pf-proof

By step [](#s1-15){.pf-ref},
$$
H^{2n}(S^n\times S^n;\ZZ)\cong\ZZ
$$
has no nonzero torsion.

:::

:::

::: {.pf-step #s1-18}

Therefore $n$ is not even.


::: pf-proof

The assumption of evenness led to the contradiction in step [](#s1-17){.pf-ref}.

:::

:::

::: {.pf-step #s1-19}

Since $n>0$,
$$
\boxed{n\text{ is odd}}.
$$


::: pf-proof

Every positive integer is either even or odd, and step [](#s1-18){.pf-ref} excludes the even case.

:::

:::

::: pf-qed

Step [](#s1-19){.pf-ref} is the required conclusion.

:::

:::

:::
