---
schema: qual/card@1
id: P-JHUSP07ANC
kind: problem
title: "Iterates of a non-rotational disk map vanish at the fixed point"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the nonrotation assumption and iteration recurrence with Spring 2007 problem 3 in the retained source; restored the map arrow, explicit initial value and removed the trailing fragment."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked strictness for the removable quotient also at zero, a uniform contraction factor on the whole orbit disk and the zero initial-value case."
---

::: problem
Let $f:D\to D$ be holomorphic on the unit disk, with
$f(0)=0$, and suppose $f$ is not a rotation $z\mapsto e^{i\theta}z$.
For $w\in D$, set $w_0=w$ and $w_{n+1}=f(w_n)$.
Prove that $w_n\to0$.
:::

::: solution
<1>1. The quotient $f(z)/z$ is strictly bounded by one on each compact subdisk.

::: proof
Because $f(0)=0$, the quotient extends holomorphically
to $h$ on $D$, with $h(0)=f'(0)$. Schwarz's lemma and
continuity give $|h|\leq1$ on all of $D$ [@SS03].
If equality held at any point, the maximum modulus
principle would make $h$ a constant of modulus one,
so $f$ would be a rotation. Therefore $|h(z)|<1$
at every point. On $|z|\leq r<1$, continuity and
compactness give a maximum $M_r<1$.
:::

<1>2. The iterates decay geometrically to zero.

::: proof
If $w=0$, all iterates are zero. Otherwise let $r=|w|<1$
and choose $q=(1+M_r)/2$, so $0<q<1$. Schwarz's lemma
gives $|w_{n+1}|\leq|w_n|$, so the whole orbit stays in
$|z|\leq r$. On this disk step <1>1 implies
$$
|w_{n+1}|=|w_n|\,|h(w_n)|\leq q|w_n|.
$$
Induction yields $|w_n|\leq q^n|w|$ for all $n\geq0$.
Since $q^n\to0$, the required limit follows.
:::
:::
