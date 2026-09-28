---
schema: qual/card@1
id: P-AZOFF-F01
kind: problem
title: Laurent expansions of $\frac{z+1}{z(z-1)}$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Laurent expansions and singularities, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Decomposed the rational function as -1/z+2/(z-1) and expanded the
    nonsingular factor geometrically on each maximal annulus about 0 and 1.
    Both the inner punctured disks and the exterior annuli are included.
---

::: {.problem}
Find the Laurent expansions of $\textstyle { \frac { z + 1 } { z ( z - 1 ) } }$ about

a) $z = 0$

b) $z = 1$
:::

::: {.solution}
Set
$$
F(z)=\frac{z+1}{z(z-1)}.
$$

<1>1. The partial-fraction decomposition is
$$
F(z)=-\frac1z+\frac2{z-1}.
$$

::: {.proof}
One has
$$
-\frac1z+\frac2{z-1}
=
\frac{-(z-1)+2z}{z(z-1)}
=
\frac{z+1}{z(z-1)}.
$$
:::

<1>2. About $z=0$, on the annulus $0<\abs{z}<1$,
$$
\boxed{
F(z)
=
-\frac1z
-2\sum_{n=0}^{\infty}z^n.
}
$$

::: {.proof}
For $\abs{z}<1$,
$$
\frac2{z-1}
=
-\frac2{1-z}
=
-2\sum_{n=0}^{\infty}z^n.
$$
Substitute this into step <1>1. The factor $1/z$ requires $z\neq0$, so the
resulting Laurent expansion is valid on $0<\abs{z}<1$.
:::

<1>3. About $z=0$, on the annulus $\abs{z}>1$,
$$
\boxed{
F(z)
=
-\frac1z
+2\sum_{n=0}^{\infty}z^{-n-1}.
}
$$

::: {.proof}
For $\abs{z}>1$,
$$
\frac2{z-1}
=
\frac2z\frac1{1-z^{-1}}
=
2\sum_{n=0}^{\infty}z^{-n-1}.
$$
Substitution into step <1>1 gives the displayed expansion.
:::

<1>4. About $z=1$, write
$$
w=z-1.
$$
On the annulus $0<\abs{w}<1$,
$$
\boxed{
F(1+w)
=
\frac2w
-\sum_{n=0}^{\infty}(-1)^n w^n.
}
$$

::: {.proof}
Step <1>1 becomes
$$
F(1+w)
=
-\frac1{1+w}
+\frac2w.
$$
For $\abs{w}<1$,
$$
\frac1{1+w}
=
\sum_{n=0}^{\infty}(-1)^n w^n.
$$
Substitution yields the displayed Laurent series, valid away from the center
$w=0$.
:::

<1>5. About $z=1$, on the annulus $\abs{w}>1$,
$$
\boxed{
F(1+w)
=
\frac2w
-\sum_{n=0}^{\infty}(-1)^n w^{-n-1}.
}
$$

::: {.proof}
For $\abs{w}>1$,
$$
\frac1{1+w}
=
\frac1w\frac1{1+w^{-1}}
=
\sum_{n=0}^{\infty}(-1)^n w^{-n-1}.
$$
Substitution into
$$
F(1+w)=-\frac1{1+w}+\frac2w
$$
gives the displayed series.
:::

<1>6. The expansions in steps <1>2--<1>5 exhaust the Laurent expansions on
the maximal annuli centered at $0$ and $1$.

::: {.proof}
The only singularities of $F$ are at $0$ and $1$. About the center $0$, the
other singularity lies at radius $1$, producing the maximal annuli
$$
0<\abs{z}<1
\qquad\text{and}\qquad
1<\abs{z}<\infty.
$$
About the center $1$, the other singularity $0$ again lies at distance $1$,
producing
$$
0<\abs{z-1}<1
\qquad\text{and}\qquad
1<\abs{z-1}<\infty.
$$
Steps <1>2--<1>5 give one Laurent series on each of these maximal annuli.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>2--<1>6 give all requested Laurent expansions about both centers.
:::
:::
