---
schema: qual/card@1
id: P-AGH3122HYPERCONST
kind: problem
title: Cohomology of a family of hypersurfaces of fixed degree is constant
classification:
  areas:
  - algebraic-geometry
  topics:
  - Semicontinuity
  - Hypersurfaces
  - Flat Families
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.12.2 and derived the cohomology directly from the degree-d hypersurface sequence.
    The calculation was then compared with an external solution and cross-checked against the projective-space
    cohomology formula in Stacks Project Tag 01XV.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $\ts{X_t}$ be a family of hypersurfaces of the same degree in $\PP_k^n$.
Show that for each $i$ the function $h^i(X_t, \mco_{X_t})$ is a constant function of $t$.
:::

::: {.solution}
Let $d$ be the common degree of the hypersurfaces.

<1>1. For every parameter value $t$, the hypersurface $X_t\subseteq\PP_k^n$
fits into an exact sequence
$$
0
\longrightarrow
\mco_{\PP^n}(-d)
\xrightarrow{\cdot F_t}
\mco_{\PP^n}
\longrightarrow
\mco_{X_t}
\longrightarrow0,
$$
where $F_t$ is a homogeneous equation of degree $d$ for $X_t$.

::: {.proof}
A hypersurface of degree $d$ is the effective Cartier divisor cut out by
one nonzero homogeneous form $F_t$ of degree $d$. Its ideal sheaf is
therefore
$$
\mci_{X_t}\cong\mco_{\PP^n}(-d),
$$
with inclusion into $\mco_{\PP^n}$ given by multiplication by $F_t$.
Taking the quotient gives the displayed sequence.
:::

<1>2. The cohomology groups of the two line bundles in step <1>1 depend only
on $n$ and $d$:
$$
H^q(\PP^n,\mco)=
\begin{cases}
k,&q=0,\\
0,&q>0,
\end{cases}
$$
and
$$
H^q(\PP^n,\mco(-d))=0
\qquad
(0<q<n).
$$
Moreover
$$
h^n(\PP^n,\mco(-d))
=
\begin{cases}
\binom{d-1}{n},&d\ge n+1,\\
0,&d\le n.
\end{cases}
$$

::: {.proof}
These are the standard cohomology formulas for twisting sheaves on
projective space, recorded in
[[T-IJW1K|the cohomology of $\mco_{\PP^n}(d)$]].
:::

<1>3. Assume $n\ge2$. Then for every $t$,
$$
h^0(X_t,\mco_{X_t})=1,
$$
$$
h^q(X_t,\mco_{X_t})=0
\qquad
(0<q<n-1),
$$
and
$$
h^{n-1}(X_t,\mco_{X_t})
=
\begin{cases}
\binom{d-1}{n},&d\ge n+1,\\
0,&d\le n,
\end{cases}
$$
and
$$
H^q(X_t,\mco_{X_t})=0
\qquad
(q\ge n).
$$

::: {.proof}
Apply cohomology to the exact sequence of step <1>1. Since
$$
H^0(\PP^n,\mco(-d))=0
$$
and, for $n\ge2$,
$$
H^1(\PP^n,\mco(-d))=0,
$$
the beginning of the long exact sequence gives
$$
H^0(X_t,\mco_{X_t})\cong k.
$$
For $0<q<n-1$, both neighbouring projective-space groups vanish by
step <1>2, so
$$
H^q(X_t,\mco_{X_t})=0.
$$
Finally the relevant tail is
$$
0
\longrightarrow
H^{n-1}(X_t,\mco_{X_t})
\longrightarrow
H^n(\PP^n,\mco(-d))
\longrightarrow
H^n(\PP^n,\mco)
=0.
$$
Thus
$$
H^{n-1}(X_t,\mco_{X_t})
\cong
H^n(\PP^n,\mco(-d)),
$$
whose dimension is the value in step <1>2. The same long exact sequence
gives $H^q(X_t,\mco_{X_t})=0$ for $q\ge n$. None of these dimensions
depends on $t$.
:::

<1>4. If $n=1$, then for every $t$,
$$
h^0(X_t,\mco_{X_t})=d
$$
and
$$
H^q(X_t,\mco_{X_t})=0
\qquad
(q>0).
$$

::: {.proof}
The long exact sequence of step <1>1 becomes
$$
0
\longrightarrow
k
\longrightarrow
H^0(X_t,\mco_{X_t})
\longrightarrow
H^1(\PP^1,\mco(-d))
\longrightarrow0,
$$
because $H^0(\PP^1,\mco(-d))=H^1(\PP^1,\mco)=0$.
By [[T-IJW1K|the projective-line case]],
$$
h^1(\PP^1,\mco(-d))=d-1
$$
for $d\ge1$. Hence
$$
h^0(X_t,\mco_{X_t})=1+(d-1)=d.
$$
A hypersurface in $\PP^1$ is zero-dimensional, so its higher coherent
cohomology vanishes.
:::

<1>5. For every $i$, the number
$$
h^i(X_t,\mco_{X_t})
$$
is independent of $t$.

::: {.proof}
For $n\ge2$, step <1>3 gives every cohomology dimension explicitly in
terms of $n$ and $d$. For $n=1$, step <1>4 does the same. If $n=0$, a
positive-degree hypersurface in $\PP^0$ is empty, so every cohomology group
is zero. Thus fixing $i$, the function of the parameter $t$ is constant.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
