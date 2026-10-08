---
schema: qual/card@1
id: P-EPDRU
kind: problem
title: The torsion submodule of a finitely generated module over a PID splits as a
  direct summand
classification:
  areas:
  - algebra
  topics:
  - Torsion
  - Free Modules
  - Structure Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $M$ be a finitely generated module over a PID $R$.

a. $M_t$ be the set of torsion elements of $M$, and show that $M_t$ is a submodule of $M$.

b. Show that $M/M_t$ is torsion free.

c. Prove that $M \cong M_t \oplus F$ where $F$ is a free module.
:::

::: {.solution}
<1>1. The torsion elements $M_t=\{m\in M:\exists\,0\neq r\in R,\ rm=0\}$ form a submodule of $M$.

::: {.proof}
The zero element is torsion. If $rx=0$ and $sy=0$ for nonzero $r,s\in R$, then $rs\neq0$ because $R$ is a domain, and $(rs)(x-y)=0$. For $a\in R$, the equality $r(ax)=a(rx)=0$ shows that scalar multiples of torsion elements are torsion. Thus $M_t$ is an $R$-submodule.
:::

<1>2. The quotient $M/M_t$ is torsion-free.

::: {.proof}
Suppose $0\neq r\in R$ and $r(m+M_t)=0$. Then $rm\in M_t$, so some $0\neq s\in R$ satisfies $srm=0$. Since $sr\neq0$, the element $m$ belongs to $M_t$. Hence $m+M_t=0$, establishing torsion-freeness.
:::

<1>3. There is an isomorphism
\[
\boxed{M\cong M_t\oplus F}
\]
for a finite-rank free $R$-module $F$.

::: {.proof}
The quotient $M/M_t$ is finitely generated because $M$ is. By step <1>2 it is torsion-free, so the structure theorem for finitely generated modules over a PID makes it free. Choose a basis of $M/M_t$ and arbitrary lifts to $M$; these lifts define an $R$-linear section of the quotient map $\pi:M\to M/M_t$. Consequently the exact sequence $0\to M_t\to M\to M/M_t\to0$ splits. Taking $F=M/M_t$ gives the stated isomorphism.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1, <1>2, and <1>3 establish parts (a), (b), and (c), respectively.
:::
:::
