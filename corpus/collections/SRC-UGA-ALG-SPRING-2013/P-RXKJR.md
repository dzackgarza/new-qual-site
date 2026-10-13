---
schema: qual/card@1
id: P-RXKJR
kind: problem
title: Jordan forms of a $5$-dimensional operator annihilated by $(x+1)^2$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Minimal and Characteristic Polynomials
  - Eigenvalues and Eigenvectors
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $T: V\to V$ be a linear map from a 5-dimensional $\CC\dash$vector space to itself and suppose $f(T) = 0$ where $f(x) = x^2 + 2x + 1$.

a. Show that there does not exist any nonzero vector $v\in V$ such that $Tv = v$, but there *does* exist a nonzero vector $w\in V$ such that $T^2 w= w$.

b. Give all of the possible Jordan canonical forms of $T$.
:::

::: {.solution}
Set $N=T+I$. Then $N^2=0$ and $T=-I+N$.

<1>1. There is no nonzero $v$ such that $Tv=v$.

::: {.proof}
If $Tv=v$, then $Nv=2v$. Consequently $0=N^2v=2Nv=4v$, forcing $v=0$ over $\mathbb C$.
:::

<1>2. There exists a nonzero $w$ such that $T^2w=w$.

::: {.proof}
Since $N^2=0$, the operator $N$ has nonzero kernel on the five-dimensional space $V$: if it were injective, $N^2=0$ would imply $V=0$. Choose $0\neq w\in\ker N$. Then $Tw=-w$ and $T^2w=w$.
:::

<1>3. All possible Jordan forms are
\[
\boxed{[-1]^{\oplus5},\quad J_2(-1)\oplus[-1]^{\oplus3},\quad J_2(-1)^{\oplus2}\oplus[-1]}.
\]

::: {.proof}
The relation $(T+I)^2=0$ forces the sole eigenvalue to be $-1$ and all Jordan blocks to have size at most two. The partitions of five into parts of size at most two are $1+1+1+1+1$, $2+1+1+1$, and $2+2+1$, which give precisely these forms. Conversely, the square of $T+I$ vanishes on every listed block, so all three forms occur.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 prove part (a), and step <1>3 proves part (b).
:::
:::
