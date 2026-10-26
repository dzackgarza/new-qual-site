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
Let $f:\mathbb C\to\mathbb C$ be holomorphic with $f(z)\ne0$ for every $z\in\mathbb C$.
Define
\[
U=\{z\in\mathbb C:|f(z)|<1\}.
\]
Show that every connected component of $U$ is unbounded.
:::

Suppose, toward a contradiction, that
\[
\Omega
\]
is a bounded connected component of
\[
U=\{z\in\mathbb C:|f(z)|<1\}.
\]

::: pf

::: pf-step

The set \(U\) is open.


::: pf-proof

The function
\[
z\mapsto |f(z)|
\]
is continuous, and
\[
U=|f|^{-1}((-\infty,1)).
\]

:::

:::

::: pf-step

The component \(\Omega\) is open.


::: pf-proof

Connected components of open subsets of \(\mathbb C\) are open, because \(\mathbb C\) is locally connected.

:::

:::

::: pf-step

For every
\[
z\in\overline\Omega,
\]
one has
\[
\boxed{|f(z)|\le1}.
\]


::: pf-proof

Choose a sequence
\[
z_n\in\Omega
\]
with
\[
z_n\to z.
\]
Since
\[
|f(z_n)|<1,
\]
continuity gives
\[
|f(z)|\le1.
\]

:::

:::

::: pf-step

For every
\[
z\in\partial\Omega,
\]
one has
\[
\boxed{|f(z)|=1}.
\]


::: pf-proof

Step <1>3 gives
\[
|f(z)|\le1.
\]
Suppose instead that
\[
|f(z)|<1.
\]
Then \(z\in U\). Since \(U\) is open, there is a connected open disk
\[
B(z,r)\subseteq U.
\]
Because \(z\in\partial\Omega\), the disk meets \(\Omega\). Thus
\[
\Omega\cup B(z,r)
\]
is a connected subset of \(U\) strictly larger than the connected component \(\Omega\), contradiction.
Hence \(|f(z)|\not<1\), so equality holds.

:::

:::

::: pf-step

Since \(f\) has no zeros,
\[
g(z)=\frac1{f(z)}
\]
is entire.


::: pf-proof

The reciprocal of a nowhere-zero holomorphic function is holomorphic.

:::

:::

::: pf-step

On \(\Omega\),
\[
\boxed{|g(z)|>1}.
\]


::: pf-proof

By definition of \(U\),
\[
|f(z)|<1
\]
for \(z\in\Omega\), and \(f(z)\ne0\). Taking reciprocals gives
\[
|g(z)|=\frac1{|f(z)|}>1.
\]

:::

:::

::: pf-step

On \(\partial\Omega\),
\[
\boxed{|g(z)|=1}.
\]


::: pf-proof

Use step <1>4:
\[
|g(z)|=\frac1{|f(z)|}=1.
\]

:::

:::

::: pf-step

Since \(\Omega\) is bounded, \(\overline\Omega\) is compact.


::: pf-proof

The closure is closed and bounded in \(\mathbb C\cong\mathbb R^2\). By Heine--Borel, it is compact.

:::

:::

::: pf-step

The continuous function \(|g|\) attains a maximum on \(\overline\Omega\).


::: pf-proof

Apply the extreme-value theorem to the compact set from step <1>8.

:::

:::

::: pf-step

This maximum is strictly greater than \(1\).


::: pf-proof

Every point of \(\Omega\) satisfies
\[
|g|>1
\]
by step <1>6.

:::

:::

::: pf-step

No boundary point can attain that maximum.


::: pf-proof

By step <1>7, every boundary point has modulus exactly \(1\), while the maximum is \(>1\) by step <1>10.

:::

:::

::: pf-step

Hence \(|g|\) attains its maximum at an interior point of \(\Omega\).


::: pf-proof

The maximum is attained somewhere in \(\overline\Omega\) by step <1>9, and step <1>11 excludes the boundary.

:::

:::

::: pf-step

By the maximum modulus principle,
\[
\boxed{
g\text{ is constant on }\Omega}.
\]


::: pf-proof

A holomorphic function on a connected open set that attains a modulus maximum at an interior point is constant.

:::

:::

::: pf-step

By the identity theorem, \(g\) is constant on all of \(\mathbb C\).


::: pf-proof

The entire function \(g\) agrees with a constant function on the nonempty open set \(\Omega\), so the identity theorem extends that equality to the connected domain \(\mathbb C\).

:::

:::

::: pf-step

Hence \(f=1/g\) is also constant on \(\mathbb C\).


::: pf-proof

The constant value of \(g\) is nonzero because \(g=1/f\).

:::

:::

::: pf-step

This contradicts the existence of the boundary \(\partial\Omega\) with
\[
|f|=1
\]
while
\[
|f|<1
\]
throughout \(\Omega\).


::: pf-proof

If \(f\) were constant, its modulus could not be both \(<1\) on \(\Omega\) and equal to \(1\) on \(\partial\Omega\).

:::

:::

::: pf-step

Therefore no connected component of \(U\) can be bounded.


::: pf-proof

The assumption of a bounded component led to the contradiction in step <1>16.

:::

:::

::: pf-step

Thus
\[
\boxed{
\text{every connected component of }
\{z:|f(z)|<1\}
\text{ is unbounded}.}
\]


::: pf-proof

This is step <1>17.

:::

:::

::: pf-qed

Step <1>18 is the required conclusion.

:::

:::
