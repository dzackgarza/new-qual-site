---
schema: qual/card@1
id: P-AGXVARSINGCLOSED
kind: problem
title: The singular locus is a proper Zariski closed subset
classification:
  areas:
  - algebraic-geometry
  topics:
  - Singular Locus
  - Smoothness
  - Zariski Topology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Definitions 6.1 and Proposition 6.4 in the recorded source.
    The proposition states that the singular locus of an affine variety is
    proper Zariski closed and that the regular locus is dense open.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Restored the source's affine-variety context and standing algebraically
    closed characteristic-zero field on the standalone card.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Described the singular locus by the rank-(n-d) Jacobian minors, then used
    the conormal sequence over the function field and separability in
    characteristic zero to show that the generic Jacobian rank is n-d.
    Therefore a nonempty distinguished open consists of smooth points.
---

::: {.problem}
Let
$$
X\subseteq\AA^n_k
$$
be an affine variety of dimension $d$ over an algebraically closed field
$k$ of characteristic zero. Show that the singular points of $X$ form a
proper Zariski-closed subset. Deduce that the smooth points form a dense
Zariski-open subset.
:::

::: {.solution}
Choose generators
$$
I(X)=(f_1,\ldots,f_m)
$$
and put
$$
c=n-d.
$$
Let
$$
J
=
\left(
\frac{\partial f_i}{\partial x_j}
\right)_{i,j}
$$
be the Jacobian matrix.

::: pf

::: {.pf-step #sing-locus-minors}
The singular locus is the common zero set on $X$ of all
$c\times c$ minors of $J$.

::: pf-proof
If $c=0$, the Jacobian criterion says that every point is smooth, so the
singular locus is empty and the assertion is immediate.

Assume $c>0$. By the Jacobian criterion [[PR-MORJAC]], a point
$$
p\in X
$$
is smooth exactly when
$$
\rank J(p)=c.
$$
For points of the pure $d$-dimensional variety $X$, one has
$$
\rank J(p)\leq c.
$$
Indeed,
$$
\dim T_pX
=
n-\rank J(p)
\geq
\dim_pX
=
d.
$$
Hence $p$ is singular exactly when
$$
\rank J(p)<c,
$$
which is equivalent to the vanishing at $p$ of every $c\times c$ minor of
$J$.

Therefore
$$
\operatorname{Sing}(X)
$$
is the intersection of $X$ with the zero loci of those minors, hence is
Zariski closed.
:::

:::

::: {.pf-step #jacobian-rank-generic}
Over the function field
$$
K=k(X),
$$
the Jacobian matrix has rank exactly
$$
c=n-d.
$$

::: pf-proof
Let
$$
A=k[X]
=
k[x_1,\ldots,x_n]/I(X).
$$
Since $X$ is irreducible, $A$ is a domain and
$$
K=\Frac A.
$$

The conormal sequence for
$$
A=k[x_1,\ldots,x_n]/I(X)
$$
becomes, after tensoring with $K$,
$$
(I/I^2)\tensor_A K
\longrightarrow
K^n
\longrightarrow
\Omega_{K/k}
\longrightarrow
0.
$$
The first map sends a defining equation $f$ to
$$
\left(
\frac{\partial f}{\partial x_1},
\ldots,
\frac{\partial f}{\partial x_n}
\right),
$$
so its image is the row space of $J$ over $K$.

The extension $K/k$ is finitely generated of transcendence degree
$$
\trdeg_kK=d.
$$
Because $\characteristic k=0$, it is separably generated, and therefore
$$
\dim_K\Omega_{K/k}=d.
$$
Exactness gives
$$
\rank_KJ
=
n-\dim_K\Omega_{K/k}
=
n-d
=
c.
$$
:::

:::

::: {.pf-step #minor-nonzero-regular}
At least one $c\times c$ minor of $J$ is a nonzero regular function
on $X$.

::: pf-proof
By step [](#jacobian-rank-generic){.pf-ref}, the rank of $J$ over $K$ is $c$. Hence some $c\times c$
minor $\Delta$ has nonzero determinant in $K$.

The entries of $J$ lie in $A$, so $\Delta\in A$. Its image in the fraction
field is nonzero, hence
$$
\Delta\ne0
$$
in the domain $A$.
:::

:::

::: {.pf-step #smooth-locus-contains-dx}
The smooth locus contains the nonempty distinguished open
$$
D_X(\Delta).
$$

::: pf-proof
Since $\Delta\ne0$ in the domain $A$, the distinguished open
$$
D_X(\Delta)
$$
is nonempty.

For every
$$
p\in D_X(\Delta),
$$
the chosen $c\times c$ minor is nonzero at $p$, so
$$
\rank J(p)\geq c.
$$
Step [](#sing-locus-minors){.pf-ref} gives the opposite inequality
$$
\rank J(p)\leq c.
$$
Thus
$$
\rank J(p)=c,
$$
and the Jacobian criterion makes $p$ smooth.
:::

:::

::: {.pf-step #sing-locus-proper-closed}
The singular locus is a proper Zariski-closed subset of $X$.

::: pf-proof
Step [](#sing-locus-minors){.pf-ref} proves closedness. Step [](#smooth-locus-contains-dx){.pf-ref} produces a nonempty open subset
consisting entirely of smooth points, so
$$
\operatorname{Sing}(X)\ne X.
$$
Hence the singular locus is proper closed.
:::

:::

::: {.pf-step #smooth-locus-dense-open}
The smooth locus
$$
X_{\reg}
=
X\sm\operatorname{Sing}(X)
$$
is dense Zariski open.

::: pf-proof
By step [](#sing-locus-proper-closed){.pf-ref}, the complement of the singular locus is a nonempty open subset
of the irreducible variety $X$. Every nonempty open subset of an irreducible
space is dense. Therefore
$$
\boxed{X_{\reg}\text{ is dense and Zariski open}.}
$$
:::

:::

::: pf-qed
Steps [](#sing-locus-minors){.pf-ref}, [](#jacobian-rank-generic){.pf-ref}, [](#minor-nonzero-regular){.pf-ref}, [](#smooth-locus-contains-dx){.pf-ref} and [](#sing-locus-proper-closed){.pf-ref} prove that the singular locus is proper Zariski closed, and
step [](#smooth-locus-dense-open){.pf-ref} gives the dense-open smooth locus.
:::

:::

:::
