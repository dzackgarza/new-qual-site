---
title: Free and projective modules
order: 20
topics:
- Free Modules
- Projective Modules
---

# Free and projective modules

## Free modules, rank, and torsion

An $R$-module is [[D-LIEMF|free]] if it has a basis, equivalently if it is isomorphic to $\bigoplus_{i\in I}R$ for some set $I$; over a commutative ring $R\neq0$ the cardinality of $I$ is its [[D-IGB7I|rank]].
Over an integral domain, a free module is [[D-ZJJ7G|torsion-free]]: if $r\neq0$ and $x=\sum_i c_ie_i\neq0$ in a basis $(e_i)$, then $rx=\sum_i rc_ie_i\neq0$.

[[D-LIEMF]]

[[D-IGB7I]]

[[FD-CVEAI]]

[[PR-DLPTR]]

[[D-ZJJ7G]]

[[FF-CY5EA]]

[[FD-BPUNZ]] [[FD-U6KUJ]]

[[FD-SK4ON]]

[[PR-4K4XZ]]

## Projective modules

An $R$-module is [[D-RHJMK|projective]] if and only if it is a direct summand of a free module.
Every free module is projective, and every short exact sequence $0\to A\to B\to P\to0$ with $P$ projective splits.
Over a PID, a finitely generated torsion-free module is free, so finitely generated projective and free modules coincide.

[[D-RHJMK]]

[[FD-6XJ7D]]

[[PR-RPL4Q]]

::: {.remark title="Free, projective, flat, torsion-free"}
For modules over an integral domain,
$$
\text{free} \implies \text{projective} \implies \text{flat} \implies \text{torsion-free},
$$
no implication reverses in general, and for finitely generated modules over a PID all four conditions coincide.
Examples separating them are on [[algebra/modules/classify-this-module|Classify this module]].
:::
