---
schema: qual/card@1
id: P-AZOFF-F03
kind: problem
title: Laurent expansions of $\frac{z+1}{z(z-1)^2}$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Laurent expansions and singularities, Problem 3, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used the partial-fraction decomposition
    1/z-1/(z-1)+2/(z-1)^2 and the differentiated geometric series to expand
    on both maximal annuli about 0. Recentered with w=z-1 and expanded
    1/(1+w) on both maximal annuli about 1.
---

::: {.problem}
Find the Laurent expansions of $\frac { z + 1 } { z ( z - 1 ) ^ { 2 } }$ about

a) $z = 0$

b) $\mathbf { Z } { = } 1$

Hint: Recall that power series can be differentiated.
:::

::: {.solution}
Set
$$
F(z)=\frac{z+1}{z(z-1)^2}.
$$

<1>1. One has the partial-fraction decomposition
$$
F(z)
=
\frac1z
-\frac1{z-1}
+\frac2{(z-1)^2}.
$$

::: {.proof}
Multiplying the proposed identity by $z(z-1)^2$ gives
$$
(z-1)^2-z(z-1)+2z
=
z+1.
$$
Thus the two rational functions agree.
:::

<1>2. About $z=0$, on $0<\abs{z}<1$,
$$
\boxed{
F(z)
=
\frac1z
+\sum_{n=0}^{\infty}(2n+3)z^n.
}
$$

::: {.proof}
For $\abs{z}<1$,
$$
\frac1{1-z}
=
\sum_{n=0}^{\infty}z^n.
$$
Differentiating term by term gives
$$
\frac1{(1-z)^2}
=
\sum_{n=0}^{\infty}(n+1)z^n.
$$
Since
$$
-\frac1{z-1}=\frac1{1-z},
\qquad
\frac2{(z-1)^2}=\frac2{(1-z)^2},
$$
step <1>1 becomes
$$
\begin{aligned}
F(z)
&=
\frac1z
+\sum_{n=0}^{\infty}z^n
+2\sum_{n=0}^{\infty}(n+1)z^n\\
&=
\frac1z
+\sum_{n=0}^{\infty}(2n+3)z^n.
\end{aligned}
$$
The pole at the center excludes $z=0$, so this is valid on
$0<\abs{z}<1$.
:::

<1>3. About $z=0$, on $\abs{z}>1$,
$$
\boxed{
F(z)
=
\sum_{k=2}^{\infty}(2k-3)z^{-k}.
}
$$

::: {.proof}
For $\abs{z}>1$,
$$
-\frac1{z-1}
=
-\frac1z\frac1{1-z^{-1}}
=
-\sum_{n=0}^{\infty}z^{-n-1},
$$
and differentiation of the geometric series gives
$$
\frac2{(z-1)^2}
=
\frac2{z^2}\frac1{(1-z^{-1})^2}
=
2\sum_{n=0}^{\infty}(n+1)z^{-n-2}.
$$
Adding these to $1/z$ as in step <1>1, the $z^{-1}$ terms cancel. For
$k\geq2$, the coefficient of $z^{-k}$ is
$$
-1+2(k-1)=2k-3.
$$
This yields the displayed Laurent series.
:::

<1>4. About $z=1$, write
$$
w=z-1.
$$
On $0<\abs{w}<1$,
$$
\boxed{
F(1+w)
=
\frac2{w^2}
-\frac1w
+\sum_{n=0}^{\infty}(-1)^n w^n.
}
$$

::: {.proof}
Substituting $z=1+w$ into step <1>1 gives
$$
F(1+w)
=
\frac1{1+w}
-\frac1w
+\frac2{w^2}.
$$
For $\abs{w}<1$,
$$
\frac1{1+w}
=
\sum_{n=0}^{\infty}(-1)^n w^n.
$$
Substitution proves the formula.
:::

<1>5. About $z=1$, on $\abs{w}>1$,
$$
\boxed{
F(1+w)
=
-\frac1w
+\frac2{w^2}
+\sum_{n=0}^{\infty}(-1)^n w^{-n-1}.
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
Insert this into the recentered expression from step <1>4.
:::

<1>6. Steps <1>2--<1>5 give all Laurent expansions on the maximal annuli
about $0$ and $1$.

::: {.proof}
The only singularities of $F$ are $0$ and $1$. Their mutual distance is
$1$. Hence the maximal annuli centered at $0$ are
$$
0<\abs{z}<1
\qquad\text{and}\qquad
1<\abs{z}<\infty,
$$
while those centered at $1$ are
$$
0<\abs{z-1}<1
\qquad\text{and}\qquad
1<\abs{z-1}<\infty.
$$
The preceding four steps supply one Laurent series on each such annulus.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 gives the complete collection of requested expansions.
:::
:::
