---
schema: qual/card@1
id: P-AZOFF-H02
kind: problem
title: Two roots of $z^3+3z^2+bz+b^2$ in the unit disk
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Rouché’s theorem, Problem 2, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    On the unit circle compared f with 3z^2. The remaining terms have
    modulus at most 1+|b|+|b|^2<3, so Rouché gives the same zero count as
    3z^2, namely two counting multiplicity.
---

::: {.problem}
Assuming that $| b | < 1$ , show that $f ( z ) = z ^ { 3 } + 3 z ^ { 2 } + b z + b ^ { 2 }$ has exactly two roots (counting multiplicity) in $| z | < 1$
:::

::: {.solution}
<1>1. On the unit circle,
$$
\abs{z^3+bz+b^2}<3.
$$

::: {.proof}
If $\abs{z}=1$, then
$$
\begin{aligned}
\abs{z^3+bz+b^2}
&\leq
\abs{z}^3
+\abs{b}\abs{z}
+\abs{b}^2\\
&=
1+\abs{b}+\abs{b}^2.
\end{aligned}
$$
Since $\abs{b}<1$,
$$
1+\abs{b}+\abs{b}^2<3.
$$
:::

<1>2. On the unit circle,
$$
\abs{z^3+bz+b^2}
<
\abs{3z^2}.
$$

::: {.proof}
By step <1>1, the left-hand side is less than $3$. If $\abs{z}=1$, then
$$
\abs{3z^2}=3.
$$
:::

<1>3. The polynomial
$$
f(z)=z^3+3z^2+bz+b^2
$$
has exactly two zeros in $\abs{z}<1$, counting multiplicity.

::: {.proof}
Write
$$
f(z)=3z^2+(z^3+bz+b^2).
$$
Step <1>2 is the strict Rouché inequality on $\abs{z}=1$. Hence $f$ and
$3z^2$ have the same number of zeros in the unit disk, counting
multiplicity. The polynomial $3z^2$ has exactly two zeros there, both at
$z=0$ counted with multiplicity.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
