---
schema: qual/card@1
id: E-HAT-3.C-12
kind: problem
title: Pontryagin product in lens space homology
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 12; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 12; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read; the answer is right and so are the three relations. Repaired two places where the
    argument was named rather than given. First, primitivity of $\alpha$ is now derived from the
    absence of bidegrees $(i,j)$ with $i,j>0$ summing to $1$, and $\Delta(\beta)$ now records
    what about the Bockstein is used — naturality and additivity — and that $\beta$ is $\pm\beta_1(\alpha)$
    with the sign harmless; the previous line appealed to "naturality" alone, which does not
    produce the two terms by itself. Second, the dualization is now justified: $H_*$ is the dual of
    $H^*$ (finite type over the field $\ZZ_p$), the Pontryagin product is the transpose of the
    coproduct, and the note shows the paired computations for $x^2=0$ and $y_iy_j=\binom{i+j}{i}y_{i+j}$,
    with $xy_i=y_ix$ from graded commutativity in even degree $|y_i|=2i$. Also corrected a typo in
    the text ($H_{2n+1}(H;\ZZ_p)$) and added the remark that the displayed relations determine the
    multiplication. The boxed answer $\Lambda_{\ZZ_p}(x)\otimes\Gamma_{\ZZ_p}(y)$ is correct.
---

::: {.problem}
Compute the Pontryagin product structure in $H_*(L; \ZZ_p)$ where $L$ is an infinite-dimensional lens space $S^\infty / \ZZ_p$, for $p$ an odd prime, using the coproduct in $H^*(L; \ZZ_p)$.
:::

::: {.solution}

The computation is the card's own: the coproduct on the two algebra generators is determined by primitivity, and dualising gives the divided-power Pontryagin algebra. Coefficients are $\ZZ_{p}$ with $p$ an odd prime.

Let $L=S^{\infty}/\ZZ_{p}=K(\ZZ_{p},1)$.

::: pf

::: {.pf-step #cohomology}
$H^{*}(L;\ZZ_{p})\cong\Lambda(\alpha)\otimes\ZZ_{p}[\beta]$ with $\abs\alpha=1$, $\abs\beta=2$, and $\beta=\pm\beta_{1}(\alpha)$ for the Bockstein $\beta_{1}$ of $0\to\ZZ_{p}\to\ZZ_{p^{2}}\to\ZZ_{p}\to0$; the coproduct $\Delta$ comes from the H-space structure given by the group structure on $L$.

::: pf-proof
The lens space $S^{\infty}/\ZZ_{p}$ has the cohomology of $\CP^{\infty}$ truncated by an exterior generator in odd degrees: $H^{*}(L;\ZZ_{p})=\Lambda(\alpha)\otimes\ZZ_{p}[\beta]$ with $\abs\alpha=1$ and $\abs\beta=2$, and the Bockstein of $\alpha$ is a nonzero class in degree $2$, hence $\pm\beta$. As a $K(\ZZ_{p},1)$ it is an H-space with multiplication induced by the group structure of $\ZZ_{p}$ on the loop space of the delooping, and $\Delta$ is the map $H^{*}(L)\to H^{*}(L\times L)$ induced by that multiplication.
:::

:::

::: {.pf-step #alpha-primitive}
$\Delta(\alpha)=\alpha\otimes1+1\otimes\alpha$.

::: pf-proof
$\Delta$ is a ring homomorphism and $\Delta(\alpha)$ has degree $1$ with $\epsilon\otimes\epsilon$ term the augmentation, so $\Delta(\alpha)-\alpha\otimes1-1\otimes\alpha$ is a sum of terms of bidegree $(i,j)$ with $i,j>0$ and $i+j=1$. No such bidegree exists, so the difference vanishes.
:::

:::

::: {.pf-step #beta-primitive}
$\Delta(\beta)=\beta\otimes1+1\otimes\beta$.

::: pf-proof
The Bockstein $\beta_{1}$ is natural for maps of spaces, so $\Delta\big(\beta_{1}(\alpha)\big)=\beta_{1}\big(\Delta(\alpha)\big)$, and it is a derivation for the cross product: $\beta_{1}(x\otimes y)=\beta_{1}(x)\otimes y+(-1)^{\abs x}x\otimes\beta_{1}(y)$. Since $\beta_{1}(1)=0$ and $\beta=\pm\beta_{1}(\alpha)$,
$$
\Delta(\beta)=\pm\beta_{1}(\alpha\otimes1+1\otimes\alpha)=\pm\big(\beta_{1}(\alpha)\otimes1+1\otimes\beta_{1}(\alpha)\big)=\beta\otimes1+1\otimes\beta,
$$
the sign absorbed into the choice of $\beta$. So both algebra generators are primitive. What is used is additivity and naturality of $\beta_{1}$, not its derivation property for cup products.
:::

:::

::: {.pf-step #coproducts}
$\Delta(\beta^{n})=\sum_{i=0}^{n}\binom{n}{i}\beta^{i}\otimes\beta^{n-i}$ and $\Delta(\alpha\beta^{n})=\sum_{i=0}^{n}\binom{n}{i}\big(\alpha\beta^{i}\otimes\beta^{n-i}+\beta^{i}\otimes\alpha\beta^{n-i}\big)$.

::: pf-proof
$\Delta$ is a ring homomorphism and $\beta$ is even, so $\Delta(\beta^{n})=\Delta(\beta)^{n}$, which is the binomial expansion in the commutative ring $H^{*}(L\times L)$ with $(\beta\otimes1)(1\otimes\beta)=\beta\otimes\beta$. Multiplying by $\Delta(\alpha)=\alpha\otimes1+1\otimes\alpha$ and using that $\alpha$ is odd while $\beta^{i}$ is even, so that $(1\otimes\alpha)(\beta^{i}\otimes\beta^{n-i})$ carries no sign, gives the second formula.
:::

:::

::: {.pf-step #dual}
With $x\in H_{1}$ dual to $\alpha$ and $y_{n}\in H_{2n}$ dual to $\beta^{n}$, the Pontryagin products satisfy $x^{2}=0$, $y_{i}y_{j}=\binom{i+j}{i}y_{i+j}$ and $xy_{i}=y_{i}x$.

::: pf-proof
$H_{*}(L;\ZZ_{p})$ is the dual of $H^{*}(L;\ZZ_{p})$ because the cohomology has finite type in each degree and $\ZZ_{p}$ is a field, and the Pontryagin product is defined by $\langle uv,w\rangle=\langle u\otimes v,\Delta w\rangle$. The monomials $\alpha^{i}\beta^{j}$ form a basis, so it suffices to pair against them. For $x^{2}$, which lies in the one-dimensional space $H_{2}=\ZZ_{p}y_{1}$,
$$
\langle x^{2},\beta\rangle=\langle x\otimes x,\beta\otimes1+1\otimes\beta\rangle=\langle x,\beta\rangle\langle x,1\rangle+\langle x,1\rangle\langle x,\beta\rangle=0,
$$
so $x^{2}=0$. For the second relation,
$$
\langle y_{i}y_{j},\beta^{i+j}\rangle=\langle y_{i}\otimes y_{j},\Delta\beta^{i+j}\rangle=\binom{i+j}{i}\langle y_{i},\beta^{i}\rangle\langle y_{j},\beta^{j}\rangle=\binom{i+j}{i},
$$
and $\langle y_{i}y_{j},\alpha\beta^{i+j}\rangle=0$ because every term of $\Delta(\alpha\beta^{i+j})$ has one factor of the form $\alpha\beta^{m}$, which $y_{i}$ and $y_{j}$ annihilate. The third relation is graded commutativity: $xy_{i}=(-1)^{\abs x\abs{y_{i}}}y_{i}x=y_{i}x$ since $\abs{y_{i}}=2i$ is even.
:::

:::

::: {.pf-step #rest}
The same pairings with $\alpha\beta^{m}$ give $x\cdot xy_{i}=0$ and $xy_{i}\cdot y_{j}=\binom{i+j}{i}xy_{i+j}$, so the displayed relations determine the whole product.

::: pf-proof
Pair $x\cdot xy_{i}$ and $xy_{i}\cdot y_{j}$ against the basis: $\langle x\cdot xy_{i},\alpha\beta^{m}\rangle=\langle x\otimes xy_{i},\Delta(\alpha\beta^{m})\rangle$, and each term of the coproduct has one factor in odd degree, which is annihilated by $x$ (dual to $\alpha$) unless it is $\alpha$ itself, in which case the other factor carries an $\alpha$ that $xy_{i}$ annihilates; so the product vanishes. Similarly $\langle xy_{i}y_{j},\alpha\beta^{i+j+m}\rangle=\binom{i+j}{i}$ by the second relation applied to the $y$'s. Hence every product of basis elements is determined.
:::

:::

::: {.pf-step #answer}
$H_{*}(L;\ZZ_{p})\cong\Lambda_{\ZZ_{p}}(x)\otimes\Gamma_{\ZZ_{p}}(y)$, with $\abs x=1$, $y_{n}$ of degree $2n$ and the divided-power product $y_{i}y_{j}=\binom{i+j}{i}y_{i+j}$.

::: pf-proof
The dual basis $\{x^{\varepsilon}\beta^{n}\}$ of $H^{*}$ corresponds to $\{x^{\varepsilon}y_{n}\}$ in homology with $\varepsilon\in\{0,1\}$, giving the exterior factor $\Lambda(x)$ and the divided-power algebra $\Gamma(y)$ spanned by $y_{0}=1,y_{1},y_{2},\ldots$; steps [](#dual){.pf-ref} and [](#rest){.pf-ref} give exactly the relations of the tensor product with $x^{2}=0$ and $y_{i}y_{j}=\binom{i+j}{i}y_{i+j}$, and no others.
:::

:::

:::
:::
