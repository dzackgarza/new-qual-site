---
schema: qual/card@1
id: P-TZCW3
kind: problem
title: Fundamental theorem of algebra via Rouché's theorem and the maximum modulus
  principle
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Maximum Modulus Principle
  - Polynomials
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, which gives both proofs correctly. Added
    the reasons the steps need: that f and g are polynomials and so holomorphic on a neighbourhood of
    the closed disc, which is the hypothesis of Rouche's theorem on that disc; the triangle-inequality
    estimate |P(z)| >= |a_n| R^n / 2 on the circle, and its version for large |z| giving |P| -> infinity;
    and the argument that the maximum of |h| on the compact disc is attained at an interior point
    because the boundary values are smaller than |h(0)|. The case a_0 = 0 is disposed of before h(0)
    is used. Not checked: the printed question, since the collection carries no provenance file.
---

::: {.problem}
Prove the fundamental theorem of algebra using

(a) Rouché's theorem;

(b) the maximum modulus principle.
:::

::: {.solution}
This is the fundamental theorem of algebra asked twice, once by Rouché's theorem and once by the maximum modulus principle, in the collection `SRC-CA-ART-T34TG3`, whose `provenance` is empty, so no source sheet was available and the printed question was not re-read; the argument below is the card's own.

::: pf

::: {.pf-step #bound}
With $f(z)=a_{n}z^{n}$ and $g(z)=a_{n-1}z^{n-1}+\cdots+a_{0}$, there is $R>0$ with $\abs{g(z)}<\abs{f(z)}$ for every $z$ with $\abs{z}=R$.

::: pf-proof
On $\abs{z}=R$ one has $\abs{f(z)}=\abs{a_{n}}R^{n}$ and $\abs{g(z)}\leq\abs{a_{n-1}}R^{n-1}+\cdots+\abs{a_{0}}$, so
$$\frac{\abs{g(z)}}{\abs{f(z)}}\leq\frac{\abs{a_{n-1}}}{\abs{a_{n}}R}+\cdots+\frac{\abs{a_{0}}}{\abs{a_{n}}R^{n}},$$
a finite sum of terms tending to $0$ as $R\to\infty$, with $a_{n}\neq0$. Choose $R$ large enough that this bound is below $1$.
:::
:::

::: {.pf-step #rouche}
(a) $P$ has exactly $n$ zeros, counted with multiplicity, in $D(0,R)$, hence at least one zero in $\CC$.

::: pf-proof
$f$ and $g$ are polynomials, hence holomorphic on a neighbourhood of the closed disc $\overline{D(0,R)}$, and $\abs{g}<\abs{f}$ on its boundary circle by step [](#bound){.pf-ref}. Rouché's theorem then gives that $f+g=P$ and $f$ have the same number of zeros, counted with multiplicity, in $D(0,R)$. The function $f(z)=a_{n}z^{n}$ has the single zero $0$ there, of multiplicity $n$, so $P$ has exactly $n$ zeros in the disc; and $n\geq1$ because $P$ is nonconstant, so at least one complex root exists.
:::
:::

::: {.pf-step #growth}
If $P$ has no zeros, then $h=1/P$ is entire and, for $R$ as in step [](#bound){.pf-ref}, $\abs{P(z)}\geq\abs{a_{n}}R^{n}/2$ on $\abs{z}=R$; hence $\abs{P(z)}\to\infty$ and $\abs{h(z)}\to0$ as $\abs{z}\to\infty$.

::: pf-proof
$P$ is entire and nowhere zero by assumption, so $1/P$ is entire. On $\abs{z}=R$,
$$\abs{P(z)}=\abs{a_{n}}R^{n}\abs{1+\frac{a_{n-1}}{a_{n}z}+\cdots+\frac{a_{0}}{a_{n}z^{n}}}\geq\abs{a_{n}}R^{n}\left(1-\frac{\abs{g(z)}}{\abs{f(z)}}\right)\geq\frac{\abs{a_{n}}R^{n}}{2},$$
using the triangle inequality and step [](#bound){.pf-ref}. The same computation with $R$ tending to infinity shows $\abs{P(z)}\geq\frac{\abs{a_{n}}}{2}\abs{z}^{n}$ for all large $\abs{z}$, so $\abs{P}\to\infty$ and $\abs{h}\to0$ at infinity.
:::
:::

::: {.pf-step #maxpoint}
If $P$ has no zeros then $\abs{h}$ attains a global maximum on $\CC$ at a point of the open disc $D(0,R)$.

::: pf-proof
If $a_{0}=0$ then $P(0)=0$ and there is nothing to prove, so assume $a_{0}\neq0$; then $h(0)=1/a_{0}\neq0$. Since $\abs{h(z)}\to0$ at infinity there is $R'>0$ with $\abs{h(z)}<\abs{h(0)}$ for $\abs{z}\geq R'$. The continuous function $\abs{h}$ attains a maximum on the compact disc $\overline{D(0,R')}$, say at $z_{0}$; then $\abs{h(z_{0})}\geq\abs{h(0)}>\abs{h(z)}$ for every $z$ outside the disc, so $z_{0}$ is a global maximum, and $z_{0}$ lies in the open disc $D(0,R')$ because on the boundary circle $\abs{h}<\abs{h(0)}\leq\abs{h(z_{0})}$.
:::
:::

::: {.pf-step #maximum}
(b) $P$ has a zero in $\CC$.

::: pf-proof
Suppose not. Then $h=1/P$ is entire by step [](#growth){.pf-ref}, and by step [](#maxpoint){.pf-ref} the modulus $\abs{h}$ attains a global maximum at an interior point $z_{0}$. The maximum modulus principle for a holomorphic function attaining its maximum modulus at an interior point makes $h$ constant; then $P=1/h$ is constant, contradicting $\deg P=n\geq1$. So $P$ has at least one zero.
:::
:::
:::

:::
