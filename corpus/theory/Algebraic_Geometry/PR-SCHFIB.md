---
schema: qual/card@1
id: PR-SCHFIB
kind: example
title: Scheme-theoretic fibres retain multiplicity and residue fields
slogan: 'The fibre over $y$ is base change to $\Spec\kappa(y)$, retaining multiplicities and residue-field extensions that the set-theoretic fibre forgets.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fibre Products
  - Fibres
  - Residue Fields
relations:
- kind: uses
  target: D-MORFIB
review: draft
prompts:
- How does a scheme-theoretic fibre retain multiplicity and residue-field information that the set-theoretic preimage forgets?
- For $K = \QQ(\sqrt 3)$, describe the fibres of $\Spec \OO_K \to \Spec \ZZ$ over each prime, and which primes split, are inert or ramify.
---

::: {.example}
For the finite morphism
$$
\AA^1_k\longrightarrow\AA^1_k,
\qquad
t\longmapsto t^2,
$$
the fibre over the $k$-rational point $a$ is
$$
\Spec k[t]/(t^2-a).
$$
If $a\ne0$ and $\operatorname{char}k\ne2$, this is two reduced $k$-points when $a$ is a square in $k$, and one closed point with residue field $k(\sqrt a)$ when $a$ is not a square. The fibre over $0$ is
$$
\Spec k[t]/(t^2),
$$
a single nonreduced point of length $2$.
:::

::: {.example title="$\QQ(\sqrt3)$ over $\QQ$"}
Let $K=\QQ(\sqrt3)$. Since $\OO_K=\ZZ[\sqrt3]$, the fibre of
$$
\Spec\OO_K\longrightarrow\Spec\ZZ
$$
over the prime $(p)$ is
$$
\Spec\qty{\FF_p[x]/(x^2-3)}.
$$

- For $p=2$ or $p=3$, the polynomial has a double root, so $p$ ramifies and the fibre is one nonreduced point of length $2$.
- For odd $p\ne3$ with $p\equiv1,11\pmod{12}$, the element $3$ is a quadratic residue modulo $p$, so the polynomial has two distinct roots and $p$ splits.
- For odd $p\ne3$ with $p\equiv5,7\pmod{12}$, the polynomial is irreducible and $p$ is inert; the fibre is one reduced point with residue field $\FF_{p^2}$.
:::

::: {.remark}
These examples exhibit the information retained by the fibre scheme from [[D-MORFIB]]: nilpotents record ramification multiplicity, while residue fields record nonsplit points. In both examples the morphism is finite locally free of rank $2$, so every fibre has scheme-theoretic length $2$ even though the number of underlying points varies.
:::
