---
schema: qual/card@1
id: P-AZOFF-H05
kind: problem
title: Solutions of $e^z=az^n$ in the unit disk
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Rouché’s theorem, Problem 5, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    On the unit circle, |exp(z)| lies between e^(-1) and e. For |a|>e,
    -a z^n dominates exp(z), so Rouché gives n zeros. For |a|<e^(-1),
    exp(z) dominates a z^n, so the difference has the same zero count as the
    exponential, namely zero.
---

::: {.problem}
Let $n \in \NN$. Prove that the equation $\exp(z) = a z^n$ has $n$ solutions in the open unit disk $D$ if $\abs{a} > e$ and none if $\abs{a} < \frac{1}{e}$.
:::

::: {.solution}
Set
$$
F(z)=e^z-az^n.
$$

<1>1. On the unit circle,
$$
e^{-1}
\leq
\abs{e^z}
\leq
e.
$$

::: {.proof}
If $\abs{z}=1$, then
$$
-1\leq\operatorname{Re}z\leq1.
$$
Since
$$
\abs{e^z}=e^{\operatorname{Re}z},
$$
the displayed bounds follow.
:::

<1>2. If $\abs{a}>e$, then on $\abs{z}=1$,
$$
\abs{e^z}
<
\abs{-az^n}.
$$

::: {.proof}
By step <1>1,
$$
\abs{e^z}\leq e.
$$
On the unit circle,
$$
\abs{-az^n}=\abs{a}>e.
$$
:::

<1>3. If $\abs{a}>e$, then the equation
$$
e^z=az^n
$$
has exactly $n$ solutions in the open unit disk, counting multiplicity.

::: {.proof}
Write
$$
F(z)=-az^n+e^z.
$$
By step <1>2 and Rouché's theorem, $F$ and $-az^n$ have the same number of
zeros in $\abs{z}<1$. The latter has exactly $n$ zeros there, all at
$z=0$ counted with multiplicity.
:::

<1>4. If $\abs{a}<e^{-1}$, then on $\abs{z}=1$,
$$
\abs{az^n}
<
\abs{e^z}.
$$

::: {.proof}
On the unit circle,
$$
\abs{az^n}=\abs{a}<e^{-1}.
$$
Step <1>1 gives
$$
\abs{e^z}\geq e^{-1}.
$$
Thus the inequality is strict.
:::

<1>5. If $\abs{a}<e^{-1}$, then the equation
$$
e^z=az^n
$$
has no solutions in the open unit disk.

::: {.proof}
By step <1>4 and Rouché's theorem, $F=e^z-az^n$ and $e^z$ have the same
number of zeros in $\abs{z}<1$. The exponential function has no zeros
anywhere in $\CC$, so this number is zero.
:::

<1>6. Therefore the equation has exactly $n$ solutions in the unit disk
when $\abs{a}>e$, and none when $\abs{a}<e^{-1}$.

::: {.proof}
This combines steps <1>3 and <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
