::: {.pf-step #s3a}

$H_{n+1}(X; \QQ) = 0$.

::: pf-proof

Theorem 3A.3 in degree $n+1$ applies to the free cellular chain complex of $X$ and, together with $\widetilde H_{n+1}(X) = 0$ and $\widetilde H_n(X) \cong A$, gives the exact sequence
$$
0 \longrightarrow H_{n+1}(X) \otimes \QQ \longrightarrow H_{n+1}(X; \QQ) \longrightarrow \operatorname{Tor}(H_n(X), \QQ) \longrightarrow 0,
$$
whose outer terms are $0 \otimes \QQ = 0$ and $\operatorname{Tor}(A, \QQ) = 0$, the latter because $\QQ$ is torsionfree (Proposition 3A.5(3)). Hence $H_{n+1}(X; \QQ) = 0$.

:::

:::

::: {.pf-step #s3b}

$H^{n+1}(X; \QQ) = 0$, and hence $\operatorname{Ext}(A, \QQ) = 0$.

::: pf-proof

Over the field $\QQ$, cohomology is the dual of homology, $H^{n+1}(X; \QQ) \cong \operatorname{Hom}_{\QQ}(H_{n+1}(X; \QQ), \QQ)$, since the $\operatorname{Ext}$ term of the universal coefficient theorem vanishes when the coefficient group is a field (§3.1, page 198); this group is zero by step [](#s3a){.pf-ref}. Then Theorem 3.2 in degree $n+1$, with $H_n(X) \cong A$ and $H_{n+1}(X) = 0$, gives the exact sequence
$$
0 \longrightarrow \operatorname{Ext}(A, \QQ) \longrightarrow H^{n+1}(X; \QQ) \longrightarrow \operatorname{Hom}(H_{n+1}(X), \QQ) \longrightarrow 0,
$$
so $\operatorname{Ext}(A, \QQ) = 0$.

:::

:::
