---
schema: qual/card@1
id: P-WESTOP12-4
kind: problem
title: CW structures on $\mathbb{RP}^2$ and $\mathbb{CP}^4$ and the homology of $\mathbb{CP}^4$
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. Define a CW complex.
2. Give CW-complex structures on $\mathbb{RP}^2$ and $\mathbb{CP}^4$.
3. Using the CW structure from part 2, compute the homology of $\mathbb{CP}^4$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A **CW complex** is a Hausdorff space
\[
X
\]
built inductively from skeleta
\[
X^0
\subseteq
X^1
\subseteq
X^2
\subseteq
\cdots
\]
as follows.


::: pf-proof

The $0$-skeleton
\[
X^0
\]
is a discrete set of points.

For each
\[
n\ge1,
\]
the $n$-skeleton is obtained from
\[
X^{n-1}
\]
by attaching a collection of $n$-disks
\[
D^n_\alpha
\]
along continuous attaching maps
\[
\varphi_\alpha:
S^{n-1}
\to
X^{n-1}.
\]
Thus
\[
X^n
\cong
X^{n-1}
\cup_{\{\varphi_\alpha\}}
\bigsqcup_\alpha D^n_\alpha.
\]

The space satisfies:

- **closure-finiteness**: the closure of each cell meets only finitely many
  cells;
- **weak topology**: a subset
  \[
  A\subseteq X
  \]
  is closed iff its intersection with the closure of every cell is closed.

The open cells are the images of the interiors of the attached disks.

:::

:::

::: {.pf-step #s1-2}

The projective plane
\[
\mathbb{RP}^2
\]
has a CW structure with exactly one cell in each dimension
\[
0,1,2.
\]


::: pf-proof

Use the filtration
\[
\mathbb{RP}^0
\subset
\mathbb{RP}^1
\subset
\mathbb{RP}^2.
\]

The space
\[
\mathbb{RP}^0
\]
is a point, giving one $0$-cell.

The difference
\[
\mathbb{RP}^1
\setminus
\mathbb{RP}^0
\]
is an open $1$-cell, so one $1$-cell is attached.
Indeed,
\[
\mathbb{RP}^1
\cong
S^1.
\]

Finally,
\[
\mathbb{RP}^2
\setminus
\mathbb{RP}^1
\]
is an open $2$-cell.
Equivalently,
\[
\mathbb{RP}^2
\]
is obtained from a closed disk
\[
D^2
\]
by identifying antipodal boundary points.
Thus the $2$-cell is attached to
\[
\mathbb{RP}^1\cong S^1
\]
by the double covering
\[
S^1\to S^1,
\qquad
z\mapsto z^2,
\]
which has degree $2$.

:::

:::

::: {.pf-step #s1-3}

The complex projective space
\[
\mathbb{CP}^4
\]
has one cell in each even dimension
\[
0,2,4,6,8
\]
and no odd-dimensional cells.


::: pf-proof

Use the standard filtration
\[
\mathbb{CP}^0
\subset
\mathbb{CP}^1
\subset
\mathbb{CP}^2
\subset
\mathbb{CP}^3
\subset
\mathbb{CP}^4.
\]

For each
\[
k=0,1,2,3,4,
\]
the difference
\[
\mathbb{CP}^k
\setminus
\mathbb{CP}^{k-1}
\]
is homeomorphic to
\[
\CC^k
\cong
\RR^{2k}.
\]
Indeed, on the chart where the last homogeneous coordinate is nonzero,
normalize it to $1$:
\[
[z_0:\cdots:z_{k-1}:1]
\longleftrightarrow
(z_0,\dots,z_{k-1})
\in
\CC^k.
\]
Thus exactly one new open cell of real dimension
\[
2k
\]
appears at each stage.

:::

:::

::: {.pf-step #s1-4}

Therefore the cellular chain groups of
\[
\mathbb{CP}^4
\]
are
\[
C_n^{\mathrm{cell}}
(\mathbb{CP}^4)
\cong
\begin{cases}
\ZZ,
&n=0,2,4,6,8,\\
0,
&\text{otherwise}.
\end{cases}
\]


::: pf-proof

The cellular chain group in degree $n$ is free abelian on the $n$-cells.
Step [](#s1-3){.pf-ref} gives exactly one cell in each listed even degree and none in the
odd degrees.

:::

:::

::: {.pf-step #s1-5}

Every cellular boundary map for
\[
\mathbb{CP}^4
\]
is zero.


::: pf-proof

The cellular differential has degree $-1$:
\[
d_n:
C_n^{\mathrm{cell}}
\to
C_{n-1}^{\mathrm{cell}}.
\]

If
\[
n
\]
is even, then
\[
C_{n-1}^{\mathrm{cell}}=0.
\]
If
\[
n
\]
is odd, then
\[
C_n^{\mathrm{cell}}=0.
\]
Thus in every degree the source or target is zero, so
\[
d_n=0.
\]

:::

:::

::: {.pf-step #s1-6}

Hence the cellular homology is
\[
H_n(\mathbb{CP}^4;\ZZ)
\cong
C_n^{\mathrm{cell}}(\mathbb{CP}^4).
\]


::: pf-proof

Because every differential is zero,
\[
\ker d_n
=
C_n^{\mathrm{cell}}
\]
and
\[
\operatorname{im}d_{n+1}
=
0.
\]
Therefore
\[
H_n
=
\ker d_n/
\operatorname{im}d_{n+1}
\cong
C_n^{\mathrm{cell}}.
\]

:::

:::

::: {.pf-step #s1-7}

Thus
\[
\boxed{
H_n(\mathbb{CP}^4;\ZZ)
\cong
\begin{cases}
\ZZ,
&n=0,2,4,6,8,\\
0,
&\text{otherwise}.
\end{cases}
}
\]


::: pf-proof

Combine steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} defines a CW complex.
Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} give the requested CW structures.
Step [](#s1-7){.pf-ref} computes the homology of
\[
\mathbb{CP}^4.
\]

:::

:::

:::
