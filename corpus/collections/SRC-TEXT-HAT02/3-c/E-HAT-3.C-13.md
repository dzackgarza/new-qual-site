---
schema: qual/card@1
id: E-HAT-3.C-13
kind: problem
title: Self-duality of Hopf algebras
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
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 13; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Both computations read and checked. The dual-basis bookkeeping and the two coproducts are
    right, as is the divided-power formula $\beta_i\beta_j=\binom{i+j}{i}\beta_{i+j}$ and the
    conclusion that the dual basis rescales to a polynomial generator, $\beta_k=\beta_1^k/k!$ with
    $k!$ invertible in $\FF_p$ for $k<p$. Repaired: the degrees of $\alpha$ were never stated, and
    they are essential. In the exterior case $|\alpha|$ must be odd, since for even $|\alpha|$ the two
    middle terms of $\Delta(\alpha)^2$ add instead of cancelling and $\Delta$ is not an algebra map
    although $\alpha^2=0$; in the truncated polynomial case $|\alpha|$ must be even, since otherwise
    the binomial expansion of $\Delta(\alpha^k)$ needs Koszul signs. Both points are now in the
    solution. Also repaired: "$\beta_1^p=p!\beta_p=0$" named a basis element that does not exist,
    and now reads $\beta_1^p=(p-1)!\,\beta_1\beta_{p-1}=(p-1)!\,p\,\beta_p=0$. No statement changed.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 13 of §3.C, printed p. 292. Both self-dualities are correct and
    the two degree hypotheses are essential, as the card says: $\Delta(\alpha)^2$ has middle terms
    $2\,\alpha\otimes\alpha$ when $|\alpha|$ is even, so the exterior algebra is a Hopf algebra only
    in odd degree, and the binomial formula for $\Delta(\alpha^k)$ in the truncated polynomial
    algebra needs $|\alpha|$ even. Restructured: ten steps, of which eight had no proof child at
    all and two carried the whole computation, are now four steps with proofs, one per claim —
    the exterior case with both dual structures, the coproduct formula in the truncated case, the
    dual product with $\beta_i\beta_j=\binom{i+j}{i}\beta_{i+j}$ and $\beta_1^p=(p-1)!\,p\,\beta_p=0$,
    and the dual coproduct with $\beta_1$ primitive. The mathematics is unchanged. Not claimed:
    a published solution, and no certificate.
---

::: {.problem}
Verify that the Hopf algebras $\Lambda_R[\alpha]$ and $\ZZ_p[\alpha]/(\alpha^p)$ are self-dual.
:::

::: {.solution}
Both Hopf algebras are self-dual as graded Hopf algebras over their coefficient rings; the degrees of the generators matter in both cases and are stated where they are used. The exercise is Exercise 13 of §3.C, printed p.~292.

::: pf

::: {.pf-step #s1}

$\Lambda_R[\alpha]$ with $\alpha$ of odd degree is self-dual.

::: pf-proof

As an $R$-module the algebra has basis $\{1,\alpha\}$ with $\alpha^2=0$, and $\alpha$ primitive, $\Delta(\alpha)=\alpha\otimes1+1\otimes\alpha$. Oddness is required: were $\abs{\alpha}$ even, the two middle terms of
$$
\Delta(\alpha)^2=\alpha^2\otimes1+(\alpha\otimes1)(1\otimes\alpha)+(1\otimes\alpha)(\alpha\otimes1)+1\otimes\alpha^2
$$
would add to $2\,\alpha\otimes\alpha$ instead of cancelling, while $\Delta(\alpha^2)=\Delta(0)=0$, so $\Delta$ would not be an algebra map; in odd degree the Koszul rule cancels them. In the dual $A^*=\operatorname{Hom}_R(A,R)$ with dual basis $\{1^*,\alpha^*\}$, the product is dual to $\Delta$, so
$$
\langle\alpha^*\alpha^*,\alpha\rangle=\langle\alpha^*\otimes\alpha^*,\alpha\otimes1+1\otimes\alpha\rangle=0,
$$
and $A^*$ vanishes above degree $\abs{\alpha}$, so $(\alpha^*)^2=0$ as well; hence $A^*\cong\Lambda_R[\alpha^*]$ as an algebra. The coproduct of $A^*$ is dual to the multiplication, and $\langle\Delta^*(\alpha^*),x\otimes y\rangle=\langle\alpha^*,xy\rangle$ is $1$ exactly for $(x,y)=(1,\alpha)$ and $(\alpha,1)$, so $\alpha^*$ is primitive. The correspondence $\alpha\mapsto\alpha^*$ is therefore an isomorphism of graded Hopf algebras.

:::

:::

::: {.pf-step #s2}

For $A=\FF_p[\alpha]/(\alpha^p)$ with $\alpha$ of even degree, $\Delta(\alpha^k)=\sum_j\binom{k}{j}\alpha^j\otimes\alpha^{k-j}$.

::: pf-proof

$\alpha$ is primitive, so $\Delta(\alpha^k)=(\alpha\otimes1+1\otimes\alpha)^k$, and expanding gives the stated sum with no signs because $\abs{\alpha}$ is even: in odd degree each mixed term would carry the Koszul sign $(-1)^{\abs{\alpha}j(k-j)}$ and the formula would fail. The basis is $\{1,\alpha,\dots,\alpha^{p-1}\}$ with $\alpha^p=0$.

:::

:::

::: {.pf-step #s3}

The dual $A^*$ with basis $\beta_0,\dots,\beta_{p-1}$ dual to $1,\alpha,\dots,\alpha^{p-1}$ satisfies $\beta_i\beta_j=\binom{i+j}{i}\beta_{i+j}$ for $i+j<p$ and $\beta_i\beta_j=0$ for $i+j\ge p$; hence $A^*\cong\FF_p[\beta_1]/(\beta_1^p)$.

::: pf-proof

$\langle\beta_i\beta_j,\alpha^k\rangle=\langle\beta_i\otimes\beta_j,\Delta(\alpha^k)\rangle=\binom{k}{i}\delta_{i+j,k}$, which gives the product formula and shows that $\beta_i\beta_j$ vanishes when $i+j\ge p$ because $\alpha^{i+j}=0$ in $A$. Inductively $\beta_1^k=k!\,\beta_k$, and $k!$ is a unit in $\FF_p$ for $k<p$, so $\beta_k=\beta_1^k/k!$ and $\beta_1$ generates $A^*$ as an algebra. At the edge, $\beta_1^p=(p-1)!\,\beta_1\beta_{p-1}=(p-1)!\,p\,\beta_p=0$, the last product already being zero in $A^*$ since $1+(p-1)=p$; so $A^*\cong\FF_p[\beta_1]/(\beta_1^p)$.

:::

:::

::: {.pf-step #s4}

$\beta_1$ is primitive and $\alpha\mapsto\beta_1$ is an isomorphism of graded Hopf algebras $A\to A^*$.

::: pf-proof

$\langle\Delta^*(\beta_1),\alpha^i\otimes\alpha^j\rangle=\langle\beta_1,\alpha^{i+j}\rangle$ is $1$ exactly when $i+j=1$, so $\Delta^*(\beta_1)=\beta_1\otimes1^*+1^*\otimes\beta_1$. The algebra isomorphism of the previous step sends the generator $\alpha$ to $\beta_1$ and preserves the coproduct because $\alpha$ and $\beta_1$ are both primitive and both generate, so the two Hopf algebras are isomorphic. Together with the exterior case, both Hopf algebras named in the exercise are self-dual.

:::

:::

:::
:::
