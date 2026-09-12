---
schema: qual/card@1
id: P-JHUFA02CAG
kind: problem
title: Holomorphic and smooth equivalence of an annulus with a punctured disk
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Annuli
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both parts, the annulus radii, punctured-disk target and inverse-map hint with Fall 2002 Complex Analysis problem 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Extended the hypothetical inverse across the puncture and eliminated all possible limit moduli by maximum/minimum modulus arguments; then verified an explicit radial C-infinity bijection and inverse."
---

2. (a) (15 points) Show that there is no one-to-one holomorphic mapping of the open annulus $\{ z : 1 < | z | < 2 \}$ onto the punctured unit disc $\{ z : 0 < | z | < 1 \}$ . (HINT: consider the inverse mapping)

(b) (5 points) Give an example of a one-to-one $C ^ { \infty }$ mapping of the open annulus $\{ z : 1 < | z | < 2 \}$ onto the punctured unit disc $\{ z : 0 < | z | < 1 \}$


::: solution
<1>1. Part (a): a biholomorphism would give a bounded inverse on the punctured disk.
::: proof
Suppose, for contradiction, that
$$
f:A=\{1<|z|<2\}\longrightarrow D^*=\{0<|w|<1\}
$$
is one-to-one, holomorphic, and onto. Since a one-to-one holomorphic map has
nonzero derivative, its inverse
$$
g=f^{-1}:D^*\to A
$$
is holomorphic. It satisfies $1<|g(w)|<2$, so $g$ is bounded near the puncture.
The removable-singularity theorem extends it to a holomorphic map
$G:D\to\mathbb C$.

Continuity and the inequalities on $D^*$ give
$$
1\le |G(0)|\le2.
$$
If $1<|G(0)|<2$, then $G(0)\in A$. Since $f\circ g$ is the identity on $D^*$,
continuity of $f$ at $G(0)$ gives
$$
f(G(0))=\lim_{w\to0}f(g(w))=\lim_{w\to0}w=0,
$$
contradicting $f(A)\subset D^*$.

If $|G(0)|=2$, then $|G|\le2$ on $D$ and $G$ attains its maximum modulus at
the interior point $0$, so the maximum modulus principle makes $G$ constant,
contradicting that $g$ is the inverse of a bijection. If $|G(0)|=1$, then
$G$ is nowhere zero and $|1/G|\le1$ on $D$, with equality at $0$; the same
principle applied to $1/G$ again makes $G$ constant. All cases are impossible.
Thus no such holomorphic bijection exists.
:::

<1>2. Part (b): a radial rescaling is a smooth bijection.
::: proof
Define
$$
F(z)=\left(1-\frac1{|z|}\right)z,
\qquad 1<|z|<2.
$$
Writing $z=re^{i\theta}$ gives
$$
F(re^{i\theta})=(r-1)e^{i\theta}.
$$
Hence $0<|F(z)|<1$, and the map preserves the angular coordinate while sending
$r\in(1,2)$ bijectively to $r-1\in(0,1)$. Its inverse is
$$
F^{-1}(w)=\left(1+\frac1{|w|}\right)w,
\qquad 0<|w|<1.
$$
Both formulas are $C^\infty$ on their respective domains because the modulus
function is smooth away from zero. Thus $F$ is a one-to-one $C^\infty$ mapping
of the annulus onto the punctured unit disk, as required.
:::
:::
