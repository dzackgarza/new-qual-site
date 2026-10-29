---
schema: qual/card@1
id: P-TIE-S15-04
kind: problem
title: Analytic functions unimodular on the unit circle are finite Blaschke products
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 4.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed the OCR accent on f, cleaned the LaTeX, and moved the Stein cross-reference to a remark, against Spring 2015, question 4, page 11 of Questions_from_Tie.pdf.
---

::: {.problem}
Suppose $f$ is analytic in an open set containing the unit disc $\DD$ and $\abs{f(z)} = 1$ when $\abs{z} = 1$. Show that either $f(z) = e^{i\theta}$ for some $\theta \in \RR$ or there are finite number of $z_k \in \DD$, $k \le n$ and $\theta \in \RR$ such that
$$
f(z) = e^{i\theta} \prod_{k=1}^n \frac{z - z_k}{1 - \bar{z}_k z}.
$$
:::

::: {.remark}
The source adds "Also cf. Stein et al, 1.4.7, 3.8.17", a pointer to exercises in Stein and Shakarchi, *Complex Analysis*; the statement does not depend on them.
:::

::: {.solution}

::: pf

::: pf-step

The function $f$ has only finitely many zeros in $\DD$, counted with multiplicity.


::: pf-proof

Since $\abs{f(z)}=1$ on $\abs{z}=1$, the function $f$ has no zeros on the unit circle. It is holomorphic on an open neighborhood $U$ of the closed disk. If $f$ had infinitely many zeros in $\DD$, compactness of the closed unit disk would give an accumulation point of those zeros in $\overline{\DD}\subset U$. By the identity theorem, $f$ would then vanish identically on the connected component of $U$ containing the closed disk, contradicting $\abs{f}=1$ on the boundary. Hence there are only finitely many zeros.

:::

:::

::: {.pf-step #s1-2}

Let
$$
z_1,\ldots,z_n\in\DD
$$
be the zeros of $f$, repeated according to multiplicity, and define
$$
B(z)
\coloneqq
\prod_{k=1}^{n}
\frac{z-z_k}{1-\overline{z_k}z}.
$$
Then $B$ is holomorphic on a neighborhood of $\overline{\DD}$ and
$$
\abs{B(z)}=1
$$
for every $\abs{z}=1$.


::: pf-proof

For each $k$ and $\abs{z}\le1$,
$$
\abs{\overline{z_k}z}
\le
\abs{z_k}
<1,
$$
so $1-\overline{z_k}z\ne0$ on a neighborhood of the closed disk. Thus each factor and hence $B$ is holomorphic there.

If $\abs{z}=1$, then
$$
\begin{aligned}
\abs{z-z_k}^2
&=
(z-z_k)(\overline z-\overline{z_k})\\
&=
1-z\overline{z_k}-z_k\overline z+\abs{z_k}^2,
\end{aligned}
$$
whereas
$$
\begin{aligned}
\abs{1-\overline{z_k}z}^2
&=
(1-\overline{z_k}z)(1-z_k\overline z)\\
&=
1-z\overline{z_k}-z_k\overline z+\abs{z_k}^2.
\end{aligned}
$$
Hence
$$
\abs{\frac{z-z_k}{1-\overline{z_k}z}}=1
$$
on the unit circle. Multiplying over $k$ gives $\abs{B(z)}=1$.

:::

:::

::: {.pf-step #s1-3}

The quotient
$$
h(z)\coloneqq\frac{f(z)}{B(z)}
$$
extends to a holomorphic nowhere-zero function on a neighborhood of $\overline{\DD}$.


::: pf-proof

By construction, the zeros of $B$ in $\DD$ are exactly $z_1,\ldots,z_n$ with the same multiplicities as the zeros of $f$. Thus at each common zero, the quotient $f/B$ has a removable singularity and extends holomorphically with a nonzero value. Away from those zeros, $B$ is nonzero. Hence the extended function $h$ is holomorphic and nowhere zero on a neighborhood of the closed disk.

:::

:::

::: {.pf-step #s1-4}

On the unit circle,
$$
\abs{h(z)}=1.
$$


::: pf-proof

For $\abs{z}=1$, the hypotheses and step [](#s1-2){.pf-ref} give
$$
\abs{h(z)}
=
\frac{\abs{f(z)}}{\abs{B(z)}}
=
\frac11
=1.
$$

:::

:::

::: {.pf-step #s1-5}

Throughout the unit disk,
$$
\abs{h(z)}=1.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, both $h$ and $1/h$ are holomorphic on a neighborhood of the closed disk. Step [](#s1-4){.pf-ref} and the maximum modulus principle give
$$
\abs{h(z)}\le1
$$
for $z\in\DD$. Applying the same argument to $1/h$ gives
$$
\abs{\frac1{h(z)}}\le1,
$$
equivalently
$$
\abs{h(z)}\ge1.
$$
Hence $\abs{h(z)}=1$ throughout $\DD$.

:::

:::

::: {.pf-step #s1-6}

The function $h$ is a unimodular constant.


::: pf-proof

If $h$ were nonconstant, the open mapping theorem would imply that $h(\DD)$ is open in $\CC$. But step [](#s1-5){.pf-ref} gives
$$
h(\DD)\subset\{w\in\CC:\abs{w}=1\},
$$
which has empty interior. Therefore $h$ is constant:
$$
h(z)\equiv c.
$$
Step [](#s1-5){.pf-ref} gives $\abs{c}=1$, so
$$
c=e^{i\theta}
$$
for some $\theta\in\RR$.

:::

:::

::: {.pf-step #s1-7}

If $f$ has at least one zero in $\DD$, then
$$
\boxed{
f(z)
=
e^{i\theta}
\prod_{k=1}^{n}
\frac{z-z_k}{1-\overline{z_k}z}.
}
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
f=hB.
$$
Substitute the constant value of $h$ from step [](#s1-6){.pf-ref} and the definition of $B$ from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

If $f$ has no zeros in $\DD$, then
$$
\boxed{f(z)=e^{i\theta}}
$$
for some $\theta\in\RR$.


::: pf-proof

In the zero-free case, take the empty product $B\equiv1$. Steps [](#s1-3){.pf-ref} through [](#s1-6){.pf-ref} then apply directly to $h=f$, showing that $f$ is a unimodular constant.

:::

:::

::: pf-qed

Steps [](#s1-7){.pf-ref} and [](#s1-8){.pf-ref} give exactly the two alternatives in the statement.

:::

:::

:::
