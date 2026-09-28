---
schema: qual/card@1
id: E-SMI-8000E-FEG
kind: problem
title: Proof choice — Galois correspondence or irreducibility of cyclotomic polynomials
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared both proof choices with Smith 8000 Fall 2006 final part G; solved option (i)."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "For an arbitrary intermediate field L, set H=Gal(E/L), used that E/L remains finite Galois, and compared |H| with the degree over the fixed field E^H to force E^H=L."
---

::: {.exercise}
Prove one:

(i) If $E$ is a finite Galois extension of $k$, the map from subgroups of $\operatorname{Gal}_k(E)$ to fields intermediate between $k$ and $E$, taking a subgroup to its fixed field, is surjective;

or

(ii) If $c_1, \ldots, c_r$ are the primitive $n$th roots of 1 contained in the complex field, then the "cyclotomic" polynomial

$$
f_n = \prod_{i=1}^{r} (X - c_i)
$$

lies in $\ZZ[X]$ and is irreducible over $\QQ$.
:::

::: {.solution}
We prove option (i).

<1>1. Fix an intermediate field and its pointwise stabilizer.
::: {.proof}
Let
$$
k\subseteq L\subseteq E
$$
be an intermediate field, and put
$$
H=\operatorname{Gal}(E/L)
=\{\sigma\in\operatorname{Gal}_k(E):\sigma|_L=\operatorname{id}_L\}.
$$
Let
$$
F=E^H
=\{x\in E:\sigma(x)=x\text{ for all }\sigma\in H\}
$$
be its fixed field. Since every element of $H$ fixes $L$ pointwise,
$$
L\subseteq F.
$$
:::

<1>2. The extension $E/L$ is finite Galois, so $|H|=[E:L]$.
::: {.proof}
The extension $E/L$ is finite because $E/k$ is finite. It is separable because
separability is preserved when the base field is enlarged inside $E$.

It is also normal: any $L$-embedding
$$
\tau:E\longrightarrow\overline{k}
$$
fixes $k$ as well, hence is a $k$-embedding. Since $E/k$ is normal,
$$
\tau(E)=E.
$$
Thus $E/L$ is finite Galois. Therefore its number of $L$-automorphisms equals
its degree:
$$
\boxed{|H|=[E:L].}
$$
:::

<1>3. Compare the degree over the fixed field with the size of $H$.
::: {.proof}
Because $L\subseteq F$, the tower law gives
$$
[E:F]\le [E:L].
$$

Every element of $H$ fixes $F$ by definition, so
$$
H\subseteq\operatorname{Aut}_F(E).
$$
For any finite field extension, the number of automorphisms over the base is
at most the degree. Hence
$$
|H|
\le |\operatorname{Aut}_F(E)|
\le [E:F].
$$
Combining this with step <1>2 gives
$$
[E:L]
=|H|
\le [E:F]
\le [E:L].
$$
All inequalities are therefore equalities, so
$$
[E:F]=[E:L].
$$
Since $L\subseteq F$, the tower law yields
$$
[F:L]=1,
$$
and hence
$$
F=L.
$$
:::

<1>4. Conclude surjectivity of the fixed-field map.
::: {.proof}
For the arbitrary intermediate field $L$, the subgroup
$$
H=\operatorname{Gal}(E/L)
$$
satisfies
$$
E^H=L.
$$
Thus every intermediate field occurs as the fixed field of a subgroup of
$\operatorname{Gal}_k(E)$. Therefore the map
$$
H\longmapsto E^H
$$
is surjective onto the intermediate fields.
:::
:::
