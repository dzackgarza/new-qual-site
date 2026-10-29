---
schema: qual/card@1
id: FE-MODZOO
kind: example
title: Separating quasicoherent, coherent, and locally free
classification:
  areas:
  - algebraic-geometry
  topics:
  - Quasicoherent Sheaves
  - Coherent Sheaves
  - Locally Free Sheaves
relations:
- kind: uses
  target: D-QNTZY
- kind: uses
  target: T-MODVB
review: draft
prompts:
- Give a sheaf of modules that is not quasicoherent.
- Give a quasicoherent sheaf that is not coherent.
- Give a coherent sheaf that is not locally free.
---

::: {.example title="Not quasicoherent"}
On $X = \AA^1_k = \Spec k[t]$ with $j\colon U = X \setminus \theset{0} \injects X$, the extension by zero $j_!\OO_U$ is an $\OO_X$-module that is not quasicoherent.
Its stalk at the origin is $0$, so a global section vanishes on a neighbourhood of the origin, hence on the dense open $U$, hence everywhere; thus $\Gamma(X, j_!\OO_U) = 0$.
But $\Gamma(U, j_!\OO_U) = k[t,t^{-1}] \neq 0 = \Gamma(X, j_!\OO_U)_t$, so the sections over the basic open $U = D(t)$ are not the localization of the global sections.
:::

::: {.example title="Quasicoherent, not coherent"}
$\OO_{\AA^1}$ pushed to a point: $f: \AA^1_k \to \Spec k$ has $f_*\OO_{\AA^1} = \widetilde{k[t]}$, quasicoherent but not finitely generated over $k$.
On any integral Noetherian $X$ of positive dimension, the constant sheaf of rational functions $\mck_X$ with $U \mapsto K(X)$ is quasicoherent and not coherent.
:::

::: {.example title="Coherent, not locally free"}
On $X = \Spec k[t]$, the skyscraper $\widetilde{k[t]/(t)}$ at the origin is coherent, with fibre dimension $1$ at the origin and $0$ elsewhere.
Any nonzero finitely generated torsion $k[t]$-module gives such an example, and the non-constant fibre dimension is exactly the obstruction.
On a singular curve the maximal ideal sheaf at the singular point is coherent, torsion-free, and still not locally free.
:::

::: {.remark}
The three examples show that each implication in the hierarchy is strict.
They separate the failure mechanisms: quasicoherence can fail through incompatibility with localization, coherence through failure of finite generation, and local freeness through varying fibre dimension.
Over a reduced Noetherian scheme, a coherent sheaf is locally free exactly when
$$
x
\longmapsto
\dim_{\kappa(x)}
\qty{
\mcf_x\tensor_{\OO_{X,x}}\kappa(x)
}
$$
is locally constant.
:::
