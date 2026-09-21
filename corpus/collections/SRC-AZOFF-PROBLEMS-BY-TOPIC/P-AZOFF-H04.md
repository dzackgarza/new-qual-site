---
schema: qual/card@1
id: P-AZOFF-H04
kind: problem
title: Roots of $z^7-4z^3-1$ in the unit disk
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Rouché’s theorem, Problem 4, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    On the unit circle compared z^7-4z^3-1 with -4z^3. The remaining part
    z^7-1 has modulus at most two, strictly less than four, so Rouché gives
    exactly three roots in the unit disk counting multiplicity.
---

::: {.problem}
How many roots does the equation $z ^ { 7 } - 4 z ^ { 3 } - 1 = 0$ have in the open disk $| z | < 1 \ \mathrm { ? }$
:::

::: {.solution}
Set
$$
p(z)=z^7-4z^3-1.
$$

<1>1. On the unit circle,
$$
\abs{z^7-1}
<
\abs{-4z^3}.
$$

::: {.proof}
If $\abs{z}=1$, then
$$
\abs{z^7-1}
\leq
\abs{z}^7+1
=
2,
$$
while
$$
\abs{-4z^3}
=
4\abs{z}^3
=
4.
$$
Hence the strict inequality holds.
:::

<1>2. The polynomial $p$ has exactly three zeros in the open unit disk,
counting multiplicity.

::: {.proof}
Write
$$
p(z)=-4z^3+(z^7-1).
$$
By step <1>1, Rouché's theorem implies that $p$ and $-4z^3$ have the same
number of zeros in $\abs{z}<1$, counting multiplicity. The polynomial
$-4z^3$ has exactly three zeros there, all at $z=0$ counted with
multiplicity.
:::

<1>3. The answer is
$$
\boxed{3}.
$$

::: {.proof}
This is step <1>2.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested number of roots.
:::
:::
