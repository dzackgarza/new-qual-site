---
schema: qual/card@1
id: P-JHUMAY12CA3
kind: problem
title: Removable singularity when real part is bounded below
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the punctured unit disk and lower bound on the real part with May 2012 problem 3 in the retained JHU extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the bounded fractional transform, exclusion of a boundary value at its removable extension, and nonvanishing of the inverse transform's denominator at the puncture."
---

::: {.problem}
Suppose $f$ is holomorphic on $U \coloneqq D(0,1) \setminus \{0\}$.
Assume that the real part $\operatorname{Re}(f)$ is bounded from below on $U$.
Prove that $z = 0$ is a removable singularity.
:::

::: {.solution}
Choose $m\in\RR$ with $\operatorname{Re}f(z)\geq m$
on the punctured disk $U$.

<1>1. A fractional transform of $f$ is bounded and holomorphic on $U$.

::: {.proof}
Let $F=f-m+1$, so $\operatorname{Re}F\geq1$, and put
$$
q(z)=\frac{F(z)-1}{F(z)+1}.
$$
Since $\operatorname{Re}(F+1)\geq2$, its denominator
never vanishes. Moreover,
$$
\abs{F+1}^2-\abs{F-1}^2=4\operatorname{Re}F\geq4>0,
$$
so $\abs{q}<1$ throughout $U$. [[D-BQLJV|Riemann's removable singularity theorem]]
extends $q$ holomorphically to the full unit disk; write $Q$ for this extension.
Continuity gives $\abs{Q(0)}\leq1$.
:::

<1>2. The inverse transform extends $f$ across zero.

::: {.proof}
In fact $\abs{Q(0)}<1$. Otherwise $Q$ would attain its
maximum modulus one at an interior point of the disk.
The [[T-BYNL5|maximum modulus principle]] would make $Q$ constant
of modulus one, contradicting $\abs{q(z)}<1$ on $U$.
Together with the original strict bound, this gives
$\abs{Q}<1$ everywhere on the full disk. Hence $1-Q$ is
nowhere zero there, and
$$
\widetilde f(z)=m+\frac{2Q(z)}{1-Q(z)}
$$
is holomorphic on that disk. On $U$, solving
$q=(F-1)/(F+1)$ gives $F=(1+q)/(1-q)$ and consequently
$f=m+2q/(1-q)$. Thus $\widetilde f=f$ on $U$.
The displayed function is a holomorphic extension of
$f$ through zero, proving removability.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 constructs the required holomorphic extension across zero.
:::
:::
