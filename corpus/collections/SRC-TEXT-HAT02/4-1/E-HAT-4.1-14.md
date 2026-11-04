---
schema: qual/card@1
id: E-HAT-4.1-14
kind: problem
title: "Homotopy equivalent skeleta"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 14; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Read against the book (AT.txt:17874-17875 for the statement, 17395-17397 for cellular approximation).
    Correct: cellular approximation makes f and g cellular, so they restrict to the n-skeleta; the
    homotopy gf ~ id restricted to X^n x I is a map of CW pairs already cellular on X^n x dI, so its
    relative form homotopes it rel the two ends to a cellular map, whose image lies in X^{n+1} = X^n
    because X^n x I has dimension n+1 and there are no (n+1)-cells. The same for f_n g_n, so the
    restrictions are homotopy inverses. The (n+1)-cell hypothesis is used exactly where it is needed.
    Not checked: nothing beyond the written argument.

---

::: {.problem}
Use cellular approximation to show that the $n$-skeleta of homotopy equivalent CW complexes without cells of dimension $n+1$ are also homotopy equivalent.
:::

::: {.solution}
Let $X$ and $Y$ be homotopy equivalent CW complexes, and suppose neither has cells of dimension $n+1$. Choose homotopy inverse maps
$$
f:X\to Y,
\qquad
g:Y\to X.
$$
By cellular approximation, replace $f$ and $g$ by cellular maps. Then
$$
f(X^n)\subset Y^n,
\qquad
g(Y^n)\subset X^n,
$$
so they restrict to maps
$$
f_n:X^n\to Y^n,
\qquad
g_n:Y^n\to X^n.
$$

We have homotopies
$$
gf\simeq\operatorname{id}_X,
\qquad
fg\simeq\operatorname{id}_Y.
$$
Restrict the first to $X^n\times I$. By cellular approximation for homotopies, relative to the two ends, it is homotopic to a cellular map
$$
X^n\times I\longrightarrow X.
$$
The product CW structure on $X^n\times I$ has dimension at most $n+1$, so a cellular homotopy has image in $X^{n+1}$. Since $X$ has no $(n+1)$-cells,
$$
X^{n+1}=X^n.
$$
Hence
$$
g_nf_n\simeq\operatorname{id}_{X^n}
$$
through maps into $X^n$. The same argument gives
$$
f_ng_n\simeq\operatorname{id}_{Y^n}.
$$
Therefore $f_n$ and $g_n$ are homotopy inverses, and
$$
\boxed{X^n\simeq Y^n.}
$$
:::
