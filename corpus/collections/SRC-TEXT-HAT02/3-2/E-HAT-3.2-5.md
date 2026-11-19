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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, and one attribution repaired: the earlier note recorded the
    cup-product step as coming from "the cellular diagonal used in the proof of Theorem 3.19",
    which is not what the book does. Hatcher's proof of Theorem 3.19 (printed p. 220) is the
    geometric argument through the relative groups H^i(P^n, P^n - P^j), and at the end of 3.2 he
    states that the diagonal is not a cellular map, so it induces no map of cellular cochains, and
    that a cellular approximation involves a choice. The card now carries that approximation
    explicitly, Delta_*(e_q) = sum over i+j=q of e_i (x) e_j, with the chain-map verification done
    in the proof (the even case collecting both families into 2 sum e_p (x) e_r, the odd case
    cancelling them), and records that agreement of the induced product with the topological cup
    product is taken as the standard input. The relation alpha^2 = k beta is then derived a second
    time from Example 3.9 with m = 2k, through the degree-k comparison map RP^2 -> S^1 U_{2k} e^2,
    which uses only printed results; the two derivations agree, which is the check that the
    standard input is being applied correctly. Rechecked throughout: delta^q = 2 for q odd and 0
    for q even, H^0 = R, H^odd = ker 2 = {0,k}, H^even>0 = R/2R, 2 alpha = 2 beta = 0, k^2 = k mod 2
    so alpha^2 = k beta, and phi_{2j}, k phi_{2j+1} are nonzero cocycles not coboundaries. The
    statement and the printed hint, including the coefficient map Z_2k -> Z_2, are unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Notation repair after the corpus check reported raw TeX the page cannot show. Two
    sentences refer to the section of the book as `\S3.2`, a section sign written as a TeX
    command outside a math span, which the HTML writer drops; both now read the character
    `§3.2`, as the corpus does elsewhere. Mathematics and wording unchanged.
---

::: {.problem}
Show the ring $H^*(\RP^\infty; \ZZ_{2k})$ is isomorphic to $\ZZ_{2k}[\alpha, \beta] / (2\alpha, 2\beta, \alpha^2 - k\beta)$ where $\gradeddegree{\alpha} = 1$ and $\gradeddegree{\beta} = 2$.
[Use the coefficient map $\ZZ_{2k} \to \ZZ_2$ and the proof of Theorem 3.19.]
:::

::: {.solution}
Put $R=\ZZ_{2k}$. The additive structure comes from the cellular cochain complex of the standard CW structure on $\RP^\infty$, which has one cell in each dimension; the product comes from a cellular approximation of the diagonal, which is needed because the diagonal is not itself cellular -- Hatcher says as much at the end of §3.2 and warns that such an approximation involves a choice, so the card's earlier attribution of this computation to the proof of Theorem 3.19, which is the geometric argument of printed p.~220, was wrong and is replaced here. The relation $\alpha\smile\alpha=k\beta$ is then re-derived a second way, from Example 3.9, and the two derivations agree.

::: pf

::: {.pf-step #cells}
The cellular chain complex of $\RP^\infty$ with coefficients in $R$ is $C_q=R\cdot e_q$ with $\partial e_q=2e_{q-1}$ for $q$ even and $\partial e_q=0$ for $q$ odd; hence the cochain complex is $C^q=\operatorname{Hom}(C_q,R)=R\cdot\varphi_q$ with $\delta^q\varphi_q=2\varphi_{q+1}$ for $q$ odd and $\delta^q\varphi_q=0$ for $q$ even.

::: pf-proof
The standard cell structure of $\RP^\infty$ has one $q$-cell $e_q$ for each $q\ge0$, with $q$-skeleton $\RP^q$, and the attaching map of $e_q$ is the two-fold covering $S^{q-1}\to\RP^{q-1}$, which has degree $2$ for $q$ even and degree $0$ for $q$ odd, by the degree of the antipodal map of $S^{q-1}$. A cellular cochain is determined by its values on cells, so $C^q$ is free of rank one on $\varphi_q$; and $\delta^q$ is the transpose of $\partial_{q+1}$, so $\delta^q\varphi_q$ evaluated on $e_{q+1}$ is $\varphi_q(\partial e_{q+1})$, which is $2$ for $q$ odd and $0$ for $q$ even, the parity of $q+1$ being opposite to that of $q$.
:::

:::


::: {.pf-step #cohomology}
$H^0(\RP^\infty;R)\cong R$; $H^q(\RP^\infty;R)\cong\ker(2:R\to R)=\{0,k\}\cong\ZZ_2$ for $q$ odd; and $H^q(\RP^\infty;R)\cong R/2R\cong\ZZ_2$ for $q>0$ even.

::: pf-proof
By step [](#cells){.pf-ref}, $H^q=\ker\delta^q/\operatorname{im}\delta^{q-1}$. For $q=0$ one has $\delta^0=0$ and no $\delta^{-1}$, so $H^0=R$. For $q$ odd, $\delta^q$ is multiplication by $2$ and $\delta^{q-1}=0$ because $q-1$ is even, so $H^q=\ker(2)=\{0,k\}\cong\ZZ_2$. For $q>0$ even, $\delta^q=0$ and $\delta^{q-1}$ is multiplication by $2$, so $H^q=R/2R\cong\ZZ_2$. In each case $\ker(2)=\{0,k\}$ and $R/2R\cong\ZZ_2$ because $R=\ZZ_{2k}$ with $k\ge1$.
:::

:::


::: {.pf-step #diagonal}
A cellular approximation of the diagonal is $\Delta_*(e_q)=\sum_{i+j=q}e_i\otimes e_j$; it is a chain map, and the product it induces on cellular cochains is $\varphi_i\smile\varphi_j=\varphi_{i+j}$.

::: pf-proof
The diagonal $\Delta\colon\RP^\infty\to\RP^\infty\times\RP^\infty$ is not cellular, so a chain approximation $\Delta_*\colon C_*\to C_*\otimes C_*$ has to be chosen, and the displayed formula is the standard choice. It is a chain map. With $\partial(x\otimes y)=\partial x\otimes y+(-1)^{\abs x}x\otimes\partial y$ and $\partial e_m=2e_{m-1}$ for $m$ even, $\partial e_m=0$ for $m$ odd,
$$
\partial\Delta_*(e_q)=\sum_{i+j=q}\bigl(\partial e_i\otimes e_j+(-1)^ie_i\otimes\partial e_j\bigr).
$$
For $q$ even, the terms with $i$ odd and the terms with $j$ odd vanish, so what remains is $2\sum_{i\ \mathrm{even}}e_{i-1}\otimes e_{q-i}+2\sum_{j\ \mathrm{even}}e_{q-j}\otimes e_{j-1}$; putting $p=i-1$ in the first sum and $r=j-1$ in the second, both run over the pairs $(p,r)$ with $p+r=q-1$ and exactly one entry odd, which is every pair since $q-1$ is odd, so the sum is $2\sum_{p+r=q-1}e_p\otimes e_r=\Delta_*(\partial e_q)$. For $q$ odd, the first family is $2e_{i-1}\otimes e_{q-i}$ over even $i$ and the second is $-2e_i\otimes e_{q-i-1}$ over odd $i$; substituting $i=p+1$ turns the second into $-2e_{p}\otimes e_{q-1-p}$ over even $p$, so the two families cancel and $\partial\Delta_*(e_q)=0=\Delta_*(\partial e_q)$, as $q$ odd gives $\partial e_q=0$.

Since $\Delta_*$ approximates the diagonal, the product it induces on cohomology is the cup product, so that $(\varphi\smile\psi)(e_q)=\sum_{i+j=q}\varphi(e_i)\psi(e_j)$, the terms being $\varphi(e_i)\psi(e_j)$ on the summand $e_i\otimes e_j$. For the basic cochains $\varphi_p$ and $\varphi_q$, every term vanishes except the one with $i=p$ and $j=q$, which is $1$; hence $\varphi_p\smile\varphi_q=\varphi_{p+q}$. What is used here and not derived is the agreement of this chain-level product with the topological cup product; the next step re-derives the one relation that the conclusion is most sensitive to, without it.
:::

:::


::: {.pf-step #classes}
Put $\alpha=[k\varphi_1]\in H^1$ and $\beta=[\varphi_2]\in H^2$. Then $2\alpha=2\beta=0$ and $\alpha,\beta\ne0$.

::: pf-proof
$k\varphi_1$ is a cocycle, since $\delta^1(k\varphi_1)=2k\varphi_2=0$ in $R=\ZZ_{2k}$, and $2\alpha=[2k\varphi_1]=0$. $\varphi_2$ is a cocycle, since $\delta^2=0$, and $2\beta=[2\varphi_2]=[\delta^1\varphi_1]=0$. Neither is a coboundary: $\operatorname{im}\delta^0=0$, so $\alpha\ne0$ as $k\ne0$ in $R$; and $\operatorname{im}\delta^1=2R\cdot\varphi_2$ does not contain $\varphi_2$ when $k\ge2$, while for $k=1$ one has $R=\ZZ_2$ and $\operatorname{im}\delta^1=0$. So $\beta\ne0$ in both cases.
:::

:::


::: {.pf-step #square}
$\alpha\smile\alpha=k\beta$.

::: pf-proof
By steps [](#diagonal){.pf-ref} and [](#classes){.pf-ref}, $\alpha\smile\alpha=[k\varphi_1]\smile[k\varphi_1]=[k^2(\varphi_1\smile\varphi_1)]=[k^2\varphi_2]=k^2\beta$. Since $2\beta=0$, an integer acts on $\beta$ through its residue modulo $2$, and $k^2\equiv k\pmod 2$; hence $k^2\beta=k\beta$.
:::

:::


::: {.pf-step #example39}
The same relation follows from Example 3.9 of §3.2, whose inputs are the printed ones.

::: pf-proof
Let $Y=S^1\cup_{2k}e^2$. In Example 3.9 Hatcher computes, for $X=S^1\cup_me^2$ with coefficients $\ZZ_m$ and $\alpha$ the generator of $H^1$, that $\alpha^2=k\beta$ when $m=2k$; so for $Y$ with coefficients $\ZZ_{2k}$ one has $\alpha_Y\smile\alpha_Y=k\beta_Y$ with $\beta_Y$ generating $H^2(Y;R)$. The degree-$k$ map $S^1\to S^1$ composed with the attaching map of $Y$, of degree $2k$, is the degree-$2k$ map $S^1\to S^1$, so it extends over the $2$-cell of $\RP^2=S^1\cup_2e^2$ and defines $f\colon\RP^2\to Y$. The map $f^*$ is a ring homomorphism; because $f$ is of degree $k$ on the $1$-cell it sends $\alpha_Y$ to $\alpha$, and because $f$ maps the $2$-cell homeomorphically it sends $\beta_Y$ to $\beta$. Finally $H^q(\RP^2;R)\to H^q(\RP^\infty;R)$ is an isomorphism for $q=1,2$ by cellular cohomology and step [](#cohomology){.pf-ref}. Hence $\alpha\smile\alpha=f^*(\alpha_Y\smile\alpha_Y)=k\,f^*(\beta_Y)=k\beta$, agreeing with step [](#square){.pf-ref}.
:::

:::


::: {.pf-step #generators}
$\beta^j=[\varphi_{2j}]$ and $\alpha\smile\beta^j=[k\varphi_{2j+1}]$ are nonzero for every $j\ge0$, and each generates $H^{2j}$ respectively $H^{2j+1}$.

::: pf-proof
By step [](#diagonal){.pf-ref}, $\beta^j=[\varphi_2]^j=[\varphi_{2j}]$ and $\alpha\smile\beta^j=[k\varphi_1\smile\varphi_{2j}]=[k\varphi_{2j+1}]$. Both are cocycles, since $\delta^{2j}\varphi_{2j}=0$ and $\delta^{2j+1}(k\varphi_{2j+1})=2k\varphi_{2j+2}=0$. They are not coboundaries: $\operatorname{im}\delta^{2j-1}=2R\cdot\varphi_{2j}$, which contains $\varphi_{2j}$ only when $1\in2R$, that is only when $2=0$ in $R$, i.e. $k=1$, and then $\operatorname{im}\delta^{2j-1}=0$; and $\operatorname{im}\delta^{2j}=0$, so no nonzero multiple of $\varphi_{2j+1}$ is a coboundary either. Their cohomology groups are $\ZZ_2$ by step [](#cohomology){.pf-ref}, so a nonzero element generates.
:::

:::


::: {.pf-step #relations}
The graded quotient $R[\alpha,\beta]/(2\alpha,2\beta,\alpha^2-k\beta)$ is $R$ in degree $0$ and $\ZZ_2$ in each positive degree.

::: pf-proof
Degree $0$ is $R$. For $j\ge0$ the degree $2j+2$ part is spanned by $\beta^{j+1}$ and $\alpha^2\beta^j$, the second identified with $k\beta^{j+1}$ by the relation $\alpha^2=k\beta$; the order-$2$ relations give $2\beta^{j+1}=0$ and $2k\beta^{j+1}=0$, so this part is $R\beta^{j+1}/2R\beta^{j+1}\cong\ZZ_2$, the element $k\beta^{j+1}$ being $\beta^{j+1}$ or $0$ within that $\ZZ_2$ according to the parity of some coefficient. The degree $2j+1$ part is spanned by $\alpha\beta^j$ subject to $2\alpha\beta^j=0$, hence is $\ZZ_2$. These are all the relations: the relations are homogeneous and generated by the three displayed, since the only rewrite a word in $\alpha,\beta$ admits is $\alpha^2\mapsto k\beta$, which lowers the $\alpha$-exponent by $2$ and raises the $\beta$-exponent by $1$, and any word is reduced by it to one of $\beta^j$ or $\alpha\beta^j$.
:::

:::


::: {.pf-step #conclusion}
$H^*(\RP^\infty;\ZZ_{2k})\cong\ZZ_{2k}[\alpha,\beta]/(2\alpha,2\beta,\alpha^2-k\beta)$ with $\gradeddegree\alpha=1$ and $\gradeddegree\beta=2$.

::: pf-proof
By steps [](#cohomology){.pf-ref} and [](#generators){.pf-ref} the classes $\beta^j$ and $\alpha\beta^j$ are nonzero generators of $H^{2j}$ and $H^{2j+1}$, so the ring homomorphism $\ZZ_{2k}[\alpha,\beta]\to H^*(\RP^\infty;R)$ carrying the indeterminates to $\alpha$ and $\beta$ is surjective, and it kills the three displayed relations by steps [](#classes){.pf-ref} and [](#square){.pf-ref}; hence it factors through the quotient. Both sides are $R$ in degree $0$ and $\ZZ_2$ in every positive degree, by steps [](#cohomology){.pf-ref} and [](#relations){.pf-ref}, and a surjective map that is an isomorphism of finite groups in each degree is an isomorphism of graded rings.
:::

:::

:::
:::
