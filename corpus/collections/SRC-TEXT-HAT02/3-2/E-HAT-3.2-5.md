---
schema: qual/card@1
id: E-HAT-3.2-5
kind: problem
title: Cohomology ring $H^*(\RP^\infty;\ZZ_{2k})$
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher's corrected Section 3.2 Exercise 5; the stored statement matches the 2004 correction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 5. The printed bracketed hint "[Use the coefficient map $\ZZ_{2k} \to \ZZ_2$ and the proof of Theorem 3.19.]" was missing and is restored.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the whole computation: the alternating cellular differential gives $R$ in degree $0$,
    $\ker(2)=\{0,k\}$ in odd degrees and $R/2R$ in positive even degrees; $\alpha$ is the class of
    $k$ times the basic $1$-cochain and $\beta$ the class of the basic $2$-cochain, so
    $2\alpha=2\beta=0$ and $\alpha^2=k^2\beta=k\beta$ since $2\beta=0$ and $k^2\equiv k$ mod $2$;
    the products $\alpha\beta^j$ are the nonzero elements of $\ker 2$, so $\alpha$ and $\beta$
    generate with no further relations.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 5 (p.229) including the bracketed hint about the coefficient map and Theorem 3.19. Rechecked the cellular computation with R = Z_2k: delta^q = 2 for q odd and 0 for q even, so H^0 = R, H^odd = ker 2 = {0,k} = Z_2, H^even>0 = R/2R = Z_2, and alpha (the class of the 1-cocycle of value k) and beta (the 2-cocycle of value 1) satisfy alpha^2 = k^2 beta = k beta because beta has order 2, with 2alpha = 2beta = 0 and alpha beta^j = k times the (2j+1)-cell, nonzero even for k even. One defect repaired: the diagonal was cited to Theorem 3.12, which is the pre-2015 number (the table on p. xii of this reprinting lists old 3.12 as new 3.19); it now reads Theorem 3.19 p.220. Also noted that the coefficient reduction kills alpha, which is consistent with alpha^2 = k beta. Not covered: no independent derivation of the diagonal formula, which is taken from the proof of Theorem 3.19.
---

::: {.problem}
Show the ring $H^*(\RP^\infty; \ZZ_{2k})$ is isomorphic to $\ZZ_{2k}[\alpha, \beta] / (2\alpha, 2\beta, \alpha^2 - k\beta)$ where $\gradeddegree{\alpha} = 1$ and $\gradeddegree{\beta} = 2$.
[Use the coefficient map $\ZZ_{2k} \to \ZZ_2$ and the proof of Theorem 3.19.]
:::

::: {.solution}
Put $R=\ZZ_{2k}$. With the standard CW structure on $\RP^\infty$, there is one cell in each dimension and the cellular boundary is multiplication by $2$ in even dimensions and $0$ in odd dimensions. Hence the cellular cochain differential with coefficients in $R$ is
$$
\delta^q=
\begin{cases}
2,&q\text{ odd},\\
0,&q\text{ even}.
\end{cases}
$$
Therefore
$$
H^q(\RP^\infty;R)\cong
\begin{cases}
R,&q=0,\\
\ker(2:R\to R)=\{0,k\}\cong\ZZ_2,&q\text{ odd},\\
R/2R\cong\ZZ_2,&q>0\text{ even}.
\end{cases}
$$

Let $\alpha\in H^1$ be represented by the cellular $1$-cocycle taking the value $k$ on the unique $1$-cell, and let $\beta\in H^2$ be the class of the cellular $2$-cochain taking value $1$ on the unique $2$-cell. Then
$$
2\alpha=2\beta=0.
$$
The cellular diagonal used in the proof of Hatcher's Theorem 3.19 (p.220) shows that the cup product of the basic degree-one cellular cochain with itself represents the basic degree-two cochain. Since our degree-one cocycle has coefficient $k$, its square is represented by $k^2$ times the basic degree-two cochain. Thus
$$
\alpha^2=k^2\beta.
$$
But $\beta$ has additive order $2$, and $k^2\equiv k\pmod 2$, so
$$
\boxed{\alpha^2=k\beta.}
$$

Reduction of coefficients $R\to\ZZ_2$, which is a ring map, sends $\beta$ to the nonzero class in $H^2(\RP^\infty;\ZZ_2)$ and $\alpha$ to $0$ (the $1$-cocycle of value $k$ reduces to the zero cochain when $k$ is even); since $\beta^j$ is nonzero in $H^{2j}(\RP^\infty;\ZZ_2)=\ZZ_2$ by Theorem 3.19 (p.220), $\beta^j$ is nonzero in the $R$-cohomology for every $j\ge1$. The same cellular diagonal computes $\alpha\beta^j$ as the cochain taking value $k$ on the unique cell of degree $2j+1$; this is the nonzero element of $\ker(2:R\to R)$, also when $k$ is even. Hence $\alpha,\beta$ generate the whole ring and there are no further relations. Therefore
$$
\boxed{
H^*(\RP^\infty;\ZZ_{2k})
\cong
\ZZ_{2k}[\alpha,\beta]/(2\alpha,2\beta,\alpha^2-k\beta),
\quad \gradeddegree{\alpha}=1,\ \gradeddegree{\beta}=2.
}
$$
:::
