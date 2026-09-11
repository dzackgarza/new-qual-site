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
On $X = \Spec A$ with $Z \subseteq X$ closed and $j: U = X \setminus Z \injects X$ open, the sheaf $j_!\OO_U$ extended by zero is an $\OO_X$-module that is not quasicoherent: its sections are not a localization at any point of $Z$.
The constant sheaf $\ul{\ZZ}$ on a positive-dimensional $X$ is another, for the same reason — restriction maps do not localize.
:::

::: {.example title="Quasicoherent, not coherent"}
$\OO_{\AA^1}$ pushed to a point: $f: \AA^1_k \to \Spec k$ has $f_*\OO_{\AA^1} = \widetilde{k[t]}$, quasicoherent but not finitely generated over $k$.
On any integral $X$, the constant sheaf of rational functions $\mck_X$ with $U \mapsto K(X)$ is quasicoherent and not coherent.
:::

::: {.example title="Coherent, not locally free"}
On $X = \Spec k[t]$, the skyscraper $\widetilde{k[t]/(t)}$ at the origin is coherent, with fibre dimension $1$ at the origin and $0$ elsewhere.
Any torsion module gives such an example, and the non-constant fibre dimension is exactly the obstruction.
On a singular curve the maximal ideal sheaf at the singular point is coherent, torsion-free, and still not locally free.
:::

::: {.remark}
The three separations are the fastest way to show the hierarchy is strict, and they are all the examiner wants.
Read them as: quasicoherence fails when the sheaf ignores localization, coherence fails when a fibre is infinite-dimensional or the base is non-Noetherian, local freeness fails when the fibre dimension jumps.
The last criterion is the one to state as a test: over a reduced Noetherian scheme, a coherent sheaf is locally free exactly when $x \mapsto \dim_{\kappa(x)} \mcf \tensor \kappa(x)$ is locally constant.
:::
