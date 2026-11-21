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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.1, Exercise 12; it matches the printed text. The card also states the proof of Lemma 2.34(c) that the exercise refers to; that is extra context, not a change to the exercise.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the copied structure of the second proof of Lemma 2.34(c): good-pair reduction to $X/X^n$;
    the finite-dimensional case from injectivity of $H^k(Y^m)\to H^k(Y^{m-1})$ for $m>n$; the two
    telescope steps, with $R=Y^0\times[0,\infty)$ contractible and $Z/R$, $T/Z$ wedges of
    finite-dimensional complexes whose $n$- and $(n+1)$-skeleta are points; and the conclusion
    applied to $Y=X/X^n$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 12 (p.205), whose extra paragraph restating Lemma 2.34's second proof matches Hatcher pp.137-139. The cohomological transcription rechecked step by step: good pair and Proposition 2.22 p.124 for the reduction to Y = X/X^n; vanishing of H^k(Y^m,Y^{m-1}) for k != m now derived from Theorem 3.5 p.203 applied to the wedge of m-spheres rather than cited vaguely, with the product (not sum) in degree m noted; the restriction maps injective by the sequence of the pair on p.200; steps for Z and T as in the book. Not covered: the book's own homology proof is not re-derived here, only its cohomological counterpart.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 12 of §3.1, printed p. 205, and against the second proof of
    Lemma 2.34(c) on printed pp. 137--139 which the exercise transcribes, with Proposition 2.22
    (printed p. 124), Theorem 3.5 (printed p. 203) and the sequence of a pair on printed p. 200.
    Repaired one step. The vanishing of $\widetilde H^k(Z)$ was derived from a claimed isomorphism
    $\widetilde H^k(Z)\cong H^k(Z,R)$ justified by $\widetilde H^k(R)=0$; that hypothesis gives only
    that $\widetilde H^k(Z)$ is a quotient of $H^k(Z,R)$, not an isomorphism. The step now draws
    the quotient conclusion, which is what the argument needs and what the vanishing of
    $H^k(Z,R)\cong\widetilde H^k(Z/R)$ supplies. The rest checks out: the reduction to
    $Y=X/X^n$, the finite-dimensional induction using $H^k(Y^m,Y^{m-1})=0$ for $0<k\ne m$ with the
    product in degree $m$, and the two telescope steps, where the middle group of a sequence with
    both neighbours zero is legitimately zero. Not claimed: the book's homology proof is not
    re-derived, and no certificate.
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

::: pf

::: {.pf-step #s1}

It suffices to show that $\widetilde H^k(Y)=0$ for $k\le n$ whenever $Y$ is a CW complex whose $n$-skeleton is a point.

::: pf-proof

$(X,X^n)$ is a CW pair and hence a good pair, so Proposition 2.22 in its cohomological form gives $H^k(X,X^n;G)\cong\widetilde H^k(X/X^n;G)$.
The quotient $X/X^n$ is a CW complex whose $n$-skeleton is a point.

:::

:::

::: {.pf-step #s2}

The claim holds when $Y$ is finite-dimensional.

::: pf-proof

$H^k(Y^m,Y^{m-1})\cong\widetilde H^k(Y^m/Y^{m-1})$ vanishes for $k\ne m$: the quotient is a wedge of $m$-spheres, so its cellular cochain complex has $G$ in degree $0$, one factor $G$ per sphere in degree $m$ and nothing else, and Theorem 3.5 gives $H^k=0$ for $0<k\ne m$ (and $\prod G$ for $k=m$).
For $m>n$ and $k\le n$, the exact sequence of the pair (Theorem 2.13)
$$
H^k(Y^m,Y^{m-1})\to\widetilde H^k(Y^m)\to\widetilde H^k(Y^{m-1})
$$
has first term $0$, so restriction $\widetilde H^k(Y^m)\to\widetilde H^k(Y^{m-1})$ is injective.
Since $\widetilde H^k(Y^n)=0$ for all $k$, induction on $m$ gives $\widetilde H^k(Y^m)=0$ for all $m$ and $k\le n$, and $Y=Y^m$ for $m$ large.

:::

:::

::: {.pf-step #s3}

$\widetilde H^k(Z)=0$ for $k\le n$.

::: pf-proof

$R=Y^0\times[0,\infty)$ is contractible because $Y^0$ is a point, so in the sequence of the pair (Theorem 2.13) the last term of $H^k(Z,R)\to\widetilde H^k(Z)\to\widetilde H^k(R)=0$ vanishes and $\widetilde H^k(Z)$ is a quotient of $H^k(Z,R)$. Proposition 2.22 gives $H^k(Z,R)\cong\widetilde H^k(Z/R)$, and the quotient $Z/R$ is a wedge of finite-dimensional complexes with $n$-skeleton a point, so its reduced cohomology in degrees $k\le n$ is a product of groups that vanish by step [](#s2){.pf-ref}. Hence $\widetilde H^k(Z)=0$.

:::

:::

::: {.pf-step #s4}

$\widetilde H^k(T)=0$ for $k\le n$.

::: pf-proof

The quotient $T/Z$ is a wedge of finite-dimensional complexes with $(n+1)$-skeleton a point, so $H^k(T,Z)\cong\widetilde H^k(T/Z)=0$ for $k\le n+1$ by step [](#s2){.pf-ref} applied with $n+1$.
In the exact sequence
$$
H^k(T,Z)\to\widetilde H^k(T)\to\widetilde H^k(Z)
$$
both outer terms vanish for $k\le n$, by this and step [](#s3){.pf-ref}.

:::

:::

::: pf-step

$H^k(X,X^n;G)=0$ for $k\le n$.

::: pf-proof

Apply the construction to $Y=X/X^n$.
$T\simeq Y$, so $\widetilde H^k(Y)\cong\widetilde H^k(T)=0$ for $k\le n$ by step [](#s4){.pf-ref} and homotopy invariance, and step [](#s1){.pf-ref} concludes.

:::

:::

:::

:::
