---
schema: qual/card@1
id: P-AZOFF-I09
kind: problem
title: Reflection principle for functions on the closed upper half-disk
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Schwarz lemma and reflection principle, Problem 9, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-corrected
  by: chatgpt
  date: 2026-09-21
  note: >-
    The retained PDF prints f:S→C. The extracted card had lost the arrow;
    the statement now restores it.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Defined the lower-half-disk values by conjugate reflection
    F(z)=conjugate(f(conjugate(z))). The real boundary values make the two
    formulas agree on the diameter, and the standard Schwarz reflection
    principle gives a holomorphic function on the whole unit disk.
---

::: {.problem}
[April 1999 Problem $\# 7 ]$ Let $S : = \{ z \in \mathbb { D } : \operatorname { I m } ( z ) \geq 0 \}$ . Suppose $f : S \to \mathbb { C }$ is continuous on S, real on $S \cap \mathbb { R }$ , and holomorphic on the interior of S. Prove that f is the restriction of a holomorphic function on the open unit disk.
:::

::: {.solution}
Define $F:\DD\to\CC$ by
$$
F(z)
=
\begin{cases}
f(z),&\operatorname{Im}z\geq0,\\
\overline{f(\bar z)},&\operatorname{Im}z<0.
\end{cases}
$$

<1>1. The two formulas defining $F$ agree on the real diameter
$(-1,1)$.

::: {.proof}
If $x\in(-1,1)$ is real, then $\bar x=x$. Since $f$ is real-valued on
$S\cap\RR$,
$$
\overline{f(\bar x)}
=
\overline{f(x)}
=
f(x).
$$
Thus the reflected lower-half-disk formula has the same boundary value as
the upper-half-disk formula.
:::

<1>2. The function $F$ is continuous on $\DD$.

::: {.proof}
On the open upper half-disk and the open lower half-disk, continuity follows
from continuity of $f$ and of conjugation. Along the real diameter, step
<1>1 shows that the two formulas have the same value, and the continuity of
$f$ on $S$ makes both one-sided limits equal to that value. Hence $F$ is
continuous everywhere in $\DD$.
:::

<1>3. The function $F$ is holomorphic on the open upper and lower
half-disks.

::: {.proof}
It equals $f$ on the open upper half-disk, where $f$ is holomorphic. If
$z_0$ lies in the open lower half-disk, then $\bar z_0$ lies in the open
upper half-disk. Writing the local power series
$$
f(w)=\sum_{n=0}^{\infty}a_n(w-\bar z_0)^n
$$
near $\bar z_0$ gives
$$
\overline{f(\bar z)}
=
\sum_{n=0}^{\infty}\bar a_n(z-z_0)^n
$$
near $z_0$. Hence the reflected formula is holomorphic there.
:::

<1>4. The function $F$ is holomorphic across the real diameter.

::: {.proof}
Steps <1>1--<1>3 give exactly the hypotheses of the Schwarz reflection
principle across the real axis: the upper-half-disk function is holomorphic,
extends continuously to the real diameter, and is real-valued there.
Therefore its reflected extension $F$ is holomorphic through every point of
$(-1,1)$.
:::

<1>5. The function $F$ is holomorphic on the entire open unit disk and
restricts to $f$ on $S$.

::: {.proof}
Step <1>3 gives holomorphy away from the real diameter, and step <1>4 gives
holomorphy on the diameter. Hence $F$ is holomorphic on $\DD$. By its
definition, $F=f$ wherever $\operatorname{Im}z\geq0$, which is precisely
$S$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required holomorphic extension.
:::
:::
