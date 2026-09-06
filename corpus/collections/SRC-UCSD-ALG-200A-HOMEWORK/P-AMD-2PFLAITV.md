---
schema: qual/card@1
id: P-AMD-2PFLAITV
kind: problem
title: Groups of orders $24$, $36$, and $48$ are not simple
classification:
  areas:
  - algebra
  topics:
  - Simple Groups
  - Sylow Theory
  - Group Actions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 5, Exercise 5(b). The
    previous card promoted the source's optional suggestion of proving the full
    order-<60 theorem. Restored the actual submitted task: prove nonsimplicity
    only for orders 24, 36, and 48, using conjugation on Sylow subgroups.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    For orders 24 and 48, a nonnormal Sylow 2-subgroup would give respectively
    3 Sylow 2-subgroups and hence a nontrivial action into S3; simplicity would
    force an impossible injection. For order 36, a nonnormal Sylow 3-subgroup
    gives 4 Sylow 3-subgroups and an impossible injection into S4.
---

::: {.problem}
Prove that a group of each of the following orders is not simple:
\[
24,
\qquad
36,
\qquad
48.
\]

Hint: consider the kernel of the conjugation action on the set of Sylow $p$-subgroups.
:::

::: {.solution}
<1>1. Let a finite group $G$ act by conjugation on its set of Sylow $p$-subgroups.
If there is more than one Sylow $p$-subgroup and $G$ is simple, then the associated homomorphism
\[
\varphi:G\longrightarrow S_{n_p}
\]
is injective.
::: {.proof}
The conjugation action gives a homomorphism
\[
\varphi:G\longrightarrow S_{n_p},
\]
where $n_p$ is the number of Sylow $p$-subgroups.
Its kernel is a normal subgroup of $G$.

If $n_p>1$, the action is nontrivial: Sylow's conjugacy theorem says that $G$ acts transitively on the Sylow $p$-subgroups, and a trivial action on a set with more than one element cannot be transitive.
Thus
\[
\ker\varphi\ne G.
\]
If $G$ is simple, its only normal subgroups are $\{1\}$ and $G$, so
\[
\ker\varphi=\{1\}.
\]
Hence $\varphi$ is injective.
:::

<1>2. Every group of order $24$ is not simple.
::: {.proof}
Let $|G|=24=2^3\cdot3$ and let $n_2$ be the number of Sylow $2$-subgroups.
Sylow's theorem gives
\[
n_2\equiv1\pmod2
\qquad\text{and}\qquad
n_2\mid3.
\]
Hence
\[
n_2\in\{1,3\}.
\]
If $n_2=1$, the unique Sylow $2$-subgroup is a nontrivial proper normal subgroup, so $G$ is not simple.

Suppose instead that $n_2=3$ and that $G$ were simple.
By <1>1, conjugation on the three Sylow $2$-subgroups would give an injection
\[
G\hookrightarrow S_3.
\]
But
\[
|G|=24>6=|S_3|,
\]
which is impossible.
Therefore $G$ is not simple.
:::

<1>3. Every group of order $36$ is not simple.
::: {.proof}
Let $|G|=36=2^2\cdot3^2$ and let $n_3$ be the number of Sylow $3$-subgroups.
Sylow's theorem gives
\[
n_3\equiv1\pmod3
\qquad\text{and}\qquad
n_3\mid4.
\]
Thus
\[
n_3\in\{1,4\}.
\]
If $n_3=1$, the unique Sylow $3$-subgroup is normal and $G$ is not simple.

If $n_3=4$ and $G$ were simple, <1>1 would give an injection
\[
G\hookrightarrow S_4.
\]
This is impossible because
\[
|G|=36>24=|S_4|.
\]
Hence every group of order $36$ is not simple.
:::

<1>4. Every group of order $48$ is not simple.
::: {.proof}
Let $|G|=48=2^4\cdot3$ and let $n_2$ be the number of Sylow $2$-subgroups.
Sylow's theorem gives
\[
n_2\equiv1\pmod2
\qquad\text{and}\qquad
n_2\mid3.
\]
Hence
\[
n_2\in\{1,3\}.
\]
If $n_2=1$, the Sylow $2$-subgroup is normal and $G$ is not simple.

If $n_2=3$ and $G$ were simple, <1>1 would give an injection
\[
G\hookrightarrow S_3.
\]
But
\[
|G|=48>6=|S_3|,
\]
again impossible.
Therefore every group of order $48$ is not simple.
:::
:::
