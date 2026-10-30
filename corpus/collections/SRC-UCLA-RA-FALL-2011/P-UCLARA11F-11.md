---
schema: qual/card@1
id: P-UCLARA11F-11
kind: problem
title: Sublevel components of a zero-free entire function are unbounded
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $f:\CC\to\CC$ be holomorphic with $f(z)\ne0$ for every $z\in\CC$.
Define
$$
U=\{z\in\CC:\abs{f(z)}<1\}.
$$
Show that every connected component of $U$ is unbounded.
:::

::: {.solution}

Suppose, toward a contradiction, that
$$
\Omega
$$
is a bounded connected component of
$$
U=\{z\in\CC:\abs{f(z)}<1\}.
$$

::: pf

::: pf-step

The set $U$ is open.


::: pf-proof

The function
$$
z\mapsto \abs{f(z)}
$$
is continuous, and
$$
U=\abs{f}^{-1}((-\infty,1)).
$$

:::

:::

::: pf-step

The component $\Omega$ is open.


::: pf-proof

Connected components of open subsets of $\CC$ are open, because $\CC$ is locally connected.

:::

:::

::: {.pf-step #s1-3}

For every
$$
z\in\overline\Omega,
$$
one has
$$
\boxed{\abs{f(z)}\le1}.
$$


::: pf-proof

Choose a sequence
$$
z_n\in\Omega
$$
with
$$
z_n\to z.
$$
Since
$$
\abs{f(z_n)}<1,
$$
continuity gives
$$
\abs{f(z)}\le1.
$$

:::

:::

::: {.pf-step #s1-4}

For every
$$
z\in\partial\Omega,
$$
one has
$$
\boxed{\abs{f(z)}=1}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} gives
$$
\abs{f(z)}\le1.
$$
Suppose instead that
$$
\abs{f(z)}<1.
$$
Then $z\in U$. Since $U$ is open, there is a connected open disk
$$
B(z,r)\subseteq U.
$$
Because $z\in\partial\Omega$, the disk meets $\Omega$. Thus
$$
\Omega\cup B(z,r)
$$
is a connected subset of $U$ strictly larger than the connected component $\Omega$, contradiction.
Hence $\abs{f(z)}\not<1$, so equality holds.

:::

:::

::: pf-step

Since $f$ has no zeros,
$$
g(z)=\frac1{f(z)}
$$
is entire.


::: pf-proof

The reciprocal of a nowhere-zero holomorphic function is holomorphic.

:::

:::

::: {.pf-step #s1-6}

On $\Omega$,
$$
\boxed{\abs{g(z)}>1}.
$$


::: pf-proof

By definition of $U$,
$$
\abs{f(z)}<1
$$
for $z\in\Omega$, and $f(z)\ne0$. Taking reciprocals gives
$$
\abs{g(z)}=\frac1{\abs{f(z)}}>1.
$$

:::

:::

::: {.pf-step #s1-7}

On $\partial\Omega$,
$$
\boxed{\abs{g(z)}=1}.
$$


::: pf-proof

Use step [](#s1-4){.pf-ref}:
$$
\abs{g(z)}=\frac1{\abs{f(z)}}=1.
$$

:::

:::

::: {.pf-step #s1-8}

Since $\Omega$ is bounded, $\overline\Omega$ is compact.


::: pf-proof

The closure is closed and bounded in $\CC\cong\RR^2$. By Heine--Borel, it is compact.

:::

:::

::: {.pf-step #s1-9}

The continuous function $\abs{g}$ attains a maximum on $\overline\Omega$.


::: pf-proof

Apply the extreme-value theorem to the compact set from step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

This maximum is strictly greater than $1$.


::: pf-proof

Every point of $\Omega$ satisfies
$$
\abs{g}>1
$$
by step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

No boundary point can attain that maximum.


::: pf-proof

By step [](#s1-7){.pf-ref}, every boundary point has modulus exactly $1$, while the maximum is $>1$ by step [](#s1-10){.pf-ref}.

:::

:::

::: pf-step

Hence $\abs{g}$ attains its maximum at an interior point of $\Omega$.


::: pf-proof

The maximum is attained somewhere in $\overline\Omega$ by step [](#s1-9){.pf-ref}, and step [](#s1-11){.pf-ref} excludes the boundary.

:::

:::

::: pf-step

By the maximum modulus principle,
$$
\boxed{
g\text{ is constant on }\Omega}.
$$


::: pf-proof

A holomorphic function on a connected open set that attains a modulus maximum at an interior point is constant.

:::

:::

::: pf-step

By the identity theorem, $g$ is constant on all of $\CC$.


::: pf-proof

The entire function $g$ agrees with a constant function on the nonempty open set $\Omega$, so the identity theorem extends that equality to the connected domain $\CC$.

:::

:::

::: pf-step

Hence $f=1/g$ is also constant on $\CC$.


::: pf-proof

The constant value of $g$ is nonzero because $g=1/f$.

:::

:::

::: {.pf-step #s1-16}

This contradicts the existence of the boundary $\partial\Omega$ with
$$
\abs{f}=1
$$
while
$$
\abs{f}<1
$$
throughout $\Omega$.


::: pf-proof

If $f$ were constant, its modulus could not be both $<1$ on $\Omega$ and equal to $1$ on $\partial\Omega$.

:::

:::

::: {.pf-step #s1-17}

Therefore no connected component of $U$ can be bounded.


::: pf-proof

The assumption of a bounded component led to the contradiction in step [](#s1-16){.pf-ref}.

:::

:::

::: {.pf-step #s1-18}

Thus
$$
\boxed{
\text{every connected component of }
\{z:\abs{f(z)}<1\}
\text{ is unbounded}.}
$$


::: pf-proof

This is step [](#s1-17){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-18){.pf-ref} is the required conclusion.

:::

:::

:::
