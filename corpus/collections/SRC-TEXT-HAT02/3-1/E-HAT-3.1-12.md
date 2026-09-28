---
schema: qual/card@1
id: E-HAT-3.1-12
kind: problem
title: Vanishing of $H^k(X,X^n;G)$ for $k\le n$
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Moved the statement into a problem block and summarized the second proof of Lemma 2.34(c) from Hatcher, Algebraic Topology, pp. 137-139.
- event: solution-written
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced a Milnor lim^1 argument with the telescope argument the problem requires.
---

::: {.problem}
The second proof in Hatcher of Lemma 2.34(c) for infinite-dimensional $X$ runs as follows.
From the long exact sequence of the pair $(X, X^n)$ it suffices to show $H_k(X, X^n) = 0$ for $k \leq n$; since $H_k(X, X^n) \approx \widetilde{H}_k(X/X^n)$, this reduces to showing that $\widetilde{H}_k(X) = 0$ for $k \leq n$ if the $n$-skeleton of $X$ is a point.
The finite-dimensional case follows from the long exact sequences of the pairs $(X^m, X^{m-1})$.
In general, let $T = \bigcup_i X^i \times [i, \infty) \subset X \times [0, \infty)$; then $X \times [0,\infty)$ deformation retracts onto $T$, so $T \simeq X$.
With $R = X^0 \times [0, \infty)$ and $Z = R \cup \bigcup_i X^i \times \{i\}$, the quotient $Z/R$ is a wedge sum of finite-dimensional complexes with $n$-skeleton a point and $T/Z$ is a wedge sum of finite-dimensional complexes with $(n+1)$-skeleton a point, and the long exact sequences of the pairs $(Z, R)$ and $(T, Z)$ give $\widetilde{H}_k(T) = 0$ for $k \leq n$.

Show $H^k(X, X^n; G) = 0$ if $X$ is a CW complex and $k \leq n$, by using the cohomology version of the second proof of the corresponding result for homology in Lemma 2.34.
:::

::: {.solution}
We follow the second proof of Lemma 2.34(c), replacing homology by cohomology.
Cohomology with coefficients in $G$ is suppressed from the notation.

<1>1. It suffices to show that $\widetilde H^k(Y)=0$ for $k\le n$ whenever $Y$ is a CW complex whose $n$-skeleton is a point.
::: {.proof}
$(X,X^n)$ is a good pair, so $H^k(X,X^n)\cong\widetilde H^k(X/X^n)$ [@Hat02, §3.1].
The quotient $X/X^n$ is a CW complex whose $n$-skeleton is a point.
:::

<1>2. The claim holds when $Y$ is finite-dimensional.
::: {.proof}
$H^k(Y^m,Y^{m-1})\cong\widetilde H^k(Y^m/Y^{m-1})$ vanishes for $k\ne m$, since $Y^m/Y^{m-1}$ is a wedge of $m$-spheres and the reduced cohomology of a wedge is the product of the reduced cohomologies of the summands [@Hat02, §3.1].
For $m>n$ and $k\le n$, the exact sequence
\[
H^k(Y^m,Y^{m-1})\to\widetilde H^k(Y^m)\to\widetilde H^k(Y^{m-1})
\]
has first term $0$, so restriction $\widetilde H^k(Y^m)\to\widetilde H^k(Y^{m-1})$ is injective.
Since $\widetilde H^k(Y^n)=0$ for all $k$, induction on $m$ gives $\widetilde H^k(Y^m)=0$ for all $m$ and $k\le n$, and $Y=Y^m$ for $m$ large.
:::

<1>3. $\widetilde H^k(Z)=0$ for $k\le n$.
::: {.proof}
$R=Y^0\times[0,\infty)$ is contractible because $Y^0$ is a point, so $\widetilde H^k(Z)\cong H^k(Z,R)\cong\widetilde H^k(Z/R)$ by the long exact sequence of the good pair $(Z,R)$.
The quotient $Z/R$ is a wedge of finite-dimensional complexes with $n$-skeleton a point, so its reduced cohomology in degrees $k\le n$ is a product of groups that vanish by <1>2.
:::

<1>4. $\widetilde H^k(T)=0$ for $k\le n$.
::: {.proof}
The quotient $T/Z$ is a wedge of finite-dimensional complexes with $(n+1)$-skeleton a point, so $H^k(T,Z)\cong\widetilde H^k(T/Z)=0$ for $k\le n+1$ by <1>2 applied with $n+1$.
In the exact sequence
\[
H^k(T,Z)\to\widetilde H^k(T)\to\widetilde H^k(Z)
\]
both outer terms vanish for $k\le n$, by this and <1>3.
:::

<1>5. $H^k(X,X^n;G)=0$ for $k\le n$.
::: {.proof}
Apply the construction to $Y=X/X^n$.
$T\simeq Y$, so $\widetilde H^k(Y)\cong\widetilde H^k(T)=0$ for $k\le n$ by <1>4 and homotopy invariance, and <1>1 concludes.
:::
:::
