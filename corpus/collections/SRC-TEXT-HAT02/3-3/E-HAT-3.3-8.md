---
schema: qual/card@1
id: E-HAT-3.3-8
kind: problem
title: Degree as sum of local signs
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 8; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the local-degree computation: at a regular value the fundamental class goes to the tuple
    of local generators, each carrying the sign $\varepsilon_i$, so the degree is
    $\sum_i\varepsilon_i$.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Added the published corroboration: Steven V. Sam, Solutions to Algebraic Topology (2008),
    SS3.3 Exercise 8, printed pp.14-15, is the same diagram-of-local-homology argument. Sam's set is
    thin here (its SS3.3 covers only Exercises 8, 17 and 32) and the file carries a cover sheet, so
    printed pages, not PDF pages, are cited. Sam's proof is corroborative only: it is not used to
    replace any step, and the local-degree step is checked against Hatcher p.135.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Second published solution located for the same exercise: Math 538 homework solutions, HMW 4
    handwritten pp.1-2 (PDF pages 17-18), which runs the identical diagram and excision argument and
    reaches d = sum of the local signs. The card now cites both sets (Sam printed pp.14-15 and this
    sheet) with their page locators.

- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, transcribing the diagram argument of the cited published
    solution: Steven V. Sam, Solutions to Algebraic Topology (2008), §3.3 Exercise 8, printed
    pp. 14-15 (re-read in the retained text, tmp/sources/hatcher-solutions-sam-2008.md), and the
    same argument in Math 538 HMW 4, handwritten pp. 1-2. Checked against Hatcher, Section 3.3
    Exercise 8, printed p. 259, and the local degree discussion of p. 136. Each step re-read: the
    preimages of an interior point are interior points of the disjoint balls; excision splits the
    relative homology over the $B_i$; the image of $[M]$ is the tuple of local orientation classes;
    $f$ restricted to $B_i$ induces an isomorphism of local homology groups, and its sign is
    $+1$ exactly when the local orientations are preserved; and the same class computed through
    $H_n(N)$ is $\deg(f)\mu_y$. Not claimed: anything about the points of $B$ at which $f$ is not a
    local homeomorphism, or about the degree of a map not satisfying the hypothesis.
---

::: {.problem}
For a map $f: M \to N$ between connected closed orientable $n$-manifolds, suppose there is a ball $B \subset N$ such that $f^{-1}(B)$ is the disjoint union of balls $B_i$ each mapped homeomorphically by $f$ onto $B$.
Show the degree of $f$ is $\sum_i \varepsilon_i$ where $\varepsilon_i$ is $+1$ or $-1$ according to whether $f: B_i \to B$ preserves or reverses local orientations induced from given fundamental classes $[M]$ and $[N]$.
:::

::: {.solution}
The argument is transcribed from the published solution of Steven V. Sam, *Solutions to Algebraic Topology* (2008), §3.3 Exercise 8, printed pp. 14--15, which sets up the diagram of local homology groups used below; the same argument, with the same diagram, is in the Math 538 homework solutions, HMW 4, handwritten pp. 1--2 (PDF pp. 17--18 of `tmp/sources/hatcher-math538-homework4-solutions.pdf`). It is checked against Hatcher, Algebraic Topology, Section 3.3 Exercise 8, printed p. 259, and against the local degree discussion of p. 136.

::: pf

::: {.pf-step #points}
Choose $y\in\operatorname{int}B$. Then $f^{-1}(y)=\{x_1,\ldots,x_r\}$ with $x_i\in\operatorname{int}B_i$, and the $B_i$ are pairwise disjoint.

::: pf-proof
Each $B_i$ is mapped homeomorphically onto $B$, so each contains exactly one point over $y$, and that point lies in its interior because $y$ is an interior point of the target and the map is a homeomorphism. Distinct $B_i$ are disjoint by hypothesis, and $f^{-1}(B)=\bigsqcup_i B_i$ with $f$ mapping $B_i$ onto $B$ means there are no other points over $y$.
:::

:::

::: {.pf-step #excision}
There are identifications
$$
H_n(M,M\setminus f^{-1}(y))\cong\bigoplus_i H_n(B_i,B_i\setminus\{x_i\})\cong\bigoplus_i\ZZ,
\qquad
H_n(N,N\setminus\{y\})\cong\ZZ .
$$

::: pf-proof
The set $f^{-1}(y)$ lies in the disjoint union of the open sets $\operatorname{int}B_i$, so excision applies to each $B_i$ and, the $B_i$ being disjoint, the relative homology of $(M,M\setminus f^{-1}(y))$ splits as the direct sum over $i$ of $H_n(B_i,B_i\setminus\{x_i\})$. Each $B_i$ is an open $n$-ball and $x_i$ an interior point, so $H_n(B_i,B_i\setminus\{x_i\})\cong\ZZ$. The pair $(N,N\setminus\{y\})$ is a closed ball with an interior point removed, so $H_n(N,N\setminus\{y\})\cong\ZZ$ as well.
:::

:::

::: {.pf-step #fundamentalclass}
Under the identification of step [](#excision){.pf-ref}, the image of the fundamental class $[M]$ in $\bigoplus_i H_n(B_i,B_i\setminus\{x_i\})$ is the tuple of local orientation classes $(\mu_{x_1},\ldots,\mu_{x_r})$.

::: pf-proof
The map $H_n(M)\to H_n(M,M\setminus f^{-1}(y))$ followed by the projection $p_i$ to the $i$th summand is induced by the inclusion of pairs $(M,\varnothing)\to(M,M\setminus f^{-1}(y))$ and then by the map on relative homology induced by the inclusion $B_i\to M$; by naturality of the connecting maps it equals the map $H_n(M)\to H_n(M,M\setminus\{x_i\})$, which carries $[M]$ to the local orientation class $\mu_{x_i}$ at $x_i$ determined by $[M]$. So the image is the tuple of these classes.
:::

:::

::: {.pf-step #localdegree}
On the $i$th summand the map induced by $f$ is multiplication by $\varepsilon_i$.

::: pf-proof
$f$ carries the pair $(B_i,B_i\setminus\{x_i\})$ into $(N,N\setminus\{y\})$ and, restricted to $B_i$, is a homeomorphism onto $B$. Hence $f_*:H_n(B_i,B_i\setminus\{x_i\})\to H_n(N,N\setminus\{y\})$ is an isomorphism $\ZZ\to\ZZ$, that is multiplication by $+1$ or $-1$. By the definition of the local orientation classes, this sign is $+1$ exactly when $f$ carries $\mu_{x_i}$ to $\mu_y$, that is, when $f:B_i\to B$ preserves the local orientations induced from $[M]$ and $[N]$; so the multiplier is $\varepsilon_i$.
:::

:::

::: {.pf-step #computation}
The image of $[M]$ in $H_n(N,N\setminus\{y\})$ is $\left(\sum_i\varepsilon_i\right)\mu_y$.

::: pf-proof
$f$ induces a map of pairs $(M,M\setminus f^{-1}(y))\to(N,N\setminus\{y\})$, and the two ways of going from $H_n(M)$ to $H_n(N,N\setminus\{y\})$ — first to $H_n(M,M\setminus f^{-1}(y))$ and then by $f_*$, or first to $H_n(N)$ and then to $H_n(N,N\setminus\{y\})$ — agree, since both are induced by the same map of pairs and the relative map is natural. By step [](#fundamentalclass){.pf-ref} the class $[M]$ maps to the sum $\sum_i k_i(\mu_{x_i})$ over the summands, and step [](#localdegree){.pf-ref} gives $f_*k_i(\mu_{x_i})=\varepsilon_i\mu_y$; summing gives $\left(\sum_i\varepsilon_i\right)\mu_y$.
:::

:::

::: {.pf-step #degree}
The image thus computed is also $\deg(f)\mu_y$.

::: pf-proof
By definition of the degree, $f_*[M]=\deg(f)[N]\in H_n(N)\cong\ZZ$, and the map $H_n(N)\to H_n(N,N\setminus\{y\})$ carries $[N]$ to the local orientation class $\mu_y$ determined by $[N]$. So the image of $[M]$ is $\deg(f)\mu_y$.
:::

:::

::: {.pf-step}
$\deg(f)=\sum_i\varepsilon_i$, as claimed.

::: pf-proof
Steps [](#computation){.pf-ref} and [](#degree){.pf-ref} express the same class as $\left(\sum_i\varepsilon_i\right)\mu_y$ and as $\deg(f)\mu_y$; since $\mu_y$ is a generator of $H_n(N,N\setminus\{y\})\cong\ZZ$, the coefficients agree:
$$
\boxed{\deg(f)=\sum_i\varepsilon_i.}
$$
:::

:::

:::
:::
