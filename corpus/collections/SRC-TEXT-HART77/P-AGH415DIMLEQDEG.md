---
schema: qual/card@1
id: P-AGH415DIMLEQDEG
kind: problem
title: $\dim \abs{D} \leq \deg D$ for an effective divisor, with equality iff $D=0$ or $g=0$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Linear Systems
  - Riemann-Roch
  - Genus
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Hartshorne IV.1.5 and independently derived the proof before comparing it with the retained solution transcription; cross-checked the linear-series and genus-zero bounds against Stacks Tags 0CCS and 0C6T.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
For an effective divisor $D$ on a curve $X$ of genus $g$, show that $\dim \abs{D} \leq \deg D$.
Furthermore, equality holds if and only if $D=0$ or $g=0$.
:::

::: {.solution}
Write
$$
d=\deg D,
\qquad
\ell(D)=h^0(X,\mco_X(D)).
$$
Since $D$ is effective, $d\ge0$ and
$$
\dim\abs{D}=\ell(D)-1.
$$


<1>1. The divisor sequence gives
$$
0\to\mco_X\to\mco_X(D)\to\mco_X(D)|_D\to0,
$$
and
$$
h^0(D,\mco_X(D)|_D)=d.
$$

::: {.proof}
The first map is multiplication by the canonical section with zero divisor
$D$. The finite scheme $D$ has length $d$. Since
$\mco_X(D)|_D$ is locally free of rank one on $D$, it also has length
$d$, so its space of global sections has dimension $d$.
:::

<1>2. One has $\dim\abs{D}\le\deg D$.

::: {.proof}
Global sections of step <1>1 give
$$
0\to H^0(X,\mco_X)\to H^0(X,\mco_X(D))
\to H^0(D,\mco_X(D)|_D).
$$
Since $h^0(X,\mco_X)=1$, step <1>1 gives
$\ell(D)\le d+1$. Therefore
$$
\dim\abs{D}=\ell(D)-1\le d=\deg D.
$$
:::

<1>3. If $D=0$, then equality holds.

::: {.proof}
Here $\ell(0)=h^0(X,\mco_X)=1$, so
$$
\dim\abs{0}=0=\deg0.
$$
:::

<1>4. If $g=0$, then equality holds for every effective $D$.

::: {.proof}
The case $D=0$ is step <1>3. If $d>0$, Riemann--Roch gives
$$
\ell(D)-\ell(K-D)=d+1.
$$
Now $\deg K=-2$, so $\deg(K-D)<0$ and hence
$\ell(K-D)=0$. Thus $\ell(D)=d+1$, and therefore
$$
\dim\abs{D}=d=\deg D.
$$
:::

<1>5. Conversely, suppose equality holds and $D\ne0$. Then
$\ell(K-D)=g$.

::: {.proof}
Equality means $\ell(D)=d+1$. Riemann--Roch gives
$$
\ell(D)-\ell(K-D)=d+1-g.
$$
Hence $\ell(K-D)=g$. It also gives $\ell(K)=g$.
:::

<1>6. Choose a point $P$ in the support of $D$.

::: {.proof}
Because $D-P$ is effective, the section spaces for $K-D$, $K-P$, and $K$ are nested.
The first and third have dimension $g$ by step <1>5, so the middle one also has dimension $g$. Riemann--Roch for the degree-one divisor $P$ then gives
$$
\ell(P)=2.
$$
:::

<1>7. The equality $\ell(P)=2$ forces $X\cong\PP^1$, hence $g=0$.

::: {.proof}
Constants give one section of $\mco_X(P)$, so a second linearly independent section gives a nonconstant rational function
$$
f\in H^0(X,\mco_X(P)).
$$
Its pole divisor is bounded by $P$. Since every global regular function on the proper integral curve $X$ is constant, $f$ must actually have pole divisor exactly $P$.

Thus $f$ defines a finite morphism
$$
f:X\longrightarrow\PP^1
$$
whose degree is the degree of its polar divisor, namely $1$. A finite degree-one morphism between integral smooth projective curves is birational, and since $\PP^1$ is normal it is an isomorphism. Hence $X\cong\PP^1$ and $g=0$.
:::

<1>8. Equality holds if and only if $D=0$ or $g=0$.

::: {.proof}
Steps <1>3--<1>4 prove the two sufficient cases. Steps <1>5--<1>7 show that equality with $D\ne0$ forces $g=0$.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>2 proves the inequality and step <1>8 characterizes equality.
:::
:::
