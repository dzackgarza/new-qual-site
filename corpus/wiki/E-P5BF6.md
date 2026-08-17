---
schema: qual/card@1
id: E-P5BF6
kind: exercise
title: "Notation: let $N$ or $N(R)$ be the set of nilpotents in $R$."
classification:
  areas:
  - algebra
  topics:
  - nilpotence
  - rings
  - polynomials
relations: []
review: draft
solved: false
---
:::{.exercise title="?"}
\envlist
Notation: let $N$ or $N(R)$ be the set of nilpotents in $R$.
Let $ZD$ or $ZD(R)$ be the set of zero divisors.
Let $U, U(R), R\units$ be the units of $R$.

- Show that every nilpotent is either zero or a zero divisor.
  - Solution: $a^m=0$ with $a\neq 0$ and $m>1$, then $x x^{m-1} = 0$, so $x^{m-1}$ is a nontrivial element annihilating $x$.
- Show that $R$ commutative and unital and $x$ nilpotent implies $1+x$ is a unit, and moreover $N + R\units = R\units$ (the sum of a nilpotent and unit is a unit).
  - Solution: expand $1/(1+x) = \sum_{k=0}^\infty (-x)^k = \sum_{k=0}^n (-x)^k \da f(x)$, so $(1+x)f(x) =1$.
  Now use that $RN = N$ since $x^n=0$ implies $(rx)^n = rxrx\cdots rx = r^n x^n = 0$.
  Taking $n + u\in N + R\units$, then $u+n = u\inv(1 + u\inv n) \in R\units R\units$ since $u\inv n\in N$ and $1+u\inv\in R\units$ by the first part.

- Show that $f(x) = \sum a_k x^k \in R[x]$ iff $f\in R[x]\units \iff a_0\in R\units, a_{k>1}\in N$.
  - Solution: use that if $a_k$ is nilpotent, $a_k x^k$ is nilpotent.
    Then $a_0$ a unit at $a_1 x$ nilpotent implies $a_0 + a_1 x$ is a unit, and inductively $f$ is a unit.
    If $f$ is a unit, take $fg=1$ with $f = \sum_{k=0}^na_k x^k$ and $g = \sum_{k=0}^m a_k x^k$.
    Write $fg(x) = \sum_{k=0}^{n+m} c_k x^k$ where $c_k = \sum_{j=0}^k a_j b_{k-j}$.
    Using $fg=1$, $c_{0} = a_0 b_0 = 1$ so $a_0, b_0$ are units, and proceed inductively by descending coefficients, checking that $a_n b_m$ is the $r=0$ case.

- Show that $f(x) \in N(R[x]) \iff a_k \in N(R)$ for all $k$.
  - Solution: $f$ nilpotent with $f(x) = \sum a_k x^k$ implies $f^m=0$, and check the leading term $a_n^m x^{nm}$.
    Induct down: $f, a_nx^n$ nilpotent implies $f - a_n x^n$ nilpotent.
    Conversely, if $a_i^{n_i} = 0$, use that $N(R) \normal R$ form an ideal.

- Show that $f\in ZD(R[x]) \iff f\neq 0$ and $rf(x) = 0$ for some $r\in R$.

:::
